# a3.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kelly Bach
# kbach3@uci.edu
# 18576745
# a2.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kelly Bach
# kbach3@uci.edu
# 18576745

from pathlib import Path
import Profile
import json
import ui

def searches(string):
    splits = [] 
    pos = -1 
    last_pos = -1 
    while ' ' in string[pos + 1:]: 
        pos = string.index(' ', pos + 1) 
        splits.append(string[last_pos + 1:pos]) 
        last_pos = pos
    splits.append(string[last_pos + 1:]) 
    return splits 

def get_command(string):
    return searches(string)[0]

#C /ics32/a2-starter/Assignment2/ -n meow


def create_user(string):
    new = searches(string)[1] + searches(string)[3] + '.dsu'
    Path(new).touch()
    info = profile_info()
    create_profile(info, new)
    return new, info

def profile_info():
    user = input('Please enter a username.\n')
    password = input(f'Please enter a password, {user}.\n')
    bio = input(f'Please enter a bio {user}.\n')
    info = [user, password, bio]
    return info

def create(string):
    new = searches(string)[1] + searches(string)[3] + '.dsu'
    Path(new).touch()
    info = profile_info_admin()
    create_profile(info, new)
    return new, info

def profile_info_admin():
    user = input()
    password = input()
    bio = input()
    info = [user, password, bio]
    return info

def create_profile(string, pathway):
    profile = Profile.Profile(dsuserver=None, username=string[0], password=string[1], bio=string[2]) 
    Profile.Profile.save_profile(profile, pathway)

#O /ics32/a2-starter/Assignment2/meow.dsu
def open_file(string):
    path_name = searches(string)[1]
    try:
        f = json.load(open(path_name))
        username = f["username"]
        password = f["password"]
        bio = f["bio"]
        info = [username, password, bio]
    except FileNotFoundError:
        print('File not found. Please enter an existing file.') 
    return path_name, info       

def edit_file(string, pathway, info):
    num = (len(searches(string)) - 1 )
    i = 1 
    while i <= num: 
        profile = Profile.Profile(dsuserver=None, username=info[0], password=info[1], bio=info[2])
        if searches(string)[i] == '-usr':
            info[0] = searches(string)[i + 1]
            profile = Profile.Profile(dsuserver=None, username=info[0], password=info[1], bio=info[2])
        elif searches(string)[i] == '-pwd':
            info[1] = searches(string)[i + 1]
            profile = Profile.Profile(dsuserver=None, username=info[0], password=info[1], bio=info[2])
        elif searches(string)[i] == '-bio':
            info[2] = searches(string)[i + 1]
            profile = Profile.Profile(dsuserver=None, username=info[0], password=info[1], bio=info[2])
        elif searches(string)[i] == '-addpost':
            new_post = Profile.Post(searches(string)[i + 1])
            Profile.Profile.load_profile(profile, pathway)
            Profile.Profile.add_post(profile, post = new_post)
        elif searches(string)[i] == '-delpost':
            Profile.Profile.load_profile(profile, pathway)
            Profile.Profile.del_post(profile, int(searches(string)[i + 1]))
        Profile.Profile.save_profile(profile, pathway)
        i += 2

def print_info(string, pathway, info):
    num = (len(searches(string)) - 1 )
    i = 1 
    f = json.load(open(pathway))
    username = f["username"]
    password = f["password"]
    bio = f["bio"]
    info = [username, password, bio]
    entries = f["_posts"]
    while i <= num:
        if searches(string)[i] == '-usr':
            print(info[0])
        elif searches(string)[i] == '-pwd':
            print(info[1])
        elif searches(string)[i] == '-bio':
            print(info[2])
        elif searches(string)[i] == '-posts':
            for entry in entries:
                print(f'Your entry: {entry['entry']}. Time: {entry['timestamp']}.')
        elif searches(string)[i] == '-post':
            i += 1
            print(entries[int(searches(string)[i])]['entry'])
        elif searches(string)[i] == '-all':
            print(f'Your username: {info[0]}.\nYour password: {info[1]}.\nYour bio: {info[2]}.')
            for entry in entries:
                print(f'Your entry: {entry['entry']}. Time: {entry['timestamp']}.')
        i += 1

def get_file_name(string):
    if get_command(string) == 'C':
        info = create(string)
        return info
    elif get_command(string) == 'O': 
        info = open_file(string)
        return info
    

def get_file_name_user(string):
    if get_command(string) == 'C':
        info = create_user(string)
        return info
    elif get_command(string) == 'O': 
        info = open_file(string)
        return info 
    
def run():
    command = input(ui.welcome)
    if command == 'C':
        file_path = input(ui.create)
        name = input(ui.create2)
        search = f'{command} {file_path} -n {name}'
    elif command == 'O':
        file_path = input(ui.open_file)
        while file_path[-4:] != '.dsu':
            file_path = input()
        search = f'{command} {file_path}'
    data = get_file_name_user(search)
    pathway = data[0]
    info = data[1]
    comm = input(ui.subcommands)
    while comm != 'Q':
        if comm == 'E':
            inlist = []
            newcomm = 'E '
            subcomm = ''
            while subcomm != 'D':
                subcomm = input(ui.eoptions)
                if subcomm == 'D':
                    break
                inlist.append(subcomm)
                information = input(ui.specifics)
                inlist.append(information)
            for item in inlist:
                newcomm += f'{item} '
            edit_file(newcomm, pathway, info)
        elif comm == 'P':
            inlist = []
            newcomm = 'P '
            subcomm = ''
            while subcomm != 'D':
                subcomm = input(ui.poptions)
                if subcomm == 'D':
                    break
                inlist.append(subcomm)
            for item in inlist:
                newcomm += f'{item} '
            print_info(newcomm, pathway, info)
        comm = input(ui.subcommands)

def admin():
    search = input()
    data = get_file_name(search)
    pathway = data[0]
    info = data[1]
    while get_command != 'Q':
        search = input()
        if get_command(search) == 'E':
            edit_file(search, pathway, info)
        elif get_command(search) == 'P':
            print_info(search, pathway, info)

if __name__ == '__main__':
    initialuser = input('Hi! Are you a user or an admin?\n')
    useropt = ['user', 'admin']
    while initialuser not in useropt:
        initialuser = input('Please select user or admin.\n') 
    if initialuser == 'user':
        run()
    else:
        admin()
    