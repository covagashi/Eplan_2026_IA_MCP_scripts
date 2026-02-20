# Create(Project,String,String,Int32,List<Placement3D>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Cabinet~Create(Project,String,String,Int32,List{Placement3D}).html

---

Creates not placed Cabinet based on article which contain macro.

Syntax

**C#**



public void Create( 

   Project oProject,

   string strPartNr,

   string strVariant,

   int nMacroVariant,

   List<Placement3D> listOfAdditionalPlacements

)

public:

void Create( 

   Project^ oProject,

   String^ strPartNr,

   String^ strVariant,

   int nMacroVariant,

   List<Placement3D^>^ listOfAdditionalPlacements

)


#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*strPartNr*
:   Part number of article used to create this object. Can't be null or have zero length.

*strVariant*
:   Part variant of article. If `null` or `empty` first variant is used.

*nMacroVariant*
:   Variant of macro which will be used for creating the object.

*listOfAdditionalPlacements*
:   Additionally created objects are stored in this list. If not `null` will be cleared.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when required param is `null` value. Check exception message for more info. |
| [System.ArgumentException](#) | Thrown when one of params is invalid. Check exception message for more info. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when object can't be created. Check exception message for more info. |
| [Eplan.EplApi.DataModel.MacroMissingException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroMissingException.html) | Thrown when macro file is missing or is invalid. Check exception message for more info. |
| [Eplan.EplApi.DataModel.MacroVariantNotFoundException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroVariantNotFoundException.html) | Thrown when macro doesn't contain requested variant. Check exception message for more info. |

Remarks

This method can create a cabinet only from a part which has an assign macro. If no macro is available then exception is thrown.

Example

**C#**

```
//Data for creating the cabinet

List<Placement3D> listAdditionalPlacements = new List<Placement3D>();

String strPartNr = "Cabinet_With_Variants";

String strPartVariantNr = "1";          //First part variant

int nMacroVariant = 1;                  //Variant B

//Creating cabinet

Cabinet oCabinet = new Cabinet();

oCabinet.Create(m_oTestProject, strPartNr, strPartVariantNr, nMacroVariant, listAdditionalPlacements);

//Placing cabinet

oCabinet.SetParent(oInstallationSpace, true);

```
