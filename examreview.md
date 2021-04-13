##### Questions containing REST are usually related to APIs so api gateway is the best answer

##### Each read capacity unit provdes one strongly consistent read per second or two for eventually consistent, for items up to 4KBs

##### Serverless applications should be built with lambda, api gateway and S3

##### RDS is NOT a supported event source for lambda

##### The load balancer configuration for migrating an ERP system is an App Load Balancer with sticky sessions - whenever you see the need to use HTTp its application load balancer. If the questions path based routing, it also needs to be an application load balancer

##### You can simulate an AZ failure by rebooting your RDS instance with forced failover

##### The KMS operation generate-data-key returns a plaintext data key, ready to be used to encrypt a document

##### IAM roles are specific for allowing isntances to make API requests securly

##### Secrets store charges you for storing your secrets

##### If a lambda function is not running as quickly as you'd like, try configuring more memory for it. Choosing 256MB of memory allocates approximately twice as much CPU power to your lambda - lambda allocates CPU linearly in proportion to the amount of memory configured

##### User Pools manage sign in and sign up functionality in cognito

##### Api gateway throttling supports 10 thousand requests per second, with 5 thousand concurrent requests

##### Dynamo DB integrates well with serverless

##### Dynamo db streams give you a time ordered sequence of all activity, good for audits. Great as lambda event source

##### Write capacity: 1kb per second. Read capacity 4kb per second for strongly consistent, 2 * 4KB per second for eventually consistent

##### Use CloudFront with signed urls and store videos in S3

- Enable stack termination protection to prevent accidental deletion of cloudformation stacks

- The CloudFormation cfn-init helper script is used to install packages and start stop services on ec2 instances

- Configure a VPC flow log with CloudWatch logs as the destintion. Create a Cloudwatch metric filter for destination. Create a Cloudwatdh alarm trigger. ##### - this is how you can configure alerts for more than x attempts to connect to the host

- 500 server errors should be fixed by using an exponential backoff, you can retry the request then

- Dead letter queues allow you to prevent data loss

- You want to separate the lambda handler from the core logic because

- Codedeploy has in-place or blue-green deployments

- While the bucket policy specifies AES256 for encryption, the ####header should say x-amz-server-side-encryption: aws:kms

- For added security you should ####terminate https connections on your ec2 instances

- The reason for separating a lambda handler from its core business logic is for re-usability

- SES lets you send emails from applications, but SQS is what you need if you want users to subscribe to emails

- Kinesis consumes application records according to a sequence number assigned when a record is written to a stream

- Combine cloudformation with codedeploy and aws sam to deploy code

#### X-ray does NOT integrate with S3

#### 429 means ou have reached concurrent execution limits for Lambda

#### ChangeMessageVisibility lets you extend the lenght of time to process jobs in SQS

#### You should ensure the number of instances does not exceed the number of shards

- DAX is a highly available in memory cache delivering up to 10x performance improvement from miliseconds to microseconds

- After a lambda function is executed, it maintains execution context for some time in anticipation of another invocation. The service "freezes" that execution context after the function completes, and thaws the context for reuse. Each context provides 512 MB of additional disk space in the /tmp directory. If the question/issue that needs solving is about a large download being made by lambda, you should store the file in the /tmp directory of the execution context and reuse it

