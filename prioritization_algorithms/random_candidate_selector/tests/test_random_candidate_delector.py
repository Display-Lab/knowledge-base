
from rdflib import RDF, BNode, Graph, Literal, URIRef
from random_candidate_selector import RandomCandidateSelector

def test_select_candidate():
    graph = Graph()
    candidate1 = graph.resource(BNode("candidate1"))
    candidate2 = graph.resource(BNode("candidate2"))

    candidate1[URIRef("http://example.com/slowmo#Score")] = Literal(0.2)
    candidate2[URIRef("http://example.com/slowmo#Score")] = Literal(0.1)
    candidate1[URIRef("coachiness_score")] = Literal(1.00)
    candidate2[URIRef("coachiness_score")] = Literal(1.00)
    candidate1[URIRef("http://example.com/slowmo#AcceptableBy")] = Literal(True)
    candidate2[URIRef("http://example.com/slowmo#AcceptableBy")] = Literal(True)
    candidate1[RDF.type] = URIRef("http://example.com/slowmo#Candidate")
    candidate2[RDF.type] = URIRef("http://example.com/slowmo#Candidate")
    candidate1[URIRef("http://example.com/slowmo#AcceptableBy")] = Literal("Social Worse")
    candidate1[URIRef("http://example.com/slowmo#AcceptableBy")] = Literal("improving")

    # get graph that has candidates scored by esteemer
    selected_candidate = RandomCandidateSelector.select_candidate(graph)
    assert str(selected_candidate.identifier) in ["candidate1", "candidate2"]

    candidate3 = graph.resource(BNode("candidate3"))
    candidate3[URIRef("http://example.com/slowmo#Score")] = Literal(0.2)
    candidate3[URIRef("http://example.com/slowmo#AcceptableBy")] = Literal("Social Worse")
    selected_candidate = RandomCandidateSelector.select_candidate(graph)
    assert str(selected_candidate.identifier) in ["candidate1", "candidate2", "candidate3"]
    if str(selected_candidate.identifier) in ["candidate1", "candidate3"]:
        assert graph.resource(selected_candidate.identifier).value(URIRef("http://example.com/slowmo#Score")) == Literal(0.2)
    else:
        assert graph.resource(selected_candidate.identifier).value(URIRef("http://example.com/slowmo#Score")) == Literal(0.1)