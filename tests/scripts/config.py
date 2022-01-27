import os

CONFIG_TEMPLATE = open('scripts/config_template.txt', 'r').read()


def loop_students(lab_dir, sol_path, config_dict):
    with os.scandir(lab_dir) as students:
        for student in students:
            if student.is_dir():
                print(f'* Creating configs for {student.name}')
                add_to_config(student.name, sol_path, config_dict)


def add_to_config(student_dir, sol_path, config_dict):
    # create a config file
    config_file = open("config_file.txt", "a")

    for class_name in config_dict:

        for solution_file in config_dict[class_name]:

            print(f'\t - making config {solution_file}')

            config = CONFIG_TEMPLATE.format(
                config_name=student_dir + " - " + solution_file,
                class_name=class_name,
                module_name=student_dir,
                cmd_params=config_dict[class_name][solution_file],  # command line parameters
                solution_path=sol_path + "/" + solution_file,
            )

            config_file.write(config + '\n')


def execute(lab_dir, sol_path, config_dict):
    """
    :param lab_dir: Where the student directories are stored
    :param sol_path: Where the solution files are stored
    :param config_dict: The configurations to make
    """
    print('==== Creating Configurations.... =====')
    loop_students(lab_dir, sol_path, config_dict)
    print('Finished creating configurations')
