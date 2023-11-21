
from authorization.authorozation_controller import AuthorizationController
from qr_reader.qr_reader import *
from ast import literal_eval
from face_detection.face_autho import *

def main():
    authorization = AuthorizationController()
    qr_reader = QrReader()
    user_json = literal_eval(qr_reader.run())
    print(user_json)
    authorization.load_image(str(user_json.get('userId')))
    face_authorization = FaceAuthorization()
    if face_authorization.authorize():
        authorization.redirect_to_voting(str(user_json.get('userId')),str(user_json.get('electionId')))



if __name__ == '__main__':
    main()