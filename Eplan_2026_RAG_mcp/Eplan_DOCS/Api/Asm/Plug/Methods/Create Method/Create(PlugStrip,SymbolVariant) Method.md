# Create(PlugStrip,SymbolVariant) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Plug~Create(PlugStrip,SymbolVariant).html

---

Creates a Plug object related to a [PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html) given as a parameter. The created plug will get its symbol and function definition from the [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) parameter.

Syntax

**C#**



public void Create( 

   PlugStrip strip,

   SymbolVariant variant

)

public:

void Create( 

   PlugStrip^ strip,

   SymbolVariant^ variant

)


#### Parameters

*strip*
:   A [PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html) where the plug will be located.

*variant*
:   A [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) of the plug.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the Plug object cannot be created. |
| [System.ArgumentNullException](#) | Thrown when any of the parameters is `null`. |
