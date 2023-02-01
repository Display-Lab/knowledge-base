# Precision Feedback Knowledge Base

The Precision Feedback Knowledge Base describes the influence of motivating information, such as performance comparisons, trends, achievement, and loss as the key information content of feedback interventions. These elements of motivating information are represented in models of factors affecting the success of feedback interventions. The models for feedback intervention success serve dual purposes of 1) explaining how we believe feedback interventions influence behavior (i.e. program theory), and 2) configuring a precision feedback system that uses the models to generate feedback emails. 

These models are a kind of causal pathway diagram (i.e. causal pathways) that links the motivating information in performance data with email text and visual displays that can be used to deliver the information. The models are implemented semantically in a computer-processable format using a linked-data approach (JSON-LD).

Each causal pathway in the knowledgebase is illustrated by a vignette that demonstrates how the pathway is used by a precision feedback system, together with the following inputs: a feedback recipient's performance data, feedback preferences, and a collection of email templates.
 
The knowledge base can be used by a precision feedback system to prioritize motivating feedback messages. For example, if a person (the feedback recipient) is performing below average but is improving, a precision feedback system could use information about the recipient's preferences to determine whether or not to deliver one of the following messages: "You are not a top performer", "Your performance is improving", "Your performance is approaching the goal", or "You may have an opportunity to improve."

This project is supported by a grant from the National Library of Medicine: "A knowledge-based message tailoring system" (1K01 LM012528-01). This work is not peer-reviewed.


## Causal pathways

The causal pathways are located under the /causal_pathways directory.
Each pathway is described in a corresponding vignette directory.


## Version
1.0.0




