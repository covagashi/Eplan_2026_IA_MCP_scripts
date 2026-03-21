---
title: "Generating the current status of the component list"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutword_h_test2.htm"
file: "tutword_h_test2"
category: "tutword"
---

# Generating the current status of the component list

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Generating the current status of the component list Generate the current status of the component list.
    1. In the Project Explorer select the Mechatronic component.
    2. In the popup menu select Word > Generate and open Word document.
This operation creates an error. The reason for this is that the component Image.Logo to be accessed in the model has not yet been created. The error message can be acknowledged by pressing [OK].
    1. In the popup menu select Word > Update Word document fields.
The discipline structure for Word is generated in parallel to Mechatronic. The structure consists of the project components ListOfComponents as instance of the component Body and two project components ActuatorsTable and SensorsTable as instances of the component Chapter. The created ListOfComponents document is saved to the Workspace folder Word\Word and looks as follows:
    1. The parameter specifications #{Heading} are replaced by their values in the ListOfComponents document.
    2. The components ActuatorsTable and SensorsTable are inserted.
    3. The logo on the cover sheet is missing.
    4. The table of contents is not up-to-date, although the contents that are shown appear to be correct.
