This program can be run from the driver.py file. It can be used in the 
following ways:

Usage: command source_file [destination_file]
    Command options:
	-prepareFile
	-addErrors
	-findErrors

Each command has a different functionality.
	-PrepareFile: Take and clean the source file. This removes many
	 columns and removes all aggregate rows. You must specify a 
	 destination file. 
	-addErrors: Adds 20 random errors to the dataset to experiment 
	 with data cleansing. 
	-findErrors: Allows user to choose columns and set boundaries for
	 acceptable values. The program will then alert the user which 
	 rows have values outside of the acceptable boundary.
