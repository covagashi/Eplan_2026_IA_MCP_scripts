# ProjectEntries(String) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Masterdata~ProjectEntries(String).html

---

Returns the file names of all master data stored in the project.

Syntax

**C#**



public StringCollection ProjectEntries( 

   string strFullLinkFileName

) {get;}

public:

property StringCollection^ ProjectEntries {

   StringCollection^ get(String^ strFullLinkFileName);

}


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project, of which the information will be read.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | A parameter was set to a null reference. |
| **ArgumentException** | \Parameters are invalid, e.g. the project does not exist. |
| **ApplicationException** | \Internal interface for master data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Project master data could not be correctly determined.. |

Remarks

The project "strFullLinkFileName" may be open in EPLAN or not. If the project was not already open, it will be opened and after the export it will be closed again.
