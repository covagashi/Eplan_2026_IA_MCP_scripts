# ImportSchemes Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~ImportSchemes.html

---

Import all schemes from file.

Syntax

**C#**



public void ImportSchemes( 

   string strFileName,

   bool bOverwriteExisting

)

public:

void ImportSchemes( 

   String^ strFileName,

   bool bOverwriteExisting

)


#### Parameters

*strFileName*
:   The file to import from to. Must include the complete path

*bOverwriteExisting*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when a parameter is `null`. |
| [System.ArgumentException](#) | Thrown when a parameter is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when strName is not a valid last used scheme. |
