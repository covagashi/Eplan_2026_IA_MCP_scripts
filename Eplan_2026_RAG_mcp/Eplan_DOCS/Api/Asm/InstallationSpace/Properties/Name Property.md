# Name Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.InstallationSpace~Name.html

---

Returns the name of the Function3D.

Syntax

**C#**



public override string Name {get; set;}

public:

property String^ Name {

   String^ get() override;

   void set (    String^ value) override;

}


#### Property Value

name of the function

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the name cannot be retrieved from the function |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Function3D is transient. |
| [System.ArgumentNullException](#) | Thrown while setting if new value is `null`. |
