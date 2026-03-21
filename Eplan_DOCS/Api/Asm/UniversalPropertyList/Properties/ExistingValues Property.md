# ExistingValues Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html

---

Returns array of PropertyValue objects.

Syntax

**C#**



public PropertyValue[] ExistingValues {get;}

public:

property array<PropertyValue^>^ ExistingValues {

   array<PropertyValue^>^ get();

}


Remarks

Content of returned array depends on a method of obtaining property list. If it was taken from a DataModel object by using [StorableObject.Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Properties.html) member from [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html) then it will contain values from all existing properties (on this object). Note that some of these values can be empty. If the property was taken from an offline property list (i.e. without a parent assigned), then it returns an array of non-empty values stored in this property list.
