# Social Better Vignette

## Introduction
Clinical performance feedback commonly includes peer comparison because it helps providers to understand how their care differs from the norm, and may motivate them to improve the care they provide to align with peers. Peer comparison feedback may also motivate providers to maintain a social status of being a high performer, once they have achieved it. The Social Better Causal Pathway specifies feedback messages that are capable of motivating providers through the delivery of information about high performance, relative to peers. This vignette serves the purpose of illustrating how a precision feedback system uses the Social Better Causal Pathway to motivate providers.

## Data

### Performance data
MPOG has received data for January 2023 about Alice and Bob's operative cases and that of their peers for analysis, to measure care quality and outcomes. MPOG analyses the data for each performance measure, and calculates the following performance information for the measure SUS-04:

### Individual healthcare professionals
Alice has a performance level of 97% for January 2023. 

Bob has a performance level of 94% for January 2023.

### Comparators
The top 25% peer benchmark at Midwest Medicine for January 2023 is 93%. The performance level for this comparator is calculated as the 75th percentile for all anesthesia providers at Midwest Medicine (http://purl.obolibrary.org/obo/psdo_0000128). 

The top 10% peer benchmark at Midwest Medicine for January 2023 is 96%. The performance level for this comparator is calculated as the 90th percentile for all anesthesia providers at Midwest Medicine (http://purl.obolibrary.org/obo/psdo_0000129).

The top 25% peer benchmark at Danville Hospital for January 2023 is 93%. The performance level for this comparator is calculated as the 75th percentile for all anesthesia providers at Midwest Medicine (http://purl.obolibrary.org/obo/psdo_0000128).

The top 10% peer benchmark at Danville Hospital for January 2023 is 95%. The performance level for this comparator is calculated as the 90th percentile for all anesthesia providers at Midwest Medicine (http://purl.obolibrary.org/obo/psdo_0000129).


### Preference data
Preferences for precision feedback are elicited through a preference survey that providers can take. The preference survey produces a preference model for each provider that, with the provider's permission, is shared with MPOG to maintain. MPOG analyses preferences data that is shared to identify population-level preference segments. These are generates as preference profiles that can serve as a default preference model for an organization, or which can be selected by providers who do not take the preference survey, but who identify preferences that are close enough to their own in the settings menu for the precision feedback system.

Alice's preference data: (TODO)
Bob's preference data: (TODO)

To generate precision feedback, MPOG sends de-identified performance and preference data to a precision feedback system that processes each provider's data with their peer comparator performance data, to select an optimal precision feedback message. 


# Precision feedback system
The precision feedback system is a knowledge-based system that is comprised of the following parts: 1) A knowledge base, 2) A software pipeline, and 3) A web service.

## Precision Feedback Knowledge Base
The knowledge base contains the following components: Causal pathways, message templates, and performance measures.

## Social Better Causal Pathway 
The causal pathway "social better" describes the influence of feedback interventions that show the recipient that their performance is better than that of a social comparator, such as a top performer benchmark or peer average. Example messages that uses the social better pathway are "You are a top performer" and "Your performance is better than average." The causal pathway model is made up of preconditions, moderators, mechanisms, and outcomes. 

### Preconditions
Preconditions are factors that are necessary for the success of the feedback intervention that uses the social better pathway. The social better pathway has the following preconditions:

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

### Mechanisms
Mechanisms the factors that the intervention operates through to influence the feedback recipient. The social better pathway has the following mechanisms of action:
1. Awareness (knowledge): The message may change the recipient's awareness of their high performance, relative to peers.
2. Subjective norms: The message may influence the precipient by creating or reinforcing their perception of their own top-performer status within their peer group.
3. Motivation: The message may motivate the recipient to work to  maintain their status as a top performer.

### Outcomes
The expected outcome of the successful influence of an email that uses the social better pathway is clinical process performance improvement or sustainment.


## Message templates
Message templates represent a possible tailored motivational message that a precision feedback system can send. There are two message templates that the Precision Feedback Pipeline can access for this vignette: 

A. The [Top 10 Performer](https://github.com/Display-Lab/knowledge-base/blob/social_better/message_templates/top_10_performer.json) message template contains the following message:
"Congratulations on your high performance last month! Your performance was above the 90th percentile of [Top 10% Benchmark performance level] for the measure [performance measure name]. Your performance was [recipient performance level]."
This message template is about a positive performance gap set and a social comparator element (the MPOG Top 10% Benchmark), and is specified to be about (http://purl.obolibrary.org/obo/IAO_0000136) the following metadata:
1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
2. Positive performance gap set (http://purl.obolibrary.org/obo/psdo_0000117)
3. Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)
4. Display format compatibility: Line graph (http://purl.obolibrary.org/obo/IAO_0000573), bar chart (http://purl.obolibrary.org/obo/STATO_0000166)

B. The [Top 25 Performer](https://github.com/Display-Lab/knowledge-base/blob/social_better/message_templates/top_25_performer.json) message template contains the following message: 
"Congrats on your high performance for the measure [performance measure name]! Your performance was [recipient performance level], above the 75th percentile benchmark [Top 25% Benchmark performance level] of your peers." 
This message template is about a positive performance gap set and a social comparator element (the Top 25% Peer Benchmark), and has the following metadata:
1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
2. Positive performance gap set (http://purl.obolibrary.org/obo/psdo_0000117)
3. Top 25% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000128)
4. Display format compatibility: Line graph (http://purl.obolibrary.org/obo/IAO_0000573), bar chart (http://purl.obolibrary.org/obo/STATO_0000166)


## Software Pipeline (Precision Feedback Pipeline)

### Recipient annotations (Bitstomach)
This data set should result in the following annotations:

Alice: Annotations indicate the presence of information content about a social comparator and a positive performance gap for both the Top 10% and Top 25% Benchmarks.
1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
2. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) regarding comparator Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)
3. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) regarding comparator Top 25% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000128)

Bob: Annotations indicate the presence of information content about a social comparator and a positive performance gap for the Top 25% Benchmark.
1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
2. Negative performance gap content (http://purl.obolibrary.org/obo/psdo_0000105) regarding comparator Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)
3. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) regarding comparator Top 25% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000128)


### Candidate Message Generation (Candidate Smasher)
For both Alice and Bob, their annotations above are associated with the metadata from each candidate message, so that two candidate messages are created for each person.

Alice's candidate messages:
A. Candidate A has the following annotations:
 Message is about:
	1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
	2. Positive performance gap set (http://purl.obolibrary.org/obo/psdo_0000117)
	3. Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)
	4. Display format compatibility: Line graph (http://purl.obolibrary.org/obo/IAO_0000573), bar chart (http://purl.obolibrary.org/obo/STATO_0000166)
 Alice's performance is about:
	1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
	2. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) regarding comparator Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)
	3. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) regarding comparator Top 25% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000128)

