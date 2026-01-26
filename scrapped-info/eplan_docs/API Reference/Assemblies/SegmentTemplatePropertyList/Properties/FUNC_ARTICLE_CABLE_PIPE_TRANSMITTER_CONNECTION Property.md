# FUNC_ARTICLE_CABLE_PIPE_TRANSMITTER_CONNECTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1117.html

---

BACnet: Character set acc. to BACnet specification # 26652.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_CHARACTER_SET_ACCORDING_TO_BACNET_SPECIFICATION( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_CHARACTER_SET_ACCORDING_TO_BACNET_SPECIFICATION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Character set that fulfills the requirements of the BACnet specification.
