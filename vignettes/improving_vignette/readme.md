# Improving Causal Pathway Vignette

## Introduction 

This vignette illustrates the process for generating precision feedback messages about a recipient's performance when it is improving. Feedback messages about improving performance motivate providers by enhancing providers' knowledge about their performance trends and fostering a sense of optimism. Example feedback messages that are part of the Improving Causal Pathway include "Your performance is improving" and "Congratulations on your improved performance." 

A healthcare quality improvement consortium called the Multicenter Perioperative Outcomes Group (MPOG) uses precision feedback to prioritize motivating performance information about the quality and outcomes of operative cases. A performance measure that MPOG assesses for operative cases regards the minimization of the use of climate-sensitive anesthetic gases: [BP-03: Low Map Prevention < 65](https://spec.mpog.org/Spec/Public/34).

## Performance Data

A healthcare quality improvement consortium called the Multicenter Perioperative Outcomes Group (MPOG) uses precision feedback to prioritize motivating performance information about the quality and outcomes of operative cases. A performance measure that MPOG assesses for operative cases regards the minimization of the use of climate-sensitive anesthetic gases: [BP-03: Low Map Prevention < 65](https://spec.mpog.org/Spec/Public/34).

### Healthcare professional performance
MPOG has received operative case data from last month about Deepa and Gaile's cases and that of their peers. MPOG calculates the following performance information for the measure BP-03:

### Healthcare professional performance
Deepa, a dedicated Certified Registered Nurse Anesthetist (CRNA) at Midwest Medicine, has the following performance data over the last 6 months for BP-03:

|Month|Performance Level|Peer Average|75th Percentile Benchmark|90th Percentile Benchmark|MPOG Goal|
|-----|-----------------|------------|-------------------------|-------------------------|--|
|Jul  |              80%|          80|                       85|                       90|90|
|Aug  |              80%|          80|                       85|                       90|90|
|Sept |              80%|          80|                       85|                       90|90|
|Oct  |              80%|          80|                       85|                       90|90|
|Nov  |        * *82%* *|          80|                       85|                       90|90|
|Dec  |        * *84%* *|          80|                       85|                       90|90|

Gaile, a resident at Midwest Medicine, has the following performance data over the last 6 months for BP-03:

|Month|Performance Level|Peer Average|75th Percentile Benchmark|90th Percentile Benchmark|MPOG Goal|
|-----|-----------------|------------|-------------------------|-------------------------|--|
|Jul  |              85%|          85|                       88|                       92|90|
|Aug  |              85%|          85|                       88|                       92|90|
|Sept |              85%|          85|                       88|                       92|90|
|Oct  |              85%|          85|                       88|                       92|90|
|Nov  |        * *87%* *|          85|                       88|                       92|90|
|Dec  |        * *90%* *|          85|                       88|                       92|90|

## Preference data
Preferences for precision feedback are elicited through a preference survey that providers can take. The preference survey produces a preference model for each provider that, with the provider's permission, is shared with MPOG to maintain. MPOG analyses preference data that is shared to identify population-level preference segments. These segments are generated as preference profiles that can serve as a default preference model for an organization, or which can be selected by providers who do not take the preference survey, but who identify preferences that are close enough to their own in the settings menu for the precision feedback system.

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


Gaile's preference data: 
|Motivating information |Utility value|Description                                                                     |
|-----------------------|-------------|--------------------------------------------------------------------------------|
|Social Gain	           |xx.xxxxx	    |Performance was previously low, but it has improved to reach the peer benchmark.|
|Social Stayed Better   |-11.3618	    |Performance is consistently high (no recent change).                            |
|Worsening             	|11.6598	   |Performance is worsening.                                                       |
|Improving	             |7.58489	    |Performance is improving.                                                       |
|Social Loss             |8.46823	    |Performance was previously high, but it has dropped below the peer average.     |
|Social Stayed Worse	   |-3.64987	   |Performance has remained below average (no recent change).                      |
|Social Better	         |-8.64669	    |Performance is high this month.                                                 |
|Social Worse	          |12.1645	   |Performance is low this month.                                                  |
|Social Approach	       |-10.6889 	   |Performance is improving, getting closer to the peer benchmark.                 |

# Precision feedback message generation
To generate precision feedback, MPOG sends de-identified performance and preference data to a precision feedback system that processes each provider's data with their peer comparator performance data. The precision feedback system produces and evaluates candidate messages using metadata from message templates, then selects an optimal precision feedback message to return to MPOG. The precision feedback system is a knowledge-based system that is comprised of the following parts: 1) A knowledge base, 2) A software pipeline, and 3) A web service.

## Precision Feedback Knowledge Base
The knowledge base contains the following components: Causal pathways, message templates, and performance measures.

## Improving Causal Pathway
This pathway describes the influence of feedback interventions that show the message recipient that their performance has improved. The causal pathway model is made up of preconditions, moderators, mechanisms, and outcomes.

### Preconditions 
Preconditions for improving are factors that are necessary for the success of the feedback intervention using this pathway. The improving pathway has the following preconditions:

Information content preconditions:
1. [Positive performance trend content<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO/?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000099)

Message preconditions:
1. [Positive performance trend set<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO/?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)
 
### Moderators 
Moderators are factors that inhibit or promote the influence of the feedback intervention on the recipient. The improving causal pathway has the following moderators:
1. `Habituation` - How many times has the recipient previously received this message in the last year?
2. `Regulatory fit` - To what extent is this message aligned with characteristics of the behavior/task, context, and recipient personality, with regard to motivation to avoid negative outcomes / problem (prevention focus), or motivation to achieve positive outcomes / develop and learn (promotion focus)?
3. `Gap size` - How large is the gap between the recipient's performance level and that of the social comparator?

### Mechanisms 
Mechanisms are factors that the intervention operates through to influence the feedback recipient. The social loss pathway has the following mechanisms:
1. `Awareness (knowledge)`: The message may change the recipient's awareness of their high performance, relative to peers.
2. `Optimism` - The message may influence the recipient's confidence that things will happen for the best and they will continue to increase their performance, gaining social status.

### Outcomes
The expected outcome of the successful influence of an email that uses the improving pathway is clinical process performance improvement.

## Message templates (TODO)
Message templates represent a possible motivational message that a precision feedback system can send. There are two message templates that the precision feedback system can access for this vignette: 

A. `The Performance Improving`[<sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/performance_improving.json) message template contains the following message: 
> Your performance is improving this month for the measure [measure name].

This message template `is about`[<sub>(OntoBee)</sub>](http://purl.obolibrary.org/obo/IAO_0000136) the following features of performance data:

1. [Positive performance trend set<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO/?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)
2. Display format compatibility: [Line Graph <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/IAO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FIAO_0000573), [Bar Chart <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/STATO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FSTATO_0000166), text only (TODO ?)

B. The `Congrats Improved Performance`[<sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/congrats_improved_performance.json) message template contains the following message: 
> Congratulations on your improved performance this month for the measure [measure name].

This message template [is about<sub>(BP)</sub>](http://purl.obolibrary.org/obo/IAO_0000136) the following features of performance data:

1. [Positive performance trend set<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO/?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)
2. Display format compatibility: [Line Graph <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/IAO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FIAO_0000573), [Bar Chart <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/STATO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FSTATO_0000166), text only (TODO ?)

## Software Pipeline (Precision Feedback Pipeline) TODO

## Recipient annotations (Bitstomach)
The first stage of the pipeline analyzes performance to identify features of performance, such as comparisons and trends that are related to motivation. The analysis from this stage results in the following annotations:

Deepa's annotations indicate the presence of the following in her performance data this month:
1. **TODO**

Gaile's annotations indicate the presence of the following in his performance data this month:
1. **TODO**

### Candidate Message Generation (Candidate Smasher)
The second stage of the pipeline creates possible messages by associating the annotations for Deepa and Gaile with each message template, so that two candidate messages are created for each person.

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
