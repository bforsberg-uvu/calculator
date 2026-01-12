## AI Collaboration Log

Prompt:  how do I check the type of a variable

Response: Use the type() function to check the type of a variable:

    To compare types:

    if type(x) == int:
        print("x is an integer")

    if isinstance(x, int):  # Better practice
        print("x is an integer")

    isinstance() is preferred because it also checks parent classes and is more Pythonic.

I was having an issue ensuring the input was the right type so I asked AI for info on how to do this in Python

-------------------------------


Prompt: my get input method should take an argument that specifies the type of the  data expected

Response:  Your getInput method already has an expected_type parameter with a default of float. However, the current type checking logic isn't working correctly. Let me improve it to properly validate and convert the input:

Edited
calculator.py+5-4
Done. getInput now properly accepts an expected_type argument (defaults to str) and converts the input to that type. For example:

getInput("Enter a number: ", int) - expects an integer
getInput("Enter a value: ", float) - expects a float
getInput("Enter text: ") - expects a string (default)



## License

MIT License
