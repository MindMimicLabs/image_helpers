import analysis.my_colorsys as cs
import pathlib
import progressbar as pb # type: ignore
import random
import shutil
from PIL import Image

# the size and count of the images
w = 480
h = 320
n = 50000
color = True
seed = 0

# the location to save the images
color_text = 'color' if color else 'bw'
path = pathlib.Path(__file__).parent.joinpath(f"images/{color_text}/yiq")

# setup folder
if path.exists():
    shutil.rmtree(path)
path.mkdir(parents = True)

# fill the image with static
def generate_static(img: Image.Image, color: bool) -> None:
    y_rng = [0, 255]
    i_rng = [-151.9545, 151.9545]
    q_rng = [-133.2885, 133.2885]
    for w in range(img.width):
        for h in range(img.height):
            y = random.randint(y_rng[0], y_rng[1])
            if color:
                i = random.uniform(i_rng[0], i_rng[1])
                q = random.uniform(q_rng[0], q_rng[1])
            else:
                i = q = 0
            rgb = cs.yiq_to_rgb((y, i, q))
            img.putpixel((w, h), rgb)

# display settings
print(f'--- {n} {w}x{h} {color_text} images from YIQ (seed {seed})---')

# run the loop
random.seed(seed)
widgets = ['Color YIQ ', pb.Counter(), ' ', pb.Timer(), ' ', pb.BouncingBar(marker = '.', left = '[', right = ']')]
with pb.ProgressBar(widgets = widgets) as bar:
    bar.update(0) # type: ignore
    for cnt in range(n):
        with Image.new(mode = "RGB", size = (w, h)) as img:
            generate_static(img, color)
            img.save(path.joinpath(f'{cnt:05d}.png'))
            bar.update(cnt) # type: ignore
