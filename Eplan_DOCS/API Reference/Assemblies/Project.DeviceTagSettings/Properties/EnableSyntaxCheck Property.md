# EnableSyntaxCheck Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~EnableSyntaxCheck.html

---

Representation of XDtcDeviceTagCheck.Hierarchy.ActivateDeviceTagCheck settings value. In P8-GUI it can be found in the "File" -> "Settings..." Projects/<project>/Devices/DT syntax check:Structure identifier/Enable check. If value of this property is `false` then all others properties of this class will not be used - syntax checking for DeviceTags names is disabled.

Syntax

**C#**



public bool EnableSyntaxCheck {get; set;}

public:

property bool EnableSyntaxCheck {

   bool get();

   void set (    bool value);

}


Remarks

This property might throw this same exceptions what functions **Eplan::EplApi::DataModel::ProjectSettings:** and **Eplan::EplApi::DataModel::ProjectSettings:** might throw.
