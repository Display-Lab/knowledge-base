# Social Worse Vignette
## Introduction
This vignette delineates the process for creating precision feedback messages about a recipient's performance worsening in comparison with their peers. These messages use the Social Worse causal pathway, which provides negative feedback that may motivate providers by delivering information about their recent performance falling below a specified social comparator for a given month. An example messages that uses the social worse pathway is "you are not a top performer this month".

This vignette also contains example data and unique identifiers for the data entities that a precision feedback system uses to evaluate the potential success of a precision feedback message. An example of a unique identifier is http://purl.obolibrary.org/obo/psdo_0000126, an ID that points to a [peer average comparator](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126), defined in the [Performance Summary Display Ontology](https://github.com/Display-Lab/psdo) as an average representing the mean performance of a peer group. 

## Performance Data
Each month, MPOG receives data about operative case quality and outcomes from approximately 60 healthcare institutions. MPOG calculates performance for each provider individually, for approximately 35 performance measures of quality and outcomes. One example of these measures is [GLU-01 : High Glucose Treated, Intraop](https://spec.mpog.org/Spec/Public/5).

### Benchmark comparators
MPOG calculates performance benchmarks and averages for each institution. One comparator is a [top 10% benchmark](http://purl.obolibrary.org/obo/psdo_0000129), which represents the 90th percentile for performance among providers at an institution for a given measure. Another comparator is the [peer average](http://purl.obolibrary.org/obo/psdo_0000126), which is the mean performance for all providers at an insitution for a given measure.

### Healthcare professional performance
Deepa, a nurse anesthetist (CRNA) at Midwest Medicine, has the following performance data over the last 6 months for the GLU-01 measure:

|Month|Performance Level|Top 10% Benchmark|Peer Average|
|-----|-----------------|-----------------|------------|
|Oct  |              xx%|               xx|          xx|
|Nov  |              xx%|               xx|          xx|
|Dec  |              xx%|               xx|          xx|
|Jan  |              xx%|               xx|          xx|
|Feb  |              xx%|               xx|          xx|
|Mar  |              xx%|               xx|          xx|

Eugene, a resident anesthesiologist at Midwest Medicine, has the following performance data over the last 6 months for the GLU-01 measure:

|Month|Performance Level|Top 10% Benchmark|Peer Average|
|-----|-----------------|-----------------|------------|
|Oct  |              xx%|               xx|          xx|
|Nov  |              xx%|               xx|          xx|
|Dec  |              xx%|               xx|          xx|
|Jan  |              xx%|               xx|          xx|
|Feb  |              xx%|               xx|          xx|
|Mar  |              xx%|               xx|          xx|

## Preference data
Deepa's preference data:

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


Eugene's preference data:

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

## Social Worse Causal Pathway
This pathway describes the influence of feedback interventions informing the recipient that their performance is worse than that of a social comparator, such as a top performer benchmark or peer average. The causal pathway model is made up of preconditions, moderators, mechanisms, and outcomes.

### Preconditions
Several preconditions are necessary for the success of feedback intervention using the social worse causal pathway. They are subdivided into informational and message preconditions, and are as follows:

Information content preconditions:
1. [Negative performance gap content](http://purl.obolibrary.org/obo/PSDO_0000105) - prefixIRI PSDO:0000105
2. [Social comparator content](http://purl.obolibrary.org/obo/psdo_0000095) - prefixIRI PSDO:0000095

Message preconditions:
1. [Negative performance gap set](http://purl.obolibrary.org/obo/PSDO_0000116) - prefixIRI PSDO:0000116
2. [Social comparator set](http://purl.obolibrary.org/obo/PSDO_0000045) - prefixIRI PSDO:0000045
 
### Moderators
Moderators are factors that inhibit or promote the influence of the feedback intervention on the recipient. The social gain causal pathway has the following moderators:
1. **Habituation** - How many times has the recipient previously received this message in the last year?
2. **Regulatory fit** - How aligned is the message with characteristics of the behavior/task, context, and recipient personality (motivated by prevention vs. promotion mindset with regard to future outcomes)?
3. **Gap size** - How large is the gap between the recipient's performance level and that of the social comparator?

### Mechanisms
Mechanisms are factors that the intervention operates through to influence the feedback recipient. The social gain pathway has the following mechanisms:
1. **Awareness (knowledge)** - The message may change the provider's awareness of their own lagging performance relative to their peers.
2. **Subjective Norms** - Messages may influence the recipient's perception of their own performance status (below average, in this case) within their peer group.
3. **Motivation** - The message may motivate the provider to work to lose their status as a non-top-performer among their peers.

### Outcomes
The expected outcome of a successful social worse pathway intervention, as with any precision feedback intervention, is clinical performance improvement.

## Message templates
Message templates represent possible motivational messages that a precision feedback system may send. There are two(?) <sub> Todo </sub> message templates that the precision feedback system can access for this vignette: 

The *Todo: message name?* message reads: 
> You are not a top performer this month for the measure [Measure name]. Your performance was [recipient performance level - percentage], below the [comparator name].

This message template [is about](http://purl.obolibrary.org/obo/IAO_0000136) *todo*...
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