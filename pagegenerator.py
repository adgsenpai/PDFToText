import os
from pdf2image import convert_from_path
import glob

# find all pdf files in the current directory
pdfs = glob.glob('*.pdf')
pdf = pdfs[0]

pages = convert_from_path(pdf, 100)

# create 'Pages' folder
if not os.path.exists('Pages'):
    os.makedirs('Pages')
else:
    # delete all files in 'Pages' folder
    files = glob.glob('Pages/*')
    for f in files:
        os.remove(f)
    # create 'Pages' folder
    os.makedirs('Pages')
    
i = 1
for page in pages:
    print('Saving page', i)    
    image_name = "./Pages/"+"Page_" + str(i) + ".jpg"  
    page.save(image_name, "JPEG")
    i = i+1