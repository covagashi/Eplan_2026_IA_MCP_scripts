---
title: "Using REST API in PowerShell"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refjobserver_r_restapi.htm"
file: "refjobserver_r_restapi"
category: "refjobserver"
---

# Using REST API in PowerShell

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Using REST API in PowerShell You can use REST API calls to  
     * Start the execution of a job.
     * Start the execution of a job and place it directly at the top of the queue.
     * Provide the result of the execution for download.
     * Determine the status of a job.
     * Remove a job from the queue.
The following REST API methods are supported:
     * POST: Calls up the execution of a job. Moves a job within the queue to the head of the queue.
     * GET: Retrieves a record.
     * DELETE: Deletes a record.
POST Syntax:
    
        $Response = Invoke-RestMethod -Uri $Uri -Body $Body -Method Post -ContentType 'application/json'

You ideally transfer the data for the POST request as a JSON record. [Example for the execution of a job (PowerShell)](javascript:void\(0\);)
    
        $Body = @{
    	params = @{
    		pathToXslt = "C:\Service\JobServer\XSL\ParameterWithType.xsl"
    		pathToTemplate = "C:\Service\JobServer\IMX\Template_CSV.imx"
    		projectOrMo = "Feeder"
    		pathToCsv = "C:\Service\JobServer\CSV\Parameter.csv"
    		pathToIMX = "C:\Service\JobServer\IMX\T2_Extension_AllLevels.imx"
    		delimiter = ";"
    		}
    	}
    $JsonBody = $Body | ConvertTo-Json
    $JobServerUrl = "https://myjobserver.com"
    $JobServerRequestPath = "/api/jobs/request/"
    $JobServerJobDef = "jobdef9"
    
    # Concatenate URI for Job request								
    $RequestUriPost = $JobServerUrl+$JobServerRequestPath+$JobServerJobDef
    
    # Invoke Job request
    **$Response = Invoke-RestMethod -Uri $RequestUriPost -Body $JsonBody -Method Post -ContentType 'application/json'**
    
    # Return Job ID to Host
    $JobId = $Response.id
    Write-Host $JobId
    
    $JobServerResponsePath = "/api/jobs/"
    
    # Concatenate URI for Job status request
    $RequestUriGet = $JobServerUrl+$JobServerResponsePath+$JobId
    
    # Wait for finished job
    while ($Response.status -ne "finishedSuccessfully" -and $Response.status -ne "finishedInError") {
    	
    	# Invoke Job status request
    	$Response = Invoke-RestMethod -Uri $RequestUriGet -Method Get -ContentType 'application/json'
    	
    	# Return Job status to host
    	$CurrentState = $Response.status;
    	Write-Host "Wait for job to finish. Current state: $CurrentState"
    }

Description: To call up the POST request, first a string variable $Body is defined with an assignment of parameters and their values (lines 1 to 10). In this example the values that are required for the execution of the command Engineering.ImportIMXCommand are transferred. The string variable is then converted to JSON and saved in the $JsonBody variable (line 11). The URI of the POST request as well as the GET request is composed of the URL, path to the job definition and name of the job definition (line 17 and line 29). With Invoke-RestMethod the REST method is called up with specification of the URI, the body data, the POST request and the type specification of the transferred data (line 20). The ID of the POST request is then returned to the host (lines 23 to 24). The state of a job is determined by means of the GET request and returned to the host (lines 32 to 40). [Example for execution of a job at the first position of the queue (PowerShell)](javascript:void\(0\);)
    
        $Body = @{
    	params = @{
    		pathToXslt = "C:\Service\JobServer\XSL\ParameterWithType.xsl"
    		pathToTemplate = "C:\Service\JobServer\IMX\Template_CSV.imx"
    		projectOrMo = "Feeder"
    		pathToCsv = "C:\Service\JobServer\CSV\Parameter.csv"
    		pathToIMX = "C:\Service\JobServer\IMX\T2_Extension_AllLevels.imx"
    		delimiter = ";"
    	}
    }
    $JsonBody = $Body | ConvertTo-Json
    $JobServerUrl = "https://myjobserver.com"
    $JobServerRequestPath = "/api/jobs/request/"
    $JobServerResponsePath = "/api/jobs/"
    $JobServerJobDef = "jobdef9"
    $JobServerJobTop = "?to=highestPriority"
    
    # Concatenate URI for Job request
    $RequestUriPost = $JobServerUrl+$JobServerRequestPath+$JobServerJobDef
    
    # Invoke Job request
    $Response = Invoke-RestMethod -Uri $RequestUriPost -Body $JsonBody -Method Post -ContentType 'application/json'
    
    # Return Job ID to host
    $JobId = $Response.id
    Write-Host $JobId
    
    # Concatenate URI for Job to top of queue request
    $RequestUriPostTop = $JobServerUrl+$JobServerResponsePath+$JobId+$JobServerJobTop
    
    # Invoke moving Job to top of queue
    **$Response = Invoke-RestMethod -Uri $RequestUriPostTop -Body $JsonBody -Method Post -ContentType 'application/json'**
    
    # Concatenate URI for Job status request
    $RequestUriGet = $JobServerUrl+$JobServerResponsePath+$JobId
    
    # Wait for finished job
    while ($Response.status -ne "finishedSuccessfully" -and $Response.status -ne "finishedInError") {
    	
    	# Invoke Job status request
    	$Response = Invoke-RestMethod -Uri $RequestUriGet -Method Get -ContentType 'application/json'
    	
    	# Return Job status to host
    	$CurrentState = $Response.status;
    	Write-Host "Wait for job to finish. Current state: $CurrentState"
    }

