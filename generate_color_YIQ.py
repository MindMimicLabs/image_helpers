import analysis.my_colorsys as cs
import pathlib
import progressbar as pb # type: ignore
import shutil
from PIL import Image
from random import randint, uniform

# the size and count of the images
w = 480
h = 320
n = 50000

# the location to save the images
path = pathlib.Path(__file__).parent.joinpath('images/color/yiq')

# setup folder
if path.exists():
    shutil.rmtree(path)
path.mkdir(parents = True)

y_rng = [0, 255]
i_rng = [-151.9545, 151.9545]
q_rng = [-133.2885, 133.2885]

widgets = ['Color YIQ ', pb.Counter(), ' ', pb.Timer(), ' ', pb.BouncingBar(marker = '.', left = '[', right = ']')]
with pb.ProgressBar(widgets = widgets) as bar:
    bar.update(0) # type: ignore
    for cnt in range(n):
        with Image.new(mode = "RGB", size = (w, h)) as img:
            img = img.convert("RGB")
            for w in range(img.width):
                for h in range(img.height):
                    y = randint(y_rng[0], y_rng[1])
                    i = uniform(i_rng[0], i_rng[1])
                    q = uniform(q_rng[0], q_rng[1])
                    rgb = cs.yiq_to_rgb((y, i, q))
                    img.putpixel((w, h), rgb)
            img.save(path.joinpath(f'{cnt:05d}.png'))
            bar.update(cnt) # type: ignore
