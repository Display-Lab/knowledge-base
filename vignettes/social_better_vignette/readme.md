# Social Better Pathway Vignette

## Causal pathway 
The causal pathway "social better" describes the influence of feedback interventions that show the recipient that their performance is better than that of a social comparator, such as a top performer benchmark or peer average. An example message that uses the social better pathway is "You are a top performer."

### Preconditions
Preconditions are factors that are necessary for the success of the feedback intervention that uses the social better pathway. The social_better pathway has the following preconditions:

Information content preconditions:
1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
2. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104)

Candidate message preconditions:
1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
2. Positive performance gap set (http://purl.obolibrary.org/obo/psdo_0000117)


### Moderators
Moderators are factors that inhibit or promote the influence of the feedback intervention on the recipient. The social better causal pathway has the following moderators:
1. Habituation: How many times has the recipient previously received this message in the last year?
2. Regulatory fit: To what extent is this message aligned with characteristics of the behavior/task, context, and recipient personality, with regard to motivation to avoid negative outcomes / problem (prevention focus), or motivation to achieve positive outcomes / develop and learn (promotion focus)?
3. Gap size: How large is the gap between the recipient's performance level and that of the social comparator?

### Mechanisms of action
Mechanisms of action are the factors that the intervention operates through to influence the feedback recipient. The social better pathway has the following mechanisms of action:
1. Awareness (knowledge): The message may change the recipient's awareness of their high performance, relative to peers.
2. Subjective norms: The message may influence the precipient by creating or reinforcing their perception of their own top-performer status within their peer group.
3. Motivation: The message may energize the recipient to continue putting effort into performance for this measure, to maintain their status as a top performer.

### Outcomes
The outcome of the successful use of the social better pathway is clinical process performance improvement or sustainment.


## Vignette 

###Organizational Context
A healthcare quality improvement consortium called the Multicenter Perioperative Outcomes Group (MPOG) uses precision feedback to prioritize motivating performance information about the quality and outcomes of operative cases. One performance measure that MPOG assesses for operative cases regards the minimization of the use of climate-sensitive anesthetic gases: [SUS-04 : Fresh Gas Flow, less than or equal to 2L/min](https://spec.mpog.org/Spec/Public/63).

### Personas
Alice is an attending anesthesiologist at Midwest Medicine, a medical-school affiliated hospital. She is motivated to continue improving her practice and that of her team. She is an innovator who has lead the development of new techniques for [research area X] and who values setting new goals for her and her team to reach. Alice prefers to receive feedback that emphasizes improvement over time in line charts that clearly visualize trends and help her to anticipate where the changes her team has implemented are resulting in improvement.

Bob is a CRNA at Danville Health System, a community hospital. He cares deeply about the safety of his patients and the efficiency of his team to provide the best care for patients in his community. He is proud of his team's record of providing high-quality and exceptionally safe care, and the quality awards that his hospital has received in recognition of their exceptional work. Bob prefers to receive notifications about any potential quality issues or significant problems, such as adverse events, that may require special attention from him and his team. Bob prefers to receive these in a brief sentence that does not require him to look at a chart, but which helps him understand that there is some follow-up required to dig into the details of one or more operative cases.


## Performance data

Alice has a performance level of 97% for January 2023. 
Bob has a performance level of 94% for January 2023.


## Comparator
The peer benchmark at Midwest Medicine for January 2023 is 93%.
The peer benchmark at Danville Health System for January 2023 is 95%.

## Recipient annotations
This data set should result in the following annotations for Alice, but not for Bob, indicating the presence of information content about a social comparator and a positive performance gap:

1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
2. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104)

## Message templates
The top_performer_bar message template displays the message "You are top performer this month for the measure [performance measure name]. Your performance was X, above the peer benchmark of Y" with a bar chart showing the recipient's performance over the last 6 months. The message template is about a positive performance gap set and a social comparator element, and has the following metadata:
1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
2. Positive performance gap set (http://purl.obolibrary.org/obo/psdo_0000117)

The top_performer_text message template displays the message "You are top performer this month for the measure [performance measure name]" Your performance was X, above the peer benchmark of Y" with no other chart or visual display about performance. The message template is about a positive performance gap set and a social comparator element, and has the following metadata:
1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
2. Positive performance gap set (http://purl.obolibrary.org/obo/psdo_0000117)


## Candidate Messages
Two candidates are produced for Alice that have the following annotations:

1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
2. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
3. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104)
4. Positive performance gap set (http://purl.obolibrary.org/obo/psdo_0000117)

No candidate messages are produced for Bob.

## Evaluation result
The candidate is found to be acceptable by the causal pathway social_better.

