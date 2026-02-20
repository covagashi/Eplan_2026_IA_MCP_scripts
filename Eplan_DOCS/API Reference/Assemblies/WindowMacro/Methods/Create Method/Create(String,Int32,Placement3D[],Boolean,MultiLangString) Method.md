# Create(String,Int32,Placement3D[],Boolean,MultiLangString) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic742.html

---

Writes a window macro file from the pPlacements If at least one given Placement object is valid, created macro is opened.

Syntax

**C#**



public void Create( 

   string macroFileName,

   WindowMacro.Enums.RepresentationType nRepresentationType,

   int nVariant,

   Placement[] pPlacements,

   MultiLangString strDescription,

   PointD oReferencePoint

)

public:

void Create( 

   String^ macroFileName,

   WindowMacro.Enums.RepresentationType nRepresentationType,

   int nVariant,

   array<Placement^>^ pPlacements,

   MultiLangString^ strDescription,

   PointD oReferencePoint

)


#### Parameters

*macroFileName*
:   The name (including path) for the macro file. Parameter value must include a valid extension (otherwise an exception is thrown).

*nRepresentationType*


*nVariant*
:   The variant written (A file can contain more than one variants)

*pPlacements*
:   The placements the macro should contain. They should be from the same page.

*strDescription*
:   The description for this macro file or null when no description should be set.

*oReferencePoint*
:   The reference point of the macro

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when parameters are not valid |
