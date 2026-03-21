---
title: "Image Folder"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_modelvar_p8imagefolder.htm"
file: "admin_r_modelvar_p8imagefolder"
category: "admin"
---

# Image Folder

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Image Folder

Path to model variable:

Disciplines > ECAD > Eplan Electric P8 > Folder

The path in which the initial search for P8 images is carried out is specified with the model variables Image Folder.

No default value is specified.

If a relative path is specified for the Image folder, the resulting absolute path is composed of the following settings:

    1. The specification for -Dde.eplan.eec.global.resourcePath= in the initialization file (e.g. ec.ini).
    2. The specification Image Folder in the model variables.

An absolute path specification for the image folder overrides the specifications in the initialization file and the settings.
