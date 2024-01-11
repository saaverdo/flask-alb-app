## Simple app
This simple flask app is for load balancer/auto-scaling demonstration.  
It'll show client's IP and server's hostname.  

## Installation:
### Install app
#### install packages required for app

```
sudo apt install -y python3-pip
```

#### install app and dependencies

```
git clone https://github.com/saaverdo/flask-alb-app -b alb

cd flask-alb-app

sudo pip install -r requirements.txt
```

### Run app

```
gunicorn -b 0.0.0.0 app:app
```

App will be available via url `http://<instance_dns_or_ip>:8000`  

   
