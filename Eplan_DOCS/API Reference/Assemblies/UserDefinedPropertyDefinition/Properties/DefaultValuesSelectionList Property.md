# DefaultValuesSelectionList Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UserDefinedPropertyDefinition~DefaultValuesSelectionList.html

---

Gets/Sets list of default values for selection list.

Syntax

**C#**



public IList<MultiLangString> DefaultValuesSelectionList {get; set;}

public:

property IList<MultiLangString^>^ DefaultValuesSelectionList {

   IList<MultiLangString^>^ get();

   void set (    IList<MultiLangString^>^ value);

}


Example

**C#**

```


string strPropertyNameFunction = "test.009a_FUNCTION";

UserDefinedPropertyDefinition oUDPDFunction = UserDefinedPropertyDefinition.Create(m_oTestProjectDemo, strPropertyNameFunction, UserDefinedPropertyDefinition.Enums.ClientType.Function);

oUDPDFunction.InputAid = UserDefinedPropertyDefinition.Enums.InputAidType.SelectionList;

List<MultiLangString> lstPossibleValues = new List<MultiLangString>();

MultiLangString mlsValue1 = new MultiLangString();

mlsValue1.AddString(ISOCode.Language.L___, "Possible value 1");

lstPossibleValues.Add(mlsValue1);

MultiLangString mlsValue2 = new MultiLangString();

mlsValue2.AddString(ISOCode.Language.L_en_US, "Possible value 2 EN");

mlsValue2.AddString(ISOCode.Language.L_de_DE, "Possible value 2 DE");

lstPossibleValues.Add(mlsValue2);

MultiLangString mlsValue3 = new MultiLangString();

mlsValue3.AddString(ISOCode.Language.L___, "Possible value 3");

lstPossibleValues.Add(mlsValue3);

oUDPDFunction.DefaultValuesSelectionList = lstPossibleValues;

```
