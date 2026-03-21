---
title: "command"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_command.htm"
file: "refformui_r_command"
category: "refformui"
---

# command

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  command By means of the <command> element enclosed by the <dialog> element before opening and after closing as well as by clicking the buttons [OK], [Cancel], [Yes] and [No] actions, resp. commands are executed. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
event | required | after,  
before,  
beforebuild,  
cancel,  
closed,  
doubleclick,  
no,  
ok,  
yes |  | Event type, which describes when the action resp. the command is executed.  
after = after the dialog or the Form-UI page is built  
before = before opening the dialog  
beforebuild = before the new Form-UI page is built  
cancel = after clicking the cancel button  
closed = after the dialog is closed  
doubleclick = after double-clicking an entry of the table (only for pureTable)  
ok = after clicking the OK button  
yes = after clicking the Yes button  
no = after clicking the No button  
name | required |  |  | full qualified name of the action resp. the command which is to perform.  
arguments | optional | List |  | List of arguments that are passed to the action resp. the command  
Allowed sub-elements | Quantity  
---|---  
none |   
[Example code](javascript:void\(0\);) A link performs an action before jumping to the link target:
    
        <open ref="linkTarget" receiver="x" type="link" text="OPEN">
    	<command event="before"
    		name="myActions.myAction" />
    		arguments="=List{this.$myParameter1,this.$myParameter2}" />
    </open>
