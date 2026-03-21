# CorrectDeviceTagProperties Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~CorrectDeviceTagProperties.html

---

Do a correction on the namelist, if properties for main and nested devicetags are incorrect. In detail the nested devicetags are moved to the main devicetags if these have been empty.

Syntax

**C#**



public bool CorrectDeviceTagProperties( 

   UniversalPropertyList nameParts

)

public:

bool CorrectDeviceTagProperties( 

   UniversalPropertyList^ nameParts

)


#### Parameters

*nameParts*
:   PropertyList for correction.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
