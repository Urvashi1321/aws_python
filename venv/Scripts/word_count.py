import PyPDF2
import re
from collections import Counter

#Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page_num in range(len(pdf_reader.pages)):
        pages = pdf_reader.pages[page_num]
        text += pages.extract_text()
    return text

#Function to count unique words and their occurence
def count_unique_words(text):
    words = re.findall(r'\b\w+\b', text.lower()) #extract words and convert to lowercase
    word_count = Counter(words)
    return word_count

#Main program
if __name__ == "__main__":
    pdf_file_path = "EN_TECH Skill Level.pdf"
    with open(pdf_file_path, "rb") as pdf_file:
        pdf_text = extract_text_from_pdf(pdf_file)
        word_count = count_unique_words(pdf_text)

        #Sort words in alphabetical order
        sorted_word_count = dict(sorted(word_count.items()))
        #Print unique words and their occurence
        for word, count in sorted_word_count.items():
            print(f"{word}: {count}")