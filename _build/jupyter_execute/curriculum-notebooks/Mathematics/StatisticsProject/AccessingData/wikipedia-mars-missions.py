![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/StatisticsProject/AccessingData/wikipedia-mars-missions.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Mars Missions

We can look at Mars missions using a [data table from Wikipedia](https://en.wikipedia.org/wiki/List_of_missions_to_Mars#Missions). 

url = 'https://en.wikipedia.org/wiki/List_of_missions_to_Mars'

import pandas as pd
df = pd.read_html(url)[0]
df

Then we can create a new column called `Year` from the `Launch Date` column, and graph the number of missions over time.

df['Year'] = df['Launch Date'].str.split(' ', expand=True)[2]
import cufflinks as cf
cf.go_offline()
df.groupby(by='Year')['Year'].count().iplot(kind='bar', yTitle='Number of Missions', xTitle='Year', title='Mars Missions over Time')

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)