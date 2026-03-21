---
title: "Setting a breakpoint"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecscripting_k_debug_set_breakpoint.htm"
file: "eecscripting_k_debug_set_breakpoint"
category: "eecscripting"
---

# Setting a breakpoint

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Setting a breakpoint Eclipse makes a perspective available for the debugging in which all required elements are displayed. This includes views on the stack, the variables, breakpoints, the code editor, the console etc. In addition buttons for starting debugging, stopping, skipping, etc. can be displayed. In order to halt the execution of a plug-in at a specific position, a break-point is set in the code editor. This is accomplished by double-clicking the left edge of a line of code. The following screenshot shows Eclipse in the debug perspective with the IncrementLength halted. The breakpoint is set in Line 28 in the figure above. The breakpoint is depicted as a filled circled. As soon as the execution of the code halts at this point, the current values of the variables are displayed in the Variables tab. The buttons with which the execution of the method is controlled are located in the toolbar of the Debug tab. Changes to the method can be made directly in the Debug perspective and tested. If the result is satisfactory, the method can be exported as a plug-in and directly used in the EEC (see [Compiling and exporting a plug-in](eecscripting_k_implement_compile_and_export_plugin.htm)).
