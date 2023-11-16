import PyPDF2
import re

def categorize_pdf_data(pdf_path):
    data_dict = {}
    root_cause_flag = False
    current_key = None

    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = pdf_reader.numPages

        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text = page.extractText()

            # Define the regular expression pattern
            pattern = re.compile(r'(\d+\.\s.*?)(?=\sDescription|$)')

            # Find all matches in the page text
            matches = re.finditer(pattern, text)

            for match in matches:
                key = match.group(1).strip()

                if 'Description' in key:
                    root_cause_flag = True
                    current_key = key.replace('Description', '').strip()
                    data_dict[current_key] = ''
                elif not root_cause_flag:
                    current_key = key
                    data_dict[current_key] = ''
                else:
                    # Append the matched text to the current key's value
                    data_dict[current_key] += match.group(1).strip() + '\n'

    return data_dict

# Example usage
pdf_path = 'your_pdf_file.pdf'
result = categorize_pdf_data(pdf_path)
print(result)
