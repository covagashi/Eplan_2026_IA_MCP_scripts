---
title: "Navigation"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_navigation.htm"
file: "refformui_r_navigation"
category: "refformui"
---

# Navigation

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Navigation The usual navigation with link attributes, as known for websites, is created with the element <open>. Furthermore it is possible to provide the elements <label> and <input> with links, which, however, are not be represented in the usual formatting and equipped with the usual behavior (see [label](refformui_r_label.htm) and [input](refformui_r_input.htm)). Editable and controllable items in Form-UIs can be accessed by the tab key. In this case the items are accessed in the order upper left to lower right. The order is reversed if the Shift key is pressed. The navigation to the Form-UI of another project is not supported by default. The navigation is realized by means of the subsequently described method. First you have to create a method:
    1. Create a new object of the Util type with the name ResolveUtil.
    2. Switch to the Methods editor.
    3. Enter the resolvePath name in the Name field.
    4. Mark the Class method option.
    5. Select the language java.
    6. Add an argument.
    7. Enter the absolutePath name and the Engineering.String type.
    8. Enter the following code into the Code field:
    
        import com.mind8.mechatronic.skill.ResourceUtil;
    return ResourceUtil.getResourceByAbsolutePath(absolutePath,self.getUnitOfWork());

  4. The method has been successfully created as a result.
With this method an object can be converted into a path and applied in the <open> tag. [Example code](javascript:void\(0\);)
    
        <open
    	text="='Goto Project 2'"
    	receiver="type('FormUI.Helper.ResolveUtil').resolvePath('Project2.Mechatronic.Page')"
    	ref="projectId">
    </open>
