from pprint import pprint
s = "The common tern (Sterna hirundo) is a seabird with four subspecies breeding in temperate and subarctic regions of Europe, Asia and North America. This tern is migratory, wintering in warmer coastal regions. Adults have light grey upperparts, whiter underparts, a black cap, orange-red legs, and a narrow pointed black-tipped red or all-black bill. The bird nests on any flat bare surface close to water, including rafts. The nest is a scrape lined with whatever is available. It lays up to three blotchy camouflaged eggs, incubated by both sexes, that hatch in around 21 to 22 days. The downy chicks fledge in 22 to 28 days. This tern feeds by plunge-diving for fish in the sea or freshwater. Eggs and young are vulnerable to predation by mammals and large birds. The common tern's large population and huge breeding range mean that it is classed as being of least concern. Despite international protection, in some areas populations are threatened by habitat loss or the disturbance of breeding colonies."

d = {}
lst = s.split()
for w in lst:
    d[w] = d.get(w, 0) + 1

pprint(d)


lst1 = []
for w in lst:
    if w in lst1:
        continue

    lst1.append(w)

"""
    v = dict[key]
    v = dict.get(key)
    v = dict.get(key, def_value)
"""
