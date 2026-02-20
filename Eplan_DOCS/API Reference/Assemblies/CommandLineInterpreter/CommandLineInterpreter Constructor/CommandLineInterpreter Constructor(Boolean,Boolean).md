# CommandLineInterpreter Constructor(Boolean,Boolean)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.CommandLineInterpreter~_ctor(Boolean,Boolean).html

---

Constructor

Syntax

**C#**



public CommandLineInterpreter( 

   bool bEnableExceptions,

   bool bCollectSysMessages

)

public:

CommandLineInterpreter( 

   bool bEnableExceptions,

   bool bCollectSysMessages

)


#### Parameters

*bEnableExceptions*
:   If this parameter is TRUE, raised exceptions are transmitted to the caller.  
    If this parameter is FALSE, only a boolean value will be returned by calling the Execute method. If this boolean return value is FALSE, this means the action has not succeeded. Otherwise all things are OK.

*bCollectSysMessages*
:   If this parameter is TRUE, system messages will be collected by the Execute method in ActionCallingContext.SysMessages.

Remarks

If this parameter is TRUE, exceptions of the type System::BaseException can be raised.
