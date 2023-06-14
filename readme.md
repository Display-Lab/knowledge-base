# Precision Feedback Knowledge Base

The Precision Feedback Knowledge Base is a collection of pathways through which feedback influences human behavior, with healthcare and clinical practice as the primary application domain. Each pathway specifies the influence of motivating information, such as performance comparisons, trends, achievement, and loss as the key information content of feedback interventions. The elements of motivating information are represented pragmatically as models of factors affecting the success of feedback interventions. These models for feedback intervention success serve dual purposes of 1) explaining how we believe feedback interventions influence behavior (i.e. program theory), and 2) configuring a precision feedback system that uses the models to generate feedback messages that can be delivered in emails, quality dashboards, feedback reports, or other digital interventions. 

Each pathway is represented in a causal pathway diagram that links the motivating information in performance data with message text and visual displays that can be used to deliver the information. The models are implemented semantically in a computer-processable format using a linked-data approach (JSON-LD), based on the Performance Summary Display Ontology and the Causal Pathway Ontology.

The knowledge base contains vignettes that illustrate how a pathway is used by a precision feedback system to deliver motivating information to one or more feedback recipients, based on their performance data, their preferences, and a collection of message templates that determine a minimal set of possible feedback interventions.
 
The knowledge base can be used by a precision feedback system to prioritize motivating feedback messages. For example, if a person (the feedback recipient) is performing below average but is improving, a precision feedback system could use information about the recipient's preferences to determine whether or not to prioritize and deliver one of the following messages: "You are not a top performer", "Your performance is improving", "Your performance is approaching the benchmark", or "You may have an opportunity to improve."

This project is supported by funding from the NIH National Library of Medicine awards: "A knowledge-based message tailoring system" (1K01 LM012528-01) and "A scalable service to improve health care quality through precision audit and feedback" (5R01LM013894-01).

## Causal pathways

The causal pathways are located under the /causal_pathways directory.
Each pathway is described in a corresponding vignette directory.

## Versioning *(WIP)*
The knowledge base contains files in a spectrum of developmental states, from robustly functional to pre-psuedocode. Specific version of the `main` knowledge base repo exists in tandem with a specified version of the software pipeline, which are dependent on one-another for proper functionality.

Versioning of the knowledge base may implement breaking changes; as such version pairings of the knowledge base and software pipeline which are compatible are documented below.

|Release Pair| Knowledgebase Version | Software Pipeline Version | 
|-|-|-|
| deprecated | 1.0.1 | *not yet published* |
| 6/14/23 | 1.1.0 | *not yet published* |

Future version of the knowledge base may be independent of the pipeline software version, and may be developed for standalone tools or other independent uses.

## Version
1.1.0




