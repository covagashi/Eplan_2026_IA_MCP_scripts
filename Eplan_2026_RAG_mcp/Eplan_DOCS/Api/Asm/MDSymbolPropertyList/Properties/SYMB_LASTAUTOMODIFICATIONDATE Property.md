# SYMB_LASTAUTOMODIFICATIONDATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPropertyList~SYMB_LASTAUTOMODIFICATIONDATE().html

---

Modification date (automatic) # 16023.

Syntax

**C#**



public MDPropertyValue SYMB_LASTAUTOMODIFICATIONDATE {get; set;}

public:

property MDPropertyValue^ SYMB_LASTAUTOMODIFICATIONDATE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Date of last changes to the symbol. The time is output in the local time of the user in accordance with the set time zone.
