from PIL import Image
from pprint import pprint as pp
from os.path import exists

DIR_INPUT = './traits'
DIR_OUTPUT = './assets'

for t1 in range(0, 10):
    for t2 in range(0, 10):
        for t3 in range(0, 10):
            for t4 in range(0, 10):

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
