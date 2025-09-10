import PyPDF2
import os
import re

def extract_text_from_pdf(file_path):
    """Extract text from PDF file"""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"

def analyze_invoice_simple(file_path):
    """Extract and parse specific data from PDF generically"""
    if not os.path.exists(file_path):
        return f"Error: File {file_path} not found"
    
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    
    # Extract text from PDF
    pdf_text = extract_text_from_pdf(file_path)
    
    # Clean up text
    clean_text = ' '.join(pdf_text.split())
    
    # Company name extraction
    company = "Not found"
    lines = [line.strip() for line in pdf_text.split('\n') if line.strip()]
    
    company_parts = []
    for line in lines:
        if (len(line) > 1 and 
            not any(word in line.lower() for word in ['www.', '@', 'project', 'invoice', 'number:', 'brand', 'design', 'marketing']) and
            not line.replace('-', '').replace('(', '').replace(')', '').replace(' ', '').isdigit()):
            company_parts.append(line)
        else:
            break
            
    if company_parts:
        company = ' '.join(company_parts[:3])
    
    # Invoice number extraction
    invoice_num = "Not found"
    invoice_patterns = [
        r'Invoice\s+Number:\s*([A-Z0-9-]+)',
        r'Invoice\s*#:\s*([A-Z0-9-]+)',
        r'INVOICE\s*#?\s*([A-Z0-9-]+)'
    ]
    for pattern in invoice_patterns:
        match = re.search(pattern, clean_text, re.IGNORECASE)
        if match:
            invoice_num = match.group(1)
            break
    
    # Amount extraction
    amount = "Not found"
    amount_patterns = [
        r'TOTAL[^$]*\$?([\d,]+\.?\d{2})',
        r'Total[^$]*\$?([\d,]+\.?\d{2})'
    ]
    for pattern in amount_patterns:
        match = re.search(pattern, clean_text)
        if match:
            amount = f"${match.group(1)}"
            break
    
    # Date extraction
    date = "Not found"
    date_pattern = r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),?\s+(\d{4})'
    match = re.search(date_pattern, clean_text)
    if match:
        date = f"{match.group(1)} {match.group(2)}, {match.group(3)}"
    
    return f"""Invoice Analysis Complete!
File: {file_name}
Size: {file_size/1024:.1f} KB

Company: {company}
Invoice Number: {invoice_num}
Amount: {amount}
Date: {date}

Analysis finished successfully!"""

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) >= 3 and sys.argv[1] == "analyze_invoice":
        file_path = sys.argv[2]
        result = analyze_invoice_simple(file_path)
        print(result)
    else:
        print("Usage: python main.py analyze_invoice <file_path>")