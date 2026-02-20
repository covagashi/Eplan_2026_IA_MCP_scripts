# partsmanagementapi

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/partsmanagementapi.html

---

```
Action class for exporting and importing parts and other parts management items like addresses, constructions, terminals, accessory lists and accessory placements.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to be performed:
 '¢ "IMPORT": Import parts (and other record types)
 '¢ "EXPORT": Export parts (and other record types)
 '¢ "EXPORTPARTS": Exports parts via the property numbers of specified properties
 '¢ "EXPORTMANUFACTURERS": Exports manufacturers via the property numbers of specified properties
 '¢ "EXPORTCONSTRUCTIONS": Exports construction via the property numbers of specified properties
 '¢ "EXPORTCONNECTIONPATTERNS": Exports connection point pattern via the property numbers of specified properties
 '¢ "EXPORTACCESSORYLISTS": Exports accessory list via the property numbers of specified properties
 '¢ "EXPORTACCESSORYPLACEMENTS": Exports accessory placements via the property numbers of specified properties
 ``` |
| ``` IMPORTFILE
 ``` | ``` The directory and the file name of the file to be imported must be specified here. This only applies to "IMPORT".
 ``` |
| ``` EXPORTFILE
 ``` | ``` The directory and the file name of the file to be exported must be specified here. The file extension is automatically added by the system. This only applies to "EXPORT".
 ``` |
| ``` FORMAT
 ``` | ``` File format ("XPamImportXml","XPamExportXml", or user-defined format) (optional). "IXPartsImportExportEdz" - export to .edz and import from .edz.
 '¢ "XPamExportXml" is the default format value for tasks of TYPE "EXPORT".
 '¢ "XPamImportXml" is the default format value for tasks of TYPE "IMPORT".
 ``` |
| ``` PARTNUMBER
 ``` | ``` Used for exporting parts: Part number of article (optional). 
 ``` |
| ``` MANUFACTURER
 ``` | ``` Used for exporting addresses: Long name of an address (optional).
 ``` |
| ``` CONSTRUCTION
 ``` | ``` Used for exporting constructions: Name of construction (optional).
 ``` |
| ``` CONNECTIONPOINTPATTERN
 ``` | ``` Used for exporting terminals: Name of terminal (optional).
 ``` |
| ``` ACCESSORYLIST
 ``` | ``` Used for exporting accessory lists: Name of accessorylist (optional). 
 ``` |
| ``` ACCESSORYPLACEMENT
 ``` | ``` Used for exporting accessory placements: Name of accessoryplacement (optional).
 ``` |
| ``` MODE
 ``` | ``` Used for Importing: Import mode  (optional).
 Supported modes are:
 '¢ 0: Append new records only
 '¢ 1: Update existing records only
 '¢ 2: Update existing records and append new ones
 '¢ 3: Replace existing records and append new ones
 Default value = 0, append new records only. If an invalid value is set, the default value 0 will be used.
 ``` |
| ``` ADDITIONAL_LANGUAGE
 ``` | ``` Valid only when TYPE has "IMPORT" value (optional).
 If the value of this parameter is 1, multi-language properties will be updated with another language values rather than being replaced with the file's content.
 If the parameter is omitted, content of the file replaces values of multi-language properties.
 ``` |
| ``` FILTERSCHEME
 ``` | ``` Configuration scheme for export parts. 
 Filter is empty by default. Using scheme allows to filter which items (e.g. parts, addresses, constructions, etc.) should be imported or exported.
 ``` |
| ``` PROPERTYIDn
 ``` | ``` Article property number. Where n in PROPERTYIDn is a number corresponding to n number in PROPERTYVALUEn.
 ``` |
| ``` PROPERTYVALUEn
 ``` | ``` Value for given article property number. Where n in PROPERTYVALUEn is a number corresponding to n number in PROPERTYIDn.
 ``` |

**Remarks**

```
In order to export more than one item, please use parameter item type + counter with following number of exported item (for example /PARTNUMBER1:A-B.100-C09EJ01 /PARTNUMBER2:A-B.140M-C-AFA11, etc)

If an error occurs during a parts list operation, a "BaseException" is thrown.

```

**Example**

```
Export a part, manufacturer and construction:

partsmanagementapi /TYPE:EXPORT /EXPORTFILE:C:\temp\PartsList.xml /PARTNUMBER:A-B.100-C09EJ01 /MANUFACTURER:LAPP /CONSTRUCTION:A-B.100-C_FS0_I_CH_DP

Export 2 parts and 2 manufacturers to XML format:

partsmanagementapi /TYPE:EXPORT /EXPORTFILE:C:\temp\PartsList.xml /PARTNUMBER1:A-B.100-C09EJ01 /PARTNUMBER2:A-B.140M-C-AFA11 /MANUFACTURER1:LAPP /MANUFACTURER2:Rittal

Export all parts to EDZ format:

partsmanagementapi /TYPE:EXPORT /FORMAT:IXPartsImportExportEdz /EXPORTFILE:C:\temp\PartsList.edz /PARTNUMBER1:*


Import from XML:

partsmanagementapi /TYPE:IMPORT /MODE:1 /IMPORTFILE:C:\temp\PartsList.xml

Import from EDZ:

partsmanagementapi /TYPE:IMPORT /FORMAT:IXPartsImportExportEdz /IMPORTFILE:C:\temp\PartsList.edz

Import from EDZ with mode 'Append new records only':

partsmanagementapi /TYPE:IMPORT /MODE:0 /FORMAT:IXPartsImportExportEdz /IMPORTFILE:C:\temp\PartsList.edz


Export parts with use FILTERSCHEME:

partsmanagementapi /TYPE:EXPORT /FILTERSCHEME:ExportFilterScheme /EXPORTFILE:C:\temp\PartsList.xml


Export every part with variant '2' or manufacturer 'ABB':

partsmanagementapi /TYPE:EXPORTPARTS /PROPERTYID1:22024 /PROPERTYVALUE1:2 /PROPERTYID2:22007 /PROPERTYVALUE2:ABB /EXPORTFILE:C:\temp\PartsList

Export every construction with name 'FES.130642' or 'RIT.SV9677x65':

partsmanagementapi /TYPE:EXPORTCONSTRUCTIONS /PROPERTYID1:22931 /PROPERTYVALUE1:FES.130642 /PROPERTYID2:22931 /PROPERTYVALUE2:RIT.SV9677x65 /EXPORTFILE:C:\temp\ConstructionsList

Export every manufacturer with short name 'PXC' to .edz format:

partsmanagementapi /TYPE:EXPORTMANUFACTURERS /FORMAT:IXPartsImportExportEdz /PROPERTYID1:22900 /PROPERTYVALUE1:PXC /EXPORTFILE:C:\temp\Manufactures

```