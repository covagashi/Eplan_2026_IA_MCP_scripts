# AdditionalDescription Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDFunctionTemplatePosition~AdditionalDescription.html

---

Refers to the Description column in GUI.

Syntax

**C#**



public virtual MultiLangString AdditionalDescription {get; set;}

public:

virtual property MultiLangString^ AdditionalDescription {

   MultiLangString^ get();

   void set (    MultiLangString^ value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown while setting, if new value is `NULL`. |
