from PIL import Image
from math import sqrt

initialImage = Image.open('test.png')
new_image = initialImage.resize((200, 200))
new_image.save('resized.png')

imagePath = 'resized.png'
newImagePath = 'output.png'
im = Image.open(imagePath)

COLORS = (
    (190, 0, 57),
    (255, 168, 0),
    (0, 163, 104),
    (126, 237, 86),
    (0, 158, 170),
    (54, 144, 234),
    (73, 58, 193),
    (129, 30, 159),
    (255, 56, 129),
    (109, 72, 47),
    (0, 0, 0),
    (212, 215, 217),
    (255, 69, 0),
    (255, 214, 53),
    (0, 204, 120),
    (0, 117, 111),
    (36, 80, 164),
    (81, 233, 244),
    (54, 144, 234),
    (106, 92, 255),
    (180, 74, 192),
    (255, 153, 170),
    (156, 105, 38),
    (137, 141, 144),
    (255, 255, 255)
)

GREENS = (
    (0, 163, 104),
    (0, 204, 120),
    (126, 237, 86)
)

REDS = (
    (0, 163, 104),
    (0, 204, 120),
    (126, 237, 86)
)

BLUES = (
    (0, 163, 104),
    (0, 204, 120),
    (126, 237, 86)
)

def closest_color(rgb):
    r, g, b = rgb
    color_diffs = []
    if(g > b and g > r):
        for color in GREENS:
            cr, cg, cb = color
            color_diff = sqrt((r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2)
            color_diffs.append((color_diff, color))
        return min(color_diffs)[1]

    for color in COLORS:
        cr, cg, cb = color
        color_diff = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]

def newImage (im):
    newimdata = []
    for color in im.getdata():
        color = [color[0],color[1],color[2]]
        newpixel = closest_color(color)
        newimdata.append(newpixel)

    print(newimdata)
    newim = Image.new(im.mode,im.size)
    newim.putdata(newimdata)
    return newim

newImage(im).save(newImagePath)