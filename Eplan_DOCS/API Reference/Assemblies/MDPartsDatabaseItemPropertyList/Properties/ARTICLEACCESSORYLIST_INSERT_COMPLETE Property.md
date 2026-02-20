# ARTICLEACCESSORYLIST_INSERT_COMPLETE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1721.html

---

Insert complete accessory list # 22987.

Syntax

**C#**



public MDPropertyValue ARTICLEACCESSORYLIST_INSERT_COMPLETE {get; set;}

public:

property MDPropertyValue^ ARTICLEACCESSORYLIST_INSERT_COMPLETE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

If this property is activated, all parts of the accessory list are inserted automatically during the device selection. If the property is deactivated, the desired accessory parts have to be selected from the list during the device selection.

When inserting or placing a device, all parts of an accessory list are added automatically if this property is activated and in addition the project setting Add required accessories automatically is activated.
