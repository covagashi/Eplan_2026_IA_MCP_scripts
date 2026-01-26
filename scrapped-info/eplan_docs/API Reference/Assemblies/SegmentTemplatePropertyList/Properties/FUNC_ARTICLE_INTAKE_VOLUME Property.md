# FUNC_ARTICLE_INTAKE_VOLUME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList~FUNC_ARTICLE_INTAKE_VOLUME(Int32).html

---

Intake volume # 26197.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_INTAKE_VOLUME( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_INTAKE_VOLUME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Volume of the air or gas drawn in by the device within a certain period. The value is specified in cubic meters (m³).
