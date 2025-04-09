### ARN Format for s3
url: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-resources-for-iam-policies

- S3 accesspoint
[arn:${Partition}:s3:${Region}:${Account}:accesspoint/${AccessPointName}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-resources-for-iam-policies)

- S3 bucket
[arn:${Partition}:s3:::${BucketName}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-resources-for-iam-policies)

- S3 storagelensgroup
[arn:${Partition}:s3:${Region}:${Account}:storage-lens-group/${Name}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-resources-for-iam-policies)

- S3 object
[arn:${Partition}:s3:::${BucketName}/${ObjectName}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-resources-for-iam-policies)


### ARN Format for IAM
url: https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentityandaccessmanagementiam.html#awsidentityandaccessmanagementiam-resources-for-iam-policies

- IAM mfa
[arn:${Partition}:iam::${Account}:mfa/${MfaTokenIdWithPath}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentityandaccessmanagementiam.html#awsidentityandaccessmanagementiam-resources-for-iam-policies)

- IAM role
[arn:${Partition}:iam::${Account}:role/${RoleNameWithPath}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentityandaccessmanagementiam.html#awsidentityandaccessmanagementiam-resources-for-iam-policies)

- IAM user
[arn:${Partition}:iam::${Account}:user/${UserNameWithPath}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentityandaccessmanagementiam.html#awsidentityandaccessmanagementiam-resources-for-iam-policies)


### ARN Format for IAM
url: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html#amazonec2-resources-for-iam-policies

- EC2 elastic-ip
[arn:${Partition}:ec2:${Region}:${Account}:elastic-ip/${AllocationId}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html#amazonec2-resources-for-iam-policies)

- EC2 fleet
[arn:${Partition}:ec2:${Region}:${Account}:fleet/${FleetId}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html#amazonec2-resources-for-iam-policies)

- EC2 instance
[arn:${Partition}:ec2:${Region}:${Account}:instance/${InstanceId}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html#amazonec2-resources-for-iam-policies)

- EC2 image
[arn:${Partition}:ec2:${Region}::image/${ImageId}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html#amazonec2-resources-for-iam-policies)
