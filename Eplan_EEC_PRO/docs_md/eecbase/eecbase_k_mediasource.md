---
title: "Media sources"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_mediasource.htm"
file: "eecbase_k_mediasource"
category: "eecbase"
---

# Media sources

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Media sources

The system library MediaSource allows for the internalization of media data in a model, which makes references to externally stored media data unnecessary. Due to the internalization of media data, it is no longer necessary to pass them on additionally to an EOX file and / or to back them up.

Currently, these media formats (image formats) are supported: JPG, GIF (not animated), PNG, BMP, and ICO.

The resource folder for media sources can be specified in the settings (see the following image). If stated as a relative path, relative to the installation folder of EEC or to the value of the variable, the resource folder is de.eplan.eec.global.resourcePath (see [Java Virtual Machine Arguments (VMArgs)]()). As well, an absolute path to another resource folder can be used.

With the model variable Disciplines > Media sources > Store resources), you can specify globally whether new media source resources are to be internalized directly. By default newly added resources are not stored (see [Manage Resources Internally](admin_r_modelvar_mediasources_resources.htm)).

Images (Image), image registers (Image register), and image register extensions (Image register extension) can be created in a library.

In analogy to other source files, image objects can be created via mass import.
