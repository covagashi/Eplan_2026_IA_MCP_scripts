# Create(Page,MultiLangString,Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Text~Create(Page,MultiLangString,Double).html

---

Creates the Text object.

Syntax

**C#**



public virtual void Create( 

   Page page,

   MultiLangString contents,

   double textHeight

)

public:

virtual void Create( 

   Page^ page,

   MultiLangString^ contents,

   double textHeight

)


#### Parameters

*page*
:   [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) the Text will be placed on.

*contents*
:   [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html) containing text to display.

*textHeight*
:   Height of the Text.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `page` is `null`. |
| [System.ArgumentNullException](#) | Thrown when `contents` is `null`. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the Text cannot be created. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the Text has already been created. |
| [Eplan.EplApi.DataModel.IncorrectObjectTypeException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IncorrectObjectTypeException.html) | Thrown when function is invoked with object of higher class. |
| [Eplan.EplApi.DataModel.InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when given [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) has PageType sets to ExternalDocument. |
