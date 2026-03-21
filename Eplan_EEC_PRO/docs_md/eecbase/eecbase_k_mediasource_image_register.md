---
title: "Image register and image-register extension"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_mediasource_image_register.htm"
file: "eecbase_k_mediasource_image_register"
category: "eecbase"
---

# Image register and image-register extension

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Image register and image-register extension

The new MediaSource system library allows the flexible referencing of images through the image register.

The image register is the assignment of components to an image object each for the library component and the project component (see the following figure). This property is implemented in all places where objects are given a graphical representation. The assignment for an image object of the project components is optional. If no image object is specified, the register uses the same image objects for library and project components.

An example of the usage of image registers is the placing of objects in diagrams. By assigning the object class to a certain image (and the configuration of the diagram in order to use the image register), all elements of the same type can be assigned to a uniform image. This assignment can also be modified centrally in the image register, which then applies to all diagrams that use this image register.

In order to access the assignment table of an image register, several methods have been added to the formula language. Like image objects, the image register, too, offers the methods "image" and "disabledImage". But while a parameter is not needed for an image object, a key object must be specified for the image register. Then, the register searches the assignment table for an entry for the class of the key object and / or the key object itself, if it is already a class object. If the register does not find an assignment, it will look for one for the supertype of the class. This will be repeated until no further supertype is available or an image has been found. If no image is found for the top supertype either, the method will return <<null>>.

If an assignment is found, the register will distinguish between two cases: the key object originates from the class level, or it comes from the instance level. If the former is true, the register loads the image of the assigned image object for the class level. If the key object comes from the instance level, the register will check whether the assignment found provides an image for the project component. If this is true, the image of the image object assigned there will be loaded. Otherwise, the image object of the library component will be used.

Problem:

Since the image registers lie in libraries, it is possible with more complex models that a change to an image register is not possible, not desired or not useful. Possibly individual images cannot be assigned unambiguously, which would render a central image register impossible. If this affects only part of the images, the constant component of the images assigned would have to be entered and managed several times.

Solution:

Using image register extensions, it is possible to extend the assignment table of registers dynamically (see the following figure).

To extend a register, create a new image register extension. The extension allows for the same assignment of classes to image objects as the image register. The register to be extended is selected in the editor for the extension. This way, all entries in the assignment table of the register extension are assigned to those of the register. The extension becomes noticeable in the evaluation of an image request for a class.

Now, the evaluation does not merely search the image register, but checks the assignment tables of the register extensions first. If the search of extensions finds an image, that image will be used. If none of the extensions defines an image, the search is run on the image register itself. This order creates the possibility of overwriting the assignments of the image register by means of extensions.

This functionality lies fully within the image register. Even when register extensions are used, all requests are directed to the register. The image register searches for existing extensions automatically. A further distinction in the formulas is not necessary.

With more complex models, it may happen that a register is extended by several register extensions. These extensions may be located in different libraries. If a project is searched for an assignment, the register must not search each individual extension. The project may possibly not import every library that contains an extension for the register. From the point of view of the project, therefore, the request must be handled as if the non-visible extensions did not exist.

The key object serves as orientation for the register in this context. The register checks which libraries are visible from the key object. All extensions that are in libraries outside of this view will be ignored for the request.

Depending on the origin of the key object, the view becomes too limited. If the key object comes from a modular system library, register extensions will not be visible from the project library. In such cases, an extended image and / or disabledImage method can be used. This will adopt two parameters. The first parameter is a "context object"; the second parameter, the already known key object. If the key originates in an imported library, a context object can be transferred to determine the extensions in visible libraries.

Special case:

If there are several extensions eligible for assignment in the search of extensions, the import order in the context library / context project is used. If two extensions are located in the same library and define different images for the same object, the entry used will be selected randomly. The extensions in the library are stored in the data model in an unsorted order. Such an unclear assignment does not trigger an error in the model validation, but may cause behavior that is not immediately comprehensible in terms of the runtime.

Create a new image register:

To insert a new image register in the library, select New > Media sources > Image register in the popup menu.

The new image register is created without data at first. On the Image assignment page of the editor (see the following figure), the user selects for an object type (1) the images for the library component (2) and the project component (3):

Re-create the image register extension:

An image register can be extended with an image register extension. To implement a new image register extension, select New > Media sources > Image register extension in the popup menu.

On the Attributes page, select the image register to be extended:

On the Image assignment page, the user then selects for an object type (1) the images for the library component (2) and the project component (3).
