# SelectEplanObjects Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.IEplanRemoteClient~SelectEplanObjects.html

---

Selects objects in GED

Syntax

**C#**



EplanResponse SelectEplanObjects( 

   string strFullProjectName,

   StringCollection objectIds,

   bool bDeselectAll

)

EplanResponse^ SelectEplanObjects( 

   String^ strFullProjectName,

   StringCollection^ objectIds,

   bool bDeselectAll

)


#### Parameters

*strFullProjectName*
:   Full link file name of the project. The already selected objects will be deselected.

*objectIds*
:   List of Ids of objects to be selected. Note that an object Id MUST have three parts separated with slash: Type/Id/transient flag. Transient flag can have 2 values, 0 means object is persistent, 1 means object is transient. e.g.: 17/142/0. When you get the object Id from `Properties.PROPUSER_DBOBJECTID`, you have to remove the first number (project id) and the first '/' from this String (see example).

*bDeselectAll*
:   Deselect all objects which were already selected.

Remarks

The already selected objects will be deselected. In which mode this call is executed, synchronously or asynchronously, depends on the SynchronousMode property. Per default all calls are executed asynchronously (except Connect). You can change this behavior by setting the SynchronousMode property to true in order to make synchronous calls. If the call is asynchronous, EPLAN application sends a completed-execution acknowledgment response when the call is completely executed. The property AsyncCallCompleted in EplanResponse is set to true.

Example

The following examples shows a method to mark all the motors on a given schematic page.

**C#**

```
private static void MarkMotorsOnPage(Page page)

{

		DMObjectsFinder dMObjectsFinder = new DMObjectsFinder(page.Project);

		FunctionsFilter functionsFilter = new FunctionsFilter();

		functionsFilter.Page = page;

		functionsFilter.FunctionCategory = FunctionCategory.Motor;

		Function[] functions = dMObjectsFinder.GetFunctions(functionsFilter);

		StringCollection scFuncIds = new StringCollection();

		foreach (Function function in functions)

		{

			String objectId = function.Properties.PROPUSER_DBOBJECTID;

			int idxOfSlash = objectId.IndexOf("/", 1, objectId.Length - 1, StringComparison.InvariantCultureIgnoreCase);

			String objectIdWithoutProjectId = objectId.Substring(idxOfSlash + 1, (objectId.Length - idxOfSlash - 1));

			scFuncIds.Add(objectIdWithoutProjectId);

		}

     // Connect to server via a remoting client

     EplanRemoteClient oClient = new EplanRemoteClient();

     try{       

          oClient.Connect(Environment.MachineName, "60000"); //In this case the Eplan server was started on port 60000

          //Connection is successful then select objects 

		     oClient.SelectObjects(page.Project.ProjectLinkFilePath, scFuncIds, true);

      }

      catch(Exception) 

      {

         // Connection to server failed!

      }

}
```
