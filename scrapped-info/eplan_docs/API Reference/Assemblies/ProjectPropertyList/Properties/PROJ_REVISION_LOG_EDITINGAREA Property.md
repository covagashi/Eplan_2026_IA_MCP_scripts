# PROJ_REVISION_LOG_EDITINGAREA Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_LOG_EDITINGAREA(Int32).html

---

Defined working section (from change tracking) # 10195.

Syntax

**C#**



public PropertyValue PROJ_REVISION_LOG_EDITINGAREA( 

   int index

) {get; set;}

public:

property PropertyValue^ PROJ_REVISION_LOG_EDITINGAREA {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

The property is used in projects with revised defined working sections. Shows the defined working section that was completed in a revision, a maximum of 1,000 is possible. This allows you, for example, to view the revision status of the individual defined working sections in the project properties.
