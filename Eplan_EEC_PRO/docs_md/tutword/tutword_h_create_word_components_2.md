---
title: "Splitting the target file into Word resources"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutword_h_create_word_components_2.htm"
file: "tutword_h_create_word_components_2"
category: "tutword"
---

# Splitting the target file into Word resources

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Splitting the target file into Word resources Before you can define Word components, it is necessary to create the documents required for this purpose. The predefined target file has to be split up into a main document and several fragment documents in a way that allows the target file to be recreated from them.
    1. Open the ListOfComponents.docx file located in the <EEC installation folder>\install\Tutorial\Word folder.
    2. Replace the heading List of Components with #(Heading) on the first page.
The number string #{ instructs the parser to treat the following text up to character } as the name of a parameter and to replace with the parameter value.
    1. Also replace the image with #(Image:Logo) on the first page.
The parameter type is specified here as Image in front of the name of a parameter. Without this information String would be used as the type and, as a result, no image returned. Do not make any changes to the table of contents.
    1. Delete everything below the second heading 1.1 Actuators on the third page and replace Actuators with (*{LOOP:dos}*)(*{Content}*)(*{END_LOOP}*).
The line contains three commands in the form of (*{â¦}*). The first and last commands act as a loop construct that iterates across all directly contained discipline components (dos = **d** iscipline **o** bject**s**). The middle command is responsible for their content.
    1. Save the document as Body.docx in the folder resources\Office\Word\Tutorial.
    2. Repeat the first step.
    3. Delete pages 1 and 2, the heading 1 Actuators and Sensors, the heading 1.2 Sensors the Sensors table.
    4. Replace the heading 1.1 Actuators with #{Heading}.
    5. Replace the word Actuators with #{Heading} in the table header.
    6. Replace the image for actuator () with (*{LOOP:dos}*) in the first row, the image for actuator () with (*{Content}*) in the second row, and the image for actuator () with (*{END_LOOP}*) in the third row in the Symbol column.
    7. Delete all table rows below this (positions 4 to 7).
    8. Delete the contents from the table cells below Position and Description.
    9. Add a second blank row below the table.
    10. Save the document as Chapter.docx.
    11. Repeat the first step.
    12. Delete pages 1 and 2, all headings, and the bottom table.
    13. Delete everything except for the final row in the remaining table.
    14. Replace the image for actuator () with the #{Image:Icon} parameter, the number of the position with the #{Pos} parameter, and the descriptor with the #{Descriptor} parameter in the remaining table row.
    15. Save the document as Row.docx.
