# GitHub Actions Part-1 Basics


Status of Last Deployment:<br>
<img src="https://github.com/MysykAndrii/githab-actions-part1/workflows/My-GitHubActions-Basics/badge.svg?branch=main"><br>

Copyleft by Andrii Mysyk 2022

pyramid_blogr
=============
Getting Started
---------------

- Change directory into your newly created project.

    cd pyramid_blogr

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Initialize and upgrade the database using Alembic.

    - Generate your first revision.

        env/bin/alembic -c development.ini revision --autogenerate -m "init"

    - Upgrade to that revision.

        env/bin/alembic -c development.ini upgrade head

- Load default data into the database using a script.

    env/bin/initialize_pyramid_blogr_db development.ini

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini
