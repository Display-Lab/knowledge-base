# Social Approach Vignette
## Introduction
This vignette illustrates the process for creating precision feedback messages about a recipient's performance approaching an explicit target, such as a top performer benchmark or peer average. These messages use the *social approach causal pathway*, which specifies feedback messages that may motivate providers by delivering information about their performance nearing a benchmark. Example messages that use social approach are "your performance is approaching the peer average this month for the measure GLU-01" and "your performance is approaching the peer 90th percentile benchmark this month for the measure ABX-01-OB".

This vignette also contains examples of data features and other entities that a precision feedback system uses to evaluate the potential success of a precision feedback message. An example of such an entity is a [peer average comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126), which is defined in the [Performance Summary Display Ontology <sub>(GH)</sub>](https://github.com/Display-Lab/psdo) as an average representing the mean performance of a peer group. 

## Performance Data
Each month, MPOG receives data about operative case quality and outcomes from approximately 60 healthcare institutions. MPOG calculates performance for each provider individually, for approximately 35 performance measures of quality and outcomes. One example of these measures is [FLUID-01-NC: Minimizing Colloid Use (Non-Cardiac) <sub>(MPOG)</sub>](https://spec.mpog.org/Spec/Public/15).

### Benchmark comparators
MPOG calculates performance benchmarks and averages for each institution. One comparator is a [peer 90th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000129), which represents the 90th percentile for performance among providers at an institution, for each measure. Another is the [peer average comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126), which is the mean performance for all providers at an insitution, for each measure.

### Healthcare professional performance
Bob, a nurse anesthetist (CRNA) at Max Commuity Hospital, has the following performance data over the last 6 months for the FLUID-01-NC measure:

|Month|Performance Level|Top 10% Benchmark|Peer Average|
|-----|-----------------|-----------------|------------|
|Oct  |              84%|               90|          85|
|Nov  |              85%|               92|          86|
|Dec  |              85%|               93|          87|
|Jan  |              83%|               92|          86|
|Feb  |              81%|               92|          86|
|Mar  |              83%|               91|          85|

Deepa, another CRNA at Midwest Medicine, a medical-school affiliated hospital, has the following performance data over the last 6 months for the FLUID-01-NC measure:

|Month|Performance Level|Top 10% Benchmark|Peer Average|
|-----|-----------------|-----------------|------------|
|Oct  |              83%|               93|          85|
|Nov  |              84%|               95|          87|
|Dec  |              85%|               93|          85|
|Jan  |              84%|               92|          88|
|Feb  |              84%|               93|          87|
|Mar  |              85%|               91|          86|

## Preference data
Preferences for precision feedback are elicited through a preference survey that providers can take. The preference survey produces a preference model for each provider that, with the provider's permission, is shared with MPOG to maintain. MPOG analyses preferences data that is shared to identify population-level preference segments. These are generates as preference profiles that can serve as a default preference model for an organization, or which can be selected by providers who do not take the preference survey, but who identify preferences that are close enough to their own in the settings menu for the precision feedback system.

Bob's preference data:

|Motivating information |Utility value|Description                                                                     |
|-----------------------|-------------|--------------------------------------------------------------------------------|
|Social Gain	           |11.0000	    |Performance was previously low, but it has improved to reach the peer benchmark.|
|Social Stayed Better   |-6.0000	    |Performance is consistently high (no recent change).                            |
|Worsening             	|12.0000	   |Performance is worsening.                                                       |
|Improving	             |11.0000	    |Performance is improving.                                                       |
|Social Loss             |08.0000	    |Performance was previously high, but it has dropped below the peer average.     |
|Social Stayed Worse	   |-9.0000	   |Performance has remained below average (no recent change).                      |
|Social Better	         |1.5000	    |Performance is high this month.                                                 |
|Social Worse	          |-3.0000	   |Performance is low this month.                                                  |
|Social Approach	       |02.0000 	   |Performance is improving, getting closer to the peer benchmark.                 |


Deepa's preference data:

|Motivating information |Utility value|Description                                                                     |
|-----------------------|-------------|--------------------------------------------------------------------------------|
|Social Gain	           |-8.1654	    |Performance was previously low, but it has improved to reach the peer benchmark.|
|Social Stayed Better   |-6.2514	    |Performance is consistently high (no recent change).                            |
|Worsening             	|11.5498	   |Performance is worsening.                                                       |
|Improving	             |-5.2654	    |Performance is improving.                                                       |
|Social Loss             |12.1369	    |Performance was previously high, but it has dropped below the peer average.     |
|Social Stayed Worse	   |09.8987	   |Performance has remained below average (no recent change).                      |
|Social Better	         |01.5484	    |Performance is high this month.                                                 |
|Social Worse	          |10.5656	   |Performance is low this month.                                                  |
|Social Approach	       |-10.2541	   |Performance is improving, getting closer to the peer benchmark.                 |

# Precision feedback message generation
To generate precision feedback, MPOG sends de-identified performance and preference data to a precision feedback system that processes each provider's data with their peer comparator performance data. The precision feedback system produces and evaluates candidate messages using metadata from message templates, then selects an optimal precision feedback message to return to MPOG. The precision feedback system is a knowledge-based system that is comprised of the following parts: a knowledge base, a software pipeline, and a web service.

## Precision Feedback Knowledge Base
The knowledge base contains the following components: causal pathways, message templates, and performance measures.

## Social Approach Causal Pathway
This pathway describes the influence of feedback interventions informing the recipient that their performance is approaching that of a social comparator, such as a top performer benchmark or peer average. The causal pathway model is made up of preconditions, moderators, mechanisms, and outcomes.

### Preconditions
Preconditions are factors necessary for the success of a social approach precision feedback itervention. The social approach causal pathway has the following preconditions:

Information content preconditions:
1. [Social comparator content <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000095)
2. [Negative performance gap content <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000105)
3. [positive performance trend content <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000099)

Message preconditions:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045)
2. [Negative performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000116)
3. [Positive performance trend set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)
 
### Moderators
Moderators are factors that inhibit or promote the influence of the feedback intervention on the recipient. The social approach causal pathway has the following moderators:
1. `Habituation` - How many times has the recipient previously received this message in the last year?
2. `Regulatory fit` - To what extent is the message aligned to the behavior/task's characteristics, context, and recipient personality (motivated by bad outcome prevention vs. good outcome promotion).
3. `Gap size` - How large is the gap between the recipient's performance level and that of the social comparator?
4. `Slope of trend` - Derivative of the performance measure in the time domain

### Mechanisms
Mechanisms are factors that the intervention operates through to influence the feedback recipient. The social approach pathway has the following mechanisms:
1. `Awareness (knowledge)` - The message may change the recipient's awareness of their performance increasing and nearing a high performance benchmark relative to their peers.
2. `Subjective norms` - The message may influence the recipient by creating or reinforcing their proximity to top/high-performer status within their peer group.
3. `Motivation` - The message may motivate the recipient to keep up their recent performance increase to reach new social status.
4. `Optimism` - *WIP* The message may influence the recipient to continue to be optimistic about their ability to improve their performance.

### Outcomes
A successful precision feedback intervention leveraging the social approach pathway should increase clinical process performance improvement.

## Message templates
Message templates represent possible motivational messages that a precision feedback system can send. There are three message templates that the precision feedback system can access for this vignette: 

The `Approach Top 10 Peer Benchmark`[<sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/drop_below_peer_average.json) message reads as follows:
> Your performance is approaching the top 10% peer benchmark this month for the measure [Measure name].

This message template [[is about] <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/IAO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FIAO_0000136) the following data features:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045) 
2. [Negative performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000116)
3. [Positive performance trend set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)
4. [Peer 90th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126)
5. Display format compatability: [Line Graph <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/IAO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FIAO_0000573), [Bar Chart <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/STATO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FSTATO_0000166)

