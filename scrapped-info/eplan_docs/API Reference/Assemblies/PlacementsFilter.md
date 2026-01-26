# PlacementsFilter

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementsFilter.html

---

This class represents filter for [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s objects.

The PlacementsFilter can be accessed as a property of a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) object or can be used as a parameter for [DMObjectsFinder](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder.html).

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.AbstractDMObjectFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter.html)  
      [Eplan.EplApi.DataModel.StorableObjectsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter.html)  
         **Eplan.EplApi.DataModel.PlacementsFilter**  
            [Eplan.EplApi.DataModel.FunctionsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter.html)  
            [Eplan.EplApi.DataModel.InterruptionPointsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointsFilter.html)  
            [Eplan.EplApi.DataModel.SegmentPlacementsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SegmentPlacementsFilter.html)

Syntax

**C#**



public class PlacementsFilter : StorableObjectsFilter

public ref class PlacementsFilter : public StorableObjectsFilter


Example

**C#**

```
DMObjectsFinder oFinder = new DMObjectsFinder(m_oTestProject);

PlacementsFilter oFilter = new PlacementsFilter();

oFilter.Page = m_oTestProject.Pages[10];

Placement[] oP = oFinder.GetPlacements(oFilter);

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
| Public Constructor | [PlacementsFilter Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementsFilter~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementsFilter~Page.html) | Overridden. Sets the [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) that [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s matching the filter must be placed on. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter~Dispose().html) | Destructor (Inherited from [Eplan.EplApi.DataModel.AbstractDMObjectFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter.html)) |
| Public Method | [ResetFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementsFilter~ResetFilter.html) | Overridden. Resets the filter. Filter matches all [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s then. |
| Public Method | [SetFilteredPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementsFilter~SetFilteredPropertyList.html) | Overloaded. Sets the [PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html) that [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s matching the filter must have. |


