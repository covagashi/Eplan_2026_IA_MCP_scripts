# PropertyDefinition.PropertyType

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition+PropertyType.html

---

Types of stored values

Syntax

**C#**



public enum PropertyDefinition.PropertyType : System.Enum

public enum class PropertyDefinition.PropertyType : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **Bool** | 1 | Boolean type, contains true or false |
| **Coord** | 16 | Double value |
| **Double** | 6 | Longer floating point value |
| **Long** | 4 | Long numeric value |
| **MultilangString** | 15 | Multi language string [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html) |
| **Point** | 13 | Point |
| **String** | 7 | Unicode-String |
| **Time** | 14 | Time value |
| **ValueWithUnit** | 26 | Value with unit |

Example

When setting properties of type Double as string, e.g.

**C#**

```
oConnection.Properties[DataModel.Properties.Connection.CONNECTION_WIRECROSSSECTION] = "2.5";

//... the current culture is not considered. You always have to

//us a '.' as decimal separator.
```

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.DataModel.PropertyDefinition.PropertyType**
