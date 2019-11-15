# cfn_update_lambda
Way to automatically update lambda functions deployed using CloudFormation, when there is a code change for the lambda package in S3 staging bucket

In this architecture, the code package zip used for the lambda function is stored in a staging s3 bucket.


1. Enable versioninig on the s3 staging bucket. Hence, whenever a new lambda code package is uploaded to s3,
   the version ID changes.

2. Create a Cloudformation stack using the template file in this repo. It will ask you for the staging bucket name,
   prefix, and also the version ID of the lambda package (you can get this from CLI or Console). Enter all of that.

3. During stack creation, the CopyZips custom resource will grab the s3 object with the specified version ID and create
   the lambda function using that.

4. Now, say you need to make changes to the lambda package code. You make changes and upload the new zip to the staging
   bucket. This will update the version ID. Grab this version ID from s3 object.

5. Apply an update to the Cloudformation Stack, with all parameters same, and only update the version ID. When CopyZips
   resource property is updated, this will re-create/update the custom resource which will in-turn copy the specific
   version bucket key from
