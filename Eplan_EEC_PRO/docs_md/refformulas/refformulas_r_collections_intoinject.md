---
title: "intoInject(Block expession,Object startValue)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_collections_intoinject.htm"
file: "refformulas_r_collections_intoinject"
category: "refformulas"
---

# intoInject(Block expession,Object startValue)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  intoInject(Block expession,Object startValue) General methods for Collections Accumulates a current value by evaluating expression. intoInject(Block expession,Object startValue)  
---  
Arguments | Block | expression | Expression that should be applied to all objects in the collection.  
Object | startValue | Start value of the accumulation.  
Return value | Object | Result of the accumulation  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=List{ 10, 11, 12}.intoInject(indexValue,startValue | indexValue + startValue,0) | 33  
=List{'String1','String2','String3'}.intoInject(indexValue,startValue | startValue.append(Pair{indexValue,indexValue + '_Value'}),List{}) | [String1Â»String1_Value,String2Â»String2_Value,String3Â»String3_Value]  
Description for the example 1: Data in this example
     * List{10,11,12} = List of objects iterated over with intoInject
     * indexValue = Index variable
     * startValue = Variable for the intermediate value
     * indexValue + startValue = Instruction (any EEC formula is possible)
     * 0 = Starting value for startValue
Index number of iteration | Index variable indexValue | Intermediate value startValue | Result value for indexValue + startValue  
---|---|---|---  
1 | 10 | 0 | 10  
2 | 11 | 10 | 21  
3 | 12 | 21 | 33  
intoInject is used in practice, e.g., to apply Maps whose key-value pairs contain lists as values. The following example shows how signal names are collected in a project and sorted in a map depending on their signal type. [Example for creating a map](javascript:void\(0\);) The following signal types are available in the data model:
     * AbsSignal.AbsActuator.AO
     * AbsSignal.AbsActuator.DO
     * AbsSignal.AbsSensor.AI
     * AbsSignal.AbsSensor.DI
The following formula collects the signal names of the whole model:
    
        =rmos('ModularSystem.Controller.Signals.AbsSignal').intoInject(signal,map| // check if signal is already in map
    	if map.containsKey(signal.$SignalType)then // if yes, then add the signal to the list
    		map.add(signal.$SignalType,map.value(signal.$SignalType).append(signal))
    	else // if not, then add the signal to the map (creates new list)
    		map.add(signal.$SignalType,List{signal})
    	endif
    		,Map{})

The result looks like follows:
    
        [DOÂ»[<<DO>>,<<DO>>],AIÂ»[<<AI>>],DIÂ»[<<DI_1>>,<<DI_2>>,<<DI>>]]

A map with three key-value pairs was formed in which the key is always the signal type and the value is always a list of signals of the signal type.
