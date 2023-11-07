import requests
def repos(username):
    access_token='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'
    url=f'https://api.github.com/users/{username}/repos'
    headers={
        'Authorization': f'tokan{access_token}'
    }
    response=requests.get(url,headers=headers)
    my_data=response.json()
    # print(my_data)
    response=[]
    for repo_dict in my_data:
        response.append(repo_dict['name'])
    return response
print(repos(username='rohitnaruka'))
print(len(repos(username='rohitnaruka')))

import requests
# def repos(username,repo_name):
#     access_token='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'
#     url=f"https://api.github.com/repos/{username}/{repo_name}/commits"
#     headers={ 'Authorization': f'tokan{access_token}'}
#     response=requests.get(url,headers=headers)
#     my_data=response.json()
#     print(my_data)
#     commit_list=[]
#     for commit in my_data:
#         commit_dict={
#             'sha':commit ['sha'],
#             'date':commit['commit']['author']['date'],
#             'author_name':commit['commit']['author']
#         }
#         commit_list.append(commit_dict)
#     return commit_list
# print((repos(username='rohitnaruka',repo_name='python_')))
# print(len(repos(username="rohitnaruka",repo_name='python_')))




# import requests
# def repos(username,repo_name):
#     access_token='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'
#     url=f"https://api.github.com/repos/{username}/{repo_name}/commits"
#     headers={ 'Authorization': f'tokan{access_token}'}
#     response=requests.get(url,headers=headers)
#     my_data=response.json()
#     print(my_data)
# print(repos(username='rohitnaruka',repo_name='python'))

