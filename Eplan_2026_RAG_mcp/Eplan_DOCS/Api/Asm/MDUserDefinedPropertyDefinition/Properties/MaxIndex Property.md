# MaxIndex Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDUserDefinedPropertyDefinition~MaxIndex.html

---

Allows to check maximal index value of given property.

Syntax

**C#**



public override int MaxIndex {get;}

public:

property int MaxIndex {

   int get() override;

}


#### Property Value

Maximal index of given property.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when MaxIndex property is called on MDPropertyDefinition object with invalid property Id. |

Remarks

Should be called only on MDPropertyDefiniton objects with valid Id.

Example

**C#**

```
MDPart oPart = m_MDPartsDatabase.Parts[0]; //a valid part object

//a valid call

int iMaxIndex = oPart.Properties[Eplan.EplApi.MasterData.Properties.MDPartsDatabaseItem.ARTICLE_ADDITIONALTEXT].Definition.MaxIndex;
```
