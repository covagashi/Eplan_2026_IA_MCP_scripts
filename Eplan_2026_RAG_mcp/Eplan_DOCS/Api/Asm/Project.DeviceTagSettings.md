# Project.DeviceTagSettings

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings.html

---

DeviceTagSettings class allows to access specified settings values for DeviceTag (names of devices, pages etc) syntax configuration. Object of this class is created by [Project.DeviceTagConfig](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~DeviceTagConfig.html) property. Please see property members of this class for details.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.Project.DeviceTagSettings**

Syntax

**C#**



public class Project.DeviceTagSettings

public ref class Project.DeviceTagSettings

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Project.DeviceTagSettings Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~_ctor.html) | Constructor for DeviceTagSettings class which allow to access specified settings values for DeviceTag syntax configuration. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AllowedLetters](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~AllowedLetters.html) | Representation of XDtcDeviceTagCheck.Hierarchy.AllowedLetters setting value. In P8-GUI it can be found in the "File" -> "Settings..." Projects/<project>/Devices/DT syntax check:Structure identifier/All upper-case letters and numbers. It provides possibility to use letters in DeviceTag. To make it work [EnableSyntaxCheck](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~EnableSyntaxCheck.html) must be `true`. |
| Public Property | [AllowSpecialCharacters](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~AllowSpecialCharacters.html) | Representation of XDtcDeviceTagCheck.Hierarchy.AllowSpecialCharacters setting value. In P8-GUI it can be found in "File" -> "Settings..." Projects/<project>/Devices/DT syntax check:Structure identifier/Valid special characters. It provides possibility to use special characters in DeviceTag. Special characters are: `\_' `?' `\*' `,' . It might be changed by dynamic configuration. To make it work [EnableSyntaxCheck](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~EnableSyntaxCheck.html) must be `true`. |
| Public Property | [AllowUserCharacters](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~AllowUserCharacters.html) | Representation of XDtcDeviceTagCheck.Hierarchy.AllowUserCharacters setting value. In P8-GUI it can be found in the "File" -> "Settings..." Projects/<project>/Devices/DT syntax check:Structure identifier/Special text characters. When this option is enabled, all characters in [UserCharacters](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~UserCharacters.html) string are possible to be used in DeviceTags. To make it work [EnableSyntaxCheck](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~EnableSyntaxCheck.html) must be `true`. |
| Public Property | [EnableSyntaxCheck](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~EnableSyntaxCheck.html) | Representation of XDtcDeviceTagCheck.Hierarchy.ActivateDeviceTagCheck settings value. In P8-GUI it can be found in the "File" -> "Settings..." Projects/<project>/Devices/DT syntax check:Structure identifier/Enable check. If value of this property is `false` then all others properties of this class will not be used - syntax checking for DeviceTags names is disabled. |
| Public Property | [PlantDesignationNumbersOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~PlantDesignationNumbersOnly.html) | Representation of XDtcDeviceTagCheck.Hierarchy.PlantDesignationNumbersOnly setting value. In P8-GUI it can be found in the "File" -> "Settings..." Projects/<project>/Devices/DT syntax check:Structure identifier/Valid special characters. When this option is enabled (has `true` value) only numbers can be used in DeviceTag syntax. To make it work [EnableSyntaxCheck](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~EnableSyntaxCheck.html) must be `true`. |
| Public Property | [UserCharacters](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~UserCharacters.html) | Representation of XDtcDeviceTagCheck.Hierarchy.UserCharacters setting value. In P8-GUI it can be found in the "File" -> "Settings..." Projects/<project>/Devices/DT syntax check:Structure identifier/Special text characters. It provides possibility to enhance allowed characters used in DeviceTag syntax. To use this property [AllowUserCharacters](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~AllowUserCharacters.html) must be `true` like also [EnableSyntaxCheck](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~EnableSyntaxCheck.html) must be `true` |


