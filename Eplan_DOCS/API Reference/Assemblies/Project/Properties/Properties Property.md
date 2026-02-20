# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~Properties.html

---

Enables access to P8 properties of the project.

Syntax

**C#**



public new ProjectPropertyList Properties {get;}

public:

new property ProjectPropertyList^ Properties {

   ProjectPropertyList^ get();

}


#### Property Value

ProjectPropertyList: projects properties

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown during attempt to access transient project's properties. |
