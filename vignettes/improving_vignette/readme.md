# Improving Causal Pathway Vignette

A healthcare quality improvement consortium called the Multicenter Perioperative Outcomes Group (MPOG) uses precision feedback to prioritize motivating performance information about the quality and outcomes of operative cases. A performance measure that MPOG assesses for operative cases regards the minimization of the use of climate-sensitive anesthetic gases: [SUS-04 : Fresh Gas Flow, less than or equal to 2L/min](https://spec.mpog.org/Spec/Public/63).

## Personas

Deepa is a dedicated Certified Registered Nurse Anesthetist (CRNA) at Midwest Medicine, a medical-school affiliated hospital. She is committed to delivering the best possible care to her patients. She values the quality of patient care and always strives to improve it by working collaboratively with her team. Deepa is passionate about using data to enhance patient outcomes and regularly reviews feedback reports to identify areas for improvement. Deepa is specifically interested in knowing when her performance is worsening compared to her peers and goals. She values the insights that data can provide and prefers to receive feedback reports that are easy to interpret and act upon. Deepa prefers to receive feedback reports in the form of line charts, which allow her to easily visualize trends over time. She believes that line charts are more effective than other types of charts because they provide a clear and concise representation of data. 

Gaile is a resident at Midwest Medicine, a medical-school affiliated hospital. Gaile is always interested in improving their practice and continuing to learn to care for patients to the best of their ability. Gaile has not yet taken the preference survey, so an organizational preference profile of residents at Midwest Medicine is used to generate precision feedback for the group. The resident profile prioritizes positive encouragement with gain-framing messages so that those early in their career feel motivated to continue providing high quality care. The resident profile also prioritizes social comparison, as residents often want to know how they are performing relative to the group overall. Finally, visualizations that are easy to understand at a quick glance are also included, given the busy schedule and time constraints of this group.

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

## Recipient annotations
This data set should result in an annotation that there is information content about a positive performance trend for Alice:
1. Positive performance trend content (http://purl.obolibrary.org/obo/psdo_0000099)

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


