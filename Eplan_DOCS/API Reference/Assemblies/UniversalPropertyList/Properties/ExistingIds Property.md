# ExistingIds Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html

---

Returns array of property ids. Returns array of AnyPropertyId objects.

Syntax

**C#**



public AnyPropertyId[] ExistingIds {get;}

public:

property array<AnyPropertyId^>^ ExistingIds {

   array<AnyPropertyId^>^ get();

}


Remarks

Content of returned array depends on a method of obtaining property list. If it was taken from a DataModel object by using [StorableObject.Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Properties.html) member from [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html) then it will contain ids from all existing properties (on this object). If the property was taken from an offline property list (i.e. without a parent assigned), then it returns an array of ids which have corresponding non-empty values stored in this property list.
