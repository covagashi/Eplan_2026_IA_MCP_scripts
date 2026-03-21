# Functions3DFilter

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Functions3DFilter.html

---

Represents data used for filtering [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html) by [DMObjectsFinder](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder.html)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.AbstractDMObjectFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter.html)  
      [Eplan.EplApi.DataModel.StorableObjectsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter.html)  
         [Eplan.EplApi.DataModel.Placements3DFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placements3DFilter.html)  
            **Eplan.EplApi.DataModel.Functions3DFilter**

Syntax

**C#**



public class Functions3DFilter : Placements3DFilter

public ref class Functions3DFilter : public Placements3DFilter


Example

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
| Public Constructor | [Functions3DFilter Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Functions3DFilter~_ctor.html) | Default constructor. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [FunctionCategory](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placements3DFilter~FunctionCategory.html) | Gets/Sets the filter's category (Inherited from [Eplan.EplApi.DataModel.Placements3DFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placements3DFilter.html)) |
| Public Property | [InstallationSpace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placements3DFilter~InstallationSpace.html) | Sets the [Eplan.EplApi.DataModel.E3D.InstallationSpace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.InstallationSpace.html) that [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)s matching the filter must be placed in. (Inherited from [Eplan.EplApi.DataModel.Placements3DFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placements3DFilter.html)) |
| Public Property | [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter~Page.html) | Sets the [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) that [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s matching the filter must be placed on. (Inherited from [Eplan.EplApi.DataModel.StorableObjectsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter.html)) |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placements3DFilter~Parent.html) | Sets the [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) for which all children will be found. (Inherited from [Eplan.EplApi.DataModel.Placements3DFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placements3DFilter.html)) |
| Public Property | [Recursive](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placements3DFilter~Recursive.html) | Gets a value indicating whether [DMObjectsFinder](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder.html) search for children recursively traversing from parent down. (Inherited from [Eplan.EplApi.DataModel.Placements3DFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placements3DFilter.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter~Dispose().html) | Destructor for deterministic finalization of Functions3DFilter object. (Inherited from [Eplan.EplApi.DataModel.AbstractDMObjectFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter.html)) |
| Public Method | [ResetFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter~ResetFilter.html) | Resets the filter. Filter matches all [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s then. (Inherited from [Eplan.EplApi.DataModel.StorableObjectsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter.html)) |
| Public Method | [SetFilteredPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placements3DFilter~SetFilteredPropertyList.html) | Overloaded. Sets the [Eplan.EplApi.DataModel.E3D.Placement3DPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html) that will be used for searching [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html). (Inherited from [Eplan.EplApi.DataModel.Placements3DFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placements3DFilter.html)) |


