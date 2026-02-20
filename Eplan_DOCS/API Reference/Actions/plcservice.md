# plcservice

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/plcservice.html

---

```
Exports/imports PLC data using the specified converter.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to be performed by the action:
 '¢ "BUSDATAEXPORT": Bus data export.
 '¢ "BUSDATAIMPORT": Bus data import.
 '¢ "GENERATEPLCSCHEMATIC": Schematics generation.
 '¢ "EXPORTADDRESSOVERVIEW": Address overview export.
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path.
 ``` |
| ``` LANGUAGE
 ``` | ``` Language identifier 
 This parameter is only effective with the following values of the TYPE parameter: "BUSDATAEXPORT", "BUSDATAIMPORT"
 ``` |
| ``` CONVERTERID
 ``` | ``` Identification for busdata exporter. Values are:
 '¢ "PlcDcExchangerBeckhoffTC3AML" = Beckhoff TwinCAT 3 (AR APC 1.1.0)
 '¢ "PlcDcExchangerBoschAML" = Bosch Nexeed Automation (AR APC 1.0.0)
 '¢ "PlcDcExchangerLogiCals3AML" = logi.cals logi.CAD 3 (AR APC 1.1.0)
 '¢ "PlcDcExchangerMitsubishiAML" = Mitsubishi iQ Works (AR APC 1.0.0)
 '¢ "PlcDcExchangerMitsubishi110AML" = Mitsubishi iQ Works (AR APC 1.1.0)
 '¢ "PlcDcExchangerPhoenixContactAML" = Phoenix Contact PLCnext Engineer 2019 (AR APC 1.0.0)
 '¢ "PlcDcExchangerRockwellArchitectAML" = Rockwell Automation Studio 5000 (AR APC 1.0.0)
 '¢ "PlcDcExchangerSiemensTIA15AML" = Siemens SIMATIC STEP 7 TIA-Portal 15 (AR APC 1.0.0)
 '¢ "PlcDcExchangerSiemensTIA151AML" = Siemens SIMATIC STEP 7 TIA Portal 15.1 (AR APC 1.0.0)
 '¢ "PlcDcExchangerSiemensTIA16AML" = Siemens SIMATIC STEP 7 TIA Portal 16 (AR APC 1.1.0)
 '¢ "PlcDcExchangerSiemensTIA17AML" = Siemens SIMATIC STEP 7 TIA Portal 17 (AR APC 1.2.0)
 '¢ "PlcDcExchangerSiemensTIA18AML" = Siemens SIMATIC STEP 7 TIA Portal 18 (AR APC 1.3.0)
 '¢ "PlcDcExchangerSiemensTIA19AML" = Siemens SIMATIC STEP 7 TIA Portal 19 (AR APC 1.4.0)
 '¢ "PlcDcExchangerSiemensTSTAML" = Siemens TIA Selection Tool (AR APC 1.1.0)
 '¢ "PlcDcAMLExchangerGeneral" = Eplan Electric P8 AML-format
 '¢ "PlcDcXMLExchangerABB" = ABB Automation Builder
 '¢ "PlcDcXMLExchangerBandR" = B and R Automation Studio
 '¢ "PlcDcXMLExchangerRexroth" = Bosch Rexroth Indra Works
 '¢ "PlcDcXMLExchangerSchneider" = Schneider Unity Pro XL
 '¢ "PlcDcXMLExchangerSiemens" = Siemens SIMATIC STEP 7 5.6
 '¢ "PlcDcXMLExchangerUniversal" = Eplan Electric P8 PLC standard exchange format
 This parameter is only effective with the following values of the TYPE parameter: "BUSDATAEXPORT", "BUSDATAIMPORT"
 ``` |
| ``` CONFIGURATIONPROJECT
 ``` | ``` The name of the PLC configuration data set to export. 
 This parameter is only effective with the following values of the TYPE parameter: "BUSDATAEXPORT", "EXPORTADDRESSOVERVIEW"
 ``` |
| ``` DESTINATIONFILE
 ``` | ``` Destination file for data export.
 This parameter is only effective with the following values of the TYPE parameter: "BUSDATAEXPORT", "EXPORTADDRESSOVERVIEW"
 ``` |
| ``` SOURCEFILE
 ``` | ``` Source file for data import.
 This parameter is only effective with the following values of the TYPE parameter: "BUSDATAIMPORT"
 ``` |
