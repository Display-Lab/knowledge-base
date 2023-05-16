# Improving Causal Pathway Vignette

A healthcare quality improvement consortium called the Multicenter Perioperative Outcomes Group (MPOG) uses precision feedback to prioritize motivating performance information about the quality and outcomes of operative cases. A performance measure that MPOG assesses for operative cases regards the minimization of the use of climate-sensitive anesthetic gases: [SUS-04 : Fresh Gas Flow, less than or equal to 2L/min](https://spec.mpog.org/Spec/Public/63).

## Personas

Alice is an attending anesthesiologist at Midwest Medicine, a medical-school affiliated hospital. She is motivated to continue improving her practice and that of her team, and who values setting new goals for her and her team to reach. MPOG has not yet elicited preferences from Alice about precision feedback. An organizational preference profile for anesthesia providers at Midwest Medicine has been developed from a cluster analysis of a sample of providers who have taken an online preference survey, and these results are used for Alice and any other anesthesia provider who has not yet taken a preference survey. This profile prioritizes feedback messages about changes in performance involving the achievement of peer benchmarks, drops in performance below a peer average, and improvement towards the peer benchmark, as well as time-series visualization in bar charts and line charts. The Midwest Medicine Anesthesia Provider Preference Profile is a set of relative utilities for attributes of feedback messages that a precision feedback system uses to prioritize performance information and feedback display format.

Bob is a CRNA at Max Community Hospital. He cares deeply about the safety of his patients and the efficiency of his team to provide the best care for patients in his community. He is proud of his team's record of providing high-quality and exceptionally safe care, and the quality awards that his hospital has received in recognition of their exceptional work. Bob prefers to receive notifications about any potential quality issues or significant problems, such as adverse events, that may require special attention from him and his team. Bob prefers to receive these in a brief sentence that does not require him to look at a chart, but which helps him understand that there is some follow-up required to dig into the details of one or more operative cases. Bob took a feedback preference survey which generated a set of relative utilities for feedback message attributes that a precision feedback system can use.


## Performance data
Alice's performance rate for SUS-04 has level of 75% for November 2023, 74% for December 2023, and 77% for January 2023. Bob's performance is 72% for November 2023, 75% for December 2023, and 74% for January 2023. 

## Recipient annotations
This data set should result in an annotation that there is information content about a positive performance trend for Alice:
1. Positive performance trend content (http://purl.obolibrary.org/obo/psdo_0000099)

## Template annotations
The performance_improving template is about a positive performance trend set:
1. Positive performance trend set (http://purl.obolibrary.org/obo/psdo_0000120)

## Resulting candidates
The candidate produced for Alice has:
1. Positive performance trend content (http://purl.obolibrary.org/obo/psdo_0000099)
2. Positive performance trend set (http://purl.obolibrary.org/obo/psdo_0000120)

## Causal pathway preconditions
The improving causal pathway has preconditions:
1. Positive performance trend content (http://purl.obolibrary.org/obo/psdo_0000099)
2. Positive performance trend set (http://purl.obolibrary.org/obo/psdo_0000120)

## Evaluation result
The candidate is found to be acceptable by the causal pathway 'improving'.


