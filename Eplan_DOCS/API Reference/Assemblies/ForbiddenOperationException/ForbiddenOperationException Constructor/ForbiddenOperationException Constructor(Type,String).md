# ForbiddenOperationException Constructor(Type,String)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException~_ctor(Type,String).html

---

Constructor with custom description created with IDS\_ERR\_INVALID\_OPERATION\_FOR\_THIS\_CLASS error message. Should be used for functions which don't make sens for specified objects.

Syntax

**C#**



public ForbiddenOperationException( 

   Type className,

   string functionName

)

public:

ForbiddenOperationException( 

   Type^ className,

   String^ functionName

)


#### Parameters

*className*
:   Class name

*functionName*
:   Function name
