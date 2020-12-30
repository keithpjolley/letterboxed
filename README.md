# letterboxed
Solve the ny times letterboxed puzzle.

## usage

```
$ ./letterboxed.py --help
usage: letterboxed.py [-h] [--maxlength MAXLENGTH] letters

Somebody do something.

positional arguments:
  letters               Allowed letters as one list: "abcde.."

optional arguments:
  -h, --help            show this help message and exit
  --maxlength MAXLENGTH
                        Show chains at least this long.

Ouput:
    Number of words in the path (shorter is "better").
    Total number of characters in the path.
    Number of repeated (extra) characters (smaller is "bettter").
    Path as "word1->word2..."
```
