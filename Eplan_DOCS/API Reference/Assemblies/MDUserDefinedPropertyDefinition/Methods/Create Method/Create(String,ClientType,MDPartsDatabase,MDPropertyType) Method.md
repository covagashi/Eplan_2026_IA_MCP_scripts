# Create(String,ClientType,MDPartsDatabase,MDPropertyType) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1731.html

---

Creates new property definition

Syntax

**C#**



public static MDUserDefinedPropertyDefinition Create( 

   string strIdentifyingName,

   MDUserDefinedPropertyDefinition.Enums.ClientType nClient,

   MDPartsDatabase partsDatabase,

   MDPropertyDefinition.MDPropertyType fieldType

)

public:

static MDUserDefinedPropertyDefinition^ Create( 

   String^ strIdentifyingName,

   MDUserDefinedPropertyDefinition.Enums.ClientType nClient,

   MDPartsDatabase^ partsDatabase,

   MDPropertyDefinition.MDPropertyType fieldType

)


#### Parameters

*strIdentifyingName*
:   Identifying name of a property.

*nClient*
:   Possible user of a property definition.

*partsDatabase*
:   Parts database where a property will be created.

*fieldType*
:   Field type of this property definition.
