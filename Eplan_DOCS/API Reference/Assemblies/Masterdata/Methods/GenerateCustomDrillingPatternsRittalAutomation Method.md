# GenerateCustomDrillingPatternsRittalAutomation Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Masterdata~GenerateCustomDrillingPatternsRittalAutomation.html

---

Generating Drilling Patterns from NC files.

Syntax

**C#**



public int GenerateCustomDrillingPatternsRittalAutomation( 

   Project oProject,

   StringCollection oFileNames,

   string strOutputDirectory,

   ref int nCountoursImported

)

public:

int GenerateCustomDrillingPatternsRittalAutomation( 

   Project^ oProject,

   StringCollection^ oFileNames,

   String^ strOutputDirectory,

   int% nCountoursImported

)


#### Parameters

*oProject*
:   Project from which data to macro will be taken. Can't be `null`.

*oFileNames*
:   List of full paths to Rittal Automation NC files used to import data. Only files with extensions: `*.PBT`, `*.PVB` and `*.PKU` are used. Can't be `null`.

*strOutputDirectory*
:   Output directory for user defined contours. If `null` or `empty` by default `$MD_MACROS` is used. If directory is passed then it must exists.

*nCountoursImported*
:   (Ref) Number of generated user defined contours files.

#### Return Value

Number of drilling patters added to system database.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | If any needed parameter is `null` or `empty`. |
| [System.ArgumentException](#) | If any parameter is invalid. |
| [System.ApplicationException](#) | Internal interface for master data could not be created. Please check if ProPanel add-on is installed and current license gives rights to use it. |

Remarks

The import of drilling information from Rittal Automation NC files encompasses the files with file extensions: `*.PBT`, `*.PVB` and `*.PKU`.

With this method only drilling patterns for individual items can be generated, not however complete mounting panels from RittalAutomation item files (\*.PBT or \*.PVB).

A user-defined outline is created from a Rittal Automation outline file (\*.PKU). A "NC Rittal Automation" record is already assigned to this outline. After the import you create a drilling pattern with drill type "User-defined outline" that uses the outline created by the import of the PKU file in the parts management.

This method uses a scheme called `Standard` when exporting the Rittal Automation NC data.
