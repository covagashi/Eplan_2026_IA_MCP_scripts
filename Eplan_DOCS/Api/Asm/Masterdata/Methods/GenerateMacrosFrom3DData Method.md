# GenerateMacrosFrom3DData Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Masterdata~GenerateMacrosFrom3DData.html

---

Generates 3d macros from step files.

Syntax

**C#**



public bool GenerateMacrosFrom3DData( 

   Project oProject,

   StringCollection oFileNames

)

public:

bool GenerateMacrosFrom3DData( 

   Project^ oProject,

   StringCollection^ oFileNames

)


#### Parameters

*oProject*
:   Project from which data to macro will be taken.

*oFileNames*
:   List of full paths to step files from which macros will be created.

#### Return Value

`True` if generation of all macros is successful, or `false` if something went wrong.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | If any parameter is `null`. |
| [System.ArgumentException](#) | If any parameter is invalid. |
| [System.ApplicationException](#) | Internal interface for master data could not be created. Please check if ProPanel add-on is installed and current license gives rights to use it. |

Remarks

This functionality is available only when ProPanel add-on is installed and current license gives rights to use this add-on.

Macros are generated to `$(MD_MACROS)` directory. Every created file has the same name as step file with extension `.ema`. If in output directory exists file with the same name as generated file then the old file is overwritten.
