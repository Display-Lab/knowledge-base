# Precision Feedback Knowledge Base

The Precision Feedback Knowledge Base is comprised of four elements. The four elements are:

1. Causal Pathways

Each causal pathway specifies the influence of "motivating information", such as performance comparisons, on its recipients. They are called causal pathways because there is published scientific evidence to suggest that when "motivating information" is incorported into precision feedback interventions it can change recipient behaviors. In this case, "motivating information" is the combination of a recipient's past performance record and added contextual information to support comparisons. As an element of the knoweldge base, causal pathways serve the dual purposes of 1) explaining why feedback interventions influence behavior (i.e. program theory), and 2) configuring a precision feedback intervention to generate messages that can be delivered to recipients in emails, reports, or by other means. 

2. Templates

 Each template specifies an evidence-based text and display format for a performance feedback message corresponding to a causal pathway. (Note: A single causal pathway may have more than one template.) The contents of each template include links to concept definitions from relevant ontologies.

4. Measures

7. Vignettes
   
   (Main Ontologies Used)

   
a collection of pathways through which feedback influences human behavior, with healthcare and clinical practice as the primary application domains. 

Vignettes (Narrative)
Templates (CEDAR-JSON)
Measures (JSON)



Each pathway is represented in a causal pathway diagram that links the motivating information in performance data with message text and visual displays that can be used to deliver the information. The models are implemented semantically in a computer-processable format using a linked-data approach (JSON-LD), based on the Performance Summary Display Ontology and the Causal Pathway Ontology.

The knowledge base contains vignettes that illustrate how a pathway is used by a precision feedback system to deliver motivating information to one or more feedback recipients, based on their performance data, their preferences, and a collection of message templates that determine a minimal set of possible feedback interventions.
 
The knowledge base can be used by a precision feedback system to prioritize motivating feedback messages. For example, if a person (the feedback recipient) is performing below average but is improving, a precision feedback system could use information about the recipient's preferences to determine whether or not to prioritize and deliver one of the following messages: "You are not a top performer", "Your performance is improving", "Your performance is approaching the benchmark", or "You may have an opportunity to improve."

This project is supported by funding from the NIH National Library of Medicine awards: "A knowledge-based message tailoring system" (1K01 LM012528-01) and "A scalable service to improve health care quality through precision audit and feedback" (5R01LM013894-01).

## Causal pathways

The causal pathways are located under the /causal_pathways directory.
Each pathway is described in a corresponding vignette directory.

## Governance Policy
The knowledge base contains files on a spectrum of developmental states, from robustly functional to pre-pseudocode. Versioning of the knowledge base may implement breaking changes, and as such a registry of stable pairs are maintained by the Display-Lab team. Stable release pairs of the software pipeline and knowledgebase are recorded as new versions are released, to ensure full functionality of the pipeline despite the changing nature of the knowledgebase. Future versions of the knowledge base may be independent of the software pipeline's version, and may be developed for standalone uses.

|Release Pair| Knowledgebase Version | Software Pipeline Version | 
|-|-|-|
| deprecated | 1.0.1 | 1.2.2 |
| 6/14/23 | 1.1.0 | *todo* |

## Version
1.1.0




