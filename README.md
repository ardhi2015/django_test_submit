# Django testing

## Init
- create a new virtualenv
- install the requirements in `requirements.txt`
- create an `.env` file to supply Django's `SECRET_KEY` environment variable.
- start the project by running `./manage.py runserver`
  
## What you should do
- you will need to create API and unit testing to this Django project. you can use Django's own testing framework or Pytest, but the latter is recommended.
- if you use Pytest, you can use these plugins to make it easier to do your test:
  - `pytest-django`
  - `pytest-mock`
  - `requests-mock`
- create `test` folder, inside you will need to create two files, `test_unit.py` and `test_api.py`.
- create tests in each of these files, test whatever you think needs to be tested, more is always better. Please ensure that the tests cover at minimum 80% of the use case. be sure to try supplying wrong data to some of the endpoints and functions and class methods to test if they can handle the wrong data correctly, or give the right exceptions.
- in api testing, provide tests to call each of the api endpoint, and give some assertions for the response (i.e. using `assert`).
- in unit tests, you need to make sure that the test is self-contained by the use of mocking. make sure to avoid calling external API or reading the database during the testing.
- run your tests
- provide a github repo of what you've done along with the instruction on how to run it.

## Information
- the credentials for the two accounts in the database are as follows:
  - username: human, password: 000
  - username: alien, password: 000

## Acknowledgements
some data are sourced from [BMKG (Badan Meteorologi, Klimatologi, dan Geofisika)](https://data.bmkg.go.id)
