---
title: "Create parameter"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutpropanel_h_create_parameters.htm"
file: "tutpropanel_h_create_parameters"
category: "tutpropanel"
---

# Create parameter

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Create parameter In addition parameters have to be created to be able to specify and place the discipline components more closely. See [Create parameter](eecbase_k_create_parameter.htm) Create all parameters of the following table in the ECAD.Parameter unit: Name | Type | Meaning  
---|---|---  
Coordinate | Coordinate | For specifying coordinates when positioning objects  
CoordinateMap | CoordinateMap | For specifying coordinates as map when positioning objects  
Syntax: Map{Pair{'x',100},Pair{'y',100}}  
DeviceTag | DeviceTag | Device tag  
Dimension | Dimension | For specifying the length, the angle of orientation or the surface area  
Syntax:  
=List{Length} or =List{Length,Angle} or =List{Length,Width}  
DT_Code | String | Part of the device code (BMK)  
DT_Counter | String | Part of the device code (BMK)  
EPN | PartNumber | EPLAN Part Number is the part number of a device from the Eplan parts database  
Id | Id | Identification number that clearly identifies a mounting surface  
Mate | Mate | For positioning objects in relation to the mates of a parent object  
Syntax:  
=List{'Source handle','Destination mounting point',Distance}  
MateMap | MateMap | For positioning objects in relation to a MateMarker  
Syntax:  
=Map{Pair{'src','C'},Pair{'dest','C'},Pair{'dx',0},Pair{'dy',0},Pair{'dz',0},Pair{'angle',0}}  
Plug | Plug | Components whose plug value corresponds to the socket value of a superordinate component can be installed there.  
Position | String | Attachment sequence: the higher the value, the further back the object is attached.  
Socket | Socket | Parent Components provide a socket value that determines which subordinate components may be installed there  
Width | Double | Width of an installed object. This value can be obtained from the parts data
