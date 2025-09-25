# WaterCard
WaterCard maker for [![wir-kaufen-dein-arschwasser.de](/WaterCard/static/Arschwasser.png)](https://wir-kaufen-dein-arschwasser.de).

Examples can be seen [here](https://wir-kaufen-dein-arschwasser.de/WaterCard/).


## How To Install

You need `Python>=3.12.0` and `poetry>=2.0.0`.

After cloning the repo run `poetry install` in this directory.

### I don't want to use `poetry`...
It's OK if you're not a poet.
You can also use `requirements.txt`.

#### OK, so what's the `requirements.txt`?
Oh ok, so you can run `pip install -r requirements.txt`.
*Should you encounter any issues just use a search-engine of your choice!*

## How To Run

Just run `poetry run python -m WaterCard` and answer the questions.

### I said "I don't want to use `poetry`..."
Then just use `python -m WaterCard` *or any other equivalent* and answer the questions.


## The Program Exits With An Error :(

My guess is that a library required by `WeasyPrint` is missing.
Copy the error message and paste it into a browser of your choice.
There should be a thread explaining the required steps to install the library.

> [!NOTE]
> If you're helpless and on Windoof and have a error message like `OSError: cannot load library 'libgobject-2.0-0': error 0x7e.  Additionally, ctypes.util.find_library() did not manage to locate a library called 'libgobject-2.0-0'` try installing the [GTK3 runtime](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases) *\*no warranty*
> 
> This is what an [old version of WeasyPrint](https://doc.courtbouillon.org/weasyprint/v62.0/first_steps.html#windows) suggests at least...
>
> If that doesn't work for you just try to stick to the [latest documentation of WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html).
