import subprocess
import sys


def ldd_of_shared_object(shared_objects, executable):
    std_out = run_bash_command(["ldd", str(executable).strip()])
    return std_out_to_shared_objects(shared_objects, std_out)


def std_out_to_shared_objects(shared_objects, std_out):
    for std_out_line in convert_std_out_to_list(std_out):
        find_dependencies(shared_objects, std_out_line)
    return shared_objects


def find_dependencies(shared_objects, std_out_line):
    line_list = std_out_line.split(" ")
    shared_object_name = line_list[0].strip()
    if shared_object_name not in shared_objects.keys():
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
    popen = subprocess.Popen(command, stdout=subprocess.PIPE)
    std_out, std_err = popen.communicate("")
    write_file(command, std_out)
    return std_out


def write_file(command, std_out):
    with open("tests/fixtures/{0}.txt".format("_".join(command).replace("/", "_")), 'w') as f:
        f.write(std_out)


if __name__ == "__main__":
    for directory in sys.argv[1:]:
        main(directory)
