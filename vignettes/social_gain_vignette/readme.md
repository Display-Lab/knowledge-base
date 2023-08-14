# Social Gain Vignette

## Introduction
This vignette illustrates the process for creating precision feedback messages about a recipient's performance rising above a peer comparator, such as a top performer benchmark or peer average. These messages use the Social Gain Causal Pathway, which specifies feedback messages that may motivate providers by delivering information about their performance improving. Motivation from these messages can arise from the recognition of a gain of social status as a top or above-average performer. Example messages that use social gain are "you reached the top 10% `peer benchmark" and "your performance has increased above the peer average".

This vignette also contains example data and unique identifiers for the data entities that a precision feedback system uses to evaluate the potential success of a precision feedback message. An example of a unique identifier is http://purl.obolibrary.org/obo/psdo_0000126, an ID that points to a [peer average comparator](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126), defined in the [Performance Summary Display Ontology](https://github.com/Display-Lab/psdo) as an average representing the mean performance of a peer group. 

## Performance Data
Each month, MPOG receives data about operative case quality and outcomes from approximately 60 healthcare institutions. MPOG calculates performance for each provider individually, for approximately 35 performance measures of quality and outcomes. One example of these measures is [PUL-01: Protective Tidal Volume, 10 mL/kg PBW](https://spec.mpog.org/Spec/Public/4).

### Benchmark comparators
MPOG calculates performance benchmarks and averages for each institution. One comparator is a [top 10% benchmark](http://purl.obolibrary.org/obo/psdo_0000129), which represents the 90th percentile for performance among providers at an institution for a given measure. Another comparator is the [peer average](http://purl.obolibrary.org/obo/psdo_0000126), which is the mean performance for all providers at an insitution for a given measure.

### Healthcare professional performance
Chikondi, a resident physician at Max Community Hospital, has the following performance data over the last 6 months for the PUL-01 measure:

|Month|Performance Level|Peer Average|75th Percentile Benchmark|90th Percentile Benchmark|MPOG Goal|
|-----|-----------------|------------|-------------------------|-------------------------|--|
|Jul  |       85%| 85| 88| 92|90|
|Aug  |       85%| 85| 88| 92|90|
|Sept |       85%| 85| 88| 92|90|
|Oct  |       85%| 85| 88| 92|90|
|Nov  | ***85%***| 85| 88| 92|90|
|Dec  | ***91%***| 85| 88| 92|90|

Fahad, an attending pediatric anesthesiologist at Max Community Hospital, has the following performance data over the last 6 months for the PUL-01 measure:

|Month|Performance Level|Peer Average|75th Percentile Benchmark|90th Percentile Benchmark|MPOG Goal|
|-----|-----------------|------------|-------------------------|-------------------------|--|
|Jul  |       90%| 90| 92| 96|90|
|Aug  |       90%| 90| 92| 96|90|
|Sept |       90%| 90| 92| 96|90|
|Oct  |       90%| 90| 92| 96|90|
|Nov  | ***93%***| 90| 92| 96|90|
|Dec  | ***97%***| 90| 92| 96|90|

## Preference data
Preferences for precision feedback are elicited through a preference survey that providers can take. The preference survey produces a preference model for each provider that, with the provider's permission, is shared with MPOG to maintain. MPOG analyses preference data that is shared to identify population-level preference segments. These segments are generated as preference profiles that can serve as a default preference model for an organization, or which can be selected by providers who do not take the preference survey, but who identify preferences that are close enough to their own in the settings menu for the precision feedback system.

Chikondi's preference data:

|Motivating information |Utility value|Description                                                                     |
|-----------------------|-------------|--------------------------------------------------------------------------------|
|Social Gain               |11.0000     |Performance was previously low, but it has improved to reach the peer benchmark.|
|Social Stayed Better   |-6.0000        |Performance is consistently high (no recent change).                            |
|Worsening              |12.0000       |Performance is worsening.                                                       |
|Improving               |11.0000       |Performance is improving.                                                       |
|social gain             |08.0000       |Performance was previously high, but it has dropped below the peer average.     |
|Social Stayed Worse       |-9.0000    |Performance has remained below average (no recent change).                      |
|Social Better           |1.5000        |Performance is high this month.                                                 |
|Social Worse             |-3.0000     |Performance is low this month.                                                  |
|Social Approach           |02.0000        |Performance is improving, getting closer to the peer benchmark.                 |


Fahad's preference data:

|Motivating information |Utility value|Description                                                                     |
|-----------------------|-------------|--------------------------------------------------------------------------------|
|Social Gain               |-8.1654     |Performance was previously low, but it has improved to reach the peer benchmark.|
|Social Stayed Better   |-6.2514        |Performance is consistently high (no recent change).                            |
|Worsening              |11.5498       |Performance is worsening.                                                       |
|Improving               |-5.2654       |Performance is improving.                                                       |
|social gain             |12.1369       |Performance was previously high, but it has dropped below the peer average.     |
|Social Stayed Worse       |09.8987    |Performance has remained below average (no recent change).                      |
|Social Better           |01.5484       |Performance is high this month.                                                 |
|Social Worse             |10.5656     |Performance is low this month.                                                  |
|Social Approach           |-10.2541       |Performance is improving, getting closer to the peer benchmark.                 |

# Precision feedback message generation
To generate precision feedback, MPOG sends de-identified performance and preference data to a precision feedback system that processes each provider's data with their peer comparator performance data. The precision feedback system produces and evaluates candidate messages using metadata from message templates, then selects an optimal precision feedback message to return to MPOG. The precision feedback system is a knowledge-based system that is comprised of the following parts: a knowledge base, a software pipeline, and a web service.

## Precision Feedback Knowledge Base
The knowledge base contains the following components: causal pathways, message templates, and performance measures.

## Social Gain Causal Pathway
This pathway describes the influence of feedback interventions informing the recipient that their performance has become better than that of a social comparator, such as a top performer benchmark or peer average. The causal pathway model is made up of preconditions, moderators, mechanisms, and outcomes.

### Preconditions
Preconditions for social gain are factors necessary for the success of the precision feedback intervention using this pathway. The social gain pathway has the following preconditions:
Information content preconditions:
1. [Social comparator content <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000095)
2. [Positive performance gap content <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000104)
3. [Positive performance trend content <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000099)
4. [Achievement content <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000112)

Message preconditions:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045)
2. [Positive performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000117)
3. [Positive performance trend set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)
4. [Achievement set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000121)
 
### Moderators
Moderators are factors that inhibit or promote the influence of the feedback intervention on the recipient. The social gain causal pathway has the following moderators:
1. `Message recency` - The number of months since this message was delivered previously.
2. `Message delivery count` - How many times has the recipient previously received this message in the last year?  
3. `Regulatory fit` - To what extent is the message aligned to the behavior/task's characteristics, context, and recipient personality (motivated by bad outcome prevention vs. good outcome promotion).
4. `Gap size` - How large is the gap between the recipient's performance level and that of the social comparator?
5. `Slope of trend` - Derivative of the performance measure in the time domain
6. `Time since last loss` - Time in months since the last "loss" event

### Mechanisms
Mechanisms are factors that the intervention operates through to influence the feedback recipient. The social gain pathway has the following mechanisms:
1. `Awareness (knowledge)` - The message may change the recipient's awareness of their newfound or increased high performance relative to their peers.
2. `Subjective norms` - The message may influence the recipient by creating or reinforcing their perception of their newfound top-performer status within their peer group.
3. `Motivation` - The message may motivate the recipient to work to maintain their new status as a top performer.


### Outcomes
A successful precision feedback intervention leveraging the social gain pathway should increase clinical process performance improvement.

## Message templates
Message templates represent possible motivational messages that a precision feedback system can send. There are three message templates that the precision feedback system can access for this vignette: 

The `Achieved top 10% peer benchmark` [<sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/achieved_top_10_peer_benchmark.json) message reads:
> You reached the top 10% peer benchmark this month for the measure [Measure name].

This message template `is about` [<sub>(OntoBee)</sub>](https://ontobee.org/ontology/IAO?iri=http://purl.obolibrary.org/obo/IAO_0000136) the following data features:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045)
2. [Positive performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000117)
3. [Positive performance trend set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)
4. [Achievement set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000121)
5. [Peer 90th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000129)
6. Display format compatability: `Line Graph` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/IAO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FIAO_0000573), `Bar Chart` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/STATO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FSTATO_0000166)

