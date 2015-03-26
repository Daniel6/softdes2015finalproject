# softdes2015finalproject
Final Project for Software Design 2015

###The Big Idea
The big idea of our project is to explore the workflow of capturing an image, saving it, uploading it, and sharing it.  We will explore this workflow and streamline it for the user. We will combine all of these steps into one customizable action for the user, where the user can define where to upload the picture, how to save the picture, and how to share the picture. This will streamline the workflow for the user and make sharing images possible in one keystroke!

###Minimum Product
Our minimum viable product is an application that captures a user defined rectangle and uploads the screenshot to imgur and provides the user with a link to the hosted picture.

###Learning Goals
Our learning goals for this project are to learn about the API’s for many different hosting sites, learn about registering hotkeys with Ubuntu, learn about capturing the screen in various ways, and to learn about moving image data around without saving it to a file.

###Project Schedule
We plan to implement image capturing with the gtk library, and then use http requests to connect to all the web services. We will save user settings in a file and use xlib to register hotkeys in Ubuntu.

As a rough outline, after one week we should have a method of grabbing image data for a particular section of screen. The next week, we should be able to upload the picture to an image hosting site. The third week should see the implementation of hotkeys and the complete pipeline of capture->upload->share. This will complete our minimum viable product and give us 3 more weeks to add more features and polish the application.

###Collaboration Plan
Since none of us know that much about these libraries, we will all research them individually and integrate what we learn to make some sort of working unit test for each functionality. Having the part working, we can then integrate it into the main project.

###Risks
Some of the biggest risks to our project are getting stalled on one of the core functionalities such as registering hotkeys. If we can’t figure out how to do it, progress would basically be halted. There is also a risk of not putting enough time into the project and falling behind schedule.

###Helpful Things
It would be helpful if in class we covered screenshotting and registering of hotkeys, since we have already covered using web API’s.
