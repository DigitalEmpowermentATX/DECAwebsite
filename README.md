# DECAwebsite

A website that delivers information about digital inclusion training, events, and locations in the Austin area

## Development

### Nanobox

If you want an environment that is similar to the production environment on the server, you can use Nanobox!
Nanobox will setup the database, python dependencies and networking for you.
For documentation on nanobox visit https://docs.nanobox.io

#### Downloading Nanobox

It is highly recommended that you use the VirtualBox version of Nanobox
Download Nanobox from https://nanobox.io

#### Local Development

##### Running Nanobox

Head to the project directory

```bash
cd digital_inclusion
```

If you are using Windows, it is recommended that you switch the file-system used by nanobox to native

```bash
nanobox configure set mount-type native
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

You should be able to access the website from http://django.local:8000

#### Deployment

##### Local Deployment (dry-run)

Head to the project directory

```bash
cd digital_inclusion
```

If you are using Windows, it is recommended that you switch the file-system used by nanobox to native

```bash
nanobox configure set mount-type native
```

You will need to add the dry-run dns

```bash
nanobox dns add dry-run django.dry
```

Deploy application

```bash
nanobox deploy dry-run
```

The app should be available at http://django.dry

##### Live Deployment

Head to the project directory

```bash
cd digital_inclusion
```

If you are using Windows, it is recommended that you switch the file-system used by nanobox to native

```bash
nanobox configure set mount-type native
```

You will need login to nanobox

```bash
nanobox login
```

Add the deca remote

```bash
nanobox remote add deca
```

Deploy application

```bash
nanobox deploy
```

The app should be available at https://deca.nanoapp.io or the live domain of the application