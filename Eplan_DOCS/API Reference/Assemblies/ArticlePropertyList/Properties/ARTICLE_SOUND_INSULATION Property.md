# ARTICLE_SOUND_INSULATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SOUND_INSULATION().html

---

Sound insulation # 26543.

Syntax

**C#**



public PropertyValue ARTICLE_SOUND_INSULATION {get; set;}

public:

property PropertyValue^ ARTICLE_SOUND_INSULATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Designation for noise abatement measures to reduce sound generation and propagation. The sound insulation values are specified in decibels (dB), which is also the measuring unit of the sound level. In this case, the sound-damping measure R corresponds to the difference between the sound level in the transmitting space and the sound level in the receiving space.
