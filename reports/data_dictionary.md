# fund_master

| Column      | Type    | Definition               |
|-------------|---------|--------------------------|
| amfi_code   | Integer | Unique AMFI scheme code  |
| scheme_name | Text    | Scheme name              |
| fund_house  | Text    | Asset management company |
| category    | Text    | Equity/Debt              |
| risk_grade  | Text    | Risk classification      |

---

# nav_history

| Column    | Type    | Definition        |
|-----------|---------|-------------------|
| amfi_code | Integer | Scheme identifier |
| date      | Date    | NAV date          |
| nav       | Decimal | Net Asset Value   |

---

# aum_by_fund_house

| column         | type     |  Defination           |
|----------------|----------|-----------------------|
| Date           | date     |  aum date             |
| fund_house     | Text     |  fund_institute name  |
| aum_lakh_crore | decimal  |  decimal value of fund|
| aum_core       | Integer  |  actual fund amount   |

# monthly sip inflows

| column           | Type     |  Defination             |
|------------------|----------|-------------------------|
| month            | date     |  month of the year      |
| sip_inflow_crore | Integer  |  inflow in integer      |
| column           | Type     |  Defination             |
| column           | Type     |  Defination             |
| column           | Type     |  Defination             |
| column           | Type     |  Defination             |

