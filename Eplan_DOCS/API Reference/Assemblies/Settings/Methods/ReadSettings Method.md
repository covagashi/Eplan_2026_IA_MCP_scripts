# ReadSettings Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~ReadSettings.html

---

Imports a settings xml file and sets all the settings it contains.

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
:   Indicates the name of the settings \file.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strFilename` is `null`. |
| [System.ArgumentException](#) | Thrown when `strFilename` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Method failed. |

Remarks

In contrary to GUI all the settings from the XML file are imported, not only those, which are visible in the settings dialog. Settings imported by this method may not take effect immediately.
