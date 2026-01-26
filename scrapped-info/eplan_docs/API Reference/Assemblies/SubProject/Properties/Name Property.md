# Name Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.SubProject~Name.html

---

Displayed scheme name of the associated defined working section for the this subproject.

Syntax

**C#**



public MultiLangString Name {get;}

public:

property MultiLangString^ Name {

   MultiLangString^ get();

}


Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown if project of this subproject becames invalid and it is not possible to continue. |
