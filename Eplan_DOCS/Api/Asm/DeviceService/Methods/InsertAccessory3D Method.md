# InsertAccessory3D Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~InsertAccessory3D.html

---

Creates and inserts accessories of a placement.

Syntax

**C#**



public bool InsertAccessory3D( 

   Placement3D pMainPlacement,

   string strPartNumber,

   string strPartVariant,

   string strAccessoryPlacement,

   string strInstallationVariant,

   bool bTransient,

   ICollection<Placement3D> colCreatePlacements

)

public:

bool InsertAccessory3D( 

   Placement3D^ pMainPlacement,

   String^ strPartNumber,

   String^ strPartVariant,

   String^ strAccessoryPlacement,

   String^ strInstallationVariant,

   bool bTransient,

   ICollection<Placement3D^>^ colCreatePlacements

)


#### Parameters

*pMainPlacement*
:   Placement which will be the parent of the new object. Can't be `null`.

*strPartNumber*
:   Accessory part number. Can't be `null`.

*strPartVariant*
:   Accessory part variant. Can't be `null`.

*strAccessoryPlacement*
:   Accessory placement name. First one found will be used. Can't be `null`.

*strInstallationVariant*
:   Accessory installation name which will used for placing. Can't be `null`.

*bTransient*
:   Determins if created object will be transient.

*colCreatePlacements*
:   Collection which will be filled with created objects. Can be `null`.

#### Return Value

`True` if accessory has been placed automatically.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | NULL was passed as a needed parameter. |
| [System.ArgumentException](#) | Invalid or empty parameter passed. |
| [System.ApplicationException](#) | The internal interface could not be created. |
| [Eplan.EplApi.HEServices.Exceptions.HEServicesBase](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Exceptions.HEServicesBase.html) | Creation of accessory failed. Please check if accessory placement is assigned to the article or the installation variant is valid. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred while performing the action. Please refer to the exception message. |

Remarks

Accessories are placed automatically, which means that their transformation have been calculated and set, only if it results from the information contained in the accessory placement. The device tag will be set automatically on the inserted accessory. In other case accessories transformation must be calculated and set manually.  
  
If an evaluation of the full names for all placed functions is required, after insertion of 3D acessories, it is recommended to call the EvaluateAndSetAllNames() method of the [NameService3D](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService3D.html) class.

Example

The following examples shows how to insert a 3d accessory.

**C#**

```
//get 3d function from selection

SelectionSet oSelectionSet = new SelectionSet();

Function3D oMainFunction = oSelectionSet.Selection[0] as Function3D;

//set accessory data

String strPartNumber = "SE.GV3A01";

String strPartVariant = "1";

//set accessory placement data

String strAccessoryPlacement = "SE.GV";

String strInstallationVariant = "Top";

//insert accessory

List<Placement3D> listCreatedPlacements = new List<Placement3D>();

bool bPlacedAutomatically = new DeviceService().InsertAccessory3D(

        oMainFunction,

        strPartNumber,

        strPartVariant,

        strAccessoryPlacement,

        strInstallationVariant,

        false,

        listCreatedPlacements);

//evaluates the full name for all placed functions and interruption points

new NameService3D(oMainFunction.InstallationSpace).EvaluateAndSetAllNames();

//if accessory not placed automatically then location needs to be set manually

if (bPlacedAutomatically == false)

{

    foreach (Placement3D oPlacement in listCreatedPlacements)

    {

        //set parent for accessory

        oPlacement.SetParent(oMainFunction, false);

        //calculate transformation

        Matrix3D oTransformation = new Matrix3D();                       

        //set location is 3d space relatively to parent function

        oPlacement.RelativeTransformation = oTransformation;

    }

}

```
