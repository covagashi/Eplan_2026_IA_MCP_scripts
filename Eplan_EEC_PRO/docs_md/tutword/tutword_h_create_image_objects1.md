---
title: "Creating image objects and image registers"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutword_h_create_image_objects1.htm"
file: "tutword_h_create_image_objects1"
category: "tutword"
---

# Creating image objects and image registers

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating image objects and image registers The images for the tutorial have to be copied into the folder <Installation path>/resources/MediaSources.
    1. Copy the files Aktor.gif, Logo.gif and Sensor.gif from the folder <Installation path>/install/icon-collection into the folder <Installation path>/resources/MediaSources.
Image objects are created in a new unit.
    1. Create the Images unit in the T_Mechatronic_ModularSystem library.
    2. Select the Images unit.
    3. Select New > Media sources > Image in the shortcut menu of the unit.
    4. Enter Actuator in the Name field.
    5. Click Import.
    6. Select the resources/MediaSources\Aktor.gif image. The path for this image is saved in the Resource path field.
    7. Repeat Steps 2 to 6, assign the Sensor name to the new image object and select the image Sensor.gif.
    8. Repeat Steps 2 to 6, assign the Logo name to the new image object and select the image Logo.gif.
The image register is created subsequently:
    1. Select the Images unit.
    2. Select New > Media sources > Image register in the popup menu of the unit.
    3. Enter Actuators_Sensors_Imageregister in the Name field.
    4. Open the Image assignment editor page.
    5. Click .
    6. Select the component Actuators from T_Mechatronic_Architecture.Levelcomponents.
    7. Select the image object Actuator in the Library component image field and in the Project component image field.
    8. Repeat steps 5 to 7 and select Sensor from T_Mechatronic_Architecture.Levelcomponents as well as the image object Sensor.
    9. Save the image register.
The result should correspond to the following image:
