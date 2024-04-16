# Trend Detector

## Introduction
The trend detector function identifies changes in the performance level of a feedback recipient for a single measure or metric across time intervals. This function interprets trends as changes in the absolute rate of performance. 

The trend detector function receives performance data as input, and produces the following outputs:
1. Identification: Indicates the existence of a trend
2. Monotonicity: Classifies a trend as simple monotonic or nonmonotonic
3. Slope: 
	- Classifies the slope as negative or positive
	- Indicates magnitude of the trend (Range: 0 to 1)
4. Duration: Indicates the number of time intervals (i.e. months) that the trend spans

The output of the trend detector function is used by a precision feedback system to prioritize candidate messages.

## Example
The performance data below contains an example trend that can be detected by the Trend Signal Detector function:

|Month|Performance Level|Peer Average|75th Percentile Benchmark|90th Percentile Benchmark|Organizational Goal|
|-----|-----------------|------------|-------------------------|-------------------------|--|
|Oct  |       85%| 85| 88| 92|90|
|Nov  | ***85%***| 85| 88| 92|90|
|Dec  | ***91%***| 85| 88| 92|90|

- For the month of December, this performance data will generate a positive trend signal. The magnitude of the trend will be evaluated as 3, the formula below denotes how this magnitude is determined:
     - trend magnitude = (month t0 - month t2)/2
     - trend magnitude = **(91 - 85)/2 = 3**

## Implementation
The method operates with the following formula:
time1 performance - time2 performance / 2

## Signal detection criteria
The following criteria must be met for a trend to be detected:

1. The recipient's performance level must differ between the current month and the previous month.



## Test cases
These test cases are based on the following performance dataset header:

      ["staff_number","measure","month","passed_count","flagged_count","denominator","peer_average_comparator","peer_75th_percentile_benchmark","peer_90th_percentile_benchmark", "MPOG_goal"],

1. A trend is detected in these cases:

      [3,"PUL01","2023-01-01",1,0,0,1,2,9,90],
      [3,"PUL01","2023-02-01",40,0,0,40,42,6,90],
      [3,"PUL01","2023-03-01",100,0,0,100,33,99,90],

      [3,"PUL01","2023-01-01",99,0,0,18,2,9,90],
      [3,"PUL01","2023-02-01",98,0,0,48,42,6,90],
      [3,"PUL01","2023-03-01",97,0,0,1,33,99,90],

      [3,"PUL01","2024-02-01",78,0,0,100,88,9,90],
      [3,"PUL01","2024-03-01",18,0,0,40,42,68,90],
      [3,"PUL01","2024-04-01",17,0,0,100,33,99,90],


2. No trend is detected in these cases:

      [3,"PUL01","2023-01-01",1,0,0,1,22,19,90],
      [3,"PUL01","2023-02-01",1,0,0,40,2,76,90],
      [3,"PUL01","2023-03-01",1,0,0,10,33,9,90],

      [3,"PUL01","2023-01-01",99,0,0,1,2,9,90],
      [3,"PUL01","2023-02-01",99,0,0,40,42,6,90],
      [3,"PUL01","2023-03-01",99,0,0,100,33,99,90],

      [3,"PUL01","2024-02-01",78,0,0,1,2,9,90],
      [3,"PUL01","2024-03-01",78,0,0,40,42,6,90],
      [3,"PUL01","2024-04-01",78,0,0,100,33,99,90],

