# ForbiddenOperationException Constructor(Type,Type)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException~_ctor(Type,Type).html

---

Constructor with custom description created with IDS\_ERR\_INVALID\_CLASS\_INHIERANCE\_FOR\_PROPERTYLIST error message. Should be used for PropertyLists members for objects of TerminalStrip and PlugStrip.

Syntax

**C#**



public ForbiddenOperationException( 

   Type functionType,

   Type objectType

)

public:

ForbiddenOperationException( 

   Type^ functionType,

   Type^ objectType

)


#### Parameters

*functionType*
:   Type of class from which Properties member was called.

*objectType*
:   Type of class from which object was created.
