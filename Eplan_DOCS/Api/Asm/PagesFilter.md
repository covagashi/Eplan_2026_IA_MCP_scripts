# PagesFilter

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagesFilter.html

---

This class represents filter of [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and derived from it classes.

The PagesFilter can be accessed as a property of a [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) object or can be used as a parameter for [DMObjectsFinder](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder.html).

Setting more than one criterion of matching the filter (for example [Page.PageType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PageType.html) and [Page.Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~Name.html)), causes that returned pages must match both conditions.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.AbstractDMObjectFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter.html)  
      **Eplan.EplApi.DataModel.PagesFilter**

Syntax

**C#**



public class PagesFilter : AbstractDMObjectFilter

public ref class PagesFilter : public AbstractDMObjectFilter


Example

**C#**

```
Project proj;  //a valid project

DMObjectsFinder oFinder = new DMObjectsFinder(proj);

PagesFilter oPagesFilter = new PagesFilter();

oPagesFilter.Name = @"=AP+ST1";

oPagesFilter.DocumentType = DocumentTypeManager.DocumentType.Frame;

Page[] oPages = oFinder.GetPages(oPagesFilter); //now we have all pages with names starting with "=AP+ST1" and type with "DocumentType.Frame"
```

The following example shows how to filter by user-defined properties

**C#**

```


Project myProject = m_oProject; // A valid project

Page myPage = myProject.Pages[0]; // A valid Page object

// Define test property

MultiLangString mlsTestValue = new MultiLangString();

mlsTestValue.AddString(ISOCode.Language.L_de_DE, "Test043c");

string strPropertyIdentyfingName = "Page.Test043c";

UserDefinedPropertyDefinition oUDPD = UserDefinedPropertyDefinition.Create(myProject, strPropertyIdentyfingName, UserDefinedPropertyDefinition.Enums.ClientType.Page);

// Set test property on myPage

myPage.Properties[strPropertyIdentyfingName] = mlsTestValue;

// Search page with property value

DMObjectsFinder objFinder = new DMObjectsFinder(myProject);

PagesFilter pagesFilter = new PagesFilter();

PagePropertyList pagePropertyList = new PagePropertyList();

AnyPropertyId anyPropertyId = new AnyPropertyId(myProject, strPropertyIdentyfingName);

pagePropertyList[anyPropertyId] = mlsTestValue;

pagesFilter.SetFilteredPropertyList(pagePropertyList);

Page[] arrPages1 = objFinder.GetPages(pagesFilter);

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [PagesFilter Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagesFilter~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [DocumentType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagesFilter~DocumentType.html) | Returns the [Page.PageType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PageType.html) that was set to this filter. |
| Public Property | [ExactNameMatching](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagesFilter~ExactNameMatching.html) | Gets if the filtered function, when is filtered by name, should be matched exactly, it means that if searched name is only its name' prefix, it is not matching to the filter. |
| Public Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagesFilter~Name.html) | Returns the name that was set to this filter. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter~Dispose().html) | Destructor for deterministic finalization of PagesFilter object. (Inherited from [Eplan.EplApi.DataModel.AbstractDMObjectFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter.html)) |
| Public Method | [ResetFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagesFilter~ResetFilter.html) | Overridden. Resets the filter. Filter matches all [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)s then. |
| Public Method | [SetFilteredPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagesFilter~SetFilteredPropertyList.html) | Sets the [PagePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList.html) that [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)s matching the filter must have. |


