---
title: "Device names defining outgoing bus lines"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_modelvar_iogen_devnameisoutbus.htm"
file: "admin_r_modelvar_iogen_devnameisoutbus"
category: "admin"
---

# Device names defining outgoing bus lines

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Device names defining outgoing bus lines

Path to model variable:

Disciplines > IO Generator

Select a Boolean value. The value determines whether the name of the discipline component is used as the name of the outgoing bus and whether missing parameters are automatically created when Word resources are added.

Valid values are true and false.

If the value true is selected, the control components on the [Parameter Name For The Outgoing Bus Line](admin_r_modelvar_iogen_outbus.htm) model variable are not required, since a bus with the name of the control component is then formed.

### Read more

     * [Modeling bus topology](eecplc_k_create_controller_topology_modeling_bustopology.htm)
