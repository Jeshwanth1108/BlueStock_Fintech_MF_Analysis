# Day 1 Data Quality Summary

## Dataset Overview

Total Datasets: 10

Total Schemes: 40

NAV Records: 46,000

Investor Transactions: 6,599

Portfolio Holdings: 322

Benchmark Records: 5,999



## Validation Results

### AMFI Code Validation

Total Scheme Codes in fund_master: 40

Total Scheme Codes in nav_history: 40

Matching Codes: 40

Missing Codes: 0

Coverage: 100%

---

## Missing Values

Only one dataset contains missing values:

monthly_sip_inflows.csv

Column:
yoy_growth_pct

Missing Count:
12

Reason:
Initial months do not have prior year values.



## Data Quality Status

No duplicate AMFI codes.

No orphan NAV records.

No major datatype inconsistencies.

No critical data quality issues detected.