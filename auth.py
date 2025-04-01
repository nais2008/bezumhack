import os

def register_user(username, password):
    user_data_dir = "user_data"
    if not os.path.exists(user_data_dir):
        os.makedirs(user_data_dir)
    user_file_path = os.path.join(user_data_dir, f"{username}.txt")
    if not os.path.exists(user_file_path):
        with open(user_file_path, "w") as f:
            f.write(password)
        return True
    else:
        return False
    
def login_user(username, password):
    user_data_dir = "user_data"
    if not os.path.exists(user_data_dir):
        return False
    if os.path.exists(os.path.join(user_data_dir, f"{username}.txt")):
        with open(os.path.join(user_data_dir, f"{username}.txt"), "r") as f:
            stored_password = f.read()
        if stored_password == password:
            return True
    return False
