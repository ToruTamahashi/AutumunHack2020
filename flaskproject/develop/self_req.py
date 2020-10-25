import requests



def get_req():
    r = requests.get(
        'http://localhost:5000/get?value=111'
    )
    print(r.text)
    return r

def post_req():
    # headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
    # ,headers=headers
    payload = \
        [
                {"no": "1", "name": "name1", "score": "98"},
                {"no": "2", "name": "name2", "score": "80"},
                {"no": "3", "name": "name3", "score": "67"},
                {"no": "4", "name": "name4", "score": "32"}
        ]
    #payload = {'username': 'mike'}
    r = requests.post(
        'http://localhost:5000/post', json=payload
    )
    print(r.text)
    return r

def oauth_test():
    r = requests.get(
        'http://localhost:5000/login'
    )
    print(r.text)
    redirect_url = r.text
    param = redirect_url.split('&')
    oauth_verifier = param[1].split('=')
    print(oauth_verifier)
    return r