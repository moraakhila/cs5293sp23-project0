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

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments


Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
