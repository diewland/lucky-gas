import json, os, glob, random
from pprint import pprint as pp
 
NAME = "Lucky Gas"
DESC = "Every month on the 9th of the month at 1pm UTC, we will use the result of BURN ETH Volume 30 days from https://ultrasound.money/ (reference time from https://vclock.com/time/) by using 4 digits to produce award results XX.XX such as 12.34, 45.67 or 80.34. Prizes are granted based on the number of Apetmism NFTs held (1 Apetmism NFT = 1$ (Max 10$) plus 50% Creator Fee). Prizes of up to $300 are available to LuckyGas holders."
IMG = "https://diewland.github.io/lucky-gas/assets/unrevealed.png"
ENGINE = "Jigsaw Engine"

OUTPUT_DIR = "./json"
MAX_SUPPLY = 10_000

# craft metadata
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

# build json + write to file
for id in range(0, MAX_SUPPLY):

    # update data
    metadata["name"] = "{} #????".format(NAME, id)
    metadata["image"] = IMG
    metadata["attributes"][0]["value"] = "??.??"

    # debug
    #print(metadata)

    # write file
    with open("./{}/{}.json".format(OUTPUT_DIR, id), "w") as f:
        json.dump(metadata, f, ensure_ascii=False)
