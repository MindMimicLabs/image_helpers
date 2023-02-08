# Question: what part of the YIQ color space is not addressable as RGB
# 1. Start with the analog YIQ space [0, 255] x [-151.9545, 151.9545] x [-133.2885, 133.2885]
# 2. Sample 4 x 256 x 256 x 256 times from the space
# 3. Convert from  YIQ to RGB
# 4. Check to see if the RGB is outside the bounds of [0, 255]

import my_colorsys as cs
from random import randint, uniform

y_rng = [0, 255]
i_rng = [-151.9545, 151.9545]
q_rng = [-133.2885, 133.2885]
tot = 4 * 256 * 256 * 256
good = tot

for _ in range(tot):
    y = randint(y_rng[0], y_rng[1])
    i = uniform(i_rng[0], i_rng[1])
    q = uniform(q_rng[0], q_rng[1])
    (r, g, b) = cs.yiq_to_rgb((y, i, q))
    if not all([0 <= r, r < 256, 0 <= g, g < 256, 0 <= b, b < 256]):
        good -= 1

print(f'{100 * good / tot} % of the YIQ space is addressable as RGB ({good}/{tot})')
