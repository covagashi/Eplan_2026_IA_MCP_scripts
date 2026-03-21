---
title: "tree"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_tree.htm"
file: "refformui_r_tree"
category: "refformui"
---

# tree

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  tree The <tree> element is used to display project components in a tree structure. The root of the tree is specified by the root attribute and the branches to be displayed are specified by the <treeNode> sub-element. Furthermore, the display permits the background color, foreground color, horizontal and vertical expansion and visibility to be defined (see [treeNode](refformui_r_treenode.htm)). Furthermore, the names of the project components can be manipulated and supplemented with symbols. If the new <treeNotification> element is used in combination with the <onClickEvent> sub-element, actions can be executed via the displayed project components. (see [treeNotifications](refformui_r_treenotifications.htm) and [onClickEvent](refformui_r_onclickevent.htm)). Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
bColor | optional | 0,0,0 to 255,255,255 | System color | Background color as RGB value  
fColor | optional | 0,0,0 to 255,255,255 | System color | Foreground color as RGB value  
hSize | optional |  |  | Width of the element  
EEC = width in characters  
Web application = width in pixels  
root | required |  |  | The specified formula must yield a project component that serves as the root of the tree structure.  
visible | optional | true, false | true | true = table is visible  
true = table is invisible  
vSize | optional |  |  | Height of the element  
EEC = height in characters  
Web application = height in pixels  
Allowed sub-elements | Quantity  
---|---  
[treeNode](refformui_r_treenode.htm) | 0..1  
[treeNotifications](refformui_r_treenotifications.htm) | 0..1  
Tree structure with icons in front of every project component: The following example displays a tree structure that shows a different icon in front of each project component, depending on a parameter value. [Example of code for tree structure with symbols](javascript:void\(0\);)
    
        <form title="project tree" id="projectTree">
    	<tree root="=ref('Documentation_UI_Configuration.Mechatronic.Documentation')">
    		<treeNode name="='Node: '+ node.name" 
    			icon="=	if ($found = true)
    				then type('Documentation_UI_Configuration.ProjectLibrary.
    					HelpObjects.Images.action').image
    				else type('Documentation_UI_Configuration.ProjectLibrary.
    					HelpObjects.Images.next_class').image endif"
    				children="=node.mos.flatten" />
    	</tree>  
    </form>

Result: Tree structure in which each project component is preceded by an icon that triggers an action when clicked: The following example displays a tree structure that shows a different icon in front of each project component, depending on a parameter value. The project components have stored a parameter value that is used by an action to calculate a value to be displayed. The action is triggered by clicking the project component in the tree structure.[Example of code for tree structure with actions and symbols](javascript:void\(0\);)
    
        <form title="project tree with action" id="projectTreeAction">
    	<tree root="=ref('Documentation_UI_Configuration.Mechatronic.Documentation')">
    		<treeNode name="='Node: '+ node.name" 
    			icon="=	if ($found = true)
    				then type('Documentation_UI_Configuration.ProjectLibrary.
    					HelpObjects.Images.action').image
    				else type('Documentation_UI_Configuration.ProjectLibrary.
    					HelpObjects.Images.next_class').image endif"
    				children="=node.mos.flatten" />
    		<treeNotifications>
    			<onClickEvent>
    				<performEvent name="Documentation_UI_Configuration.ProjectLibrary.
    					HelpObjects.CalculateCoordinateAction"
    					arguments="=List{node.$Coordinate, this}" />
    			</onClickEvent>
    		</treeNotifications>
    	</tree>
    	<line>
    		<label text="='Calculated cardinal point: '"></label>
    		<label text="=$CardinalPoints"></label>
    	</line>
    </form>

Result:
