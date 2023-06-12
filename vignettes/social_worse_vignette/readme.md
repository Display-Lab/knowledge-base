# Social Worse Vignette
## Introduction
This vignette delineates the process for creating precision feedback messages about a recipient's performance worsening in comparison with their peers. These messages use the Social Worse causal pathway, which provides negative feedback that may motivate providers by delivering information about their recent performance being below a specified social comparator for a given month. An example messages that uses the social worse pathway is "you are not a top performer this month".


This vignette also contains examples of data features and other entities that a precision feedback system uses to evaluate the potential success of a precision feedback message. An example of such an entity is a [peer average comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126), which is defined in the [Performance Summary Display Ontology <sub>(GH)</sub>](https://github.com/Display-Lab/psdo) as an average representing the mean performance of a peer group.

## Performance Data
Each month, MPOG receives data about operative case quality and outcomes from approximately 60 healthcare institutions. MPOG calculates performance for each provider individually, for approximately 35 performance measures of quality and outcomes. One example of these measures is [GLU-01 : High Glucose Treated, Intraop<sub>(MPOG)</sub>](https://spec.mpog.org/Spec/Public/5).

### Benchmark comparators
MPOG calculates performance benchmarks and averages for each institution. One comparator is a [peer 90th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000129), which represents the 90th percentile for performance among providers at an institution, for each measure. Another is the [peer average comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126), which is the mean performance for all providers at an insitution, for each measure.

### Healthcare professional performance
Deepa, a nurse anesthetist (CRNA) at Midwest Medicine, has the following performance data over the last 6 months for the GLU-01 measure:

|Month|Performance Level|Peer Average|75th Percentile Benchmark|90th Percentile Benchmark|
|-----|-----------------|------------|-------------------------|-------------------------|
|Jul  |              80%|          80|                       85|                       90|
|Aug  |              80%|          80|                       85|                       90|
|Sept |              80%|          80|                       85|                       90|
|Oct  |              80%|          80|                       85|                       90|
|Nov  |          **88%**|          80|                       85|                       90|
|Dec  |          **89%**|          80|                       85|                       90|

Eugene, a resident anesthesiologist at Midwest Medicine, has the following performance data over the last 6 months for the GLU-01 measure:

|Month|Performance Level|Peer Average|75th Percentile Benchmark|90th Percentile Benchmark|
|-----|-----------------|------------|-------------------------|-------------------------|
|Jul  |              85%|          85|                       88|                       92|
|Aug  |              85%|          85|                       88|                       92|
|Sept |              85%|          85|                       88|                       92|
|Oct  |              85%|          85|                       88|                       92|
|Nov  |          **90%**|          85|                       88|                       92|
|Dec  |          **90%**|          85|                       88|                       92|

## Preference data
Preferences for precision feedback are elicited through a preference survey that providers can take. The preference survey produces a preference model for each provider that, with the provider's permission, is shared with MPOG to maintain. MPOG analyses preference data that is shared to identify population-level preference segments. These segments are generated as preference profiles that can serve as a default preference model for an organization, or which can be selected by providers who do not take the preference survey, but who identify preferences that are close enough to their own in the settings menu for the precision feedback system.

Deepa's preference data:

|Motivating information |Utility value|Description                                                                     |
|-----------------------|-------------|--------------------------------------------------------------------------------|
|Social Gain	           |-5.64820	    |Performance was previously low, but it has improved to reach the peer benchmark.|
|Social Stayed Better   |-6.01254	    |Performance is consistently high (no recent change).                            |
|Worsening             	|11.1987	   |Performance is worsening.                                                       |
|Improving	             |-9.5648	    |Performance is improving.                                                       |
|Social Loss             |10.1248	    |Performance was previously high, but it has dropped below the peer average.     |
|Social Stayed Worse	   |2.79345	   |Performance has remained below average (no recent change).                      |
|Social Better	         |1.64862	    |Performance is high this month.                                                 |
|Social Worse	          |12.8645	   |Performance is low this month.                                                  |
|Social Approach	       |-10.2458 	   |Performance is improving, getting closer to the peer benchmark.                 |


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

# Precision feedback message generation
To generate precision feedback, MPOG sends de-identified performance and preference data to a precision feedback system that processes each provider's data with their peer comparator performance data. The precision feedback system produces and evaluates candidate messages using metadata from message templates, then selects an optimal precision feedback message to return to MPOG. The precision feedback system is a knowledge-based system that is comprised of the following parts: a knowledge base, a software pipeline, and a web service.

## Precision Feedback Knowledge Base
The knowledge base contains the following components: causal pathways, message templates, and performance measures.

## Social Worse Causal Pathway
This pathway describes the influence of feedback interventions informing the recipient that their performance is worse than that of a social comparator, such as a top performer benchmark or peer average. The causal pathway model is made up of preconditions, moderators, mechanisms, and outcomes.

### Preconditions
There are several preconditions that are necessary for the success of feedback intervention using the social worse causal pathway. They are subdivided into informational and message preconditions, and are as follows:

Information content preconditions:
1. [Social comparator content <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000095)
2. [Negative performance gap content <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000105)

Message preconditions:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045)
2. [Negative performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000116)

### Moderators
Moderators are factors that inhibit or promote the influence of the feedback intervention on the recipient. The social gain causal pathway has the following moderators:
1. `Habituation` - How many times has the recipient previously received this message in the last year?
2. `Regulatory fit` - How aligned is the message with characteristics of the behavior/task, context, and recipient personality (motivated by prevention vs. promotion mindset with regard to future outcomes)?
3. `Gap size` - How large is the gap between the recipient's performance level and that of the social comparator?

### Mechanisms
Mechanisms are factors that the intervention operates through to influence the feedback recipient. The social gain pathway has the following mechanisms:
1. `Awareness (knowledge)` - The message may change the provider's awareness of their own lagging performance relative to their peers.
2. `Subjective Norms` - Messages may influence the recipient's perception of their own performance status (below average, in this case) within their peer group.
3. `Motivation` - The message may motivate the provider to work to lose their status as a non-top-performer among their peers.

### Outcomes
The expected outcome of a successful social worse pathway intervention is clinical performance improvement.

## Message templates

Message templates represent a possible motivational message that a precision feedback system can send. There is one message template that the precision feedback system can currently access for this vignette: 

The `Not Top Performer` [<sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/not_top_performer.json) message reads:
> You are not a top performer this month for the measure [Measure name]. Your performance was [recipient performance level - percentage], below the [comparator name].

This message template `is about` [<sub>(OntoBee)</sub>](https://ontobee.org/ontology/IAO?iri=http://purl.obolibrary.org/obo/IAO_0000136) the following data features:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045) 
2. [Negative performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000116)
3. [Peer 90th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000129)
4. Display format compatability: [Line Graph <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/IAO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FIAO_0000573), [Bar Chart <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/STATO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FSTATO_0000166)

## Software Pipeline (Precision Feedback Pipeline)
**TODO**

### Recipient annotations (Bitstomach)
The first stage of the pipeline analyzes performance to identify features of performance, such as comparisons and trends that are related to motivation. The analysis from this stage results in the following annotations:

Deepas's annotations indicate the presence of the following in her performance data this month:
1. **TODO**

Eugene's annotations indicate the presence of the following in his performance data this month:
1. **TODO**


### Candidate Message Generation (Candidate Smasher)
The second stage of the pipeline creates possible messages by associating the annotations for Deepa and Eugene with each message template, so that two candidate messages are created for each person.

Deepa's candidate messages:

A. Candidate A has the following annotations:

The [**TODO**](**TODO**) message template [is about](**TODO**) the following features of performance data:
1. **TODO**

Deepa's annotations from this month:
1. **TODO**

B. Candidate B has the following annotations:

The [**TODO**](**TODO**) message template [is about] (**TODO**) the following features of performance data:
TODO

Deepa's annotations from this month:
TODO

Eugene's candidate messages:

A. Candidate A has the following annotations:

TODO

Eugene's performance is about:
TODO

B. Candidate B has the following annotations:

TODO

Eugene's performance is about:
TODO

### Candidate Message Preconditions Evaluation (Think Pudding)
TODO

### Candidate Message Moderator Evaluation and Selection (Esteemer)
TODO

### Message Generation and Delivery (Pictoralist)
TODO
