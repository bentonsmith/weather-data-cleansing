## Running the program:
This program can be run from the driver.py file. It can be used in the following ways:  

Usage: driver.py command source_file [destination_file]  
  * Command options:  
    * prepareFile
    * addErrors
    * findErrors

Each command has a different functionality.  
  * PrepareFile: Take and clean the source file. This removes many columns and removes all aggregate rows. You must specify a destination file.
  * addErrors: Adds 20 random errors to the dataset to experiment with data cleansing.
  * findErrors: Allows user to choose columns and set boundaries for acceptable values. The program will then alert the user which rows have values outside of the acceptable boundary.

## Viewing the program:
  * Data Cleansing Programs:
    * aggregate.py: This program removes all of the aggregate columns from the weather data set.
    * cols.py: This program removes a specified list of columns as well as all columns after a specified point.
    * findErrors.py: This is an interactive program that finds errors based on user rules and inputs.
  * Data Scrambling Programs: 
    * scramble.py: This program creates random errors in the file.
  * Driver Programs:
    * driver.py: This program allows the program to run from the command line.
