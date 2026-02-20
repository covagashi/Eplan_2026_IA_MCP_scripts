# SetAreaByWidth Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Image~SetAreaByWidth.html

---

Sets the size of an image by setting the coordinates of the lower left corner and the width. By this means the the aspect ratio is kept always the same as in the original image. The height results of the aspect ratio.

Syntax

**C#**



public void SetAreaByWidth( 

   PointD pntStart,

   double width

)

public:

void SetAreaByWidth( 

   PointD pntStart,

   double width

)


#### Parameters

*pntStart*
:   [Eplan.EplApi.Base.PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html) representing image's lower left corner

*width*
:   width of the Image
