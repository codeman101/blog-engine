from tinydb import TinyDB, Query

class Create:
    def __init__(self):
        self.db = TinyDB('posts.json')
    
    def add_post(self, data):
        self.db.insert(data)
        return "post added"