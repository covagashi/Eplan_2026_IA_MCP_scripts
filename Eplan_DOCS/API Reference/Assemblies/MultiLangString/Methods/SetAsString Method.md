# SetAsString Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString~SetAsString.html

---

Sets the contents of a MultiLangString with a string passed as argument using language marker if necessary. If argument is in MultiLangString form, it will be parsed and saved under given languages. Otherwise '??\_??@' prefix is added which means that the object is visible the same in every language.

Syntax

**C#**



public void SetAsString( 

   string val

)

public:

void SetAsString( 

   String^ val

)


#### Parameters

*val*
:   String that is set.
