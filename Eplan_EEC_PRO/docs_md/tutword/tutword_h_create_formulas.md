---
title: "Creating formulas for image objects in the parameters"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutword_h_create_formulas.htm"
file: "tutword_h_create_formulas"
category: "tutword"
---

# Creating formulas for image objects in the parameters

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating formulas for image objects in the parameters The text #{Image:Logo} is now shown instead of the logo on the cover sheet of the document. A formula that returns the image of the Eplan logo is now used for the Logo parameter.
    1. Open the Feeder station.
    2. Select the installed components ListOfComponents.
    3. Enter the =type('T_Mechatronic_ModularSystem.Images.Logo').image formula for the Logo parameter in the Value column.
With type(âT_Mechatronic_ModularSystem.Images.Logoâ), the formula identifies the image object Logo and returns the image using the Image method. In the Word component Row, the Icon parameter is contained in the first column of the table. Only the text #{Image:Icon} was previously displayed. A formula is added for the Icon parameter in the component Row. This identifies an image in the Actuators_Sensors_Imageregister image register that matches the type of the current component.
    1. Open the component Row.
    2. Enter the =type('T_Mechatronic_ModularSystem.Images.Actuators_Sensors_Imageregister').image(mc.type) formula as the value for the Icon parameter:
    3. Save the component Row.
    4. All the formulas for the image objects are created as a result.
