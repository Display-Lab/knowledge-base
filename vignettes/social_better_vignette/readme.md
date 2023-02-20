# Social Better Vignette


## Introduction
Clinical performance feedback commonly includes peer comparison because it helps providers to understand how their care differs from the norm, and may motivate them to improve the care they provide to align with peers. Peer comparison feedback may also motivate providers to maintain a social status of being a high performer, once they have achieved it. The Social Better Causal Pathway specifies feedback messages that are capable of motivating providers through the delivery of information about high performance, relative to peers. This vignette serves the purpose of illustrating how a precision feedback system uses the Social Better Causal Pathway to motivate providers, and illustrates the process of generating research data about precision feedback for the study of feedback systems in healthcare. This vignette is written for clinical feedback system stakeholders, including feedback system developers, researchers, healthcare professionals and leaders, and patients.

## Context: Precision feedback emails in a quality improvement network
A healthcare quality improvement consortium called the Multicenter Perioperative Outcomes Group (MPOG) uses precision feedback to prioritize motivating performance information about the quality and outcomes of operative cases. Precision feedback is an kind of feedback intervention that prioritizes motivating performance information and customizes its delivery based on the preferences of the feedback recipient, or that of their population segment. Emails with precision feedback about various performance measures are sent each month to anesthesia providers in approximately 35 healthcare institutions. One performance measure that MPOG assesses for operative cases regards the minimization of the use of climate-sensitive anesthetic gases: [SUS-04 : Fresh Gas Flow, less than or equal to 2L/min](https://spec.mpog.org/Spec/Public/63).

## Healthcare professionals and Healthcare Organizations (Personas)
Alice is an attending anesthesiologist at Midwest Medicine, a medical-school affiliated hospital. She is motivated to continue improving her practice and that of her team, and who values setting new goals for her and her team to reach. MPOG has not yet elicited preferences from Alice about precision feedback. An organizational preference profile for anesthesia providers at Midwest Medicine has been developed from a cluster analysis of a sample of providers who have taken an online preference survey, and these results are used for Alice and any other anesthesia provider who has not yet taken a preference survey. This profile prioritizes feedback messages about changes in performance involving the achievement of peer benchmarks, drops in performance below a peer average, and improvement towards the peer benchmark, as well as time-series visualization in bar charts and line charts. The Midwest Medicine Anesthesia Provider Preference Profile is a set of relative utilities for attributes of feedback messages that a precision feedback system uses to prioritize performance information and feedback display format.

Bob is a CRNA at Danville Hospital, a community hospital. He cares deeply about the safety of his patients and the efficiency of his team to provide the best care for patients in his community. He is proud of his team's record of providing high-quality and exceptionally safe care, and the quality awards that his hospital has received in recognition of their exceptional work. Bob prefers to receive notifications about any potential quality issues or significant problems, such as adverse events, that may require special attention from him and his team. Bob prefers to receive these in a brief sentence that does not require him to look at a chart, but which helps him understand that there is some follow-up required to dig into the details of one or more operative cases. Bob took a feedback preference survey which generated a set of relative utilities for feedback message attributes that a precision feedback system can use.


## Data

### Performance data
MPOG has received data about Alice and Bob's operative cases and that of their peers for analysis, to measure care quality and outcomes. MPOG analyses the data for each performance measure, and calculates the following performance information for the measure SUS-04:

### Individual healthcare professionals
Alice has a performance level of 97% for January 2023. 
Bob has a performance level of 94% for January 2023.

### Comparators
The top 25% peer benchmark at Midwest Medicine for January 2023 is 93%.
The top 10% peer benchmark at Midwest Medicine for January 2023 is 96%.
The top 25% peer benchmark at Danville Hospital for January 2023 is 93%.
The top 10% peer benchmark at Danville Hospital for January 2023 is 95%.

### Preference data
Preferences for precision feedback are elicited through a preference survey that providers can take. The preference survey produces a preference model for each provider that, with the provider's permission, is shared with MPOG to maintain. MPOG analyses preferences data that is shared to identify population-level preference segments. These are generates as preference profiles that can serve as a default preference model for an organization, or which can be selected by providers who do not take the preference survey, but who identify preferences that are close enough to their own in the settings menu for the precision feedback system.

Alice's preference data: (TODO)
Bob's preference data: (TODO)

To generate precision feedback, MPOG sends de-identified performance and preference data to a precision feedback system that processes each provider's data with their peer comparator performance data, to select an optimal precision feedback message. 


# Precision feedback system
The precision feedback system is a knowledge-based system that is comprised of the following parts: 1) A knowledge base, 2) A software pipeline, and 3) A web service.

## Precision Feedback Knowledge Base
The knowledge base contains the following components: Causal pathways, message templates, and performance measures.

