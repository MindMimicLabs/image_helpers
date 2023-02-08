import pathlib
import progressbar as pb # type: ignore
import shutil
from PIL import Image
from random import randint

# the size and count of the images
w = 480
h = 320
n = 50000

# the location to save the images
path = pathlib.Path(__file__).parent.joinpath('images/color/rgb')

# setup folder
if path.exists():
    shutil.rmtree(path)
path.mkdir(parents = True)

r_rng = [0, 255]
g_rng = [0, 255]
b_rng = [0, 255]

widgets = ['Color RGB ', pb.Counter(), ' ', pb.Timer(), ' ', pb.BouncingBar(marker = '.', left = '[', right = ']')]
with pb.ProgressBar(widgets = widgets) as bar:
    bar.update(0) # type: ignore
    for cnt in range(n):
        with Image.new(mode = "RGB", size = (w, h)) as img:
            img = img.convert("RGB")
            for w in range(img.width):
                for h in range(img.height):
                    r = randint(r_rng[0], r_rng[1])
                    g = randint(g_rng[0], g_rng[1])
                    b = randint(b_rng[0], b_rng[1])
                    img.putpixel((w, h), (r, g, b))
            img.save(path.joinpath(f'{cnt:05d}.png'))
            bar.update(cnt) # type: ignore
