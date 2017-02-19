import subprocess
import sys

INVOCATION_COUNT = 0


def ldd_of_shared_object(shared_objects, executable):
    std_out = run_bash_command(["ldd", str(executable).strip()])
    return std_out_to_shared_objects(shared_objects, std_out)


def std_out_to_shared_objects(shared_objects, std_out):
    for std_out_line in convert_std_out_to_list(std_out):
        line_list = std_out_line.split(" ")
        find_dependencies(shared_objects, line_list)
    return shared_objects


def find_dependencies(shared_objects, line_list):
    shared_object_name = line_list[0]
    if shared_object_name not in shared_objects:
        if len(line_list) > 3 and line_list[2] not in ('', 'not'):
            shared_objects[shared_object_name] = line_list[2]
        if len(line_list) == 2 and shared_object_name not in ['statically']:
            shared_objects[shared_object_name] = shared_object_name
        if shared_object_name in shared_objects:
            ldd_of_shared_object(
                    shared_objects,
                    shared_objects[shared_object_name]
            )
    return shared_objects


def convert_std_out_to_list(std_out):
    return std_out.replace("\t", "").strip().split("\n")


def main(directory):
    find_command = ['find', directory, '-type', 'f', '-perm', '/a+x', '-exec', 'ldd', '{}', ';']
    jvm_find_std_out = run_bash_command(find_command)
    shared_objects = std_out_to_shared_objects({}, jvm_find_std_out)
    return shared_objects


def run_bash_command(command):
    global INVOCATION_COUNT
    popen = subprocess.Popen(command, stdout=subprocess.PIPE)
    std_out, std_err = popen.communicate("")
    write_file(std_out)
    INVOCATION_COUNT += 1
    return std_out


def write_file(std_out):
    with open("tests/fixtures/output_{0}.txt".format(INVOCATION_COUNT), 'w') as f:
        f.write(std_out)


if __name__ == "__main__":
    for directory in sys.argv[1:]:
        main(directory)
