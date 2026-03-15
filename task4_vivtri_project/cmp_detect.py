from Entity_extract import extract_financial_entities

# Run extraction first
annual_entities = extract_financial_entities("Annual_Report_Extracted.txt")
gst_entities = extract_financial_entities("GST_Bank_Filing_Extracted.txt")

def compare_entities(annual: dict, gst: dict) -> list:
    report = []
    for key, annual_val in annual.items():
        if key in gst:
            gst_val = gst[key]
            if annual_val == gst_val:
                report.append(f"✅ {key} matches: {annual_val}")
            else:
                report.append(f"⚠️ {key} mismatch: Annual = {annual_val}, GST = {gst_val}")
        else:
            report.append(f"ℹ️ {key} missing in GST filing")

    for key, gst_val in gst.items():
        if key not in annual:
            report.append(f"ℹ️ {key} present in GST but missing in Annual Report")

    return report

# Generate anomaly report
comparison_report = compare_entities(annual_entities, gst_entities)

print("\nAnomaly Detection Report:")
for line in comparison_report:
    print(line)