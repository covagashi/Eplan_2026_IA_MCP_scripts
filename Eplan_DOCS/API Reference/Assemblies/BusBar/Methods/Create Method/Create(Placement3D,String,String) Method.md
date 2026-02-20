# Create(Placement3D,String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBar~Create(Placement3D,String,String).html

---

Creates bended bus bar object.

Syntax

**C#**



public static BusBar Create( 

   Placement3D oParent,

   string strArticleNr,

   string strVariant

)

public:

static BusBar^ Create( 

   Placement3D^ oParent,

   String^ strArticleNr,

   String^ strVariant

)


#### Parameters

*oParent*
:   [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) object which will be parent of created bus bar.

*strArticleNr*
:   Part number of article used to create this object. Can't be null or have zero length.

*strVariant*
:   Part variant of article.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown if `strArticleNr` is invalid. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the bus bar cannot be created. |

Remarks

If given article in `strArticleNr` don't have property ARTICLE\_BENDINGRADIUS\_COPPER set or value is less or equal to 0, default value "5.0" will be used. If given article is `strArticleNr` don't have property ARTICLE\_MACRO set or macro is invalid exception will be thrown. If `strVariant` is null or have zero length default variant "1" is used. If `oParent` isn't a [CopperBundle](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.CopperBundle.html) new copper bundle will be created as parent of bus bar and then object passed as `oParent` will be set as parent to newly created copper bundle.
