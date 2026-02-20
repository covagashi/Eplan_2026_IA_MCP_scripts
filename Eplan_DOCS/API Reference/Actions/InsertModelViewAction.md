# InsertModelViewAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/InsertModelViewAction.html

---

```
Action to insert model view object on a page.

```

| Parameter | Description |
| --- | --- |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar).
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` LAYOUTSPACE
 ``` | ``` Name of layout space for which model view is created. This parameter is mandatory.
 ``` |
| ``` STRUCTURE
 ``` | ``` Structure identifier for which model view is created. This parameter is mandatory if name of layout space is not unique in project.
 ``` |
| ``` PAGENAME
 ``` | ``` Full name of page on which model view will be inserted. This parameter is mandatory.
 ``` |
| ``` X
 ``` | ``` X-coordinate of model view's lower left corner. This parameter is mandatory.
 ``` |
| ``` Y
 ``` | ``` Y-coordinate of model view's lower left corner. This parameter is mandatory.
 ``` |
| ``` DX
 ``` | ``` Width of model view. This parameter is mandatory.
 ``` |
| ``` DY
 ``` | ``` Height of model view. This parameter is mandatory.
 ``` |
| ``` VIEWNAME
 ``` | ``` Name of model view.
 ``` |
| ``` DESCRIPTION
 ``` | ``` Description of model view. Value of this parameter can be in multi-language string format.
 ``` |
| ``` ANGLE
 ``` | ``` Rotation of the content of model view. 
 Possible values are: 
 '¢ 1 - content is rotated 90° counter-clockwise; 
 '¢ 2 - content is rotated 90° in opposite direction.
 ``` |
| ``` SELECTIONSCHEME
 ``` | ``` Name of the selection scheme. It must be used with cabinet VIEWTYPE parameter.
 ``` |
| ``` STYLE
 ``` | ``` Style in which content of model view is displayed.
 Possible values are:
 '¢ 0 - Wire frame model;
 '¢ 1 - Hidden lines;
 '¢ 2 - Shading;
 '¢ 3 - Hidden lines / Simplified representation;
 '¢ 4 - Shading / Simplified representation.
 ``` |
| ``` ITEMLABELING
 ``` | ``` Name of the scheme which is applied for labeling the items in the model view.
 ``` |
| ``` VIEWPOINT
 ``` | ``` The direction from which objects are seen in model view.
 Possible values are:
 '¢ 0 - Default;
 '¢ 1 - Bottom;
 '¢ 2 - Top;
 '¢ 3 - Left;
 '¢ 4 - Right;
 '¢ 5 - Front;
 '¢ 6 - Rear;
 '¢ 7 - SE isometric;
 '¢ 8 - SW isometric;
 '¢ 9 - NE isometric;
 '¢ 10 - NW isometric;
 ``` |
| ``` ROOTELEMENTS
 ``` | ``` Values of property FUNCTION3D_ID_RELATIVE separated by # from 3D placements which will be set as root elements in created model view.
 ``` |
| ``` SCALESETTING
 ``` | ``` Type of scaling used to display objects in the model view.
 Possible values are:
 '¢ 0 - Automatic;
 '¢ 1 - Fit;
 '¢ 2 - Manually defined;
 ``` |
| ``` SCALE
 ``` | ``` Scale used to display objects in model view.
 ``` |
| ``` VIEWTYPE
 ``` | ``` Type of view used to display objects. 
 Possible values are:
 '¢ 0 - Undefined;
 '¢ 1 - Cabinet;
 '¢ 2 - EMI;
 '¢ 3 - Unfolding;
 '¢ 4 - DrillView;
 ``` |
| ``` OBJECTID
 ``` | ``` [OUT] Object id of created model view.
 ``` |

**Example**

```
Insert model view on a given page:

InsertModelViewAction /PROJECTNAME:C:\Projects\EPLAN\testProject.elk /PAGENAME:"/1" /VIEWNAME:SomeName /LAYOUTSPACE:ProjectLayoutSpaceName

/X:20 /Y:20 /DX:300 /DY:300 /STYLE:1 /VIEWPOINT:5 /SCALESETTING:0 /VIEWTYPE:1

```