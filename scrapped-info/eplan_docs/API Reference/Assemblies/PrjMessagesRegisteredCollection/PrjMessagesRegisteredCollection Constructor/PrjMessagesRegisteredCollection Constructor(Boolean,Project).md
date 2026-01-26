# PrjMessagesRegisteredCollection Constructor(Boolean,Project)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesRegisteredCollection~_ctor(Boolean,Project).html

---

Constructor. initializes the matching enumerator.

Syntax

**C#**



public PrjMessagesRegisteredCollection( 

   bool bOnlyLicensed,

   Project oProject

)

public:

PrjMessagesRegisteredCollection( 

   bool bOnlyLicensed,

   Project^ oProject

)


#### Parameters

*bOnlyLicensed*
:   If set to true only messages that are licensed in the actual system will be regarded

*oProject*
:   Properties of ElectroMessage will be set/get to/from this Project. Can't be null.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Null Project was passed to a parameter. |
| [System.ArgumentException](#) | Invalid Project was passed to a parameter. |
