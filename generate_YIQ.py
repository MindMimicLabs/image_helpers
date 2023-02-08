import analysis.my_colorsys as cs
import pathlib
import progressbar as pb # type: ignore
import shutil
from PIL import Image
from random import randint, uniform, seed

# the size and count of the images
w = 480
h = 320
n = 50000
color = True

# the location to save the images
path = pathlib.Path(__file__).parent.joinpath(f"images/{'color' if color else 'bw'}/yiq")

# setup folder
if path.exists():
    shutil.rmtree(path)
path.mkdir(parents = True)

def generate_static(img: Image.Image, color: bool) -> None:
    y_rng = [0, 255]
    i_rng = [-151.9545, 151.9545]
    q_rng = [-133.2885, 133.2885]
    for w in range(img.width):
        for h in range(img.height):
            y = randint(y_rng[0], y_rng[1])
            if color:
                i = uniform(i_rng[0], i_rng[1])
                q = uniform(q_rng[0], q_rng[1])
            else:
                i = q = 0
            rgb = cs.yiq_to_rgb((y, i, q))
            img.putpixel((w, h), rgb)

seed(0)
widgets = ['Color YIQ ', pb.Counter(), ' ', pb.Timer(), ' ', pb.BouncingBar(marker = '.', left = '[', right = ']')]
with pb.ProgressBar(widgets = widgets) as bar:
    bar.update(0) # type: ignore
    for cnt in range(n):
        with Image.new(mode = "RGB", size = (w, h)) as img:
            generate_static(img, color)
            img.save(path.joinpath(f'{cnt:05d}.png'))
            bar.update(cnt) # type: ignore
