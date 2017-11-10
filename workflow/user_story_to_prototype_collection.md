# Workflow: User Story to Prototype Collection

## Givens:
- User Story
- Situation/Context Spec
- Performance Metric Spec
- Templates Library
- ISRs Application Ontology

## Definitions:
- **Wireframe**:
    Performance display template that is the representative of that class of performance displays.  Where the class of performance displays is defined by the performance display taxonomy of FIO.  They are identified by an annotation in their metadata.
- **Prototype**:
    A wireframe that uses labels from a user story and synthetic data that approximates a performance metric specification.
- **Information Needs**:
    Annotations added to user story used to select applicable performance display summary templates.  examples are:
    - Gap between recipient & standard
    - Change in performance over time

## Path:

1. Annotate User Story
    - Information Needs
    - Labels for Performance Summary
    - Relevant ISRs
1. Retrieve Applicable Wireframes from Templates Library
    - Meet information needs of user story
    - Support an ISR of user story
1. Generate Prototypes
    - Use labels from user story
    - Use synthetic data
1. Gategeekper Reduction of Prototypes
  Trimming down the number of prototypes to consider by stakeholder or domain expert.
1. CYCLE (per prototype):
    1. Prototype Useability Testing 
        - Using provided interview guide for prototypes
        - Eye tracking, galvanic response (optional)
        - Web interface survey
    1. Add discovered information to situation spec
        - Additional requirements or constraints
        - Unacceptable prototypes
    1. Refine Performance Metric
        - Client side
    1. Redesign Prototype
        - Different individual of same display taxa
        - Adjust parameters
        - Create new template in same display taxa
    1. CYCLE END CONDITION
        - No useability errors
        - Satisfactory comprehension
        - Satisfactory acceptance
1. Record Accepted Prototypes
    - Collection specific to story + situation + performance metric
1. Quality Check of Prototypes
    - No changes that break the implications of the user story annotations
    - Still represents ISRs
    - Member of original template taxa
1. Collection of Accepted Prototypes
