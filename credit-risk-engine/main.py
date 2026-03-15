import pandas as pd

from src.scoring_model import calculate_score
from src.cam_generator import generate_cam_pdf
from src.recommendation_engine import loan_decision


df = pd.read_csv("data/synthetic_credit_companies_50.csv")

results = []

cam_reports = ""

for _, row in df.iterrows():

    score = calculate_score(row)

    # Updated line (now captures explanation)
    decision, loan, interest, explanation = loan_decision(score, row)

    # Pass explanation to CAM generator
    generate_cam_pdf(row, decision, loan, interest, explanation)

    results.append({
        "Company": row["company_name"],
        "Score": round(score, 2),
        "Decision": decision,
        "Loan Amount (Cr)": loan,
        "Interest Rate (%)": interest,
        "Explanation": explanation
    })

results_df = pd.DataFrame(results)

results_df.to_csv("output/results.csv", index=False)

with open("output/cam_reports.txt", "w") as f:
    f.write(cam_reports)

print("Processing Complete!")