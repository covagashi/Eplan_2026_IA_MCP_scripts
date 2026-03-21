---
title: "IO generation"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_io_generation.htm"
file: "concept_k_io_generation"
category: "concept"
---

# IO generation

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## IO generation

Controllers are hierarchically structured. They have at their disposal a **controller computer** with programs that evaluate signals coming from sensors connected to the inputs and use this data to calculate what signals are to be sent to the actuators. In the following subsection, inputs and outputs are summarized under the rubric of **connection points**. Terminals are connected to the controller by means of so-called **bus terminals**. Bus terminals offer special inputs and/or outputs depending on the type of terminal. **Bus couplers** can be used to interconnect terminals or other bus couplers with **bus systems** that ultimately connect to the controller computer (CPU) (see the below diagram).

One task when building the controller is to connect the actuators and sensors to their intended, uniquely addressed connection points. In the process, boundary conditions that are specific to the machine or company have to be observed, for example, that when the emergency-off switch is activated, a gripper should not drop a workpiece it has just grasped, or that cables should not be run through the machine.

The **3-station machine with controller** diagram presents the layout of a simple 3-station machine with a hard-wired controller. Concepts fundamental to the modeling process are explained in the following passages, using this machine as an example.

**Task**

The task of a modular system developer is to model the controller. The controller components are specified by means of interfaces and parameters in such a way as to ensure that no user interaction is necessary during configuration. In the process, it should be kept in mind that different variants may arise during configuration. Sensors and actuators can be added or dropped by selecting or deselecting optional components:

All of these cases should be kept in mind when modeling the controller, in order to ensure that the controller of a configured machine contains only the desired connection points and that all sensors and actuators are connected to their intended connection points. Attention should also be paid here to company-specific guidelines, for example, for addressing connection points, for specifying the sequence of controller components, or for reserving free connection points for future expansions (reserves).

**Procedure for functional configuration**

For functional configuration purposes, the controller components are modeled as mechatronic components. Unneeded controller components are deactivated via the disabler mechanism in line with the concept of maximization (see [Disabler](eecbase_k_variantmanagement_disabler.htm). Guidelines for assigning addresses and properties (e.g. connection type) to connection points are specified via parameters. The IO generator uses these parameters to calculate the addresses and connections. The IO generator addresses all connection points to controller components and also connects sensors and actuators to the components; this process is fully automated.
