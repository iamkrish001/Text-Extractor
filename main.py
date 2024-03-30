import os
from pdf2image import convert_from_path
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# Path to your PDF file
pdf_file_path = 'C:/Users/ASUS/OneDrive/Documents/test.pdf'

# Path to the directory where you want to save the extracted text file
output_text_file_path = 'C:/Users/ASUS/OneDrive/Documents/convertedpdf.txt'

# Convert PDF to images
pages = convert_from_path(pdf_file_path)

# List to store extracted text from each page
extracted_text = []

# Iterate through each page and perform OCR
for page_number, page_image in enumerate(pages):
    # Perform OCR on the page image
    page_text = pytesseract.image_to_string(page_image, lang='eng')
    # Append the extracted text to the list
    extracted_text.append(page_text)

# Join the extracted text from all pages
all_text = "\n".join(extracted_text)

# Write the extracted text to a text file
with open(output_text_file_path, 'w', encoding='utf-8') as text_file:
    text_file.write(all_text)

print("Text extraction completed. Output saved to:", output_text_file_path)
