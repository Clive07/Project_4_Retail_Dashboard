# SkillsUnion Project 4 - Dashboard
This project consists of the creation of a Dashboard to present data for a large pseudo retail company which was collected over a 10 year period.
And before hand the cleaning, analysing and transforming of the raw data in order for it to be presentable and useful.


## Table of contents

- [Introduction](#introduction)
- [Technologies & Designing](#technologies-used-&-designing)
- [Launch](#launch)
- [To Do](#to-do)
- [List Of Known Issues](#list-of-known-issues)
- [Lessons Learnt](#lessons-learnt)

### Introduction

This project is a python dashboard created with the purpose to store and present data about and for a large pseudo retail company. This data has been collected on a 10 year period though some data points are 9 or 8 year periods due to it being based on when a branch was established. This data was in csv and json format types. Firstly the task is to clean, analyse and transform the data so the desired information could be obtained from the complete data set.

Then once this information has been assertained it was deployed on heroku to be viewable in various different graphs and the like.

The entirety of this project is solely for educational purposes in order to test my skills with the specific technologies used.

### Technologies Used & Designing

- Classic pen & paper
- VS-Code
- Github
- Heroku
- Python 3.9.9
    - virtual environment
    - petl
    - pandas
    - dash
    - dash bootstrap
 
The other packages used can be seen within the requirements.txt file kept within the deployment branch.
It should be noted that the pywin32 package was removed to allowd the heroku deployment to work.

VS Code was the code editor used for this project.
Github held the repository which links to Heroku for the deployment.
Heroku was used for the deployment.
Python package Virtual Environment was utilised in order to freeze the required packages and the version they all were at the time of creation.

The link below is to give access to the same raw data that I was starting with.

LINKS: 
      https://drive.google.com/file/d/12T1_3h0kUkgc-flBeSa_nDdHNjuAIsX7/view

### Launch

URL:  https://clive-h-project-4-dashboard.herokuapp.com/

### To Do

      - THESE to do's are only for wishing to see how the 'sausage' was made.
- acquire the raw files from source.

- Switch to the 'cleanup' branch in order to run the data cleanup and then the data manipulation files.
    it should be noted this section does take a long minute. So be prepared to make a brew!

- After you've successful run both files. The cleanup created clean data whilst the manipulation section takes said files and acquires various results based on criteria given via the project brief.

      - THIS to do is for the end and purely dashboard related.
- Go onto the dashboard linked above to view the various data results acquired from the raw data.

### List Of Known Issues

product_lists.csv file had one error with the product categories. One fruit and veg entry didn't have an s at the end. I amended this manually but it would have been nice to think up perhaps a way to iterate through it and fix any typos. This time round it is no issue but if the file is much larger than a manually fix becomes incredibly difficult.

The dashboard is not as mobile friendly as I would have liked it to be. 

The results able to be viewed... I believe it is what was asked but I could have gone further by expanding from just overall to yearly statistics too.

The cleanup and manipulation sections could have been better. They do indeed work.. however it takes a considerably amount of time for the cleanup section to occur.
I have narrowed it down to when I convert a petl table to a pandas dataframe. My solution to this is to see if it's possible to do everything with petl and then save as csv files instead of converting to a df before converting. Or perhaps instead flip it to see how possible it was to do everything using pandas only since it is a much faster package when compared to petl.

The graphs on the dashboard are indeed nice but due to my lack of knowledge using them I feel like they are lacking somewhat. It would have been quite nice as the user to request which chart the data will be presented as whilst also picking multiple counties or regions to compare against one another. Alas with time and other more pressing bugs and tweaks this was put on the back burner.

### Lessons Learnt

  Fortunately this time round there was not that many issues during the making of this project. Looking back all lessons learned was less macro and more micro. meaning specifically I didn't really learn lessons as a software engineer but rather as a python programmer. For example using petl, pandas and dash. Before the project I sort of knew how to utilise these packages but now after having gone through this project I feel far more capable using all of these tools.
  
  I did learn something off handed which is the need to have disciplined breaks. I noticed after days of working several hours straight that simple mistakes like typos and forgetting names of variables would come up more frequently but also be that more annoying. As fun as it can be to work on a project and seeing your progress it is important to also not get burnt out. This project only being a week long helps but I felt on the last couple days I was ready for this to be done already. But given there was more time I would naturally keep going and think of ways to improve anything. 
  
  This means of course you need to notice when you're running low on steam and be able to take a step back... have a tea and biscuit and get back to it. 
    Now... while that is true it is also important for myself to note how it must be a **disciplined** break. Don't step away for too long otherwise the productive mindset fades away and also you are losing precious time.
    
    The balance for the most efficiency is always difficult but important to remember.
  
  

### Notes for found code

  Here are links to various sites & posts I discovered whilst working on this project. These helped tremendously whilst completing this project and since at least the very first link is something that we've not gone over during class... I felt it would be good to share in case it helps the other students or anyone else for that matter.

https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/
https://petl.readthedocs.io/en/stable/_modules/petl/transform/basics.html#addfieldusingcontext
https://tutorialdeep.com/knowhow/round-float-to-2-decimal-places-python/
https://stackoverflow.com/questions/42504984/python-pandas-select-both-head-and-tail
https://www.sharpsightlabs.com/blog/pandas-unique/
