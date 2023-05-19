# Social Gain Vignette

## Introduction
This vignette illustrates the process for creating precision feedback messages about a recipient's performance rising above a peer comparator, such as a top performer benchmark or peer average. These messages use the Social Gain Causal Pathway, which specifies feedback messages that may motivate providers by delivering information about their performance improving. Motivation from these messages can arise from the recognition of a gain of social status as a top or above-average performer. Example messages that use social gain are "you reached the top 10% peer benchmark" and "your performance has increased above the peer average".

This vignette also contains example data and unique identifiers for the data entities that a precision feedback system uses to evaluate the potential success of a precision feedback message. An example of a unique identifier is http://purl.obolibrary.org/obo/psdo_0000126, an ID that points to a [peer average comparator](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126), defined in the [Performance Summary Display Ontology](https://github.com/Display-Lab/psdo) as an average representing the mean performance of a peer group. 

## Performance Data
Each month, MPOG receives data about operative case quality and outcomes from approximately 60 healthcare institutions. MPOG calculates performance for each provider individually, for approximately 35 performance measures of quality and outcomes. One example of these measures is [OPIOID: Opioid Equivalency](https://spec.mpog.org/Spec/Public/37).

### Benchmark comparators
MPOG calculates performance benchmarks and averages for each institution. One comparator is a [top 10% benchmark](http://purl.obolibrary.org/obo/psdo_0000129), which represents the 90th percentile for performance among providers at an institution for a given measure. Another comparator is the [peer average](http://purl.obolibrary.org/obo/psdo_0000126), which is the mean performance for all providers at an insitution for a given measure.

### Healthcare professional performance
Chikondi, a resident physician at Max Community Hospital, has the following performance data over the last 6 months for the OPIOID measure:

|Month|Performance Level|Top 10% Benchmark|Peer Average|
|-----|-----------------|-----------------|------------|
|Oct  |              xx%|               xx|          xx|
|Nov  |              xx%|               xx|          xx|
|Dec  |              xx%|               xx|          xx|
|Jan  |              xx%|               xx|          xx|
|Feb  |              xx%|               xx|          xx|
|Mar  |              xx%|               xx|          xx|

Fahad, an attending pediatric anesthesiologist at Max Community Hospital, has the following performance data over the last 6 months for the OPIOID measure:

|Month|Performance Level|Top 10% Benchmark|Peer Average|
|-----|-----------------|-----------------|------------|
|Oct  |              xx%|               xx|          xx|
|Nov  |              xx%|               xx|          xx|
|Dec  |              xx%|               xx|          xx|
|Jan  |              xx%|               xx|          xx|
|Feb  |              xx%|               xx|          xx|
|Mar  |              xx%|               xx|          xx|

## Preference data
Chikondi's preference data (note that she has *not* completed the individual preference survey):

|Motivating information |Utility value|Description                                                                     |
|-----------------------|-------------|--------------------------------------------------------------------------------|
|Social Gain	           |00.0000	    |Performance was previously low, but it has improved to reach the peer benchmark.|
|Social Stayed Better   |00.0000	    |Performance is consistently high (no recent change).                            |
|Worsening             	|00.0000	   |Performance is worsening.                                                       |
|Improving	             |00.0000	    |Performance is improving.                                                       |
|Social Loss             |00.0000	    |Performance was previously high, but it has dropped below the peer average.     |
|Social Stayed Worse	   |00.0000	   |Performance has remained below average (no recent change).                      |
|Social Better	         |00.0000	    |Performance is high this month.                                                 |
|Social Worse	          |00.0000	   |Performance is low this month.                                                  |
|Social Approach	       |00.0000 	   |Performance is improving, getting closer to the peer benchmark.                 |


Fahad's preference data:

|Motivating information |Utility value|Description                                                                     |
|-----------------------|-------------|--------------------------------------------------------------------------------|
|Social Gain	           |00.0000	    |Performance was previously low, but it has improved to reach the peer benchmark.|
|Social Stayed Better   |00.0000	    |Performance is consistently high (no recent change).                            |
|Worsening             	|00.0000	   |Performance is worsening.                                                       |
|Improving	             |00.0000	    |Performance is improving.                                                       |
|Social Loss             |00.0000	    |Performance was previously high, but it has dropped below the peer average.     |
|Social Stayed Worse	   |00.0000	   |Performance has remained below average (no recent change).                      |
|Social Better	         |00.0000	    |Performance is high this month.                                                 |
|Social Worse	          |00.0000	   |Performance is low this month.                                                  |
|Social Approach	       |00.0000 	   |Performance is improving, getting closer to the peer benchmark.                 |

# Precision feedback message generation
To generate precision feedback, MPOG sends de-identified performance and preference data to a precision feedback system that processes each provider's data with their peer comparator performance data. The precision feedback system produces and evaluates candidate messages using metadata from message templates, then selects an optimal precision feedback message to return to MPOG. The precision feedback system is a knowledge-based system that is comprised of the following parts: a knowledge base, a software pipeline, and a web service.

## Precision Feedback Knowledge Base
The knowledge base contains the following components: causal pathways, message templates, and performance measures.

## Social Gain Causal Pathway
This pathway describes the influence of feedback interventions informing the recipient that their performance has become better than that of a social comparator, such as a top performer benchmark or peer average. The causal pathway model is made up of preconditions, moderators, mechanisms, and outcomes.

### Preconditions
Preconditions for social gain are factors necessary for the success of the precision feedback intervention using this pathway. The social gain pathway has the following preconditions:

Information content preconditions:
1. [Positive performance gap content](http://purl.obolibrary.org/obo/PSDO_0000104) - prefixIRI PSDO:0000104
2. [Social comparator content](http://purl.obolibrary.org/obo/psdo_0000095) - prefixIRI PSDO:0000095
3. [Positive trend content](http://purl.obolibrary.org/obo/PSDO_0000099) - prefixIRI PSDO:0000099
4. [Achievement content](http://purl.obolibrary.org/obo/PSDO_0000112) - prefixIRI PSDO:0000112

Message preconditions:
1. [Positive performance gap set](http://purl.obolibrary.org/obo/PSDO_0000117) - prefixIRI PSDO:0000117
2. [Social comparator set](http://purl.obolibrary.org/obo/PSDO_0000045) - prefixIRI PSDO:0000045
3. [Positive performance trend set](http://purl.obolibrary.org/obo/PSDO_0000120) - prefixIRI PSDO:0000120
4. [Achievement set](http://purl.obolibrary.org/obo/PSDO_0000121) - prefixIRI PSDO:0000121
 
### Moderators
Moderators are factors that inhibit or promote the influence of the feedback intervention on the recipient. The social gain causal pathway has the following moderators:
1. **Habituation** - How many times has the recipient previously received this message in the last year?
2. **Regulatory fit** - To what extent is the message aligned to the behavior/task's characteristics, context, and recipient personality (motivated by bad outcome prevention vs. good outcome promotion).
3. **Gap size** - How large is the gap between the recipient's performance level and that of the social comparator?
4. **Slope of trend** - Derivative of the performance measure in the time domain
5. **Time since last loss**

### Mechanisms
Mechanisms are factors that the intervention operates through to influence the feedback recipient. The social gain pathway has the following mechanisms:
1. **Awareness (knowledge)** - The message may change the recipient's awareness of their newfound or increased high performance relative to their peers.
2. **Subjective norms** - The message may influence the recipient by creating or reinforcing their perception of their newfound top-performer status within their peer group.
3. **Motivation** - The message may motivate the recipient to work to maintain their new status as a top performer.


### Outcomes
A successful precision feedback intervention leveraging the social gain pathway should increase clinical process performance improvement.

## Message templates
Message templates represent possible motivational messages that a precision feedback system can send. There are three message templates that the precision feedback system can access for this vignette: 

+ [Top 10% Peer Benchmark](https://i.imgur.com/I1EeK7L.jpeg) message: <sub>placeholder link</sub>
> You reached the top 10% peer benchmark this month for the measure [Measure name].

This message template [is about](http://purl.obolibrary.org/obo/IAO_0000136) the following data features:
1. *todo* - need clarification on finding these, making sure everything is correct.
+ [Top 25% Peer Benchmark](https://i.imgur.com/I1EeK7L.jpeg) <sub>placeholder link</sub>
> You reached the top 25% peer benchmark this month for the measure [Measure name].

This message template [is about](http://purl.obolibrary.org/obo/IAO_0000136) the following data features:
1. *todo* 
+ [Above Peer Average](https://i.imgur.com/I1EeK7L.jpeg) <sub>placeholder link</sub>
> Your performance is above the peer average this month for the measure [Measure name].

This message template [is about](http://purl.obolibrary.org/obo/IAO_0000136) the following data features:
1. *todo*

## Software Pipeline (Precision Feedback Pipeline)
**TODO**

### Recipient annotations (Bitstomach)
The first stage of the pipeline analyzes performance to identify features of performance, such as comparisons and trends that are related to motivation. The analysis from this stage results in the following annotations:

Chikondis's annotations indicate the presence of the following in her performance data this month:
1. **TODO**

Fahad's annotations indicate the presence of the following in his performance data this month:
1. **TODO**


### Candidate Message Generation (Candidate Smasher)
The second stage of the pipeline creates possible messages by associating the annotations for Chikondi and Fahad with each message template, so that two candidate messages are created for each person.

Chikondi's candidate messages:

A. Candidate A has the following annotations:

The [**TODO**](**TODO**) message template [is about](**TODO**) the following features of performance data:
1. **TODO**

Chikondi's annotations from this month:
1. **TODO**

B. Candidate B has the following annotations:

The [**TODO**](**TODO**) message template [is about] (**TODO**) the following features of performance data:
TODO

Chikondi's annotations from this month:
TODO

Fahad's candidate messages:

A. Candidate A has the following annotations:

TODO

Fahad's performance is about:
TODO

B. Candidate B has the following annotations:

TODO

Fahad's performance is about:
TODO

### Candidate Message Preconditions Evaluation (Think Pudding)
TODO

### Candidate Message Moderator Evaluation and Selection (Esteemer)
TODO

### Message Generation and Delivery (Pictoralist)
TODO

