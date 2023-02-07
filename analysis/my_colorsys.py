# There is a built-in color package (colorsys) in Python.
# There is a built-in image package (PIL) in Python.
# Pixel values in PIL work in the range [0, 255]. 
# colorsys does not allow for rgb => yiq => rgb in PIL's range.
# the math is based on the formulas found [here](https://en.wikipedia.org/wiki/YIQ)
import typing as t

def rgb_to_yiq(rgb: t.Tuple[int, int, int]) -> t.Tuple[float, float, float]:
    y = 0.2990 * rgb[0] + 0.5870 * rgb[1] + 0.1140 * rgb[2]
    i = 0.5959 * rgb[0] - 0.2746 * rgb[1] - 0.3213 * rgb[2]
    q = 0.2115 * rgb[0] - 0.5227 * rgb[1] + 0.3112 * rgb[2]
    return (y, i, q)

def yiq_to_rgb(yiq: t.Tuple[float, float, float]) -> t.Tuple[int, int, int]:
    r = round(1 * yiq[0] + 0.956 * yiq[1] + 0.619 * yiq[2])
    g = round(1 * yiq[0] - 0.272 * yiq[1] - 0.647 * yiq[2])
    b = round(1 * yiq[0] - 1.106 * yiq[1] + 1.703 * yiq[2])
    return (r, g, b)
