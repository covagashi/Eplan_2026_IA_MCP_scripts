# SYMB_PROPERTYINSTANCESET Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList~SYMB_PROPERTYINSTANCESET(Int32).html

---

Property arrangements # 16050.

Syntax

**C#**



public PropertyValue SYMB_PROPERTYINSTANCESET( 

   int index

) {get; set;}

public:

property PropertyValue^ SYMB_PROPERTYINSTANCESET {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 64.

Contains multi-language designations for user-defined sets of properties (max. 64).
