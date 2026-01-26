# SYMBLIB_OLDNAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibraryPropertyList~SYMBLIB_OLDNAME().html

---

Name of original symbol library # 15098.

Syntax

**C#**



public MDPropertyValue SYMBLIB_OLDNAME {get; set;}

public:

property MDPropertyValue^ SYMBLIB_OLDNAME {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is used internally. It contains the name of the original symbol library if the symbol library has been converted. It is possible check whether the symbol library is compatible with an "old" EPLAN 5 symbol library.
