# SetAreaBySize Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.QRCode~SetAreaBySize.html

---

Sets the size of an QRCode.

Syntax

**C#**



public void SetAreaBySize( 

   PointD pntStart,

   double size

)

public:

void SetAreaBySize( 

   PointD pntStart,

   double size

)


#### Parameters

*pntStart*
:   [Eplan.EplApi.Base.PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html) representing image's lower left corner

*size*
:   Size of QRCode

Remarks

Sets the size of an QRCode by setting the coordinates of the lower left corner and the size. QRCode should always have the same width as height so no additional data is required.
