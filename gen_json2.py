import json, os, glob, random
from datetime import datetime
from pprint import pprint as pp
 
NAME = "Lucky Gas"
DESC = "Every month on the 9th of the month at 1pm UTC, we will use the result of BURN ETH Volume 30 days from https://ultrasound.money/ (reference time from https://vclock.com/time/) by using 4 digits to produce award results XX.XX such as 12.34, 45.67 or 80.34. Prizes are granted based on the number of Apetmism NFTs held (1 Apetmism NFT = 1$ (Max 10$) plus 50% Creator Fee). Prizes of up to $300 are available to LuckyGas holders."
IMG = "https://diewland.github.io/lucky-gas-{}/{}.png"
ENGINE = "Jigsaw Engine"

OUTPUT_DIR = "./json"
MAX_SUPPLY = 10_000
SHUFFLE_TIME = 99

# helper
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))
def now():
    return format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# build chunk
chunk = []
for id in range(0, MAX_SUPPLY):

    # template
    metadata = {
      "name": "***",
      "description": DESC,
      "image": "***",
      "attributes": [
        {
          "trait_type": "Volume",
          "value": "***",
        },
      ],
      "compiler": ENGINE,
    }

    # update data
    pid = "{:04}".format(id)
    metadata["name"] = "{} #{}".format(NAME, pid)
    metadata["image"] = IMG.format(pid[0], pid)
    metadata["attributes"][0]["value"] = "{}.{}".format(pid[:2], pid[2:])

    # add to chunk
    chunk.append(metadata)

# shuffle
for rnd in range(1, SHUFFLE_TIME+1):
    random.shuffle(chunk)
    # log
    print("<{}> shuffle #{:02}".format(now(), rnd))
    for cc in chunker(chunk, 25):
        print('-'.join([ c['name'].split('#')[1] for c in cc ]))
    print('')

# write file
for id, metadata in enumerate(chunk):
    with open("./{}/{}.json".format(OUTPUT_DIR, id), "w") as f:
        json.dump(metadata, f, ensure_ascii=False)
    # log
    print("<{}> ID {:04} -> {}".format(now(), id, metadata['name']))
