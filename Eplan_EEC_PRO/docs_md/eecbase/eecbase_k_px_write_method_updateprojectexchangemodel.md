---
title: "Writing method updateProjectExchangeModel"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_px_write_method_updateprojectexchangemodel.htm"
file: "eecbase_k_px_write_method_updateprojectexchangemodel"
category: "eecbase"
---

# Writing method updateProjectExchangeModel

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Writing method updateProjectExchangeModel

The ProjectExchangeModelUpdate1.java class is pre-defined in the following lines:

### [Example code](javascript:void\(0\);)
    
        package de.eplan.px.update;
    import com.mind8.project.exchange.api.IProjectExchangeAPI;
    import com.mind8.project.exchange.update.AbstractProjectExchangeModelUpdate;
    import com.mind8.project.exchange.update.IProjectExchangeModelUpdate;
    public class ProjectExchangeModelUpdate1 extends AbstractProjectExchangeModelUpdate implements
    IProjectExchangeModelUpdate
    public ProjectExchangeModelUpdate1()
    {
    	// TODO Auto-generated constructor stub
    }
    @Override
    public void updateProjectExchangeModel(IProjectExchangeAPI pxModel) throws ProjectExchangeModelModificationException
    {
    	// TODO Auto-generated method stub
    }
    						

The constructor can be removed from this definition.

The update to be executed must be implemented in the method updateProjectExchangeModel(IProjectExchangeAPI pxModel). There are methods available to do this, which are described in the following sections.

After the implementation, the plug-in is exported either directly to the folder \dropins or to a temporary folder, and finally copied to the folder \dropins. This is explained in the section [Exporting plug-ins](eecbase_k_px_plugin_export.htm).
