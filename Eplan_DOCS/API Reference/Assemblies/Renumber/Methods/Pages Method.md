# Pages Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Renumber~Pages.html

---

Method for renumbering pages specified by the collection pages;

Syntax

**C#**



public void Pages( 

   Page[] pages,

   bool bStructureOriented,

   int nStartvalue,

   int nIncrement,

   bool bKeepInterval,

   bool bKeepText,

   Renumber.Enums.SubPages eSubPages

)

public:

void Pages( 

   array<Page^>^ pages,

   bool bStructureOriented,

   int nStartvalue,

   int nIncrement,

   bool bKeepInterval,

   bool bKeepText,

   Renumber.Enums.SubPages eSubPages

)


#### Parameters

*pages*
:   Pages to be renumbered.

*bStructureOriented*
:   Set this parameter to true to provide numbering per structure identifier. If false, then pages are continuously number without

*nStartvalue*
:   Here you enter the page number from which the numbering is to begin.

*nIncrement*
:   Here you enter the increment value for the separation between the page numbers.

*bKeepInterval*
:   In combination with the definition of the start page, this parameter retains the increments between the selected pages for the target pages. In this way you can move any desired number of selected pages by a specified increment. Entering the increment size is not possible in this case.

*bKeepText*
:   Set this to true, if the alphabetic part of the page name should not be overwritten.

*eSubPages*
:   Values are:

    - Retain: Existing subpages are adopted unchanged into the target page.

    - ConsecutiveNumbering:Existing subpages are renumbered using the starting value "1" and an increment of "1". At every change of the main page, the subpage numbering begins again from "1". The subpage numbering follows the project settings defined in the project setting "Characters for subpages".

    - ConvertIntoMainPages: Subpages are converted to main pages and renumbered.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown, if an argument is set to null. |
| **ApplicationException** | An error occurred during numbering. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during numbering. |
| [System.ArgumentException](#) | Thrown when the objects in the parameter belong to more than one project. |

Remarks

The objects in the parameter may only belong to one project otherwise a "System::ArgumentException" is thrown.
