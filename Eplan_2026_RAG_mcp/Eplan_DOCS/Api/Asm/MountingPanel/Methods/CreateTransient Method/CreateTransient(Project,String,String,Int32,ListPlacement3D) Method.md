# CreateTransient(Project,String,String,Int32,List<Placement3D>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic490.html

---

Creates transient not placed MountingPanel based on article which contain macro.

Syntax

**C#**



public void CreateTransient( 

   Project oProject,

   string strPartNr,

   string strVariant,

   int nMacroVariant,

   List<Placement3D> listOfAdditionalPlacements

)

public:

void CreateTransient( 

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

This method can create mounting panel only from part which has an assign macro and this macro contains a 3d object with function definition of mounting panel. If no macro is available or macro doesn't contain applicable 3d object then exception is thrown.

Example

**C#**

```
//Data for creating the Mounting Panel

List<Placement3D> listAdditionalPlacements = new List<Placement3D>();

String strPartNr = "MP_With_Variants";

String strPartVariantNr = "1";          //First part variant

int nMacroVariant = 1;                  //Variant B

//Creating Mounting Panel

MountingPanel oMountingPanel = new MountingPanel();

oMountingPanel.CreateTransient(m_oTestProject, strPartNr, strPartVariantNr, nMacroVariant, listAdditionalPlacements);

//Placing Mounting Panel

oMountingPanel.SetParent(oInstallationSpace, true);

```
