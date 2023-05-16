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
Bob's preference data: (TODO)

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


