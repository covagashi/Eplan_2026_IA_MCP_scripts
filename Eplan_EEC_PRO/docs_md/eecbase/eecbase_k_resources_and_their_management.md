---
title: "Resources and their management"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_resources_and_their_management.htm"
file: "eecbase_k_resources_and_their_management"
category: "eecbase"
---

# Resources and their management

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Resources and their management

Resources can be managed either externally in the file system or internally in the model.

The resource path validation displays the input of an invalid path in the editor as an error. Outside of editors (e.g., EOX Import), this is displayed as a warning.

To allow for an integrated versioning not only of the components, but also of the referenced resources, it is possible to manage (internalize) the resources also internally, i.e., in the model.

The state graph of the following graphic shows the states that a component can adopt with respect to the resource, and which changes are possible:

Assigning resources is not meaningful in the case of abstract components. Their state, therefore, is No resource.

A component can be assigned an external resource. In this state, the component is merely assigned a path to the external resource. Alternatively, it is also possible to save the resource in the model (Resource internal).

As illustrated in the graphic, it is possible to modify the state of a component in such a way that an external resource is converted to an internal resource (internalize) or an internal resource to an external resource (externalize).

Independently of this, a resource can be imported as new for an existing component (import). Both for internal and external resources, it is possible by analogy to export a resource to a file system.

Whether a resource must be managed internally or externally is defined separately for each discipline (except text discipline) using a model variable:

     * ECAD - [Manage Resources Internally](admin_r_modelvar_ecad_ressourcesinternalize.htm).
     * Media sources - [Manage Resources Internally](admin_r_modelvar_mediasources_resources.htm).
     * Office Word - [Manage Resources Internally](admin_r_modelvar_office_word_resources.htm).
     * PLC AutomationWorX - [Manage Resources Internally](admin_r_modelvar_plc_awx_resources.htm).
     * PLC CoDeSys - [Manage Resources Internally](admin_r_modelvar_plc_cds_resources.htm).
     * PLC STEP 7 - [Manage Resources Internally](admin_r_modelvar_plc_s7_resources.htm).

The appropriate differentiation must be selected for text disciplines on the Attributes page of a TextDisciplineConfiguration. The Manage Resources Internally check box has to be selected.

Existing external resources are imported into the model via the popup menu in library views using the action Internalize External Resources.

It is possible to internalize entire libraries or only individual files.

Internal resources of individual discipline components or of all discipline components below a unit or of all discipline components of a library can be exported to the resources folder of the corresponding discipline via File > Externalize Internal Resources. The externalized resources are then linked to the discipline components.

The storage location of a resource is specified on the Attributes editor page.

### Note

The consistent versioning of models requires that all external resources be internalized in the model.

If the resource of a discipline component has been changed externally, for example by an additional parameter, the data of the discipline components can be updated with data of the resources by means of the [Synchronize...] button. To this purpose the Synchronization view opens and lists the changed discipline components.
