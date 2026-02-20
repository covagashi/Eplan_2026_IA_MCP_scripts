# ConvertCoordinate(Page,PointD,CoordinateSystems) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.CoordinateService~ConvertCoordinate(Page,PointD,CoordinateSystems).html

---

Method that converts from coordinate system based on page type to another

Syntax

**C#**



public PointD ConvertCoordinate( 

   Page oPage,

   PointD oSourcePoint,

   CoordinateService.CoordinateSystems oDestinationCoordinateSystem

)

public:

PointD ConvertCoordinate( 

   Page^ oPage,

   PointD oSourcePoint,

   CoordinateService.CoordinateSystems oDestinationCoordinateSystem

)


#### Parameters

*oPage*
:   Page which frame size, height and type will be used to calculate new coordinates

*oSourcePoint*
:   Source Point.

*oDestinationCoordinateSystem*
:   Destination coordinate system.
