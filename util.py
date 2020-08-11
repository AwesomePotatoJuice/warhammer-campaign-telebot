import os

filename = 'users.wah'


def write_to_app_data(user_name, user_id):
    path_app_data = os.getenv('APPDATA')

    if os.path.exists(path_app_data + filename):
        append_write = 'a'  # append if already exists
    else:
        append_write = 'w'  # make a new file if not

    users_file = open(filename, append_write)
    users_file.write(user_name + ':' + user_id + ";")
    users_file.close()
