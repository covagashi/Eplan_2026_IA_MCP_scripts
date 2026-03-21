---
title: "Development steps for configurations"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_configurations_development.htm"
file: "concept_k_configurations_development"
category: "concept"
---

# Development steps for configurations

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
