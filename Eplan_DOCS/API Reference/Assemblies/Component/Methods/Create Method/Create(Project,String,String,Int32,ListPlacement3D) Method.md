# Create(Project,String,String,Int32,List<Placement3D>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Component~Create(Project,String,String,Int32,List{Placement3D}).html

---

Creates not placed Component object from part with given variant of macro.

Syntax

**C#**



public static Component Create( 

   Project oProject,

   string strArticleNr,

   string strVariant,

   int nMacroFromArticleVariant,

   List<Placement3D> listOfAdditionalObjects

)

public:

static Component^ Create( 

   Project^ oProject,

   String^ strArticleNr,

   String^ strVariant,

   int nMacroFromArticleVariant,

   List<Placement3D^>^ listOfAdditionalObjects

)


#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*strArticleNr*
:   Part number of article used to create this object. Can't be null or have zero length.

*strVariant*
:   Part variant of article.

*nMacroFromArticleVariant*
:   Variant number of macro which is used to create mesh of object.

*listOfAdditionalObjects*
:   list, that will be filled by additional created objects. may be null

#### Return Value

The created Component.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [System.ArgumentException](#) | Thrown if `strArticleNr` has zero length. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the component cannot be created. |

Remarks

If strArticleVariant null or have zero length default part variant "1" is used.

Variant number of macro is used only if it is defined for the part used to create object. Numeration of variants start from `0` which corresponds to the variant `A`, `1` is for variant `B`, ... . It is possible to pass also value `-2` which forces the function to take first variant defined for the macro. Note that only variants for representation type `ArticlePlacement3D` are taken into account. If macro is defined for part but it does not contain a given variant then object will not be created.
