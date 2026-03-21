---
title: "Development of virtual mechatronic components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_development_of_virtual_mechatronic_components.htm"
file: "concept_k_development_of_virtual_mechatronic_components"
category: "concept"
---

# Development of virtual mechatronic components

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Development of virtual mechatronic components

The functional configuration approach requires a functional component not only to contain information from individual disciplines, but also to describe interdisciplinary relationships.

The following diagram uses the example of a functional component for a clamp to illustrate how pieces of information are distributed and how they interact.

The clamp component consists of paths for the schematics diagram, a universally valid function block for connected axes and a dual-position monitor. Pieces of information are provided here in the form of names or parameters.

The parameters are each assigned values based on the functional component. In this way it is determined, for example, if a cam switch is available or what dimensions a contactor should be given. To avoid having to enter the corresponding value for each clamping unit or its superordinate unit, the values can be derived. This means that individual values can be handed down to components or passed through them. In this way, many parameters can obtain their values from already parameterized components or calculate their own values based on the values obtained. An additional possibility is the use of initial values. This involves introducing and applying automatically predefined values, for example, for a very frequently installed variant of a clamp fixture.

The principle of deriving from parameter values is illustrated in the following diagram:

Functional mechatronic components must be adjustable via mechatronic parameters so that they can be used in different areas of application. Subcomponents, in turn, have parameters that either can already be specified when the mechatronic components are being developed or can be derived from mechatronic parameters. Aspects of the clamping function that must be adjustable if the component is to be reused flexibly include, for example, the motor being used, the IO addresses and the release condition.

The internal pre-wiring in virtual mechatronical components reduces the multitude of parameters that today must be adjusted in various tools to just a few parameters. Internal pre-wiring ensures, for example, that IO addresses are always consistent in the schematics diagram and the PLC software.

Parameter values are derived via formulas similarly to how data is transferred between cells in MS Excel tables. The formula mc. $ArticleNo_Motor directly assigns the value of the mechatronical parameter ArticleNo_Motor as the value of the parameter of a subcomponent. Furthermore, formulas can also be used to formulate all sorts of calculations, if-then conditions, etc.

A very powerful possibility for modeling variants is presented by the enabler concept: The EEC assigns each component a boolean enable parameter, for which a formula can be defined that decides whether or not the component is to be used in a specific configuration. In the case of the clamping function, for example, the Boolean âWS_monitoringâ parameter can help decide whether to use one or two sensors when determining the âclampedâ condition. This concept makes a major contribution towards minimizing the number of modular system components and, by extension, the amount of administrative effort required for the modular systems.
