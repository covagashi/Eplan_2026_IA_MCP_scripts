# FileName Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Image~FileName.html

---

Full file name of the image file.

Syntax

**C#**



public string FileName {get; set;}

public:

property String^ FileName {

   String^ get();

   void set (    String^ value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strName` is `null`. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when file name cannot be set. |

Remarks

The file name may contain PathMap variables. When setting the property, PathMap variables will automatically be assigned if a respective assignment is possible.
