zvirata =["otter", "whale", "goose", "chipmunk", "fox", "sheep", "rabbit", "marten"]
sorted_zvirata = sorted(zvirata, key=lambda x: len(x))
print(sorted_zvirata)


mesta_populace =[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
podle_max_populace = sorted(mesta_populace, key= lambda x: x[0])
mesta_podle_abecedy = sorted(mesta_populace, key= lambda x: x[1])
print(podle_max_populace)
print(mesta_podle_abecedy)
