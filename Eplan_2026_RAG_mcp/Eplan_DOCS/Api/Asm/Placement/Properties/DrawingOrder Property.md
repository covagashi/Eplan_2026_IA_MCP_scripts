# DrawingOrder Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~DrawingOrder.html

---

Sets display sequence. The drawing order flag will be used to sort elements according to drawing order within a group. If elements chare the same value the drawing order will result from order of the data model. Default value is 67.

Syntax

**C#**



public short DrawingOrder {get; set;}

public:

property short DrawingOrder {

   short get();

   void set (    short value);

}


#### Property Value

Number of position.
