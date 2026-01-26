# Create(Group,AnyPropertyId) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement~Create(Group,AnyPropertyId).html

---

Creates and inserts it into a group ContextPropertyPlacement which displays symbol properties.

Syntax

**C#**



public static ContextPropertyPlacement Create( 

   Group group,

   AnyPropertyId propertyId

)

public:

static ContextPropertyPlacement^ Create( 

   Group^ group,

   AnyPropertyId^ propertyId

)


#### Parameters

*group*
:   Group on which object will be inserted.

*propertyId*
:   Property of the object that belongs to the group which will be displayed.

#### Return Value

the newly created ContextPropertyPlacement.

Example

**C#**

```
MDSymbolVariant variant = symbol.Variants[0];

ContextPropertyPlacement cpp = ContextPropertyPlacement.Create(variant.AsGroup, Properties.Function.FUNC_DEVICETAG_FULLNAME);
```
