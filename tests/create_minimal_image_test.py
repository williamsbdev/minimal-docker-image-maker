import json
from unittest import TestCase

import create_minimal_image
from create_minimal_image import main


class CreateMinimalImageTest(TestCase):

    def setUp(self):
        create_minimal_image._run_bash_command = stubbed_run_bash_command

    def test_main_will_correctly_return_shared_objects_and_locations(self):
        result = main('/usr/lib/jvm')
        with open("tests/fixtures/expected_openjdk_java1.8.0_121.txt", "r") as f:
            expected_result = json.loads(f.read())
        self.assertEquals(len(expected_result.keys()), 40)
        self.assertEquals(expected_result, result)


def stubbed_run_bash_command(command):
    with open("tests/fixtures/{0}.txt".format("_".join(command).replace("/", "_")), 'r') as f:
        std_out = f.read()
    return std_out
