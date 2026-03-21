# CreateScheme Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~CreateScheme.html

---

Create a new scheme with a specified name, description and the node name for the settings. The data for the new scheme is specified by P8 for each scheme type. The data is the same as the new button in the scheme dialog of P8.

Syntax

**C#**



public void CreateScheme( 

   string strSettingsNodeName,

   MultiLangString mlNewName,

   MultiLangString mlDescription

)

public:

void CreateScheme( 

   String^ strSettingsNodeName,

   MultiLangString^ mlNewName,

   MultiLangString^ mlDescription

)


#### Parameters

*strSettingsNodeName*
:   The node name in the settings

*mlNewName*
:   The new name of the scheme

*mlDescription*
:   The description of the scheme

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when a parameter is `null`. |
| [System.ArgumentException](#) | Thrown when a parameter is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when strName is not a valid last used scheme. The scheme with this strSettingsNodeName already exists |
