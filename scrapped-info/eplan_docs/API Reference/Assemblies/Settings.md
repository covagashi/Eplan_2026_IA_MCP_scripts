# Settings

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings.html

---

Settings are used to save values of variables beyond the runtime of the program and to make them available again the next time program is run (similar to the Windows registry). A setting has a unique identifier in the system. A value or a list of values can be saved to a setting. It is possible to group settings into structures [SchemeSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting.html).

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Base.Settings**

Syntax

**C#**



public class Settings : ISettings

public ref class Settings : public ISettings


Remarks

Due to changes in EPLAN, it may happen that settings will change their type or name or that some settings will be completely removed. We cannot guarantee the long-term compatibility of settings. When updating to a newer version, please check your source code, whether the settings you use are still working.

Example

Access to a setting of the system

**C#**

```
try

{

  String strGuiLanguage= new Settings().GetStringSetting("USER.SYSTEM.GUI.LANGUAGE", 0);

  new Decider().Decide(EnumDecisionType.eOkDecision, "The user interface language is set to: "+ strGuiLanguage, "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

}

catch (BaseException exc)

{

  String strMessage= exc.Message;

  new Decider().Decide(EnumDecisionType.eOkDecision, "Exception: " + strMessage, "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

}
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Settings Constructor](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~_ctor.html) | Default constructor |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddBoolDefault](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~AddBoolDefault.html) | Defines a new setting for a boolean default. |
| Public Method | [AddBoolSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~AddBoolSetting.html) | Defines a new setting for a boolean value. |
| Public Method | [AddDoubleDefault](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~AddDoubleDefault.html) | Defines a new setting for a double default. |
| Public Method | [AddDoubleSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~AddDoubleSetting.html) | Defines a new setting for a double value. |
| Public Method | [AddMultiLangStringDefault](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~AddMultiLangStringDefault.html) | Defines a new default setting for a multilanguage string value. |
| Public Method | [AddMultiLangStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~AddMultiLangStringSetting.html) | Defines a new setting for a multilanguage string value. |
| Public Method | [AddNumericDefault](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~AddNumericDefault.html) | Defines a new setting for a numeric default. |
| Public Method | [AddNumericSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~AddNumericSetting.html) | Defines a new setting for a numeric value. |
| Public Method | [AddStringDefault](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~AddStringDefault.html) | Defines a new setting for a string default. |
| Public Method | [AddStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~AddStringSetting.html) | Defines a new setting for a string value. |
| Public Method | [DeleteSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~DeleteSetting.html) | Resets an individual setting to the value of the corresponding default setting. If it has no default setting, the setting is deleted. |
| Public Method | [Dispose](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~Dispose().html) | Destructor for deterministic finalization of Settings object. |
| Public Method | [ExistSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~ExistSetting.html) | Verifies whether specified setting exists. |
| Public Method | [GetBoolDefault](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetBoolDefault.html) | Returns default boolean value of a setting. The index starts at 0. |
| Public Method | [GetBoolSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetBoolSetting.html) | Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0. |
| Public Method | [GetCountOfDefaultValues](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetCountOfDefaultValues.html) | Returnes the number of default values of a setting. |
| Public Method | [GetCountOfValues](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetCountOfValues.html) | Returnes the number of values of a setting. |
| Public Method | [GetDescription](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetDescription.html) | \Returns the description of a setting. |
| Public Method | [GetDoubleDefault](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetDoubleDefault.html) | Returns default double value of a setting. The index starts at 0. |
| Public Method | [GetDoubleSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetDoubleSetting.html) | Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0. |
| Public Method | [GetExpandedStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetExpandedStringSetting.html) | Returns the value of a string setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0. If this path is identified via an EPLAN path (e.g. $Eplan, $MD, ...) this identifier is resolved. |
| Public Method | [GetMultiLangStringDefault](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetMultiLangStringDefault.html) | Returns default MultiLangString value of a setting. The index starts at 0. |
| Public Method | [GetMultiLangStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetMultiLangStringSetting.html) | Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0. |
| Public Method | [GetNumericDefault](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetNumericDefault.html) | Returns default numeric value of a setting. The index starts at 0. |
| Public Method | [GetNumericSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetNumericSetting.html) | Reads numeric value from settings. It can be 16 bit or 32 bit, signed or unsigned setting. |
| Public Method | [GetStringDefault](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetStringDefault.html) | Returns default string value of a setting. The index starts at 0. |
| Public Method | [GetStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetStringSetting.html) | Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0. |
| Public Method | [GetTypeOfSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetTypeOfSetting.html) | Returns the type of the setting. |
| Public Method | [IsMainNodeReadOnly](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~IsMainNodeReadOnly.html) | Verifies whether the main node (COMPANY / STATION / USER) of the specified setting is Readonly. |
| Public Method | [ReadSettings](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~ReadSettings.html) | Imports a settings xml file and sets all the settings it contains. |
| Public Method | [RemoveAllIndexedSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~RemoveAllIndexedSetting.html) | Removes all indexed setting. |
| Public Method | [SetBoolSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~SetBoolSetting.html) | Overloaded. Sets the value of a setting. The index under which setting will be written is evaluated automatically. First free index is used. The index starts at 0. |
| Public Method | [SetDoubleSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~SetDoubleSetting.html) | Overloaded. Sets the value of a setting. The index under which setting will be written is evaluated automatically. First free index is used. The index starts at 0. |
| Public Method | [SetMultiLangStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~SetMultiLangStringSetting.html) | Overloaded. Sets the value of a setting. The index under which setting will be written is evaluated automatically. First free index is used. The index starts at 0. |
| Public Method | [SetNumericSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~SetNumericSetting.html) | Overloaded. Sets the value of a setting. The index under which setting will be written is evaluated automatically. First free index is used. The index starts at 0. |
| Public Method | [SetStringSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~SetStringSetting.html) | Overloaded. Sets the value of a setting. The index under which setting will be written is evaluated automatically. First free index is used. The index starts at 0. |
| Public Method | [WriteSetting](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~WriteSetting.html) | Exports the specified setting to an XML file. |


