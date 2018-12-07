from bs4 import BeautifulSoup
import os
import pandas as pd

# List of dictionaries to build file by file and later convert to a DataFrame
df_list = []
folder = 'rt_html'

for movie_html in os.listdir(folder): #Here there should be a list of similar webpages to scrap from
    with open(os.path.join(folder, movie_html)) as file: #Define file as the name to be used
        soup = BeautifulSoup(file, 'lxml') #We need to add the lxml don't know why
        title = soup.find('title') #This one was easy. IT will get worse
        #For this one we first find the div tag but whenever there's class (original text <div class="audience-score meter">) we need the class_
        #Just by inputting audience_score = soup.find('div',class_='audience-score meter') we get a larger text so we need to find a substring by using find('span')
        audience_score = soup.find('div',class_='audience-score meter').find('span').contents[0 ][:-1] #The [:-1] will eliminate the right character so we don't get the % sign
        num_audience_ratings = soup.find('div', class_='audience-info hidden-xs superPageFontColor') #This will give a larger portion of text
        #from the larger section, we notice that there are 2 'divs' so we find them both by using find_all, then we want the 2nd one which is why we use the [1]
        #just by num_audience_ratings = num_audience_ratings.find_all('div')[1] we still get a lot of the tags, which is why we use .contents and we use [2] to select the number we wants
        num_audience_ratings = num_audience_ratings.find_all('div')[1].contents[2].strip().replace(',','') #we use strip() to remove spaces and replace to take out the comma
        # Append to list of dictionaries
        df_list.append({'title': title,
                        'audience_score': int(audience_score),
                        'number_of_audience_ratings': int(num_audience_ratings)})
df = pd.DataFrame(df_list, columns = ['title', 'audience_score', 'number_of_audience_ratings'])
