# Synchronize.StoreMode

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize+StoreMode.html

---

Store mode determines, whether parts, which are already existing in the parts database, should be modified.

Syntax

**C#**



public enum Synchronize.StoreMode : System.Enum

public enum class Synchronize.StoreMode : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **AppendNew** | 0 | append new articles |
| **OverwriteExisting** | 1 | overwrite existing articles (including variants) |
| **OverwriteExistingAndAppendNew** | 2 | overwrite existing articles (including variants) and append new ones |

Remarks

Default value is `AppendNew`. When the article is being removed, all its variants are also removed.

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.HEServices.Synchronize.StoreMode**
