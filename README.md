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




## License

MIT License
