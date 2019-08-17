import boto3, yaml, json
from cfn_flip import flip, to_yaml, to_json
import sys

def create_stack():
    # file must in the same dir as script
    template_file_location = 'cfn-template.yml'
    stack_name = 'ansibleStack1'

    # # read entire file as yaml
    with open(template_file_location, 'r') as content_file:
        content = to_json(content_file)
    #content_json = to_json(template_file_location)
    cloud_formation_client = boto3.client('cloudformation')

    print("Creating {}".format(stack_name))
    response = cloud_formation_client.create_stack(
        StackName=stack_name,
        TemplateBody=content
    )

def delete_stack():
    cloud_formation_client = boto3.client('cloudformation')
    stack_name = 'ansibleStack1'
    print("Deleting  {}".format(stack_name))
    response = cloud_formation_client.delete_stack(
                StackName = stack_name )

def read_stack_update_inventory():
    stack_name = 'ansibleStack1'
    print("Reading  {}".format(stack_name))
    cloudformation = boto3.resource('cloudformation')
    stack = cloudformation.Stack(stack_name)
    print(stack.outputs)
    
if __name__=='__main__':
    globals()[sys.argv[1]]()