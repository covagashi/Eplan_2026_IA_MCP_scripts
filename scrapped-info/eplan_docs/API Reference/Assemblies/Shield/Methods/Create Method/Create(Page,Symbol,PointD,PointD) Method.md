# Create(Page,Symbol,PointD,PointD) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Shield~Create(Page,Symbol,PointD,PointD).html

---

Creates new Shield object of given dimensions and places on page.

Syntax

**C#**



public void Create( 

   Page pPage,

   Symbol pSymbol,

   PointD oStartPoint,

   PointD oEndPoint

)

public:

void Create( 

   Page^ pPage,

   Symbol^ pSymbol,

   PointD oStartPoint,

   PointD oEndPoint

)


#### Parameters

*pPage*
:   Page on which shield will be placed. Can't be `null`.

*pSymbol*
:   Determines symbol which will be assigned to shield. Can't be `null` and must have at least one variant.

*oStartPoint*
:   Position of shield area corner.

*oEndPoint*
:   Position of shield area corner which is `opposite` to `oStartPoint`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the Shield has been already created. |
| [System.ArgumentNullException](#) | Thrown if parameter is `null`. |
| [System.ArgumentException](#) | Thrown if symbol type is different from Symbol.SymbolType.Shielding or has no variants. |

Remarks

Create method automatically determines symbol variant which will be used based dependently on logical area passed as argument. In case of Shield this is important due to location of connection point. Method checks the area (whether is horizontally or vertically placed) and relative location of its oStartPoint to oEndPoint. For example when area is placed horizontally and start point is on the left, then variant A is used. If the end point is located on the left side of the area, then variant C is used.

Example

The following example shows how to create and place Shield on page.

**C#**

```
//prepare symbol of Shield

SymbolVariant oSymbolVariant = new SymbolVariant();

string strSymbolLibName = "SPECIAL";

string strSymbolName = @"SH";

SymbolLibrary oSymbolLibrary = new SymbolLibrary(oProject, strSymbolLibName);

Symbol oSymbol = new Symbol(oSymbolLibrary, strSymbolName);

//create Shield

Page oPage = oProject.Pages[14];

Shield oShield = new Shield();

oShield.Create(oPage, oSymbol, new PointD(50.0, 200.0), new PointD(120.0, 230.0));

```
