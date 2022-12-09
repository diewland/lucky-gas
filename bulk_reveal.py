import sys

FROM_DIR = './json_revealed'
TO_DIR   = './json'

minted_amount = int(sys.argv[1])

for id in range(0, minted_amount):
    cmd = "cp {}/{}.json {}/{}.json"
    print(cmd.format(FROM_DIR, id, TO_DIR, id))
