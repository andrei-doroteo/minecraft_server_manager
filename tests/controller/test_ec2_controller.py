"""
test_ec2_controller.py

this module contains tests for the Ec2 class
in the ec2_controller module
"""

import json

import pytest

from controller.ec2_controller import Ec2


@pytest.fixture(scope="module")
def credentials():
    with open("env/env.json") as data:
        credentials = json.load(data)

        return (
            credentials["region"],
            credentials["aws_access_key_id"],
            credentials["aws_secret_access_key"],
            credentials["ec2_instance_id"],
        )


class TestEc2:

    @pytest.fixture(autouse=True)
    def setup_aws(self, credentials):
        region, access_key_id, secret_access_key, ec2_instance_id = credentials

        self.ec2 = Ec2(
            ec2_instance_id, region, access_key_id, secret_access_key
        )

    def test_init(self):
        # !!! TODO
        pass
