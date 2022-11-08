from PIL import Image
from pprint import pprint as pp
from os.path import exists
import sys

DIR_INPUT = './traits'
DIR_OUTPUT = './assets'

from_id = int(sys.argv[1])
to_id = int(sys.argv[2])

for id in range(from_id, to_id+1):
    (t1, t2, t3, t4) = list("{:04}".format(id))

    outpath = "{}/{}{}{}{}.png".format(DIR_OUTPUT, t1, t2, t3, t4)
    print("{}...".format(outpath))

    layers = [
        Image.open("{}/{}.png".format(DIR_INPUT, "Enew")),
        Image.open("{}/t1{}.png".format(DIR_INPUT, t1)).convert("RGBA"), # P to RGBA
        Image.open("{}/t2{}.png".format(DIR_INPUT, t2)).convert("RGBA"), # P to RGBA
        Image.open("{}/t3{}.png".format(DIR_INPUT, t3)).convert("RGBA"), # P to RGBA
        Image.open("{}/t4{}.png".format(DIR_INPUT, t4)).convert("RGBA"), # P to RGBA
    ]
    new_img = Image.new("RGBA", layers[0].size)

    for layer in layers:
        #new_img.paste(layer, (0, 0), layer.convert('RGBA')) --- not good border
        #new_img.paste(layer, (0, 0), layer.convert('RGBa')) --- overlay bug
        new_img = Image.alpha_composite(new_img, layer)    # --- perfect!
    new_img.save(outpath, "PNG")
