# ExistingIds Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObjectPropertyList~ExistingIds.html

---

Returns array of MDPropertyValue objects. If PropertiesAndHandleObjectPropertyList works on local property list it will be an array of unique properties from local property list. Otherwise it will be an array of all existing properties for related object.

Syntax

**C#**



public MDAnyPropertyId[] ExistingIds {get;}

public:

property array<MDAnyPropertyId^>^ ExistingIds {

   array<MDAnyPropertyId^>^ get();

}