The `Approach Top 25 Peer Benchmark`[<sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/approach_top_25_peer_benchmark.json) message reads as follows:
> Your performance is approaching the top 25% peer benchmark this month for the measure [Measure name].

This message template [[is about] <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/IAO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FIAO_0000136) the following data features:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045) 
2. [Negative performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000116)
3. [Positive performance trend set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)
4. [Peer 75th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000129)

The `Approach Peer Average` [<sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/approach_peer_average.json) message reads as follows:
> Your performance is approaching the peer average this month for the measure [Measure name].

This message template [[is about] <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/IAO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FIAO_0000136) the following data features:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045) 
2. [Negative performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000116)
3. [Positive performance trend set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)
4. [Peer average comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126)

## Software Pipeline (Precision Feedback Pipeline)
**TODO**

### Recipient annotations (Bitstomach)
The first stage of the pipeline analyzes performance to identify features of performance, such as comparisons and trends that are related to motivation. The analysis from this stage results in the following annotations:

Bobs's annotations indicate the presence of the following in her performance data this month:
1. **TODO**

Deepa's annotations indicate the presence of the following in his performance data this month:
1. **TODO**


### Candidate Message Generation (Candidate Smasher)
The second stage of the pipeline creates possible messages by associating the annotations for Bob and Deepa with each message template, so that two candidate messages are created for each person.

Bob's candidate messages:

A. Candidate A has the following annotations:

The [**TODO**](**TODO**) message template [is about](**TODO**) the following features of performance data:
1. **TODO**

Bob's annotations from this month:
1. **TODO**

B. Candidate B has the following annotations:

The [**TODO**](**TODO**) message template [is about] (**TODO**) the following features of performance data:
TODO

Bob's annotations from this month:
TODO

Deepa's candidate messages:

A. Candidate A has the following annotations:

TODO

Deepa's performance is about:
TODO

B. Candidate B has the following annotations:

TODO

Deepa's performance is about:
TODO

### Candidate Message Preconditions Evaluation (Think Pudding)
TODO

### Candidate Message Moderator Evaluation and Selection (Esteemer)
TODO

### Message Generation and Delivery (Pictoralist)
TODO

