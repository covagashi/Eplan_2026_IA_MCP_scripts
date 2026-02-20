# ARTICLE_PLCDEVICE_ID Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICE_ID().html

---

Device description: File name # 22037.

Syntax

**C#**



public PropertyValue ARTICLE_PLCDEVICE_ID {get; set;}

public:

property PropertyValue^ ARTICLE_PLCDEVICE_ID {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. File name of the device description file of a PLC card. The part allocation during the import of PLC configuration files is carried out on the basis of this property. The file name is entered with the file name extension, but without file path. In addition to the property Device description: File name, the property Object description or Device description: Index in file must also be specified. On the basis of these properties a device is selected within the file during the import of PLC configuration files. During a part selection or device selection the property is filled with the corresponding value from the parts management.

In the Device description: File name property not only the GSD file name but also other entries, for example device IDs of CC Link modules can be stored. To this purpose you enter a prefix followed by a colon before the actual device ID, for example "CSP+:AJ65VBTCE2-8T". This entry is then exported unchanged. If the entry does not contain a prefix (meaning no colon) or the prefix "GSD:", for example "GSD:SIEM8139.GSD", the entry is interpreted as a device description file during the export in the AutomationML AR APC format.
