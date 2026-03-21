# SetAreaByHeigth Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Image~SetAreaByHeigth.html

---

Sets the size of an image by setting the coordinates of the lower left corner and the height. By this means the the aspect ratio is kept always the same as in the original image. The width results of the aspect ratio.

Syntax

**C#**



public void SetAreaByHeigth( 

   PointD pntStart,

   double height

)

public:

void SetAreaByHeigth( 

   PointD pntStart,

   double height

)


#### Parameters

*pntStart*
:   [Eplan.EplApi.Base.PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html) representing image's lower left corner

*height*
:   Height of the image