## Social Better Causal Pathway 
The causal pathway "social better" describes the influence of feedback interventions that show the recipient that their performance is better than that of a social comparator, such as a top performer benchmark or peer average. Example messages that uses the social better pathway are "You are a top performer" and "Your performance is better than average." The causal pathway model is made up of preconditions, moderators, mechanisms, and outcomes. 

### Preconditions
Preconditions are factors that are necessary for the success of the feedback intervention that uses the social better pathway. The social better pathway has the following preconditions:

Information content preconditions:
1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
2. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104)

Candidate message preconditions:
1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
2. Positive performance gap set (http://purl.obolibrary.org/obo/psdo_0000117)


### Moderators
Moderators are factors that inhibit or promote the influence of the feedback intervention on the recipient. The social better causal pathway has the following moderators:
1. Habituation: How many times has the recipient previously received this message in the last year?
2. Regulatory fit: To what extent is this message aligned with characteristics of the behavior/task, context, and recipient personality, with regard to motivation to avoid negative outcomes / problem (prevention focus), or motivation to achieve positive outcomes / develop and learn (promotion focus)?
3. Gap size: How large is the gap between the recipient's performance level and that of the social comparator?

### Mechanisms
Mechanisms the factors that the intervention operates through to influence the feedback recipient. The social better pathway has the following mechanisms of action:
1. Awareness (knowledge): The message may change the recipient's awareness of their high performance, relative to peers.
2. Subjective norms: The message may influence the precipient by creating or reinforcing their perception of their own top-performer status within their peer group.
3. Motivation: The message may motivate the recipient to work to  maintain their status as a top performer.

### Outcomes
The expected outcome of the successful influence of an email that uses the social better pathway is clinical process performance improvement or sustainment.


## Message templates
Message templates represent a possible tailored motivational message that a precision feedback system can send. There are two message templates that the Precision Feedback Pipeline can access for this vignette: 

A. The top_10_performer message template contains the following message:
"Congratulations on your high performance last month! You were a top performer for the measure [performance measure name]. Your performance was [recipient performance level], above the Top 10% peer benchmark of [Top 10% Benchmark performance level]". 
This message template is about a positive performance gap set and a social comparator element (the MPOG Top 10% Benchmark), and has the following metadata:
1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
2. Positive performance gap set (http://purl.obolibrary.org/obo/psdo_0000117)
3. MPOG Top 10% Benchmark Comparator (TODO)
4. Display format compatibility: Line_chart_ID_TODO, Bar_chart_ID_TODO, Text-only

B. The top_25_performer message template contains the following message: 
"Congrats on your high performance for the measure [performance measure name]! Your performance was [recipient performance level], above the Top 25% peer benchmark of [Top 25% Benchmark performance level]". 
This message template is about a positive performance gap set and a social comparator element (the MPOG Top 25% Peer Benchmark), and has the following metadata:
1. Social comparator element (http://purl.obolibrary.org/obo/psdo_0000045)
2. Positive performance gap set (http://purl.obolibrary.org/obo/psdo_0000117)
3. MPOG Top 25% Benchmark Comparator (TODO)
4. Display format compatibility: Line_chart_ID_TODO, Bar_chart_ID_TODO, Text-only


## Software Pipeline (Precision Feedback Pipeline)

### Recipient annotations (Bitstomach)
This data set should result in the following annotations:

Alice: Annotations indicate the presence of information content about a social comparator and a positive performance gap for both the Top 10% and Top 25% Benchmarks.
1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
2. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) with MPOG Top 10% Benchmark Comparator (TODO)
3. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) with MPOG Top 25% Benchmark Comparator (TODO)

Bob: Annotations indicate the presence of information content about a social comparator and a positive performance gap for the Top 25% Benchmark.
1. Social comparator content (http://purl.obolibrary.org/obo/psdo_0000095)
2. Positive performance gap content (http://purl.obolibrary.org/obo/psdo_0000104) with MPOG Top 25% Benchmark Comparator (TODO)


### Candidate Message Generation (Candidate Smasher)
For both Alice and Bob, their annotations above are associated with the metadata from each candidate message, so that two candidate messages are created for each person.

### Candidate Message Preconditions Evaluation (Think Pudding)
For Alice, both candidates are matched with the causal pathway Social Better, and are indicated as acceptable for ranking in the next stage of the pipeline.

For Bob, the candidate with a Top 25% benchmark is matched with the causal pathway Social Better, but the candidate with a Top 10% benchmark is not matched, because Bob's performance level is below the benchmark. The candidate message with the Top 25% benchmark is indicated as acceptable for ranking in the next stage of the pipeline.

### Candidate Message Moderator Evaluation and Selection (Esteemer)
TODO

### Message Generation and Delivery (Pictoralist)
TODO

