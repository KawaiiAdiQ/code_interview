# Code interview

### About:

This script takes text file on stdin and applies the ceasar cypher onto it with offset given in argv.  
Outputs the encrypted data to "zasifrovana(CYPHER_KEY).txt" and stdout.

### Usage:

a) `python3 cypher.py YOUR_INT [OPTION] < YOUR_FILE_TO_ENCRYPT`

b) `python3 cypher.py YOUR_SOURCE_CHAR YOUR_DESTINATION_CHAR [OPTION] < YOUR_FILE_TO_ENCRYPT`

[OPTION]:  
**-h --help**  
prints usage (this).

**-f --force-overwrite**  
if destination file exists, overwrites it. Otherwise doesn't execute.

**Variables:**  
`YOUR_INT`: decimal, indicates offset of the cypher  
`YOUR_SOURCE_CHAR`: single character, sets offset to `YOUR_DESTINATION_CHAR` (also single character)  
`YOUR_FILE_TO_ENCRYPT`: path to text file that you want to apply cypher to

### Integrity constrains:

- cypher applies only to characters from english alphabet (both lowercase and uppercase)  
  other characters are skipped

- `YOUR_INT` can be either positive or negative

- `YOUR_SOURCE_CHAR` and `YOUR_DESTINATION_CHAR` aren't case sensitive
