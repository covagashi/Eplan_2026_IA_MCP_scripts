---
title: "Parameter types"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_create_parametertypes.htm"
file: "eecbase_k_create_parametertypes"
category: "eecbase"
---

# Parameter types

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Parameter types

The following table provides an overview of all parameter types. Use the header fields for sorting and the input fields in the second table row for filtering.

Parameter type | Discipline | Usage | Description  
---|---|---|---  
Dimension | ECAD3D | Dimensions |  Dimensions: Height, Width, Depth  
Components: Enclosure, Enclosure_Part, MountingPanel, FreeMountingPanel, Plane  
Examples:  
Dimension: =List{'10','20','30'} Dimensions: Height, width, angle  
Components: Area Examples:  
Dimension: =List{'10','20','90'} Dimensions: Length, angle  
Components: Busbar, MountingRail, WireDuct Examples:  
Dimension: =List{'100','90'} Dimensions: Angle  
Components: CutOut, Device Examples:  
Dimension: =List{'90'}  
DimensionMap | ECAD3D | Dimensions |  Dimensions: Height, Width, Depth  
Components: Enclosure, Enclosure_Part, MountingPanel, FreeMountingPanel, Plane  
Examples:  
DimensionMap: =Map{Pair{'height',10}, Pair{'width',20}, Pair{'depth',30}} Dimensions: Height, width, angle  
Components: Area Examples:  
DimensionMap: =Map{Pair{'height',10}, Pair{'width',20}, Pair{'angle',90}} Dimensions: Length, angle  
Components: Busbar, MountingRail, WireDuct Examples:  
DimensionMap: =Map{Pair{'length',100}, Pair{'angle',90}} Dimensions: Angle  
Components: CutOut, Device Examples:  
DimensionMap: =Map{Pair{'angle',90}}  
PartNumber | ECAD3D | Part number | Part number of a component in the parts database  
ArticleVariant | ECAD3D | Part variant |  The variant of the part of a Pro Panel component. The part variant must correspond to the name of the variant in the parts database. This can be any string.  
  
Map | ECAD3D | Layout space description |  Map for the specification of the input field Description in the dialog Properties (components): Layout space dialog. Example: =Map{Pair{'36018','LayoutSpace description'}}  
PropertyMap | ECAD3D | Component property | Map for specifying component characteristics. The key corresponds to the property number, the value corresponds to the property text. Example for the specification Remark: Remark <20045>: =Map{Pair{'20045','Stack of workpieces'}}  
DeviceTag | ECAD3D | Device tag | Device tag (DT). The DT has to be specified fully for Pro Panel components. It is not compiled during the creation of Pro Panel from individual structure identifiers.  
DrillingPatternVariant | ECAD3D | Drilling pattern | The variant of a drilling pattern of a Pro Panel article. The variant of the drilling pattern must conform to the name of the drilling pattern in the part definition. This can be any string.  
Id | ECAD3D | Identification number | Identification number that clearly identifies a mounting surface.  
Coordinate | ECAD3D | Coordinate | Coordinates for the placement of objects with the syntax =List{x,y}  
CoordinateMap | ECAD3D | Coordinates map | Coordinates for the placement of objects with the syntax =Map{Pair{'x',<value>},Pair{'y',<value>}}  
Macro3D | ECAD3D | 3D-Macro | Places the specified 3D macro directly instead of a part with the syntax =type('Engineering.System').globalResourcePath()+'<Macro name.ema>'  
String | ECAD3D | Macro variant | The variant of the macro for a part.  
The name of this parameter is to be entered in the model variables under Disciplines > ECAD > Eplan Electric P8 > Parameter Name For The Window Macro Variant so that macro variants can be used (see [Parameter Name For The Window Macro Variant](admin_r_modelvar_p8variant.htm)).  
MateMap | ECAD3D | Placement mate on mate with coordinate specification and angle specification | For the placement of objects in relation to a MateMarker with the syntax =Map{Pair{'src','C'},Pair{'dest','C'},Pair{'dx',<value>},Pair{'dy',<value>},Pair{'dz',<value>},Pair{'angle',<value>}}  
Mate | ECAD3D | Placement mate on mate, optionally with distance | For the placement of objects in relation to the mates, a predecessor object with the syntax =List{'source-Mate','destination-Mate',distance}  
MateMarker | ECAD3D | Placement marker | Designates a distinct object, on which placement should take place or which is referred to.  
BusBarId | ECAD3D | BusBarId | ID of the busbar system  
SupplementaryMap | ECAD3D | Enclosure description | Map for the specification of the input field Description in the dialog Properties (components): Layout space: =Map{Pair{'36018','Enclosure description'}}  
PropertyMap | ECAD3D |  Supplementary field / Supplementary field [x] Indexed properties <property>[x] |  Map for the specification of the property Supplementary field or Supplementary field [1] to Supplementary field [1000] or another indexed property. A map with a list or a map with the key value pairs can be specified for the values. For a map with list the specifications have to take place in sequence starting with 1. Empty fields must be specified as such.  
Example map with list: =Map{Pair{'20901', List{'Text1','Text2','','Text4'}}} Example map with key value pairs: =Map{Pair{'20901', Map{Pair{'0','Text1'},Pair{'1','Text2'},Pair{'5','Text6'}}}} Indexed properties can currently only be applied with the following ProPanel components:
     * BusBarSystem
     * CutOut,
     * Device,
     * Enclosure,
     * EnclosurePart,
     * LayoutSpace,
     * MountingRail,
     * WireDuct,  
