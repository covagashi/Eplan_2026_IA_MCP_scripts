---
title: "Generation of variants via disabler"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutmechatronic_h_create_variants_per_disabler.htm"
file: "tutmechatronic_h_create_variants_per_disabler"
category: "tutmechatronic"
---

# Generation of variants via disabler

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Generation of variants via disabler First, using the maximum principle, all possible components are created in the library. To create variants, the components that are not to be included will be excluded (disabled) by the composition. In this tutorial, we do not want to use in the Feeder component the function groups Inspect and Discard. For this purpose, we disable the installed components Inspect and Discard.
    1. Open the Feeder component.
    2. Click the installed component Inspect.
    3. In the Disabled field, enter = true.
    4. Repeat the steps 2 to 3 for the Discard component.
The effect is visible in the project without updating via [F5]: In the Feeder project component, only the components Store, Insert, and Move remain. Note As long as the filter is not enabled, the disabled components will be displayed as well. The filter is enabled in the toolbar of the Project Catalog.
    1. Enable the filter by clicking .
    2. Open the filter dialog by clicking .
You set the options in the filter dialog.
    1. Highlight the Disabled Components option.
