# EndangeredLanguageL3

Link to the original respiratory (and original README file!): https://github.com/Sarahyouuu/EndangeredLanguageL3
___
## Navigation
Each folder contains the respective dictionary's PDF and the scraper code. 
It also contains:
- the raw text (`...stripped_final.txt`)
- text with no bracket characters (`...no_br.txt`)
- text with no brackets and none of the text inside (`...no_br_no_te.txt`)

`.Meta` contains much of the testing code I used with the text. 

`spacer.ipynb` contains the code used to transform the `no_br_no_te` text files into an XML file with the Pangloss formatting.

`bracket_remover.py` contains the code used to transform the `stripped_final` files into  the `no_br_no_te` and `no_br` files. 
___
## Dependencies
The code was ran in Python 3.12.2 and relies on the following modules:
- re
- sys
- os
- Path from pathlib

Please verify that the modules are installed before running any code.
___
## Contact
Email me! - lascanoj@bc.edu
