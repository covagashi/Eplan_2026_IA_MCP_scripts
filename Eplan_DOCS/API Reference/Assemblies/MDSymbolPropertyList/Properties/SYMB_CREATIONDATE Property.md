# SYMB_CREATIONDATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPropertyList~SYMB_CREATIONDATE().html

---

Creation date # 16021.

Syntax

**C#**



public MDPropertyValue SYMB_CREATIONDATE {get; set;}

public:

property MDPropertyValue^ SYMB_CREATIONDATE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Creation date of the symbol. The time is output in the local time of the user in accordance with the set time zone.
