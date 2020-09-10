# Springboard-prd

This project is my capstone submission for the 400+ hours course made available by Springboard. The project consists in an API that has texts as the input and it outputs the sentiment of the chosen text and store the model's prediction along with the input so it can be used for retraining in the future.

## Getting Started

```console
$ git clone https://github.com/litchumah/Springboard-prd.git

```

### Prerequisites

At least python 3.6 and the latest docker version (currently it is version 19)

### Installing

In order to properly install ktrain, tensorflow's version should be higher than 2. 
For a simpler installation just do the following:

```
sh install.sh
```
After running the install file the database will be located on the port 8000 and the python app on the port 9000, both through Docker.

#### Installing only the python part
It is possible to install only the python project's prerequisites by typing the following command:

```console
$ pip install -r requirements.txt
```
After installing the requirements just run the command:

```console
$ python app.py
```

And the application should start on port 9000 but it will try to connect to a DynamoDB instance. It is possible to comment the DynamoDB part to take advantage of the trained model.

## Running the tests
The tests are visible by typing the following command on the tests folder:

```console
$ pytest .
```

## Deployment

The deplyment was made on a EC2 machine on AWS and accessed by it's IP address.

## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [ktrain](https://github.com/amaiya/ktrain) - Keras wrapper for NLP modeling
* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - Database

## Authors

* **Litchi Sun Zulato** - *Initial work* - [litchumah](https://github.com/litchumah)

See also the list of [contributors](https://github.com/litchumah/Springboard-prd/contributors) who participated in this project.

### Example template from: https://gist.github.com/PurpleBooth/109311bb0361f32d87a2
