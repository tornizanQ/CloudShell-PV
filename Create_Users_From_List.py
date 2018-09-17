import cloudshell.api.cloudshell_api as api
import json
users_data = json.load(open("C:\Python Projects\Create Cloud Providers\Data\Users Data.json"))
session = api.CloudShellAPISession("192.168.30.50", "admin", "admin", "Global")
#set new IP for the session
def Update_server_ip(server_ip,user="admin",password="admin",domain="Global"):
    global session
    session = api.CloudShellAPISession(server_ip, user, password, domain)
    return

#Create Groups from json data,
def Create_New_Groups():
    for group in users_data:
        group_name = group
        group_role = users_data[group]["Role"]
        group_domain = users_data[group]["Domain"]
        try:
            session.AddNewGroup(group_name,"test",group_role)
            print group_name + " was created successfully"
        except Exception as e:
            print e.message
        try:
            session.AddGroupsToDomain(group_domain,[group_name])
        except Exception as e:
            print e.message
            print" "
            print "Creating new Domain named: " + group_domain
            session.AddNewDomain(group_domain)
            session.AddGroupsToDomain(group_domain, [group_name])
        users_json = users_data[group]["Users"]
        users_list = list_of_New_Users(users_json)
        try:
            print "Adding the users to the group: " + group_name
            session.AddUsersToGroup(users_list,group_name)
        except Exception as e:
            print "there where a problem adding some of the users to the following group: " + group_name
            print e.message
            raise e
        print "The users has been created and added to their grups successfully"
    return

#get a list of users and passwords
def list_of_New_Users(users_json):
    user_list=[]
    for user in users_json:
        try:
            session.AddNewUser(user,users_json[user],"",True)
            print "user named: " + user + " was created"
        except Exception as e:
            print "the "+ user+" allready exist"
            #print e.message

        user_list.append(user)
    return user_list



#Define the destenation of the json file
def update_user_data_dest(updated_user_dest):
    global users_data
    try:
        json_data = json.load(open(updated_user_dest))
        users_data = json_data["Groups"]
        print"new user data json was loaded successfully"
    except:
        print "the file is from wrong format or unreachable"
        return
    Create_New_Groups()
    return