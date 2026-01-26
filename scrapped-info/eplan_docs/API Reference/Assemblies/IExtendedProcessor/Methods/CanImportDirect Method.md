# CanImportDirect Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IExtendedProcessor~CanImportDirect.html

---

Indicates whether the converter can import external formats

Syntax

**C#**



bool CanImportDirect( 

   Context oContext,

   ref bool bSupportsProgress

)

bool CanImportDirect( 

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
