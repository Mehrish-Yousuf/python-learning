from bs4 import BeautifulSoup
import requests

weburl = "https://www.imdb.com/title/tt0468569/reviews?ref_=tt_urv"


page = requests.get(weburl)

soup = BeautifulSoup(page.content,'html.parser')

results = soup.find('div', id='main')

movie_name = results.find('h3').find('a')

movie_year = results.find('h3').find('span')

print(movie_name.text.strip() +movie_year.text.strip()) 

main_content = results.find('div', class_='lister')

noOfReviews = main_content.find('span')

print(noOfReviews.text)
 
reviewsList = main_content.find_all('div', class_='lister-item')

# print(reviewsList)

for review in reviewsList:

    print(" ")  #just for adding a line 


    #The div contains the user reviews
    listContent = review.find('div', class_='lister-item-content')

    reviewTitle = listContent.find('a', class_='title')

    print('Review Title:', reviewTitle.text.strip())

    rating = listContent.find('span', class_='rating-other-user-rating')  #rating span

    if rating==None:
        continue

    ratingText = rating.find_all('span')  #the actual rating text
    
    print("Rating: ",ratingText[0].text.strip())

    userName = listContent.find('span', class_='display-name-link')

    print('Username: ', userName.text)

    reviewDate = listContent.find('span', class_='review-date')
    print('Review Date:', reviewDate.text)

    reviewContent = listContent.find('div', class_='text')

    print('Review:',reviewContent.text)

