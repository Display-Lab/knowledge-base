# Social Approach Vignette

## Introduction
This vignette illustrates the process for creating precision feedback messages about a recipient's performance approaching an explicit target, such as a top performer benchmark or peer average. These messages use the Social Approach Causal Pathway, which specifies feedback messages that may motivate providers by delivering information about their performance improving. Motivation from these messages can arise from the recognition of their work improving and near-future gain of social status as a top or above-average performer [*todo* needs work]. Example messages that use social approach are "your performance is approaching the peer average this month for the measure GLU-01" and "your performance is approaching the peer 10% benchmark this month for the measure ABX-01-OB".

This vignette also contains example data and unique identifiers for the data entities that a precision feedback system uses to evaluate the potential success of a precision feedback message. An example of a unique identifier is http://purl.obolibrary.org/obo/psdo_0000126, an ID that points to a [peer average comparator](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126), defined in the [Performance Summary Display Ontology](https://github.com/Display-Lab/psdo) as an average representing the mean performance of a peer group. 

## Performance Data
Each month, MPOG receives data about operative case quality and outcomes from approximately 60 healthcare institutions. MPOG calculates performance for each provider individually, for approximately 35 performance measures of quality and outcomes. One example of these measures is [FLUID-01-NC: Minimizing Colloid Use (Non-Cardiac)](https://spec.mpog.org/Spec/Public/15).

### Benchmark comparators
MPOG calculates performance benchmarks and averages for each institution. One comparator is a [top 10% benchmark](http://purl.obolibrary.org/obo/psdo_0000129), which represents the 90th percentile for performance among providers at an institution for a given measure. Another comparator is the [peer average](http://purl.obolibrary.org/obo/psdo_0000126), which is the mean performance for all providers at an insitution for a given measure.

### Healthcare professional performance
Eugene, a resident anesthesiologist at Midwest Medicine Hospital, has the following performance data over the last 6 months for the FLUID-01-NC measure:

|Month|Performance Level|Top 10% Benchmark|Peer Average|
|-----|-----------------|-----------------|------------|
|Oct  |              xx%|               xx|          xx|
|Nov  |              85%|               95|          87|
|Dec  |              85%|               93|          85|
|Jan  |              87%|               96|          88|
|Feb  |              88%|               97|          87|
|Mar  |              91%|               95|          86|

Gaile, another resident physician anesthesiologist at Midwest Medicine, has the following performance data over the last 6 months for the FLUID-01-NC measure:

|Month|Performance Level|Top 10% Benchmark|Peer Average|
|-----|-----------------|-----------------|------------|
|Oct  |              xx%|               xx|          xx|
|Nov  |              95%|               95|          87|
|Dec  |              94%|               93|          85|
|Jan  |              92%|               96|          88|
|Feb  |              94%|               97|          87|
|Mar  |              97%|               95|          86|

## Preference data
Eugene's preference data:

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


Gaile's preference data:

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
Preconditions for social approach are factors necessary for the success of the precision feedback intervention using this pathway. The social approach causal pathway has the following preconditions:

Information content preconditions:
1. [Negative performance gap content](http://purl.obolibrary.org/obo/PSDO_0000105) - prefixIRI PSDO:0000105
2. [Social comparator content](http://purl.obolibrary.org/obo/psdo_0000095) - prefixIRI PSDO:0000095
3. [Positive performance trend content](http://purl.obolibrary.org/obo/PSDO_0000099) - prefixIRI PSDO:0000099

Message preconditions:
1. [Negative performance gap set](http://purl.obolibrary.org/obo/PSDO_0000116) - prefixIRI PSDO:0000116
2. [Social comparator set](http://purl.obolibrary.org/obo/PSDO_0000045) - prefixIRI PSDO:0000045
3. [Positive performance trend set](http://purl.obolibrary.org/obo/PSDO_0000120) - prefixIRI PSDO:0000120
 
### Moderators
Moderators are factors that inhibit or promote the influence of the feedback intervention on the recipient. The social approach causal pathway has the following moderators:
1. **Habituation** - How many times has the recipient previously received this message in the last year?
2. **Regulatory fit** - To what extent is the message aligned to the behavior/task's characteristics, context, and recipient personality (motivated by bad outcome prevention vs. good outcome promotion).
3. **Gap size** - How large is the gap between the recipient's performance level and that of the social comparator?
4. **Slope of trend** - Derivative of the performance measure in the time domain

### Mechanisms - WIP/todo
Mechanisms are factors that the intervention operates through to influence the feedback recipient. The social approach pathway has the following mechanisms:
1. **Awareness (knowledge)** - The message may change the recipient's awareness of their performance increasing and nearing a high performance benchmark relative to their peers.
2. **Subjective norms** - The message may influence the recipient by creating or reinforcing their proximity to top-performer status within their peer group.
3. **Optimism** - *todo- approve* The message may motivate the recipient by reinforcing that their recent effort to improve is paying off, and that they are close to recieving new social status.
4. **Motivation** - The message may motivate the recipient to work to cross the threshold with further improvement and gain new status as a top performer.


### Outcomes
A successful precision feedback intervention leveraging the social approach pathway should increase clinical process performance improvement.

## Message templates
Message templates represent possible motivational messages that a precision feedback system can send. There are three message templates that the precision feedback system can access for this vignette: 

**[Approach Top 10 Peer Benchmark](https://i.imgur.com/I1EeK7L.jpeg)** <sub>Todo - JSON template in Github, link here</sub> message:
> Your performance is approaching the top 10% peer benchmark this month for the measure [Measure name].

This message template [[is about]](http://purl.obolibrary.org/obo/IAO_0000136) the following data features:
1. [Negative performance gap set](http://purl.obolibrary.org/obo/PSDO_0000116)
2. [Social comparator element](http://purl.obolibrary.org/obo/PSDO_0000045)
3. [Positive performance trend set](http://purl.obolibrary.org/obo/PSDO_0000120)
4. [Peer 90th percentile benchmark](http://purl.obolibrary.org/obo/PSDO_0000129)

**[Approach Top 25 Peer Benchmark](https://i.imgur.com/I1EeK7L.jpeg)** <sub>Todo - JSON template in Github, link here</sub> message:
> Your performance is approaching the top 25% peer benchmark this month for the measure [Measure name].

This message template [[is about]](http://purl.obolibrary.org/obo/IAO_0000136) the following data features:
1. [Negative performance gap set](http://purl.obolibrary.org/obo/PSDO_0000116)
2. [Social comparator element](http://purl.obolibrary.org/obo/PSDO_0000045)
3. [Positive performance trend set](http://purl.obolibrary.org/obo/PSDO_0000120)
4. [Peer 75th percentile benchmark](http://purl.obolibrary.org/obo/PSDO_0000128)

**[Approach Peer Average](https://cedar.metadatacenter.org/dashboard?folderId=https:%2F%2Frepo.metadatacenter.org%2Ffolders%2Fe07ec526-60ca-486d-b8ae-b1522ae676b8)** <sub>Todo - JSON template in Github, link here</sub> message:
> Your performance is approaching the peer average this month for the measure [Measure name].

This message template [[is about]](http://purl.obolibrary.org/obo/IAO_0000136) the following data features:
1. [Negative performance gap set](http://purl.obolibrary.org/obo/PSDO_0000116)
2. [Social comparator element](http://purl.obolibrary.org/obo/PSDO_0000045)
3. [Positive performance trend set](http://purl.obolibrary.org/obo/PSDO_0000120)
4. [Peer average comparator](http://purl.obolibrary.org/obo/PSDO_0000126)

## Software Pipeline (Precision Feedback Pipeline)
**TODO**

### Recipient annotations (Bitstomach)
The first stage of the pipeline analyzes performance to identify features of performance, such as comparisons and trends that are related to motivation. The analysis from this stage results in the following annotations:

Eugenes's annotations indicate the presence of the following in her performance data this month:
1. **TODO**

Gaile's annotations indicate the presence of the following in his performance data this month:
1. **TODO**


### Candidate Message Generation (Candidate Smasher)
The second stage of the pipeline creates possible messages by associating the annotations for Eugene and Gaile with each message template, so that two candidate messages are created for each person.

Eugene's candidate messages:

A. Candidate A has the following annotations:

The [**TODO**](**TODO**) message template [is about](**TODO**) the following features of performance data:
1. **TODO**

Eugene's annotations from this month:
1. **TODO**

B. Candidate B has the following annotations:

The [**TODO**](**TODO**) message template [is about] (**TODO**) the following features of performance data:
TODO

Eugene's annotations from this month:
TODO

Gaile's candidate messages:

A. Candidate A has the following annotations:

TODO

Gaile's performance is about:
TODO

B. Candidate B has the following annotations:

TODO

Gaile's performance is about:
TODO

### Candidate Message Preconditions Evaluation (Think Pudding)
TODO

### Candidate Message Moderator Evaluation and Selection (Esteemer)
TODO

### Message Generation and Delivery (Pictoralist)
TODO

