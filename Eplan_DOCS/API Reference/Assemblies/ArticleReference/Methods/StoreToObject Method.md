# StoreToObject Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~StoreToObject.html

---

Commits all changes of the ArticleReference to the matching properties of a parent object (Project/Function/Connection).

Syntax

**C#**



public void StoreToObject()

public:

void StoreToObject();


Exceptions

| Exception | Description |
| --- | --- |
| [FixedDeviceException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FixedDeviceException.html) | Thrown if device of the Object is fixed. |

Remarks

When values of properties of the ArticleReferencePropertyList are changed, these changes do not appear in GUI immediately. You need to store the changes of ArticleReference object. After calling this method get corresponding ArticleReference object from the parent object again, in order to read up-to-date values of changed properties (or use this ArticleReference object for writing again). Property values may have been changed on parent object, because some part reference properties are taken from the part if they are set to empty on the reference.
