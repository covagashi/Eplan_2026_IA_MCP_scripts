---
title: "Querying job status"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_webservicetrigger_jobstatus.htm"
file: "refjobserver_r_webservicetrigger_jobstatus"
category: "refjobserver"
---

# Querying job status

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Querying job status A Job that has been created but not completed can have the following statuses:  
     * "Queued" = Job is in the queue for execution on a Worker.
     * "Running" = Job is being executed on a Worker.
A completed Job can have the following statuses:
     * "FinishedSuccessfully" = Job has been completed successfully without errors.
     * "FinishedInError" = Job has been completed with errors.
A completed job can return the following information:
     * Job name (see Line 34 in example code).
     * Executing Worker (see Line 35 in example code).
     * Execution time in milliseconds (see Line 36 in the example code).
     * Link to the log (see Line 43 in the example code).
     * Link to the repository (see Line 45 in the example code).
[Example of GET call of the Job Server for a running Job](javascript:void\(0\);) Request | GET /api/jobs/be3e05a5-de59-480e-80a4-181962267a90 HTTP/1.1  
---|---  
Accept | application/json  
Accept-Encoding | gzip, deflate  
Pragma | no-cache  
Body | _empty_  
Response | HTTP/1.1 200 OK  
---|---  
Content-Type | application/json  
Body | 
    
        {
    	"id": "be3e05a5-de59-480e-80a4-181962267a90",
    	"status": "Running",
    	"message": "Entering myjob with mykey: 1234",
    	"inputData": {
    		"params": {
    			"ricsid": "1234567"
    		}
    	},
    	"jobDef": {
    		"name": "myjob",
    		"workerData": {
    			"type": "jmx",
    			"data": {
    				"name": "myjob",
    				"continueOnError": false,
    				"baseModelFile": "model.eox",
    				"successMailRecipients": "",
    				"failedMailRecipients": "",
    				"actions": [
    					{
    						"name": "MyLibrary.MyCustomActionWithMapArg",
    						"args": "List{trigger.params}"
    					},
    [â¦]
    				]
    			}
    		},
    		"serviceData": {
    			"type": "WebService/empty",
    			"data": {}
    		}
    	},
    	"jobName": "myjob_150817_1708_57700",
    	"executedOnWorker": "http://workerurl:5901",
    	"duration": "2485",
    	"resultData": {},
    	"@meta": {
    		"self": "http://aliasurl/api/jobs/be3e05a5-de59-480e-80a4-181962267a90"
    	}
    	"links": {
    		"logs": {
    			"href": "http://aliasurl/api/logs/"
    		},
    		"repository": {
    			"href": "http://aliasurl/api/repository/"
    		}
    	}
    }
