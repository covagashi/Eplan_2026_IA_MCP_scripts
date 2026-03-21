---
title: "Development steps of the modular system development"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_modularsystemvariations.htm"
file: "concept_k_modularsystemvariations"
category: "concept"
---

# Development steps of the modular system development

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Development steps of the modular system development

The complexity of a modular systems depends on the requirements of the machine or plant to be modeled and the documents to be created of the respective discipline.

In the following section possible development steps are displayed by means of a very simple model. Each development step is based on a possible requirement:

### [Initial model with few mechatronic components](javascript:void\(0\);)

A modular system with few mechatronic components can serve as the initial model.

  * The modular system imports the system library Engineering which contains all super classes in order to derive the objects for mechatronics from this.
  * The mechatronic components are derived from MechatronicComponent and can be freely nested within each other.
  * The mechatronic components contain few parameters.
  * The parameters save texts (strings) and numbers (integer).



### [Example](javascript:void\(0\);)

The following figure shows a modular system with mechatronic components for a machine and three mechatronic components of a power supply. The mechatronic components of the power supply all contain the same parameters but with different values apart from the value for the DocumentKind parameter.

### [Inheriting the same properties](javascript:void\(0\);)

The initial model contains multiple mechatronic components with mainly the same properties (parameters).

Requirement:

Identical properties of similar mechatronic components should not have to be created again for each individual mechatronic component. The identical properties should also only have to be changed at a central location.

Solution:

  * A new mechatronic component is created that has all shared properties.
  * The similar mechatronic components are not derived from MechatronicComponent anymore but from the new mechatronic component and therefore inherit their properties.



### [Example](javascript:void\(0\);)

The following interactive figure shows the modular system before and after the conversion. After the conversion the derived mechatronic components inherit all parameters and also the parameter value EFS1 (displayed in green). If one these parameter names or the value EFS1 were to change in the component PowerSupply, these changes are inherited to all other derived components.

  *   * 

  * 1
  * 2



### [Adding discipline components](javascript:void\(0\);)

The model contains multiple mechatronic but no discipline components yet.

  * A schematic that has already been created with Eplan Electric P8 exists.
  * The schematic pages of the power supply already exist as page macros.
  * The Eplan Electric P8 project already exists as a basic project template.



Requirement:

Discipline components are to be created for the power supply of the machine with which a schematic can be created.

Solution:

  * The symbol library of a discipline (for example ECAD) is to be imported into the modular system library.
  * A new discipline component is created that is derived from WiringDiagram and contains the basic project as a resource.
  * Discipline components are created that are derived from Page and that contain the page macros as resources.
  * The discipline components are installed directly in the existing mechatronic components.



### [Example](javascript:void\(0\);)

The following interactive figure shows the modular system before and after the conversion. After the conversion the modular system contains four discipline components that are directly installed in the corresponding mechatronic components.

  *   * 

  * 1
  * 2



### [Switching on/switching off components](javascript:void\(0\);)

The model contains multiple mechatronic and discipline components.

Requirement:

Two variants are to exist for the power supply of the machine.

Variant 1 contains three pages:

  * PS_400V_230VAC
  * PS_24VDC_PLC
  * PS_24VDC_Devices



Variant 2 contains two pages:

  * PS_400V_230VAC
  * PS_24VDC_Devices



Solution:

  * A Boolean parameter is created.
  * The new parameter is installed in the superior component.
  * A disabler is set up for the installed mechatronic component. This means a formula is inserted in the field for Disabled that determines the value of the Boolean parameter in the superior component. The installed mechatronic component is activated/deactivated depending on the parameter value.



### [Example](javascript:void\(0\);)

The following interactive figure shows the modular system before and after the conversion. After the conversion the mechatronic component Machine contains the Boolean parameter withoutPLC. The mechatronic component PowerSupply_24VDC_PLC contains this formula in the Disabler field: =mc.$withoutPLC (The formula navigates with mc to the superior component, here Machine, and in it determines the value of the parameter withoutPLC by means of $withoutPLC).

This function is only effective in a configuration (a project)!

  *   * 

  * 1
  * 2



### [Installing additional components](javascript:void\(0\);)

The model contains multiple mechatronic and discipline components. A part of the components that always occur in the same configuration are directly installed in each other.

Requirement:

During the configuration a page of the power supply is be installed, if required.

Solution:

  * A Placeholder is installed instead of a specific mechatronic component.
  * By means of specifications for the Type and Number you can control which component can be installed at it and how many of them.
  * The specific mechatronic component can be installed at the placeholder during the configuration. This can be carried out via Drag & Drop, a user interface (Form-UI) or an action.



### [Example](javascript:void\(0\);)

The following interactive figure shows the modular system before and after the conversion. After the conversion the modular system contains three mechatronic components, of which only two are directly installed. In addition a placeholder is now available on which exactly one component (Multiplicity=0..1) of the type PowerSupply_24VDC_PLC can be installed during the configuration.

  *   * 

  * 1
  * 2
