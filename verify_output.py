import json, glob
from pprint import pprint as pp

bulk = [ f for f in glob.glob('./json/*.json') ]

v = []
for b in bulk:
    data = json.load(open(b))
    #print(b, data["name"], data["attributes"][0]["value"])
    v.append(data["attributes"][0]["value"])

v.sort()
pp(v)
