# MDPropertyDefinition.MDPropertyType

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyDefinition+MDPropertyType.html

---

Types of stored values

Syntax

**C#**



public enum MDPropertyDefinition.MDPropertyType : System.Enum

public enum class MDPropertyDefinition.MDPropertyType : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **Bool** | 1 | Boolean type contain true or false |
| **Double** | 6 | Floating type value |
| **Long** | 4 | Long numeric value |
| **MultilangString** | 15 | Multi language string [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html) |
| **Point** | 13 | Point |
| **String** | 7 | Unicode-String |
| **Time** | 14 | Time value |
| **Undefined** | 0 | Type not defined |
| **ValueWithUnit** | 26 | Value with unit |

Example

When setting properties of type Double as string, e.g.

**C#**

```
MDPart oPart = m_MDPartsDatabase.Parts[0];

oPart.Properties[Eplan.EplApi.MasterData.Properties.MDPartsDatabaseItem.ARTICLE_HEIGHT] = "2.5";

//... the current culture is not considered. You always have to

//us a '.' as decimal separator.
```

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.MasterData.MDPropertyDefinition.MDPropertyType**
