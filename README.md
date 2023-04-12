# CSC-Final-Project

## - Proposed Architecture
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231434301-76d903f6-6c12-4340-b80e-3c40b2ed945c.png">

## -	Create a simple index.html file and compress it into a .zip file.
 <img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231430019-44335ffb-2161-4232-8a72-e251fa168569.png">
 
## -	Go to AWS Amplify and click on Host your web app
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231430949-014c3172-d5a9-4ace-a89c-10ca6baaa7d4.png">

<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231431033-047c092b-0e0d-4b8d-bf86-625e22461036.png">

## -	Give an app name -> Environment Name -> Drag and Drop .zip file -> Save and Deploy
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231431070-0eddaf56-441f-4261-8a8c-3430469bb522.png">

## -	App successfully created and deployment successful.
 <img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231431103-9a2bebf5-5854-4dab-a111-3d3a69cfaf45.png">
 
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231431147-bfe28b03-2172-43c2-8675-3f1332556abd.png">
 
## -	Go to AWS Lambda and create a function.
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231431238-73e0edf1-d78c-41bf-8a99-8fa0bd202aaf.png">

## -	Delete the existing code and paste code that parses an into put into multiple currency notes.
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231431273-3417b89d-5170-474b-aced-0480495d9402.png">

## -	Save the code -> Deploy.
## -	Drop down next to Test -> Configure Test Event.
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231431394-b82df3c7-2e0e-43bd-ae59-a49df43a38b5.png">

## -	Save -> Test.
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231431484-c08017cd-2dd9-4fd8-8832-c7d33463fea0.png">

## -	Go to Amazon API Gateway -> REST API -> Build
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231431554-2b69b217-7ca2-43e7-aecf-15b1812791df.png">

## -	New API -> Give API Name -> Click Create API.
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231431588-0b2296f1-8f86-4899-b2cf-dc1de1a34661.png">

## -	Resources -> Actions -> Create Method -> POST – Lambda Function -> Choose Lambda Function -> Save - > OK.
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231431633-6b4bed34-1ace-4cf8-9764-4bc59d53a8dc.png">

## -	Actions -> Enable CORS -> Enable CORS and replace existing CORS headers.
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231431685-df77974f-1c54-4b56-a49f-8f2c9d252f59.png">

<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231431773-0b973d5a-b3e7-4de6-90a8-5b05683d35dd.png">

## -	Resources -> POST -> Test -> …. (similar text to Configure Test Event) -> Test.
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231431825-5b29370e-9abb-42f2-815b-1182b08df83a.png">

## -	Actions -> Deploy API -> New Stage -> dev -> Deploy. Copy invoke URL on notepad.
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231431870-ccf8b5c3-db9c-402b-8594-91dbf5e6a888.png">

## -	Go to Amazon DynamoDB -> Create Table -> 
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231431918-32231426-14ef-47cd-ac27-c7089d45ffd7.png">

## -	Create Table.
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231431960-25e2bca9-535b-43c9-8903-3388a66eacb8.png">

## -	Copy ARN and paste in notepad.
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231431996-ee4a2c47-cfd8-425e-91bf-103b77230aff.png">

## -	Go back to Lambda Function -> Configuration -> Permissions -> Execution Role -> Click on the role to be redirected to IAM in a new tab.
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231432045-ae4cd776-48d4-4ad3-b02a-8cd66721cc90.png">

## -	In IAM -> Add Permissions -> Create Inline Policy -> 
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231432098-37b999a7-4114-47eb-af00-23cc0aa1c77e.png">

## -	Click on JSON -> Delete existing code and paste ExecutionRolePolicy in the field below -> Paste your DynamoDB ARN where mentioned.
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231432155-e3088449-981a-4226-83d9-dcaaf79a582d.png">

## -	Review Policy -> Give Policy Name -> Create Policy.
## -	Go back to Lambda and update to final function. New lines of code added to put items into DynamoDB based on time API Gateway URL is invoked.
## -	Function also returns solution to the application.
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231432244-8d71b1b8-60c2-4965-877a-f34e73628fa2.png">

## -	Updated in DynamoDB Table too.
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231432279-9c9297b5-9aaa-4d33-9163-dc9ff5c85cdf.png">

## -	Go back to AWS Amplify and update the html file with API Gateway invoke URL. Just Drag and Drop new .zip file.
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231432334-46b9c752-201a-4382-9710-4914defa328d.png">

<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231432398-3258a11b-c951-458b-abb3-86b19005c03b.png">

<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231432490-c6841e49-8b8a-4d7d-af97-d66d47fb072d.png">

## -	Make sure app is working ->
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231432529-626b3de5-968b-4235-87cb-79e294467e79.png">

## -	Updated in DynamoDB aswell.
<img width="600" alt="image" src="https://user-images.githubusercontent.com/96164843/231432564-e678907b-4724-4bdf-902c-9c80747abb01.png">

