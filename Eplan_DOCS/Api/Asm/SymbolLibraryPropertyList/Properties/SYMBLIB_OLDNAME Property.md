# SYMBLIB_OLDNAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_OLDNAME().html

---

Name of original symbol library # 15098.

Syntax

**C#**



public PropertyValue SYMBLIB_OLDNAME {get; set;}

public:

property PropertyValue^ SYMBLIB_OLDNAME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is used internally. It contains the name of the original symbol library if the symbol library has been converted. It is possible check whether the symbol library is compatible with an "old" EPLAN 5 symbol library.