| ``` OVERWRITE
 ``` | ``` If the output file already exists, this parameter specifies     whether it should be overwritten.
 Possible values: 0 = No (default), 1 = Yes.
 This parameter is only effective with the following values of the TYPE parameter: "BUSDATAEXPORT"
 ``` |
| ``` FORMAT
 ``` | ``` Format of export file(optional).
 This parameter is only effective with the following values of the TYPE parameter: "BUSDATAEXPORT".
 Some of the Converters, which have multiple formats are listed here along with the possible format values
 '¢ "PlcDcExchangerRockwellArchitectAML" = "AutomationML AR APC V1.0.0"
 '¢ "PlcDcExchangerRockwellArchitectAML" = "AutomationML AR APC V1.1.0"
 '¢ "PlcDcExchangerRockwellArchitectAML" = "AutomationML AR APC V1.2.0"
 '¢ "PlcDcXMLExchangerBandR" = "SPS-Standardaustauschformat V1.0"
 '¢ "PlcDcXMLExchangerBandR" = "SPS-Standardaustauschformat V2.0"
 '¢ "PlcDcXMLExchangerRexroth" = "SPS-Standardaustauschformat V1.0"
 '¢ "PlcDcXMLExchangerRexroth" = "SPS-Standardaustauschformat V2.0"
 '¢ "PlcDcAMLExchangerGeneral" = "AutomationML AR APC V1.0.0"
 '¢ "PlcDcAMLExchangerGeneral" = "AutomationML AR APC V1.1.0"
 '¢ "PlcDcAMLExchangerGeneral" = "AutomationML AR APC V1.2.0"
 '¢ "PlcDcAMLExchangerGeneral" = "AutomationML AR APC V1.3.0"
 '¢ "PlcDcAMLExchangerGeneral" = "AutomationML AR APC V1.4.0"
 '¢ "PlcDcAMLExchangerGeneral" = "PLC standard exchange format V1.0"
 '¢ "PlcDcAMLExchangerGeneral" = "PLC standard exchange format V2.0"
 '¢ "PlcDcXMLExchangerSchneider" = "Schneider XEF"
 '¢ "PlcDcXMLExchangerSchneider" = "Schneider XHW"
 '¢ "PlcDcXMLExchangerSchneider" = "Schneider XSY"
 '¢ "PlcDcXMLExchangerSchneider" = "Schneider ZEF"
 ``` |
| ``` EXPORTPORTSPECIFICINTERCONNECTION
 ``` | ``` Export port-specific interconnection(optional).
 Possible values: 0 = No, 1 = Yes. If the parameter is not used, the default value is the same as what is currently set in the GUI.
 This parameter is only effective with the following values of the TYPE parameter: "BUSDATAEXPORT"
 ``` |
| ``` EXPORTACCESSORIES
 ``` | ``` Export accessories(optional).
 Possible values: 0 = No, 1 = Yes. If the parameter is not used, the default value is the same as what is currently set in the GUI.
 This parameter is only effective with the following values of the TYPE parameter: "BUSDATAEXPORT"
 ``` |
| ``` EXPORTDRIVES
 ``` | ``` Export drives(optional).
 Possible values: 0 = No, 1 = Yes. If the parameter is not used, the default value is the same as what is currently set in the GUI.
 This parameter is only effective with the following values of the TYPE parameter: "BUSDATAEXPORT"
 ``` |
| ``` EXPORTDEVICESPECIFICCONFIGURATIONVALUES
 ``` | ``` Export device-specific configuration values(optional).
 Possible values: 0 = No, 1 = Yes. If the parameter is not used, the default value is the same as what is currently set in the GUI.
 This parameter is only effective with the following values of the TYPE parameter: "BUSDATAEXPORT"
 ``` |
| ``` IMPORTMATCH
 ``` | ``` Matching options for PLC data import. 
 The import process tries to match imported objects with those existing in the project.
 Based on the option selected, the matching may be performed by internal object ids or by objects' identifying names.
 If an imported object is matched with an existing function, properties of the existing function will be updated whereas for unmatched imported objects, new functions will be created in the project.
 The options are:
 '¢ 0 = Match by internal object ids.
 '¢ 1 = Match by identifying names. Note: in this case, a comparison dialog may be displayed for the user to individually selecting some function to update.
 '¢ 2 = Don't match. Create new functions for all imported objects.
 This parameter is only effective with the following values of the TYPE parameter: "BUSDATAIMPORT"
 ``` |
