# Goal Gain Vignette

## Introduction
Clinical performance feedback commonly includes goal comparisons that motivate providers to increase effort, including effort for problem-solving to improve the care they provide. When goals are reached, feedback about goal acheivement can be motivating to providers whose motivational orientation (i.e. regulatory focus), task, and context orient them toward growth and improvement. The feedback about the acheivement of goals can also satisfy provider's information needs for understanding changes in performance, to indicate that past efforts have yielded improvements, and that effort towards learning to improve might be shifted elsewhere. The Goal Gain Pathway specifies feedback messages that are capable of motivating providers through the delivery of information about goal achievement. An example message that uses the goal gain pathway is "You reached the goal." This vignette serves the purpose of illustrating how a precision feedback system uses the Goal Gain Pathway to motivate providers. 

## Performance Data
MPOG has received operative case data from last month about Eugene and Gaile's cases and that of their peers. MPOG calculates the following performance information for the measure [TOC-01: Intraoperative Transfer of Care <sub>(MPOG)</sub>](https://spec.mpog.org/Spec/Public/29).

### Healthcare professionals
Eugene ... Todo
|Month|Performance Level|Peer Average|75th Percentile Benchmark|90th Percentile Benchmark|MPOG Goal|
|-----|-------- |---|---|---|---|
|Jul  |      85%| 85| 88| 92| 90|
|Aug  |      85%| 85| 88| 92| 90|
|Sept |      85%| 85| 88| 92| 90|
|Oct  |      85%| 85| 88| 92| 90|
|Nov  |***85%***| 85| 88| 92| 90|
|Dec  |***91%***| 85| 88| 92| 90|

Gaile ... Todo
|Month|Performance Level|Peer Average|75th Percentile Benchmark|90th Percentile Benchmark|MPOG Goal|
|-----|-------- |---|---|---|---|
|Jul  |      85%| 85| 88| 92| 90|
|Aug  |      85%| 85| 88| 92| 90|
|Sept |      85%| 85| 88| 92| 90|
|Oct  |      85%| 85| 88| 92| 90|
|Nov  |***88%***| 85| 88| 92| 90|
|Dec  |***95%***| 85| 88| 92| 90|

### Benchmark comparators
Alice's peer benchmarks for last month are 93% for the top 25% peer benchmark (75th percentile http://purl.obolibrary.org/obo/psdo_0000128), and 96% for the top 10% peer benchmark (90th percentile http://purl.obolibrary.org/obo/psdo_0000129).

## Preference data
Preferences for precision feedback are elicited through a preference survey that providers can take. The preference survey produces a preference model for each provider that, with the provider's permission, is shared with MPOG to maintain. MPOG analyses preference data that is shared to identify population-level preference segments. These segments are generated as preference profiles that can serve as a default preference model for an organization, or which can be selected by providers who do not take the preference survey, but who identify preferences that are close enough to their own in the settings menu for the precision feedback system.

# Precision feedback system
To generate precision feedback, MPOG sends de-identified performance and preference data to a precision feedback system that processes each provider's data with their peer comparator performance data, to select an optimal precision feedback message. 
The precision feedback system is a knowledge-based system that is comprised of the following parts: 1) A knowledge base, 2) A software pipeline, and 3) A web service.

## Precision Feedback Knowledge Base
The knowledge base contains the following components: Causal pathways, message templates, and performance measures.

## Goal Gain Causal Pathway 
The causal pathway "goal gain" describes the influence of feedback interventions that show the recipient that their performance is better than that of a social comparator, such as a top performer benchmark or peer average. The causal pathway model is made up of preconditions, moderators, mechanisms, and outcomes.

