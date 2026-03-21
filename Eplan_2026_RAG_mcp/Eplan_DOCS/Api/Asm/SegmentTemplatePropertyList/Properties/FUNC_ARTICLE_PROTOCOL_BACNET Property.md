# FUNC_ARTICLE_PROTOCOL_BACNET Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1233.html

---

Provision of cable # 26233.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PROVISION_OF_THE_CABLE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PROVISION_OF_THE_CABLE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specifies who is responsible for the provision of the cable. The cable can be provided as a separate component or can already be included in the scope of delivery of a device or system.
