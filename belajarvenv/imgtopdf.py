from PIL import Image
img = Image.open('histogram.png')
img.convert('RGB').save('versiPDF.pdf')
