---
title: "Collections (Collections Of Objects)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_collections.htm"
file: "refformulas_r_collections"
category: "refformulas"
---

# Collections (Collections Of Objects)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Collections (Collections Of Objects) The type Collection is an abstract superordinate class (superclass) of List, Set and Bag. The abstract superclass Collection can therefore not be used to generate collections. There are different types of collections:  
    1. **List:** Objects in a list have a defined sequence. Objects may appear multiple.
    2. **Set:** The objects in sets are not sorted, there is no defined sequence. Each object is contained in the set only once.
    3. **Bag:** The objects in bags are not sorted, there is no defined sequence. Objects may appear multiple.
Common applications for collections are the return values of the methods mos, rmos, dos, rdos (see the tutorial Eplan Electric P8 - [Use formulas for plugs, sockets, and PLC inputs](tutp8_h_assign_formulas_to_plugs_sockets_plc_inputs.htm)). You can apply general methods for collections to all types. Specific methods are also available for the derived types List, Set and Bag (see the following sections). [Generating Collections](javascript:void\(0\);) In most cases collections are returned from methods (see method [mos()](refformulas_r_mos_1.htm)). If in contrast collections should be created explicitly, the following syntax is used: <Collection-Type>{<Object1>,<Object2>,...} List, Set or Bag must be used for the <Collection-Type>. Example formula | Result  
---|---  
List {1,2,3} | [1, 2, 3]  
List {1,2,3,3} | [1, 2, 3, 3]  
List {1,2,3,3,List{4,5}} | [1, 2, 3, 3, [4, 5]]  
Set {1,2,3} | [2, 1, 3]  
Set {1,2,3,3} | [2, 1, 3]  
Set{1,2,3,3,List{4,5}} | [1, 2, 3, [4, 5]]  
Bag {1,2,3,3} | [2, 1, 3, 3]
