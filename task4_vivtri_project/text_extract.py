# Install required libraries before running:
# pip install pdfplumber pytesseract pdf2image pillow

import pdfplumber
import pytesseract
from pdf2image import convert_from_path

def extract_text_from_pdf(pdf_path, output_file):
    extracted_text = ""

    try:
        # Try text-based extraction first
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    extracted_text += text + "\n"

        # If no text found, fallback to OCR
        if not extracted_text.strip():
            print(f"No text found in {pdf_path} with pdfplumber. Switching to OCR...")
            pages = convert_from_path(pdf_path)
            for page in pages:
                text = pytesseract.image_to_string(page)
                extracted_text += text + "\n"

    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")

    # Save extracted text to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(extracted_text.strip())

    print(f"✅ Extraction complete for {pdf_path}. Text saved to {output_file}")


# --- Process both dummy files ---
annual_report_pdf = r"C:/Users/Sanghamithra/Desktop/task4_vivtri_project/annual_report.pdf"       # Dummy Annual Report
gst_bank_pdf = r"C:/Users/Sanghamithra/Desktop/task4_vivtri_project/gst_bank_filing.pdf"          # Dummy GST/Bank Filing

annual_output = r"C:/Users/Sanghamithra/Desktop/task4_vivtri_project/Annual_Report_Extracted.txt" # Professional output file name
gst_output = r"C:/Users/Sanghamithra/Desktop/task4_vivtri_project/GST_Bank_Filing_Extracted.txt"  # Professional output file name

extract_text_from_pdf(annual_report_pdf, annual_output)
extract_text_from_pdf(gst_bank_pdf, gst_output)