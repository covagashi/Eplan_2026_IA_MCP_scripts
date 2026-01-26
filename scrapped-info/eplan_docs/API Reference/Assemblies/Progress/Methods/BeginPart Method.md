# BeginPart Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress~BeginPart.html

---

Starts a new segment. All parallel segments should result in a sum of 100%.

Syntax

**C#**



public void BeginPart( 

   double dPercentageNeeded,

   string strSegmentName

)

public:

void BeginPart( 

   double dPercentageNeeded,

   String^ strSegmentName

)


#### Parameters

*dPercentageNeeded*
:   Percentage value of using progress bar (or parent segment) in this segment.

*strSegmentName*
:   Name for this segment
