---
title: "Call back by the Job Server"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_webservicetrigger_callback.htm"
file: "refjobserver_r_webservicetrigger_callback"
category: "refjobserver"
---

# Call back by the Job Server

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Call back by the Job Server webserviceTrigger If a Callback URL is specified when creating the Job, the Job Server calls the URL with a POST when the Job has been completed. The response is ignored. [Example POST of the Job Servers to Callback URL](javascript:void\(0\);) Request | POST http(s)://callbackurl  
---|---  
Accept | application/json  
Accept-Encoding | gzip, deflate  
Pragma | no-cache  
Body | 
    
        "id": "be3e05a5-de59-480e-80a4-181962267a90",
    	"status": "Running",
    	"message": "Entering myjob with mykey: 1234",
    	"inputData": {
    		"params": {
    			"ricsid": "1234567"
    		},
    		"callback": {
    			"href": "http://callbackurl"
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
    		"downloads": {
    			"href": "http://aliasurl/api/jobs/be3e05a5-de59-480e-80a4-181962267a90/downloads"
    		}
    	}
    }  
  
Support for the EPLAN Data Portal: [Example POST of the Job Servers to Callback URL](javascript:void\(0\);) Request | POST http(s)://callbackurl  
---|---  
Accept | application/json  
Accept-Encoding | gzip, deflate  
Pragma | no-cache  
Body | 
    
        "id": "be3e05a5-de59-480e-80a4-181962267a90",
    	"status": "Running",
    	"message": "Entering myjob with mykey: 1234",
    	"inputData": {
    		"params": {
    			"ricsid": "1234567"
    		},
    		"dataPortalCallback": {
    			"href": "http://my-dataportal-url.de"
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
    		"downloads": {
    			"href": "http://aliasurl/api/jobs/be3e05a5-de59-480e-80a4-181962267a90/downloads"
    		}
    	}
    }
