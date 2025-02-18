-data gathering script-

-refrances text file of previous users and checks a new users name against others, 
if they are identified as a repeat user their data entry is bypassed as they already have a valid text file recourding thier specifics
-if a user is new it directs them twords the data entry
-users are asked to answer a few questions, such as which class they have during wich block
-their information is stored in a list
-this list if formatted using a for loop and users are asked to confirm if they entered the data correctly
-if not they are redirected, the list is cleared and the data entry process restarts
-once complete this information is commited to a text file under thier name
since they are first time users a new file is created for them
-costume elements such as a pingree pegusis inspired logo and a color scheme are employed throught the UI
-data gathering calls the script primary where the process continues, currently this is done by instancing a class in primary.
However, I am in the process of having primary instance a class from data gathering instead so that the logic flows more smoothly

-Primary script-

-THough this is currently headed by a class in the final version this will be the only script withoput a class and the other scripts will be called from it
-currently users are asked to reiterate thier names, beacuse despite substantial effort I was unable to pass the variable, this is somthing I intend to change promptly
-Once the name is rerecorded they are directed to a screen with a Drop down menu here they can select if they wish to view the TO-Do list functionality or the calender display
-Both of these currently work but do not actually lead to the displays 
-I am currently working on having the to-do drop down option send users to Max's scrtipt to recourd their tasks

-up next-

- up next I will do a major restructuring of classess to have primary as the parent script calling other scripts via thier classess

