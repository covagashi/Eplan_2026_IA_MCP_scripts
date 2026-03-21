---
title: "Unused objects search"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_model_navigation_search_unusedobjectssearch.htm"
file: "eecbase_k_model_navigation_search_unusedobjectssearch"
category: "eecbase"
---

# Unused objects search

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Unused objects search

It is a specific requirement for modular system developers to identify objects that cannot be installed in the model on the basis of the mechatronic level configuration and pre-instantiated components and extension points. Projects and instances contained in the model are not captured by the search. When a component is identified as installable, its supertypes, parameters and interfaces implemented by it will also be identified as installable.

### Note

Note that this is only about the possibility of installing a component, rather than whether or not it is actually installed.

The present model can be searched only if it is valid, as invalid models lack important connections, which causes objects to be recognized, falsely, as not being usable. This is why the model is validated first prior to a search. If validation finds an error, the search process is terminated. This does not include warnings about missing resources.

The search starts with the mechatronic components of the top level, as these can generally be installed. Then, the extension points and pre-instantiated components are parsed.

Objects that use each other, without one of them being determined to be mountable, are deemed unused objects.

Furthermore, the search excludes objects

     * that have class methods that were not defined in system libraries;
     * that are created as abstract components, but do not contain their own or inherited class methods, nor any specific and used subtypes, and that are not used for type limitation in connection with extension points.

The search for unused objects includes parameters, interfaces, mechatronic components and discipline components.

The search can be canceled at any time, however, no partial result will be displayed in this case.

The result is displayed in a table. All of the objects contained in it can be opened by double-clicking or using the Open popup menu entry. Marked objects are deleted from the result list and the model via the [Del] key or the popup menu entry Remove Selected Match. All of the matches are removed from the result list and the model with the Remove All Matches popup menu entry.

In the Installed column, the display shows whether an unused parameter is installed or not, with Yes and No.

Example table:

Name | Absolute name | Installed | Comment  
---|---|---|---  
separateParameter | T_ECAD_P8.ECAD.Parameter | No | non-installed and unused parameter  
installedParameter | T_ECAD_P8.ECAD.Parameter | Yes | installed but unused parameter  
  
Double-clicking the name of a parameter opens it in the editor.
