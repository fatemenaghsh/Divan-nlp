import glob
import pdf2image
import pytesseract
from PIL import Image
from pathlib import Path
import fitz,sys
#import PyMuPDF

pdffile = 'divan/divan.pdf'
directory = '/Users/fatemenaghshvarian/PycharmProjects/pythonProject2/feyzi'
def pdf2image(pdffile):
    zoom_x = 2.0  # horizontal zoom
    zoom_y = 2.0  # vertical zoom
    mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension
    doc = fitz.open(pdffile)
    for page in doc:
        pix = page.get_pixmap(matrix=mat)
        pix.save("page-%i.png" % page.number)

def img2txt ():
    imgs = Path(directory).glob('*.png')
    for img in imgs:
        png= Image.open(img)
        data = pytesseract.image_to_string(png, lang='fas', config='--psm 6')
        print(data, file=open('extract-text.txt',"a",encoding="utf-8"))

pdf2image(pdffile),img2txt()

#images = pdf2image.convert_from_path("divan/divan.pdf")
#for i in range(len(images)):
    # Save pages as images in the pdf
    #images[i].save('page' + str(i) + '.jpg', 'JPEG')
#images = glob.glob("./feyzi/*.jpg")
#for image in images:
    #img = Image.open(image)
    #data = pytesseract.image_to_string(img, lang='fas')
    #with open ('test.txt','a') as f:
        #f.write(data)
        #print(f.open('test.txt'))
    #print(data, file=open('extract-text.txt',"a"))
    #print(data)

#imq= "page8.jpg"
#imq1= Image.open(imq)
#ocr_result = pytesseract.image_to_string(imq1, lang='fas')
#print(ocr_result)

# img = Image.open(images)

# ocr_result = pytesseract.image_to_string(img, lang='fas')
# print(ocr_result)
