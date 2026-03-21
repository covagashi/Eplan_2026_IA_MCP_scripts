# ARTICLE_PLCGROUP_INDEXINFILE_1 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_INDEXINFILE_1().html

---

PLC subdevice 1: Device description: Index in file # 22366.

Syntax

**C#**



public PropertyValue ARTICLE_PLCGROUP_INDEXINFILE_1 {get; set;}

public:

property PropertyValue^ ARTICLE_PLCGROUP_INDEXINFILE_1 {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Index for PLC subdevice 1 in the device description file of a PLC card. This property has to be filled for PLC subdevices if these are expected as independent devices in the PLC configuration program and are identified via a device description file and the associated index. The device description file is specified at the PLC box (main device). Through the index it is possible to select a device in a language-neutral form within such a file. During a part selection or device selection the property is filled with the corresponding value from the parts management. The property is taken into account during the PLC data exchange in AutomationML AR APC format.
