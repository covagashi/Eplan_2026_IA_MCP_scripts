# Width Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Pen~Width.html

---

Line width. Normally it is 0.13 - 2. Please use "-16002" as "from layer" value.

Syntax

**C#**



public double Width {get; set;}

public:

property double Width {

   double get();

   void set (    double value);

}


#### Property Value

Line width

Example

oPen.Width = 0.13 //oPen.Width = 0.18 //oPen.Width = 0.25 //oPen.Width = 0.35 //oPen.Width = 0.5 //oPen.Width = 0.7 //oPen.Width = 1 //oPen.Width = 2
