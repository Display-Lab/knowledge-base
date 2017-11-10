# ISR Related Workflows
Copied from a brainstorming session on 2017-11-03.

## Definitions

- **wireframe**: 
- **intervention**:
- **situation**:
- **context**: An instance of a situation for a specific client and time.
- **client**: Individual or organization requesting feedback tailoring.
- **performance summary**: A plot of data with representation of the recipient's performance over time.


## Tasks
- Check that terms in an ISR are in FIO
- Add term to FIO (rough in)
- Refine Term in FIO
  -  Aristotilean definition
  -  BFO compliant placement
  -  Publication reference if applicable
  -  Example usage
- Read paper and summarize intervention or theory.
- Write intervention or theory as ISR.
- Write SWRL representation of ISR.
- Write RDF description of ISR.
- Run a test of an ISR using a reasoner.
- Write a test for an ISR which uses a reasoner.
- Identify intervention characteristics in a performance summary template.
- Create a wireframe that has given intervention charateristic.
- Generate a scenario given answer to survey questions and use case description.
- Define computable guidelines that map input data to situation characteric values of a context.
- Create input field annotations for the specific context of a client.
- Annotate the attributes and cardinality of a performance summary template.

## Workflows

- Generate an ISR from publication.
  1. Read paper and summarize intervention.
  1. Write intervention as ISR in natural language.
  1. Write SWRL representation of ISR.
  1. Write a test of the ISR.
  1. Run test of the ISR.

- Add terms from an ISR to FIO.
  1. Check that terms used in ISR are in FIO.
  1. Add term to FIO roughly.
  1. Refine Term in FIO
    1. Write aristotilean definition
    1. Place in ontology following BFO rules.
    1. Write publication reference if applicable.
    1. Write example usage

## Related Repositories
- FIO: Display Lab formal ontology for upper level classes.
  - The FIO Ontology: owl format.
  - Protege development support files.
- Knowledge Base: The application ontology.
  - ISR swirl rules: owl format.
  - ISR RDF descriptions: owl format.
  - Performance Summary Templates: R, Python, or JS scripts.



