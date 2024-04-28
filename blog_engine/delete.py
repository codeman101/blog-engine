from tinydb import TinyDB, where
class Delete:
    def __init__(self):
        self.db = TinyDB('posts.json')
    
    def delete_post(self, thing, ):
        self.db.remove(where[""])
        return "post deleted"