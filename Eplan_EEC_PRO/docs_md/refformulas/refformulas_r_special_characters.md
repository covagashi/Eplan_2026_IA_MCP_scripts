---
title: "Special characters"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_special_characters.htm"
file: "refformulas_r_special_characters"
category: "refformulas"
---

# Special characters

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Special characters If the result of a formula is not a single value of the type String, Integer, Double or Boolean it will be marked by special characters which enclose the collection (collection and map) as well as the single values. If it is a collection of values (collection), it is enclosed by square brackets: [ ] enclose a collection (List, Set, Bag), e.g. [1,2,3,4,5] If complex objects (components) are listet instead of values, each single object is enclosed by guillemets: Â«Â» enclose components (complex objects) of a list, e.g. [Â«St01RoundTableÂ»,Â«St02InsertingÂ»,Â«St07TransportÂ»] Key-value-pairs which are for example created by database queries are usually stored in maps. Here the keys are separated from the values by Â» and the key-value-pairs from each other by ||: Â» separates the key from the value, e.g. [Sensor1Â»0245] â here the map consists of only one key-value-pair! || separates the key-value-pairs from each other, e.g. [BerlinÂ»030||StuttgartÂ»0711||MunichÂ»089] For maps each value can be a single value, a collection or a map! Special characters for XML data The following XML-specific character sequences that stand for a special character are not supported in formulas: XML-specific character sequences | Special characters  
---|---  
&amp; | &  
&lt; | <  
&gt; | >  
&#13; | \r  
&#10; | \n  
&#09; | \t  
&quot; | \"  
In order to be able to use an XML-specific character sequence in formulas nevertheless, a parameter of the String type that stores the XML-specific character sequence has to be created. The string may not begin with the character = like a formula. This parameter can then be referenced in a formula. [Example of a formula with special characters:](javascript:void\(0\);)
    
        =$NameOfDocument + $xmlLineFeed + $DescriptionOfDocument

The following values are stored in the parameters:
     * $NameOfDocument: BillOfMaterial.pdf
     * $xmlLineFeed: &10;
     * $DescriptionOfDocument: Bill of material
Result:
    
        BillOfMaterial.pdf
    Bill of material
