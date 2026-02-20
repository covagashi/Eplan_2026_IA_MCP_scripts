# FUNC_ARTICLE_CABLE_ENTRY_INTO_THE_DEVICE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1114.html

---

Cable length, routed # 26398.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_CABLE_LENGTH_LAID( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_CABLE_LENGTH_LAID {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Routed length of the cable.
