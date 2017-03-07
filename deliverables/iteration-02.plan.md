# LIMBSFREE GROUP 4

 > _Note:_ This document is meant to be written during (or shortly after) your initial planning meeting.     
 > It does not really make sense for you to edit this document much (if at all) while working on the project - Instead, at the end of the planning phase, you can refer back to this document and decide which parts of your plan you are happy with and which parts you would like to change.


## Iteration 02

 * Start date: February 17th 2017
 * End date: March 6th 2017

# Before We Begin
One of the issues that were brought up by the TA in Iteration 1 was the misunderstanding of the main focus of the project. While it may seem that the webcam control software was our goal, **its not**. It merely acts as a tool to reach our true goal - to create a web UI to bridge the gap between the inaccuracies of using a webcam to control the mouse and the small buttons of a normal computer/web. Our main focus is an all-in-one solution which focuses on a chrome extension/landing page to create an exclusive UI for the disabled person. We understand that we were not detailed enough in Iteration 1 and have made a stronger attempt to communicate that point through in this iteration as well as being more detailed in this plan. 

## Process


#### Roles & responsibilities

Describe the different roles on the team and the responsibilities associated with each role.

Create a Chrome extension that creates an UI for easier and more accurate navigation. It will make buttons appear on the website which offer functionality which makes it easier to browse the internet. Such functions include zoom buttons, back and forward buttons, and etc

Create a Python application that allows for the user to control the mouse cursor with the webcamera. **It is important to note that this is not the focus of our product; but rather a tool to achieve the purpose of ease-of-navigation**. This will be done by Raymond and Timothy. This goal is around 50% completed as of the end of Iteration 1. This program is composed of two pieces - a python program to track the face, as well as a python program that can accept inputs to move the mouse cursor around the screen. **This program’s control mechanism is different from other webcam control software as this program treats the controlling mechanism as a Touchpoint rather than a Trackpad. (Again, not the main purpose of this project, but worth noting)**

#### Events

Describe meetings (and other events) you are planning to have:

 * When and where? In-person or online?
 * What's the purpose of each meeting?
 * Other events could be coding sessions, code reviews, quick weekly sync' meeting online, etc.

Three in person meetings. One on February 24th in Bahen. This is a hackathon like coding session where all team members will come together in the school lab and work on the project for a day. Two more on February 27th and March 6th, also in Bahen labs. These are meetings before class for code review,  giving each other status updates, and for general discussion.

Team members working on the same area of the project frequently communicate with one another online. We also plan to have online meetings on February 23rd and March 3rd. The first online meeting will be to plan for our in-person meeting on the 24th. The seconds online meeting is to make sure everyone is on the right track and to prepare for our review meeting.

#### Artifacts

List/describe the artifacts you will produce in order to organize your team.       

 * Artifacts can be To-do lists, Task boards, schedule(s), etc.
 * We want to understand:
   * How do you keep track of what needs to get done?
   * How do you prioritize tasks?
   * How do tasks get assigned to team members?

* To-do list in a kanban/scrum fashion. Hosted on Trello. This allows for the prioritization and tracking of the progress of each task. It also allows for members to input new ideas into the board as well as find out who is working on what task quickly. 

* Priority are determined in our planning meetings and labelled using labels in our Trello. For example, a high priority is to get a major feature working (such as having the extension overlay properly) and fixing major bugs while new minor features are prioritized lower. We aim to create a stable program first before adding new features. 
* Since each member knows their role, they are assigned to each card on Trello that matches their role. To be more precise, Raymond and timothy focus on the mouse webcam control **tool**, Rohan focuses on the landing page, and Kevin, Brock, James focuses on **the main purpose** of our project - the Chrome extension.

* Scheduling is determined in our planning meetings and assigned on the card in Trello so that it is easy to view due dates. Please refer up to the prioritization point for more information. 

* Code to be managed on Github. Please refer to the **Git / GitHub workflow** section for more information on our workflow.

* The person that created the pull request cannot merge their own code. It must be approved by another team member before being merged by yourself/other members. By doing this we make sure two experts on that section of the code has looked at the code; ensuring that the code runs according to specification.

* Issues are to be managed on Trello. New issues are opened up with a high priority label and assigned to the respective members who are working on that feature. The issue is also communicated through Slack. 

