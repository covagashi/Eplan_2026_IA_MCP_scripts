# GetUncompletedPages Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision~GetUncompletedPages.html

---

Returns an array of modified and not completed pages in the current revision of a project. Used for change tracking.

Syntax

**C#**



public Page[] GetUncompletedPages( 

   Project oProject

)

public:

array<Page^>^ GetUncompletedPages( 

   Project^ oProject

)


#### Parameters

*oProject*
:   A project to get the pages from.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ApplicationException** | Internal interface necessary for the revision management could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the action. |

Remarks

Used for change tracking. In case of a project on which no "Complete project" operation was called (from API or GUI), an empty array will be returned. Pages in the mode "Complete always" are always included here. When a revision for a project section is active, only the pages of this project section are returned.
