DIR_INPUT = "./assets"
DIR_OUTPUT = "../lucky-gas-{}"

for id in range(0, 10_000):
    padded_id = "{:04}".format(id)
    cmd = "mv {}/{}.png ../lucky-gas-{}/".format(DIR_INPUT, padded_id, padded_id[0])
    print(cmd)
