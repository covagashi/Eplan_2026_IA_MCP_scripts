---
title: "Object model"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_object_model.htm"
file: "refformulas_r_object_model"
category: "refformulas"
---

# Object model

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Object model The object model is shown in the Classification view. The object model differentiates between the following types of objects:  
     * **Components** are divided into **discipline components** and **mechatronic components**. Discipline components are assigned to a discipline (e.g. ECAD). Mechatronic components may contain, compared to discipline components, further discipline or mechatronic components. Reusable components, stored in a library, are library components. Project components are the result of library components, which are used in a project (this procedure is called instantiation). Each project component is assigned to exactly one library component.
     * **Basic types** are **String** (character string), **Boolean** (), **Integer** and **Double** (floating point number).
     * **Collections** are collections of objects, which means they may contain components, basic types and collections.
