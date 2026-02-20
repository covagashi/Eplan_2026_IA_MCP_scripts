# Create(String,RepresentationType,Int32,Placement[],MultiLangString) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic744.html

---

Writes a window macro file from the pPlacements If at least one given Placement object is valid, created macro is opened.

Syntax

**C#**



public void Create( 

   string macroFileName,

   int nVariant,

   Placement[] pPlacements,

   MultiLangString strDescription

)

public:

void Create( 

   String^ macroFileName,

   int nVariant,

   array<Placement^>^ pPlacements,

   MultiLangString^ strDescription

)


#### Parameters

*macroFileName*
:   The name (including path) for the macro file. Parameter value must include a valid extension (otherwise an exception is thrown).

*nVariant*
:   The variant written (A file can contain more than one variants)

*pPlacements*
:   The placements the macro should contain. They should be from the same page.

*strDescription*
:   The description for this macro file or null when no description should be set.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when parameters are not valid |
