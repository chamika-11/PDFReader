import PyPDF2
from pdf2image import convert_from_path
import pdfplumber
import io
from PIL import Image



#extract the data from the pdf file
def extract_content_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:

        #extract the data from the pdf file
        reader = PyPDF2.PdfReader(file)
        text=""
        for page_num in range(len(reader.pages)):   
            page=reader.pages[page_num]
            text += page.extract_text()


    # Specify the Poppler path manually
        poppler_path = r"C:/poppler/Library/bin"


    #extract the image from the pdf file
    pages=convert_from_path(pdf_path,300,poppler_path=poppler_path)#DPI quality
    image_files=[]
    for i,page in enumerate(pages):
        image_file=f"page_{i+1}.jpg"
        page.save(image_file,'JPEG')
        image_files.append(image_file)

    return text,image_files



pdf_path = 'true-pdf-sample-1.pdf'
text,image=extract_content_from_pdf(pdf_path)
print(text)
print(image)
