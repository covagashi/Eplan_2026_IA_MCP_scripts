# GenerateSchematic Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService~GenerateSchematic.html

---

Generates PLC schematic pages.

Syntax

**C#**



public Page[] GenerateSchematic( 

   Project oProject,

   string strConfigFileName,

   bool bGenerateSingleLineRepresentations,

   bool bGenerateMultiLineRepresentations,

   bool bGenerateOverviews,

   bool bGenerateRackOverviews

)

public:

array<Page^>^ GenerateSchematic( 

   Project^ oProject,

   String^ strConfigFileName,

   bool bGenerateSingleLineRepresentations,

   bool bGenerateMultiLineRepresentations,

   bool bGenerateOverviews,

   bool bGenerateRackOverviews

)


#### Parameters

*oProject*
:   Project into which the PLC schematic pages will be generated.

*strConfigFileName*
:   The config \file name in the xml format.

*bGenerateSingleLineRepresentations*
:   the pages of the type "SingleLine" should be generated

*bGenerateMultiLineRepresentations*
:   the pages of the type "MultiLine" should be generated

*bGenerateOverviews*
:   the pages of the type "Overview" should be generated

*bGenerateRackOverviews*
:   the pages of the type "RackOverview" should be generated

#### Return Value

returns changed pages.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing parameters. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the given Project does not exist or isn't valid. |
| **ApplicationException** | Internal interface for generating plc schematic pages could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Error during plc schematic pages generating. |

Remarks

Description of the available XML tags:

root node of xml file:  
PLC\_CONFIG\_FILE

node attributes:  
FileName - path of the XML file(purely informative)  
Type - "PLC schematics generator"(purely informative)  
Version - version of the XML file(z.Z.: "1.0")

standard node:  
DEVICE - device data

node attribute  
Name - Device tag, e.g.: "=EB3+ET1-A7"

standard node:  
Function - data of the individual functions of the device

node attributes:  
Name - function name, e.g.: "=EB3+ET1-A7:1"  
Macro - path to the macro file, e.g.: "$(MD\_MACROS)\\PLC\\Beschaltung1.ema"  
FuncText - function text (multi language string)  
SingleLinePage - name of the single-line page  
SingleLinePageLadder - ladder of the single-line page (calculated by the GUI function 'Calculate pages...')  
MultiLinePage - name of the multi-line page  
MultiLinePageLadder - ladder of the multi-line page (calculated by the GUI function 'Calculate pages...')  
OverviewPage -overwiew page  
RackPage -rack page

standard node:  
Variable - variable of the placeholder object in the macro

node attributes:  
Name - name of the variable  
Value - value to be set for the variable

Example

The XML file has the following format:

- [XML](#i-tab-content-1d838eba-07f6-4532-9577-5d9b7ebdabbe)

```
<?xml version="1.0" encoding="utf-8" ?>

<PLC_CONFIG_FILE FileName="C:\\Users\\EPL\\Desktop\\PLC.xml" Type="PLC schematics generator" Version="1.0">

 <DEVICE Name="=EB3+ET1-A1">

  <Function Name="=EB3+ET1-A1" Macro="$(MD_MACROS)\\SIE.6ES7315-2AG10-0AB0.ema" FuncText="de_DE@CPU 315-2 DP&#10;input 24VDC;en_US@CPU 315-2 DP&#10;input 24VDC;" SingleLinePage="=EB3+ETA/1" MultiLinePage="=EB3+EBS/1"/>

  <Function Name="=EB3+ET1-A1:X1" SingleLinePage="=EB3+ETA/1"/>

  <Function Name="=EB3+ET1-A1:X2"/>

  <Function Name="=EB3+ET1-A1:L+" MultiLinePage="=EB3+EBS/1"/>

  <Function Name="=EB3+ET1-A1:M1" MultiLinePage="=EB3+EBS/1"/>

  <Function Name="=EB3+ET1-A1:M2" MultiLinePage="=EB3+EBS/1"/>

  <Function Name="=EB3+ET1-A1:PE" MultiLinePage="=EB3+EBS/1"/>

 </DEVICE>

</PLC_CONFIG_FILE>
```
