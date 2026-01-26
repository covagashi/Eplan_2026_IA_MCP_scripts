# FUNC_ARTICLE_SECONDARY_CASING_PRESSURE_STAGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic451.html

---

Pressure level of secondary housing # 26262.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_SECONDARY_CASING_PRESSURE_STAGE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_SECONDARY_CASING_PRESSURE_STAGE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specification of the nominal pressure of the secondary housing of a process measuring instrument.
