# Social Better Vignette

## Introduction
Clinical performance feedback commonly includes peer comparison because it helps providers to understand how their care differs from the norm, and may motivate them to improve the care they provide to align with peers. Peer comparison feedback may also motivate providers to maintain a social status of being a high performer, once they have achieved it. The Social Better Causal Pathway specifies feedback messages that are capable of motivating providers through the delivery of information about high performance, relative to peers. Example messages that uses the social better pathway are "You are a top performer" and "Congratulations, your performance was in the top 10% of providers this month." This vignette serves the purpose of illustrating how a precision feedback system uses the Social Better Causal Pathway to motivate providers. 

This vignette also contains examples of data features and other entities that a precision feedback system uses to evaluate the potential success of a precision feedback message. An example of such an entity is a [peer average comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126), which is defined in the [Performance Summary Display Ontology <sub>(GH)</sub>](https://github.com/Display-Lab/psdo) as an average representing the mean performance of a peer group. 

## Performance Data
Each month, MPOG receives data about operative case quality and outcomes from approximately 60 healthcare institutions. MPOG calculates performance for each provider individually, for approximately 35 performance measures of quality and outcomes. One example of these measures is [SUS-04 : Fresh Gas Flow, less than or equal to 2L/min <sub>(MPOG)</sub>](https://spec.mpog.org/Spec/Public/63).

### Benchmark comparators
MPOG calculates performance benchmarks and averages for each institution. One comparator is a [peer 90th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000129), which represents the 90th percentile for performance among providers at an institution, for each measure. Another is the [peer average comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126), which is the mean performance for all providers at an insitution, for each measure.

### Healthcare professional performance
Alice, an attending anesthesiologist at Midwest Medicine, has the following performance data over the last 6 months for SUS-04:

|Month|Performance Level|Peer Average|75th Percentile Benchmark|90th Percentile Benchmark|MPOG Goal|
|-|-|-|-|-|-|
|Jul  |      90%|90|92|96|90|
|Aug  |      90%|90|92|96|90|
|Sept |      90%|90|92|96|90|
|Oct  |      90%|90|92|96|90|
|Nov  |***88%***|90|92|96|90|
|Dec  |***98%***|90|92|96|90|

Gaile, a resident anesthesiologist at Midwest Medicine, has the following performance data over the last 6 months for SUS-04:

|Month|Performance Level|Peer Average|75th Percentile Benchmark|90th Percentile Benchmark|MPOG Goal|
|-----|-----------------|------------|-------------------------|-------------------------|-|
|Jul  |      85%|          85|                       88|                       92|90|
|Aug  |      85%|          85|                       88|                       92|90|
|Sept |      85%|          85|                       88|                       92|90|
|Oct  |      85%|          85|                       88|                       92|90|
|Nov  |***83%***|          85|                       88|                       92|90|
|Dec  |***87%***|          85|                       88|                       92|90|

## Preference data
Preferences for precision feedback are elicited through a preference survey that providers can take. The preference survey produces a preference model for each provider that, with the provider's permission, is shared with MPOG to maintain. MPOG analyses preference data that is shared to identify population-level preference segments. These segments are generated as preference profiles that can serve as a default preference model for an organization, or which can be selected by providers who do not take the preference survey, but who identify preferences that are close enough to their own in the settings menu for the precision feedback system.

Alice's preference data:
|Motivating information |Utility value|Description                                                                     |
|-----------------------|-------------|--------------------------------------------------------------------------------|
|Social gain	           |12.97730	    |Performance was previously low, but it has improved to reach the peer benchmark.|
|Social stayed better   |6.164377	    |Performance is consistently high (no recent change).                            |
|Worsening             	|-12.23023	   |Performance is worsening.                                                       |
|Improving	             |3.325883	    |Performance is improving.                                                       |
|Social loss             |9.956127	    |Performance was previously high, but it has dropped below the peer average.     |
|Social stayed worse	   |-7.710484	   |Performance has remained below average (no recent change).                      |
|Social better	         |-1.61124	    |Performance is high this month.                                                 |
|Social worse	          |-14.86794	   |Performance is low this month.                                                  |
|Social approach	       |13.99621 	   |Performance is improving, getting closer to the peer benchmark.                 |


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

# Precision feedback system
To generate precision feedback, MPOG sends de-identified performance and preference data to a precision feedback system that processes each provider's data with their peer comparator performance data. The precision feedback system produces and evaluates candidate messages using metadata from message templates, then selects an optimal precision feedback message to return to MPOG. The precision feedback system is a knowledge-based system that is comprised of the following parts: knowledge base, software pipeline, and web service.

## Precision Feedback Knowledge Base
The knowledge base contains the following components: Causal pathways, message templates, and performance measures.

### Social Better Causal Pathway 
The causal pathway "social better" describes the influence of feedback interventions that show the recipient that their performance is better than that of a social comparator, such as a top performer benchmark or peer average. The causal pathway model is made up of preconditions, moderators, mechanisms, and outcomes.

### Preconditions
Preconditions for social better are factors that are necessary for the success of feedback intervention using this pathway. The social better pathway has the following preconditions:

**Information content preconditions:**
1. [Social comparator content <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000095)
2. [Positive performance gap content <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000104)

**Message preconditions:**
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045)
2. [Positive performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000117)

### Moderators
Moderators are factors that inhibit or promote the influence of the feedback intervention on the recipient. The social better causal pathway has the following moderators:
1. `Habituation` - How many times has the recipient previously received this message in the last year?
2. `Regulatory fit` - To what extent is this message aligned with characteristics of the behavior/task, context, and recipient personality, with regard to motivation to avoid negative outcomes / problem (prevention focus), or motivation to achieve positive outcomes / develop and learn (promotion focus)?
3. `Gap size` - How large is the gap between the recipient's performance level and that of the social comparator?

### Mechanisms
Mechanisms are factors that the intervention operates through to influence the feedback recipient. The social better pathway has the following mechanisms:
1. `Awareness (knowledge)` - The message may change the recipient's awareness of their high performance, relative to peers.
2. `Subjective norms` - The message may influence the precipient by creating or reinforcing their perception of their own top-performer status within their peer group.
3. `Motivation` - The message may motivate the recipient to work to  maintain their status as a top performer.

### Outcomes
The expected outcome of the successful influence of an email that uses the social better pathway is clinical process performance improvement or sustainment.


## Message templates
Message templates represent a possible motivational message that a precision feedback system can send. There is one message template that the precision feedback system can currently access for this vignette:

The `Top Performer`[ <sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/top_performer.json) message:
> You are a top performer this month for the measure [Measure name]. Your performance was [recipient performance level - percentage], above the [comparator name].

This message template `is about` [<sub>(OntoBee)</sub>](https://ontobee.org/ontology/IAO?iri=http://purl.obolibrary.org/obo/IAO_0000136) the following data features:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045) 
2. [Positive performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000117)
3. [Peer 90th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000129)
4. Display format compatability: [Line Graph <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/IAO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FIAO_0000573), [Bar Chart <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/STATO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FSTATO_0000166)

## Software Pipeline (Precision Feedback Pipeline)
WIP 
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

