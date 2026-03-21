---
title: "messageText"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_messagetext.htm"
file: "refformui_r_messagetext"
category: "refformui"
---

# messageText

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  messageText The <messageText> element defines the text displayed in the message window, which is either a normal text or the result of a formula. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
text | required |  |  | Displays a text in the message window. The text can be the result of a formula or directly input.  
Examples:  
text="Hello World"  
text="='Hello World'"  
text="=mc.$text"  
Allowed sub-elements | Quantity  
---|---  
none |   
[Example code](javascript:void\(0\);)
    
        <messageForm id="questionWindow" title="Question Window">
    		<messageIcon type="Question"/>
    		<messageText text="='Already inserted '+ mos.type('Documentation_UI_Configuration.ProjectLibrary.HelpObjects.Station').size + 'stations\nContinue inserting?'"/>
    		<formButtonArea>
    			<yesButton>
    				<performEvent name="Documentation_UI_Configuration.ProjectLibrary.HelpObjects.yesAction" arguments="=List{this}"/>
    			</yesButton>
    			<noButton/>
    		</formButtonArea>
    </messageForm>
