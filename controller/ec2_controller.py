"""
ec2_controller.py

This module provides methods to control an AWS EC2 instance.
"""

from boto3 import Session


class Ec2:
    """
    A class representing an AWS EC2 instance.

    Attributes:
        region (str): the AWS region of the EC2 instance. i.e. "us-east-1" or "ca-central-1".

        aws_access_key (str): an AWS IAM user access key with a policy
        that includes: RevokeSecurityGroupIngress,
        AuthorizeSecurityGroupIngress, StartInstances, CreateTags,
        and StopInstances. Must have access to your EC2 instance's ARN.

        aws_secret_access_key (str): the AWS IAM user secret key.

        ec2_instance_id (str): the AWS EC2 instance id.

        ec2: a boto3 ec2 Session object.

        ipv4: the ipv4 of the AWS EC2 instance.
    """

    def __init__(
        self,
        ec2_instance_id: str,
        region: str,
        aws_access_key: str,
        aws_secret_access_key: str,
    ) -> None:
        """Initializes an Ec2 object with the given details from AWS

        Args:
            ec2_instance_id (str): the id of an AWS EC2 instance

            region (str): the region of the AWS EC2 instance

            aws_access_key (str): an AWS IAM user access key id

            aws_secret_access_key (str): the AWS IAM user secret access
            key


        """
        self._region = region
        self._aws_access_key = aws_access_key
        self._aws_secret_access_key = aws_secret_access_key
        self._ec2_instance_id = ec2_instance_id
        self._ec2 = None
        self.ipv4 = ""

        session = Session(
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region,
        )

        self.ec2 = session.client("ec2")

    def start(self):
        # !!! TODO
        pass

    def stop(self):
        # !!! TODO
        pass

    def get_ipv4(self):
        # !!! TODO
        pass

    def get_url(self):
        # !!! TODO
        pass

    def create_inbound_rule(self):
        # !!! TODO
        pass

    def delete_inbound_rule(self):
        # !!! TODO
        pass
