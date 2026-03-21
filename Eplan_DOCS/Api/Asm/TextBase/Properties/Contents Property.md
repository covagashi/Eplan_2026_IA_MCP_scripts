# Contents Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.TextBase~Contents.html

---

Contents of object represented by this type.

Syntax

**C#**



public virtual MultiLangString Contents {get; set;}

public:

virtual property MultiLangString^ Contents {

   MultiLangString^ get();

   void set (    MultiLangString^ value);

}


#### Property Value

[Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html) stored in the TextBase.

Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown when setting a value and this object is of type [PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html). |

Remarks

It is invalid to set content of [PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html) and because of it an exception is thrown when setting the value for object of that type.
