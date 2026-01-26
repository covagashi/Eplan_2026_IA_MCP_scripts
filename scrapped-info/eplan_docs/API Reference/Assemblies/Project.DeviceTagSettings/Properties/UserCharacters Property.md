# UserCharacters Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~UserCharacters.html

---

Representation of XDtcDeviceTagCheck.Hierarchy.UserCharacters setting value. In P8-GUI it can be found in the "File" -> "Settings..." Projects/<project>/Devices/DT syntax check:Structure identifier/Special text characters. It provides possibility to enhance allowed characters used in DeviceTag syntax. To use this property [AllowUserCharacters](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~AllowUserCharacters.html) must be `true` like also [EnableSyntaxCheck](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~EnableSyntaxCheck.html) must be `true`

Syntax

**C#**



public string UserCharacters {get; set;}

public:

property String^ UserCharacters {

   String^ get();

   void set (    String^ value);

}


Remarks

This property might throw this same exceptions what functions **Eplan::EplApi::DataModel::ProjectSettings:** and **Eplan::EplApi::DataModel::ProjectSettings:** might throw.
