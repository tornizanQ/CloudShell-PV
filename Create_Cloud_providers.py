import cloudshell.api.cloudshell_api as api
import json

cloudproviders_data = json.load(open('C:\Python Projects\Create Cloud Providers\Data\Cloudproviders data.json'))
#session = api.CloudShellAPISession("172.40.0.213", "admin", "admin", "Global")
#set new IP for the session
def Update_server_ip(server_ip,user="admin",password="admin",domain="Global"):
    print "the selected server is on " + server_ip
    global session
    session = api.CloudShellAPISession(server_ip, user, password, domain)
    return

def clp_selector (clp_type):
    clp_full_name = ""
    if clp_type=="VC":
        clp_full_name="VMware vCenter"
    elif clp_type=="MA":
        clp_full_name ="Microsoft Azure"
    elif clp_type=="OS":
        clp_full_name ="OpenStack"
    elif clp_type=="AWS":
        clp_full_name ="AWS EC2"
    else:
        help_doco()
    clp_creator(clp_full_name)
    return

def help_doco():
    print "AWS for aws Ec2 \n"\
          "VC for VMWare vCenter \n"\
          "OS for OpenStack \n"\
          "MA for Microsoft Azure \n"
    return

def clp_creator(clp_type):
    ip_address="None"
    if clp_type=="VMware vCenter":
        ip_address=cloudproviders_data["Cloud oroviders addresses"]["VMware vCenter address"]
        print "VMware vCenter address is:" + ip_address
    try:
        cloudprovider = session.CreateResource("Cloud Provider",clp_type,clp_type,ip_address)
        print "Starting to create " + clp_type + " cloudProvider"
    except:
        print "There is already cloudprovider named " + clp_type
    attribute_list = Attribute_list_gen(clp_type)
    clp_attributes = api.ResourceAttributesUpdateRequest(clp_type, attribute_list)
    session.SetAttributesValues(clp_attributes)
    #session.UpdateResourceDriver(clp_type, "VCenter Shell Driver")
    session.AutoLoad(clp_type)

    print clp_type + " created successfully"
    return

# get the clp type chosen by the user and setting the relevant attributes from the "cloudproviders data.json" file
def Attribute_list_gen(clp_type):
    set_attributes = []
    selected_cloudprovider = cloudproviders_data[clp_type]
    print "Configuring " + clp_type + "attributes:"
    for attribute in selected_cloudprovider:
        print attribute+ " = "+ selected_cloudprovider[attribute]
        # put all the attribute from the json file to a list "attribute name","attribute value"
        set_attributes.append(api.AttributeNameValue(attribute, selected_cloudprovider[attribute]))
    return set_attributes