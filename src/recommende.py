import pandas as pd

df = pd.read_csv(
    "../data/processed/scheme_performance_clean.csv"
)

risk = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

risk_map = {

    "Low": ["Low"],

    "Moderate": ["Moderate"],

    "High": ["High","Very High"]

}

filtered = df[

    df["risk_grade"]

    .isin(
        risk_map[risk]
    )

]

recommendations = (

    filtered

    .sort_values(
        "sharpe_ratio",
        ascending=False
    )

    .head(3)

)

print(

    recommendations[

        [

            "scheme_name",

            "risk_grade",

            "sharpe_ratio",

            "return_3yr_pct"

        ]

    ]

)

