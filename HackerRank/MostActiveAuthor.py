# MOst Active Authors

# url: https://jsonmock.hackerrank.com/api/article_users?page=<pageNumber>

#threshold : integer that represents the threshold value for the number of submission COunt
# function should return an array of strings representing the usernames of users whose submission count is greater than the given threshold

# usernames in array must be ordered in order they appear in API response

import requests
import json

def getusernames(threshold):
    usernames = []
    page = 1
    totalPages = 1

    #check total pages
    while page < totalPages:
        #request for each page
        apiRequest = requests.get('https://jsonmock.hackerrank.com/api/article_users?page=' + str(page))
        userdata = apiRequest.json()['data']

        #setting totalPages Number
        if page == 1:
            totalPages = apiRequest.json()['total_pages']
        
        #get data for each user
        for value in userdata:
            submissionCount = value['submissionCount']

            #check if the submissionCount > threshold
            if submissionCount > threshold:
                usernames.append(value['username'])
        
        #increase page by 1
        page += 1
    return usernames

names = getusernames(10)
print(names)