SupplementaryMap | ECAD3D | Supplementary Map | Transfer of supplemental information, e.g. placement of the hold with busbars.  
Syntax for number of holders for busbars:  
=Map{Pair{'holder',<number of holders>}, Pair{'startoffset',<value>}, Pair{'endoffset',<value>}}  
Syntax for placement barred areas:  
=Map{Pair{'type',1}}  
Syntax for drilling barred areas:  
=Map{Pair{'type',2}}  
Bag | Engineering | Collection |  A collection of objects. The objects in bags are not sorted, there is no defined sequence. Objects may appear multiple. =Bag{1,3,3,2,4}  
BidiMap | Engineering | Key-value pairs |  A map of key-value pairs. BidiMaps realize a bi-directional access, i.e. it can be either accessed efficiently with the key on the values and with the value of the associated key. Unlike the other maps each value can be included in the map only once. =BidiMap{Pair{'A',1}, Pair{'B',2}} Inverted BidiMap: =BidiMap{Pair{1,'A'}, Pair{2,'B'}}  
Boolean | Engineering | Logical value |  The data type Boolean is used to save the truth values true or false. =true =false  
Double | Engineering | Floating-point number |  The double data type stores 64-bit floating-point numbers Values from +/-4.9E-324 to +/-1.7E+308  
List | Engineering | Collection of objects |  A collection of objects. Objects in a list have a defined sequence. Objects may appear multiple. =List{1.2,3.4} =List {1,2,3,3,List{4,5}}  
Socket | Engineering | Modularization |  A socket may be viewed as an electrical socket. Plugs can be plugged into these sockets. More than one plug can be plugged into a single socket. However, a plug can only be plugged into a single socket. Sockets also serve as graphical reference points, e.g. on a schematic page. Other elements or fragments can be positioned, e.g. on a schematic page, relative to these reference points. These elements or fragments must be equipped with parameters of the âplugâ type. Example of a socket specification for a schematic page: #<socket:Parameter name> #<socket:Input1>  
Plug | Engineering | Modularization |  Objects with Plug-type parameters are used to connect discipline components to Sockets. This involves a Plug docking with the assigned Socket. The assignment is made based on matching parameter values. It is also possible for more than one plug to reference a single socket. Example of a plug specification for a window macro: #<plug:Parameter name> #<plug:EP>  
OrderedMap | Engineering | Key-value pairs | Key-value pairs with ordered keys. Order criterion is the order of inserting the keys into the map.  
String | Engineering | String |  The String data type is used to store any string. ='Hello World'  
Map | Engineering | Key-value pairs |  A map of key-value pairs. Each key is contained in the map only once. Values may be included any number of times in the map. =Map{Pair{'Hallo','hello'}, Pair{'Welt', 'world'}}  
Set | Engineering | Collection of objects |  A collection of objects. The objects in sets are not sorted, there is no defined sequence. Each object is contained in the set only once. =Set{1,3,2,4} =Set{1,2,3,3,List{4,5}}  
Integer | Engineering |  |  The integer data type is used to store 32-bit integers Values from -2,147,483,648 to 2,147,483,647  
BOOL | PLC | Boolean text |  false or true  
BYTE | PLC | 8-bit dual or hexadecimal number |  Values from B#16#0 to B#16#FF  
DATE | PLC | Date |  Date in PLC context. Values from 1990-01-01 to 2168-12-31  
DATE_AND_TIME | PLC | Date and time |  Compound data type. Values from 1990-01-01-0:0:0 to 2089-12-31-23:59:59.999  
DINT | PLC | Decimal number with preceding sign | Values from L#-2147483648 to L#2147483647  
DT | PLC | Date and time |  Date in PLC context. Values from 1990-01-01-0:0:0 to 2089-12-31-23:59:59.999  
DWORD | PLC |  32-bit dual or hexadecimal number Decimal number without preceding sign |  Values from 2#0 to 2#1111_1111_1111_1111_1111_1111_1111_1111 DW#16#0000_0000 to DW#16#FFFF_FFFF B#(0,0,0,0) to B#(255,255,255,255)  
IX | PLC | PLC input |  For the modeling of binary PLC inputs. Examples: =0 =1 =false =true  
IB | PLC | PLC inputs |  For the modeling of PLC inputs in byte format. Values from 0 to 255  
IW | PLC | PLC inputs |  For the modeling of PLC outputs in word format. Values from 0 to 65535, or from -32768 to 32767 respectively  
ID | PLC | PLC inputs |  For the modeling of PLC inputs in double-word format. Values from -2 147 483 648 to 2 147 483 647, or from 3.402823e38 to -1.175495e38 respectively  
INT | PLC | Integer with preceding sign | Values from -32768 to 32767  
LREAL | PLC | IEEE floating-point number with double precision | Values from -1.7976931348623158e+308 to -2.2250738585072014e-308  
LWORD | PLC | 8 byte dual number | Values from 16#000000000000000000000000 to 16#FFFFFFFFFFFFFFFF (-922337203685475808 to 922337203685475807).  
QX | PLC | PLC outputs |  For the modeling of binary PLC outputs. Examples: =0 =1 =false =true  
QB | PLC | PLC outputs |  For the modeling of PLC outputs in byte format. Values from 0 to 255  
QW | PLC | PLC outputs | For the modeling of PLC outputs in word format.Values from 0 to 65535, or from -32768 to 32767 respectively  
QD | PLC | PLC outputs |  For modeling PLC outputs in double-word format. Values from -2 147 483 648 to 2 147 483 647, or from 3.402823e38 to -1.175495e38 respectively  
Byte | PLC | 8 bit dual number |  Values from B#16#0 to B#16#F (0 to 255)  
DATE | PLC | IEC date in steps of 1 day | Values from D#1990-1-1 to D#2168-12-31  
REAL | PLC | IEEE floating point number with single precision | Values from Â±1.175 495e-38 to Â±3.402823e+38  
SINT | PLC | Short integer number with preceding sign | Values from -128 to 127  
STRING | PLC | String | A group of a maximum of 254 characters (data type CHAR)  
TIME | PLC | IEC time in steps of 1 ms, integer with preceding sign |  Values from T#-24D_20H_31M_23S_648MS to T#24D_20H_31M_23S_647MS  
TIME_OF_DAY | PLC | Time in steps of 1 ms | TOD#0:0:0.0 to TOD#23:59:59.999  
TOD | PLC | Time | 32 bit values from 00:00:00,000 to 23:59:59,999  
UDINT | PLC | Positive integer values | Values from 0 to 4294967295  
UINT | PLC | Positive integer values | Values from 0 to 65535  
ULINT | PLC | Positive integer values | Values from 0 to 18446744073709551615  
USINT | PLC | Positive integer values | Values from 0 to 255  
WORD | PLC |  16-bit dual or hexadecimal number BCD decimal number without preceding sign |  2#0 to 2#1111_1111_1111_1111 W#16#0 to W#16#FFFF C#0 to C#999 B#0.0 to B#255.255  
ANY | PLC | ANY pointer |  ANY pointer pointing to a data area.  
BLOCK_DB | PLC | Source Data Block Editor | Declaration for a data block as a data block  
BLOCK_FB | PLC | Source Data Block Editor |  Declaration for a data block as a function block  
BLOCK_FC | PLC | Source Data Block Editor |  Declaration for a data block as a function  
BLOCK_SDB | PLC | Source Data Block Editor | Declaration for a data block as a system data block  
CHAR | PLC | ASCII character |  Single character, or letter. Example: N  
COUNTER | PLC | PLC counter |  16 bit counter values Values from 0000 to FFFF, or 0 to 65535 respectively  
POINTER | PLC | Pointer | Points to a storage location of a data block  
S5TIME | PLC | S7 time in steps of 10 ms. |  S5T#0H_0M_0S_10MS to S5T#2H_46M_30S_0MS and S5T#0H_0M_0S_0MS  
TIMER | PLC | PLC timer | Real-time clock or value for a time function (pulse, switch-on delay, switch-off delay, storing switch-on delay or extended pulse)
