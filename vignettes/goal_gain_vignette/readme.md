# Goal Gain Vignette

## Introduction
Clinical performance feedback commonly includes goal comparisons that motivate providers to increase effort, including effort for problem-solving to improve the care they provide. When goals are reached, feedback about goal acheivement can be motivating to providers whose motivational orientation (i.e. regulatory focus), task, and context orient them toward growth and improvement. The feedback about the acheivement of goals can also satisfy provider's information needs for understanding changes in performance, to indicate that past efforts have yielded improvements, and that effort towards learning to improve might be shifted elsewhere. The Goal Gain Pathway specifies feedback messages that are capable of motivating providers through the delivery of information about goal achievement. An example message that uses the goal gain pathway is "You reached the goal." This vignette serves the purpose of illustrating how a precision feedback system uses the Goal Gain Pathway to motivate providers. 

## Performance Data
Each month, MPOG receives data about operative case quality and outcomes from approximately 60 healthcare institutions. MPOG calculates performance for each provider individually, for approximately 35 performance measures of quality and outcomes. One example of these measures is [TOC-01: Intraoperative Transfer of Care <sub>(MPOG)</sub>](https://spec.mpog.org/Spec/Public/29).

### Healthcare professional performance 
Eugene, a resident at Midwest Medicine, has the following performance data over the last 6 months for TOC-01:

|Month|Performance Level|Peer Average|75th Percentile Benchmark|90th Percentile Benchmark|MPOG Goal|
|-----|-------- |---|---|---|---|
|Jul  |      85%| 85| 88| 92| 90|
|Aug  |      85%| 85| 88| 92| 90|
|Sept |      85%| 85| 88| 92| 90|
|Oct  |      85%| 85| 88| 92| 90|
|Nov  |***85%***| 85| 88| 92| 90|
|Dec  |***91%***| 85| 88| 92| 90|

Gaile, also a resident at Midwest Medicine, has the following performance data over the last 6 months for TOC-01:

|Month|Performance Level|Peer Average|75th Percentile Benchmark|90th Percentile Benchmark|MPOG Goal|
|-----|-------- |---|---|---|---|
|Jul  |      85%| 85| 88| 92| 90|
|Aug  |      85%| 85| 88| 92| 90|
|Sept |      85%| 85| 88| 92| 90|
|Oct  |      85%| 85| 88| 92| 90|
|Nov  |***88%***| 85| 88| 92| 90|
|Dec  |***95%***| 85| 88| 92| 90|

## Preference data
Preferences for precision feedback are elicited through a preference survey that providers can take. The preference survey produces a preference model for each provider that, with the provider's permission, is shared with MPOG to maintain. MPOG analyses preference data that is shared to identify population-level preference segments. These segments are generated as preference profiles that can serve as a default preference model for an organization, or which can be selected by providers who do not take the preference survey, but who identify preferences that are close enough to their own in the settings menu for the precision feedback system.

Eugene's preference data: 

|Motivating information |Utility value|Description                                                                     |
|-----------------------|-------------|--------------------------------------------------------------------------------|
|Social Gain	           |10.4659	    |Performance was previously low, but it has improved to reach the peer benchmark.|
|Social Stayed Better   |-11.3618	    |Performance is consistently high (no recent change).                            |
|Worsening             	|11.6598	   |Performance is worsening.                                                       |
|Improving	             |7.58489	    |Performance is improving.                                                       |
|Social Loss             |8.46823	    |Performance was previously high, but it has dropped below the peer average.     |
|Social Stayed Worse	   |-3.64987	   |Performance has remained below average (no recent change).                      |
|Social Better	         |-8.64669	    |Performance is high this month.                                                 |
|Social Worse	          |12.1645	   |Performance is low this month.                                                  |
|Social Approach	       |-10.6889 	   |Performance is improving, getting closer to the peer benchmark.                 |

Gaile's preference data:

|Motivating information |Utility value|Description                                                                     |
|-----------------------|-------------|--------------------------------------------------------------------------------|
|Social gain	           |xx.xxxxx	    |Performance was previously low, but it has improved to reach the peer benchmark.|
|Social stayed better   |-12.76936	   |Performance is consistently high (no recent change).                            |
|Worsening             	|1.06977     	|Performance is worsening.                                                       |
|Improving	             |-0.26266	    |Performance is improving.                                                       |
|Social loss            |2.72075	     |Performance was previously high, but it has dropped below the peer average.     |
|Social stayed worse	   |9.97743	     |Performance has remained below average (no recent change).                      |
|Social better	         |-5.97766	    |Performance is high this month.                                                 |
|Social worse	          |-0.05277	    |Performance is low this month.                                                  |
|Social approach	       |-0.24384	    |Performance is improving, getting closer to the peer benchmark.                 |

# Precision feedback message generation
To generate precision feedback, MPOG sends de-identified performance and preference data to a precision feedback system that processes each provider's data with their peer comparator performance data. The precision feedback system produces and evaluates candidate messages using metadata from message templates, then selects an optimal precision feedback message to return to MPOG. The precision feedback system is a knowledge-based system that is comprised of the following parts: a knowledge base, a software pipeline, and a web service.

## Precision Feedback Knowledge Base
The knowledge base contains the following components: Causal pathways, message templates, and performance measures.

## Goal Gain Causal Pathway 
The goal gain causal pathway describes the influence of feedback interventions that show the recipient that their performance is better than that of an explicit goal, such as the performance threshold set by MPOG. The causal pathway model is made up of preconditions, moderators, mechanisms, and outcomes.

### Preconditions
Preconditions for goal gain are factors that are necessary for the success of the feedback intervention that uses the goal gain pathway. The goal gain pathway has the following preconditions:

**Information content preconditions:**
1. [Goal comparator content <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000094)
2. [Positive performance gap content <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000104)
3. [Positive performance trend content <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000099)
4. [Achievement content <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000112)

**Message preconditions:**
1. [Goal comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000046)
2. [Positive performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000117)
3. [Positive performance trend set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)
4. [Achievement set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000121)

### Moderators
Moderators are factors that inhibit or promote the influence of the feedback intervention on the recipient. The goal gain causal pathway has the following moderators:
1. `Message recency` - The number of months since the message was delivered previously.
2. `Message delivery count` - How many times has the recipient previously received this message in the last year?  
3. `Regulatory fit` - To what extent is the message aligned to the behavior/task's characteristics, context, and recipient personality (motivated by bad outcome prevention vs. good outcome promotion).
4. `Gap size` - How large is the gap between the recipient's performance level and that of the social comparator?
5. `Slope of trend` - Derivative of the performance measure in the time domain
6. `Time since last loss`

### Mechanisms
Mechanisms are factors that the intervention operates through to influence the feedback recipient. Adapted from [Carey et. al. 2019](https://doi.org/10.1093/abm/kay078). The goal gain pathway has the following mechanisms:
1. `Awareness (knowledge)`: The message may change the recipient's awareness of their own performance and of institutional performance goals.
2. `Goals`: The message may create or reinforce mental representations of outcomes or end states that an individual wants to achieve, relative to their clinical performance.
3. `Motivation`: The message may give the recipient purpose or direction towards changing their own performance.

### Outcomes
The expected outcome of the successful influence of an email that uses the goal gain pathway is clinical process performance improvement or sustainment.

## Message templates
Message templates represent a possible motivational message that a precision feedback system can send. There is one message templates that the precision feedback system can access for this vignette: 

**[Reached Goal <sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/reached_goal.json)** message:
> You reached the goal this month for the measure [Measure name]. Your performance was [recipient performance level as percentage (with numerator and denominator)].
    
This message template `is about` [<sub>(OntoBee)</sub>](https://ontobee.org/ontology/IAO?iri=http://purl.obolibrary.org/obo/IAO_0000136) the following data features:
1. `Goal comparator element` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000046)
2. `Positive performance gap set` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000117)
3. `Positive performance trend set` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)
4. `Achievement set` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000121)

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

