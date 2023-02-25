# Improving Causal Pathway Vignette

A healthcare quality improvement consortium called the Multicenter Perioperative Outcomes Group (MPOG) uses precision feedback to prioritize motivating performance information about the quality and outcomes of operative cases. A performance measure that MPOG assesses for operative cases regards the minimization of the use of climate-sensitive anesthetic gases: [SUS-04 : Fresh Gas Flow, less than or equal to 2L/min](https://spec.mpog.org/Spec/Public/63).

## Personas

Alice is an attending anesthesiologist at Midwest Medicine, a medical-school affiliated health system. She is motivated to continue improving her practice and that of her team. She is an innovator who has lead the development of new techniques for [research area X] and who values setting new goals for her and her team to reach. Alice prefers to receive feedback that emphasizes improvement over time in line charts that clearly visualize trends and help her to anticipate where the changes her team has implemented are resulting in improvement.

Bob is a CRNA at Danville Health System, a community hospital. He cares deeply about the safety of his patients and the efficiency of his team to provide the best care for patients in his community. He is proud of his team's record of providing high-quality and exceptionally safe care, and the quality awards that his hospital has received in recognition of their exceptional work. Bob prefers to receive notifications about any potential quality issues or significant problems, such as adverse events, that may require special attention from him and his team. Bob prefers to receive these in a brief sentence that does not require him to look at a chart, especially when there is some follow-up required to dig into the details of one or more operative cases.


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


