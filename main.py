from blog_engine.create import Create
from blog_engine.delete import Delete
from blog_engine.read import Read
from blog_engine.update import Update


def main():
    operation = input("what operation do you want to do in regards to a post?\n Choices: search, make, delete, update")
    if operation == "search":
        Read()
    elif operation == "make":
        Create()
    elif operation == "delete":
        Delete()
    elif operation == "update":
        Update()
    else:
        return "invalid operation"  