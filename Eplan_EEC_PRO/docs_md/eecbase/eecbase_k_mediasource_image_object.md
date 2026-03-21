---
title: "Image objects"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_mediasource_image_object.htm"
file: "eecbase_k_mediasource_image_object"
category: "eecbase"
---

# Image objects

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Image objects

The MediaSource library allows the creation of image objects. A MediaSource image object manages an image and enables the internalization of the image in the model. This neutralizes the reference to objects in the file system, and the backing up, restoration and replacement of models are simplified. The MediaSource image object is upstream from the actual image and enables uniform usage in EEC in analogy to other model objects. To access the image thus stored, the image object has a preview page in the editor, as well as two methods for the formula language (see [Image object methods](refformulas_r_image_objects_methods.htm) and [Image register methodss](refformulas_r_image_register_methods.htm)).

The imported and/or referenced image is loaded from the image object using the image method. An inactive image can be represented using the method disabledImage. This way, the image is changed in color prior to loading. By converting the colors to grayscale, the graphical effect is one of an inactive button. The imported image itself is not modified by these changes in color and contrast.

To insert a new image in the library, select New > Media sources > Image in the context menu.

If the model variable MediaSources â Manage Resources has the value false:

On the Attributes page of the editor for the image (see figure above), use [Import], or in the Resource path field [..] to (1) create a reference to the external resource at first. Then use the Internalize button (2) to internalize the image in the library (also see [Resources and their management](eecbase_k_resources_and_their_management.htm)).

If the model variable MediaSources â Internalize Resources has the value true:

On the Attributes page of the editor for the image, use [Import], or in the Resource path field, [...] to internalize the image directly in the library.

An internalized image can be converted to a reference to an external file by way of [Externalize]. Use [Internalize] to convert a reference to an external image to an internalized image.

An internalized image can be viewed on the Preview page of the editor.
