---
title: "Specify subcomponents of function groups"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutmechatronic_h_specify_subcomponents_of_functiongroups.htm"
file: "tutmechatronic_h_specify_subcomponents_of_functiongroups"
category: "tutmechatronic"
---

# Specify subcomponents of function groups

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Specify subcomponents of function groups In the case of the Feeder component, there are variances â for example, the function groups Inspect and Discard are installed only on an optional basis. If these variances are ignored at first (this will be addressed later), the entire functional assembly structure (see [Functional assembly](tutorial_k_example_feeder_functional_structure.htm)) can be predefined already in the modular system. Like with the Functiongroups for the Feeder station, the Functionunits must be added to the Functiongroups as components:
    1. Open Insert, and drag the Functionunits Separator and Stack to the components editor area (Components).
    2. Add the Orientationinspector Functionunit forInspect.
    3. For the Move Functiongroup, specify the Axis twice and the Gripper once as a component. The second Axis component will be inserted as Axis2 because components must be given unique names:
    4. Rename Axis to X_Axis and Axis2 to Y_Axis: Select the components to be renamed and with a further click switch to the editor mode (identifiable by the fact that only the text without a symbol is highlighted). Alternatively â as in the Library Catalog or Project Catalog view â you can switch to the editor mode using the [F2] function key.
Result:
