# SYMB_PROPERTYINSTANCESET Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPropertyList~SYMB_PROPERTYINSTANCESET(Int32).html

---

Property arrangements # 16050.

Syntax

**C#**



public MDPropertyValue SYMB_PROPERTYINSTANCESET( 

   int index

) {get; set;}

public:

property MDPropertyValue^ SYMB_PROPERTYINSTANCESET {

   MDPropertyValue^ get(int index);

   void set (int index, MDPropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 64.

Contains multi-language designations for user-defined sets of properties (max. 64).
