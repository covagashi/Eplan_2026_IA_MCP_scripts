# FUNC_ARTICLE_APPLICATION_RANGE_OF_THE_CONNECTION_CABLE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1111.html

---

Assembly structure # 20922.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ASSEMBLY_STRUCTURE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ASSEMBLY_STRUCTURE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.
