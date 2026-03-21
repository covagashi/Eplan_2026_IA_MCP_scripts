---
title: "Splitting the target file into text resources"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tuttext_h_create_text_discipline_components_split_target_into_text_resources.htm"
file: "tuttext_h_create_text_discipline_components_split_target_into_text_resources"
category: "tuttext"
---

# Splitting the target file into text resources

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Splitting the target file into text resources Before you can define text discipline components, it is necessary to create the text fragments required for this purpose. The predefined target file has to be split up into text fragments in a way that allows the target file to be recreated from them:
    1. Open ListOfComponents.txt located in the install\Tutorial\ListOfComponents sub-folder using a text editor.
    2. Replace all lines except the first two (heading and underlining) with the line (*{LOOP:dos}*)(*{Content}*)(*{END_LOOP}*). The line contains three commands in the form of (*{â¦}*). The first and last commands act as a loop construct that iterates across all directly contained discipline components (dos = "discipline objects"). The middle command is responsible for their content.
    3. Save the open text file as Body.txt in the folder Installation folder\resources\Tutorial\ListOfComponents.
    4. Repeat the first step.
    5. Delete the first two lines and replace Actuators with the parameter #{Heading}.
    6. Replace the list and everything else with the same line used in step 2: (*{LOOP:dos}*)(*{Content}*)(*{END_LOOP}*).
    7. Save the open text file as Chapter.txt in the folder Installation folder\resources\Tutorial\ListOfComponents.
    8. Repeat the first step.
    9. Delete everything except for one list line with line break. Replace the number with the #{Pos} parameter and the descriptor with the #{Descriptor}.
    10. Save the open text file Line.txt in the folder Installation folder\resources\Tutorial\ ab ListOfComponents.
