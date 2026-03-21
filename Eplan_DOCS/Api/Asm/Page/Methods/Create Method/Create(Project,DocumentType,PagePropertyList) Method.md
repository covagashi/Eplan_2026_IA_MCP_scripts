# Create(Project,DocumentType,PagePropertyList) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~Create(Project,DocumentType,PagePropertyList).html

---

Creates a new Page object. It is placed in the project under location given as parameters.

Syntax

**C#**



public void Create( 

   Project pProject,

   DocumentTypeManager.DocumentType nType,

   PagePropertyList pNameParts

)

public:

void Create( 

   Project^ pProject,

   DocumentTypeManager.DocumentType nType,

   PagePropertyList^ pNameParts

)


#### Parameters

*pProject*
:   Project the page is assigned to.

*nType*
:   Type of the page

*pNameParts*
:   Parts of name of the page, that determine its location in the project structure.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when valid page cannot be created. |
| [System.ArgumentNullException](#) | Thrown when pProject or pNameParts is null. |
| [NameConflictException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NameConflictException.html) | Thrown when page with  `pNameParts`  name already exists in  `pProject`  . |
| [InvalidPageNameException\_IncorrectParts](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidPageNameException_IncorrectParts.html) | Thrown when entries in  `pNameParts`  contain invalid tag values. |
| [ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the Page has already been created. |

Remarks

To know DeviceTag syntax please see chapter 'Dialog Settings: DT syntax check' in Eplan documentation. The name passed in the pNameParts parameter is validated whether it is correct and not yet existing in the project. Also if PAGE\_COUNTER property is not specified, it is set to a default value automatically. Property list `pNameParts` should contain only name properties, for example : · DESIGNATION\_PLANT · DESIGNATION\_SUBPLANT1 · DESIGNATION\_SUBPLANT2 · DESIGNATION\_SUBPLANT3 · DESIGNATION\_LOCATION · DESIGNATION\_SUBLOCATION1 · DESIGNATION\_SUBLOCATION2 · DESIGNATION\_SUBLOCATION3 · DESIGNATION\_SUBLOCATION4 · DESIGNATION\_SUBLOCATION5 · PAGE\_COUNTER · PAGE\_SUBCOUNTER To check whether a property is a name property, please use PropertyDefinition::IsNamePart.

Example

**C#**

```
PagePropertyList pagePropList = new PagePropertyList();

pagePropList.DESIGNATION_PLANT = "API_Test";

pagePropList.DESIGNATION_LOCATION = "New_Schematic";

pagePropList.PAGE_COUNTER = 002;

Page page = new Page( );

page.Create(project, DocumentTypeManager.DocumentType.Circuit, pagePropList);
```
