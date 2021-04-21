
#### Each read capacity unit provides one strongly consistent read per second or two for eventually consistent, for items up to 4KBs

#### Serverless applications should be built with lambda, api gateway and S3

#### The load balancer configuration for migrating an ERP system is an App Load Balancer with sticky sessions - whenever you see the need to use HTTP choose application load balancer as the correct type. If the questions path based routing, it also needs to be an application load balancer

#### IAM roles are specific for allowing instances to make API requests securly

#### User Pools manage sign in and sign up functionality in cognito

#### Write capacity: 1kb per second. Read capacity 4kb per second for strongly consistent, 2 * 4KB per second for eventually consistent

#### You can't store a certificate in aws config

#### Stage variables are name-value pairs you can define as config attributes associated with a deployment stage of a REST api.

#### Elastic container service manages running docker containers on a group of ec2 instances

- You can configure your api gateway to use an http proxy or a custom http config

- If your application performs operations that take a long time to complete, offload those tasks to a dedicated Elastic Beanstalk Worker environment to process tasks asynchronously

- Create a VPC endpoint for S3

- STS Assume role lets devs call the needed api role to access an s3 data repo

- If you are updating a runtime environment in elastic beanstalk you MUST use a blue/green deployment

### Monitoring

- To track only recently updated items in your application, you should enable streams and set the streamviewtype to NEW_IMAGE, while using kinesis adapter in the app to consume streams

### Security

- While the bucket policy specifies AES256 for encryption, the api call header should say x-amz-server-side-encryption: aws:kms

- For added security you should terminate https connections on your ec2 instances

- Secrets store charges you for storing your secrets

- The KMS operation generate-data-key returns a plaintext data key, ready to be used to encrypt a document

- In envelope encryption you encrypt plaintext data with a data key and then use a plaintext master key

- When an s3 bucket uses SSE-C encryption it should contain x-amz-server-side-encryption-customer-algorithm, x-amz-serverside-encryption customer key and x-amz-server-side-encryption customer key MD5 headers

- Getsessiontoken api call returns a temporary set of credentials if you want MFA auth

### SQS / SES / SNS queues

- SES lets you send emails from applications, but SQS is what you need if you want users to subscribe to emails

- Dead letter queues allow you to prevent data loss

- ChangeMessageVisibility lets you extend the lenght of time to process jobs in SQS

- DelaySeconds is needed as an attribute in your SQS queue to prevent a given message becoming visible

- You should increase message visibility timeout if your application is taking over 30 seconds to process it

- You can add a MessageDeduplication parameter to the sendmessage api and ensure longer times between messages to avoid duplicates

### API Error handling

- 500 server errors should be fixed by using an exponential backoff, you can retry the request then

- If you hit a ProvisionedThroughPutExceeded you can use exponential backoff, to improve flow control by retrying requests using progressively longer waits. Default included in AWS SDK

- 502 Bad Gateway with a lambda function when an api gateway proxy was configured, means there is an incompatible output returned from a lambda proxy backend


### Kinesis

- You should ensure the number of instances does not exceed the number of shards

- Kinesis consumes application records according to a sequence number assigned when a record is written to a stream

- Kinesis is the best option for storing streaming data for capture and processing. Lambda can process data directly from kinesis streams

- Data records are only accessible for 24 hours from the time they are added to a Kinesis stream

### X-ray

- X-ray does NOT integrate with S3

- Enable the X-ray daemon by including xray-daemon.config in the .ebextensions directory of your source code

- Use an X-ray filter expression to limit results based on custom attributes by adding those custom attributes as annotations on your segment document

- To use x-ray with docker configure port mappings and network settings to allow traffic on UDP port 2000

### Dynamo DB

- DAX (dynamo db accelerator) is a highly available in memory cache delivering up to 10x performance improvement from miliseconds to microseconds

- Dynamo DB integrates well with serverless

- Dynamo db streams give you a time ordered sequence of all activity, good for audits. Great as lambda event source

- To automatically trigger a lambda every time new entry is added to your dynamo db, you can enable Dynamo DB Streams

- Optimistic locking with version number lets you proect writes from being overwritten


### Lambda

#### 429 means ou have reached concurrent execution limits for Lambda

#### 500 might mean the lambda resource based policy does not include permissions for the api to invoke the function

- Lambda concurrent executions: invocations per second * avg execution duration in seconds. So a function that takes avg 3 secs to execute 10 events has 30 concurrent executions.

- The reason for separating a lambda handler from its core business logic is for re-usability

- After a lambda function is executed, it maintains execution context for some time in anticipation of another invocation. The service "freezes" that execution context after the function completes, and thaws the context for reuse. Each context provides 512 MB of additional disk space in the /tmp directory. If the question/issue that needs solving is about a large download being made by lambda, you should store the file in the /tmp directory of the execution context and reuse it

