# Social Loss Vignette

## Introduction
This vignette illustrates the process for creating precision feedback messages about a recipient's performance dropping below a peer comparator, such as a top performer benchmark or peer average. These messages use the Social Loss Causal Pathway, which specifies feedback messages that are capable of motivating providers through the delivery of information about performance worsening. Motivation from these messages can arise from the recognition of a loss of social status as a top or above-average performer. Example messages that use Social Loss are "You are no longer a top performer" and "Your performance has dropped below the peer average".

This vignette also contains example data and unique identifiers for the features of data and other entities that a precision feedback system uses to reason about the potential success of a precision feedback message. An example of a unique identifier is "http://purl.obolibrary.org/obo/psdo_0000126" which reprsents a peer average comparator, and which is defined in the [Performance Summary Display Ontology](https://github.com/Display-Lab/psdo) as an average representing the mean performance of a peer group. 

## Performance Data
Each month, MPOG receives data about operative case quality and outcomes from approximately 60 healthcare institutions. MPOG calculates performance for each provider individually, for approximately 35 performance measures of quality and outcomes. One example of these measures is [PONV-05: Post-operative Nausea and Vomiting Prophylaxis: Adults](https://spec.mpog.org/Spec/Public/53).

### Benchmark comparators
MPOG calculates performance benchmarks and averages for each institution. One comparator is a Top 10% Benchmark (http://purl.obolibrary.org/obo/psdo_0000129), which represents the 90th percentile for performance among providers at an institution, for each measure. Another comparator is the peer average (http://purl.obolibrary.org/obo/psdo_0000126), which is the mean performance for all providers at an insitution, for each measure.

### Healthcare professional performance
Alice, an attending anesthesiologist at Midwest Medicine, has the following performance data over the last 6 months for PONV-05:

|Month|Performance Level|Top 10% Benchmark|Peer Average|
|-----|-----------------|-----------------|------------|
|Oct  |              88%|               93|          86|
|Nov  |              89%|               96|          88|
|Dec  |              87%|               95|          87|
|Jan  |              86%|               97|          87|
|Feb  |              81%|               94|          86|
|Mar  |              78%|               96|          88|

Bob, a CRNA at Danville Hospital, has the following performance data over the last 6 months for PONV-05:

|Month|Performance Level|Top 10% Benchmark|Peer Average|
|-----|-----------------|-----------------|------------|
|Oct  |              97%|               94|          85|
|Nov  |              96%|               95|          87|
|Dec  |              95%|               96|          86|
|Jan  |              98%|               97|          84|
|Feb  |              95%|               95|          85|
|Mar  |              91%|               96|          87|


## Preference data

Alice's preference data: (TODO)

Bob's preference data: (TODO)


# Precision feedback message generation
To generate precision feedback, MPOG sends de-identified performance and preference data to a precision feedback system that processes each provider's data with their peer comparator performance data. The precision feedback system produces and evaluates candidate messages using metadata from message templates, then selects an optimal precision feedback message to return to MPOG. The precision feedback system is a knowledge-based system that is comprised of the following parts: 1) A knowledge base, 2) A software pipeline, and 3) A web service.

## Precision Feedback Knowledge Base
The knowledge base contains the following components: Causal pathways, message templates, and performance measures.

## Social Loss Causal Pathway
This pathway describes the influence of feedback interventions that show the message recipient that their performance has become worse than that of a social comparator, such as a top performer benchmark or peer average. The causal pathway model is made up of preconditions, moderators, mechanisms, and outcomes.

### Preconditions
Preconditions for social loss are factors that are necessary for the success of the feedback intervention using this pathway. The social loss pathway has the following preconditions:

Information content preconditions:
1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
2. Negative performance gap content (http://purl.obolibrary.org/obo/psdo_0000105)
3. Negative performance trend content (http://purl.obolibrary.org/obo/psdo_0000100)
4. Loss content (http://purl.obolibrary.org/obo/psdo_0000113)

Message preconditions:
1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
2. Negative performance gap set (http://purl.obolibrary.org/obo/psdo_0000116)
3. Negative performance trend set (http://purl.obolibrary.org/obo/psdo_0000119)
4. Loss set (http://purl.obolibrary.org/obo/psdo_0000122)
 
### Moderators
Moderators are factors that inhibit or promote the influence of the feedback intervention on the recipient. The social loss causal pathway has the following moderators:
1. Habituation: How many times has the recipient previously received this message in the last year?
2. Regulatory fit: To what extent is this message aligned with characteristics of the behavior/task, context, and recipient personality, with regard to motivation to avoid negative outcomes / problem (prevention focus), or motivation to achieve positive outcomes / develop and learn (promotion focus)?
3. Gap size: How large is the gap between the recipient's performance level and that of the social comparator?
4. Slope of trend
5. Time since last achievement

### Mechanisms
Mechanisms are factors that the intervention operates through to influence the feedback recipient. The social loss pathway has the following mechanisms:
1. Awareness (knowledge): The message may change the recipient's awareness of their high performance, relative to peers.
2. Subjective norms: The message may influence the precipient by creating or reinforcing their perception of their own top-performer status within their peer group.
3. Motivation: The message may motivate the recipient to work to  maintain their status as a top performer.

### Outcomes
The expected outcome of the successful influence of an email that uses the social loss pathway is clinical process performance improvement.

## Message templates
Message templates represent a possible motivational message that a precision feedback system can send. There are two message templates that the precision feedback system can access for this vignette: 

A. The [Lost Peer Average](https://github.com/Display-Lab/knowledge-base/blob/social_loss/message_templates/lost_peer_average.json) message template contains the following message: "Your performance dropped below the peer average for the measure [measure name]". This message template [is about] (http://purl.obolibrary.org/obo/IAO_0000136) the following features of performance data:
1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
2. Negative performance gap set (http://purl.obolibrary.org/obo/psdo_0000116)
3. Negative performance trend set (http://purl.obolibrary.org/obo/psdo_0000119)
4. Loss set (http://purl.obolibrary.org/obo/psdo_0000122)
5. Peer average comparator (http://purl.obolibrary.org/obo/PSDO_0000126)
6. Display format compatibility: Line graph (http://purl.obolibrary.org/obo/IAO_0000573), bar chart (http://purl.obolibrary.org/obo/STATO_0000166)

B. The [Lost Top 10 Benchmark](https://github.com/Display-Lab/knowledge-base/blob/social_loss/message_templates/lost_top_10_benchmark.json) message template contains the following message: "You are no longer a top performer for the measure [measure name]." This message template [is about] (http://purl.obolibrary.org/obo/IAO_0000136) the following features of performance data:

1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
2. Negative performance gap set (http://purl.obolibrary.org/obo/psdo_0000116)
3. Negative performance trend set (http://purl.obolibrary.org/obo/psdo_0000119)
4. Loss set (http://purl.obolibrary.org/obo/psdo_0000122)
5. Top 10% Benchmark comparator (http://purl.obolibrary.org/obo/PSDO_0000129)
6. Display format compatibility: Line graph (http://purl.obolibrary.org/obo/IAO_0000573), bar chart (http://purl.obolibrary.org/obo/STATO_0000166)

## Software Pipeline (Precision Feedback Pipeline)

### Recipient annotations (Bitstomach)
The first stage of the pipeline analyzes performance to identify features of performance, such as comparisons and trends that are related to motivation. The analysis from this stage results in the following annotations:

Alice's annotations indicate the presence of the following in her performance data this month:
1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
2. Negative performance gap content (http://purl.obolibrary.org/obo/psdo_0000105) regarding comparator Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)
3. Negative performance gap content (http://purl.obolibrary.org/obo/psdo_0000105) regarding comparator Peer Average Comparator (http://purl.obolibrary.org/obo/psdo_0000126)
4. Negative performance trend content (http://purl.obolibrary.org/obo/psdo_0000100)
5. Loss content (http://purl.obolibrary.org/obo/psdo_0000113) regarding comparator Peer Average Comparator (http://purl.obolibrary.org/obo/psdo_0000126)

Bob's annotations indicate the presence of the following in his performance data this month:
1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
2. Negative performance gap content (http://purl.obolibrary.org/obo/psdo_0000105) regarding comparator Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)
3. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) regarding comparator Peer Average Comparator (http://purl.obolibrary.org/obo/psdo_0000126)
4. Negative performance trend content (http://purl.obolibrary.org/obo/psdo_0000100)
5. Loss content (http://purl.obolibrary.org/obo/psdo_0000113) regarding comparator Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)


### Candidate Message Generation (Candidate Smasher)
The second stage of the pipeline creates possible messages by associating the annotations for Alice and Bob with each message template, so that two candidate messages are created for each person.

Alice's candidate messages:

A. Candidate A has the following annotations:

The [Lost Peer Average](https://github.com/Display-Lab/knowledge-base/blob/social_loss/message_templates/lost_peer_average.json) message template [is about](http://purl.obolibrary.org/obo/IAO_0000136) the following features of performance data:
1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
2. Negative performance gap set (http://purl.obolibrary.org/obo/psdo_0000116)
3. Negative performance trend set (http://purl.obolibrary.org/obo/psdo_0000119)
4. Loss set (http://purl.obolibrary.org/obo/psdo_0000122)
5. Peer average comparator (http://purl.obolibrary.org/obo/PSDO_0000126)
6. Display format compatibility: Line graph (http://purl.obolibrary.org/obo/IAO_0000573), bar chart (http://purl.obolibrary.org/obo/STATO_0000166)

Alice's annotations from this month:
1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
2. Negative performance gap content (http://purl.obolibrary.org/obo/psdo_0000105) regarding comparator Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)
3. Negative performance gap content (http://purl.obolibrary.org/obo/psdo_0000105) regarding comparator Peer Average Comparator (http://purl.obolibrary.org/obo/psdo_0000126)
4. Negative performance trend content (http://purl.obolibrary.org/obo/psdo_0000100)
5. Loss content (http://purl.obolibrary.org/obo/psdo_0000113) regarding comparator Peer Average Comparator (http://purl.obolibrary.org/obo/psdo_0000126)

B. Candidate B has the following annotations:

The [Lost Top 10 Benchmark](https://github.com/Display-Lab/knowledge-base/blob/social_loss/message_templates/lost_top_10_benchmark.json) message template [is about] (http://purl.obolibrary.org/obo/IAO_0000136) the following features of performance data:
1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
2. Negative performance gap set (http://purl.obolibrary.org/obo/psdo_0000116)
3. Negative performance trend set (http://purl.obolibrary.org/obo/psdo_0000119)
4. Loss set (http://purl.obolibrary.org/obo/psdo_0000122)
5. Top 10% Benchmark comparator (http://purl.obolibrary.org/obo/PSDO_0000129)
6. Display format compatibility: Line graph (http://purl.obolibrary.org/obo/IAO_0000573), bar chart (http://purl.obolibrary.org/obo/STATO_0000166)

Alice's annotations from this month:
1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
2. Negative performance gap content (http://purl.obolibrary.org/obo/psdo_0000105) regarding comparator Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)
3. Negative performance gap content (http://purl.obolibrary.org/obo/psdo_0000105) regarding comparator Peer Average Comparator (http://purl.obolibrary.org/obo/psdo_0000126)
4. Negative performance trend content (http://purl.obolibrary.org/obo/psdo_0000100)
5. Loss content (http://purl.obolibrary.org/obo/psdo_0000113) regarding comparator Peer Average Comparator (http://purl.obolibrary.org/obo/psdo_0000126)

Bob's candidate messages:

A. Candidate A has the following annotations:

The [Lost Peer Average](https://github.com/Display-Lab/knowledge-base/blob/social_loss/message_templates/lost_peer_average.json) message template [is about](http://purl.obolibrary.org/obo/IAO_0000136) the following features of performance data:
1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
2. Negative performance gap set (http://purl.obolibrary.org/obo/psdo_0000116)
3. Negative performance trend set (http://purl.obolibrary.org/obo/psdo_0000119)
4. Loss set (http://purl.obolibrary.org/obo/psdo_0000122)
5. Peer average comparator (http://purl.obolibrary.org/obo/PSDO_0000126)
6. Display format compatibility: Line graph (http://purl.obolibrary.org/obo/IAO_0000573), bar chart (http://purl.obolibrary.org/obo/STATO_0000166)

Bob's performance is about:
1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
2. Negative performance gap content (http://purl.obolibrary.org/obo/psdo_0000105) regarding comparator Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)
3. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) regarding comparator Peer Average Comparator (http://purl.obolibrary.org/obo/psdo_0000126)
4. Negative performance trend content (http://purl.obolibrary.org/obo/psdo_0000100)
5. Loss content (http://purl.obolibrary.org/obo/psdo_0000113) regarding comparator Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)

B. Candidate B has the following annotations:

The [Lost Top 10 Benchmark](https://github.com/Display-Lab/knowledge-base/blob/social_loss/message_templates/lost_top_10_benchmark.json) message template [is about] (http://purl.obolibrary.org/obo/IAO_0000136) the following features of performance data:
1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
2. Negative performance gap set (http://purl.obolibrary.org/obo/psdo_0000116)
3. Negative performance trend set (http://purl.obolibrary.org/obo/psdo_0000119)
4. Loss set (http://purl.obolibrary.org/obo/psdo_0000122)
5. Top 10% Benchmark comparator (http://purl.obolibrary.org/obo/PSDO_0000129)
6. Display format compatibility: Line graph (http://purl.obolibrary.org/obo/IAO_0000573), bar chart (http://purl.obolibrary.org/obo/STATO_0000166)

Bob's performance is about:
1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
2. Negative performance gap content (http://purl.obolibrary.org/obo/psdo_0000105) regarding comparator Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)
3. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) regarding comparator Peer Average Comparator (http://purl.obolibrary.org/obo/psdo_0000126)
4. Negative performance trend content (http://purl.obolibrary.org/obo/psdo_0000100)
5. Loss content (http://purl.obolibrary.org/obo/psdo_0000113) regarding comparator Top 10% Benchmark Comparator (http://purl.obolibrary.org/obo/psdo_0000129)

### Candidate Message Preconditions Evaluation (Think Pudding)
For Alice, Candidate A is acceptable by social loss.
For Bob, Candidate B is acceptable by social loss.

### Candidate Message Moderator Evaluation and Selection (Esteemer)
TODO

### Message Generation and Delivery (Pictoralist)
TODO

