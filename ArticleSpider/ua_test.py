from fake_useragent import UserAgent

class RandomUA():
    def __init__(self):
         self.ua = UserAgent()
         self.ua_type = 'random'
    def random_ua(self):
         def get_ua():
             return getattr(self.ua, self.ua_type)
         return get_ua()

r = RandomUA()
print(r.random_ua())