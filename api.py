import requests


def new_folder(my_url, my_token, path):

    headers = {'Authorization': my_token}
    params = {'path': path}
    response = requests.put(my_url, params=params, headers=headers)
    return response
