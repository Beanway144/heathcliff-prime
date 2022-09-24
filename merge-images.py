from PIL import Image
import os
import random

comics = os.listdir('./comics').copy()
descs = os.listdir('./descriptions').copy()
comics = list(filter((lambda x: x.endswith('.png')), comics))
descs = list(filter((lambda x: x.endswith('.png')), descs))

for i in range(0, 100):
    im = Image.new('RGB', (450, 550))
    comic = Image.open("./comics/" + random.choice(comics))
    im.paste(comic)
    desc = Image.open("./descriptions/" + random.choice(descs))
    im.paste(desc, (0, 500))
    path=os.path.join('./primes', "prime-%s.png" % i)
    im.save(path)
