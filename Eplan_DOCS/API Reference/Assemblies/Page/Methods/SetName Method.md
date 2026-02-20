# SetName Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~SetName(PagePropertyList).html

---

Sets the name of the page. Name parts should be given in the PagePropertyList.

Syntax

**C#**



public void SetName( 

   PagePropertyList pNameParts

)

public:

void SetName( 

   PagePropertyList^ pNameParts

)


#### Parameters

*pNameParts*
:   New name for the page

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Cannot set name of the page |
| [System.ArgumentNullException](#) | Thrown when `pNameParts` is `null`. |
| [NameConflictException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NameConflictException.html) | Thrown when page with `pNameParts` name already exists in `pProject` . |
| [InvalidPageNameException\_IncorrectParts](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidPageNameException_IncorrectParts.html) | Thrown when entries in `pNameParts` contain invalid tag values. |

Remarks

To know DeviceTag syntax please see chapter 'Dialog Settings: DT syntax check' in Eplan documentation. The name passed in the pNameParts parameter is validated whether it is correct and not yet existing in the project. Also if PAGE\_COUNTER property is not specified, it is set to a default value automatically.

Example

- [c#](#i-tab-content-2da48ed3-f886-4580-b737-6de227981637)

```
PagePropertyList pagePropList = new PagePropertyList();

pagePropList.DESIGNATION_PLANT = "API_Test";

pagePropList.DESIGNATION_LOCATION = "New_Schematic";

pagePropList.PAGE_COUNTER = 002;

page.SetName(pagePropList);
```
