# Attending Template Data
Data for: Alice  Fahad
## Six month block
Six month section of data, formatted for markdown use (vignette performance data sections)

|Month|Performance Level|Top 10% Benchmark|Peer Average|
|-----|-----------------|-----------------|------------|
|Jul  |              90%|               94|          90|
|Aug  |              90%|               94|          90|
|Sept |              90%|               94|          90|
|Oct  |              90%|               94|          90|
|Nov  |              **XX%**|               94|          90|
|Dec  |              **XX%**|               94|          90|
## Twelve month block
Data formatted for JSON file entry
  - note: confirm twelve months of data sufficient for pipeline operations
  - note: data needs to be cleaned, WIP
***To prepare template for JSON entry:***
  1 - `shft`+`ctrl`+`f` find/replace `staffID` with the ID # for the persona you are editing
  2 - `shft`+`ctrl`+`f` find/replace `MSR1` with appropriate measure name (eg `SUS04`)
  3 - Edit critical months (December, November) with appropriate data for message acceptance criteria
  
"Performance_data":[
    ["staff_number","measure","month","passed_count","flagged_count","denominator","peer_average_comparator","peer_90th_percentile_benchmark","peer_75th_percentile_benchmark", "MPOG_goal"],
    [staffID,"MSR1","2023-01-01",NumNumb,DenNumb,100,p_avg,ninety,sevenfive,Pogger],
    [staffID,"MSR1","2023-02-01",NumNumb,DenNumb,100,p_avg,ninety,sevenfive,Pogger],
    [staffID,"MSR1","2023-03-01",NumNumb,DenNumb,100,p_avg,ninety,sevenfive,Pogger],
    [staffID,"MSR1","2023-04-01",NumNumb,DenNumb,100,p_avg,ninety,sevenfive,Pogger],
    [staffID,"MSR1","2023-05-01",NumNumb,DenNumb,100,p_avg,ninety,sevenfive,Pogger],
    [staffID,"MSR1","2023-06-01",NumNumb,DenNumb,100,p_avg,ninety,sevenfive,Pogger],
    [staffID,"MSR1","2023-07-01",NumNumb,DenNumb,100,p_avg,ninety,sevenfive,Pogger],
    [staffID,"MSR1","2023-08-01",NumNumb,DenNumb,100,p_avg,ninety,sevenfive,Pogger],
    [staffID,"MSR1","2023-09-01",NumNumb,DenNumb,100,p_avg,ninety,sevenfive,Pogger],
    [staffID,"MSR1","2023-10-01",NumNumb,DenNumb,100,p_avg,ninety,sevenfive,Pogger],
    [staffID,"MSR1","2023-11-01",CritNum,CritDen,100,p_avg,ninety,sevenfive,Pogger],
    [staffID,"MSR1","2023-12-01",CritNum,CritDen,100,p_avg,ninety,sevenfive,Pogger],
  ],

# Resident Template Data
Data for: Chikondi  Eugene  Gaile
## Six month block

## Twelve month block
# CRNA Template Data
Data for: Bob   Deepa
## Six month block

## Twelve month block
