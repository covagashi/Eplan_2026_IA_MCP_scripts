# SettingNode

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode.html

---

Allows access to settings and relative access to setting-nodes. A setting key consists of a number of sections separated by '.' Each section except the last one is called a setting-node. Setting-nodes and settings together build the settings tree. The settings are the leaves of this tree. The SettingNode class helps iterating trough the nodes and e.g. gives you the possibility to delete a node completely.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Base.SettingNode**  
      [Eplan.EplApi.DataModel.ProjectSettingNode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettingNode.html)

Syntax

**C#**



public class SettingNode

public ref class SettingNode


Remarks

Due to changes in EPLAN, it may happen that settings will change their type or name or that some settings will be completely removed. We cannot guarantee the long-term compatibility of settings. When updating to a newer version, please check your source code, whether the settings you use are still working.

Example

Example of using relative path to access entries

**C#**

```
// Create setting node with path STATION.AF.Service.Actions.ActionNewModell

SettingNode oSettingNode = new SettingNode("STATION.AF.Services.Actions.ActionNewModell");

// Set or get setting relative to the path of the node

oSettingNode.SetStringSetting("ModuleName.10", "Service3DLog", 0);

string str = oSettingNode.GetStringSetting("ModuleName.10", 0);

```

Example of merging 2 nodes

**C#**

```
SettingNode oTestNode1 = new SettingNode("STATION.AF.Services.Actions.ActionNewModell");

Console.WriteLine(oTestNode1.GetCountOfNodes().ToString()); //  1

SettingNode oTestNode2 = new SettingNode("STATION.AF.Services.Actions.AdjustFromAllLineToSingleLineAndOverview");

Console.WriteLine(oTestNode2.GetCountOfNodes().ToString()); //  1

oTestNode1.MergeWithNode(oTestNode2);

Console.WriteLine(oTestNode1.GetCountOfNodes().ToString()); //  2

```

Example of listing sub-nodes

**C#**

```
SettingNode oSettingNode = new SettingNode("STATION.AF.Modules");

StringCollection oSubnodes = new StringCollection();

oSettingNode.GetListOfNodes(ref oSubnodes, false);

foreach (string sSubNode in oSubnodes)

{

    SettingNode oSubNode = oSettingNode.GetSubNode(sSubNode);

    Console.WriteLine(oSubNode.GetNodePath());

}

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [SettingNode Constructor](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~_ctor.html) | Overloaded. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddBoolDefault](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~AddBoolDefault.html) | Defines a new setting for a boolean default. |
| Public Method | [AddBoolSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~AddBoolSetting.html) | Defines a new setting for a boolean value. |
| Public Method | [AddDoubleDefault](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~AddDoubleDefault.html) | Defines a new setting for a double default. |
| Public Method | [AddDoubleSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~AddDoubleSetting.html) | Defines a new setting for a double value. |
| Public Method | [AddMultiLangStringDefault](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~AddMultiLangStringDefault.html) | Defines a new setting for a multilanguage string default. |
| Public Method | [AddMultiLangStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~AddMultiLangStringSetting.html) | Defines a new setting for a multilanguage string value. |
| Public Method | [AddNumericDefault](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~AddNumericDefault.html) | Defines a new setting for a numeric default. |
| Public Method | [AddNumericSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~AddNumericSetting.html) | Defines a new setting for a numeric value. |
| Public Method | [AddStringDefault](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~AddStringDefault.html) | Defines a new setting for a string default. |
| Public Method | [AddStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~AddStringSetting.html) | Defines a new setting for a string value. |
| Public Method | [ClearSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~ClearSetting.html) | Overloaded. Deletes the value. The setting definition is maintained. |
| Public Method | [DeleteSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~DeleteSetting.html) | Resets an individual setting to the value of the corresponding default setting. If it has no default setting, the setting is deleted. |
| Public Method | [Dispose](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~Dispose().html) | Destructor for deterministic finalization of SettingNode object. |
| Public Method | [ExistSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~ExistSetting.html) | Verifies whether specified setting exists. |
| Public Method | [ForceReload](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~ForceReload.html) | Reloads settings node. |
| Public Method | [GetBoolSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~GetBoolSetting.html) | Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0. |
| Public Method | [GetCountOfNodes](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~GetCountOfNodes.html) | Determines the number of child nodes. |
| Public Method | [GetCountOfSettings](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~GetCountOfSettings.html) | Determines the number of child settings (subordinate settings). |
| Public Method | [GetDoubleSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~GetDoubleSetting.html) | Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0. |
| Public Method | [GetListOfAllSettings](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~GetListOfAllSettings.html) | Determines all settings. |
| Public Method | [GetListOfNodes](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~GetListOfNodes.html) | Determines all settings nodes. |
| Public Method | [GetListOfSettings](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~GetListOfSettings.html) | Determines all settings of this node. |
| Public Method | [GetMultiLangStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~GetMultiLangStringSetting.html) | Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0. |
| Public Method | [GetNodePath](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~GetNodePath.html) | Determines the path of this node. |
| Public Method | [GetNodePathDot](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~GetNodePathDot.html) | Determines the path of this node. |
| Public Method | [GetNumericSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~GetNumericSetting.html) | Reads numeric value from settings. It can be 16 bit or 32 bit, signed or unsigned setting. |
| Public Method | [GetParentNode](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~GetParentNode.html) | Determines the parent node. |
| Public Method | [GetStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~GetStringSetting.html) | Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0. |
| Public Method | [GetSubNode](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~GetSubNode.html) | Determines a child node. |
| Public Method | [MergeWithNode](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~MergeWithNode.html) | Merges settings nodes. |
| Public Method | [ResetNode](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~ResetNode.html) | Resets the node to default. All settings inside are deleted and copied from defaults again. |
| Public Method | [Set](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~Set.html) | Defines the path to the settings node. |
| Public Method | [SetBoolSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~SetBoolSetting.html) | Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0. |
| Public Method | [SetDoubleSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~SetDoubleSetting.html) | Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0. |
| Public Method | [SetMultiLangStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~SetMultiLangStringSetting.html) | Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0. |
| Public Method | [SetNumericSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~SetNumericSetting.html) | Sets the value of project settings on a given path. Type of value will be converted to 16 bit, 32 bit, signed or unsigned value depending on setting type. |
| Public Method | [SetStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~SetStringSetting.html) | Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0. |
| Public Method | [Write](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~Write.html) | Writes all settings to a file. |


