import boto3

ec2 = boto3.resource('ec2')

#create a file to store key locally
outfile = open('ec2-keypair5.pem','w')

#call the boto ec2 function to create keypair
key_pair = ec2.create_key_pair(KeyName='ec2-keypair5')

#capture the key and store it in file
keypairout = str(key_pair.key_material)

print(keypairout)

outfile.write(keypairout)