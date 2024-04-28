from tinydb import TinyDB, Query

class Update:
    def __init__(self):
        self.db = TinyDB('posts.json')
    
    def delete_post(self, data):
        self.db.update(data)
        return "post updated"