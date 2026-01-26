# ColorId Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Pen~ColorId.html

---

Color index (0-255). Please use "-16002" for "from layer" value.

Predefined values for line color index are:

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

-16002 = from layer

Syntax

**C#**



public short ColorId {get; set;}

public:

property short ColorId {

   short get();

   void set (    short value);

}


#### Property Value

Color index used by object

Remarks

In case of PropertyPlacement its TextColorId property can be used to change color of both text and its boxes. In case of other texts, TextColorId changes color of text and.Pen.ColorId color of its boxes.
