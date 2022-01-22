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

        # determines if student has correct file structure
        place_dir = f'{LAB_DIR}\{student_dir}\{STUDENT_PATH}'
        if os.path.isdir(place_dir):

            for file in files:

                src_dir = f'{SOLUTION_DIR}\{file.name}'
                dest_dir = f'{LAB_DIR}\{student_dir}\{STUDENT_PATH}\{file.name}'    # what we are naming it

                if file.is_dir():
                    shutil.copytree(src_dir, dest_dir)
                    print(f'\t * Moving directory {file.name}')
                else:
                    shutil.copy(src_dir, dest_dir)
                    print(f'\t * Moving test file {file.name}')

        else:

            print(f'!! {student_dir} does not have the correct file structure... Do manually')


def main():
    print('==== Moving files.... ====')
    loop_students()
    print('Finished moving')


if __name__ == '__main__':
    main()
