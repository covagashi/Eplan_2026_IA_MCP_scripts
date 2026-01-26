# CreateTerminalDevice(Project,String,String,String,String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1330.html

---

Creates new terminals for a new or existing DT according to a particular numbering pattern. The terminals are generated from the function templates of the selected part, with the numbering pattern defining the terminal designations. The first terminal generated becomes the main terminal per device and receives the selected part.

Syntax

**C#**



public bool CreateTerminalDevice( 

   Project oProject,

   string strFullDeviceTag,

   string strPartNumber,

   string strPartVariant,

   string strNumberingPattern,

   int nNewTerminalDevicePosition,

   int nNewTerminalSortCode,

   bool bNumberByLevels

)

public:

bool CreateTerminalDevice( 

   Project^ oProject,

   String^ strFullDeviceTag,

   String^ strPartNumber,

   String^ strPartVariant,

   String^ strNumberingPattern,

   int nNewTerminalDevicePosition,

   int nNewTerminalSortCode,

   bool bNumberByLevels

)


#### Parameters

*oProject*
:   The project in which the new terminals will be.

*strFullDeviceTag*
:   This parameter determines the DT of the new terminals.

*strPartNumber*
:   The article's part number.

*strPartVariant*
:   The article's variant.

*strNumberingPattern*
:   Numbering pattern.

*nNewTerminalDevicePosition*
:   The device position of the new terminals. The device position specifies the position of the terminal device within the terminal strip to which the terminal belongs. All the terminals of a terminal device have the same device position.

*nNewTerminalSortCode*
:   The terminal sort code of the new terminals. The sort code also specifies the order of the terminals within a terminal device. This means that the sort code is only relevant for the terminals with the same device position.

*bNumberByLevels*
:   If set to true, the terminals are numbered by level.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Is thrown in case of invalid arguments. |
| **ArgumentNullException** | Is thrown, if some of the arguments are NULL. |
| **ApplicationException** | A necessary internal interface for creating devices could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | If an error occurred while creating terminals. |

Remarks

If the chosen article is not a multilevel terminal, the parameter bNumberByLevels will be set to false.
