# FUNC_ARTICLE_SERVICE_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLE_SERVICE_UNIT(Int32).html

---

Performance unit (bill of quantities) # 26430.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_SERVICE_UNIT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_SERVICE_UNIT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Measuring unit in which the output to be provided - in accordance with the performance catalog - is specified, for example cubic meter (m³) for concrete work or piece (unit) for individual items such as windows or doors. The bill of quantities describes all the services, materials and work that are required for a project or a procurement and serves as a basis for offers by suppliers or service providers.
