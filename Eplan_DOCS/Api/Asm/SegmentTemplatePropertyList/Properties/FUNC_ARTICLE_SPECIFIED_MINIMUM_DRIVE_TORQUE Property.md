# FUNC_ARTICLE_SPECIFIED_MINIMUM_DRIVE_TORQUE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1256.html

---

BACnet: Standard # 26517.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_STANDARD_BACNET_( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_STANDARD_BACNET_ {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Standard or international standard valid for BACnet.
