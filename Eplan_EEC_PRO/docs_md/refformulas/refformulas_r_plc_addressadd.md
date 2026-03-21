---
title: "addressAdd(String Address, Integer Increment, Integer Startbit, Integer Bitsize)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_plc_addressadd.htm"
file: "refformulas_r_plc_addressadd"
category: "refformulas"
---

# addressAdd(String Address, Integer Increment, Integer Startbit, Integer Bitsize)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  addressAdd(String Address, Integer Increment, Integer Startbit, Integer Bitsize) Methods for PLC addresses Adds the number of Increment bits to a PLC address that is specified with Address. addressAdd(String Address, Integer Increment, Integer Startbit, Integer Bitsize)  
---  
Arguments | String | Address | Start value in the notation Byte.Bit. The value for bit has to be greater than or equal to the value for the start bit.  
| Integer | Increment | Number of increments by which the bit is increased, relative to the start value.  
| Integer | Startbit | Number of the bit with which each byte begins. The counting begins at 0. Values greater than 0 means that correspondingly many bits at the beginning of each byte are not occupied.  
  
| Integer | Bitsize | Number of the used bits per byte. Typically: Bit size = Byte size - Start bit. In order not to occupy bits at the end of each byte, the value for the bit size is however selected lower.  
Return value | String | Resulting address  
[Examples](javascript:void\(0\);) Usage of the complete bit width: Formula | Result  
---|---  
='I'+addressAdd('0.0',3,0,8) | I0.3  
='I'+addressAdd('0.0',11,0,8) | I1.3  
='I'+addressAdd('0.0',11,0,16) | I0.11  
='I'+addressAdd('0.0',20,0,16) | I1.4  
Usage limited to the first half of the bit width: Formula | Result  
---|---  
='I'+addressAdd('0.0',2,0,4) | I0.2  
='I'+addressAdd('0.0',5,0,4) | I1.1  
Usage limited to the second half of the bit width: Formula | Result  
---|---  
='I'+addressAdd('0.4',2,4,4) | I0.6  
='I'+addressAdd('0.5',5,4,4) | I1.6
