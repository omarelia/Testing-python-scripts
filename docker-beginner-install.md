# Docker for beginners
If you have problems running the enviroment, please follow this steps
This tutorial is a simplied extension of the [official instruction](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

# Steps
Ensure get docker community edition from an updated repository

```sh
$ sudo apt-get update
$ sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
```
Download repository info
```sh
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
Verify that you now have the key with the fingerprint 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88, by searching for the last 8 characters of the fingerprint.
```sh
sudo apt-key fingerprint 0EBFCD88
```
**Now you are ready for update and install Docker CE using our friend apt**
```sh
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```
> If for any reason (frenquently by cause OSI 8th layer error), you need **re-install docker-ce**, you alredy have registered the repository from Docker Community Edition, so, just run 
>
> **sudo apt-get purge docker-ce docker-ce-cli containerd.io**
> **sudo rm -rf /var/lib/docker**
>
> and repeat the command
>
> **sudo apt-get install docker-ce docker-ce-cli containerd.io**


### 2. Post config - Don't run Docker being root (sudo) 
You **should not** develop or make changes in your enviroment as [**root user**](https://stackoverflow.com/questions/33643099/is-it-a-good-practice-to-always-use-root-user-in-development-environment) 
Thats concept apply also when you try create containers in docker being root user

[According this instruction](https://docs.docker.com/install/linux/linux-postinstall/) follow the next steps to use docker without sudo command

Create the docker group.
```sh
$ sudo groupadd docker
```

Add your user to the docker group.
```sh
$ sudo usermod -aG docker $USER
```

### 3. Is your docker correctly installed?
```sh
docker run hello-world
``` 
Any problems? See the [official instalation instructions](https://docs.docker.com/install/linux/linux-postinstall/)

