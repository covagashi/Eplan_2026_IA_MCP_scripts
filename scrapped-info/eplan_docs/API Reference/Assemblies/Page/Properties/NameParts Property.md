# NameParts Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~NameParts.html

---

Gets/Sets the name of a page.

Syntax

**C#**



public PagePropertyList NameParts {get; set;}

public:

property PagePropertyList^ NameParts {

   PagePropertyList^ get();

   void set (    PagePropertyList^ value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Cannot set name of the page |

Remarks

Note: When using this property to set a page's name, it is not validated whether the value being set is correct and not yet existing in the project. Also if PAGE\_COUNTER property is not specified, it is NOT set to a default value automatically. (Unlike when using [SetName(PagePropertyList)](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~SetName(PagePropertyList).html) method.) Changing identifying page properties, such as the higher-level function, DOES NOT rename all the DTs for the same higher-level function on the page as it is done when setting a page name in GUI. The property list being set may contain the following properties: · DESIGNATION\_PLANT · DESIGNATION\_SUBPLANT1 · DESIGNATION\_SUBPLANT2 · DESIGNATION\_SUBPLANT3 · DESIGNATION\_LOCATION · DESIGNATION\_SUBLOCATION1 · DESIGNATION\_SUBLOCATION2 · DESIGNATION\_SUBLOCATION3 · DESIGNATION\_SUBLOCATION4 · DESIGNATION\_SUBLOCATION5 · PAGE\_COUNTER · PAGE\_SUBCOUNTERER To check whether a property is a name property, please use PropertyDefinition::IsNamePart. For more information about page name syntax please see chapter 'Dialog Settings: DT syntax check' in Eplan documentation.

Example

- [c#](#i-tab-content-f9ca1542-061c-4a8a-a9ed-f4f3e20833f2)

```
Page pg;

PagePropertyList pagePropList = new PagePropertyList();

pagePropList.DESIGNATION_PLANT = "API_Test";

pagePropList.DESIGNATION_LOCATION = "New_Schematic";

pagePropList.PAGE_COUNTER = 002;

pg.NameParts = pagePropList;
```
