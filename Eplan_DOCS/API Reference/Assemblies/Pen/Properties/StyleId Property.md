# StyleId Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Pen~StyleId.html

---

Line style identifier (0-6) Please use "-16002" as "from layer" value.

Predefined line type index values are:

0 = continous: ------

1 = dash: - - - - -

2 = dot: .......

3 = dashdot: \_.\_.\_.\_

4 = dashdotdot: \_..\_..\_

5 = dash: \_ \_

6 = dashlongdot: \_\_ \_

-16002 = from layer

Syntax

**C#**



public short StyleId {get; set;}

public:

property short StyleId {

   short get();

   void set (    short value);

}


#### Property Value

Line style identifier (0-6)
