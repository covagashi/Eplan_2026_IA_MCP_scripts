# FUNC_ARTICLE_NUMBER_OF_BACNET_I_O_OBJECTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_NUMBER_OF_BACNET_I_O_OBJECTS(Int32).html

---

BACnet: Number of I/O objects # 26213.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_NUMBER_OF_BACNET_I_O_OBJECTS( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_NUMBER_OF_BACNET_I_O_OBJECTS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Number of all I/O objects in the BACnet protocol.
