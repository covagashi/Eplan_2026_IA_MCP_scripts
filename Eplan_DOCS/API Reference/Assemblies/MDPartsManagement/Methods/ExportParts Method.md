# ExportParts Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~ExportParts.html

---

Exports parts and other parts management items like addresses, constructions, terminals, accessory lists and accessory placements from the system's parts database.

Syntax

**C#**



public void ExportParts( 

   string strFilePath,

   string strConverter,

   string strPartsFilterScheme,

   bool bExportParts,

   MDObjectFilter filterParts,

   bool bExportAddresses,

   MDObjectFilter filterAddresses,

   bool bExportConstructions,

   MDObjectFilter filterConstructions,

   bool bExportTerminals,

   MDObjectFilter filterTerminals,

   bool bExportAccessoryLists,

   MDObjectFilter filterAccessoryLists,

   bool bExportAccessoryPlacements,

   MDObjectFilter filterAccessoryPlacements

)

public:

void ExportParts( 

   String^ strFilePath,

   String^ strConverter,

   String^ strPartsFilterScheme,

   bool bExportParts,

   MDObjectFilter^ filterParts,

   bool bExportAddresses,

   MDObjectFilter^ filterAddresses,

   bool bExportConstructions,

   MDObjectFilter^ filterConstructions,

   bool bExportTerminals,

   MDObjectFilter^ filterTerminals,

   bool bExportAccessoryLists,

   MDObjectFilter^ filterAccessoryLists,

   bool bExportAccessoryPlacements,

   MDObjectFilter^ filterAccessoryPlacements

)


#### Parameters

*strFilePath*
:   Full output file name.

*strConverter*
:   Converter long name, see [XPamExport](XPamExport.html) for converters

*strPartsFilterScheme*
:   Filter scheme as defined in parts management navigator.

*bExportParts*
:   Enables export for parts.

*filterParts*
:   Defines additional filter for the export for parts.

*bExportAddresses*
:   Enables export for customers and manufacturers.

*filterAddresses*
:   Defines additional filter for the export for customers and manufacturers.

*bExportConstructions*
:   Enables export for drilling patterns.

*filterConstructions*
:   Defines additional filter for the export for drilling patterns.

*bExportTerminals*
:   Enables export for connection point patterns.

*filterTerminals*
:   Defines additional filter for the export for connection point patterns.

*bExportAccessoryLists*
:   Enables export for accessory lists.

*filterAccessoryLists*
:   Defines additional filter for the export for accessory lists.

*bExportAccessoryPlacements*
:   Enables export for accessory placements.

*filterAccessoryPlacements*
:   Defines additional filter for the export for accessory placements.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred while exporting parts data. |
