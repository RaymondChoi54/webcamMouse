# LimbsFree Project Team 4

## Iteration 3

 * Start date: Friday, March 17th, 2017
 * End date: Thursday, March 23rd, 2017

## Process

#### Changes from previous iteration

List the most significant changes you made to your process (if any).

 * At most 3 items
 * Start with the most significant change
 * For each change, explain why you are making it and what you are hoping to achieve from it
 * Ideally, for each change, you will define a clear success metric (i.e. something you can measure at the end of the iteration to determine whether the change you made was successful)

 > *Note:* If you are not making any changes to your process, it means that you are happy with all of the decisions you made in the previous iterations.
 > In this case, list what you consider to be the most significant process decisions your team made. For each decision, explain why you consider it successful, and what success metric you are using (or could use) to assert that the decision is successful.

We are happy with continuing our current process. It has been fairly effective. The most significant process-related decision we made was using a Trello Scrum/Kanban style todo list. This allows for the prioritization and tracking of the progress of each task. It also allows for members to input new ideas into the board as well as find out who is working on what task quickly. We feel this has been successful as it keeps everyone on the same page. Since we have this to keep track of what everyone is working on, we can easily keep in touch with each other and find out the progress of everyone on the team. In terms of the success metric - we can point to the fact that we achieved our goals for the last iteration 

We did make a minor change regarding the tools we used - we started using Facebook messenger as our method of communication. We believe it will facilitate more productive communication than slack. As messenger is something that is checked more often, it allowed for more frequent communication. Overall, messenger will allow us to keep track how the progress on each task much easier and keep everyone on the same frequency. We will keep track of whether or not switching to messenger was successful or not in two ways. First, by comparing the number of commits in the repository after the change to before the change. Secondly, by tracking the total number comments made in messenger vs slack.

In terms of the webcam software, other than the detection algorithm change (from nose to center of the face) that was made in the early iterations, there are no significant changes that were made to the process. 

#### Roles & responsibilities

Describe the different roles on the team and the responsibilities associated with each role.

Create a Chrome extension that creates an UI for easier and more accurate navigation. It will make buttons appear on the website which offer functionality which makes it easier to browse the internet. Such functions include zoom buttons, back and forward buttons, and etc

Create a Python application that allows for the user to control the mouse cursor with the webcamera. It is important to note that this is not the focus of our product; but rather a tool to achieve the purpose of ease-of-navigation. This will be done by Raymond and Timothy. This goal is around 50% completed as of the end of Iteration 1. This program is composed of two pieces - a python program to track the face, as well as a python program that can accept inputs to move the mouse cursor around the screen. This program’s control mechanism is different from other webcam control software as this program treats the controlling mechanism as a Touchpoint rather than a Trackpad. (Again, not the main purpose of this project, but worth noting)

Create a website which provides the software to download, a video demo, and a mechanism for feedback.

Compile the entire suite of software into an executable installer. This will be done using InstallCreator (and perhaps some better/mainstream install builder if time permits). This decision to use this software was chosen as Raymond had experience using that mentioned software to create installers.

#### Events

Describe meetings (and other events) you are planning to have:

 * When and where? In-person or online?
 * What's the **purpose** of each meeting?
 * Other events could be coding sessions, code reviews, quick weekly sync' meeting online, etc.

We will have three in person meetings. The first is today, March 17th, in order to plan this iteration and finish this document. The second is the session to make the video. Shortly before the iteration review, we will meet over Skype to have a sync meeting to determine if everybody is caught up and pull everything together if needed. Finally, we will meet in person to finalize the iteration review doc 

#### Artifacts

List/describe the artifacts you will produce in order to organize your team.       

 * Artifacts can be to-do lists, task boards, schedule(s), etc.
 * We want to understand:
   * How do you keep track of what needs to get done?
   * How do you prioritize tasks?
   * How do tasks get assigned to team members?

Artifacts
To-do list in a kanban/scrum fashion. Hosted on Trello. This allows for the prioritization and tracking of the progress of each task. It also allows for members to input new ideas into the board as well as find out who is working on what task quickly. Priority are determined in our planning meetings and labelled using labels in our Trello. For example, a high priority is to get a major feature working (such as having the extension overlay properly) and fixing major bugs while new minor features are prioritized lower. We aim to create a stable program first before adding new features. https://trello.com/b/KO50esVS/projects
Since each member knows their role, they are assigned to each card on Trello that matches their role. To be more precise, Raymond and timothy focus on the mouse webcam control tool, Rohan focuses on the landing page/website, and Kevin, Brock, James focuses on the Chrome extension.
Code to be managed on Github. Please refer to the Git / GitHub workflow section for more information on our workflow.
The person that created the pull request cannot merge their own code. It must be approved by another team member before being merged by yourself/other members. By doing this we make sure two experts on that section of the code has looked at the code; ensuring that the code runs according to specification.
Issues are to be managed on Trello. New issues are opened up with a high priority label and assigned to the respective members who are working on that feature.
Communication is now primarily handled through Facebook Messenger. It integrates nicely into all of the member’s personal workflow allowing for faster and more efficient communication, as opposed to Slack. 

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

Complete the website and add all the features in
We will adjust the chrome app so that there are buttons for specific webpages. For example, on YouTube there will be a button to pause the video and on Google there will be a button to trigger voice input. This will allow for easier use of popular webpages.
We will be adding a setting menu for the user to adjust their settings for a more personalized experience. So users will be able to adjust the sensitivity, trigger calibration mode, invert the mouse, and change mouse acceleration.
The ability to save and load settings will also be added, so that the user doesn’t have to go through the calibration process each time.


#### Artifacts

List/describe the artifacts you will produce in order to present your project idea.

 * Artifacts can be text, code, images, videos, interactive mock-ups and/or any other useful artifact you can think of.
 * Make sure to explain the purpose of each artifact (i.e. Why is it on your to-do list? Why is it useful for your team?)
 * Be concise, yet precise.         
   For example: "Build the website" is not precise at all, but "Build a static home page and upload it somewhere, so that it is publicly accessible" is much clearer.

Create a demo video that shows mouse control using facial features. This will be run using the actual project and no trickery/mock-ups will be used. The purpose of this video is to demo the state of the current project as well as allow user feedback towards the usability of the software as well as any improvements that could be made. This will be used in the event that any live-demos fail due to the environmental reasons that are outside of our control including but certainly not limited to lighting, power issues, webcam issues, computer issues, and possibly more. The plan is to host this video on the Github. If not, it will be hosted on Google Drive or Google Compute Engine. May change in the future due to server upgrades/migrations.)

Create a website showcasing the project. It will include the following sections: introduction, about, product demo, download, feedback form
