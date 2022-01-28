import os
from pathlib import Path
from zipfile import ZipFile
from datetime import datetime


# dictionary - name and time modified as value
def get_assign_name():
    assign_type = input('Type [(f)inal-lab, (p)re-lab]: ').lower()
    if assign_type not in ['f', 'p']:
        assign_type = input('Please try again [(f)inal-lab, (p)re-lab]: ').lower()

    assign_num = int(input('Number [1-9]: '))
    if assign_num not in range(1, 10):
        assign_num = int(input('Please try again [1-9]: '))

    assign_name = "Final" if assign_type == 'f' else "Preliminary"
    assign_name += "-Lab "
    assign_name += str(assign_num)

    return assign_name


def extract_sequence(assign_name):
    filename = None
    with os.scandir() as files:
        for file in files:  # file is a zip file
            if file.name.startswith(assign_name):
                filename = file.name
                break

    if filename is None:
        print('Filename is not found. Please restart the program.')
        exit(0)

    print('==== Extracting downloading folder.... ====')
    new_folder = assign_name.replace(' ', '_')
    extract(filename, new_folder)
    print('Finished and removing zip folder....')

    print('==== Extracting submissions folder.... ====')
    submits = Path(new_folder)
    for sub in submits.glob('*.zip'):
        student_name = sub.name.split(' - ')[1]
        sub_date = sub.stat().st_mtime
        print(f' * Extracting "{student_name}", Submitted @ {convert_date(sub_date)}....')
        extract(f'{new_folder}/{sub.name}', f'{new_folder}/{student_name}')
        os.remove(f'{new_folder}/{sub.name}')
    print('Finished extracting submissions!')

    print('==== Deleting original files... ====')
    os.remove(filename)
    print('==== Finished deleting files ====')


def extract(zipped_dir, target_dir):
    with ZipFile(zipped_dir) as zipfile:
        zipfile.extractall(target_dir)


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    return d.strftime('%a (%m %d)')


def main():
    print('Time to Gradeeeee!')
    assign_name = get_assign_name()
    extract_sequence(assign_name)


if __name__ == '__main__':
    main()