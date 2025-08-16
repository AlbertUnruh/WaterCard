# WaterCard
WaterCard maker for [wir-kaufen-dein-arschwasser.de](https://wir-kaufen-dein-arschwasser.de)


## How To Install

You need `Python>=3.12.0` and `poetry>=2.0.0`.

After cloning the repo run `poetry install` in this directory.

### I don't want to use `poetry`...
It's OK if you're not a poet.
You can also use `requirements.txt`.


## How To Run

Just run `poetry run python -m WaterCard` and answer the questions.

### I said "I don't want to use `poetry`..."
Then just use `python -m WaterCard` *or any other equivalent* and answer the questions.


## The Program Exits With An Error :(

My guess is that a library required by `WeasyPrint` is missing.
Copy the error message and paste it into a browser of your choice.
There should be a thread explaining the required steps to install the library.
