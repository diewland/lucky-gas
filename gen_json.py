import json, os, glob, random
from pprint import pprint as pp
 
NAME = "Lucky Gas"
DESC = "*****" # TODO TODO TODO
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
