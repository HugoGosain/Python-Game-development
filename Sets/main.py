golden_island = {"gold coins", "ruby", "emerald", "map"}
silver_island = {"silver coins", "emerald", "pearl", "map"}

#combine
#union

# combine = golden_island.union(silver_island)
# print (combine)

# .intersection shows intersection

# common = golden_island.intersection(silver_island)
# print(common)

# anyvariable = golden_island.difference(silver_island)
# print(anyvariable)
anyvariable = silver_island.difference(golden_island)
print(anyvariable)

# anothervariable = golden_island.symmetric_difference(silver_island)
# print(anothervariable)
# adifferentvariable = silver_island.symmetric_difference(golden_island)
# print(adifferentvariable)

# empty set = words = set() and words is the set name