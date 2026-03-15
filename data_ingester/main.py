from extract_pdf import extract_text
from analyze_text import extract_financial_info
from detect_anomaly import check_anomalies

print("Starting program...")

print("Reading PDF...")
text = extract_text("sample.pdf")

print("Analyzing document with AI...")
info = extract_financial_info(text)

print("Document Analysis:")
print(info)

print("Checking GST vs Bank anomalies...")
anomalies = check_anomalies()

print("Transaction Analysis:")

for a in anomalies:
    print(a)

print("Program finished.")