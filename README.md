# Anothercryptosolver

Another fast cryptogram solver (for simple substitution ciphers) that performs dictionary attacks using wordlists databases, made in python. It follows the unix philosophy, i.e. *"Do One Thing and Do It Well"*.

## Usage
Use the *cryptosolver.py* script to solve a cryptogram, you will need to specify some wordlist database file, you will find a list of available wordlist databases in the wordlist directory, also you can generate your own wordlist databases using the *genwordlist.py* script. See [generating custom wordlist databases](#custom-wordlists) for more info. 

*cryptosolver.py* takes the wordlist database file specified in the first command line parameter and reads the cryptogram from the standard input, it will output (in the standard output) all the possible solutions that use the words from the specified wordlist database.

Example:

Suppose that you want to solve the following cryptogram:
```
"inmi in ju viuneyi nzvqwi iu inqectw"
```
and you know that the original message is in spanish language, so we can use the wordlists/spanish_aspell_wordlist.db spanish wordlist database to do this:
```bash
$ echo "inmi in ju viuneyi nzvqwi iu inqectw" | ./anothercryptosolver/cryptosolver.py wordlists/spanish_aspell_wordlist.db
```
 it will output:
 ```
 este es un mensaje simple en español
 ```
 
 In this case, *cryptosolver.py* found just one possible solution, but if there are more than one solution it will print all of them.
 
## <a name="custom-wordlists"></a>Generating custom wordlist databases 
