from PIL import Image
import os

importDir = '2021-2022/'

def crop(infile, left, top, right, bottom):
    try:
        im = Image.open(infile)
        imgwidth, imgheight = im.size
        box1 = (left, top, right, bottom)
        box2 = (0, bottom, right, imgheight)
        yield im.crop(box1), im.crop(box2)
    except:
        errors.append(infile)


height = 450
width = 500
k = 0
errors = []
for infile in os.listdir(importDir):
    if infile.endswith(".png"):
        infile = importDir + infile
        for (comic, desc) in crop(infile, 0, 0, height, width):
            try:
                img=Image.new('RGB', (height, width), 255)
                img.paste(comic)
                path=os.path.join('./comics/', "comic-%s.png" % k)
                img.save(path)

                dwidth, dheight = desc.size
                words=Image.new('RGB',(dwidth, dheight), 255 )
                words.paste(desc)
                path=os.path.join('./descriptions', "desc-%s.png" % k)
                words.save(path)
                k += 1
            except:
                pass

print(str(len(errors)) + " images could not be split.")
print(errors)
print("done!")