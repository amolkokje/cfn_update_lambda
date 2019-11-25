# cfn_update_lambda

Way to automatically update lambda functions deployed using CloudFormation, with new code or dependencies.

CloudFormation stack only gets update when the service detects a change in properties of the resources defined in the template.

In this example, there is a CopyZips resource that copies the lambda package from the staging bucket to the stack bucket.
Then, there is a Lambda function resource which uses that copied package to create the lambda function.
So, we need to update these two resource in order for the stack to update the lambda function when we apply the CloudFormation Stack Update.

Here, the Lambda function is packaged and deployed to the staging bucket using SAM CLI, which generates a new package name.
Follow the below steps in order to update your lambda function.

1. Create the lambda package by executing the command "sam build --template lambda_template.yaml" in the /functions folder.

2. Upload the lambda pacakge to staging bucket using the command "sam package --s3-bucket lambda-function-staging-bucket".
   NOTE: Steps 1 and 2 can be combined using command: "sam build --template lambda_template.yaml && sam package --s3-bucket lambda-function-staging-bucket"

3. Get the package zip name from the previous step(will be some random string like 'ebc7764d8dd6df6cab4fc792c714087d').
   On the CloudFormation console, click Update -> Select 'Use Current Template' -> Update the LambdaFunctionPackage string with the new package name.
   Click on Next -> Next -> Update Stack.

This will start the stack update process and correctly update the stack with new code/dependencies.

This example is to demo a very simple deployment. But you may have a very complex stack with multiple lambda functions.
In that case taking a stack input parameter may not be the best way to update the deployed function. You would have to
figure out a way to update all the relevant strings, which can be achieved with several other CloudFormation tricks.