---
title: "Configuring components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_configuring_components.htm"
file: "concept_k_configuring_components"
category: "concept"
---

# Configuring components

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Development steps for configurations

The configuration of machines and plants can be done completely manually, whereby a high degree of engineering knowledge is required. However, this can also be executed fully automatically by third party systems, for example SAP. This includes development steps that enable a manual configuration by users without engineering knowledge as well as configuration options that can be performed from distributed locations.

### [Manual configuration by users with extensive engineering knowledge](javascript:void\(0\);)

A modular system with few mechatronic components can serve as the initial model.

     * The mechatronic components are directly derived from MechatronicComponent and can be freely nested within each other.
     * The parameters save texts (strings) and numbers (integer).

The following figure shows a modular system with mechatronic components for a machine and three mechatronic components of a power supply. The mechatronic components of the power supply appear in all machines

Disadvantages:

     * None?
image/svg+xml Click to toggle between initial and next level Modular System Machine PageNumber Location HLFunction DocumentKind PageNumber Location HLFunction DocumentKind PageNumber Location HLFunction DocumentKind PowerSupply_400V_230VAC PowerSupply_24VDC_PLC PowerSupply_24VDC_Devices 1 Q1 GB1 EFS1 1 Q2 GD2 EFS1 1 Q2 GD1 EFS1 PageNumber Location HLFunction DocumentKind EFS1This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Development steps for configurations

The configuration of machines and plants can be done completely manually, whereby a high degree of engineering knowledge is required. However, this can also be executed fully automatically by third party systems, for example SAP. This includes development steps that enable a manual configuration by users without engineering knowledge as well as configuration options that can be performed from distributed locations.

### [Manual configuration by users with extensive engineering knowledge](javascript:void\(0\);)

A modular system with few mechatronic components can serve as the initial model.

     * The mechatronic components are directly derived from MechatronicComponent and can be freely nested within each other.
     * The parameters save texts (strings) and numbers (integer).

The following figure shows a modular system with mechatronic components for a machine and three mechatronic components of a power supply. The mechatronic components of the power supply appear in all machines

Disadvantages:

     * None?
image/svg+xml Click to toggle between initial and next level Modular System Machine PageNumber Location HLFunction DocumentKind PageNumber Location HLFunction DocumentKind PageNumber Location HLFunction DocumentKind PowerSupply_400V_230VAC PowerSupply_24VDC_PLC PowerSupply_24VDC_Devices 1 Q1 GB1 EFS1 1 Q2 GD2 EFS1 1 Q2 GD1 EFS1 PageNumber Location HLFunction DocumentKind EFS1 PowerSupply

### [Manual configuration by users with little engineering knowledge](javascript:void\(0\);)

     * Instances have been created and parameterized by means of a user interface (Form-UI).
     * A graphic diagram (Graph2D) can be used for instancing and specific user interfaces (Form-UIs) can be used to parameterize the instances.
     * All entries are validated so that there is no risk of incorrect entries.
     * The generation of the target documents is initiated directly by the user.
     * The target documents are created by the same computer that performs the configuration.

[](../Pictures/tutorial_g2d_test4_tooltip_etage.png)

### [Manual import of partial configurations by users with little engineering knowledge](javascript:void\(0\);)

     * By means of a user interface (Form-UI), required partial configurations are imported and this way added to an existing project basis.
     * The generation of the target documents is initiated directly by the user.
     * The target documents are created by the same computer that performs the configuration.

[](../Pictures/2018091101.png)

### [Manual configuration by users who are located in multiple locations](javascript:void\(0\);)

     * Web EEC provides the user interface (Form-UI) via online connections..
     * Instances are created and parameterized via the user interface. This can be also only a partial configuration for a certain part of the machine or plant.
     * The generation of target documents can be initiated directly by the user but also by other parties.
     * The target documents are created by a central computer that also provides the Web EEC.

[](../Pictures/2018091001.png)

### [Fully automated configuration](javascript:void\(0\);)

     * Third party systems, for example SAP, determine the configuration of a machine or plant.
     * The configuration data is transferred as a so called job definition to the Job Server.
     * The Job Server passes the job definitions to so called Workers who are capable of handling these job definitions.
     * The Workers can:
       * Create new projects.
       * Import partial projects.
       * Instantiate components.
       * Parameterize components.
       * Create target documents.
     * The Job Server in turn makes the created target documents available to the requester.

[](../Pictures/2018091102.png)

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Configuring components

Requirements for configuring components are derived from the following objectives for configuring a modular system:

     * **Universal applicability:** A modular system should be designed in such a way as to ensure that as many variants of customer-specific machines as possible can be configured using the components.
     * **Simple configuration:** Minimal effort should be expended in configuring and parameterizing the components.

New requirements that cannot be met with existing components lead to further development of the modular system. This process involves two different principles, both of which are illustrated in the following diagram.

Two variants, A and B, are depicted on the left side of the Variant generation diagram. They differ only in terms of the alternative subcomponents D and E. The modular system in the example contains two component classes, A and B, for the two variants. In order to reduce variance, the modular system can be further developed by applying the following principles:

     * **Generalization:** The difference between variants **A** and **B** lies in the installation angle. Thus, components A and B can be generalized into a powerful component F by having an angle parameter assigned to describe the installation position.
     * **Decomposition :** The components are assembled out of smaller components. In the example presented above, three components are admittedly created from what were originally two components; redundancies are avoided, however. Furthermore, the process yields fine-grained components (for example, C) that are reusable in further variants.

Depending on the focus of the principles being applied, the configuration effort is divided between configuration and parametrization tasks. Should the parametrization of powerful components become too complicated, decomposition of these components is often necessary. If the number of components to be managed in the modular system threatens confusion, it is helpful to generalize.
