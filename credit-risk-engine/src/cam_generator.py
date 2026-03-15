from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import os


def generate_cam_pdf(row, decision, loan, interest, explanation):

    folder = "output/CAM_reports"
    os.makedirs(folder, exist_ok=True)

    filename = f"{folder}/{row['company_name']}_CAM.pdf"

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph("CREDIT APPRAISAL MEMO (CAM)", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1,20))

    company = Paragraph(f"<b>Company:</b> {row['company_name']}", styles['Heading3'])
    elements.append(company)
    elements.append(Spacer(1,20))


    character_data = [
        ["Character Factor","Value"],
        ["Promoter Reputation",row["promoter_reputation_score"]],
        ["Promoter Experience",f"{row['promoter_experience_years']} years"],
        ["CIBIL Score",row["cibil_score"]],
        ["Litigation Cases",row["litigation_cases_count"]],
    ]

    capacity_data = [
        ["Capacity Factor","Value"],
        ["GST Turnover",f"{row['gst_turnover_crore']} Cr"],
        ["Revenue Growth",f"{row['revenue_growth_percent']} %"],
        ["Profit Margin",f"{row['profit_margin_percent']} %"],
    ]

    capital_data = [
        ["Capital Factor","Value"],
        ["Net Worth",f"{row['net_worth_crore']} Cr"],
        ["Total Assets",f"{row['total_assets_crore']} Cr"],
        ["Debt to Equity",row["debt_to_equity_ratio"]],
    ]

    collateral_data = [
        ["Collateral Factor","Value"],
        ["Collateral Type",row["collateral_type"]],
        ["Collateral Value",f"{row['collateral_value_crore']} Cr"],
    ]

    conditions_data = [
        ["Conditions Factor","Value"],
        ["Industry Sector",row["industry_sector"]],
        ["Sector Risk",row["sector_risk_level"]],
        ["Market Demand",row["market_demand_trend"]],
    ]

    decision_data = [
        ["Final Decision","Value"],
        ["Loan Decision",decision],
        ["Loan Amount",f"{round(loan,2)} Cr"],
        ["Interest Rate",f"{interest} %"],
    ]

    # NEW SECTION → Explanation
    explanation_data = [
        ["Model Explanation"],
        [explanation]
    ]


    tables = [
        character_data,
        capacity_data,
        capital_data,
        collateral_data,
        conditions_data,
        decision_data
    ]


    for data in tables:

        t = Table(data, colWidths=[3*inch,3*inch])
        elements.append(t)
        elements.append(Spacer(1,20))


    # Add Explanation Section
    elements.append(Paragraph("<b>Model Explanation</b>", styles['Heading3']))
    elements.append(Spacer(1,10))
    elements.append(Paragraph(explanation, styles['BodyText']))
    elements.append(Spacer(1,20))


    pdf = SimpleDocTemplate(filename, pagesize=letter)
    pdf.build(elements)