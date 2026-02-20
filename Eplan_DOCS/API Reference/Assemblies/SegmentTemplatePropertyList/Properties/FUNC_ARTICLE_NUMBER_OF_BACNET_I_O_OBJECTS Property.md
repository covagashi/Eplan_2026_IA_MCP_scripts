# FUNC_ARTICLE_NUMBER_OF_BACNET_I_O_OBJECTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1195.html

---

BACnet: Number of hardware interfaces # 26215.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_NUMBER_OF_HW_INTERFACES_BACNET( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_NUMBER_OF_HW_INTERFACES_BACNET {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Number of hardware interfaces in the BACnet protocol.
