# GetDrillingsFromDrillingPattern Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Placement3DService~GetDrillingsFromDrillingPattern.html

---

Returns drilling objects which are generated based on drilling pattern assigned to 3d placement part.

Syntax

**C#**



public Drilling[] GetDrillingsFromDrillingPattern( 

   Placement3D pPlacement

)

public:

array<Drilling^>^ GetDrillingsFromDrillingPattern( 

   Placement3D^ pPlacement

)


#### Parameters

*pPlacement*
:   3D placement for which drilling objects will be generated. Can't be `null`.

#### Return Value

Array of generated drilling objects or empty array.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when parameter is `null`. |
| [System.ArgumentException](#) | Thrown when parameter is `invalid`. |
| [System.ApplicationException](#) | The functionality is not available. |

Remarks

Method generates transient drilling objects. Number, type and location of drillings depends on two things. First is the drilling pattern assigned to part of 3D placement. Other are location on parent. In places where placement doesn't have contact with parent drills are not created.

Example

Example below prints out to consol basic information about drillings from drilling pattern:

**C#**

```
//find duct object in project

DMObjectsFinder oFinder = new DMObjectsFinder(oProject);

Duct oDuct = oFinder.GetFunctions3D(null).OfType<Duct>().First();

//get all drilling objects from duct

Drilling[] arrDrillings = new Placement3DService().GetDrillingsFromDrillingPattern(oDuct);

foreach (Drilling oDrilling in arrDrillings)

{

    Console.WriteLine("------- Drilling -------");

    //write the relative position on parent

    Console.WriteLine(

        String.Format(

            "Relative position: ({0}, {1}, {2})",

            oDrilling.RelativeTransformation.OffsetX,

            oDrilling.RelativeTransformation.OffsetY,

            oDrilling.RelativeTransformation.OffsetZ));

    //write the type of drilling

    Console.WriteLine(

        String.Format(

            "Type of drilling: {0}",

            oDrilling.FunctionDefinition.Id));

}

```
