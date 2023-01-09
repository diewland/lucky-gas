from pprint import pprint as pp

# read from file
lines = [ line.rstrip() for line in open('x') ]

# craft data
rows = []
for l in lines:
    data = l.split(' ')
    id = int(data[3])
    burn = data[-1][1:]
    rows.append((burn, id))

# sort
rows.sort(key=lambda x: x[0])

# url
url_os = "https://opensea.io/assets/optimism/0x75c8b866ac237a689bdbc1557e9dc0bd90200ed4/{}"
url_qx = "https://qx.app/asset/0x75c8b866aC237a689BDbc1557e9DC0Bd90200ED4/{}"

# print in csv
for r in rows:
    (b, id) = r
    v = "{}.{}".format(b[:2], b[2:])
    u1 = url_os.format(id)
    u2 = url_qx.format(id)
    print("{},{},{}".format(v, u1, u2))
