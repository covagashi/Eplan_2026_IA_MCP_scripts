# PageMacro(PageMacro,Project,Boolean[],NumerationMode) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert~PageMacro(PageMacro,Project,Boolean[],NumerationMode).html

---

Inserts a page macro into project. User can specify which pages can be overwritten over existing pages in project.

Syntax

**C#**



public StorableObject[] PageMacro( 

   PageMacro oMacro,

   Project oProject,

   bool[] arrOverwritePages,

   PageMacro.Enums.NumerationMode nNumerationMode

)

public:

array<StorableObject^>^ PageMacro( 

   PageMacro^ oMacro,

   Project^ oProject,

   array<bool>^ arrOverwritePages,

   PageMacro.Enums.NumerationMode nNumerationMode

)


#### Parameters

*oMacro*
:   Page macro with will be inserted into project. Can not be null.

*oProject*
:   Project into with page macro will be inserted. Can not be null.

*arrOverwritePages*
:   Defines whether an existing page is to be overwritten when a page macro is being inserted. Order of elements corresponds with order of elements in [Eplan.EplApi.DataModel.MasterData.PageMacro.Pages](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PageMacro~Pages.html). If null is passed all pages will not be overwritten.

*nNumerationMode*
:   Numeration mode.

#### Return Value

Inserted pages and functions which were not placed (with null .Page property)

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Null was set to a parameter. |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ApplicationException** | The internal interface can not be append. Operation failed. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during inserting the macro. Please refer to the error message. |

Remarks

User can determine a name for each page under which it will be inserted. This is done by setting new name to page from [Eplan.EplApi.DataModel.MasterData.PageMacro.Pages](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PageMacro~Pages.html). See example.
