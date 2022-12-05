import json, os, glob, random
from pprint import pprint as pp
 
NAME = "Lucky Gas"
DESC = "Give away prizes up to 300$ every 9th of every month using the result of BURN ETH Volume 30 days from the website https://ultrasound.money/ Time reference by https://vclock.com/time/ 20.00 UTC+7 by using 4 digits to produce prize results XX.XX such as 12.34, 45.67, 80.34. Prizes distributed according to the amount held [1 Apetmism = 1$ (Max 10$) and + 50% Creator Fee] are prizes that luckyGas holders match the prizes drawn."
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
