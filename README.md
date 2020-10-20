# nornir_flask (Simple NetApp)


[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/veprimk/nornir_flask)

This simple Web App will read your Nornirs hosts.yaml inventory file and will render the results in  a user friendly HTML Table.

## Use Case Description

This would be a good use case for automation engineers to develop a customer care (user) friendly application which can be used to check devices by simply clicking through hyperlinks instead of having to log in into network devices.
In return they will be able to easily and quickly find network device information.

## Configuration

The code allows for further customization as well as add more features. Knowledge of Nornir, Flask and HTML/JavaScript is required.

## Installation

Clone the repository into your Workstation:
```


git clone https://github.com/veprimk/nornir_flask.git

cd nornir_flask/
```

### Linux/Mac Users

```
python3.8 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

chmod 777 start_app.sh

./start_app.sh

```

### Windows Users

Create environment:
```
create_environment.bat
```

Install dependencies
```
pip install -r requirements.txt
```

Start APP
```
start_app.bat
```



## Usage

![Img](Home.png)

Each device is an anchored link which has been crafted to pass the device name as a parameter to the Flask url route decorator which then passes further to the function which calls Nornir get_facts function.
Results then are again rendered in the HTML Table:
![Img](Facts.png)


## Execution flow

![Img](nornir_flask_flow.png)


## How to test the software

Create or edit a Nornir Inventory based on the given example in *hosts.yaml* and *groups.yaml* files and then simply start the application.

### DevNet Sandbox
The hosts.yaml file contains the details to IOS XE on CSR1000V Always-On which is available from DevNet Sandbox and that can be used to test the application.

## Known issues
If you have questions, concerns, bug reports, etc., please create an issue against this [GitHub Repo](https://github.com/veprimk/nornir_flask/issues) and please make sure to include your code and the error log/traceback.


## TODO

1. Extend further to show arp table
2. Extend further to show routing table
3. Extend to show interface statistics
4. Etc.

## Getting involved

If you would like to get involved, please create a pull requests and make your changes.

## Author(s)

This project was written and is maintained by the following individuals:

* Veprim Krasnici <veprimk@gmail.com>