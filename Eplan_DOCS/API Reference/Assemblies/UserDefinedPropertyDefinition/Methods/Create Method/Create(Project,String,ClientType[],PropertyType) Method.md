# Create(Project,String,ClientType[],PropertyType) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic463.html

---

Creates new property definition.

Syntax

**C#**



public static UserDefinedPropertyDefinition Create( 

   Project pProject,

   string strName,

   UserDefinedPropertyDefinition.Enums.ClientType[] nClients,

   PropertyDefinition.PropertyType pType

)

public:

static UserDefinedPropertyDefinition^ Create( 

   Project^ pProject,

   String^ strName,

   array<UserDefinedPropertyDefinition.Enums.ClientType>^ nClients,

   PropertyDefinition.PropertyType pType

)


#### Parameters

*pProject*
:   Project to which definition will be assigned.

*strName*
:   Identifying name of the property.

*nClients*
:   Possible usages of user-defined property definition.

*pType*
:   Type of property. There are five accepted types: `MultiLangString`, `String`, `Bool`, `Double` and `Long`.

#### Return Value

Returns an object which represents new property definition or `null` if property definition can't be created.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when parameter is `null`. |
| [System.ArgumentException](#) | Thrown when identifying name is `empty` or when for parameter `pType` other value is passed than one from accepted ones. |
| [PropertyAlreadyExistsException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyAlreadyExistsException.html) | Thrown when property definition with this name already exists in the project. |
| [IncorrectNameFormatException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IncorrectNameFormatException.html) | Thrown when identifying name is invalid. |
| [ProjectLockingException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectLockingException.html) | Thrown when project can't be locked in exclusive mode. |

Remarks

The identifying name for the property must be unique. We recommend that you start the name with your company code. It may contain upper-case and lower-case letters, numbers and the special characters ".-\_&". A number can't be at the beginning of the name. At least one point must be used in the name; however, the point must not be at the beginning or end of the name. The string "EPLAN" at the beginning is not permitted either. Points within the name are treated as substructures and create a sub-level in the tree. For `pType` parameter there are five accepted types: `MultiLangString`, `String`, `Bool`, `Double` and `Long`.
