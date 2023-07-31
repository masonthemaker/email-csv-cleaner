#
#                        Email Filter GUI
#
## Overview

This Python script is an easy-to-use, graphical user interface (GUI) application that filters out specific domains from a list of emails in a CSV file. It's a simple and effective tool, whether you're trying to clean up your mailing lists or manage your email data for data analysis or marketing purposes.

## Features

- **Custom Domain Filtering:** This program lets you choose which domain(s) you want to filter out from your email list. It comes with a pre-defined list of popular domains, but you can easily customize the list according to your needs.
- **Invert Filter:** In addition to filtering out specific domains, this application also offers an "Invert Filter" feature. By checking the "Invert Filter" box, the program will only keep the emails from the selected domain(s) and remove everything else.
- **Progress Feedback:** The program has a progress bar which gives you real-time feedback about how many emails have been processed.
- **Error Handling:** The script is designed to handle a number of errors that might occur. It checks whether the selected file is a CSV, whether the file exists, whether it is empty, and whether the 'Email' column is properly labeled. If an error is encountered, a helpful message is shown to guide you to resolve the issue.
- **Detailed Summary:** Upon completion, the program provides a detailed summary of the operation. This includes the total number of emails processed, the number of emails removed or kept, and the total number of emails left in the final file.

## Usage

After running the script, select the 'Remove Emails' button to choose the CSV file you want to process. Select the domain you want to filter from the dropdown list, and check the 'Invert filter' box if you want to keep only emails from the selected domain(s). The program will then process the file and create a new CSV file named 'output.csv' in the same directory.

## Dependencies

This script uses the `pandas`, `tkinter`, and `os` libraries, so make sure you have these installed before running the script. You can install `pandas` via pip by running `pip install pandas` in your command prompt or terminal.

This project demonstrates the power of Python in handling and manipulating data in practical scenarios. It's a perfect tool for anyone working with large email lists or anyone interested in managing and cleaning their email data more efficiently.
