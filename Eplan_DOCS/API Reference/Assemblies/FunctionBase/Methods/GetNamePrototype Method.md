# GetNamePrototype Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase~GetNamePrototype.html

---

Sets properties which are used for building name of object.

Syntax

**C#**



public bool GetNamePrototype( 

   ICollection<AnyPropertyId> pIdentifying,

   ICollection<AnyPropertyId> pDescribing

)

public:

bool GetNamePrototype( 

   ICollection<AnyPropertyId^>^ pIdentifying,

   ICollection<AnyPropertyId^>^ pDescribing

)


#### Parameters

*pIdentifying*
:   List for properties which are used to indetify the device. Collection can't be read-only.

*pDescribing*
:   List for properties which is not used to identify the device but only has a descriptive purpose. Collection can't be read-only.

#### Return Value

True, if any identifing property has been found.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when parameter is `null`. |

Remarks

Method removes all elements from given collections and fills them with ids.
