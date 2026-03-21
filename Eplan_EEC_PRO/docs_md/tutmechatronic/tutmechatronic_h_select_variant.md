---
title: "Select variant"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutmechatronic_h_select_variant.htm"
file: "tutmechatronic_h_select_variant"
category: "tutmechatronic"
---

# Select variant

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Select variant Which variant of the component is used is determined at the time the component is used. Enable or disable the Inspect component by alternately setting the Option_Inspect_available parameter to true and false.
    1. Select the Parameters editor.
    2. For the Option_Inspect_available parameter, enter alternately true or false in the Value column.
You can see the result in the Project Catalog immediately after saving. Disabled components are not displayed in the Project Catalog if the filter is set up and enabled accordingly. For this purpose, click  and select the Disabled Components check box. After closing the filter dialog with [OK], the filter is enabled with the  icon. The Axis component is only used for Move, as X_Axis and Y_Axis. Y_Axis is the variant not specified; here, the parameters Sensor_2_available, Sensor_3_available, and Sensor_4_available must be given the value false:
    1. Open the Move function group.
    2. Select the component Y_Axis.
    3. In the table on the right, specify the value false in the rows Sensor_2_available, Sensor_3_available, and Sensor_4_available in the Value column.
The modifications are visible in the project without updating (via [F5]). X_Axis continues to have three sensors, while Y_Axis has only one Position_1 position sensor. X_Axis of the Move Functiongroup, depending on the Inspect Functiongroup, is to be equipped with or without the position sensors Position_2 and Position_3. For this purpose, the value of the Option_Inspect_available parameter is evaluated. Disabled components are not displayed in the Project Catalog if the filter is set up and enabled accordingly. For this purpose, click  and select the Disabled Components check box. After closing the filter dialog with [OK], the filter is enabled with the  icon.
    1. Open the Move function group.
    2. Click the X_Axis component.
    3. In the Value column for the parameters Sensor_2_available and Sensor_3_available, enter the formula: =mroot.$Option_Inspect_available.
In the formula, mroot references the root element of the mechatronic structure; in this case, Feeder, and $Option_Inspect_available queries the value of the parameter of the same name. A change to the Option_Inspect_available parameter now does not only affect the presence of the function groups Inspect and Discard, but also at the same time the presence of the position sensors Position_2 and Position_3. Test this behavior again, as already done before: If you set the value of the Option_Inspect_available parameter to true, the function groups Inspect and Discard, as well as the position sensors Position_2 and Position_3 will be installed. If you set the value of the Option_Inspect_available parameter to false, the function groups Inspect and Discard, as well as the position sensors Position_2 and Position_3 will be removed (see figure above). Disabled components are not displayed in the Project Catalog if the filter is set up and enabled accordingly. For this purpose, click  and select the Disabled Components check box. After closing the filter dialog with [OK], the filter is enabled with the  icon.
