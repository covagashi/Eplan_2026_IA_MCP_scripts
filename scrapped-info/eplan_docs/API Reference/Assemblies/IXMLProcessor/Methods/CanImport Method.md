# CanImport Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IXMLProcessor~CanImport.html

---

Indicates whether the converter can convert external formats to XML.

Syntax

**C#**



bool CanImport( 

   Context oContext,

   ref bool bSupportsProgress

)

bool CanImport( 

   Context^ oContext,

   bool% bSupportsProgress

)


#### Parameters

*oContext*
:   Context with parameters

*bSupportsProgress*
:   Indicates whether the converter supports a progress bar.

#### Return Value

true: conversion is possible; false: conversion is not possible
