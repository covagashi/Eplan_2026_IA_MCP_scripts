# DeviceTagConfig Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~DeviceTagConfig.html

---

Predefined property for accessing following project settings: EnableSyntaxCheck, UserCharacters, AllowUserCharacters, AllowedLetters, AllowSpecialCharacters, PlantDesignationNumbersOnly.

Syntax

**C#**



public Project.DeviceTagSettings DeviceTagConfig {get;}

public:

property Project.DeviceTagSettings^ DeviceTagConfig {

   Project.DeviceTagSettings^ get();

}


#### Property Value

Object of DeviceTagSettings class.

Exceptions

| Exception | Description |
| --- | --- |
| [InvalidHandleException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidHandleException.html) | Thrown when project is invalid object. |
| [ObjectNotCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectNotCreatedException.html) | Thrown when project is not created. |

Remarks

This property might throw exceptions caused by [DeviceTagConfig](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~DeviceTagConfig.html).

Example

**C#**

```
using Eplan.EplApi.DataModel;

 Project proj; // = ....

  proj.DeviceTagConfig.EnableSyntaxCheck = true;

  proj.DeviceTagConfig.UserCharacters = @"^";

  proj.DeviceTagConfig.AllowUserCharacters = true;

 // now it is possible to use for example:

 Page page; // = ...

  page.Name = @"=^^^^+^^";
```
