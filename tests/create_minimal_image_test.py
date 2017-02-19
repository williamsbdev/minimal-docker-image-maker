from unittest import TestCase

import create_minimal_image
from create_minimal_image import main

POPEN_COMMAND_LIST = []


class CreateMinimalImageTest(TestCase):

    def setUp(self):
        global POPEN_COMMAND_LIST
        POPEN_COMMAND_LIST = []
        create_minimal_image._run_popen_command = stubbed_run_popen_command

    def test_main_will_correctly_return_shared_objects_and_locations(self):
        main('/usr/lib/jvm')
        self.assertEquals(POPEN_COMMAND_LIST, get_expected_popen_comands())


def stubbed_run_popen_command(command):
    POPEN_COMMAND_LIST.append(" ".join(command))
    try:
        with open("tests/fixtures/{0}.txt".format("_".join(command).replace("/", "_")), 'r') as f:
            std_out = f.read()
        return std_out
    except:
        return ""


def get_expected_popen_comands():
    with open("tests/fixtures/expected_popen_commands.txt", "r") as f:
        expected_popen_commands = f.read().split("\n")
    return [command for command in expected_popen_commands if command != ""]
