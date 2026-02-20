# FUNC_ARTICLE_PLUG_CONNECTOR_CONNECTION_2 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PLUG_CONNECTOR_CONNECTION_2(Int32).html

---

Plug-in connector (connection 2) # 26578.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PLUG_CONNECTOR_CONNECTION_2( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PLUG_CONNECTOR_CONNECTION_2 {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specific details and properties of the plug-in connector at connection point 2, for example at a patch cable (prefabricated cable that is provided with plugs at both ends). Possible specifications are, for example, the type of plug connector, the material, etc.
