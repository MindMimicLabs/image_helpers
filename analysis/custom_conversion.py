# Question: is the custom color conversion reversible or near reversible?
# 1. Start with the digital RGB space (256 x 256 x 256)
# 2. Convert to analog YIQ space
# 3. Calculate the YIQ range
# 4. Reverse the YIQ range to RGB to check for (near)reversibility

import my_colorsys as cs

y_rng = [float('inf'), float('-inf')]
i_rng = [float('inf'), float('-inf')]
q_rng = [float('inf'), float('-inf')]
tot = 256 * 256 * 256
r1 = tot
r2 = tot
lim = 1

for r in range(256):
    for g in range(256):
        for b in range(256):
            (r_in, g_in, b_in) = (r, g, b)
            (y, i, q) = cs.rgb_to_yiq((r_in, g_in, b_in))
            (r_out, g_out, b_out) = cs.yiq_to_rgb((y, i, q))
            y_rng = (min(y_rng[0], y), max(y_rng[1], y))
            i_rng = (min(i_rng[0], i), max(i_rng[1], i))
            q_rng = (min(q_rng[0], q), max(q_rng[1], q))
            if not all([r_in == r_out, g_in == g_out, b_in == b_out]):
                r1 -= 1
            if not all([abs(r_in - r_out) <= lim, abs(g_in - g_out) <= lim, (b_in - b_out) <= lim]):
                r2 -= 1

print('--- using custom colors conversion ---')
print(f'Y: [{y_rng[0]}, {y_rng[1]}]')
print(f'I: [{i_rng[0]}, {i_rng[1]}]')
print(f'Q: [{q_rng[0]}, {q_rng[1]}]')
print(f'{100 * r1 / tot} % of the space is perfectly reversible ({r1}/{tot})')
print(f'{100 * r2 / tot} % of the space is near perfectly (diff <= {lim}) reversible ({r2}/{tot})')
