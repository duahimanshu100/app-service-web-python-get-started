# leapfrog-api
Leapfrog Api

# Setup Project On local
  - Install Python3.7
  - Install Virtualenv `pip install virtualenv`
  - Create a Virtualenv outside of the project folder `virtualenv /path/virtual-env-folder --python=python3.7`
  - Activate the Virtualenv `source /path/virtual-env-folder/bin/activate`
  - Go to your repo folder and install requirements by `pip install -r requirements.txt`. This will install all the python requirements in the newly created Virtualenv
  - Now you can run the django project by python manage.py runserver
  
    #RUN flower

    celery -A cis flower

    #RUN celery beat

    celery -A cis worker -B -l info

# Create Azure Web app
- Install azure cli and add your creds follow  [this](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
- az webapp up --resource-group cis --location eastus --plan cis-django-dev --sku B1 --name cis-django-dev

# Deploy changes to Azure Web app
- az webapp up
- For installing any new libs use following cmds
- `cd site/wwwroot`
- `apt-get update`
- `apt-get install g++`
- `apt-get install unixodbc-dev`
- Activate default virtual environment in App Service container `source /antenv/bin/activate`
- Run database migrations `python manage.py migrate`

# Setup new email Scrapper over virtual machine
- sudo apt update
- sudo apt install python-pip
- sudo apt-get install python3-dev
- sudo apt-get install python3.7-dev
- sudo su
- curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
- curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
- sudo apt-get update
- sudo ACCEPT_EULA=Y apt-get install msodbcsql17
- optional: for bcp and sqlcmd
- sudo ACCEPT_EULA=Y apt-get install mssql-tools
- echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
- echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
- source ~/.bashrc
- optional: for unixODBC development headers
- sudo apt-get install unixodbc-dev
- exit
- sudo apt install virtualenv
- sudo add-apt-repository ppa:deadsnakes/ppa
- sudo apt update
- sudo apt-get install g++
- sudo apt-get install unixodbc-dev
- sudo apt install redis-server
- sudo systemctl restart redis.service
- virtualenv ~/venv --python=python3.7
- source ~/venv/bin/activate
- pip install -r requirements.txt
- celery -A cis flower --basic_auth=user1:password1,user2:password2
- celery -A cis worker -B -l info
- Goto serverip:5555 , you will see the flower task monitoring
