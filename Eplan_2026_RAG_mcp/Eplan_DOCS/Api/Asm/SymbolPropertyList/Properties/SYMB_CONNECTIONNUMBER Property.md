# SYMB_CONNECTIONNUMBER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList~SYMB_CONNECTIONNUMBER(Int32).html

---

Connection point number # 16001.

Syntax

**C#**



public PropertyValue SYMB_CONNECTIONNUMBER( 

   int index

) {get; set;}

public:

property PropertyValue^ SYMB_CONNECTIONNUMBER {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 100.

Internal connection point number. Either a consecutive number or a "n" (for a variable connection number) or a "z" (for the last connection point with a variable connection number).
