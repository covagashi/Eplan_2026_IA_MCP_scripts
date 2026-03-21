---
title: "Parameters ExportParamFilter and ExportTableFilter"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecsap_k_library_sap_toolkit_exportparamfilter_and_exporttablefilter.htm"
file: "eecsap_k_library_sap_toolkit_exportparamfilter_and_exporttablefilter"
category: "eecsap"
---

# Parameters ExportParamFilter and ExportTableFilter

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Parameters ExportParamFilter and ExportTableFilter

The ExportParamFiler and ExportTableFilter parameters contain filter settings that should return data to the SAP modules:

     * Not specified: All data that the SAP module provides is returned.
     * Limitation: Only the data of the SAP module that was requested will be returned.

In principle, you can filter return tables with the ExportTableFilter parameter if a callup returns multiple tables.

### [Example](javascript:void\(0\);)

The SAP callup RFC_SYSTEM_INFO delivers the four structures MAXIMAL_RESOURCES, RFCSI_EXPORT, CURRENT_RESOURCES and RECOMMENDED_DELAY

For EEC only the RFCSI_EXPORT structure is interesting.

To only determine this structure the ExportParamFilter parameter has to be set to the value =List{'RFCSI_EXORT'}.
