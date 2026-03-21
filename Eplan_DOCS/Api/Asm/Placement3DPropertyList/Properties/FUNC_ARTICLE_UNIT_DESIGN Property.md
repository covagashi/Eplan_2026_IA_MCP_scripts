# FUNC_ARTICLE_UNIT_DESIGN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLE_UNIT_DESIGN(Int32).html

---

Type of construction: Device # 26365.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_UNIT_DESIGN( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_UNIT_DESIGN {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Form of the housing and structure of the device. These specifications are, among other things, relevant for mounting and the operating location.
