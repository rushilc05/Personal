from pathlib import Path
import json

def get_stored_userdata(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def get_new_userdata(path):
    """Prompt for a new username"""
    first_name = input("What's your first name: ")
    last_name = input("What's  your last name: ")
    location = input("What city do you live in: ")
    userdata = f"First Name: {first_name.title()} \nLast Name: {last_name.title()} \nLocation: {location.title()}"
    contents = json.dumps(userdata)
    path.write_text(contents)
    return userdata

def great_user():
    """Greet the user by name"""
    path = Path('username.json')
    username = get_stored_userdata(path)
    if username:
        print(f"Welcome back \n{username}")
    else: 
        username = get_new_userdata(path)
        print(f"Your information has been saved\n{username.title()}")

great_user()