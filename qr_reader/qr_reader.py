import cv2
from pyzbar import pyzbar
import re

class QrReader:

    def read_barcodes(self, frame):
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            x, y , w, h = barcode.rect
            barcode_text = barcode.data.decode('utf-8')
            result = re.findall(r'{\'userId\':\d{1,10}, \'electionId\':\d{1,10}}', barcode_text)
            if len(result) > 0:
                return frame, barcode_text
            cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        return frame, ''

    def run(self):
        json = ''
        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        while ret:
            ret, frame = camera.read()
            frame, json = self.read_barcodes(frame)
            cv2.imshow('E-vote barcode reader', frame)
            if (cv2.waitKey(1) & 0xFF == 27) or json != '':
                break

        camera.release()
        cv2.destroyAllWindows()
        return json


