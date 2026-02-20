# Init(Boolean,MDPartsDatabase) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsMessagesRegisteredEnumerator~Init(Boolean,MDPartsDatabase).html

---

Initializes the enumerator for iterating over the collection of all registered messages in the system.

Syntax

**C#**



public void Init( 

   bool bOnlyLicensed,

   MDPartsDatabase oMDPartsdb

)

public:

void Init( 

   bool bOnlyLicensed,

   MDPartsDatabase^ oMDPartsdb

)


#### Parameters

*bOnlyLicensed*
:   If set to true only messages that are licensed in the actual system will be regarded

*oMDPartsdb*
:   Properties of TemplateMDMessage will be set/get to/from this Parts Database.

Remarks

Automatically used by the constructor of [Eplan::EplApi::MasterData:](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsMessagesRegisteredCollection.html)
