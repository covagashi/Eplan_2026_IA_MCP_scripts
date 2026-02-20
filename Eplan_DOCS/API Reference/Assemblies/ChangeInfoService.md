# ChangeInfoService

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeInfoService.html

---

This class contains methods for activating and deactivating change info handling.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.ChangeInfoService**

Syntax

**C#**



public class ChangeInfoService

public ref class ChangeInfoService


Example

Setting .ArticleTimeStampActive

**C#**

```
using (var changeInfoService = new ChangeInfoService { ArticleTimeStampActive = false })

{

    part.Properties.PART_LASTCHANGE_DATE = new DateTime(1977, 4, 26);

    part.Properties.PART_LASTCHANGE_USER = "TEST_USER";

    part.Properties.ARTICLE_DESCR1 = "test_123";

}

//set properties with 'normal' timestamp settings. Will set automatically current time and user

part.Properties.PART_LASTCHANGE_DATE = new DateTime(1977, 4, 26);

part.Properties.PART_LASTCHANGE_USER = "TEST_USER";

part.Properties.ARTICLE_DESCR1 = "test_123";

```

Setting .ChangeAndCreateInfoUpdateForPage

**C#**

```
//deactivate automatic change/create information update

using (var changeInfoService = new ChangeInfoService { ChangeAndCreateInfoUpdateForPage = false })

{

    //make artificial change just to check modification date and user

    var text1 = new Eplan.EplApi.DataModel.Graphics.Text();

    text1.Create(page, "", 10.0);

    text1.Remove();

    //output changes

    Console.WriteLine(page.Properties.PAGE_LASTAUTOMODIFICATIONDATE.ToString());

    Console.WriteLine(page.Properties.PAGE_LASTAUTOMODIFICATIONTIME.ToString());

    Console.WriteLine(page.Properties.PAGE_LASTMODIFICATOR.ToString());

}

var text2 = new Eplan.EplApi.DataModel.Graphics.Text();

text2.Create(page, "", 10.0);

text2.Remove();

//output changes

Console.WriteLine(page.Properties.PAGE_LASTAUTOMODIFICATIONDATE.ToString());

Console.WriteLine(page.Properties.PAGE_LASTAUTOMODIFICATIONTIME.ToString());

Console.WriteLine(page.Properties.PAGE_LASTMODIFICATOR.ToString());

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [ChangeInfoService Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeInfoService~_ctor.html) | Constructor. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Active](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeInfoService~Active.html) | Activate or deactivate change info handling. |
| Public Property | [ArticleTimeStampActive](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeInfoService~ArticleTimeStampActive.html) | Activate or deactivate article time stamp handling. |
| Public Property | [AutoPageChangedFlag](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeInfoService~AutoPageChangedFlag.html) | Activate or deactivate AUTOPAGECHANGED info handling. |
| Public Property | [ChangeAndCreateInfoUpdateForPage](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeInfoService~ChangeAndCreateInfoUpdateForPage.html) | Activate or deactivate automatic change/create information update for a page. |
| Public Property | [ConnectionDirtyActive](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeInfoService~ConnectionDirtyActive.html) | Activate or deactivate connection dirty bit handling. |
| Public Property | [Obj2PageActive](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeInfoService~Obj2PageActive.html) | Activate or deactivate change info handling if object belongs to page. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeInfoService~Dispose().html) | Destructor |
| Public Method | [RestoreOperationMode](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeInfoService~RestoreOperationMode.html) | Restore previous operation mode. |
| Public Method | [SetActive](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeInfoService~SetActive.html) | Activate or deactivate change info handling. Helper will switch mode automatically back due to destruction. |
| Public Method | [SetAutoPageChangedFlag](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeInfoService~SetAutoPageChangedFlag.html) | Activate or deactivate AUTOPAGECHANGED change info handling. Helper will switch mode automatically back due to destruction. |
| Public Method | [SetChangeAndCreateInfoUpdateForPage](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeInfoService~SetChangeAndCreateInfoUpdateForPage.html) | Activate or deactivate automatic change/create information update for a page. Helper will switch mode automatically back due to destruction. |
| Public Method | [SetConnectionDirtyActive](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeInfoService~SetConnectionDirtyActive.html) | Activate or deactivate connection dirty bit handling. Helper will switch mode automatically back due to destruction. |
| Public Method | [SetObj2PageActive](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeInfoService~SetObj2PageActive.html) | Activate or deactivate change info handling if object belongs to page. Helper will switch mode automatically back due to destruction. |


