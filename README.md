Welcome to Darient Test!
==========================

Url
---

https://darient.alehdzdev.com

Env
---

Create your environment variables::

    cp -r .envs-example .envs

Run
---

Execute the next command to start web and database service::

    docker-compose build
    docker-compose up -d


Connect to Docker Container::

    docker-compose exec web sh

Run Management Command::

    docker-compose exec web python manage.py <command>


Stop
----

In the project root, execute the next command to stop containers::

    docker-compose stop


Down
----

In the project root, execute the next command to delete images::

    docker-compose down


Pre commit
---
Install pre-commit in your local enviroment::

    pip install pre-commit

Execute the next commad the first time to install pre commit::

    pre-commit install

Later, the next command::

    pre-commit run --all-files

# Darient Test base structure

```
project/
    backend/
        apps/
            core/
                fixtures/
                migrations/
                tests/
                models/
                views/
                urls.py
            app1/
                fixtures/
                migrations/
                tests/
                models/
                views/
                urls.py
        config/
            __init__.py
            asgi.py
            settings.py
            urls.py
            wsgi.py
        requeriments/
            _base.txt
            development.txt
            production.txt
        static/
            css/
            img/
        templates/
            admin/
        .coveragerc
        .pylintrc
        setup.cfg

    envs/
        .development
        .staging
        .production

    compose/
        development/
            Dockerfile
            entrypint.sh
        production/
            Dockerfile

    .dockerignore
    .editorconfig
    .gitignore
    .gitlab-ci.yml
    .pre-commit-config.yaml
    docker-compose-production.yml
    docker-compose-staging.yml
    docker-compose.yml
    Makefile
    README.md
```
