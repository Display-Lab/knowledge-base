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
|-|-|-|-|-|-|
|Jul  |      85%|  85| 88| 92|90|
|Aug  |      85%|  85| 88| 92|90|
|Sept |      85%|  85| 88| 92|90|
|Oct  |      85%|  85| 88| 92|90|
|Nov  |***83%***|  85| 88| 92|90|
|Dec  |***89%***|  85| 88| 92|90|

## Preference data
Preferences for precision feedback are elicited through a preference survey that providers can take. The preference survey produces a preference model for each provider that, with the provider's permission, is shared with MPOG to maintain. MPOG analyses preference data that is shared to identify population-level preference segments. These segments are generated as preference profiles that can serve as a default preference model for an organization, or which can be selected by providers who do not take the preference survey, but who identify preferences that are close enough to their own in the settings menu for the precision feedback system.

Alice's preference data:
|Motivating information |Utility value|Description                                                                     |
|-----------------------|-------------|--------------------------------------------------------------------------------|
|Social better	           |-2    |Performance was previously low, but it has improved to reach the peer benchmark.|
|Social gain   |13	    |Performance is consistently high (no recent change).                            |
|Worsening             	|-22	   |Performance is worsening.                                                       |
|Improving	             |3    |Performance is improving.                                                       |
|Social loss             |10	    |Performance was previously high, but it has dropped below the peer average.     |
|Social worse     |-15     |Performance is low this month.                                                         |
|Social stayed worse	   |-8   |Performance has remained below average (no recent change).                      |
|Social approach	         |15	    |Performance is high this month.                                     |
|Goal gain         |13	   |Performance is low this month.                                                  |
|Goal loss	       |10	   |Performance is improving, getting closer to the peer benchmark.                 |
|Goal approach   |14    |                                                                                    |


Gaile's preference data:

|Motivating information |Utility value|Description                                                                     |
|-----------------------|-------------|--------------------------------------------------------------------------------|
|social better	           |xx.xxxxx	    |Performance was previously low, but it has improved to reach the peer benchmark.|
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
1. `Message recency` - The number of months since this message was delivered previously.
2. `Message delivery count` - How many times has the recipient previously received this message in the last year?  
3. `Regulatory fit` - To what extent is this message aligned with characteristics of the behavior/task, context, and recipient personality, with regard to motivation to avoid negative outcomes / problem (prevention focus), or motivation to achieve positive outcomes / develop and learn (promotion focus)?
4. `Gap size` - How large is the gap between the recipient's performance level and that of the social comparator?

### Mechanisms
Mechanisms are factors that the intervention operates through to influence the feedback recipient. Adapted from [Carey et. al. 2019](https://doi.org/10.1093/abm/kay078). The social better pathway has the following mechanisms:
1. `Awareness (knowledge)` - The message may change the recipient's awareness of their high performance, relative to peers.
2. `Subjective norms` - The message may influence the recipient by creating or reinforcing their perception of their own high-performer status within their peer group.
3. `Motivation` - The message may influence the recipient to maintain their status as a top performer for a given measure.

### Outcomes
The expected outcome of the successful influence of an email that uses the social better pathway is clinical process performance improvement or sustainment.


## Message templates
Message templates represent a possible motivational message that a precision feedback system can send. There are two message templates that the precision feedback system can currently access for this vignette:

The `Top Performer`[ <sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/top_performer.json) message:
> You are a top performer this month for the measure [Measure name]. Your performance was [recipient performance level - percentage], above the [comparator name].

This message template `is about` [<sub>(OntoBee)</sub>](https://ontobee.org/ontology/IAO?iri=http://purl.obolibrary.org/obo/IAO_0000136) the following data features:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045) 
2. [Positive performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000117)
3. [Peer 90th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000129)
4. Display format compatability: [Line Graph <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/IAO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FIAO_0000573), [Bar Chart <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/STATO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FSTATO_0000166)

The `In Top 25%`[ <sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/knowledgebase-description-edit/message_templates/in_top_25%25.json) message:
> You are in the top 25% of providers for the measure [Measure name]. Your performance was [recipient performance level as percentage (with numerator and denominator)], above the top 25% peer benchmark, which was X% this month. 

This message template `is about` [<sub>(OntoBee)</sub>](https://ontobee.org/ontology/IAO?iri=http://purl.obolibrary.org/obo/IAO_0000136) the following data features:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045) 
2. [Positive performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000117)
3. [Peer 75th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000128)
4. Display format compatability: [Line Graph <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/IAO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FIAO_0000573), [Bar Chart <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/STATO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FSTATO_0000166)

## Software Pipeline (Precision Feedback Pipeline)
### Recipient annotation generation (Bitstomach)
The first stage of the pipeline is a script called Bitstomach. This script analyzes recipient's performance data and generates features called **annotations**. These annotations describe features of the performance data such as performance trends over time, or how performance measures relate to other values like peer performance benchmarks and institutional performance goals.

**Annotations for Alice's performance data for the most recent month:**
1. `Social comparator content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000095)
2. `Positive performance trend content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000099)
3. `Positive performance gap content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000104) 
    - *with respect to* [Peer average comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126)
    - *with respect to* [Peer 75th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000128)
    - *with respect to* [Peer 90th percentile comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000129)
    - *with respect to* [Goal comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000046) 
4. `Achievement content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000112) 
    - *with respect to* [Peer average comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126)
    - *with respect to* [Peer 75th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000128)
    - *with respect to* [Peer 90th percentile comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000129)
    - *with respect to* [Goal comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000046) 

**Annotations for Gaile's performance data for the most recent month:**
1. `Social comparator content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000095)
2. `Positive performance trend content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000099)
3. `Positive performance gap content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000104)
	+ *with respect to* [Peer average comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126)
	+ *with respect to* [Peer 75th percentile comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000128)
3. `Negative performance gap content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000105)
	- *with respect to* [Peer 90th percentile comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000129)
	- *with respect to* [Goal comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000046)
