# Name Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~Name.html

---

Get or set name of the page. When setting this property, it is not checked whether the given name already exists in project.

Syntax

**C#**



public string Name {get; set;}

public:

property String^ Name {

   String^ get();

   void set (    String^ value);

}


#### Property Value

Page's name.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when name of the page cannot be read from data model. |
| [System.ArgumentNullException](#) | Thrown when `newName` is `null`. |

Remarks

Equal to PAGE\_FULLNAME property. To know DeviceTag syntax please see chapter 'Dialog Settings: DT syntax check' in Eplan documentation.
