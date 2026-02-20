# StorableObjectsFilter

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter.html

---

This class represents filter for [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s objects.

The StorableObjectsFilter can be accessed as a property of a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) object or can be used as a parameter for [DMObjectsFinder](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder.html).

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.AbstractDMObjectFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter.html)  
      **Eplan.EplApi.DataModel.StorableObjectsFilter**  
         [Eplan.EplApi.DataModel.Placements3DFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placements3DFilter.html)  
         [Eplan.EplApi.DataModel.PlacementsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementsFilter.html)  
         [Eplan.EplApi.DataModel.PlanningSegmentsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlanningSegmentsFilter.html)  
         [Eplan.EplApi.DataModel.SegmentDefinitionsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SegmentDefinitionsFilter.html)  
         [Eplan.EplApi.DataModel.SegmentTemplatesFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SegmentTemplatesFilter.html)

Syntax

**C#**



public class StorableObjectsFilter : AbstractDMObjectFilter

public ref class StorableObjectsFilter : public AbstractDMObjectFilter


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
| Public Constructor | [StorableObjectsFilter Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter~Page.html) | Sets the [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) that [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s matching the filter must be placed on. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter~Dispose().html) | Destructor (Inherited from [Eplan.EplApi.DataModel.AbstractDMObjectFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter.html)) |
| Public Method | [ResetFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter~ResetFilter.html) | Overridden. Resets the filter. Filter matches all [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s then. |
| Public Method | [SetFilteredPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter~SetFilteredPropertyList.html) | Sets the [StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html) that [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s matching the filter must have. |


