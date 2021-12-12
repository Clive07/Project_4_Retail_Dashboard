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

It should be noted that the MAIN branch only contains this readme file. the CLEANUP branch holds the first half of this project whilst the DEPLOYMENT branch contains the second half... the dashboard itself.

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
It should be noted that the pywin32 package was removed to allow the heroku deployment to work.

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

The results are able to be viewed... I believe it is what was asked but I could have gone further by expanding from just overall to yearly statistics too. The charts themselves as well could have done with more finetuning to make them easier to understand. One example of something like this would be to of added pull or explode attribute to the pie chart which would make it much easier to point out the most profitable hour, branch or region ect.

The cleanup and manipulation sections could have been better. They do indeed work.. however initially it would take over 3 hours due to me converting from etl table to a pandas dataframe. This was curved down to half this time thanks to instead saving from etl a csv file and them with pandas reading this file instead of converting. I do still believe I could have refined this even further by perhaps using pandas as much as possible instead of using petl. Petl is certainly useful but due to its slow nature it makes pandas more desirable.

The graphs on the dashboard are indeed nice but due to my lack of knowledge using them I feel like they are lacking somewhat. It would have been quite nice as the user to request which chart the data will be presented as whilst also picking multiple counties or regions to compare against one another. Alas with time and other more pressing bugs and tweaks this was put on the back burner.

I wasn't able to go as extensive with this data as I wanted to be. The brief only ever asked for overall and not yearly but I was initially attempting to give these finer results. However I think I bit off more than I could chew attempting to get all of this data at once. Instead I should have focused on the minimum and then looked to see how more specific with the results I could go.



### Lessons Learnt

  Fortunately this time round there was not that many issues during the making of this project. Looking back all lessons learned was less macro and more micro. meaning specifically I didn't really learn lessons as a software engineer but rather as a python programmer. For example using petl, pandas and dash. Before the project I sort of knew how to utilise these packages but now after having gone through this project I feel far more capable using all of these tools.
  
  I did learn something off handed which is the need to have disciplined breaks. I noticed after days of working several hours straight that simple mistakes like typos and forgetting names of variables would come up more frequently but also be that more annoying. As fun as it can be to work on a project and seeing your progress it is important to also not get burnt out. This project only being a week long helps but I felt on the last couple days I was ready for this to be done already. But given there was more time I would naturally keep going and think of ways to improve anything. 
  
  This means of course you need to notice when you're running low on steam and be able to take a step back... have a tea and biscuit and get back to it. 
    Now... while that is true it is also important for myself to note how it must be a **disciplined** break. Don't step away for too long otherwise the productive mindset fades away and also you are losing precious time.
    
    The balance for the most efficiency is always difficult but important to remember.
    
 Overall I believe the project went reasonably well however in hindsight...

My desire to be able to iterate through all the raw and then refined files held me back a little bit. I would get overwhelmed a little by the thought of having to grab each result from each branch and but them together.

If I instead focused on one branch and acquired the data I wanted from it successfully i.e. the overall stats as well as yearly. I could have then expanded this by simply putting it within a for loop. Instead I pretty much started with the loop and this caused initially skewey results which slowed down progress.
  
  

### Notes for found code

  Here are links to various sites & posts I discovered whilst working on this project. These helped tremendously whilst completing this project and since at least the very first link is something that we've not gone over during class... I felt it would be good to share in case it helps the other students or anyone else for that matter.

https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/
https://petl.readthedocs.io/en/stable/_modules/petl/transform/basics.html#addfieldusingcontext
https://tutorialdeep.com/knowhow/round-float-to-2-decimal-places-python/
https://stackoverflow.com/questions/42504984/python-pandas-select-both-head-and-tail
https://www.sharpsightlabs.com/blog/pandas-unique/
