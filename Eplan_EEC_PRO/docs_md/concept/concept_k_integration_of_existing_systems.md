---
title: "Integration of existing systems"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_integration_of_existing_systems.htm"
file: "concept_k_integration_of_existing_systems"
category: "concept"
---

# Integration of existing systems

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Integration of existing systems

The following diagram shows how the functional configuration procedure is implemented using EEC:

The first step is to functionally configure customer-specific machines and plants. Discipline-specific configurations are created from the mechatronic configuration using **structure generators**. Finally, **system-specific generators** use the individual, discipline-specific configurations to create project documents for further processing in the existing systems.

In the construction phase of a mechatronic modular structure, it is not possible to create discipline-specific configurations straightaway in a fully automated manner. In this case, it is still necessary to manually configure and parameterize the discipline-specific configurations.

The following diagram illustrates how existing systems are integrated into EEC, thus making model-driven configuration possible.

The components managed in EECâs information model are only placeholders for **resources** , for example, parameterizable parts of wiring diagrams or PLC function blocks that are still created using the original systems in file formats specific to those systems.

Discipline-specific components can serve as a basis for configuring whole wiring diagrams, PLC programs, etc. The corresponding **project documents** are created from the information model by **system-specific generators** using referenced resources.

Virtual mechatronic components can be defined based on discipline-specific components. They facilitate the functional configuration process, by which the mechatronic configuration is created.

This procedure makes it possible to configure in parallel on both functional and discipline-specific levels.
