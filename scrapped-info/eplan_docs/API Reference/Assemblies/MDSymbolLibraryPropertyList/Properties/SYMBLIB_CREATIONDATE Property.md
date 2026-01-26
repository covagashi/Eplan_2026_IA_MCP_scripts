# SYMBLIB_CREATIONDATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibraryPropertyList~SYMBLIB_CREATIONDATE().html

---

Creation date # 15021.

Syntax

**C#**



public MDPropertyValue SYMBLIB_CREATIONDATE {get; set;}

public:

property MDPropertyValue^ SYMBLIB_CREATIONDATE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Creation date of the symbol library. The time is output in the local time of the user in accordance with the set time zone.
