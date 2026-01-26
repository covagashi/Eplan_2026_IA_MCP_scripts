# Place Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Place.html

---

Places the function onto the given page, in the given location

Syntax

**C#**



public Function Place( 

   Page page,

   PointD location,

   bool copyProperties,

   bool copyAlsoNameProperties,

   bool setPropertyPlacementsSchema

)

public:

Function^ Place( 

   Page^ page,

   PointD location,

   bool copyProperties,

   bool copyAlsoNameProperties,

   bool setPropertyPlacementsSchema

)


#### Parameters

*page*
:   A page to insert the function's symbol on.

*location*
:   Insertion point of the symbol being inserted.

*copyProperties*
:   Determines if properties (excluding related to name) should be copied from source function.

*copyAlsoNameProperties*
:   Determines if name properties should be also copied from source function. Is only effective if copyProperties is true

*setPropertyPlacementsSchema*
:   Determines whether PropertyPlacementsSchema should be copied from source function.

#### Return Value

Newly placed function.

Remarks

The method behaves similarly as when dragging Function on a page. Existing function is not changed, except from the case when it is uncovered template - then it is made persistent
