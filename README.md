# DECAwebsite
A website that delivers information about digital inclusion training, events, and locations in the Austin area

# Development
## Nanobox
If you want an environment that is similar to the production environment on the server, you can use Nanobox!
Nanobox will setup the database, python dependencies and networking for you. 
### Downloading Nanobox
Download Nanobox from https://nanobox.io
### Running Nanobox
Head to the project directory
```bash
cd digital_inclusion
```
You will need to add the local dns
```bash
nanobox dns add local django.local
```
You will then need to build the runtime so that the database/requirements are installed. You will need to do this everytime your requirements.txt file changes
```bash
nanobox build-runtime
```
Migrate the database
```bash
nanobox run python manage.py migrate
```
Run the application
```bash
nanobox run python manage.py runserver 0.0.0.0:8000
```
