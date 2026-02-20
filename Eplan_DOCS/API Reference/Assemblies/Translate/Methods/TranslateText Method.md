# TranslateText Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~TranslateText.html

---

Get translation for the given text, according to project settings.

Syntax

**C#**



public MultiLangString TranslateText( 

   string strText,

   Project oProject

)

public:

MultiLangString^ TranslateText( 

   String^ strText,

   Project^ oProject

)


#### Parameters

*strText*
:   Text to translate

*oProject*
:   Project from which settings are read.

#### Return Value

Translated text.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Throw if any parameter is invalid. |