- You can use lambda traffic shifting to point traffic to different versions of your app

- Lambda@edge lets you make your apps globally distributed, improve performance and run code in response to events generated by the amazon CDN. You can also use it to authenticate and authorise a group of users

- Reference external endpoints by using environment variables

- Change the lambda invocation type to Event in order to invoke it asynchronously. The default lambda invocation is RequestResponse which invokes the functions synchronously.

- The default RequestResponse type (synchronous) has both the response of the function and additional data in its api response

- The Event response type is asynchronous and the API response only includes a status code

- Lambda communicates with X-ray using _X_AMZN_TRACE_ID and AWS_XRAY_CONTENT_MISSING

#### If a lambda function is not running as quickly as you'd like, try configuring more memory for it. Choosing 256MB of memory allocates approximately twice as much CPU power to your lambda - lambda allocates CPU linearly in proportion to the amount of memory configured

#### RDS is NOT a supported event source for lambda

### RDS

- You can simulate an AZ failure by rebooting your RDS instance with forced failover

- RDS is NOT a supported event source for lambda

- Troubleshoot RDS issues by enable slow query log in RDS


### Api Gateway

- Ensure incoming api request data gets mapped to integration request and resulting integration is matted to response: use HTTP in API Gateway

- Api gateway throttling supports 10 thousand requests per second, with 5 thousand concurrent requests

- Questions containing REST are usually related to APIs so api gateway will be the best answer

- 502 bad gateway errors are most likely caused by an incompatible output returned from a lambda proxy integration

- A client can fetch the latest data from your endpoints and invalidate existing cache with the request Cache-Control: max-age: 0 header

### Containers

- Configure a Task Definition to allow containers to access ports on the host container instance

### CloudWatch

- Collect data on all users currently logged in every 10 seconds by publishing a high-resolution custom metric to CloudWatch. Metrics can be standard or high resolution - standard has a minute granularity, high resolution has one second granularity

- You can configure alerts of more than x attempts to connect to a host by: configuring a VPC flow log with CloudWatch logs as the destination and a Cloudwatch metric filter for the destination with an alarm trigger

- Default aws metrics are standard resolution

- Use CloudWatch for downstream call tracing of lambda functions, combined with AWS x-ray. Cloudtrail isn't appropriate for downstream tracing, as it records API calls not event source of your functions / downstream events


- Troubleshoot problems with an Api gateway + lambda proxy taking long to complete by using the CloudWatch metrics of: Latency and IntegrationLatency. Integration latency measures backend responsiveness. Latency measures overall responsiveness.


### CloudFormation

- Enable stack termination protection to prevent accidental deletion of cloudformation stacks

- The CloudFormation cfn-init helper script is used to install packages and start stop services on ec2 instances

- Set DeletionPolicy to retain when you want to preserve a specific resource even if the stack is deleted. While Stack termination protection lets you protect against deleting the entire stack, DeletionPolicy retain is used just for single resources

- Cloudformation parameters can be used to set custom values to be used at runtime

### CI / CD: Cloudformation + Codedeploy

- Combine cloudformation with codedeploy and aws sam to deploy code

- Codedeploy has in-place or blue-green deployments

- AWS lambda compute deployments cannot use an in-place codedeploy deployment

- Lambda and ECS cannot use in-place deployment types

- CodeBuild uses buildspec.yml, CodeDeploy uses appspec.yml - YAML only

- Cloudformations can be YAML or JSON


### SAM - Serverless Application Model

- Use AWS::Serverless::Application to embed an app from the AWS serverless app repo/ s3 into a nested operation

- SAM is an extension of cloudFormation, thus enabling you to define resources by using Cloudformation in your aws sam template.


#### All aws Lambda and ECS deployments are blue/green

- CodeDeploy allows you to shift traffic from a previous lambda function to a new version without shifting all traffic at once. For this you can use CodeDeployDefault.LambdaCanary10Percent5Minutes, Canary for shifts in two increments. Linear for shifts in equal increments.

### Cloudfront

- Implement HTTPS between viewers and Cloudfront by setting Viewer Protocol Policy to Redirect HTTP to HTTPS and Viewer protocol Policy to HTTPS only

- Use CloudFront with signed urls to store videos in S3

- Configure Origin protocol policy and viewer protocol policy in cloudfront to establish an end to end ssl connection between your origin and your end users. By using the Origin protocol policy combined with the Viewer Protocol policy Cloudfront can provide the SSL/TLS certificate

### Elasticache

- Lazy loading is a caching strategy that only loads data into the cache when necessary. Its good when the requirement is to retrieve data only when there is a cache miss.