### Preconditions
Preconditions for social better are factors that are necessary for the success of the feedback intervention that uses the social better pathway. The social better pathway has the following preconditions:
Information content preconditions:
1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
2. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104)
Message preconditions:
1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
2. Positive performance gap set (http://purl.obolibrary.org/obo/psdo_0000117)

### Moderators
Moderators are factors that inhibit or promote the influence of the feedback intervention on the recipient. The social better causal pathway has the following moderators:
1. Habituation: How many times has the recipient previously received this message in the last year?
2. Regulatory fit: To what extent is this message aligned with characteristics of the behavior/task, context, and recipient personality, with regard to motivation to avoid negative outcomes / problem (prevention focus), or motivation to achieve positive outcomes / develop and learn (promotion focus)?
3. Gap size: How large is the gap between the recipient's performance level and that of the social comparator?

### Mechanisms
Mechanisms are factors that the intervention operates through to influence the feedback recipient. The social better pathway has the following mechanisms:
1. Awareness (knowledge): The message may change the recipient's awareness of their high performance, relative to peers.
2. Subjective norms: The message may influence the precipient by creating or reinforcing their perception of their own top-performer status within their peer group.
3. Motivation: The message may motivate the recipient to work to  maintain their status as a top performer.

### Outcomes
The expected outcome of the successful influence of an email that uses the goal gain pathway is clinical process performance improvement or sustainment.

## Message templates
Message templates represent a possible motivational message that a precision feedback system can send. There are two message templates that the precision feedback system can access for this vignette: 
A. The [Top 10 Performer](https://github.com/Display-Lab/knowledge-base/blob/social_better/message_templates/top_10_performer.json) message template contains the following message:
"Congratulations on your high performance last month! Your performance was above the 90th percentile of [Top 10% Benchmark performance level] for the measure [performance measure name]. Your performance was [recipient performance level]."
This message template is about a positive performance gap set and a social comparator element (the MPOG Top 10% Benchmark), and is specified to be about (http://purl.obolibrary.org/obo/IAO_0000136) the following metadata:
1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
2. Positive performance gap set (http://purl.obolibrary.org/obo/psdo_0000117)
3. Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)
4. Display format compatibility: Line graph (http://purl.obolibrary.org/obo/IAO_0000573), bar chart (http://purl.obolibrary.org/obo/STATO_0000166)

## Software Pipeline (Precision Feedback Pipeline)

### Recipient annotations (Bitstomach)
The first stage of the pipeline analyzes performance to identify features of performance, such as comparisons and trends that are related to motivation. The analysis from this stage results in the following annotations:
Alice's annotations indicate the presence of information content about a social comparator and a positive performance gap for both the Top 10% and Top 25% Benchmarks:
1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
2. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) regarding comparator Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)
3. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) regarding comparator Top 25% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000128)
### Candidate Message Generation (Candidate Smasher)
The second stage of the pipeline creates possible messages by associating the annotations for Alice and Bob with each message template, so that two candidate messages are created for each person.
Alice's candidate messages:
A. Candidate A has the following annotations:
The [Top 10 Performer](https://github.com/Display-Lab/knowledge-base/blob/social_better/message_templates/top_10_performer.json) message template is about:
1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
2. Positive performance gap set (http://purl.obolibrary.org/obo/psdo_0000117)
3. Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)
4. Display format compatibility: Line graph (http://purl.obolibrary.org/obo/IAO_0000573), bar chart (http://purl.obolibrary.org/obo/STATO_0000166)
Alice's performance is about:
1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
2. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) regarding comparator Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)
3. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) regarding comparator Top 25% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000128)
B. Candidate B has the following annotations:
The [Top 25 Performer](https://github.com/Display-Lab/knowledge-base/blob/social_better/message_templates/top_25_performer.json) message template is about:
1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
2. Positive performance gap set (http://purl.obolibrary.org/obo/psdo_0000117)
3. Top 25% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000128)
4. Display format compatibility: Line graph (http://purl.obolibrary.org/obo/IAO_0000573), bar chart (http://purl.obolibrary.org/obo/STATO_0000166)
Alice's performance is about:
1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
2. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) regarding comparator Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)
3. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) regarding comparator Top 25% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000128)
### Candidate Message Preconditions Evaluation (Think Pudding)
For Alice, both candidates have matching preconditions with social better, and are indicated as acceptable for ranking in the next stage of the pipeline:
1. Candidate A acceptable by social better
2. Candidate B acceptable by social better
### Candidate Message Moderator Evaluation and Selection (Esteemer)
TODO
### Message Generation and Delivery (Pictoralist)
TODO