4. `Achievement content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000112) 
	- *with respect to* [Peer average comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126)
	- *with respect to* [Peer 75th percentile comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000128)

### Candidate Message Generation (Candidate Smasher)
The second stage of the pipeline creates two candidate messages that may be appropriate for each recipient to recieve. It does this by searching through the message template library and selecting two message templates (if two or more message templates exist) with annotations that match those annotations of the recipient's performance.

**Alice's candidate messages (A & B):**

**Candidate Message A** is the `Top Performer`[ <sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/top_performer.json) message template, which has the following annotations *in common* with the recipient's performance annotations:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045)
2. [Positive performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000117)
3. [Achievement set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000121)
4. [Peer 90th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000129)

**Candidate Message B** is the `In Top 25%`[ <sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/knowledgebase-description-edit/message_templates/in_top_25%25.json) message template, which has the following annotations *in common* with the recipient's performance annotations:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045)
2. [Positive performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000117)
3. [Achievement set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000121)
4. ~~[Peer 75th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000128)~~

Both candidate messages have annotations matching those generated from Alice's performance data, and are therefore appropriate as candidate messages.

**Gaile's candidate messages (α & β):**

**Candidate Message α** is the `Top Performer`[ <sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/top_performer.json) message template, which has the following annotations *in common* with the recipient's performance annotations:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045)
2. [Positive performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000117)
3. [Achievement set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000121)
4. ~~[Peer 90th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000129)~~

**Candidate Message β** is the `In Top 25%`[ <sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/knowledgebase-description-edit/message_templates/in_top_25%25.json) message template, which has the following annotations *in common* with the recipient's performance annotations:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045)
2. [Positive performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000117)
3. [Achievement set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000121)
4. [Peer 75th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000128)

Both candidate messages have annotations matching those generated from Gaile's performance data, and are therefore appropriate as candidate messages.

### Candidate Message Preconditions Evaluation (ThinkPudding)
The third stage of the pipeline processes and evaluates the candidate messages for each persona based on preconditions. It compares the annotations associated with the message candidates and checks them against the persona's performance data annotations to determine which candidate messages are acceptable based on message preconditions.

For Alice, **Candidate A** is acceptable by the causal pathway **social better**.

For Gaile, **Candidate β** is acceptable by the causal pathway **social better**.

### Candidate Message Moderator Evaluation and Selection (Esteemer)
The fourth stage of the pipeline ranks the candidate messages based on a number of moderators in order to determine the most appropriate message to provide to the feedback recipient. The script does this by evaluating message candidates against a number of factors: recency of the recipient having recieved a similar message, gap size, slope of the trend in the performance data, time since last loss or achievement, the recipient's feedback preferences, and the acceptability of the candidate message based on preconditions (ThinkPudding acceptability).

**For Alice, Esteemer uses the following information:**
- The acceptable candidate message is **Candidate A**
- Alice's preference for social better messages is *Todo*
- Alice has not recieved the **Candidate A** message recently. 

> ∴ Esteemer will select **Candidate A** as the most appropriate message to provide the recipient.

**For Gaile, Esteemer uses the following information:**
- The acceptable candidate message is **Candidate β**
- Gaile's preference for social better messages is *Todo*
- Gaile has not recieved the **Candidate β** message recently.
> ∴ Esteemer will select **Candidate β** as the most appropriate message to provide the recipient. 

For each of the selected messages, Eseemer will return the template ID, message text, comparator type, acceptability relationship, measure name, title, and display type preferred by the recipient. This data is used in the next step of the pipeline to generate the precision feedback message.

### Message Generation and Delivery (Pictoralist)
The fifth and final stage of the pipeline generates visual representations of the selected message based on the recipient's performance data, and sends this output off for delivery to the recipient.
The script takes in the selected message and performance data of the recipient as inputs. It then uses the recipient's display preferences to generate a figure that visualize's the reciepients performance over time related to the given measure and causal pathway. It returns the figure as an image encoded as a base64 string, alongside other elements of the precision feedback message. The precision feedback email is then created using this figure, the necessary text data, and is then sent to the recipient.
