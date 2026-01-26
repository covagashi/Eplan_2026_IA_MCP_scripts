# Article

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html

---

This class represents articles in the [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html).

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)  
      **Eplan.EplApi.DataModel.Article**

Syntax

**C#**



public class Article : StorableObject

public ref class Article : public StorableObject


Example

The following example shows how to use class Article.

**C#**

```


foreach (Article oArticle in m_oTestProject.Articles)

{

    if ("BECK.KL2012" == oArticle.PartNr)

    {

        if (!oArticle.Properties.ARTICLE_DEPTH.IsEmpty)

            Console.Out.WriteLine("ARTICLE_DEPTH : " + oArticle.Properties.ARTICLE_DEPTH);

        if (!oArticle.Properties.ARTICLE_VARIANT.IsEmpty)

            Console.Out.WriteLine("ARTICLE_VARIANT : " + oArticle.Properties.ARTICLE_VARIANT);

        foreach (int nIndex in oArticle.Properties.ARTICLE_FREE_DATA_DESCRIPTION.Indexes)

            Console.Out.WriteLine("ARTICLE_FREE_DATA_DESCRIPTION[" + nIndex + "] : " + oArticle.Properties.ARTICLE_FREE_DATA_DESCRIPTION[nIndex]);

        foreach (int nIndex in oArticle.Properties.ARTICLE_FREE_DATA_UNIT.Indexes)

            Console.Out.WriteLine("ARTICLE_FREE_DATA_UNIT[" + nIndex + "] : " + oArticle.Properties.ARTICLE_FREE_DATA_UNIT[nIndex]);

        foreach (int nIndex in oArticle.Properties.ARTICLE_FREE_DATA_VALUE.Indexes)

            Console.Out.WriteLine("ARTICLE_FREE_DATA_VALUE[" + nIndex + "] : " + oArticle.Properties.ARTICLE_FREE_DATA_VALUE[nIndex]);

    }

}

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Article Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ArticleAccessories](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~ArticleAccessories.html) | Returns the list of the accessories from the article. |
| Public Property | [ArticleAssemblies](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~ArticleAssemblies.html) | Returns an array of [Article.Assembly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article+Assembly.html) objects representing parts of an assembly. |
| Public Property | [ArticleModules](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~ArticleModules.html) | Returns an array of [Article.Module](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article+Module.html) objects representing module items. Array contains a lists of subparts structured by device tag (DT). |
| Public Property | [ConnectionPointsInfo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~ConnectionPointsInfo.html) | Connection point pattern defined for this article. Returns `null` if article does not contain connection pattern. |
| Public Property | [CrossReferencedObjectsAll](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~CrossReferencedObjectsAll.html) | Returns an array of objects cross-referenced with this object (i.e. having the same name - in case of functions - or otherwise associated) (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DatabaseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html) | Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsAssembly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~IsAssembly.html) | Represents this article an assembly. |
| Public Property | [IsLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsLocked.html) | Determines if the the StorableObject is locked.  The StorableObject is locked when it was explicitly or implicitly locked. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsReadOnly.html) | Determines if StorableObject is read-only (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html) | Determines if the the StorableObject is transient.  The StorableObject is transient when it was created by default constructor and:  it is a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),  it is a [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsValid.html) | Determines if StorableObject is correct database object and is not deleted. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [ObjectIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html) | Returns the object identifier as number. The number is unique for all objects of this type. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [PartNr](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~PartNr.html) | Returns article's part number. |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Project.html) | Returns the project to which the StorableObject belongs. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~Properties.html) | .NET Property enabling access to P8 properties of the Article object. |
| Public Property | [TypeIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TypeIdentifier.html) | Returns the type of the object as number. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [VariantNr](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~VariantNr.html) | Returns article's variant number. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddModule](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~AddModule.html) | Overloaded. Creates copy of existing module and adds it to article. |
| Public Method | [Create](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~Create.html) | Creates a Article in Project with the specified strPartnr and strVariant. |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor for deterministic finalization of Article object. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [LoadFromMasterdata](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~LoadFromMasterdata.html) | Fills the Article with data from the system parts database |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~Remove.html) | Removes the article from the [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html). |
| Public Method | [RemoveModule](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~RemoveModule.html) | Removes module from article. |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |


