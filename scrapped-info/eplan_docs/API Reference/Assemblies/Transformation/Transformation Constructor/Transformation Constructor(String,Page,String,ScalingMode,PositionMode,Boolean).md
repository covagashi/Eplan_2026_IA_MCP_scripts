# Transformation Constructor(String,Page,String,ScalingMode,PositionMode,Boolean)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1461.html

---

Constructor.

Syntax

**C#**



public Transformation( 

   string pathToDXFFile,

   Page oPage,

   string strScheme,

   Transformation.ScalingMode scalingMode,

   Transformation.PositionMode positionMode,

   bool bKeepAspectRatio

)

public:

Transformation( 

   String^ pathToDXFFile,

   Page^ oPage,

   String^ strScheme,

   Transformation.ScalingMode scalingMode,

   Transformation.PositionMode positionMode,

   bool bKeepAspectRatio

)


#### Parameters

*pathToDXFFile*
:   Path to DXF file which will be imported.

*oPage*
:   Page where DXF file will be imported.

*strScheme*
:   Name of scheme used for import. It could be crucial to use the same scheme to fill parameters and import file to have correct results.

*scalingMode*
:   Determines what scale should be used.

*positionMode*
:   Determines where imported DXF file should be placed on page.

*bKeepAspectRatio*
:   When set to true scale on X and Y will be the same.

Remarks

Using this constructor will fill all Transformation parameters. It will fill correctly scale and offset which are needed for the import DXF file to place it correctly. It is important to use the same scheme for filling the Transformation parameters as this for the import DXF file. Using a different scheme could lead to different results than expected.
