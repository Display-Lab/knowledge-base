# Improving Causal Pathway Vignette

## Introduction 

A healthcare quality improvement consortium called the Multicenter Perioperative Outcomes Group (MPOG) uses precision feedback to prioritize motivating performance information about the quality and outcomes of operative cases. A performance measure that MPOG assesses for operative cases regards the minimization of the use of climate-sensitive anesthetic gases: [BP-03: Low Map Prevention < 65](https://spec.mpog.org/Spec/Public/34).

## Performance Data
MPOG has received operative case data from last month about Deepa and Gaile's cases and that of their peers. MPOG calculates the following performance information for the measure BP-03:

### Healthcare professional performance
Deepa's performance rate for BP-03 has level of 75% for November 2023, 74% for December 2023, and 77% for January 2023. Gaile's performance is 72% for November 2023, 75% for December 2023, and 74% for January 2023. 

Deepa, a dedicated Certified Registered Nurse Anesthetist (CRNA) at Midwest Medicine, has the following performance data over the last 6 months for BP-03:

|Month|Performance Level|Top 10% Benchmark|Peer Average|
|-----|-----------------|-----------------|------------|
|Aug  |                 |                 |            |
|Sep  |                 |                 |            |
|Oct  |              88%|               93|          86|
|Nov  |              89%|               96|          88|
|Dec  |              87%|               95|          87|
|Jan  |              86%|               97|          87|

Gaile, a resident at Midwest Medicine, has the following performance data over the last 6 months for BP-03:

|Month|Performance Level|Top 10% Benchmark|Peer Average|
|-----|-----------------|-----------------|------------|
|Aug  |                 |                 |            |
|Sep  |                 |                 |            |
|Oct  |              97%|               94|          85|
|Nov  |              96%|               95|          87|
|Dec  |              95%|               96|          86|
|Jan  |              98%|               97|          84|

## Preference data
Preferences for precision feedback are elicited through a preference survey that providers can take. The preference survey produces a preference model for each provider that, with the provider's permission, is shared with MPOG to maintain. MPOG analyses preferences data that is shared to identify population-level preference segments. These are generates as preference profiles that can serve as a default preference model for an organization, or which can be selected by providers who do not take the preference survey, but who identify preferences that are close enough to their own in the settings menu for the precision feedback system.

Deepa's preference data: (TODO)
|Motivating information |Utility value|Description                                                                     |
|-----------------------|-------------|--------------------------------------------------------------------------------|
|Social gain	           |0.00000	      |Performance was previously low, but it has improved to reach the peer benchmark.|
|Social stayed better   |0.00000	    |Performance is consistently high (no recent change).                            |
|Worsening             	|0.00000	   |Performance is worsening.                                                       |
|Improving	             |0.00000	    |Performance is improving.                                                       |
|Social los             |0.00000	    |Performance was previously high, but it has dropped below the peer average.     |
|Social stayed worse	   |0.00000	   |Performance has remained below average (no recent change).                      |
|Social better	         |0.00000	    |Performance is high this month.                                                 |
|Social worse	          |0.00000	   |Performance is low this month.                                                  |
|Social approach	       |0.00000 	   |Performance is improving, getting closer to the peer benchmark.                 |


Gaile's preference data: (TODO)

|Motivating information |Utility value|Description                                                                     |
|-----------------------|-------------|--------------------------------------------------------------------------------|
|Social gain	           |-2.92114	    |Performance was previously low, but it has improved to reach the peer benchmark.|
|Social stayed better   |-12.76936	   |Performance is consistently high (no recent change).                            |
|Worsening             	|1.06977     	|Performance is worsening.                                                       |
|Improving	             |-0.26266	    |Performance is improving.                                                       |
|Social loss            |2.72075	     |Performance was previously high, but it has dropped below the peer average.     |
|Social stayed worse	   |9.97743	     |Performance has remained below average (no recent change).                      |
|Social better	         |-5.97766	    |Performance is high this month.                                                 |
|Social worse	          |-0.05277	    |Performance is low this month.                                                  |
|Social approach	       |-0.24384	    |Performance is improving, getting closer to the peer benchmark.                 |

The above tables were taken from Social Loss Vignette - PG

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
Moderators are factors that inhibit or promote the influence of the feedback intervention on the recipient. The social loss causal pathway has the following moderators:
1. Habituation: How many times has the recipient previously received this message in the last year?
2. Regulatory fit: To what extent is this message aligned with characteristics of the behavior/task, context, and recipient personality, with regard to motivation to avoid negative outcomes / problem (prevention focus), or motivation to achieve positive outcomes / develop and learn (promotion focus)?
3. Gap size: How large is the gap between the recipient's performance level and that of the social comparator?

### Mechanisms 
Mechanisms are factors that the intervention operates through to influence the feedback recipient. The social loss pathway has the following mechanisms:
1. Habituation: How many times has the recipient previously received this message in the last year?
2. Regulatory fit: To what extent is this message aligned with characteristics of the behavior/task, context, and recipient personality, with regard to motivation to avoid negative outcomes / problem (prevention focus), or motivation to achieve positive outcomes / develop and learn (promotion focus)?
3. Gap size: How large is the gap between the recipient's performance level and that of the social comparator? (TODO)

### Outcomes
The expected outcome of the successful influence of an email that uses the improving pathway is clinical process performance improvement.

## Message templates (TODO)
Message templates represent a possible motivational message that a precision feedback system can send. There are two message templates that the precision feedback system can access for this vignette: 

A. The [Performance Improving](https://github.com/Display-Lab/knowledge-base/...json TODO) message template contains the following message: "Your performance is improving this month for the measure [measure name].". This message template [is about<sub>(OB)</sub>](http://purl.obolibrary.org/obo/IAO_0000136) the following features of performance data:

1. [Positive performance trend set<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO/?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)

2. Display format compatibility: [Line Graph <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/IAO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FIAO_0000573), [Bar Chart <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/STATO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FSTATO_0000166), text only (TODO ?)

B. The [Congrats Improved Performance](https://github.com/Display-Lab/knowledge-base/blob/...json TODO) message template contains the following message: "Congratulations on your improved performance this month for the measure [measure name]." This message template [is about<sub>(BP)</sub>](http://purl.obolibrary.org/obo/IAO_0000136) the following features of performance data:

1. [Positive performance trend set<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO/?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)

2. Display format compatibility: [Line Graph <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/IAO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FIAO_0000573), [Bar Chart <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/STATO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FSTATO_0000166), text only (TODO ?)

## Software Pipeline (Precision Feedback Pipeline) TODO

## Recipient annotations (Bitstomach)
This data set should result in an annotation that there is information content about a positive performance trend for Alice:
1. Positive performance trend content (http://purl.obolibrary.org/obo/psdo_0000099)

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

## Existing notes below 5/23 - HC

## Template annotations
The performance_improving template is about a positive performance trend set:
1. Positive performance trend set (http://purl.obolibrary.org/obo/psdo_0000120)

## Resulting candidates
The candidate produced for Deepa has:
1. Positive performance trend content (http://purl.obolibrary.org/obo/psdo_0000099)
2. Positive performance trend set (http://purl.obolibrary.org/obo/psdo_0000120)

## Causal pathway preconditions
The improving causal pathway has preconditions:
1. Positive performance trend content (http://purl.obolibrary.org/obo/psdo_0000099)
2. Positive performance trend set (http://purl.obolibrary.org/obo/psdo_0000120)

## Evaluation result
The candidate is found to be acceptable by the causal pathway 'improving'.


