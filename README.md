# betgraph

A Django <3 Vue web application using Neo4j to graph crushes.

## Setup

### Development
1. Clone this repository
2. Install the required development packages using `pipenv install --dev --ignore-pipfile`
3. Create a copy of `secrets.json.example` and name it `secrets.json` in the `backend` directory.
Modify it according to your own preference.
4. Run `python manage.py install_labels` to setup labels and constraints.
5. Change directory to the `frontend` folder and install the packages using `yarn add -D`
6. Run the Django web application

### Production
* To follow.

## Requirements
* Python 3 
* Pipenv
* Node.js
* Yarn
* Neo4j Server
* Packages installed in the machine depending on the environment