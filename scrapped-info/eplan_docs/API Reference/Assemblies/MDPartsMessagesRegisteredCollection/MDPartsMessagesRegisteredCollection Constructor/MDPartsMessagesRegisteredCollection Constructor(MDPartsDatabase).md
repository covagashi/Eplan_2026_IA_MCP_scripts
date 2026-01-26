# MDPartsMessagesRegisteredCollection Constructor(MDPartsDatabase)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsMessagesRegisteredCollection~_ctor(MDPartsDatabase).html

---

Constructor initializes the matching enumerator.

Syntax

**C#**



public MDPartsMessagesRegisteredCollection( 

   MDPartsDatabase oMDPartsdb

)

public:

MDPartsMessagesRegisteredCollection( 

   MDPartsDatabase^ oMDPartsdb

)


#### Parameters

*oMDPartsdb*
:   Properties of TemplateMDMessage will be set/get to/from this PartsDatabase. Can't be null.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Null Database was passed to a parameter. |
| [System.ArgumentException](#) | Invalid Database was passed to a parameter. |
