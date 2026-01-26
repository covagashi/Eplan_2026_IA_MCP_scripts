# PrjMessagesRegisteredCollection Constructor(Project)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesRegisteredCollection~_ctor(Project).html

---

Constructor. initializes the matching enumerator.

Syntax

**C#**



public PrjMessagesRegisteredCollection( 

   Project oProject

)

public:

PrjMessagesRegisteredCollection( 

   Project^ oProject

)


#### Parameters

*oProject*
:   Properties of ElectroMessage will be set/get to/from this Project. Can't be null.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Null Project was passed to a parameter. |
| [System.ArgumentException](#) | Invalid Project was passed to a parameter. |
