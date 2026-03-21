# Pen Constructor(Int16,Int16,Double,Double,SByte)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Pen~_ctor(Int16,Int16,Double,Double,SByte).html

---

Constructor for internal usage only.

Syntax

**C#**



public Pen( 

   short nColorId,

   short nStyleId,

   double dStyleFactor,

   double crdWidth,

   sbyte nEndType

)

public:

Pen( 

   short nColorId,

   short nStyleId,

   double dStyleFactor,

   double crdWidth,

   sbyte nEndType

)


#### Parameters

*nColorId*
:   Line color index. Predefined values are:

    0 = black

    1 = red

    2 = yellow

    3 = green

    4 = cyan

    5 = blue

    6 = magenta

    7 = white

    252 = darkgray

    253 = gray

    The user can set also other values; possible values are from 0 to 255

*nStyleId*
:   Line style. Predefined line type index values are:

    0 = continous: ------

    1 = dash: - - - - -

    2 = dot: .......

    3 = dashdot: \_.\_.\_.\_

    4 = dashdotdot: \_..\_..\_

    5 = dash: \_ \_

    6 = dashlongdot: \_\_ \_

*dStyleFactor*
:   style factor

*crdWidth*
:   Line width

*nEndType*
:   Line end type
