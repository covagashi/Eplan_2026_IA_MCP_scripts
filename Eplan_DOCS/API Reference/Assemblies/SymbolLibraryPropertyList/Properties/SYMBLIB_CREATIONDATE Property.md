# SYMBLIB_CREATIONDATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_CREATIONDATE().html

---

Creation date # 15021.

Syntax

**C#**



public PropertyValue SYMBLIB_CREATIONDATE {get; set;}

public:

property PropertyValue^ SYMBLIB_CREATIONDATE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Creation date of the symbol library. The time is output in the local time of the user in accordance with the set time zone.
