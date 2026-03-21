# ReadSettings Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~ReadSettings.html

---

Reads settings from settings file.

Syntax

**C#**



public void ReadSettings( 

   string strFilename

)

public:

void ReadSettings( 

   String^ strFilename

)


#### Parameters

*strFilename*
:   Settings file name

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strFilename` is `null`. |
| [System.ArgumentException](#) | Thrown when `strFilename` is empty. |
| [System.ArgumentException](#) | Thrown when file `strFilename` does not exist. |
