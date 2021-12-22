import requests
import constants
import random
import time

def get_users():
    response = requests.get(constants.THE_PATH_TO_USERS)
    return response.json()

def show_all_information(id):
    response = requests.get(constants.THE_PATH_TO_USERS + '?id=' + str(id))
    result = response.json()[0]  
    for key, value in result.items():
        print(key, '-->', value if key not in ['address', 'company'] else '')
        if key=="address" or key=='company':
            for key_add, value_add in value.items():
                print('-----', key_add, '-->', value_add if key_add!='geo' else '') 
                if key_add=='geo':
                    for key_geo, value_geo in value_add.items():
                        print('----------', key_geo, '-->', value_geo)   
                    
def show_posts_of_user(id):
    response = requests.get(constants.THE_PATH_TO_POSTS + '?userId=' + str(id))
    result = response.json()
    for item in result:
       print('ID: {}; Title: {}'.format(item['id'], item['title']))

def show_information_about_post(id, id_post):
    response = requests.get(constants.THE_PATH_TO_POSTS + '?userId=' + str(id) + '&id=' + id_post)
    try:
        result = response.json()[0]    
    except IndexError: 
        print("There is no such post in the list!")
        return    
    print('ID: {}\nTitle: {}\nText: {}'.format(result['id'], result['title'], result['body']))  
    
    response_comments = requests.get(constants.THE_PATH_TO_COMMENTS + '?postId=' + id_post)
    result_comments = response_comments.json()
    count_of_comments = len(result_comments)
    id_comments = ', '.join([str(item['id']) for item in result_comments])
    print('Count of comments: {}\nID comments: {}'.format(count_of_comments, id_comments))

def show_task_list(id, completed=True):
    response = requests.get(constants.THE_PATH_TO_TODOS + '?userId=' + str(id) + '&completed=' + str(completed).lower())
    result = response.json()     
    if len(result)==0:
        print('There are no tasks in the user!')
    else:
        for item in result:
            print('ID: {}; Title: {}'.format(item['id'], item['title']))

def show_url_random_picture(id):
    response = requests.get(constants.THE_PATH_TO_ALBUMS + '?userId=' + str(id))
    result = response.json()
    if len(result)==0:
        print('There are no pictures in the user!')
        return
        
    index_album = random.randint(0, len(result) - 1)
    id_album = result[index_album]['id']    
    
    response_foto = requests.get(constants.THE_PATH_TO_PHOTOS + '?albumId=' + str(id_album))
    result_foto = response_foto.json()
    if len(result_foto)==0:
        print('There are no foto in the user!')
        return
    index_photo = random.randint(0, len(result_foto) - 1)
    print("URL: ", result_foto[index_photo]['url'])
    
def placeholder():  
    list_of_users = get_users()
    for item in list_of_users:
        print('ID:{}; Name:{}; Nickname:{}'.format(item['id'], item['name'], item['username']))
    
    user_ID = int(input("Enter the user ID: "))
    if len([step for step in list_of_users if step['id'] == user_ID])==0:
        print('There is no user with this ID!')
        return
      
    loop = True
    while loop == True:
        print ('===================================================')
        print ('               MENU PLACEHOLDER                    ')
        print ('===================================================')
        print (' 1 - Complete user information')
        print (' 2 - Posts')
        print ('   2.1 - List of user posts')
        print ('   2.2 - Information about a specific post')
        print (' 3 - TO DO')
        print ('   3.1 - List of uncompleted tasks')
        print ('   3.2 - List of completed tasks')
        print (' 4 - Display the URL of the random picture') 
        print (' 0 - Exit')
        print ('===================================================')
        response = input('Enter a selection -> ')
        if response == '1': show_all_information(user_ID)
        elif response == '2.1': show_posts_of_user(user_ID)
        elif response == '2.2': show_information_about_post(user_ID, input('Enter ID post: '))
        elif response == '3.1': show_task_list(user_ID, False)
        elif response == '3.2': show_task_list(user_ID)
        elif response == '4': show_url_random_picture(user_ID)
        elif response == '0': # Exit the program
            print ('Goodbye!')
            loop = False
        else:
            print ('Unrecognized command. Try again.')
        time.sleep(2)

placeholder()