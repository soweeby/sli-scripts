# sli-scripts
scripts to make grading easier for me

### Required Dependencies
- openpyxl (for `spreadsheet.py` - can be installed with `pip install openpyxl`)

### File Structure
Here are the main files and their descriptions.

1. `extract.py`
This script extracts the zip file downloaded from myCourses and stores the extracted files (the students' actual submissions into a folder). It then goes into the new folder to extract the students' zip folders into new folders with their name.

2. `tests\**<assignment>.py**`
These files are specific for each lab's testing setup. More explanation will be added as I become familiar with the grading procedure in future weeks.

3. `tests\scripts\`
These files are general automated operations that can be used with any labs. They will most likely be imported for by a **<assignment>.py** file.

## Changelog

### 1/14/22
### Added
- extract script
- test script for lab 1
- README.md

## 1/27/22
## Added
- script for creating Intellij configuration elements for c+p into xml file
## Changed
- file structure for tests: new `scripts\` directory for general scripts

## 1/29/22 (start of things unique to roshan's fork)
## Added
- created `spreadsheet.py`, a script for generating grading spreadsheet with a list of students and cells for their pss, inlab, and lab grades, as well as a formula to calculate the total grade for each student.
## Changed
- fixed `extract.py` to work for linux file paths