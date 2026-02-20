# FRAME_CONTACTIMAGE_OFFSET Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~FRAME_CONTACTIMAGE_OFFSET().html

---

Contact image margin (in path) # 12060.

Syntax

**C#**



public PropertyValue FRAME_CONTACTIMAGE_OFFSET {get; set;}

public:

property PropertyValue^ FRAME_CONTACTIMAGE_OFFSET {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

For automatically aligned contact images, this value specifies the distance of the contact image to the bottom of the page or the relevant "Ladder" borders (depending on the plot frame used).
