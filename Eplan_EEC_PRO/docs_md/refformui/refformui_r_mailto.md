---
title: "mailto"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_mailto.htm"
file: "refformui_r_mailto"
category: "refformui"
---

# mailto

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  mailto The element <mailto> creates a new e-mail by means of the locally installed mail client. The fields of the new email, e.g. âToâ and âSubjectâ can be pre-populated with text. Texts in the text field of the e-mail are wrapped by using the decimal &#10; (see [Line break](refformui_r_line_break.htm)). Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
bcc | optional |  |  | Receiver of a blind copy  
body | optional |  |  | Text content of the e-mail; the text has to be determined by a formula  
cc | optional |  |  | Receiver of a copy  
font | optional | Font name-style-size | System font | Font name, style, and size for displaying text  
hSizeMax | optional |  |  | maximum width of the element  
EEC = width in characters  
Web application = width in pixels  
hSizeMaxPx | optional |  |  | maximum width of the element  
EEC = width in pixels  
Web application = width in pixels  
img | optional | png, gif, jpg |  | assigns another image to the element  
readonly | optional | true, false |  | true = element is disabled  
false = element is enabled  
subject | optional |  |  | Text of the subject line  
text | optional |  |  | the text to display  
to | optional |  |  | Receiver  
tooltip | optional |  |  | Text or Form-UI of the overlaying tooltip (see [tooltip](refformui_r_tooltip.htm))  
type | optional | link, button | link | Representation type of the element as hyperlink or button  
button = button  
link = text as a hyperlink  
visible | optional | true, false | true | true = element is visible  
true = element is invisible  
Allowed sub-elements | Quantity  
---|---  
[tooltip](refformui_r_tooltip.htm) | 0..1  
The text of the e-mail (the body) can be additionally stated as the content of the element. In that case the text cannot be calculated (the same behavior as for the element <label>). A hyperlink, which passes an email to the email client: [Example code](javascript:void\(0\);)
    
        <mailto type="link" text="Send e-mail" to="support@mind8.com" cc="info@mind8.com" subject="Support"
    	body="='Dear Ladies and Gentlemen, '">
    	thank you for the fast response and support ...
    </mailto>

Result: A button, which passes an email to the email client: [Example code](javascript:void\(0\);)
    
        <mailto type="button" text="Send e-mail" to="support@mind8.com" cc="info@mind8.com" subject="Support"
    	body="='Dear Ladies and Gentlemen, '">
    	thank you for the fast response and support ...
    </mailto>

Result:
