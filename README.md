# ML_Project


# Software and account requirements.
1. [Github Account](https://github.com/)
2. [Cyclic Account](https://app.cyclic.sh/#/account)
3. [VS Code](https://code.visualstudio.com/Download)
4. [GIT cli]()

# Creating conda env

```
conda create -p venv2 python

```

```
conda activate venv2/
```

```
pip install -r requirements.txt
```

add files to git

```
git add .
```

>Note: to ignore folder- write name of file /folder in hitignore file

To check git status
```
git status
```

To check all version mainatined a git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send changes to guitgub

```
git push origin main
```

To check commond url
```
git remote -v
```

To set up CI/CD pipeline Cyclic


BUID DOCKER IMAGE

```
docker build -t<image_name>:<tagname> .
```
>Note: Image name for docker must be lowercase


To list docker images
```
docker images
```

Run docker images
```
docker run -p 5000:5000 -e PORT=5000 <id>
```

To check running containers in docker

```
docker ps
```

To stop docker container
```
docker stop <container_id>
```








