# SetFullNameAndAdjustVisibleName(Page,FunctionBase,UniversalPropertyList) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1389.html

---

Sets the page and sets the given full name as the new full name to the given function and adjusts the visible name of that function. Returns false, if a problem occured (if a visible name cannot be evaluated) - no changes to the function-object have been made then.

Syntax

**C#**



public bool SetFullNameAndAdjustVisibleName( 

   Page pPage,

   FunctionBase pFunctionBase,

   UniversalPropertyList eplFullName

)

public:

bool SetFullNameAndAdjustVisibleName( 

   Page^ pPage,

   FunctionBase^ pFunctionBase,

   UniversalPropertyList^ eplFullName

)


#### Parameters

*pPage*
:   Page to set.

*pFunctionBase*
:   Function for which the name is set.

*eplFullName*
:   PropertyList with new full name.

#### Return Value

Returns false, if a problem occured (if a visible name cannot be evaluated) - no changes to the function-object have been made then.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
