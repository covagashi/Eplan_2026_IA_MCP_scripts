# Working with parts

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/WorkingWithParts.html

---

As with other master data, all the information about parts that is required to work independently with a project is stored in the project itself. There are always two parts databases (redundant data management): the central parts database for all projects and the project internal parts database, which only contains parts placed into the project. The central parts database (system parts) can be either an Eplan database (\*.alk) or an SQL database. The following image represents this situation:

Within a project, the parts from the parts project database are referenced, i.e. a part that is used 10 times ' by a  Function, a  Connection, or as a project part by the project itself - is stored only once, and is referenced 10 times in the project (via the part number). Parts data can therefore be easily changed or synchronized via the central parts database.

### How does it work in API?

In the P8 API, the part stored in the internal parts database of the project is represented by the  Eplan.EplApi.DataModel.Article  class. The reference to a particular part on a  Function, a  Connection  or the  Project, is represented by the  Eplan.EplApi.DataModel.ArticleReference  class. You can get the  ArticleReference  objects through the  ArticleReferences  property on the above-mentioned classes.

In order to add a new reference to a part, you can use the  AddArticleReference  methods on  Project,  Function  or  Connection. **Please mind**, that  AddArticleReference  just adds the reference to a part. An  Article  is also added to the object, but only if the referenced part already exists in the system or project database.

In general, articles stored in a P8 project are created explicitly.Therefore you use the method  void Article.Create(string partnr, string variant). This method creates an  Article  object. If there is already a part (Article) with that  partnr  and  variant, an exception will be thrown. After calling the  Create  method, the  Article  object is completely empty. Only the part number and the variant are set, but no other property is filled.

To fill an  Article  with properties of the master data, please use the explicit function  bool Article::LoadFromMasterdata. Using the current part data source, all (the configured) article data of the master data is loaded to the embedded part. If the article (partnr  +  variant) can't be found in the master data,  Article::LoadFromMasterdata  will return "false". On Success "true" is returned.

### Adding Parts and referencing them

The following example shows how to add and reference an  Article  in Project, Function and Connection:

```csharp
Article oArticle = new Article();
     oArticle.Create(oProject, "KUKA.KR30-3", "1");            // An empty Article is created in a Project
     bool bResult = oArticle.LoadFromMasterdata();             // Article is filled with data from system parts database
 
     oProject.AddArticleReference("KUKA.KR30-3", "1", 1);      // Reference to the Article is created on a Project
     oFunction.AddArticleReference("KUKA.KR30-3", "1", 1);     // Reference to the Article is created on a Function
     oConnection.AddArticleReference("KUKA.KR30-3", "1", 1);   // Reference to the Article is created on a Connection

```