# SetVisibleNameAndAdjustFullName(Page,FunctionBase,UniversalPropertyList,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1391.html

---

Sets the page and sets the given visible name as the new visible name to the given function and adjusts the full name of that function accordingly (by calling "EvaluateName").

Syntax

**C#**



public bool SetVisibleNameAndAdjustFullName( 

   Page pPage,

   FunctionBase pFunctionBase,

   UniversalPropertyList eplVisibleName,

   string sVisibleNameFormat

)

public:

bool SetVisibleNameAndAdjustFullName( 

   Page^ pPage,

   FunctionBase^ pFunctionBase,

   UniversalPropertyList^ eplVisibleName,

   String^ sVisibleNameFormat

)


#### Parameters

*pPage*
:   Page to set.

*pFunctionBase*
:   Function for which the name is set.

*eplVisibleName*
:   PropertyList for evaluated name.

*sVisibleNameFormat*
:   New visible name.

#### Return Value

Returns false, if a problem occured - no changes have been made then.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
