# Improving Causal Pathway Vignette

## Introduction

This vignette illustrates the process for generating precision feedback messages about a recipient's performance when it is improving. Feedback messages about improving performance motivate providers by enhancing providers' knowledge about their performance trends and fostering a sense of optimism. Example feedback messages that are part of the Improving Causal Pathway include "Your performance is improving" and "Congratulations on your improved performance." 

A healthcare quality improvement consortium called the Multicenter Perioperative Outcomes Group (MPOG) uses precision feedback to prioritize motivating performance information about the quality and outcomes of operative cases. A performance measure that MPOG assesses for operative cases regards the minimization of the use of climate-sensitive anesthetic gases: [BP-03: Low Map Prevention < 65](https://spec.mpog.org/Spec/Public/34).

## Performance Data

A healthcare quality improvement consortium called the Multicenter Perioperative Outcomes Group (MPOG) uses precision feedback to prioritize motivating performance information about the quality and outcomes of operative cases. A performance measure that MPOG assesses for operative cases regards the minimization of the use of climate-sensitive anesthetic gases: [BP-03: Low Map Prevention < 65](https://spec.mpog.org/Spec/Public/34).

### Healthcare professional performance
MPOG has received operative case data from last month about Gaile and Gaile's cases and that of their peers. MPOG calculates the following performance information for the measure BP-03:

### Healthcare professional performance
Gaile, a dedicated Certified Registered Nurse Anesthetist (CRNA) at Midwest Medicine, has the following performance data over the last 6 months for BP-03:

|Month|Performance Level|Peer Average|75th Percentile Benchmark|90th Percentile Benchmark|MPOG Goal|
|-----|---------|---|---|---|---|
|Jul  |      75%| 80| 85| 90| 90|
|Aug  |      75%| 80| 85| 90| 90|
|Sept |      75%| 80| 85| 90| 90|
|Oct  |      75%| 80| 85| 90| 90|
|Nov  |***82%***| 80| 85| 90| 90|
|Dec  |***87%***| 80| 85| 90| 90|

Gaile, a resident at Midwest Medicine, has the following performance data over the last 6 months for BP-03:

|Month|Performance Level|Peer Average|75th Percentile Benchmark|90th Percentile Benchmark|MPOG Goal|
|-----|---------|---|---|---|---|
|Jul  |      85%| 85| 88| 92| 90|
|Aug  |      85%| 85| 88| 92| 90|
|Sept |      85%| 85| 88| 92| 90|
|Oct  |      85%| 85| 88| 92| 90|
|Nov  |***87%***| 85| 88| 92| 90|
|Dec  |***90%***| 85| 88| 92| 90|

## Preference data
Preferences for precision feedback are elicited through a preference survey that providers can take. The preference survey produces a preference model for each provider that, with the provider's permission, is shared with MPOG to maintain. MPOG analyses preference data that is shared to identify population-level preference segments. These segments are generated as preference profiles that can serve as a default preference model for an organization, or which can be selected by providers who do not take the preference survey, but who identify preferences that are close enough to their own in the settings menu for the precision feedback system.

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
|Social Aproach	       |-10.2541	   |Performance is improving, getting closer to the peer benchmark.                 |


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

## Message templates
Message templates represent a possible motivational message that a precision feedback system can send. There are two message templates that the precision feedback system can access for this vignette: 

A. `The Performance Improving`[<sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/performance_improving.json) message template contains the following message: 
> Your performance is improving this month for the measure [measure name].

This message template `is about`[<sub>(OntoBee)</sub>](http://purl.obolibrary.org/obo/IAO_0000136) the following features of performance data:
1. [Positive performance trend set<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO/?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)
2. Display format compatibility: [Line Graph <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/IAO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FIAO_0000573), [Bar Chart <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/STATO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FSTATO_0000166)<!--, text only (TODO ?)-->

B. The `Congrats Improved Performance`[<sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/congrats_improved_performance.json) message template contains the following message: 
> Congratulations on your improved performance this month for the measure [measure name].

This message template [is about<sub>(BP)</sub>](http://purl.obolibrary.org/obo/IAO_0000136) the following features of performance data:
1. [Positive performance trend set<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO/?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)
2. Display format compatibility: [Line Graph <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/IAO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FIAO_0000573), [Bar Chart <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/STATO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FSTATO_0000166)<!--, text only (TODO ?) -->

## Software Pipeline (Precision Feedback Pipeline)
### Recipient annotation generation (Bitstomach)
The first stage of the pipeline is a script called Bitstomach. This script analyzes recipient's performance data and generates features called **annotations**. These annotations describe features of the performance data such as performance trends over time, or how performance measures relate to other values like peer performance benchmarks and institutional performance goals.

**Annotations for Deepa's performance data for the most recent month:** 
1. `Social comparator content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000095)
2. `Positive performance trend content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000099)
3. `Negative performance gap content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000105)
    - *with respect to* [Peer 90th percentile comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000129)
    - *with respect to* [Goal comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000046)
4. `Positive performance gap content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000104) 
    - *with respect to* [Peer average comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126)
    - *with respect to* [Peer 75th percentile comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000128)

**Annotations for Gaile's performance data for the most recent month:**
1. `Social comparator content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000095)
2. `Positive performance trend content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000099)
3. `Negative performance gap content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000105)
	- *with respect to* [Peer 90th percentile comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000129)
4. `Positive performance gap content` [<sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000104)
	- *with respect to* [Goal comparator element <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000046)
    - *with respect to* [Peer 75th percentile comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000128)
    - *with respect to* [Peer average comparator <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000126)

### Candidate Message Generation (Candidate Smasher)
The second stage of the pipeline creates two candidate messages that may be appropriate for each recipient to recieve. It does this by searching through the message template library and selecting two message templates with annotations that match those annotations of the recipient's performance.

**Deepa's candidate messages (A & B):**

**Candidate Message A** is the `The Performance Improving`[<sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/performance_improving.json) message template, which has the following annotations *in common* with the performance annotations:
1. [Positive performance trend set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)

**Candidate Message B** is the `Congrats Improved Performance`[<sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/congrats_improved_performance.json) message template, which has the following annotations *in common* with the performance annotations:
1. [Positive performance trend set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)

Both candidate messages have annotations matching those generated from Deepa's performance data, and are therefore appropriate as candidate messages.

**Gaile's candidate messages (α & β):**

**Candidate Message α** is the `The Performance Improving`[<sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/performance_improving.json) message template, which has the following annotations *in common* with the performance annotations:
1. [Positive performance trend set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)

**Candidate Message β** is the `Congrats Improved Performance`[<sub>(GH)</sub>](https://github.com/Display-Lab/knowledge-base/blob/main/message_templates/congrats_improved_performance.json) message template, which has the following annotations *in common* with the performance annotations:
1. [Positive performance trend set <sub>(BP)</sub>](https://bioportal.bioontology.org/ontologies/PSDO?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPSDO_0000120)

Both candidate messages have annotations matching those generated from Gaile's performance data, and are therefore appropriate as candidate messages.

### Candidate Message Preconditions Evaluation (ThinkPudding)
The third stage of the pipeline processes and evaluates the candidate messages for each persona. It determines the ways in which the candidate message, causal pathway, and performance data are related, and ranks the candidate messages based on how closely related they are to the recipient's performance data and causal pathway. Overall, this script determines which candidate message is the best to give to the recipient based on the causal pathway and their performance data.

For Deepa, **Candidate B** is acceptable by the causal pathway **improving**.
For Gaile, **Candidate α** is acceptable by the causal pathway **improving**.

### Candidate Message Moderator Evaluation and Selection (Esteemer)
The fourth stage of the pipeline selects which message to use in this month's precision feedback message, and collects the necessary information for feedback generation. The script does this by evaluating three things: the recipient's message preferences, their message history, and the candidate message's acceptability based on performance data and causal pathway relationships (ThinkPudding output).

**For Deepa, Esteemer uses the following information:**
- The most acceptable candidate message is **Candidate B**
- Deepa's preference for improving messages is *Todo*
- Deepa has not recieved the **Candidate B** message recently. 
<!-- Todo - determine how long message cooldown is for repeat selection, change text above accordingly-->
> ∴ Esteemer will select **Candidate B** as the most appropriate message to provide the recipient.

**For Gaile, Esteemer uses the following information:**
- The most acceptable candidate message is **Candidate α**
- Gaile's preference for improving messages is *Todo*
- Gaile has not recieved the **Candidate α** message recently.
> ∴ Esteemer will select **Candidate α** as the most appropriate message to provide the recipient. 

For each of the selected messages, Eseemer will return the template ID, message text, comparator type, acceptability relationship, measure name, title, and display type preferred by the recipient. This data is used in the next step of the pipeline to generate the precision feedback message.

### Message Generation and Delivery (Pictoralist)
The fifth and final stage of the pipeline generates visual representations of the selected message based on the recipient's performance data, and sends this output off for delivery to the recipient.
The script takes in the selected message and performance data of the recipient as inputs. It then uses the recipient's display preferences to generate a figure that visualize's the reciepients performance over time related to the given measure and causal pathway. It returns the figure as an image encoded as a base64 string, alongside other elements of the precision feedback message. The precision feedback email is then created using this figure, the necessary text data, and is then sent to the recipient.
