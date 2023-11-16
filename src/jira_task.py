import re
import PyPDF2

def categorize_data(pdf_path):
    data_dict = {}
    current_key = None
    current_value = ""

    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        total_pages = pdf_reader.numPages

        for page_num in range(total_pages):
            page = pdf_reader.getPage(page_num)
            text = page.extractText()

            # Define the regular expression pattern
            pattern = re.compile(r'^\d+\.\s*\n\n', re.MULTILINE)

            # Find matches in the text
            matches = pattern.finditer(text)

            for match in matches:
                # Extract the key
                current_key = text[match.start():match.end()].strip()

                # Extract the value until the next key
                if current_key is not None:
                    start_index = match.end()
                    
                    try:
                        # Try to get the next match's start index
                        end_index = next(matches).start()
                    except StopIteration:
                        # If no more matches, set end_index to None
                        end_index = None

                    current_value = text[start_index:end_index].strip()

                    # Store the key-value pair in the dictionary
                    data_dict[current_key] = current_value

    return data_dict

# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_path = 'your_pdf_file.pdf'
result = categorize_data(pdf_path)

# Print the result
for key, value in result.items():
    print(f"{key}: {value}")


