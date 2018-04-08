# SugarPy
SugarPy is a [SugarCube v2][sugarv2] interpreter and processor heavily relying on
[ANTLR v4][antlr4] parser generator.
You can use [Twine/Twee][twinery] stories in your Python 3 code. For instance,
in the cloud-based backend.

## Installation
TODO

## Usage
TODO

## Contributing
### Updating lexer and parser
Read [ANTLR4 documentation][antlr4docs] on how to install it for development
antlr4 -Dlanguage=Python3 SugarCubeLexer.g4 -visitor -o sugarpy
antlr4 -Dlanguage=Python3 SugarCubeLexer.g4 -visitor -o sugarpy
### Debugging Lexer and Parser
antlr4 SugarCubeLexer.g4
antlr4 SugarCubeParser.g4
javac SugarCube*.java
grun SugarCube parse -tree -gui
Paste test scene data and then Ctrl+d


### Testing
Run sample/sample.py

[The source for this project is available here][src].

[sugarv2]: http://www.motoslave.net/sugarcube/2/
[antlr4]: https://github.com/antlr/antlr4
[antlr4docs]: https://github.com/antlr/antlr4/blob/master/doc/faq/installation.md
[twinery]: http://twinery.org/
[src]: https://github.com/Braza/sugarpy