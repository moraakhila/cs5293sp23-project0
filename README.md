# cs5293sp23-project0

# Akhila Mora

In this project, pdf of incident summary report is downloaded from the given link of norman.gov website. These incidents are stored in 5 columns in pdf. Our goal of the project is to read the content of the incidents from the pdf and create a database and then return the total number of incidents sorted numerically in decending order and the name of incidents in alphabetical order. This project is developed in Ubuntu in GCP using python. Finally, the output is displayed by seperating nature and incidents using pipe symbol (|)

## Author Details

* Name: Akhila Mora
* Email: akhila.mora@ou.edu
* Student ID: 113531532

## Getting Started

Below are the starting steps which needs to be done before starting the project:
* In Ubuntu, connect to the VM instance using the following command:
```
ssh -i [path-to-private-key] [username]@[instance-external-ip]
```
* Create a tree structure as shown below in VM instance:
* ![image](https://user-images.githubusercontent.com/113566461/223599377-694e9a43-802d-48dc-87a5-bb061611409b.png)
* We need to have python installed in the instance. If not, install it using below command:
```
sudo apt-get install python3
```

### Demo video

![Trim](https://user-images.githubusercontent.com/113566461/223597503-c0186072-e06b-4a0b-a517-4122be8fb15d.gif)

### Packages

* urllib
* pypdf
* tempfile
* re
* sqlite3
* argparse
* pytest
* os
* sys

### Executing program

Here is the step by step explanation to run the project.
* Clone the project into your instance:
```
git clone https://github.com/moraakhila/cs5293sp23-project0.git
```
* Change the current working directory to cloned repository:
```
cd cs5293sp23-project0
```
* Create a virtual environment
```
pipenv install
```
* Activate virtual environment
```
pipenv shell
```
* Install necessary packages
```
pipenv install pypdf
pipenv install pytest
```
* Run the project using ```main.py```
```
pipenv run python project0/main.py --incidents https://www.normanok.gov/sites/default/files/documents/2023-02/2023-02-01_daily_incident_summary.pdf
```
* Below is the output
* ![image](https://user-images.githubusercontent.com/113566461/223601116-074cac54-5a86-45b2-89a4-c65e7fc585ff.png)
* Running pytests using below command:
```
pipenv run python -m pytest
```

## Modules

* main.py
   * This file is created in the directory project0 which call the functions of project0.py by importing the project0 directory and its functions and execute then by using command provided above. 
* extractdata.py
   * This script uses pypdf, re, and tempfile modules to extract data from PDF files. It processes the data page by page using pypdf, and stores the information in a list of lists. The script handles empty cells by replacing them with the 'NaN' value, and takes care of double lines as well. 
* databaseop.py
   * createdb - creates a database normanpd.db and returns database 
   * populatedb - to insert data into incidents table in normanpd.db 
   * status - Output is a list sorted first by the total number of incidents and secondarily, alphabetically by the nature. The output is seperated by a pipe (|)

## Pytest cases

Below are the functions that are present in test_main.py
* test_fetch_incidents(url)
   * It returns True if the fetched data is an URL.
* test_extract_data(url)
   * Asserts if the length of incidents is greater than 0 and incident count is found.
* test_createdb(database_name)
   * Checks if the query is executed correctly by comparing the length of result which should be equal to 1 
* test_populatedb(database_name)
   * Checks if the query is executed correctly by comparing the count of result which should be greater than 0 
* test_status(database_name)
   * Asserts if the result is not none.

## Assumptions

Below are the assumptions which I made for this project:
1. I considered that incident ORI column has only 4 values: OK0140200, EMSSTAT, 14005, 14009.
2. I wrote a regex with an assumption that Location is in capital letters and nature is in small letters.

## Bugs

1. If there is no necessary packages, the code might not work.
2. If we run the program multiple times, there will be duplicates in database.


## Acknowledgments

* [ Github README.md ](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [W3 Schools](https://www.w3schools.com/python/python_regex.asp)
