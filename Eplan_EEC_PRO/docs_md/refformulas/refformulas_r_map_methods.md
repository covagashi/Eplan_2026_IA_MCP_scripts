---
title: "Map"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_map_methods.htm"
file: "refformulas_r_map_methods"
category: "refformulas"
---

# Map

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Map Maps is used for mapping of key-value pairs. Each key is contained in the map only once. Values may be included in any number in the map (except BidiMap). A use for maps is a dictionary (maps are therefore often referred to as dictionary). Here key is a word in the source language. Values are the terms in the target language or the target languages. Unlike lists of key-value pairs, the values can be efficiently accessed via the keys for a map. The position of the key in the map is determined by a so-called hash function. This ensures that the time required to access, is independent of the number of keys in the Map. For lists, however, the average access time is proportional to the number of objects in the list, as searching for keys must be performed by comparing the list entries with the key. There are different map types:  
    1. **Map:** Key-value pairs with disorderly keys.
    2. **OrderedMap:** Key-value pairs with ordered keys. Order criterion is the order of inserting the keys into the map.
    3. **BidiMap:** BidiMaps realize a bi-directional access, i.e. it can be either accessed efficiently with the key on the values and with the value of the associated key. Unlike the other maps each value can be included in the map only once.
It should be noted that the effort for the insertion of key-value pairs and the memory requirement of Map via OrderedMap to BidiMap increases. Therefore, OrderedMap and BidiMap should not generally be used, but only in justified cases. A SortedMap is not available as this can be mapped by <map>.keys.sortedBy(...). Note A short notation can be used to determine a value from a Map. The key is interpreted as a method that returns the value for this key. The following procedure is therefore possible: Map{Pair{'Hallo','hello'},Pair{'Welt','world'}}.Hallo returns hello. If the key is equal to an existing and usable name of a method (keys, isEmpty, notEmpty, size, values) the method is used.
