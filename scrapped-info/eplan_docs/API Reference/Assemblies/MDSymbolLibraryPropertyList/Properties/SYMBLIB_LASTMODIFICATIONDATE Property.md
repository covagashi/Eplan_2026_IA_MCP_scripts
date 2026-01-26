# SYMBLIB_LASTMODIFICATIONDATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibraryPropertyList~SYMBLIB_LASTMODIFICATIONDATE().html

---

Modification date (automatic) # 15023.

Syntax

**C#**



public MDPropertyValue SYMBLIB_LASTMODIFICATIONDATE {get; set;}

public:

property MDPropertyValue^ SYMBLIB_LASTMODIFICATIONDATE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Date of last change to the symbol library. The time is output in the local time of the user in accordance with the set time zone.
