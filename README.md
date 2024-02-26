# betgraph

A Django web application using Neo4j to graph crushes.

## Setup

### Development
1. Clone this repository
2. Install the required development packages using `pipenv install --dev --ignore-pipfile`
3. Create a copy of `secrets.json.example` and name it `secrets.json`. Modify it according to your own preference.
4. Run `python manage.py install_labels` to setup labels and constraints.
5. Run the Django web application

### Production
* To follow.

## Requirements
* Python 3
* Neo4j Server
* Pipenv
* Packages installed in the machine depending on the environment