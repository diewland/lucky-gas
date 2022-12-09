import json, glob
from pprint import pprint as pp

bulk = [ f for f in glob.glob('./json_revealed/*.json') ]

# generated value
v = []
for b in bulk:
    data = json.load(open(b))
    #print(b, data["name"], data["attributes"][0]["value"])
    v.append(data["attributes"][0]["value"])

v.sort()
#print(v)

# references
ref = [ "{:.2f}".format(r/100).zfill(5) for r in range(0, 10_000) ]
#print(ref)

print(v == ref)
