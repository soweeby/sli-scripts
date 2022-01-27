import shutil
import os


def loop_students(lab_dir, sol_dir, stu_path):
    with os.scandir(lab_dir) as students:
        for student in students:
            if student.is_dir():
                print(f'* Moving to {student.name}')
                copy_sol_files(student.name, lab_dir, sol_dir, stu_path)


def copy_sol_files(student_dir, lab_dir, sol_dir, stu_path):
    # determines if student has correct file structure
    dest_dir = f'{lab_dir}\{student_dir}\{stu_path}'
    if os.path.isdir(dest_dir):

        src_dir = f'{sol_dir}\{file.name}'
        dest_dir += f'\{file.name}'  # what we are naming it

        with os.scandir(sol_dir) as files:
            for file in files:
                if file.is_dir():
                    shutil.copytree(src_dir, dest_dir)
                    print(f'\t * Moving directory {file.name}')
                else:
                    shutil.copy(src_dir, dest_dir)
                    print(f'\t * Moving test file {file.name}')

    else:
        print(f'!! {student_dir} does not have the correct file structure... Do manually')


def execute(lab_dir, sol_dir, stu_path):
    """

    :param lab_dir:
    :param sol_dir:
    :param stu_path:
    :return:
    """
    print('==== Moving files.... ====')
    loop_students(lab_dir, sol_dir, stu_path)
    print('Finished moving')
