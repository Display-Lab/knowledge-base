
import pytest
from rdflib import RDF, BNode, Graph, Literal, URIRef
from random_candidate_selector import RandomCandidateSelector
from rdflib.namespace import Namespace

SLOWMO = Namespace("http://example.com/slowmo#")

def test_select_candidate():
    graph = Graph()
    candidate1 = graph.resource(BNode("candidate1"))
    candidate2 = graph.resource(BNode("candidate2"))

    candidate1[SLOWMO.Score] = Literal(0.2)
    candidate2[SLOWMO.Score] = Literal(0.1)
    candidate1[URIRef("coachiness_score")] = Literal(1.00)
    candidate2[URIRef("coachiness_score")] = Literal(1.00)
    candidate1[SLOWMO.AcceptableBy] = Literal(True)
    candidate2[SLOWMO.AcceptableBy] = Literal(True)
    candidate1[RDF.type] = SLOWMO.Candidate
    candidate2[RDF.type] = SLOWMO.Candidate
    candidate1[SLOWMO.AcceptableBy] = Literal("Social Worse")
    candidate1[SLOWMO.AcceptableBy] = Literal("improving")

    # get graph that has candidates scored by esteemer
    selected_candidate = RandomCandidateSelector.select_candidate(graph)
    assert str(selected_candidate.identifier) in ["candidate1", "candidate2"]

    candidate3 = graph.resource(BNode("candidate3"))
    candidate3[SLOWMO.Score] = Literal(0.2)
    candidate3[SLOWMO.AcceptableBy] = Literal("Social Worse")
    selected_candidate = RandomCandidateSelector.select_candidate(graph)
    assert str(selected_candidate.identifier) in ["candidate1", "candidate2", "candidate3"]
    if str(selected_candidate.identifier) in ["candidate1", "candidate3"]:
        assert graph.resource(selected_candidate.identifier).value(SLOWMO.Score) == Literal(0.2)
    else:
        assert graph.resource(selected_candidate.identifier).value(SLOWMO.Score) == Literal(0.1)
        
def create_candidate(graph, uri, acceptable=True):
    """
    Helper to create a candidate node.
    """
    graph.add((uri, RDF.type, SLOWMO.Candidate))
    if acceptable:
        graph.add((uri, SLOWMO.AcceptableBy, Literal("Social Worse")))
    return uri

def test_select_candidate_returns_one_of_valid_candidates():
    graph = Graph()

    c1 = create_candidate(graph, BNode("candidate1"))
    c2 = create_candidate(graph, BNode("candidate2"))

    selected = RandomCandidateSelector.select_candidate(graph)

    assert selected.identifier in {c1, c2}
    
def test_select_candidate_sets_selected_flag():
    graph = Graph()

    c1 = create_candidate(graph, BNode("candidate1"))

    RandomCandidateSelector.select_candidate(graph)

    triples = list(graph.triples((c1, SLOWMO.Selected, None)))
    assert len(triples) == 1
    assert triples[0][2] == Literal(True)

def test_select_candidate_ignores_non_acceptable_candidates():
    graph = Graph()

    # Valid candidate
    c1 = create_candidate(graph, BNode("candidate1"), acceptable=True)

    # Invalid candidate (no AcceptableBy)
    create_candidate(graph, BNode("candidate2"), acceptable=False)

    selected = RandomCandidateSelector.select_candidate(graph)

    assert selected.identifier == c1


def test_select_candidate_only_marks_selected_one():
    graph = Graph()

    create_candidate(graph, BNode("candidate1"))
    create_candidate(graph, BNode("candidate2"))

    selected = RandomCandidateSelector.select_candidate(graph)

    # Only one should be marked as Selected=True
    selected_nodes = list(graph.subjects(SLOWMO.Selected, Literal(True)))
    assert len(selected_nodes) == 1
    assert selected_nodes[0] == selected.identifier


def test_select_candidate_raises_when_no_valid_candidates():
    graph = Graph()

    # Candidate without AcceptableBy → should be ignored
    create_candidate(graph, BNode("candidate1"), acceptable=False)

    with pytest.raises(IndexError):
        RandomCandidateSelector.select_candidate(graph)


def test_select_candidate_randomness(monkeypatch):
    """
    Ensures deterministic behavior by mocking random.choice
    """
    graph = Graph()

    c1 = create_candidate(graph, BNode("candidate1"))
    create_candidate(graph, BNode("candidate2"))

    def fake_choice(seq):
        return seq[0]

    monkeypatch.setattr("random.choice", fake_choice)

    selected = RandomCandidateSelector.select_candidate(graph)

    assert selected.identifier == c1
