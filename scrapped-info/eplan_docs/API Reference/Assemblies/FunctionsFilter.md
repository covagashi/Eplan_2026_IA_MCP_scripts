# FunctionsFilter

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter.html

---

This class represents filter of [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) and derived classes. The FunctionsFilter can be accessed as a property of a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) object or can be used as a parameter for [DMObjectsFinder](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder.html). Specifying more than one matching criterion for the filter (for example, the page on which the matching functions must be placed and the category of the matching functions) causes the returned functions to match both conditions.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.AbstractDMObjectFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter.html)  
      [Eplan.EplApi.DataModel.StorableObjectsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter.html)  
         [Eplan.EplApi.DataModel.PlacementsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementsFilter.html)  
            **Eplan.EplApi.DataModel.FunctionsFilter**

Syntax

**C#**



public class FunctionsFilter : PlacementsFilter

public ref class FunctionsFilter : public PlacementsFilter


Example

This example shows how to filter functions by category:

**C#**

```


Project myProject = m_oProject; // A valid project

Page myPage = myProject.Pages[0]; // A valid Page object

// Use a filter to get only functions with category 'Motor'

myPage.Filter.FunctionCategory = Eplan.EplApi.Base.Enums.FunctionCategory.Motor;

// Place all functions with category 'Motor' on page myPage

Function[] functions = myPage.Functions;

// Another way to do the same:

// Use a filter to get only functions with category 'Motor'

FunctionsFilter myFunctionsFilter = new FunctionsFilter();

myFunctionsFilter.FunctionCategory = Eplan.EplApi.Base.Enums.FunctionCategory.Motor;

myFunctionsFilter.Page = myPage;

DMObjectsFinder objFinder = new DMObjectsFinder(myProject);

// Place all functions with category 'Motor' on page myPage

functions = objFinder.GetFunctions(myFunctionsFilter);

```

The following example shows how to filter by user-defined properties:

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
| Public Constructor | [FunctionsFilter Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ExactNameMatching](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter~ExactNameMatching.html) | Gets/Sets if the filtered function, when is filtered by name, should be matched exactly, it means that if searched name is only its name' prefix, it is not matching to the filter. Dafault this property is `false`. |
| Public Property | [FunctionCategory](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter~FunctionCategory.html) | Gets/Sets the filter's category |
| Public Property | [IsPlaced](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter~IsPlaced.html) | Gets/Sets if the filtered function should be placed (i.e. should be located on a valid page). |
| Public Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter~Name.html) | Gets/Sets the name that was set to this filter. |
| Public Property | [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter~Page.html) | Overridden. Sets the [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) that [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s matching the filter must be placed on. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter~Dispose().html) | Destructor for deterministic finalization of FunctionFilter object. (Inherited from [Eplan.EplApi.DataModel.AbstractDMObjectFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter.html)) |
| Public Method | [ResetFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter~ResetFilter.html) | Overridden. Resets the filter. Filter matches all [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s then. |
| Public Method | [SetFilteredPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter~SetFilteredPropertyList.html) | Overloaded. Sets the [FunctionBasePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList.html) that [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s matching the filter must have. |
| Public Method | [SetIdentifyingPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter~SetIdentifyingPropertyList.html) | Overloaded. Sets the [FunctionBasePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList.html) that identifies the matching [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s. |


