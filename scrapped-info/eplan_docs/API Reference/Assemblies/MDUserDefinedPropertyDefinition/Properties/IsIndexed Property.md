# IsIndexed Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDUserDefinedPropertyDefinition~IsIndexed.html

---

Checks if given property is indexed.

Syntax

**C#**



public override bool IsIndexed {get;}

public:

property bool IsIndexed {

   bool get() override;

}


#### Property Value

true : Property is indexed

false : Property is not indexed

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when IsIndexed property is called on MDPropertyDefinition object with invalid property Id. |

Remarks

Should be called only on MDPropertyDefiniton objects with valid Id.

Example

**C#**

```
MDPart oPart  = m_MDPartsDatabase.Parts[0]; //a valid part object

//a valid call

bool bIndexed = oPart.Properties[Eplan.EplApi.MasterData.Properties.MDPartsDatabaseItem.ARTICLE_ADDITIONALTEXT].Definition.IsIndexed;
```
