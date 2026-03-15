def loan_decision(score, row):

    collateral_value = row["collateral_value_crore"]
    turnover = row["gst_turnover_crore"]

    loan_amount = min(collateral_value * 0.4, turnover * 0.25)

    reasons = []

    # Risk factor checks (for explanation)

    if row["litigation_cases_count"] > 0:
        reasons.append("litigation risk identified during secondary research")

    if row["cibil_score"] < 650:
        reasons.append(f"low CIBIL score ({row['cibil_score']})")

    if row["debt_to_equity_ratio"] > 1:
        reasons.append("high leverage (debt-to-equity above ideal range)")

    if row["market_demand_trend"] == "declining":
        reasons.append("declining market demand in the industry")

    if row["gst_turnover_crore"] > 5:
        reasons.append("strong GST turnover supporting repayment capacity")

    # Decision logic (your original logic kept)

    if score >= 80:
        decision = "Approve"
        interest = 10

    elif score >= 65:
        decision = "Approve with Conditions"
        interest = 11.5

    elif score >= 50:
        decision = "High Risk"
        interest = 14

    else:
        decision = "Reject"
        loan_amount = 0
        interest = 0

    # If no specific risks found
    if not reasons:
        reasons.append("overall financial indicators within acceptable range")

    # Explanation text generation

    if decision == "Reject":
        explanation = f"Rejected due to {', '.join(reasons)} despite strong GST flows."

    elif decision == "High Risk":
        explanation = f"High risk lending due to {', '.join(reasons)}."

    elif decision == "Approve with Conditions":
        explanation = f"Approved with conditions due to {', '.join(reasons)}."

    else:
        explanation = f"Approved due to strong financial indicators including {', '.join(reasons)}."

    return decision, loan_amount, interest, explanation