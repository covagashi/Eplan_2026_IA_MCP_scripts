# PageMacro(PageMacro,Page,Project,Boolean,NumerationMode) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert~PageMacro(PageMacro,Page,Project,Boolean,NumerationMode).html

---

Inserts a page macro into a project. You need to set the page, after which the new pages are inserted. You can either overwrite already existing pages having the same name, or the macro pages will be appended after the highest existing number of the location.

Syntax

**C#**



public StorableObject[] PageMacro( 

   PageMacro oMacro,

   Page oInsertAfterPage,

   Project oProject,

   bool overwrite,

   PageMacro.Enums.NumerationMode nNumerationMode

)

public:

array<StorableObject^>^ PageMacro( 

   PageMacro^ oMacro,

   Page^ oInsertAfterPage,

   Project^ oProject,

   bool overwrite,

   PageMacro.Enums.NumerationMode nNumerationMode

)


#### Parameters

*oMacro*
:   PageMacro object to be inserted.

*oInsertAfterPage*
:   Page after which the macro will be inserted. Some structure identifiers will be taken from the Parent Node of this page. If you transfer NULL for oInsertAfterPage, then the structure identifiers will be taken from the macro.

*oProject*
:   Project into which the macro will be inserted.

*overwrite*
:   Pages with the same designation will be overwritten..

*nNumerationMode*
:   numeration mode

#### Return Value

Inserted pages and functions which were not placed (with null .Page property)

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ArgumentNullException** | Null was set to a parameter. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during inserting the macro. Please refer to the error message. |
