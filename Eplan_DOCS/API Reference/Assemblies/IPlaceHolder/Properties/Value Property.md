# Value Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~Value.html

---

Gets/Sets the value of a variable for a record.

Syntax

**C#**



string Value( 

   string strRecordName,

   string strVarName

) {get; set;}

property String^ Value {

   String^ get(String^ strRecordName, String^ strVarName);

   void set (String^ strRecordName, String^ strVarName, String^ value);

}


#### Parameters

*strRecordName*
:   The name of the record.

*strVarName*
:   The name of the variable.
