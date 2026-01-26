# MDPartsMessagesRegisteredCollection Constructor(Boolean,MDPartsDatabase)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsMessagesRegisteredCollection~_ctor(Boolean,MDPartsDatabase).html

---

Constructor initializes the matching enumerator.

Syntax

**C#**



public MDPartsMessagesRegisteredCollection( 

   bool bOnlyLicensed,

   MDPartsDatabase oMDPartsdb

)

public:

MDPartsMessagesRegisteredCollection( 

   bool bOnlyLicensed,

   MDPartsDatabase^ oMDPartsdb

)


#### Parameters

*bOnlyLicensed*
:   If set to true only messages that are licensed in the actual system will be regarded

*oMDPartsdb*
:   Properties of TemplateMDMessage will be set/get to/from this Database. Can't be null.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Null Database was passed to a parameter. |
| [System.ArgumentException](#) | Invalid Database was passed to a parameter. |
