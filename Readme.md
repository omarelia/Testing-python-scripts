# Python Test. python script testing


## Requirements

Install this pre-requisites and follow the steps

-   Docker CE  [Install Docker Community Edition version 18.09.04 or up](https://docs.docker.com/install/linux/docker-ce/ubuntu/)  according this instructions Need more help? Follow this instruction for  [beginners users](https://github.com/pablogottifredi/boilerplate-python-script/blob/master/docker-beginner-install.md)
    
-   Docker Compose cli  [Install Docker Compose cli](https://docs.docker.com/compose/install/)
    

## Quickview
The entire code here, just open [test.py](test.py)

## Getting started

### 1. Get from repo

Clone using your own credentials from repo  [https://github.com/omarelia/testing-python-scripts.git](https://github.com/omarelia/testing-python-scripts.git)

```
$ git clone https://github.com/omarelia/testing-python-scripts.git

```

### 2. Access to subfolder

```
$ cd testing-python-scripts

```

### 3. Changes values in .env

'''

$ cp .env.example .env

'''

In the variable called 'url', this is where the data source url will be placed

### 4. Run using docker-compose

All the environment is ready to use without aditional install

> Use  _**docker-compose up**_  into testing-python-scripts folder

```
:~testing-python-scripts$ docker-compose up

```

Ready!
