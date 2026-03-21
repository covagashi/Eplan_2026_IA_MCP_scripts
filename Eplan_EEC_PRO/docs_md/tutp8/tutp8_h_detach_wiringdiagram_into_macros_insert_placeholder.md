---
title: "Creating a placeholder object macro for a page"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutp8_h_detach_wiringdiagram_into_macros_insert_placeholder.htm"
file: "tutp8_h_detach_wiringdiagram_into_macros_insert_placeholder"
category: "tutp8"
---

# Creating a placeholder object macro for a page

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating a placeholder object macro for a page Insert a placeholder object in order to define the function texts as placeholders. Each function text is assigned a variable name. When the macros are imported into EEC, a parameter of the same name is created for each variable. These parameters store meaningful texts in EEC that are used instead of placeholders when generating the schematics.
    1. Select the following commands: Tab Insert > Command group Navigator > Insert placeholder object.
    2. Drag a frame around the power supply lines and PLC inputs.
    3. The Properties (components): Placeholder object opens.
    4. Open the popup menu of the table.
    5. Select Adopt variables.
    6. The Variable column is then automatically filled with the name of the variables.
Note The variables for the socket and plug parameters must not be entered in the Variable column, so that no duplicate objects can be created during the automatic application of the parameters.
    1. Select the Page property.
    2. Click  (New).
    3. The Property selection dialog opens.
    4. In the list select the entry Page description.
    5. Confirm with [OK].
    6. The Property selection dialog is closed and you are returned to the dialog Properties (components): Placeholder object.
    7. In the Variable column, enter <PageDescription>.
    8. From the Variable column remove all variable entries for socket parameters (#<Socket:Input1> to #<Socket:Input8>).
    9. Open the Values tab.
    10. From the Variable column remove all variable entries for socket parameters (#<Socket:Input1> to #<Socket:Input8>).
    11. Confirm with [OK].
    12. The Properties (components): Placeholder object is closed.
