# FUNC_ARTICLE_PUMPING_VOLUME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_PUMPING_VOLUME(Int32).html

---

Transport volume # 26329.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PUMPING_VOLUME( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PUMPING_VOLUME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Volume of the material or liquid that can or should be conveyed.
