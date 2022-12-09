import sys

FROM_DIR = './json_revealed'
TO_DIR   = './json'

to_id = int(sys.argv[1])

for id in range(0, to_id+1):
    cmd = "cp {}/{}.json {}/{}.json"
    print(cmd.format(FROM_DIR, id, TO_DIR, id))
