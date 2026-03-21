# Name Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~Name.html

---

Gets the pin's actual designation. This value is equal to FUNC\_CONNECTIONDESIGNATION property of the parent function, at the corresponding index.

Syntax

**C#**



public string Name {get;}

public:

property String^ Name {

   String^ get();

}


Remarks

Returns `NULL` if this Pin object has been obtained from a FunctionDefinition object.
