"""
creates a grading spreadsheet (.xlsx) in
the directory this script is run

author: Roshan Nunna
"""

from openpyxl import Workbook


def create_classlist():
    """
    creates a classlist from classlist.txt
    :return: a list of names in the class
    """
    classlist = []
    with open('classlist.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line != "":
                classlist.append(line)
    return classlist


def create_spreadsheet(classlist):
    """
    creates a spreadsheet from a classlist
    :param classlist: list of names from the class
    :return: nothing
    """
    f = 'grading.xlsx'
    workbook = Workbook()
    sheet = workbook.active

    sheet["A1"] = "Name"
    sheet["B1"] = "PSS"
    sheet["C1"] = "InLab"
    sheet["D1"] = "Lab"
    sheet["E1"] = "Total"

    for i in range(2, len(classlist) + 2):
        sheet[f'A{i}'] = classlist[i - 2]  # adds student name into name column
        sheet[f'E{i}'] = f'=B{i} + C{i} + D{i}'  # adds grade formula into 'total' column

    workbook.save(filename=f)  # saves workbook to 'grading.xlsx', makes a new file named that if it doesn't exist yet.


def main():
    create_spreadsheet(create_classlist())


if __name__ == '__main__':
    main()
