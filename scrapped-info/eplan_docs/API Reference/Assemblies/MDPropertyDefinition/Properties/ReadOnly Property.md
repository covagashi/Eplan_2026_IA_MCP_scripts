# ReadOnly Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyDefinition~ReadOnly.html

---

Check if a given property is read-only.

Syntax

**C#**



public virtual bool ReadOnly {get;}

public:

virtual property bool ReadOnly {

   bool get();

}


#### Property Value

true : Property is read-only

false : Property is not read-only

Remarks

Should be called only on MDPropertyDefiniton objects with valid Id.

Example

**C#**

```
MDPart oPart = m_MDPartsDatabase.Parts[0];//a valid part object

//a valid call

bool bReadOnly = oPart.Properties.ARTICLE_HEIGHT.Definition.ReadOnly;
```
