---
title: "Canceling scripts with the AbortExecutionIfErrorCommand"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_cancel_script_with_abortexecutioniferrorcommand.htm"
file: "refscripting_r_cancel_script_with_abortexecutioniferrorcommand"
category: "refscripting"
---

# Canceling scripts with the AbortExecutionIfErrorCommand

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Canceling scripts with the AbortExecutionIfErrorCommand The execution of an action is terminated by the command Engineering.AbortExecutionIfErrorCommand, if a script enters an error in the UserMessageCollector. The following example code shows a scenario of a complex script. If an error occurs the script result (viz. the created changes to the model) should not be stored. The associated action is as follows: If an error occurs, in the accompanying ScriptCommand an error is mentioned in the UserMessageCollector and the internal recursive and iterative script processing is terminated. This can be done without the use of exceptions via a global abortExecution flag or by the UserScriptException. The UserScriptException has an ID and an optional text to be given. Thus, within scripting, various termination conditions are handled. This also functions for calls of scripts in scripts. An exception, which is thrown in a subscript, can be handled in the calling script. [Example code in Groovy with terminating variable](javascript:void\(0\);)
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.eos.MechatronicObject;
    import com.mind8.mechatronic.skill.eos.MechatronicComponent;
    logText1 = "Encountered unknown object! Aborting ...";
    logText2 = "Processing ";
    void doWork1(MechatronicComponent mc)
    {
    	children = mc.getMechatronicObjects();
    	for (Iterator iter = children.iterator() ;iter.hasNext();)
    	{
    		child = iter.next();
    		// define any abnormal abort condition
    		if (child.getName().equals("unknown"))
    		{
    			// log error and abort recursion
    			// don't forget to test for error by including an
    			// AbortExecutionIfErrorCommand in the Action
    			UserMessageCollector.addError(LIBRARY, self, null, "Script", logText1);
    			super.abortExecution = true;
    			return;
    		}
    		else
    		{
    			UserMessageCollector.addInfo(LIBRARY, self, null, "Script", logText2 + child.getName());
    			// do something ...	
    			if (child instanceof MechatronicComponent)
    			{
    				// a mc has children, so go into recursion
    				doWork1(child);
    			}
    		}
    		// abort iteration in case of abortion in recursion
    		if (super.abortExecution) return;
    	}
    }
    void doWork2(MechatronicComponent mc)
    {
    	// do something
    }
    // main script
    abortExecution = false;
    for (Iterator iter = obj.getMechatronicComponents().iterator() ;iter.hasNext();)
    {
    	mc = iter.next();
    	doWork1(mc);
    	// check abort in doWork1
    	if (abortExecution) return;
    	doWork2(mc);
    	// check abort in doWork2
    	if (abortExecution) return;
    }

[Example code in Groovy with UserScriptException](javascript:void\(0\);)
    
        import com.mind8.mechatronic.skill.scripting.UserScriptException;
    import org.foederal.util.ui.messages.UserMessageCollector;
    import com.mind8.mechatronic.skill.eos.MechatronicObject;
    import com.mind8.mechatronic.skill.eos.MechatronicComponent;
    logText1 = "Encountered unknown object! Aborting ...";
    logText2 = "Processing ";
    void doWork1(MechatronicComponent mc)
    {
    	children = mc.getMechatronicObjects();
    	for (Iterator iter = children.iterator() ;iter.hasNext();)
    	{
    		child = iter.next();
    		// define any abnormal abort condition)
    		if (child.getName().equals("unknown"))
    		{		
    			// Throw UserScriptAbortException to end recursion.
    			// Don't forget to test for error by including an
    			// AbortExecutionIfErrorCommand in the Action
    			throw new UserScriptException("id_abort", logText1);
    		}
    		else
    		{
    			UserMessageCollector.addInfo(LIBRARY, self, null, "Script", logText2 + child.getName());
    			// do something ...
    			if (child instanceof MechatronicComponent)
    			{
    				// a mc has children, so go into recursion
    				doWork1(child);
    			}
    		}
    	}
    }
    void doWork2(MechatronicComponent mc)
    {
    	// do something
    }
    // main script
    try
    {
    	for (Iterator iter = obj.getMechatronicComponents().iterator();
    	iter.hasNext();)
    	{
    		mc = iter.next();
    		doWork1(mc);
    		doWork2(mc);
    	}
    }
    catch (UserScriptException e)
    {
    	// only handle desired aborts
    	if (e.getId().equals("id_abort"))
    	{
    		UserMessageCollector.addError(LIBRARY, self, null, "Script", e.getMessage());
    	}
    	else
    	{
    		// handle elsewhere
    		throw e;
    	}
    }
