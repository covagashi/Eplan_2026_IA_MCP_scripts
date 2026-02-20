# Ordinal Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.InteractionAttribute~Ordinal.html

---

Overload level of interaction.

Syntax

**C#**



public int Ordinal {get; set;}

public:

property int Ordinal {

   int get();

   void set (    int value);

}


Remarks

The new interaction can overwrite an existing interaction which has the same Name and if the ordinal number of the new interaction is higher.
