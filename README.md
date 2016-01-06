# Movie Aggregator
### Instructions

1. [fpdf](https://pypi.python.org/pypi/fpdf) is required to run this application. Its library to generate pdf in Python. Install the fpdf library using `easy_install` or `pip`:
     
       `$ pip install fpdf`

2. To start the application:

       `$ python assignment.py`

3. Type "write" to enter the user details and movie preferences or type "exit" to exit the application.

### How the application works:
The user enters the user details and preferences in the main program. All the user details and preferences are appened to the dictionary called `prefs`. Depending on the user input for file extension,`prefs["ext"]` the required class is instantiated using reflection. For example if the user enters `txt` file format, the `UserPrefTxt` class is instantiated. 

The current application stores the user preferences to either user.txt or user.pdf files depending on the user input in the same directory.
#### Reflection
In order to make the application extensible for plugging in new formats, I have used Reflections in programming. After instantiating the required class for a particular file format, the required `export` method is called 
`getattr(method, "export")()`, where `method`, is the user selected class for a particular file format.

Plug in a new file format by adding the new format file (e.g if user enters "csv"  as an extension, add csv.py to modules folder  ) to `modules` folder and adding a method `export` to the new class. 
