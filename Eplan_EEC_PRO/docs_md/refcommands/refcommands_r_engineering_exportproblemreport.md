---
title: "Engineering.ExportProblemReport"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_engineering_exportproblemreport.htm"
file: "refcommands_r_engineering_exportproblemreport"
category: "refcommands"
---

# Engineering.ExportProblemReport

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Engineering.ExportProblemReport Engineering.ExportProblemReport Exports the current model as a ZIP archive with the name Report_<priority>_<YYYY-MM-DD_HH-MM>.zip, creates a Quality Feedback Report and starts the local e-mail client in order to send the Quality Feedback Report. Argument | Type | Description  
---|---|---  
description | String | Description of the problem  
priority | String | Priority of the problem  
includeModel | Boolean | Option indicating whether the model should be attached as a ZIP file.  
true = attach model  
false = do not attach model  
sendViaEmail | Boolean | Option indicating whether the Quality Feedback Report should be sent via the e-mail client.  
true = the e-mail client opens with a new e-mail addressed to support.  
false = the Quality Feedback Report is not sent via e-mail.
