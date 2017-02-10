# LimbsFreeTeam/Team 4

## Iteration 01 - Review & Retrospect

 * When: Thursday, February 9th 2017
 * Where: Bahen Centre

## Process - Reflection

The software allows the user to control the computer cursor using the webcam. The software will also make web pages more accessible so that the cursor can click on items more easily. Intended to bridge the gap between amputees with missing limbs (including arms), the software uses computer vision to move the cursor around the screen. We also plan to make  a chrome extension that overlays controls onto the screen that when clicked, can introduce new on-screen inputs / make the page more accessible. Using only the webcam and mic, this software aims to be extremely portable with the only requirements of having a computer/laptop with a webcam (mic optional).

![alt tag](scr_it1.jpg)

#### Decisions that turned out well
 
-Using python for the cursor control. This was great for two reasons; Firstly, it is compatible with OpenCV, the computer vision library we are using for this project, and secondly it is compatible with the skillsets of our group members<br><br>
-Nobody in the group has ever made a Chrome extension; however, making an extension is an addition to the project which we feel is appropriate given our group's technical abilities. Additionally, it makes a lot of sense given the original product we are building<br><br>
-Using Trello and Slack for project management. Our project management is going very well because of this; Everyone is making good progress on the tasks they were assigned, and we are keeping each other in the loop.<br><br>


#### Decisions that did not turn out as well as we hoped

-Unfortunately we still feel the project is too simple in scope for 6 people; the amount of work we put in for iteration 1 was not enough. One group member didn't get a chance to submit any code as all the work was done.<br><br>
-Originally  we used nose tracking, then had to switch to eyes due to inaccuracies; then had to switch yet again to face tracking due to further inaccuracies TODO - need to elaborate<br><br>
-Trying to embed OpenCV in a Chrome extension: hard to control the mouse with a Chrome extension - just making script downloadable TODO - need to elaborate<br><br>


#### Planned changes

-Adding a website where users can view a demo and download the project. This is because the scope of the project was originally too simple. This also makes the project more "professional"<br><br>
-Need to figure out method to click; each choice has a tradeoff/dilemma TODO: explain the choices and associated tradeoffs<br><br>

## Product - Review

#### Goals and/or tasks that were met/completed:
 
All of the tasks described in the plan have been completed if not surpassed. Attached in this folder is a screenshot of the Trello in the state of iteration 1 completion along with a JSON export of the Trello board. 

![alt tag](trello_it1.JPG)

#### Goals and/or tasks that were planned but not met/completed:

None - we all met our tasks. However, at the last minute we decided to add the website. Due to the decision being taken just before the due date, the group member in charge of that (Rohan) did not commit any code for that part.<br><br>


## Meeting Highlights

As stated earlier, our project scope is too limited. We are thus going to build a website where users can download the software and extension from. This will give our project a more professional feel.<br><br>
Extension needs work. It is currently in a very basic state and is missing a lot of our core requirements for the application. <br><br>
Need to come up with method for clicking. Timothy will look into ways to track clicks using facial features. Current idea is to use left/right double-blink to similate a cick.<br><br>
Everyone is on the same page, and we are working together very well. Our task management (via Trello) is running smoothly, and we have all made good progress on the work we were individually assigned (all targets were met for this iteration) <br><br>
