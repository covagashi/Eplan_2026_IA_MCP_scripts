---
title: "Libraries and projects"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_libraries_and_projects.htm"
file: "concept_k_libraries_and_projects"
category: "concept"
---

# Libraries and projects

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Libraries and projects

One important task of EEC is to structure components and projects clearly and transparently. An important boundary condition here is that order-specific machines and plants should be configured using components that are reusable to varying degrees. Projects are therefore configured and parameterized using**libraries** at different **reuse levels**.

Components that can be reused in any project (company-wide) are maintained in the **standard library**. At this reuse level, a **prototype library** can be defined that contains fully configured projects or sub-projects as prototypes for copying specific configurations.

In addition to **standard solutions** that can be used throughout the company, **machine-specific solutions** are very common. It is therefore good practice to maintain these solutions not in the standard library, but in a library specific to the machine type, e.g. in a honing library for honing machines. Furthermore, **specialized, project-specific solutions** , such as a specific robot controller, are required when constructing specialized machines. These solutions are maintained in a **special library**.

Components from libraries above the project level as well as from the project-specific special library can be applied in the configuration process. However, the systematics presented here prohibit a component from the special library of Project 8396, for example, from being used in Project 8395; furthermore, components from the honing library can only be used for honing machines, etc.

Finally, the example presented in the Reuse levels for components diagram can serve as a basis for a more precise definition of the concept of modular systems. A project engineer defines a **modular system **by inventorying all of the libraries above the level of his project. The modular system for Project 8396 consists of the standard library and the honing library.
