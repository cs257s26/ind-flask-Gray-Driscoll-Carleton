# README
5/9/2026
I did not include a password in the psqlconfig file both because I did not need one, and because I do not know mine. I was not able to follow along in class at the time when we were being told the passwords, so I do not know mine (but again, it was not needed).

Copy command or literacy rates: `\copy education_data FROM 'ProductionCode/data/cleaned_education_data.csv' WITH (FORMAT csv, HEADER true, NULL '0');`
Copy command for women's roles in gov: `\copy education_data FROM 'ProductionCode/data/cleaned_education_data.csv' WITH (FORMAT csv, HEADER true, NULL '0');`
The HEADER true and NULL '0' are necessary because I kept my headers in the cleaned data (to help me refer to it because I kept forgetting ordering), and because when I cleaned the data I entered 0 for any missing data.


Describe the process by which you decided how to represent your data in your database. Include why you selected the number of tables you did, how you decided what data to include and exclude, why you selected the datatypes you did, and what the primary keys are.
I represented the data in my database as it appeared in the original CSV. I kept the same number of rows and columns, although I did clean the data before beginning this assignment because there were many empty values in both original datasets. I created two tables because I was working with two datasets--it seemed intuitive. The primary keys are simplified eay-to-remember versions of the original CSV headers. They are abreviated but the user can still understand what the category is at a glance.


Explain how each of your queries represents a user story. What does the query do, and how does this match all or part of a user story?
The first query in `lit_over_time_region` finds the year and average literacy rates for two years, then returns them. This matchs the user story: "I want to see how literacy rates have changed over a given time [in a given region]". Because the query groups by year, the user can clearly see the year, the region, and the literacy rate at the time for the two dates they entered. If they wish to perform multiple queries, they can compare the data they recieve to determine growth rates across the world.

The second query, in `five_year_global_education_comparison` seeks to help the user story of a student desiring to know the "average years of schooling in my country for any 5 years". The function does this by searching the database by country and year. For the year and the following for years, it returns that year, the country the user entered, the average education in that country during that year, and the global average. The user may then compare the average of their country during that year to the global average.



Individual Flask project.

To observe the information on a webpage, the user should run `app.py`, then enter their search.
There are two possible searches, `http://127.0.0.1:5000/avgSchooling/Canada` will display average schooling statistics from Canada, the country may be changed to any other to see their respective info.
`http://127.0.0.1:5000/litGrowth/Canada` displays literacy rates' growth over the years, likewise, "Canada" may be replaced with any country