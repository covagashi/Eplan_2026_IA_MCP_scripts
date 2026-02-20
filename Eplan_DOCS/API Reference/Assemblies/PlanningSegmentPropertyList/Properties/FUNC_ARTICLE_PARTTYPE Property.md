# FUNC_ARTICLE_PARTTYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~FUNC_ARTICLE_PARTTYPE(Int32).html

---

Record type # 20103.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PARTTYPE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PARTTYPE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

At a function for the assigned part numbers, specifies the type of parts data or cross-part data, e.g., component, assembly, cable, housing, accessory list, drilling pattern, customer. A max. of 50 is allowed.
