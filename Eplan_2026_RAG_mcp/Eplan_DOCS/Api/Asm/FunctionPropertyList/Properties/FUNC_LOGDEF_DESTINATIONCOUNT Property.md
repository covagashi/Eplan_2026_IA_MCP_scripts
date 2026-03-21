# FUNC_LOGDEF_DESTINATIONCOUNT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_LOGDEF_DESTINATIONCOUNT(Int32).html

---

Connection point logic: Number of targets allowed # 20324.

Syntax

**C#**



public PropertyValue FUNC_LOGDEF_DESTINATIONCOUNT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_LOGDEF_DESTINATIONCOUNT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

The number of possible targets / connections that the connection point may have. Using the index, you can differentiate between up to 100 settings.
