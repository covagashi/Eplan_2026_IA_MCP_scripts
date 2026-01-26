# CopyTo Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~CopyTo.html

---

Copies property value to destination including all indexes. If source property is indexed destination has to be also indexed. Only indexes from 1 to minimum of both MaxIndex are copied.

Syntax

**C#**



public void CopyTo( 

   PropertyValue destination

)

public:

void CopyTo( 

   PropertyValue^ destination

)


#### Parameters

*destination*

Exceptions

| Exception | Description |
| --- | --- |
| [NotIndexedPropertyException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NotIndexedPropertyException.html) | Throws when source is indexed and destination isn't indexed property or has static value. |
| [IndexedPropertyException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IndexedPropertyException.html) | Throws when source isn't indexed property and destination is indexed. |
| [PropertyTypesMismachException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyTypesMismachException.html) | Throws when source and destination are non-static values and are different types. |

Example

**C#**

```
PropertyValue oProperty = m_oTestProject.Pages[0].Functions[0].Properties[ FUNC_NON_INDEXED_PROPERTY ];

PropertyValue static_value = "xxx";

static_value.CopyTo ( oProperty ) ; // FUNC_NON_INDEXED_PROPERTY will be changed

PropertyValue oP1 = m_oTestProject.Pages[0].Functions[0].Properties[ FUNC_INDEXED_PROPERTY_1 ];

PropertyValue oP2 = m_oTestProject.Pages[0].Functions[0].Properties[ FUNC_INDEXED_PROPERTY_2 ];

// Let say that oP1.Definition.MaxIndex == 100 and oP2.Definition.MaxIndex == 50

oP1.CopyTo ( oP2 ); // all non-empty indexes from 1 to 50 will be copied

UniversalPropertyList ^ UPL = new UniversalPropertyList ( );

PropertyValue up = UPL [ AnyPropertyId ( FUNC_INDEXED_PROPERTY_1 ) ];

oP1.CopyTo ( up );
```
