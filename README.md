# Static as PNG

Generate RGB static and save that as an image

# Process

The image of an old black-and-white TV in horror films is ubiquitous.
This project aims to create digital snapshots of that experience both in black-and-white as well as in color. 

**Steps**

1. Generate random numbers
2. Interpret those values as [NTSC](https://en.wikipedia.org/wiki/NTSC) values.
   NTSC uses [YIQ](https://en.wikipedia.org/wiki/YIQ) as the color space
3. Convert YIQ to RGB
4. Save the images as a PNG
5. Repeat

**Options**

* _~/generate_color_YIQ.py_ works as described above
* _~/generate_bw_YIQ.py_ forces the I and Q channels to 0 creating a black-and-white image
* _~/generate_color_RGB.py_ creates random values for RGB directly

# Discussion

The color space computers generally use is RGB.
RGB is a digital color space.
It has three discrete channels all of which are represented as integers ([0, 255]).

The color space old TVs used in the US was NTSC (A.K.A. YIQ).
YIQ is _not_ a digital color space.
It was _meant_ for analog.
This means there are going to be issues that crop up.
Look at the different files in _~/analysis_ for implications.

**Results**

1. Using the built-in color space conversion
   * The RGB space must be [0, 1] for `colorsys.yiq_to_rgb()` to even make sense
   * The RGB space [0, 1] x [0, 1] x [0, 1] converts to the YIQ space [0.0, 1.0] x [-0.599, 0.599] x [-0.5251, 0.5251]
   * 12.99 % of the space is perfectly reversible
   * 100 % of the space is near perfectly (difference <= 1/256) reversible
2. Using the custom color space conversion `my_colorsys`
   * The RGB space is [0, 255]
   * The RGB space [0, 255] x [0, 255] x [0, 255] converts to the YIQ space [0, 255] x [-151.9545, 151.9545] x [-133.2885, 133.2885]
   * 100 % of the space is perfectly reversible
3. Thanks to [clamping](https://en.wikipedia.org/wiki/Clamping_(graphics)) 100 % of the YIQ space is addressable as RGB
