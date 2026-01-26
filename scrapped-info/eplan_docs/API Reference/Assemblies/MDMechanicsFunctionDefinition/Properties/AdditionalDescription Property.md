# AdditionalDescription Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDMechanicsFunctionDefinition~AdditionalDescription.html

---

Refers to the Description column in GUI.

Syntax

**C#**



public override MultiLangString AdditionalDescription {get; set;}

public:

property MultiLangString^ AdditionalDescription {

   MultiLangString^ get() override;

   void set (    MultiLangString^ value) override;

}


Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown while setting, if new value is `NULL`. |
