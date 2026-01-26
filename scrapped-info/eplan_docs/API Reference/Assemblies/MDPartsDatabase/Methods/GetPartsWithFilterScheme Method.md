# GetPartsWithFilterScheme Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetPartsWithFilterScheme.html

---

Gets parts using the filter from GUI.

Syntax

**C#**



public MDPart[] GetPartsWithFilterScheme( 

   string strGUIFilter

)

public:

array<MDPart^>^ GetPartsWithFilterScheme( 

   String^ strGUIFilter

)


#### Parameters

*strGUIFilter*
:   Filter scheme that is visible in window 'Parts management'

Remarks

If scheme-name is empty, the current filter scheme will be used (excluding 'no-filter' scheme). If scheme-name is null, the method returns elements that are visible if no filter scheme is used.
