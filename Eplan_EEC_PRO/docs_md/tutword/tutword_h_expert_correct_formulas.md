---
title: "Parameterizing encapsulating mechatronic components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutword_h_expert_correct_formulas.htm"
file: "tutword_h_expert_correct_formulas"
category: "tutword"
---

# Parameterizing encapsulating mechatronic components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Parameterizing encapsulating mechatronic components All formulas have been lost due to the encapsulation of the discipline components and the usage of interface parameters. In addition all values can now be determined in the mechatronic structure. [Parameterizing M_Body](javascript:void\(0\);)
    1. Open the component M_Body.
    2. Switch to the Parameter editor page.
    3. Enter the formula =mc.name for the Heading parameter.
    4. Enter the formula =type('T_Images.Logo').image for the Logo parameter.
    5. Enter Chapter as the value for the Socket parameter.
    6. Save the component.
[Parameterizing M_Chapter](javascript:void\(0\);)
    1. Open the component M_Chapter.
    2. Switch to the Parameter editor page.
    3. Enter the following formula for the Heading parameter:
    
        =switch mc.mos('T_Office_Word.Wrapper.M_Chapter').indexOf(this)
    {
    	case 0 : 'Actuators'
    	case 1 : 'Sensors'
    	else : 'Not defined'
    }

    1. Enter Chapter as the value for the Plug parameter.
    2. Enter the formula =$Heading for the Socket parameter.
    3. Save the component.
[Parameterizing M_Row](javascript:void\(0\);)
    1. Open the component M_Row.
    2. Switch to the Parameter editor page.
    3. Enter the formula =mroot.name + mc.absoluteName.substring(mroot.absoluteName.size, mc.absoluteName.size - 1) for the Descriptor parameter.
    4. Enter the formula =type('T_Images.Actuators_Sensors_Imageregister').image(mc.type) for the Icon parameter.
    5. Enter the following formula for the Plug parameter:
    
        =switch mc.isInstanceOf('T_Mechatronic_Architecture.Levelcomponents.Actuator')
    {
    	case true : 'Actuators'
    	case false : 'Sensors'
    	else: 'Not defined'
    }

    1. Enter the following formula for the Pos. parameter:
    
        =switch mc.type.superType.name
    {
    	case 'Actuator': mroot.rmos('Actuator').indexOf(this.mc) + 1
    	case 'Sensor': mroot.rmos('Sensor').indexOf(this.mc) + 1
    	case 'Positionsensor': mroot.rmos('Positionsensor').indexOf(this.mc) + 1
    	else: 'Not defined'
    }

    1. Save the component.
Explanation of the formula for Plug: First of all, it is a Switch-Case request. The expression for Switch is compared with expressions for Case. In the case of the Switch expression it is determined whether the parent component is an instance of the type Actuator. The Switch expression can take on the values "true", "false" or "null". If the determined value corresponds with the first Case expression "true", the value "Actuators" is used. If the determined value corresponds with the second Case expression "false", the value "Sensors" is used. If none of the two expressions applies, "Not defined" is used. Explanation of the formula for Pos: First of all, it is a Switch-Case request. The expression for Switch is compared with expressions for Case. In the case of the Switch expression it is determined whether which super type the parent component corresponds to. The Switch expression can take on the values "Actuator", "Sensor" or "Position sensor". If the determined value corresponds to the first Case expression "Actuator", a list of all instances of "Actuator" is created and in it the position of the parent component is determined. Because Collections always begin with Index 0, you still have to add "1". If the determined value corresponds to the second Case expression "Sensor", a list of all instances of "Sensor" is created and in it the position of the parent component is determined. If the determined value corresponds to the third Case expression "Position sensor", a list of all instances of "Position sensor" is created and in it the position of the parent component is determined. If none of the three expressions applies, "Not defined" is used.
