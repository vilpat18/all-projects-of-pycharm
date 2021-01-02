import boto3
ec2 = boto3.resource('ec2')

instances = ec2.create_instances(

    ImageId = 'ami-0f438f5108bf5217e',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = 'ec2-keypair4'
)

print(instances)
