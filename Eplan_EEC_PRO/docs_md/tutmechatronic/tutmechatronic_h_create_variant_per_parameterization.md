---
title: "Generation of variants via parameterization"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutmechatronic_h_create_variant_per_parameterization.htm"
file: "tutmechatronic_h_create_variant_per_parameterization"
category: "tutmechatronic"
---

# Generation of variants via parameterization

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Generation of variants via parameterization The structure of the Feeder component is not yet correct:
     * The function groups Inspect and Discard are permanently missing, and should be able to be enabled or disabled by means of a parameter.
     * The Axis component is used in two variants: On the one hand as X_Axis with four sensors and on the other hand as Y_Axis with a single end position sensor. In the following, the Axis component in the modular system is supplemented by three parameters to configure that an Axis component is used with one, two or four sensors. X_Axis should have four position sensors only if the function groups Inspect and Discard are available (see [Functional assembly](tutorial_k_example_feeder_functional_structure.htm)).
