# GetPhysicalDimensionOfImage Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Image~GetPhysicalDimensionOfImage.html

---

Returns size of the bitmap in pixels.

Syntax

**C#**



public PointD GetPhysicalDimensionOfImage( 

   string strFileName

)

public:

PointD GetPhysicalDimensionOfImage( 

   String^ strFileName

)


#### Parameters

*strFileName*
:   Path to file.

#### Return Value

[Eplan.EplApi.Base.PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html) - height and width of the bitmap in pixels.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strFileName` is `null`. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when dimension cannot be read |
