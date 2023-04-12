# CSC-Final-Project

-	Create a simple index.html file and compress it into a .zip file.
 

-	Go to AWS Amplify and click on Host your web app
<img width="423" alt="image" src="https://user-images.githubusercontent.com/96164843/231430019-44335ffb-2161-4232-8a72-e251fa168569.png">
 
-	Give an app name -> Environment Name -> Drag and Drop .zip file -> Save and Deploy
 




-	App successfully created and deployment successful.
 
 
-	Go to AWS Lambda and create a function.
 
-	Delete the existing code and paste code that parses an into put into multiple currency notes.
 

-	Save the code -> Deploy.
-	Drop down next to Test -> Configure Test Event.
 
-	Save -> Test.

 


-	Go to Amazon API Gateway -> REST API -> Build
 




-	New API -> Give API Name -> Click Create API.
 


-	Resources -> Actions -> Create Method -> POST – Lambda Function -> Choose Lambda Function -> Save - > OK.
  

-	Actions -> Enable CORS -> Enable CORS and replace existing CORS headers.
 

 





-	Resources -> POST -> Test -> …. (similar text to Configure Test Event) -> Test.
 


-	Actions -> Deploy API -> New Stage -> dev -> Deploy. Copy invoke URL on notepad.
 



-	Go to Amazon DynamoDB -> Create Table -> 
 

-	Create Table.

 



-	Copy ARN and paste in notepad.
 

-	Go back to Lambda Function -> Configuration -> Permissions -> Execution Role -> Click on the role to be redirected to IAM in a new tab.
 



-	In IAM -> Add Permissions -> Create Inline Policy -> 
 

-	Click on JSON -> Delete existing code and paste ExecutionRolePolicy in the field below -> Paste your DynamoDB ARN where mentioned.
 

-	Review Policy -> Give Policy Name -> Create Policy.

-	Go back to Lambda and update to final function. New lines of code added to put items into DynamoDB based on time API Gateway URL is invoked.

-	Function also returns solution to the application.

 

-	Updated in DynamoDB Table too.
 
-	Go back to AWS Amplify and update the html file with API Gateway invoke URL. Just Drag and Drop new .zip file.
 

 




 

-	Make sure app is working ->

 

-	Updated in DynamoDB aswell.


 

![image](https://user-images.githubusercontent.com/96164843/231429906-2a4201c3-cda1-4abc-af44-b02d814a704f.png)
