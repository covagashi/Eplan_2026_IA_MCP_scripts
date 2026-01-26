# Navigating the project data

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/NavigatingTheDatamodel.html

---

There are two distinct methods of navigating through the Eplan project. The most common is to use the navigation properties which you can find on each data model object. In addition to that, there is the  DMObjectsFinder  class. By its methods, you can retrieve filtered lists (arrays) of certain objects in a project.

### Navigating through properties

Regardless of the underlying implementation of Eplan, the entire data model can be seen as a graph, with one to many and many to many relationships between the various object types in the graph. For example, a project has a one-to-many relationship with its pages. These relationships can be thought of as if they were simple basic arrays. Each of the objects of the Eplan data model have a set of properties, which return such arrays of dependant objects, as you can see in the topic "[Data model overview](DataModelHierarchyOverview.html)".

One of the most common requirements of a program is to loop through all of the objects in an array performing some function or other on each element. As an example, the class  Eplan.EplApi.DataModel.Page  has the following navigation properties, with each of which you can loop over a different collection of objects:

- AllFirstLevelPlacements
- AllGraphicalPlacements
- AllPlacements
- BoxedDevices
- Functions
- PLCs
- PlugStrips
- TerminalStrips

There are also navigational properties with a one-to-one relationship, like  Page.Project.

The following code snippet shows how to loop over the functions on a page and get the name of the function:

**C#**
```csharp
// Get an array with all functions on the page

Function[] arrFuncs = oPage.Functions;

// Loop over the functions and get their names

foreach(Function oF in arrFuncs)

{

    string sName = oF.Name;

    // Do something with the Name

}

For Each oF In  arrFuncs

Next
```

You can even filter these lists before getting them. The following example sets a filter to get only the functions that have the function category "PLUG".

**C#**
```csharp
// Set filter category to "PLUG"

oPage.Filter.resetFilter();

oPage.Filter.Category = Function.Enums.Category.PLUG;

// Get all functions filtered by category=PLUG

Function[] arrFuncs = oPage.Functions;

foreach(Function oF in arrFuncs)

{

    string sPlugName = oF.Name;

    // Do something with the Name

}

oPage.Filter.resetFilter()

oPage.Filter.Category = Function.Enums.Category.PLUG

For Each oF In  arrFuncs

Next
```

Please mind that using navigation properties in order to set properties of an object in a nested way (e.g.  oRectangle.Pen.ColorId = 5) will not work. In the example you need to first get the  Pen  object from the rectangle and then change the color ID and afterwards set the changed  Pen  object back to the  Rectangle  class.

### DMObjectsFinder

The  DMObjectsFinder  object is always initialized with a project. Starting with the project, it can get nearly any list of objects of a given type. Before getting the lists, they can be filtered by different means like a distinct set of properties. The following example gets all functions with a given device tag ("name"):

**C#**
```csharp
string strFuncName = "=AP+PT1-X4";

// Initialize the DMObjectsFinder with a project

DMObjectsFinder oFinder = new DMObjectsFinder(m_oProject);

FunctionsFilter oFunctionsFilter = new FunctionsFilter();

oFunctionsFilter.ExactNameMatching = true;

oFunctionsFilter.Name = strFuncName;

// Get function with given name from project

Function[] arrFuncs = oFinder.GetFunctions(oFunctionsFilter);

foreach(Function oF in arrFuncs)

{

    Console.Out.WriteLine("Function name: '{0}'", oF.Name);

}

oFunctionsFilter.ExactNameMatching = True

oFunctionsFilter.Name = strFuncName

For Each oF In  arrFuncs

   Console.Out.WriteLine("Function name: '{0}'", oF.Name)

Next oF
```

### Search class

The  Eplan.EplApi.HEServices.Search  class offers another way for finding objects in a project. The class corresponds to the dialogs Find > Find... and Find > Show Results... in the GUI of Eplan. As in this dialogs, you have two result lists to store your search results.

Using this class, you can search for any string in a specified range of objects. The following example demonstrates the usage of the  Search  class.

**C#**
```csharp
Search oSearch = new Search();

// Set all needed settings

oSearch[Search.Settings.CaseSensitive] = false;

oSearch[Search.Settings.WholeTexts] = false;

oSearch[Search.Settings.DeviceTag] = true;

oSearch[Search.Settings.AllProperties] = false;

oSearch[Search.Settings.Texts] = false;

oSearch[Search.Settings.PageData] = false;

oSearch[Search.Settings.ProjectData] = false;

oSearch[Search.Settings.GraphicPages] = false;

oSearch[Search.Settings.EvalutionPages] = false;

oSearch[Search.Settings.NotPlaced] = false;

oSearch.ClearSearchDB(oProject);

if (oPage != null)

{

    // Either search in a page...

    oSearch.Page(oPage, Name);

}

else

{

    // ... or search the complete project

    oSearch.Project(oProject, Name);

}

StorableObject[] oResults = oSearch.GetAllSearchDBEntries(oProject);

oSearch.SearchDatabaseNr = 0

oSearch.ClearSearchDB(oProject, 0)

oSearch(Search.Settings.AllProperties) = True

oSearch(Search.Settings.CaseSensitive) = False

oSearch(Search.Settings.DeviceTag) = True

oSearch(Search.Settings.LogicPages) = True

oSearch(Search.Settings.GraphicPages) = False

oSearch(Search.Settings.EvalutionPages) = False

oSearch(Search.Settings.NotPlaced) = False

oSearch(Search.Settings.WholeTexts) = False

oSearch(Search.Settings.PageData) = True

oSearch(Search.Settings.ProjectData) = True

oSearch.Project(oProject, txtSearch.Text)
```