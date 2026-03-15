import pandas as pd

def calculate_score(row):

    # Character
    character = (
        row["promoter_reputation_score"] * 0.3 +
        row["promoter_experience_years"] * 0.2 +
        row["cibil_score"] * 0.3 -
        row["litigation_cases_count"] * 0.2
    )

    # Capacity
    capacity = (
        row["gst_turnover_crore"] * 0.3 +
        row["revenue_growth_percent"] * 0.3 +
        row["profit_margin_percent"] * 0.2 +
        row["loan_repayment_history_score"] * 0.2
    )

    # Capital
    capital = (
        row["net_worth_crore"] * 0.4 +
        row["total_assets_crore"] * 0.4 -
        row["debt_to_equity_ratio"] * 0.2
    )

    # Collateral
    collateral = row["collateral_value_crore"] * 0.5

    # Conditions
    conditions = 50 if row["market_demand_trend"] == "High" else 30

    total_score = (
        character * 0.25 +
        capacity * 0.30 +
        capital * 0.20 +
        collateral * 0.15 +
        conditions * 0.10
    )

    return total_score