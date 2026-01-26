# Search

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search.html

---

Class providing functionality to search within a project.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.Search**

Syntax

**C#**



[DefaultMember("Setting")]

public class Search

[DefaultMember("Setting")]

public ref class Search


Example

The following example shows how to use class Search.

**C#**

```
Search oSearch = new Search();

// Set settings which will influence the search result

oSearch[Search.Settings.CaseSensitive] = false;

oSearch[Search.Settings.Texts] = false;

oSearch[Search.Settings.DeviceTag] = true;

oSearch[Search.Settings.AllProperties] = false;

oSearch[Search.Settings.Texts] = false;

oSearch[Search.Settings.PageData] = false;

oSearch[Search.Settings.ProjectData] = false;

oSearch[Search.Settings.GraphicPages] = false;

oSearch[Search.Settings.EvalutionPages] = false;

oSearch[Search.Settings.NotPlaced] = false;

oSearch[Search.Settings.LogicPages] = true;

Project oProject = new ProjectManager().OpenProject("$(MD_PROJECTS)\\EPLAN_Sample_Project.elk");

//clear active search result list

oSearch.ClearSearchDB(oProject);

string textToFind = "EB3*";

//Search the project

oSearch.Project(oProject, textToFind);		

//Get search results

StorableObject[] arrObjects = oSearch.GetAllSearchDBEntries(oProject);

//Replace text in a searched objects.

string strSearchString = "EB3";

string strReplaceString = "EBCD3";

oSearch.Project(m_oProject, strSearchString);

StorableObject[] arrObjects = oSearch.GetAllSearchDBEntries(m_oProject);

oSearch.Replace(arrObjects, strSearchString, strReplaceString);
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Search Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~_ctor.html) | Default constructor |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Setting](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~Setting.html) | Gets/Sets whether the specified setting of a search is enabled |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddRelatedObjectsToGotoDB](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~AddRelatedObjectsToGotoDB.html) | Adds cross-referenced objects to the goto results list. |
| Public Method | [AddToSearchDB](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~AddToSearchDB.html) | Overloaded. Adds objects to the currently active list of search results. |
| Public Method | [ClearSearchDB](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~ClearSearchDB.html) | Clears the list of search results. |
| Public Method | [Dispose](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~Dispose().html) | Destructor |
| Public Method | [GetAllSearchDBEntries](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~GetAllSearchDBEntries.html) | \Returns all objects in a list of search results. |
| Public Method | [GetSearchDBEntries](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~GetSearchDBEntries.html) | Returns objects from a list of search results. |
| Public Method | [Page](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~Page.html) | Overloaded. Searches on the specified page for a search string. The search settings will influence the result. The found object will be written to the active list of results. |
| Public Method | [Project](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~Project.html) | Overloaded. Searches on the specified project for a search string. The search settings will influence the result. The found object will be written to the active list of results. |
| Public Method | [Replace](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~Replace.html) | Replaces text in a searched objects. |


