# Name Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Plane~Name.html

---

Returns the name of the IFunctionBase.

Syntax

**C#**



public virtual string Name {get; set;}

public:

virtual property String^ Name {

   String^ get();

   void set (    String^ value);

}


#### Property Value

name of the function

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the name cannot be retrieved from the function |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | IFunctionBase is transient. |
| [System.ArgumentNullException](#) | Thrown while setting if new value is `null`. |
