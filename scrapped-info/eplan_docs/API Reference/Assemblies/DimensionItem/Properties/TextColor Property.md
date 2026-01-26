# TextColor Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~TextColor.html

---

Color for displayed text. Color index (0-255) Please use -16002 as "From layer" value.

Predefined values for line colour index are:

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

Syntax

**C#**



public short TextColor {get; set;}

public:

property short TextColor {

   short get();

   void set (    short value);

}


#### Property Value

Color index used by object
