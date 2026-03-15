import pandas as pd

def check_anomalies():

    gst = pd.read_csv("gst.csv")
    bank = pd.read_csv("bank.csv")

    # merge both datasets by month
    data = pd.merge(gst, bank, on="Month")

    issues = []

    for index, row in data.iterrows():

        revenue = row["Revenue"]
        deposit = row["Deposit"]

        # simple anomaly rule
        if deposit < revenue * 0.5:
            issues.append(f"Possible anomaly in {row['Month']} (Revenue: {revenue}, Deposit: {deposit})")

    return issues