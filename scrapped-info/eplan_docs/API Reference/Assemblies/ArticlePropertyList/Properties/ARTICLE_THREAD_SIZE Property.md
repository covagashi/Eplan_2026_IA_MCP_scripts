# ARTICLE_THREAD_SIZE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_THREAD_SIZE().html

---

Thread dimension # 26108.

Syntax

**C#**



public PropertyValue ARTICLE_THREAD_SIZE {get; set;}

public:

property PropertyValue^ ARTICLE_THREAD_SIZE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Specific dimensions of a thread that is used in a product. This typically includes the diameter and the pitch of the thread. Example: The thread dimension "M10 x 1.5" for a screw means that the screw has a metric thread with a diameter of 10 mm and a pitch of 1.5 mm.
