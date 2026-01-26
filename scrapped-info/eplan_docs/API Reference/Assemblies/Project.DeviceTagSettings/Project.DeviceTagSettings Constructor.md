# Project.DeviceTagSettings Constructor

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~_ctor.html

---

Constructor for DeviceTagSettings class which allow to access specified settings values for DeviceTag syntax configuration.

Syntax

**C#**



public Project.DeviceTagSettings( 

   Project project

)

public:

Project.DeviceTagSettings( 

   Project^ project

)


#### Parameters

*project*
:   Project for which configuration will be accessed.

Exceptions

| Exception | Description |
| --- | --- |
| [InvalidHandleException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidHandleException.html) | Thrown when project is invalid object. |
| [ObjectNotCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectNotCreatedException.html) | Thrown when project is not created. |

Remarks

This function may throw this same exceptions like [Project.Settings](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~Settings.html) throws;
