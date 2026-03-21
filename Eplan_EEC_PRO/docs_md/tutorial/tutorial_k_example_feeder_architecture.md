---
title: "Architecture model"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutorial_k_example_feeder_architecture.htm"
file: "tutorial_k_example_feeder_architecture"
category: "tutorial"
---

# Architecture model

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Architecture model In order to be able to combine and reuse library components in any project, a company must define general structures based on which components are developed and used. This is done by means of an architecture model. Terms such as function group and function have already been used in the feeder description. They correspond to a definition of hierarchical levels in a machine or plant specified by the Esslingen University of Applied Sciences for the feeder components. Other companies may, for example, alternatively use units, modules, or segments. Rules that are used as the basis for the modular system of feeders:
     * Stations contain function groups.
     * Function groups are comprised of function units.
     * Function units contain actuators and sensors.
Under these rules, a function group or station is, for example, not permitted to contain a sensor. The formal mapping of these rules in a library that defines the architecture model is shown in the following diagram: The rule for permitted sublevels is formalized using the is a permitted sublevel of relationship (shown using a dashed line and a filled rhombus), for example between Functiongroup and Functionunit. This property is inherited by all derived components (e.g., insert and separator). Because all library components inherit from an architecture model component, the rules apply to all modular system developers; in other words, a modular system developer cannot, for example, create a function group that contains a sensor. The following sections show step-by-step how to model the architecture model introduced in this section, the modular system, and the feeder project in EEC. The individual steps are structured as follows:
     * **Motivation:** This will explain why the step is necessary.
     * **Screenshot:** The screenshot shows EEC interface that should correspond to the current process step. Screenshots are also provided at the relevant locations and job steps.
     * **Step-by-step instructions:** A detailed description of the job steps are then provided in the step-by-step instructions.
