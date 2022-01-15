import shutil
import os

LAB_DIR = '..\..\Final-Lab_1'
SOLUTION_DIR = 'solution_files'
STUDENT_PATH = 'src\poly'


def loop_students():
    with os.scandir(LAB_DIR) as students:
        for student in students:
            if student.is_dir():
                print(f'* Moving to {student.name}')
                copy_sol_files(student.name)


def copy_sol_files(student_dir):
    with os.scandir(SOLUTION_DIR) as files:
        for file in files:

            # what we are naming it
            src_dir = f'{SOLUTION_DIR}\{file.name}'
            dest_dir = f'{LAB_DIR}\{student_dir}\{STUDENT_PATH}\{file.name}'

            if file.is_dir():
                print(f'\t * Moving directory {file.name}')
                shutil.copytree(src_dir, dest_dir)
            else:
                print(f'\t * Moving test file {file.name}')
                shutil.copy(src_dir, dest_dir)


def main():
    print('==== Moving files.... ====')
    loop_students()
    print('Finished moving')


if __name__ == '__main__':
    main()
