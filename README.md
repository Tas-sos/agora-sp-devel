# Agora

The service portfolio management tool is a tool that allows a company / project to manage the portfolio of services they to maintain (offered to users / customers or internal).
Agora provides an intuitive user interface which allows users to create/edit/update/delete their services and components. Users can login with credentials provided by the administrator, or use the shibboleth login functionality to login with their academic account.


### Dependencies

* [git](https://git-scm.com/)
* [virualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
* [pip](https://pypi.python.org/pypi/pip)
* [NodeJS](https://nodejs.org/en/download/)
* [Yarn](https://yarnpkg.com/en/docs/install)


## Development instructions

### Get the code

```
git clone https://github.com/grnet/agora-sp.git
```

### Create a virtualenv for agora

```
cd agora
mkvirtualenv agora
```

### Install requirements

With virtualenv activated install python dependencies:

```
pip install -r requirements.txt
```

Then run `yarn` inside the `ui` directory to install npm depending libraries.

### Configuration

#### Backend configuration

You can create a configuration file in order to override the default settings for the agora project. The default location of the .conf file is `/etc/agora/settings.conf`

The default contents of `settings.conf` are:

```
SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/db.agora.sqlite3'
    }
}

DATABASES = SQLITE
EMAIL_FILE_PATH = '/tmp/agora/agora_emails'
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
```

You should override it with your database settings, [you can read more information here](https://docs.djangoproject.com/en/1.11/ref/databases/).


**NOTE:** You must create a `log` folder containing a `debug.log` file in your base project directory or configure LOGGING setting with custom log options.


Finally, you should also create a `deployment.conf` file which should specify the `root_url` attribute to reflect the url of the backend server.

The default location of `deployment.conf` is in '/etc/agora/`.

Example: 

```
{
    ":root_url": "http://127.0.0.1:8000"
}
```


#### UI configuration

You can edit the `ui/config/environment.js` file to set the default configuration options. You can alter the value of `rootURL` and `appURL` that define where the ui is served and what is the main endpoint  where the backend is located.

Example options:

```
var ENV = {
  rootURL: '/ui/'
  appURL: '/api/v2/',
}
```

#### UI Customization

You can customize the appearance of your installation by adding your own logo, style and domestic login method text.

You can place your own logo inside `public/assets` directory under the name `logo.png`.
You can also use a custom preprocessed stylesheet, which you should place inside `styles` folder.
In order to process it and import it, you have to edit `ui/config/environment.js` file and set the `theme` option to match the name of the stylesheet `my-themes.scss`:

```
var ENV = {
    theme: 'my-theme',
}
```

In case you want to alter the text for domestic login method, you can change the configuration option in `config/environment.js` as follows:

```
var ENV = {
  APP: {
    domestic_login_msg: "My login method"
  }
}

```

You can additionally customize the content of the footer. 
The available options can be found in `ui/config/environment.js` file:

```javascript
APP: {
  footer: {
    // If set, "Copyright © <copyright_years>" will appear in footer.
    copyright_years: '2018-2019',
    // If set, contact info  will be visible next to version in footer.
    contact: 'contact@example.com',
    // If set, <info> will be visible in footer.
    info: 'Agora is a service developed and maintained by <a href="https://grnet.gr/en/" alt="grnet">GRNET</a> co-funded by <a href="" alt="https://www.eosc-hub.eu/">EOSC-Hub</a> and <a href="https://www.eudat.eu/eudat-collaborative-data-infrastructure-cdi">EUDAT CDI</a>',
    // If set, a link will <policy_text> text will be visible in footer.
    policy_text: 'Privacy Policies',
    // If set, <policy_text> link will  redirect to <policy_url>. If not set,
    // <policy_text> link will point to policy.hbs template.
    policy_url: 'http://www.example.com',
    // If  set, logos will be visible in footer.
    logos: [{
      url: 'http://grnet.github.io/grnet-media-pack/grnet/logos/grnet_logo_en.svg',
      alt: 'grnet',
    }, {
      url: 'https://upload.wikimedia.org/wikipedia/commons/b/b7/Flag_of_Europe.svg',
      alt: 'europe',
    }],
  },
}
```

They are all optional. 

If you wish to use `policy.hbs` template for you policy page, you can alter the title and the content by editing `ui/app/locales/en/policy.js` file.


 


### Migrations

Run all migrations in order to construct the database schema.

Move inside `agora` folder, and run:

```
python manage.py migrate
```

You can load some initial data by running:
```
python manage.py loaddata fixtures/users.json
python manage.py loaddata fixtures/target_users.json
```

`users.json` will create users with usernames/passwords:

* superadmin/12345
* admin/12345
* service_admin_1/12345
* service_admin_2/12345
* observer/12345


### Serving

Serve ui files by running the command from inside `ui/` directory:

```
./node_modules/.bin/ember build
```

This will create a `dist` , that will be served by Agora to deliver the UI.

Finally, run `python manage.py runserver` from inside `agora` folder to test that the application is installed properly.

You can now view your application in `http://127.0.0.1:8000/`


## Development with Docker

You will need [docker-compose](https://docs.docker.com/compose/install/).

While on the root directory of the repo use the following command:
```
# docker-compose up --build -d
```

This will create a container for the backend (manage.py runserver) and the frontend (ember build --watch). The containers are named `agora-backend` and `agora-frontend` respectively.

Agora can be accessed at localhost:8000.

To check the output of the container use docker logs, e.g. `docker logs [-f] agora-backend`

The database will be created in the backend directory (agora/mydb-docker.sqlite3) and will be reused across docker builds. If you want to reset it, just remove the file. If you want to use an existing database, overwrite it. You'll probably need root, as Docker runs and therefore creates/modifies files as root.

The database will be populated with some initial data. The users with username/password:

* superadmin/12345
* admin/12345
* service_admin_1/12345
* service_admin_2/12345
* observer/12345

will be created.

If you want to run a shell in a container use
```
# docker exec -it agora-backend bash
```

If you want to attach to the running process use:
```
# docker attach agora-backend
```

### Running without docker-compose:
- To use the containers without docker-compose, you will have to build the containers, create and start them. You can check docker-compose.yml for info on options to use during container creation.


## Testing

We use [pytest](https://docs.pytest.org/en/latest/index.html) to run API testing and [cypress](https://www.cypress.io/) for e2e testing.

In order to test API, you must run
```
pytest 
```
from inside `agora` folder with virtualenv activated. Make sure you have already installed the development requirements by issuing: `pip install -r requirements_dev.txt`. This will install the required version of `pytest` along with the needed dependencies `pytest-env` and `pytest-django`.

For e2e testing, open cypress using yarn:
```
yarn run cypress open
```
and follow the instruction in [cypress test runner docs](https://docs.cypress.io/guides/core-concepts/test-runner.html#Overview).


# Copyright and license


Copyright (C) 2017-2019 GRNET S.A.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see [http://www.gnu.org/licenses/]([http://www.gnu.org/licenses/).
