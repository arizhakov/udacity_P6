# udacity_P6
Description: Create a data visualization from a data set that tells a story or highlights trends or patterns in the data. Use either dimple.js or d3.js to create the visualization. Your work should be a reflection of the theory and practice of data visualization, such as visual encodings, design principles, and effective communication.


## Summary 
"in no more than 4 sentences, briefly introduce your data visualization and add any context that can help readers understand it"

This data visualization tries to boil down a large data set into a chart that can be easily absorbed. 5 dimensions of data are shown in the chart: Fare, Age, Sex, Survived, and Family size. The main explanatory finding is that females paying greater than 50 units of fare were very highly likely to survive - an explanatory finding of the larger concept of how data can be "flattened" from a complex table to a readable chart, and insights readily drawn. The added animation guides the reader from full data set to a message about survival rates by gender.  

For more information, please see Ref. 1 and 2 for more information on the data set itself. 


## Design 
"explain any design choices you made including changes to the visualization after collecting feedback"

Although it is understood that quantity of dimensions represented in a chart does not correlate with chart quality, it is of the author's personal interest to find multidimensional data and represent it effectively without reducing dimension. The color choice seemed to be approved by the reviewers, so the theme was kept. A fairly typical and recognizable scheme of pink/blue for female/male, and green/red for survived/died was chosen. 

After receiving feedback, it was clear that encoding technique needed to be clarified, such as what was the approach for obtaining bubble size from family size? An animation and careful highlighting was also added to stress the explanatory message about females of >50 fare having great survival chance. This also has the aim of focusing the viewer on the explanatory message, but also allowing them to view the entire data set visually to check the findings/conclusions as well as find their own insights.


## Feedback 
"include all feedback you received from others on your visualization from the first sketch to the final visualization"

Compiled and sorted responses from others:

*What do you notice in the visualization?*
- Most bubbles are concentrated in the bottom of the chart. Bubbles are clumped together in a way that makes their size and color harder to distinguish. 
- so tightly, closely

*What questions do you have about the data?*
- Are we looking at a visualization of every single passenger on the titanic? I would guess not as there does not seem to be enough bubbles. 
- How was family size related to gender of the passengers? Is a male's family bubble that includes ten females still a large bubble? 
- How does bubble size correspond to number of people who died? Does a big red bubble for a man mean he had a big family and all members died? 
- I'm also surprised by the relative lack of female survivor bubbles in the higher cost area. Common thought about that is that many first class female passengers survived. 
- no ?

*What relationships do you notice?*
- In general many more bubbles at the lower cost than the higher cost. Many single/small male bubbles at the low cost, over 20ish years old, most of whom appeared to have died. 
-  more Females survived, Males low Fare died

*What do you think is the main takeaway from this visualization?*
- That there were many more passengers traveling in low cost berths, as the concentration of bubbles at the bottom is the most striking part of the visualization. 
- The majority of female bubbles appear to be green-outlined and the majority of male bubbles appear to be red-outlined.  So males are more likely to have died and females more likely to survive. 
- Who pays more lives!

*Is there something you don’t understand in the graphic*
- No! I am intrigued by it. 
- If "the Bubble area proportional to family size", then why in the legend does it say Female and Male are one person?


## Resources 
"list any sources you consulted to create your visualization"

1) Source data. [https://www.google.com/url?q=https://www.udacity.com/api/nodes/5420148578/supplemental_media/titanic-datacsv/download&sa=D&ust=1469046383909000&usg=AFQjCNEK-LrXMfu2u5PeHh80hw0oFjZarA]

2) More Titanic data info. [https://www.google.com/url?q=https://www.kaggle.com/c/titanic-gettingStarted&sa=D&ust=1469046383910000&usg=AFQjCNFPyRTqbiHns4HMoTmqW69yNDvgiw] 

3) http://bl.ocks.org/tybyers/736da90eefe0c347a1d6

4) https://jrue.github.io/coding/2014/exercises/basicbubblepackchart/

5) http://dimplejs.org/advanced_examples_viewer.html?id=advanced_custom_styling

6) https://stackoverflow.com/questions/11189284/d3-axis-labeling

7) https://stackoverflow.com/questions/15288850/font-size-is-not-working-in-my-d3-js-code

8) "L3_basic_charts_final.html", from Udacity's "DATA VISUALIZATION WITH D3.JS"

9) http://www.jeromecukier.net/blog/2012/05/28/manipulating-data-like-a-boss-with-d3/

10) http://bl.ocks.org/mbostock/3888852

11) https://stackoverflow.com/questions/38595719/javascript-d3-js-multiple-transitions-of-points-on-a-scatter-plot
