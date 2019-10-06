# serverless_web_application


###Creating a static website

####Create an S3 bucket and configuring for web hosting

First, create an S3 bucket

```
aws s3 mb s3://serverless00
```

Enable the objects in the bucket to be requested using a registered public DNS name for the bucket, as well as direct site requests to the base path of the DNS name to index.html


###Edit the S3 bucket policy from the documents

```
aws s3api put-bucket-policy --bucket serverless00 --policy file://~/Github_Rep/serverless_web_application/s3/bucket-policy.json
```

###Add the required content to S3

```
aws s3 cp index.html s3://serverless00/index.html
```

###Now, open the web browser and check the webite at

```
http://serverless00.s3-website-us-east-1.amazonaws.com/
```

###Create cloudformation stack with necessary infrasrtucture

```
aws cloudformation create-stack --stack-name serverlessCoreStack --capabilities CAPABILITY_NAMED_IAM --template-body file://~/Github_Rep/serverless_web_application/core.yml
```







