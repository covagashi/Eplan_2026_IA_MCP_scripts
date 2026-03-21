---
title: "Assigning window macros to ECAD objects"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_assignment_of_window_macro_to_ecad_object.htm"
file: "eececad_k_assignment_of_window_macro_to_ecad_object"
category: "eececad"
---

# Assigning window macros to ECAD objects

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Assigning window macros to ECAD objects

The window macro and ECAD object are linked in EEC. On the Attributes editor page of the ECAD object (e.g., Fragment), the link to the corresponding window macro is established by importing the macro file (resource storage location can be set via the settings). The storage location of the window macro must be stated.

The macro file (resource) is at first stored externally â in a folder that can be chosen freely. If necessary, the entire content of the macro file â after saving it first â can be internalized in the model via [Internalize]. This saves the entire content of the file to the database. The externally stored file can then be deleted. Only externally stored macros can be overwritten directly from within Eplan Electric P8 by overwriting a macro.

However, in this case there is no automatic synchronization of the external macro with the ECAD object in EEC. This synchronization must be triggered manually via the popup menu (Synchronize External Resources... .

By selecting a page or window macro, the variables defined in the placeholder object, as well as the sockets and plugs will be imported into EEC automatically as parameters of the ECAD object. These will be displayed on the Parameters editor page.

The variables from the placeholder object are created as a parameter of the String type; the Plug and Socket texts define their data type using the keywords Plug and / or Socket.

Assigning resources is not meaningful in the case of abstract components. Their state, therefore, is **No resource**.

If the resource of a component is stored externally, the component is merely assigned a path to the **external resource**. Alternatively, it is also possible to save the resource in the model, i.e., in the database, resp. in the EOX file (**Resource internal**).

As illustrated in the graphic, it is possible to modify the state of a component in such a way that an external resource is converted to an internal resource (Internalize) or an internal resource to an external resource (Externalize).

Independently of this, a resource can be imported as new for an existing component (import). Both for internal and external resources, it is possible by analogy to export a resource from the EEC to a file system.

Existing **external resources** are internalized via the popup menu in library views using the action Internalize External Resources:

It is possible to internalize entire libraries or only individual files.

The Attributes page of the components is represented in such a way that the three possible states of resources, and the respective actions that are possible, become transparent:

**Note:** In the event of versioning the **resources must be managed internally** so that EEC can ensure the consistency of the model.
