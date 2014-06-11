SPC REST Service
================
These instructions leverage this repository / fork. This is a fork from Matt's code, available at https://github.com/baldwinSPC/spc-rest-service.git

The Setup
---------

First, let's grab the code:

`````
git clone https://github.com/StackPointCloud/spc-rest-service.git
`````

Want to grab a branch?
```
git clone -b branchName https://github.com/StackPointCloud/spc-rest-service.git
```

Next, let's get it running:

`````
cd spc-rest-service
mkvirtualenv your_virtual_env_name
pip install -r requirements.txt
python manage.py runserver
`````

Notes
---------
To keep your global environment clean, make sure you use 'workon [project]' 

For information on setting up Virtual Environments in Python, visit:

- [Virtual Environment - The Hitchhikers Guide to Python](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
- [Installation - virtualwrapper documentation](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)
- [Command Reference - virtualwrapper documentation](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html)