# ImportDevicesText(Project,String,String,String,Int32,Int32,FunctionDefinition,FunctionDefinition,ImportMode) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1333.html

---

Creates a display list for a macro. A display list is a set of graphical placements to be drawn. Removes the representation of previously displayed objects when creating a new list.

Syntax

**C#**



public void CreateDisplayList( 

   string strMacroFile,

   string strConverter,

   WindowMacro.Enums.RepresentationType nRepType,

   int nVariant,

   Project pProject

)

public:

void CreateDisplayList( 

   String^ strMacroFile,

   String^ strConverter,

   WindowMacro.Enums.RepresentationType nRepType,

   int nVariant,

   Project^ pProject

)


#### Parameters

*strMacroFile*
:   Full file name of a window macro.

*strConverter*
:   Name of a file converter. Parameter may be empty. A file converter can be used to convert a file into a temporary macro file. After converting, the content of the temp. macro file will be used to create a display list. This is reserved for future enhancements. Today, it is not possible to write an own converter by API.

*nRepType*
:   Representation Type of Macro.

*nVariant*
:   Index of the macro variant.

*pProject*
:   Project which provides display properties.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ArgumentNullException** | A null reference is passed to a parameter. |
| **BaseException** | An error occurred, when creating the display list. |
