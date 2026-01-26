# FUNC_LOGDEF_BRIDGECOUNT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_LOGDEF_BRIDGECOUNT(Int32).html

---

Connection point logic: Number of saddle jumpers allowed # 20325.

Syntax

**C#**



public PropertyValue FUNC_LOGDEF_BRIDGECOUNT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_LOGDEF_BRIDGECOUNT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Number of possible saddle jumpers for terminals. Using the index, you can differentiate between up to 100 settings.