* Communication is handled via Slack. It is used because of its integration into Trello, Github, and its ability to add bots to help increase the productivity workflow of the chat. The ability to support channels also allows for chat between subsystem members without cluttering the general chat. 


#### Git / GitHub workflow

Describe your Git / GitHub workflow.     
Essentially, we want to understand how your team members share a codebase and avoid conflicts.

 * Be concise, yet precise.      
For example, "we use pull-requests" is not a precise statement since it leaves too many open questions - Pull-requests from where to where? Who reviews the pull-requests? Who is responsible for merging them? etc.
 * If applicable, specify any naming conventions or standards you decide to adopt.
 * Don't forget to **explain why** you chose this workflow.


Each team member has a fork of the project. Every time before working on the project, the team member would create a pull request from the group-04 main repository to his own fork to get all the latest updates. After working on the project and committing code to his own fork, the team member would create a pull-request to merge his code to the main repository. Another team member, usually the person working on the same section of the project, would review the pull request and merge it if there are no conflicts. Often we would explain to each other the sections we are working on so everyone is on the same track. Group members working on the same area of code frequently communicate with one another, either in person or online. We choose this workflow because 

There are times when members working on the same feature would make PRs to each others’ forks to prevent spamming the main repository. The files are then merged into the main repo during milestones of the feature development (that are determined by the individual partners). 

Pull-requests reviews will be made by other individuals that are familiar with the code that was edited. By doing this we make sure two experts on that section of the code has looked at the code; ensuring that the code runs according to specification.

## Product

#### Goals and tasks

 * Describe your goals for this iteration and the tasks that you will have to complete in order to achieve these goals.
 * Order the items from most to least important.
 * Feel free (but not obligated) to specify some/all tasks as user stories.

Have a Chrome extension that creates a UI with 4 buttons for zooming in, zooming out, reset, and create a new tab. **This is another major feature to our application that differentiates us from other existing products. The buttons on the UI will make navigation on Chrome much easier.**

Look into ways for user to install a chrome extension. The goal is to have this chrome extension install along with the program to minimize the user interaction that is required to install the program. Preliminary research shows that one of our members might need to create a Google Developer account. If this is true, the plan is to create a Google Developer account

Look for ways to integrate voice control into our chrome extension. Ideally, the user without limbs would be able to input data into the computer without a keyboard. Using voice would allow for easy input of text into text boxes without need for external hardware or the challenges of using an on-screen input.

Brainstorm for more ideas for our chrome extension. Although not necessarily to be completed this iteration, there is a general consensus among the group members that the Chrome extension could use more features while maintaining its minimalistic form. Any new ideas are to be added to the Trello.

#### Artifacts

List/describe the artifacts you will produce in order to present your project idea.

 * Artifacts can be text, code, images, videos, interactive mock-ups and/or any other useful artifact you can think of.
 * Make sure to explain the purpose of each artifact (i.e. Why is it on your to-do list? Why is it useful for your team?)
 * Be concise, yet precise.         
   For example: "Build the website" is not precise at all, but "Build a static home page and upload it somewhere, so that it is publicly accessible" is much clearer.

Create a demo video that shows mouse control using facial features. This will be run using the actual project and no trickery/mock-ups will be used. The purpose of this video is to demo the state of the current project as well as allow user feedback towards the usability of the software as well as any improvements that could be made. This will be used in the event that any live-demos fail due to the environmental reasons that are outside of our control including but certainly not limited to lighting, power issues, webcam issues, computer issues, and possibly more. The plan is to host this video on the Github. If not, it will be hosted on an external DigitalOcean server located in their Toronto datacenter and cached by CloudFlare’s CDN to be publicly accessible. It potentially will be embedded in the product page (for our project) also being hosted on an external DigitalOcean server (that may or may not be the same as the server hosting the video) located in their Toronto datacenter and cached by CloudFlare’s CDN to be publicly accessible (subject to availability and uptime of the server. May change in the future due to server upgrades/migrations.)

Create a chrome extension that creates a UI when browsing any webpage. This will take the form of buttons that overlay on top of the webpage allowing for multiple functionalities including zooming, creating new tabs, etc. It plays a **significant** role as it is **the main purpose of our project (and not on the webcam mouse control software)** 



