import quali_api
import os
import cloudshell.api.cloudshell_api as api
dirname = os.path.dirname(__file__)
#filename = os.path.join(dirname, 'relative/path/to/file/you/want')


def Update_server_ip(server_ip,user="admin",password="admin",domain="Global"):
    print "the selected server is on " + server_ip
    global session
    session = api.CloudShellAPISession(server_ip, user, password, domain)
    global quali_api_s
    quali_api_s = quali_api.QualiAPISession(server_ip, "admin", "admin")
    return

def selected_clp_app(clp_type):
    if clp_type=="AWS":
        import_aws_app()
    if clp_type == "MA":
        import_Azure_app()
    if clp_type == "OS":
        import_OpenStack_app()
    if clp_type == "VC":
        import_vcenter_app()

def import_aws_app():
    print "Importing AWS app"
    try:
        quali_api_s.ImportPackage(os.path.join(dirname,"Packages/AWS App.zip"))
        print "The app has been added successfully"
    except Exception as e:
        print e.message
        print "the aws app import has fail because some kind of fail"

def import_vcenter_app():
    try:
        quali_api_s.ImportPackage(os.path.join(dirname,"Packages/vCenter App.zip"))
        print "The app has been added successfully"
    except Exception as e:
        print e.message
        print "the vcenter app import has fail because some kind of fail"
    
def import_Azure_app():
    try:
        quali_api_s.ImportPackage(os.path.join(dirname,"Packages/Azure App.zip"))
        print "The app has been added successfully"
    except Exception as e:
        print e.message
        print "the Azure app import has fail because some kind of fail"

def import_OpenStack_app():
    try:
        quali_api_s.ImportPackage(os.path.join(dirname,"Packages/Azure App.zip"))
        print "The app has been added successfully"
    except Exception as e:
        print e.message
        print "the Azure app import has fail because some kind of fail"

import_OpenStack_app()