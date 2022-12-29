''' module sends a text message
'''

import re
import requests


def send_text(args):
    '''
        send a text message to the supplied numer - note requires a valid key
        current key is good for 1 message a day
    '''
    # Get params
    phone = re.sub('[^0-9]', '', args[0])
    if len(phone) == 11:  # include country code of 1 for US
        message = args[1]
        if len(message) > 0:
            resp = requests.post('https://textbelt.com/text', {
                'phone': phone,
                'message': message,
                'key': 'textbelt',
            }, timeout=3)
            if resp.status_code == 200:
                messages = resp.json()
                quota = messages['quotaRemaining']
                if messages['success'] is True:
                    print(f'Message sent ok, quota remaining = {quota}')
                else:
                    error = messages['error']
                    print(
                        f'message failed, quota remaining = {quota}, error message is: {error}')
            else:
                print(resp)
        else:
            print('message must be included')
    else:
        print(
            'Please enter a valid phone number! of 11 digits, include country code (US=1)')


send_text(['<put receipient phone number here>', '<your message>'])
