import requests
import shutil
import webbrowser

class AuthorizationController:
    
    config_file_path = 'config.txt'
    api_url = ''
    voting_url = ''
    load_image_url = ''
    image = ''
    path_save_image = 'face_detection/faces/1.jpg'


    def __init__(self):
        with open(self.config_file_path) as config:
            urls = []
            for line in config:
                urls.append(str(line).rstrip())
            self.api_url = urls[0]
            self.voting_url = urls[1]
            self.load_image_url = urls[2]
  


    def load_image(self, user_id):
        r = requests.get(self.api_url + self.load_image_url + user_id)
        json = dict(r.json())
        if json.get('imgUrl') != None:
            r = requests.get(json.get('imgUrl'))
            new_image = open(self.path_save_image, 'wb')
            new_image.write(r.content)
            new_image.close()


    def redirect_to_voting(self, user_id, election_id):
        # requests.post(self.api_url + self.voting_url + f'{user_id}/{election_id}')
        webbrowser.open_new(self.api_url + self.voting_url + f'{user_id}/{election_id}')