The `Achieved top 25% peer benchmark` [<sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/achieved_top_25_peer_benchmark.json) message reads:
> You reached the top 25% peer benchmark this month for the measure [Measure name].

This message template `is about` [<sub>(OntoBee)</sub>](https://ontobee.org/ontology/IAO?iri=http://purl.obolibrary.org/obo/IAO_0000136) the following data features:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045)
2. [Positive performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000117)
3. [Positive performance trend set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)
4. [Achievement set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000121)
5. [Peer 75th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000128)
6. Display format compatability: `Line Graph` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/IAO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FIAO_0000573), `Bar Chart` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/STATO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FSTATO_0000166)

The `Achieved peer average` [<sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/achieved_peer_average.json) message reads:
> Your performance is above the peer average this month for the measure [Measure name].

This message template `is about` [<sub>(OntoBee)</sub>](https://ontobee.org/ontology/IAO?iri=http://purl.obolibrary.org/obo/IAO_0000136) the following data features:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045)
2. [Positive performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000117)
3. [Positive performance trend set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)
4. [Achievement set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000121)
5. [Peer average comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126)
6. Display format compatability: `Line Graph` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/IAO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FIAO_0000573), `Bar Chart` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/STATO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FSTATO_0000166)
## Software Pipeline (Precision Feedback Pipeline)
### Recipient annotation generation (Bitstomach)
The first stage of the pipeline is a script called Bitstomach. This script analyzes recipient's performance data and generates features called **annotations**. These annotations describe features of the performance data such as performance trends over time, or how performance measures relate to other values like peer performance benchmarks and institutional performance goals.

