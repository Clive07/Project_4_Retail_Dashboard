# SkillsUnion Project 4 - Dashboard
Creation of a Dashboard to present data for a large pseudo retail company which was collected over a 10 year period.
Cleaning, analysing and transforming of the raw data in order for it to be presentable and useful.


## Table of contents

- [Introduction](#introduction)
- [Technologies & Designing](#technologies-used-&-designing)
- [Launch](#launch)
- [To Do](#to-do)
- [List Of Known Issues](#list-of-known-issues)
- [Lessons Learnt](#lessons-learnt)

### Introduction

This project is a python dashboard created with the purpose to store and present data about and for a large pseudo retail company. This data has been collected on a 10 year period though some data points are 9 or 8 year periods in various format types. Firstly the task is to clean, analyse and transform the data so the desired information could be obtained from the complete data set.

Then once this information has been assertained it was deployed on heroku to be viewable in various different graphs and the like.

The entirety of this project is solely for educational purposes in order to test my skills with the specific technologies used.

### Technologies Used & Designing

- 
- Miro/Draw.io
- VS-Code
- Github
- Heroku

VS Code was the code editor used for this project.
Github held the repository which links to Heroku for the deployment.
Heroku was used for the deployment.
Python package Virtual Environment was utilised in order to freeze the required packages and the version they all were at the time of creation.

The links below are for the Project Brief I was given at the start and also my designs for this project.

LINKS:

### Launch

URL:  

### To Do

- 

### List Of Known Issues

product_lists.csv file had one error with the product categories. One fruit and veg entry didn't have an s at the end. I amended this manually but if time allows I will see if I can create the code which fixes these potential issues for me

### Lessons Learnt



### Notes for found code

https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/
https://petl.readthedocs.io/en/stable/_modules/petl/transform/basics.html#addfieldusingcontext
https://tutorialdeep.com/knowhow/round-float-to-2-decimal-places-python/
https://stackoverflow.com/questions/42504984/python-pandas-select-both-head-and-tail
https://www.sharpsightlabs.com/blog/pandas-unique/


indexing:

does it have to be unique?

when creating or initialising a df or table it seems to be
a requirement

but once made I can set it to any col and then it can be duplications?

I wanted to index a large group file by the region and then the city within those regions.

I assume it will be a smaller file as I wish to have 3 or 5 files that I pull from to then acquire all the needed results from the data

can I set an index while in etl to potentially speed up the transition to a df?

or perhaps can I segment the df based on the city and/or region?

due to forgetting about duplicates... my 2010 file has a 2011 city, how can I best drop that one?

random:

how can I highlight all things and indent them together or backspace them etc