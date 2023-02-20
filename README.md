# Custom Nautobot Plugin for Ixia Chassis 

<p align="center">
    <img src ="images/ixia_logo.png" width='200'>
</p>

A nautobot plugin for Ixia XGS12 Chassis Platform. The goal of this plugin is to have separate view for Ixia chassis with attributes like modules, tenat, status, port and description.

### Installation

* Testing Locally 

	`$ git clone https://github.com/uthapa82/nautobot-plugin-ixia.git`

* Once cloned, start the development environment 
	
	```
	$ poetry shell
	$ poetry install 
	$ invoke build debug
	
	```
	
* Sudo to nautobot
	`$ sudo -iu nautobot`

* Prepare the Database 
	`$ nautobot-server migrate `	
	
* Create a Superuser 
	`$ nautobot-server createsuperuser`
	
	
* Starting Nautobot's development server on port XXXX, here 8000

	`$ nautobot-server runserver 0.0.0.0:8000 --insecure`