**Annotations for Chikondi's performance data for the most recent month:**
1. `Social comparator content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000095)
2. `Positive performance trend content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000099)
3. `Negative performance gap content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000105)
    - *with respect to* [Peer 90th percentile comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000129)
4. `Positive performance gap content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000104) 
    - *with respect to* [Peer average comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126)
    - *with respect to* [Peer 75th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000128)
    - *with respect to* [Goal comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000046)
5. `Achievement content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000112) 
    - *with respect to* [Peer 75th percentile comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000128)


**Annotations for Fahad's performance data for the most recent month:**
1. `Social comparator content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000095)
2. `Positive performance trend content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000099)
3. `Positive performance gap content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000104)
    - *with respect to* [Peer 90th percentile comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000129)
    - *with respect to* [Peer 75th percentile comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000128)
    - *with respect to* [Peer average comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126)
    - *with respect to* [Goal comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000046)
4. `Achievement content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000112) 
    - *with respect to* [Peer 90th percentile comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000129)

### Candidate Message Generation (Candidate Smasher)
The second stage of the pipeline creates two candidate messages that may be appropriate for each recipient to recieve. It does this by searching through the message template library and selecting two message templates with annotations that match those annotations of the recipient's performance.

**Chikondi's candidate messages (A & B):**

**Candidate Message A** is the `Achieved top 10% peer benchmark` [<sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/achieved_top_10_peer_benchmark.json) message template, which has the following annotations *in common* with the recipient's performance annotations:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045)
2. [Positive performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000117)
3. [Positive performance trend set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)
4. [Achievement set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000121)
5. ~~[Peer 90th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000129)~~

**Candidate Message B** is the `Achieved top 25% peer benchmark` [<sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/achieved_top_25_peer_benchmark.json) message template, which has the following annotations *in common* with the recipient's performance annotations:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045)
2. [Positive performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000117)
3. [Positive performance trend set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)
4. [Achievement set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000121)
5. [Peer 75th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000128)

Both candidate messages have annotations matching those generated from Chikondi's performance data, and are therefore appropriate as candidate messages.

**Fahad's candidate messages (α & β):**

**Candidate Message α**  is the `Achieved top 10% peer benchmark` [<sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/achieved_top_10_peer_benchmark.json) message template, which has the following annotations *in common* with the recipient's performance annotations:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045)
2. [Positive performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000117)
3. [Positive performance trend set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)
4. [Achievement set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000121)
5. [Peer 90th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000129)

**Candidate Message β** is the `Achieved top 25% peer benchmark` [<sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/achieved_top_25_peer_benchmark.json) message template, which has the following annotations *in common* with the recipient's performance annotations:
1. [Social comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000045)
2. [Positive performance gap set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000117)
3. [Positive performance trend set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)
4. [Achievement set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000121)
5. ~~[Peer 75th percentile benchmark <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000128)~~

Both candidate messages have annotations matching those generated from Fahad's performance data, and are therefore appropriate as candidate messages.

### Candidate Message Preconditions Evaluation (ThinkPudding)
The third stage of the pipeline processes and evaluates the candidate messages for each persona based on preconditions. It compares the annotations associated with the message candidates and checks them against the persona's performance data annotations to determine which candidate messages are acceptable based on message preconditions.

For Chikondi, **Candidate B** is acceptable by the causal pathway **social gain**.

For Fahad, **Candidate α** is acceptable by the causal pathway **social gain**.


### Candidate Message Moderator Evaluation and Selection (Esteemer)
The fourth stage of the pipeline ranks the candidate messages based on a number of moderators in order to determine the most appropriate message to provide to the feedback recipient. The script does this by evaluating message candidates against a number of factors: recency of the recipient having recieved a similar message, gap size, slope of the trend in the performance data, time since last loss or achievement, the recipient's feedback preferences, and the acceptability of the candidate message based on preconditions (ThinkPudding acceptability).

**For Chikondi, Esteemer uses the following information:**
- The acceptable candidate message is **Candidate B**
- Chikondi's preference for social gain messages is *Todo*
- Chikondi has not recieved the **Candidate B** message recently. 
> ∴ Esteemer will select **Candidate B** as the most appropriate message to provide the recipient.

**For Fahad, Esteemer uses the following information:**
- The acceptable candidate message is **Candidate α**
- Fahad's preference for social gain messages is *Todo*
- Fahad has not recieved the **Candidate α** message recently.
> ∴ Esteemer will select **Candidate α** as the most appropriate message to provide the recipient. 

For each of the selected messages, Eseemer will return the template ID, message text, comparator type, acceptability relationship, measure name, title, and display type preferred by the recipient. This data is used in the next step of the pipeline to generate the precision feedback message.

### Message Generation and Delivery (Pictoralist)
The fifth and final stage of the pipeline generates visual representations of the selected message based on the recipient's performance data, and sends this output off for delivery to the recipient.
The script takes in the selected message and performance data of the recipient as inputs. It then uses the recipient's display preferences to generate a figure that visualize's the reciepients performance over time related to the given measure and causal pathway. It returns the figure as an image encoded as a base64 string, alongside other elements of the precision feedback message. The precision feedback email is then created using this figure, the necessary text data, and is then sent to the recipient.
