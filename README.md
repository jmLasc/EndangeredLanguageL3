# EndangeredLanguageL3
A project for scraping the ILRDF dictionaries for sentence-translation-audio pairs for the preservation of the Formosan languages.


## Navigation
### .PanglossXML
If you're at this repo, you're probably here for this. PanglossXML contains a folder for each tribe. Within those folders, there is an audio folder and 2 XML files.

`tribeName_filePaths.xml` is a XML file in the FormosanBank format that contains objects with 4 important attributes. It contains 1) the  original Formosan sentence, 2) its Chinese translation, 3) the path to the audio file that corresponds to the Formosan sentence, and 4) the URL from which the audio was found.

`tribeName.xml` is similar to the above, but it lacks the audio file paths.

The Audio folder contains all of the mp3 files that are referenced in `tribeName_filePaths.xml`. If you are planning to move around these files, it is important that the relative path between the Audio folder and the XML is preserved. Otherwise, you may need to edit the file paths within the XMLs as needed.


### .Meta
Contains depreciated and experimental code. They may be interesting for future reference. Otherwise, it is not used in any significant capacity.


### .PickleScrapes
Contains a folder for each tribe. Within it are scrapes from the ILRDF's API compressed and stored using python's built-in pickle module. There are two types of pickles stored in these subfolders -- `ckpt` and `fails`

`ckpt` pickles contain all of the API outputs in a dictionary format of `{input word into API: API response}`. Very notably, `ckpt` will contain some entries whose values are "FAIL" since the scraping code bunches up all of them together. Therefore, always check for FAILs when using the `ckpt` pickles and be wary that it already include all fails in the event that you need to calculate percentages / do math with the length of `ckpt`.

`fails` pickles contain all of the failed words in a list format of `[failword1, failword2, failword3, ...]` These words are considered fails because the API did not return a proper json object for processing.


### Tribe Folders (Amis, Atayal, ..., Yami)
In this codebase, these folders are chiefly used to contain the pdfs of their respective dictionaries for processing. 

They do contain some text files that may be of interest. This was when the project was primarily using regex techniques to extract text from the pdfs as opposed to the API method being used now.

Text files with `stripped` in the title are from the original repository [here](https://github.com/Sarahyouuu/EndangeredLanguageL3) and contain the extracted text from the pdf dictionaries. The `.py` file also corresponds to the code that makes the `stripped` files.

The `no_br` file is a version of `stripped` but without brackets (parens, square brackets, etc.). The `no_br_no_te` similarly has no brackets, but also removes the text within the brackets.

These files may be of interest, but are far harder to work with than with the API.


### Python Notebooks
In the main repository are three ipynb files. These are `rescrape`, `xml-ify`, and `audioDL`. Together, all 3 were used in the listed order to obtain API responses, transform them into XML files, and then download the necessary audio files.



## Contact + Credits
Email - lascanoj@bc.edu