B. Candidate B has the following annotations:
 Message is about:
	1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
	2. Positive performance gap set (http://purl.obolibrary.org/obo/psdo_0000117)
	3. Top 25% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000128)
	4. Display format compatibility: Line graph (http://purl.obolibrary.org/obo/IAO_0000573), bar chart (http://purl.obolibrary.org/obo/STATO_0000166)
 Alice's performance is about:
	1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
	2. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) regarding comparator Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)
	3. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) regarding comparator Top 25% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000128)


Bob's candidate messages:
A. Candidate A has the following annotations:
 Message is about:
	1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
	2. Positive performance gap set (http://purl.obolibrary.org/obo/psdo_0000117)
	3. Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)
	4. Display format compatibility: Line graph (http://purl.obolibrary.org/obo/IAO_0000573), bar chart (http://purl.obolibrary.org/obo/STATO_0000166)
 Bob's performance is about:
	1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
	2. Negative performance gap content (http://purl.obolibrary.org/obo/psdo_0000105) regarding comparator Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)
	3. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) regarding comparator Top 25% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000128)

B. Candidate B has the following annotations:
 Message is about:
	1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
	2. Positive performance gap set (http://purl.obolibrary.org/obo/psdo_0000117)
	3. Top 25% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000128)
	4. Display format compatibility: Line graph (http://purl.obolibrary.org/obo/IAO_0000573), bar chart (http://purl.obolibrary.org/obo/STATO_0000166)
 Bob's performance is about:
	1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
	2. Negative performance gap content (http://purl.obolibrary.org/obo/psdo_0000105) regarding comparator Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)
	3. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) regarding comparator Top 25% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000128)

### Candidate Message Preconditions Evaluation (Think Pudding)
For Alice, both candidates are matched with the causal pathway Social Better, and are indicated as acceptable for ranking in the next stage of the pipeline.

For Bob, the candidate with a Top 25% benchmark is matched with the causal pathway Social Better, but the candidate with a Top 10% benchmark is not matched, because Bob's performance level is below the benchmark. The candidate message with the Top 25% benchmark is indicated as acceptable for ranking in the next stage of the pipeline.

### Candidate Message Moderator Evaluation and Selection (Esteemer)
TODO

### Message Generation and Delivery (Pictoralist)
TODO

