# importing modules 
from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.pdfbase import pdfmetrics 
from reportlab.lib import colors 

def lines(text):

    textLines=text.split()  # Splitting at the White-Space delimiter
    Arr=[]
    temp=""
    for i in textLines:
        temp+=i
        temp+=" "
        if len(temp)>43:
             Arr.append(temp)
             temp=""

    return Arr


def export(text):
    fileName = 'Speech Data.pdf'
    documentTitle = 'Speech Analysis'
    title = 'Worderu, The Speech Analyzer'
    subTitle=str(input("Enter the Unique Heading for your data: "))
    #subTitle = 'The largest thing now!!'

    Arr=lines(text)
    textLines=Arr

# creating a pdf object 
    pdf = canvas.Canvas(fileName) 

# setting the title of the document 
    pdf.setTitle(documentTitle) 

    pdf.drawCentredString(300, 770, title) 

# creating the subtitle by setting it's font, 
# colour and putting it on the canvas 
    pdf.setFillColorRGB(0, 0, 255) 
    pdf.setFont("Courier-Bold", 24) 
    pdf.drawCentredString(290, 720, subTitle) 

# drawing a line 
    pdf.line(30, 710, 550, 710) 

# creating a multiline text using 
# textline and for loop 
    text = pdf.beginText(40, 680) 
    text.setFont("Courier", 18) 
    text.setFillColor(colors.black) 
    for line in textLines: 
        text.textLine(line) 
        pdf.drawText(text) 

# drawing a image at the 
# specified (x.y) position 
#pdf.drawInlineImage(image, 130, 400) 

# saving the pdf 
    pdf.save() 


#This Module is Working
