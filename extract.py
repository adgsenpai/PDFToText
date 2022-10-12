import cv2
from PIL import Image
from pytesseract import pytesseract
import glob

def extractTextFromImage(image):
    # Read the image file
    img = cv2.imread(image)
    # Convert the image to RGB
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #set the path to the tesseract folder
    pytesseract.tesseract_cmd = r'./Tesseract-OCR/tesseract.exe'
    # Load the Tesseract OCR engine
    text = pytesseract.image_to_string(rgb) 
    return text
    

# find all jpg files in the Pages folder
jpgs = glob.glob('Pages/*.jpg')

#sort jpgs by number
jpgs.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

print('Extracting text from', len(jpgs), 'images')

buffer = ''

c = 0
for jpg in jpgs:
    print('Extracting text from', jpg)
    try:
        buffer += extractTextFromImage(jpg)
        print('Extracted text from', jpg, '(', c, '/', len(jpgs), ')')
    except Exception as e:
        print('Error extracting text from', jpg)
        print(e)
    c += 1
        
# save buffer to text file
with open('output.txt', 'w') as f:
    f.write(buffer)