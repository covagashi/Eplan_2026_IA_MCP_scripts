# Id Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Id.html

---

Returns the P8 property descriptor (id and index) that the object points to. To use the Id property, the PropertyValue object must point to a project property (persistent property). Transient PropertyValue objects don't have descriptors because they point directly to a value. A transient PropertyValue is created by operator and takes values of base types.

Syntax

**C#**



public AnyPropertyId Id {get;}

public:

property AnyPropertyId^ Id {

   AnyPropertyId^ get();

}


Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown when object is in transient mode (in other words, when the object is not pointed to a PropertyList). |

Example

**C#**

```


Function function = page.Functions[0]; // A valid Function object

PropertyValue propertyValue1 = "123"; // Transient object

PropertyValue propertyValue2 = 12; // Also transient object

PropertyValue propertyValue3 = function.Properties.FUNC_ARTICLE_PARTNR;

AnyPropertyId propertyId3 = new AnyPropertyId (myProject.Project, "20100");

Assert.AreEqual(propertyValue3.Id.AsInt, propertyId3.AsInt);

Assert.AreEqual(propertyValue3.Id.Index, 0); // In this case, where the index was not specified, PropertyValue3.Id.Index is 0.

PropertyValue propertyValue4 = function.Properties.FUNC_ARTICLE_PARTNR[12];

AnyPropertyId propertyId4 = new AnyPropertyId (myProject.Project, "20100");

propertyId4.Index = 12;

int propertyId = propertyValue4.Id.AsInt;

int propertyIndex = propertyValue4.Id.Index;

Assert.AreEqual(propertyValue4.Id.AsInt, propertyId4.AsInt);

```
