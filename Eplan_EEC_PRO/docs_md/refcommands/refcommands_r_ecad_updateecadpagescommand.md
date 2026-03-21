---
title: "ECAD.UpdateEcadPagesCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refcommands_r_ecad_updateecadpagescommand.htm"
file: "refcommands_r_ecad_updateecadpagescommand"
category: "refcommands"
---

# ECAD.UpdateEcadPagesCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  ECAD.UpdateEcadPagesCommand Generates a project with specific pages of an Eplan Electric P8 project depending on the preference Reuse existing project for schematic generation. A list with pages and/or fragments which are located within the discipline structure is handed over as the argument of the command.
     * The preference Reuse existing project for schematic generation is marked,
     * The Page number model variable is set and valid values are assigned.
The generated project contains all pages of the existing project. Only marked pages are re-generated. Pages of the same page number are replaced and completely new pages are added in accordance with the page number.
     * The preference Reuse existing project for schematic generation is marked,
     * The Page number model variable is not set.
The generated project contains all pages of the existing project unchanged. The pages passed in the list or the pages of fragments passed in the list are completely re-generated and added to the new pages. The preference Reuse existing project for schematic generation is not marked: The original project is deleted in the workspace. The generated project only contains those pages that contain the listed fragments and the directly specified pages. All other pages are not considered during generation. Argument | Type | Description  
---|---|---  
pages | List | Schematic pages and fragments within the discipline structure that are to contain the generated project.  
      
        ECAD.UpdateEcadPagesCommand(=List{mos('WiringDiagram').first.derived.dos('T_Mechatronic_ModularSystem.ECAD.Page.Page')})

[Example in Form-UI](javascript:void\(0\);)
    
        <action name="ECAD.ECAD.UpdateEcadPagesCommand"
    	arguments="=List{mos('WiringDiagram').first.derived.dos('T_Mechatronic_ModularSystem.ECAD.Page.Page')}"
    	type="link">Update pages</action>