Description: For the POST request, a string variable $Body is defined with an assignment of parameters and their values (lines 1 to 10). In this example the values that are required for the execution of the command Engineering.ImportIMXCommand are transferred. The string variable is then converted to JSON and saved in the $JsonBody variable (line 11). The URI of the POST request is made up of the URL, path to the job definition and name of the job definition (line 19). With Invoke-RestMethod the REST method is called up with specification of the URI, the body data, the POST request and the type specification of the transferred data (line 22). The ID of the POST request is then stored in the $JobId parameter and returned to the host (lines 25 to 26). In order to move the job to the first position of the queue, the URI for a POST request is first compiled with the determined ID and additionally the parameter $JobServerJobTop (line 16) (line 35). With the new URI a renewed call of the POST request follows. The state of the last POST request is determined by means of the GET request and transmitted to the host (lines 38 to 46). GET Syntax:
    
        $Response = Invoke-RestMethod -Uri $Uri -Method Get -ContentType 'application/json'

[Example for the query of the request state (PowerShell)](javascript:void\(0\);)
    
        $Body = @{
    	params = @{
    		pathToXslt = "C:\Service\JobServer\XSL\ParameterWithType.xsl"
    		pathToTemplate = "C:\Service\JobServer\IMX\Template_CSV.imx"
    		projectOrMo = "Feeder"
    		pathToCsv = "C:\Service\JobServer\CSV\Parameter.csv"
    		pathToIMX = "C:\Service\JobServer\IMX\T2_Extension_AllLevels.imx"
    		delimiter = ";"
    		}
    	}
    $JsonBody = $Body | ConvertTo-Json
    $JobServerUrl = "https://myjobserver.com"
    $JobServerRequestPath = "/api/jobs/request/"
    $JobServerJobDef = "jobdef9"
    
    # Concatenate URI for Job request								
    $RequestUriPost = $JobServerUrl+$JobServerRequestPath+$JobServerJobDef
    
    # Invoke Job request
    $Response = Invoke-RestMethod -Uri $RequestUriPost -Body $JsonBody -Method Post -ContentType 'application/json'
    
    # Return Job ID to Host
    $JobId = $Response.id;
    Write-Host $JobId
    
    $JobServerResponsePath = "/api/jobs/"
    
    # Concatenate URI for Job status request
    $RequestUriGet = $JobServerUrl+$JobServerResponsePath+$JobId
    
    # Wait for finished job
    while ($Response.status -ne "finishedSuccessfully" -and $Response.status -ne "finishedInError") {
    	
    	# Invoke Job status request
    	**$Response = Invoke-RestMethod -Uri $RequestUriGet -Method Get -ContentType 'application/json'**
    	
    	# Return Job status to host
    	$CurrentState = $Response.status;
    	Write-Host "Wait for job to finish. Current state: $CurrentState"
    }

Description: The POST request has already been described in POST. The GET request (line 35) is to determine the current state of the previously started POST request and return it to the host until the POST request has been completed successfully or with an error (lines 32 to 40). For the GET request, the URI is first made up of individual parameter values (line 29). The job ID in particular is essential for this requirement. The response object $Response of the request returns the current state with the method status (line 23). The determined state is then returned to the host (line 39). DELETE Syntax:
    
        $Response = Invoke-RestMethod -Uri $Uri -Method Delete

[Example for deleting a job (PowerShell)](javascript:void\(0\);)
    
        param (
    	[Parameter(Mandatory,HelpMessage="Please enter the Job ID to be deleted.")]
    	[string] $IdOfJob
    )
    
    $JobServerUrl ="http://myjobserver.com:8686"
    $JobServerPath ="/api/jobs/"
    
    # Concatenate URI for Job to delete request
    $RequestUri = $JobServerUrl+$JobServerPath+$IdOfJob
    
    try{
    	# Invoke Job request to delete it
    	**$Response = Invoke-RestMethod -Uri $RequestUri -Method Delete**
    	
    	# Return Job status to host
    	Write-Host "Job with $IdOfJob successfully deleted."
    }
    catch{
    	$ex=$_|ConvertFrom-Json
    	
    	# Return error message to host
    	Write-Host $ex.message
    }

Description: In this example the DELETE request requires the entry of the JobID whose job is to be removed from the queue. The specified ID is stored in the parameter $IdOfJob (line 3). The required ID can also be transferred by a third-party system For the DELETE request, the URI is first made up of individual parameter values (line 10). In a try-catch block, the REST request is called up (line 14) and either a success message (line 17) or an error message (line 23) is returned to the host.
