# ConnectionsFilter

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionsFilter.html

---

This class represents filter for [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html) class. The ConnectionsFilter can be used as a parameter for **Eplan::EplApi::DataModel::DMObjectsFinder:** method. Setting more than one criterion of matching the filter, causes that returned connections must match those conditions.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.AbstractDMObjectFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter.html)  
      **Eplan.EplApi.DataModel.ConnectionsFilter**

Syntax

**C#**



public class ConnectionsFilter : AbstractDMObjectFilter

public ref class ConnectionsFilter : public AbstractDMObjectFilter


Example

**C#**

```
//(...)

DMObjectsFinder oFinder = new DMObjectsFinder(m_oProject);

FunctionsFilter oFuncFilter = new FunctionsFilter();

string strStartFunctionName = "=AP+ST1-XTR";

oFuncFilter.Name = strStartFunctionName;

Function[] arrFuncs = oFinder.GetFunctions(oFuncFilter);

//Assert.IsTrue(arrFuncs.Length > 0, ShowMessage("Could not find function with name: {0} !"), strStartFunctionName);

Function oStartFunc = arrFuncs[0];

//Assert.AreEqual(strStartFunctionName, oStartFunc.Name, ShowMessage("Failed to get proper function !"));

//now find connection for that function

ConnectionsFilter oFilter = new ConnectionsFilter();

oFilter.Function = oStartFunc; //is it start function or end function, does it occur with both ?

//get connections

Connection[] arrConnections = oFinder.GetConnections(oFilter);

//(...)
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
| Public Constructor | [ConnectionsFilter Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionsFilter~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionsFilter~Function.html) | Sets the [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) that [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)s matching the filter must have as the start or the end function. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter~Dispose().html) | Destructor for deterministic finalization of ConnectionsFilter object. (Inherited from [Eplan.EplApi.DataModel.AbstractDMObjectFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AbstractDMObjectFilter.html)) |
| Public Method | [ResetFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionsFilter~ResetFilter.html) | Overridden. Resets the filter. Filter matches all [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)s then. |
| Public Method | [SetFilteredPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionsFilter~SetFilteredPropertyList.html) | Sets the [ConnectionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList.html) that [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)s matching the filter must have. |


