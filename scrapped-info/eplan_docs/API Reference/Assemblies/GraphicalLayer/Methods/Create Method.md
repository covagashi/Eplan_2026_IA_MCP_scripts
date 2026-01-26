# Create Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~Create.html

---

Creates new graphical layer in graphical table. This function calls Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable.AddLayer() and returned object is merged with created object.

Syntax

**C#**



public void Create( 

   GraphicalLayerTable table,

   string name,

   MultiLangString description

)

public:

void Create( 

   GraphicalLayerTable^ table,

   String^ name,

   MultiLangString^ description

)


#### Parameters

*table*
:   Table where layer will be stored. See [Eplan.EplApi.DataModel.Project.LayerTable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~LayerTable.html)

*name*
:   Name of new layer. It can be changed by [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~Name.html) property.

*description*
:   Description of new layer. [Description](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~Description.html) property.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when layer object cannot be associated in table. |
| [System.ArgumentNullException](#) | Thrown when  `table`  is null. |
