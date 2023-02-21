# Custom Nautobot Plugin for Ixia Chassis 

<p align="center">
    <img src ="images/ixia_logo.png" width='200'>
</p>
<h5 align='center'>Development Environment</h5>

<p align='center'>

<a href="https://www.postgresql.org/" target="_blank">![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)</a> <a href="https://www.djangoproject.com/" target="_blank">![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)</a> <a href="https://www.python.org" target="_blank">![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)</a> <a href="https://docs.docker.com/get-docker/" target="_blank">![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)</a> <a href="https://python-poetry.org/" target="_blank"><img src="https://img.shields.io/badge/packaging-poetry-cyan.svg" height="28"/> </a> <a href="https://redis.io/" target="_blank">![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white) <a href="https://code.visualstudio.com/" target="_blank">![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)</a>

</p>

### Overview
A nautobot plugin for Ixia XGS12 Chassis Platform. The goal of this plugin is to have separate view for Ixia chassis with attributes like modules, tenat, status, port and description.

### Installation
The plugin will be available soon as a Python package in PyPI and can be installed with `pip`:

	$ pip3 install nautobot-plugin-ixia

To ensure the nautobot-plugin-ixia is automatically re-installed during the future upgrades, create a file named **local_requirements.txt** (if not already existing) in the Nautobot root directory ( alongside **requirements.txt**) and list the nautobot-plugin-ixia packages :

	$ echo nautobot-plugin-ixia >> local_requirements.txt

Once installed teh **nautobot_config.py** needs to be updated with following:

	PLUGINS = ["nautobot-plugin-ixia"]

Testing Locally 

	$ git clone https://github.com/uthapa82/nautobot-plugin-ixia.git

Once cloned, start the development environment 
	
	
	$ poetry shell

	$ poetry install 

	$ invoke build debug
	
### Screenshots


### Useful Commands 
* Docker Status and troubleshooting commands
	```properties
	$ sudo systemctl status docker
	$ sudo systemctl enable--now docker
	$ docker volume ls
	$ doker volume rm <name_of_process_to_remove>
	$ docker ps
	$ docker ps -a 
	$ docker prume 

	# stop exiting redis and postgresql service 
	$ sudo service redis-server stop
	$ sudo service postgresql stop

	# list and kill the postgres and redis ports used 
	$ sudo lsof -i -P -n | grep <5432 or 6379>
	$ fuser -n tcp -k <port_number>
	
	```

* Remove existing virtual environment and recreate 

	```properties
	$ rm -rf~/.cache/pypoetry/virtualenvs/nautobot-plugin-<tab>

	$ poetry shell 
	# might need to select the interpreter explicitly in vscode after this command 

	#uninstall nautobot
	$ pip3 uninstall -y nautobot

* Poetry version and lock file incompatible 
	
	```properties 
	$ poetry lock --no-update
	$ poetry install 
	
	#installing specific version of nautobot 
	$ poetry add nautobot=1.4.5
	$ poetry add nautobot ---> this will install most recent stable version 

	```
* Sudo to nautobot

	`$ sudo -iu nautobot`

* Prepare the Database 

	`$ nautobot-server migrate `	
	
* Create a Superuser 

	`$ nautobot-server createsuperuser`
	
* Starting Nautobot's development server on port XXXX, here 8000

	`$ nautobot-server runserver 0.0.0.0:8000 --insecure`

### Documentation-References-Acknowledgements
* [Official Nautobot Docs](https://docs.nautobot.com/)
* [Code Reference](https://docs.nautobot.com/projects/core/en/stable/plugins/development/#extending-object-detail-views)
* Existing Plugin used as a Reference for this development
	* [nautobot-plugin-golden-config](https://github.com/nautobot/nautobot-plugin-golden-config)
	* [nautobot-plugin-netbox-importer](https://github.com/nautobot/nautobot-plugin-netbox-importer)
	* [nautobot-polugin-data-validation-engine](https://github.com/nautobot/nautobot-plugin-data-validation-engine)

* Special thanks to [@nautobot slack community](http://slack.networktocode.com/) for answering the questions and guidelines
