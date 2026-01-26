# Create(Page,String,MultiLangString) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.HyperLink~Create(Page,String,MultiLangString).html

---

Creates the HyperLink object.

Syntax

**C#**



public void Create( 

   Page page,

   string link,

   MultiLangString contents

)

public:

void Create( 

   Page^ page,

   String^ link,

   MultiLangString^ contents

)


#### Parameters

*page*
:   [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) the HyperLink will be placed on.

*link*
:   link path of the hyperlink

*contents*
:   contents of the hyperlink, can be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `page` is `null`. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the HyperLink cannot be created. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the HyperLink has already been created. |
| [Eplan.EplApi.DataModel.InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when given [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) has PageType sets to ExternalDocument. |
