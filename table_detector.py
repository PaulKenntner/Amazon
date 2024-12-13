import pdfplumber
import json

def extract_tables_with_char_position(pdf_path):
    """
    Extract tables and their character positions from PDF
    """
    results = []
    char_count = 0
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            # Get text before table
            text = page.extract_text()
            
            # Get tables
            tables = page.extract_tables()
            
            # Store table with its character position
            if tables:
                results.append({
                    "page": page_num,
                    "char_position": char_count,
                    "tables": tables
                })
            
            # Add page text length to running count
            char_count += len(text)
    
    return results

# Example usage
pdf_path = "IUR_CROWD_TABLE.pdf" #tables found
#pdf_path = "25000100129734.pdf" # no tables found
tables_data = extract_tables_with_char_position(pdf_path)

with open("tables_output.json", "w") as f:
    json.dump(tables_data, f, indent=2)
# Print results
for data in tables_data:
    print(f"\nPage {data['page']}:")
    print(f"Character position: {data['char_position']}")
    print(f"Tables: {len(data['tables'])}")
