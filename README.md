# Fast API

### For Deploying LLM Models.
To do it, at first we will install it:

### ``` pip install "fastapi[standard]" ```



### Run FastAPI(file name should be main.py):

### ```fastapi dev main.py```

### For JSON Response:
### Visit: `127.0.0.1:8000`

### For Interactive API:
### Visit: `127.0.0.1:8000/docs`

### For ALternative API with automatic documentation:
### Visit: `127.0.0.1:8000/redoc`

### For JSON Response:
### Visit: `127.0.0.1:8000/openapi.json`



## Deployment

To deploy, we have to create pyproject.toml file with necessary info. Then the process is very easy.

### Login fastapi:
### ```fastapi login```

Then a window will open for authenticate. So, before doing that we have to create an account in `fastapicloud.com`
After verifying the authentication, it will show

``` Now you are logged in! 🚀```

### Run deploy command:
### ```fastapi deploy```

It will ask some question, answer them. And you will get a link for your project.
