# SYMBLIB_LASTMODIFICATIONDATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_LASTMODIFICATIONDATE().html

---

Modification date (automatic) # 15023.

Syntax

**C#**



public PropertyValue SYMBLIB_LASTMODIFICATIONDATE {get; set;}

public:

property PropertyValue^ SYMBLIB_LASTMODIFICATIONDATE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Date of last change to the symbol library. The time is output in the local time of the user in accordance with the set time zone.
