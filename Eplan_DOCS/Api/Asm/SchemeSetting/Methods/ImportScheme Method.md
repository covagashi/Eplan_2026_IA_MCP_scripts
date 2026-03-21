# ImportScheme Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~ImportScheme.html

---

Import a scheme from file.

Syntax

**C#**



public void ImportScheme( 

   string strSettingsNodeName,

   string strFileName,

   bool bOverwriteExisting

)

public:

void ImportScheme( 

   String^ strSettingsNodeName,

   String^ strFileName,

   bool bOverwriteExisting

)


#### Parameters

*strSettingsNodeName*
:   The node name in the settings (of the file)

*strFileName*
:   The file to import from. Must include the complete path. Inside the node with the name strSettingsNodeName has to exist

*bOverwriteExisting*
:   Overwrite any existing scheme with the same name

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when a parameter is `null`. |
| [System.ArgumentException](#) | Thrown when a parameter is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The file passed to strFileName does not contain scheme with name from strSettingsNodeName parameter. Or scheme already exists but bOverwriteExisting is set to false. |
