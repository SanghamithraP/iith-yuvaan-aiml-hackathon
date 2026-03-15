import re

def extract_financial_entities(file_path: str) -> dict:
    entities = {}

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Patterns: keyword + value together
    patterns = {
        "Turnover": r"Turnover\s*[:\-]?\s*₹?\d+(\.\d+)?\s*Crores?",
        "Revenue": r"Revenue\s*[:\-]?\s*₹?\d+(\.\d+)?\s*Crores?",
        "Net Profit": r"Net Profit\s*[:\-]?\s*₹?\d+(\.\d+)?\s*Crores?",
        "Loan Obligations": r"Loan Obligations\s*[:\-]?\s*₹?\d+(\.\d+)?\s*Crores?",
        "Cash Flow (Operations)": r"Cash Flow \(Operations\)\s*[:\-]?\s*₹?\d+(\.\d+)?\s*Crores?",
        "Cash Flow (Financing)": r"Cash Flow \(Financing\)\s*[:\-]?\s*₹?\d+(\.\d+)?\s*Crores?"
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            # Extract only the currency part
            value_match = re.search(r"₹?\d+(\.\d+)?\s*Crores?", match.group(0))
            if value_match:
                entities[key] = value_match.group(0)

    return entities


# --- Run on your files ---
annual_entities = extract_financial_entities(
    r"C:\Users\Sanghamithra\Desktop\task4_vivtri_project\Annual_Report_Extracted.txt"
)
gst_entities = extract_financial_entities(
    r"C:\Users\Sanghamithra\Desktop\task4_vivtri_project\GST_Bank_Filing_Extracted.txt"
)

print("Annual Report Entities:", annual_entities)
print("GST/Bank Filing Entities:", gst_entities)