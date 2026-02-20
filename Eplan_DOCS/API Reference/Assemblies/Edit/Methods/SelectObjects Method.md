# SelectObjects Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~SelectObjects.html

---

Selects objects in GED

Syntax

**C#**



public void SelectObjects( 

   string strFullLinkFileName,

   StringCollection objectIds,

   bool bDeselectAll

)

public:

void SelectObjects( 

   String^ strFullLinkFileName,

   StringCollection^ objectIds,

   bool bDeselectAll

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project. The already selected objects will be deselected.

*objectIds*
:   List of Ids of objects to be selected.  
    Note that an object Id MUST have three parts separated with slash: Type/Id/transient flag. Transient flag can have 2 values, 0 means object is persistent, 1 means object is transient. e.g.: 17/142/0. When you get the object Id from `Properties.PROPUSER_DBOBJECTID`, you have to remove the first number (project id) and the first '/' from this string (see example).

*bDeselectAll*
:   Deselect all objects which were already selected.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Is thrown in case of invalid parameters. |
| [System.ApplicationException](#) | The graphics editor interface could not be created. |

Remarks

When passing bDeselectAll as TRUE, the already selected objects will be deselected and the objects passed in as objectIds will be selected.

Example

The following examples shows a method to mark all the motors on a given schematic page.

**C#**

```
StringCollection scFuncIds = new StringCollection();

foreach (Function oFunction in arrFunctions)

{

    //get object id

    string objectId = oFunction.Properties.PROPUSER_DBOBJECTID;

    //get index of first separator

    int idxOfSlash = objectId.IndexOf("/", 1, objectId.Length - 1, StringComparison.InvariantCultureIgnoreCase);

    //cut off value before first separator together with this separator

    string objectIdWithoutProjectId = objectId.Substring(idxOfSlash + 1, (objectId.Length - idxOfSlash - 1));

    //add value to array

    scFuncIds.Add(objectIdWithoutProjectId);

}

//remove selection from all object and then select objects passed as in a list

new Edit().SelectObjects(m_TestProject.ProjectLinkFilePath, scFuncIds, true);

```
