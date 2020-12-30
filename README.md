# letterboxed
Solve the ny times letterboxed puzzle.

## usage

```
$ ./letterboxed.py --help
usage: letterboxed.py [-h] [--verbose] [--maxlength MAXLENGTH] letters

Somebody do something.

positional arguments:
  letters               Allowed letters as one list: "abcdefg.."

optional arguments:
  -h, --help            show this help message and exit
  --verbose             Verbose
  --maxlength MAXLENGTH
                        Show chains at least this long.

Ouput:
    Number of words in the path (shorter is "better").
    Total number of charcters in the path.
    Number of repeated (extra) characters (smaller is "bettter").
    Given character set.
    Path as "word1->word2..."
```
