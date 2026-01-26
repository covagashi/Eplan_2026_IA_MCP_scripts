# Methods

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting_methods.html

---

For a list of all members of this type, see [SchemeSetting members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting_members.html).

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CheckIfSchemeExists](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~CheckIfSchemeExists.html) | Checks whether a scheme is defined. |
| Public Method | [CopyScheme](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~CopyScheme.html) | Copy an existing scheme. |
| Public Method | [CountSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~CountSetting.html) | Number of additional settings existing under the specified setting name. |
| Public Method | [CreateScheme](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~CreateScheme.html) | Create a new scheme with a specified name, description and the node name for the settings. The data for the new scheme is specified by P8 for each scheme type. The data is the same as the new button in the scheme dialog of P8. |
| Public Method | [Dispose](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~Dispose().html) | For internal use only. Needed if the scheme exists in a project's settings Destructor for deterministic finalization of SchemeSetting object. |
| Public Method | [ExportScheme](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~ExportScheme.html) | Export a scheme to file. |
| Public Method | [ExportSchemes](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~ExportSchemes.html) | Export all schemes to file. |
| Public Method | [GetBoolSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetBoolSetting.html) | Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0. |
| Public Method | [GetCount](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetCount.html) | Returns the number of various schemes in this scheme. |
| Public Method | [GetDoubleSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetDoubleSetting.html) | Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0. |
| Public Method | [GetLastUsed](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetLastUsed.html) | Returns the last used scheme name (node LastUsed). |
| Public Method | [GetLocalizedNameSettingPath](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetLocalizedNameSettingPath.html) | Returns Setting path to the localized name of this scheme. |
| Public Method | [GetMultiLangStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetMultiLangStringSetting.html) | Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0. |
| Public Method | [GetName](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetName.html) | Returns a language-independent, internal scheme identifier. |
| Public Method | [GetNodeHandle](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetNodeHandle.html) | Returns the [SettingNode](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode.html) of the data node of the current setting. The individual settings can now be accessed via the functions of the [SettingNode](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode.html). |
| Public Method | [GetNumericSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetNumericSetting.html) | Reads numeric value from settings. It can be 16 bit or 32 bit, signed or unsigned setting. |
| Public Method | [GetStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetStringSetting.html) | Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0. |
| Public Method | [ImportScheme](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~ImportScheme.html) | Import a scheme from file. |
| Public Method | [ImportSchemes](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~ImportSchemes.html) | Import all schemes from file. |
| Public Method | [Init](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~Init.html) | Initializes object with a settings node path. |
| Public Method | [RemoveScheme](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~RemoveScheme.html) | Remove a new scheme. |
| Public Method | [ResetScheme](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~ResetScheme.html) | Sets LastUsed as the current scheme. |
| Public Method | [Set](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~Set.html) | Setup internal members |
| Public Method | [SetBoolSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~SetBoolSetting.html) | Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0. |
| Public Method | [SetDoubleSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~SetDoubleSetting.html) | Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0. |
| Public Method | [SetLastUsed](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~SetLastUsed.html) | Sets the strName scheme as the current one. Value in node LastUsed will be strName |
| Public Method | [SetMultiLangStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~SetMultiLangStringSetting.html) | Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0. |
| Public Method | [SetNumericSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~SetNumericSetting.html) | Sets the value of settings on a given path. Type of value will be converted to 16 bit, 32 bit, signed or unsigned value depending on setting type. |
| Public Method | [SetScheme](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~SetScheme.html) | Overloaded. Sets a scheme by its name (LastUsed remains unchanged!) |
| Public Method | [SetStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~SetStringSetting.html) | Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0. |


