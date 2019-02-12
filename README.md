# Factory Web App

## Installation
Instructions are given for the Windows command line and may differ slightly for mac/linux. Create a [virtualenvironment](https://virtualenv.pypa.io/en/latest/) using Python 3 for the app:
```
> virtualenv venv
```
Then install the dependencies:
```
> pip install -r requirements.txt
```
If the virtual environment is installed in the application root in a folder named ```venv```, the helper script can be used to activate it by doing:
```> venv```
## Running
The API can be run by doing:
```
> set FLASK_APP=app.py
> flask run
```
or to run in debug mode:
```
> python app.py
```
## Usage
The database can be viewed by sending a **GET** request with the '**X-API-KEY**' header set to either 'food' or 'textile' to the API endpoint ```'/products/'```, which retrieves the corresponding products.
Requests with any other/no headers will return a BAD_REQUEST (400) response. Food products can be added by sending a **POST** request with the 'food' headers containing a JSON of the product in the form:  
```
{
  "name": "<name>",
  "family": "<family>",
  "tags": [
    "<tag1>",
    "<tag2>",
    ...
  ],
  "allergens": [
    "<allergen1>",
    "<allergen2>",
    ...
  ],
  "customer": "<customer>",
  "billOfMaterials": {
    "<material1>": {
      "quantity": <quantity>,
      "units": "<units>"
    },
    "<material2>": {
      "quantity": <quantity>,
      "units": "<units>"
    },
    ...
  }
}
```  
And textile products are added in a similar way using the 'textile' headers:  
```
{
  "name": "<name>",
  "colour": "<colour>",
  "range": "<range>",
  "tags": [
    "<tag1>",
    "<tag2>",
    ...
  ],
  "billOfMaterials": {
    "material1": {
      "quantity": <quantity>,
      "units": "<units>"
    },
    "material2": {
      "quantity": <quantity>,
      "units": "<units>"
    },
    ...
  }
}
```
## Testing
If the virtual environment is installed in a folder named ```venv``` in the application root, run the tests by doing:
```> test```
to use the helper script, or otherwise by doing:
```
> cd project/tests
> pytest -vv test_api.py
```
Running tests from outside the test folder will fail due to file (sample data) not found.
