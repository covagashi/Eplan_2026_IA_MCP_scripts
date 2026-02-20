# VisibleName Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Plane~VisibleName.html

---

Returns the visible name of the IFunctionBase.

Syntax

**C#**



public virtual string VisibleName {get; set;}

public:

virtual property String^ VisibleName {

   String^ get();

   void set (    String^ value);

}


#### Property Value

name of the function

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the visible name cannot be retrieved from the function. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | IFunctionBase is transient. |
| [System.ArgumentNullException](#) | Thrown while setting when the new value is `null`. |
