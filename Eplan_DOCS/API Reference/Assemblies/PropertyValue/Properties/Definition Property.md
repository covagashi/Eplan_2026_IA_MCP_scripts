# Definition Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Definition.html

---

Returns an object that provides information about the property and its definition. The information includes: name of the property, its data type, whether it's indexed or not, whether it's read-only, upper/lower bounds of values for numerical properties. To use the Definition property, the PropertyValue object must point to a project property (persistent property).It cannot point to an individual value (transient property).

Syntax

**C#**



public PropertyDefinition Definition {get;}

public:

property PropertyDefinition^ Definition {

   PropertyDefinition^ get();

}

