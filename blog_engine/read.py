from tinydb import TinyDB, Query

class Read:
    def __init__(self):
                self.db = TinyDB('posts.json')
    
    def delete_post(self, data):
        self.db.insert(data)
        return "post deleted"