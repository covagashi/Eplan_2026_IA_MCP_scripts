# GetAllPotentialsWithSameName Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PotentialVerification~GetAllPotentialsWithSameName.html

---

Returns all potentials of the project with the same name. Can be called within the Execute function.

Syntax

**C#**



public void GetAllPotentialsWithSameName( 

   Placement oPotential,

   ref ArrayList colPotentials

)

public:

void GetAllPotentialsWithSameName( 

   Placement^ oPotential,

   ArrayList^% colPotentials

)


#### Parameters

*oPotential*
:   The potential for which all other potentials with the same name are to be searched.

*colPotentials*
:   The list of results giving all potentials with the same name.

Remarks

This function uses an internal buffer mechanism and is therefore very quick when called several times in a check routine.
