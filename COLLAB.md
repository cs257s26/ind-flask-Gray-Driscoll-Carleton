# Collaboration
Put any sources (not included in the assignment) that you referenced in doing this assignment. This includes: websites, people you consulted, and (where sanctioned) GenAI prompts and chatlogs. Include a brief sentence on how you used each resource.


5/9/2026
I used almost only links from Moodle from the past labs and homework for this assignment, as well as postgresql documentation:
https://www.postgresql.org/docs/13/datatype.html#DATATYPE-TABLE
https://www.postgresql.org/docs/current/sql-copy.html

Some of the code (the main and connect functions) were copied from the original moodle code provided to us.

Gemini was used for three things: 
    -Connecting and creating databases with Stearns, it was used very lightly here and had no impact on my end work, I am confident I understand how to navigate Stearns now. (I got a little lost because I was not able to follow along in class for the introduction to postgresql last week)
    -The copy commands, I did not realize that when I added `HEADER true, NULL '0'` that I could no long just do `CSV` as in the lab example. It told me to add `FORMAT`. I also used the documentation for the `WITH` syntax.
    -The query in `def five_year_global_education_comparison`, I could not figure out how to find a second average because I did not realize you could embed SELECT statements. The rest of the that query and the query in the other function were created solely by me.




--The intro flask lab

https://flask.palletsprojects.com/en/stable/quickstart/
https://auth0.com/blog/developing-restful-apis-with-python-and-flask/ -- Both used while I was writing to help my  understanding of flask

I used several websites to help with writing flask code and tests:
https://flask.palletsprojects.com/en/stable/testing/ -- Used to figure out how to check status codes

https://codethechange.stanford.edu/guides/guide_flask_unit_testing.html -- Also used to learn checking codes and other assertions

https://stackoverflow.com/questions/69853072/writing-unit-test-for-a-flask-application-using-unittest -- Somewhat helpful SO question that helped with my syntax