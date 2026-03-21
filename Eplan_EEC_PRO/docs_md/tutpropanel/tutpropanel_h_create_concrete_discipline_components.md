---
title: "Creating concrete discipline components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutpropanel_h_create_concrete_discipline_components.htm"
file: "tutpropanel_h_create_concrete_discipline_components"
category: "tutpropanel"
---

# Creating concrete discipline components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating concrete discipline components The hierarchy of the Pro Panel components is set by the discipline. To create a discipline components structure that deviates from the mechatronic structure, the plug-socket principle is applied. This means that the superordinate discipline components receive one or more socket parameters and the subordinate discipline components receive a plug parameter. The socket and plug parameters are assigned values. Discipline components whose plug parameters have the same value as a socket parameter from a different discipline component are installed there. If more discipline components have the same value for the plug parameter, the components are installed either in the order in which they are collected in the mechatronic structure, or in the order specified by the value of the Position sequence parameter. This tutorial shows how both techniques may be applied. Create the following discipline components without adding resources in the ECAD.ProPanel unit: See [Creating discipline components](eecbase_k_create_discipline_component.htm) Name | Super class | Article | Parameter | Parameter value  
---|---|---|---|---  
LayoutSpace | LayoutSpace | Layout space | Plug | LayoutSpace  
Socket | Enclosure  
AE1050_500 | Enclosure | Enclosure | EPN | AE 1050.500  
Plug | Enclosure  
Socket | EnclosureMounted  
AE1050_500_MountingPanel | MountingPanel | Mounting panel of the enclosure | Id | 15100.3.1;0;0  
Plug | EnclosureMounted  
Socket | MP_Plane  
MP_Plane_Front | Plane | Mounting surface of the mounting panel | Id | 16000.1.2;10002;0  
Plug | MP_Plane  
Socket | PlaneMounted  
KK3040 | abstractCableDuct | Wire duct 30 mm x 40 mm (H x W) | Coordinate |   
Dimension | =List{329.0,0}  
EPN | KK3040  
Id | 15102.2.2;0;0  
Plug | PlaneMounted  
KK3060 | abstractCableDuct | Wire duct 30 mm x 60 mm (H x W) | Coordinate |   
Dimension | =List{420.0,90}  
EPN | KK3060  
Id | 15102.2.2;0;0  
Plug | PlaneMounted  
TS35_7_5 | MountingRail | Mounting rail | Coordinate |   
Dimension | =List{329.0,0}  
DT_Code | MR  
DT_Counter | =mc.mos('T_Mechatronic_ModularSystem.ECAD.ProPanel.TS35_7_5').indexOf(this)+1  
EPN | TS 35_7,5  
Id | 15102.2.2;0;0  
Plug | PlaneMounted  
Socket | =$DT_Code + $DT_Counter  
PowerSupply_PxC_2938581 | abstractDevice | PxC power adapter for PLC | Coordinate |   
DeviceTag |   
DT_Code | T  
DT_Counter | =if(not(origin.isNull())) then dc.dos('T_Mechatronic_ModularSystem.ECAD.ProPanel.abstractPowerSupply').indexOf(this)+1 else '**Calculation is performed only in discipline structure**' endif  
EPN | PXC.2938581  
Mate |   
Plug | MR1  
Position | 100  
Width |   
PxC_IL_PB_DP | abstractDevice | PxC PLC IL PB DP | Coordinate |   
DeviceTag | =$DT_Code + $DT_Counter  
DT_Code | Q  
DT_Counter | =if(not(origin.isNull())) then dc.dos('T_Mechatronic_ModularSystem.ECAD.ProPanel.abstractPLCDevice').indexOf(this)+1 else '**Calculation is performed only in discipline structure**' endif  
EPN | PXC.2862246  
Mate |   
Plug | MR1  
Position | 200  
Width | =p8dbquery($EPN,'1',22013)  
PxC_IL_24_DI | abstractDevice | PxC IL 24 DI | Coordinate |   
DeviceTag | =$DT_Code + $DT_Counter  
DT_Code | T  
DT_Counter | =if(not(origin.isNull())) then dc.dos('T_Mechatronic_ModularSystem.ECAD.ProPanel.abstractPLCDevice').indexOf(this)+1 else '**Calculation is performed only in discipline structure**' endif  
EPN | PXC.2861221  
Mate | =List{'M4','M2',-2.4}  
Plug | MR1  
Position | 300  
Width |   
EndBracket_PxC_3022276 | abstractDevice | Terminal endblock | Coordinate |   
DeviceTag |   
DT_Code |   
DT_Counter |   
EPN | PXC.3022276  
Mate |   
Plug | MR2  
Position |   
Width |   
Terminal_PxC_3031212 | abstractTerminal | Terminal clamp | Coordinate |   
EPN | PXC.3031212  
Plug | MR2  
Position | 300  
Explanation of the formulas: A formula is used for the DT_Counter parameter of the mounting rails that navigates via mc to the superordinate mechatronic component and uses mos(â<type of discipline component>') to collect all subordinate components of the same type as the discipline component. These discipline components are saved in a collection that is accessed via indexOf(this) to determine the position of the current discipline component in the collection. The result of this formula is used for the value of the socket and therefore has to be determined in the mechatronic structure so that the discipline components can reference these in the subsequent calculation. A formula is used for the DT_Counter parameter of all the devices to be placed on the mounting rails that navigates via dc to the superordinate discipline component and uses dos(â<type of discipline component>') to collect all subordinate components of the same type as the discipline component. These discipline components are saved in a collection that is accessed via indexOf(this) to determine the position of the current discipline component in the collection. Since the value cannot be determined in the mechatronic structure, if(not(origin.isNull()) is used to query whether the component is located in the mechatronic or discipline-specific structure. In the case of the mechatronic structure the text '**Calculation is performed only in discipline structure**' is displayed instead of an error message. The values for DeviceTag are assembled from the parameter values for DT_Code and DT_Counter, so that the value A2 is calculated for the PLC component PxC_IL_PB_DP. The Dimension parameter receives a list containing two values that correspond to the length and the angle, respectively. For example, =List{329.0,0} supplies a length of 329.0 mm and an angle of 0 degrees. For the Width parameter, =p8dbquery is used to initiate a database query to the Eplan Electric P8 parts database. As arguments for the query, $EPN is sent to the parts database as the value of the EPN parameter, and '1',22013 as the field number for the width. Tip If field contents are to be queried by the parts database that cannot be accessed via p8dbquery, it is advisable to convert the parts database into an SQL database. SQL database queries that return the desired result must then be inserted into the formulas of the parameters.
