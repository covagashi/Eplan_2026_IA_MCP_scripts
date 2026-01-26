# PlanningSegmentsFilter

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlanningSegmentsFilter.html

---

This class represents filter for [Eplan.EplApi.DataModel.Planning.SegmentDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition.html)s objects.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.AbstractDMObjectFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter.html)  
      [Eplan.EplApi.DataModel.StorableObjectsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter.html)  
         **Eplan.EplApi.DataModel.PlanningSegmentsFilter**

Syntax

**C#**



public class PlanningSegmentsFilter : StorableObjectsFilter

public ref class PlanningSegmentsFilter : public StorableObjectsFilter


Example

**C#**

```
DMObjectsFinder oFinder = new DMObjectsFinder(m_oTestProject);

StorableObjectsFilter oFilter = new StorableObjectsFilter();

oFilter.Page = m_oTestProject.Pages[10];

StorableObject[] oSO = oFinder.GetStorableObjects(oFilter);

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
| Public Constructor | [PlanningSegmentsFilter Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlanningSegmentsFilter~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlanningSegmentsFilter~Name.html) | Value compared with property DMPLAOBJECT\_FULLDESIGNATION while searching for planning segments. |
| Public Property | [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter~Page.html) | Sets the [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) that [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s matching the filter must be placed on. (Inherited from [Eplan.EplApi.DataModel.StorableObjectsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter~Dispose().html) | Destructor (Inherited from [Eplan.EplApi.DataModel.AbstractDMObjectFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter.html)) |
| Public Method | [ResetFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlanningSegmentsFilter~ResetFilter.html) | Overridden. Resets the filter. Filter matches all [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s then. |
| Public Method | [SetFilteredPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlanningSegmentsFilter~SetFilteredPropertyList.html) | Overloaded. Sets the [Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList.html) that [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)s matching the filter must have. |


