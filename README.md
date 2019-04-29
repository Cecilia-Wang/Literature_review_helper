# Literature Review Helper v1.02

## Introduction
The script was build under macOS system with Python 3.7.3.
&nThe tool can convert a pubmed (https://www.ncbi.nlm.nih.gov/pubmed/) downloaded txt file, a list of journal articles (with abstracts) into a csv spreadsheet.


## Installation

To use the tool, you will need to install a couple things
1. **Python3**
2. Python modules: **itertools, csv, datetime**
  For Macs: to install modules, open a terminal window and type 'pip3 <module_name>'.
    e.g. pip3 csv

## How to use

1. Go to PubMed (https://www.ncbi.nlm.nih.gov/pubmed/) and search for articles.
2. Once you are happy about the results, click the **Send to** option on the top right below the searching area.
3. Select **File** as the CHoose Destination, **Abstract(text)** as the format, then click **Create File** 
4. Save the text file to a local directory
5. Download the PubMed_Review_Helper.py and save to the directory as 4.
6. Open a terminal window, change directory to above (4.or 5.)
7. Run PubMed_Review_Helper.py file by type **python3 ./PubMed_Review_Helper.py**
8. Enter the names of input text file you downloaded and a name of the output.
9. Good luck on your literature review.

Note:
* Output is csv format so won't support or save any excel formating settings. To enable those, save as a excel file.
* To enable the link to be clickable, select the link and then move cursor to formular bar, click anywhere to activate and then enter. Don't change any text. If excel is up to date, the link should automatically turn blue.