| ``` CONFIGFILE
 ``` | ``` A path to a "GenerateSchematic" configuration file for schematics generation.
 This parameter is only effective with the following values of the TYPE parameter: "GENERATEPLCSCHEMATIC"
 ``` |
| ``` SINGLELINEPAGES
 ``` | ``` If set, single-line pages will be generated.
 Possible values: 0 = No (default), 1 = Yes.
 This parameter is only effective with the following values of the TYPE parameter: "GENERATEPLCSCHEMATIC"
 ``` |
| ``` MULTILINEPAGES
 ``` | ``` If set, multi-line pages will be generated.
 Possible values: 0 = No (default), 1 = Yes.
 This parameter is only effective with the following values of the TYPE parameter: "GENERATEPLCSCHEMATIC"
 ``` |
| ``` OVERVIEWS
 ``` | ``` If set, overview pages will be generated.
 Possible values: 0 = No (default), 1 = Yes.
 This parameter is only effective with the following values of the TYPE parameter: "GENERATEPLCSCHEMATIC"
 ``` |
| ``` RACKOVERVIEWS
 ``` | ``` If set, rack overview pages will be generated.
 Possible values: 0 = No (default), 1 = Yes.
 This parameter is only effective with the following values of the TYPE parameter: "GENERATEPLCSCHEMATIC"
 ``` |
| ``` PLCSTATION
 ``` | ``` The name of the PLC station name to export.
 This parameter is only effective with the following values of the TYPE parameter: "EXPORTADDRESSOVERVIEW"
 ``` |
| ``` PLCCPU
 ``` | ``` The name of the PLC CPU name to export.
 This parameter is only effective with the following values of the TYPE parameter: "EXPORTADDRESSOVERVIEW"
 ``` |

**Example**

```
Bus data export:

Example 1:

plcservice 

                /TYPE:BUSDATAEXPORT

                /CONFIGURATIONPROJECT:Schneider-Electric

                /DESTINATIONFILE:"c:\tempdir\plcservice_export_1.xef"

                /PROJECTNAME:"C:\Users\Public\EPLAN\Electric P8\Projects\Microsoft\EPLAN_Sample_Project.elk" 

                /LANGUAGE:de_DE

                /CONVERTERID:PlcDcXMLExchangerSchneider

                /OVERWRITE:1

Example 2:

plcservice 

                /TYPE:BUSDATAEXPORT

                /CONFIGURATIONPROJECT:Phoenix1

                /DESTINATIONFILE:"c:\tempdir\plcservice_export_1.aml"

                /PROJECTNAME:"C:\Users\Public\EPLAN\Electric P8\Projects\Microsoft\EPLAN_Sample_Project.elk" 

                /LANGUAGE:de_DE

                /CONVERTERID:PlcDcAMLExchangerGeneral

                /OVERWRITE:1

                /FORMAT:"AutomationML AR APC V1.4.0"

                /EXPORTPORTSPECIFICINTERCONNECTION:1

                /EXPORTACCESSORIES:1

                /EXPORTDRIVES:1

                /EXPORTDEVICESPECIFICCONFIGURATIONVALUES:1

Bus data import:

plcservice 

                /TYPE:BUSDATAIMPORT

                /SOURCEFILE:"c:\tempdir\plcservice_export_2.pbf"

                /PROJECTNAME:"C:\Users\Public\EPLAN\Electric P8\Projects\Microsoft\EPLAN_Sample_Project.elk" 

                /LANGUAGE:de_DE

                /CONVERTERID:PlcDcXMLExchangerUniversal

Schematics generation:

plcservice 

                /TYPE:GENERATEPLCSCHEMATIC

                /PROJECTNAME:"C:\Users\Public\EPLAN\Electric P8\Projects\Microsoft\EPLAN_Sample_Project.elk" 

                /CONFIGFILE:"c:\tempdir\schematics_generation_config.xml"

                /SINGLELINEPAGES:1

                /MULTILINEPAGES:1

Address overview export:

plcservice 

                /TYPE:EXPORTADDRESSOVERVIEW

                /PROJECTNAME:"C:\Users\Public\EPLAN\Electric P8\Projects\Microsoft\EPLAN_Sample_Project.elk" 

                /CONFIGURATIONPROJECT:"CAx_AML_Drive_00"

                /PLCSTATION:"S71500/ET200MP station_1"

                /PLCCPU:"1"

                /DESTINATIONFILE:"c:\tempdir\address_overview_export.csv"

```