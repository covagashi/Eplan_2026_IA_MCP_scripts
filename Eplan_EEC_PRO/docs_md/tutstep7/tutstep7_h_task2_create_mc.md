---
title: "Creating the mechatronic component for the controller"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutstep7_h_task2_create_mc.htm"
file: "tutstep7_h_task2_create_mc"
category: "tutstep7"
---

# Creating the mechatronic component for the controller

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating the mechatronic component for the controller The SiemensCPU controller requires a mechatronic component that can be used to calculate parameter values during the generation of the addresses.
    1. Select the ControllerComponents unit.
    2. From the popup menu, select New > Mechatronic > Functionunit.
    3. In the Name field, enter the text S7_313C.
    4. Open the Interfaces editor.
    1. Click .
    2. Click [Search].
    3. Select the IController interface.
    4. Confirm with [OK].
Due to the interdependencies, the ICoupler and ITerminal interfaces are also inserted.
