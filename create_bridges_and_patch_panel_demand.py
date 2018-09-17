import cloudshell.api.cloudshell_api as api

def Update_server_ip(server_ip,user="admin",password="admin",domain="Global"):
    global session
    print "the selected server is on "+ server_ip
    session = api.CloudShellAPISession(server_ip, user, password, domain)
    return

def construct_bridges(number_of_bridges,number_of_ports,patch_panel_requiered,server_ip):
    session = api.CloudShellAPISession(server_ip, "admin", "admin", "Global")

    PP_port_counter=0
    port_mapping_list = []
    if patch_panel_requiered=="True":
        try:
            temp_pp= session.CreateResource("PatchPanel","Generic PatchPanel","Patch Panel","1.1.1.1")
        except:
            temp_pp=session.GetResourceDetails("Patch Panel")
            print "Patch Panel resource allready exist"

    for i in range(number_of_bridges):
        try:
            temp_bridge=session.CreateResource("Bridge","Bridge Generic Model","Br"+str(i),"1.1.1.1")
        except:
            temp_bridge=session.GetResourceDetails("Br"+str(i))
            print "Br"+str(i)+" resource allready exist"

        for y in range(number_of_ports):
            try:
                temp_pp_port = session.CreateResource("Panel Jack","Generic Jack","P"+str(PP_port_counter),"1.1.1.1","","Patch Panel")
            except:
                temp_pp_port = session.GetResourceDetails("Patch Panel"+"\\"+"P"+str(PP_port_counter))
                print "P"+str(PP_port_counter)+" resource allready exist"
            PP_port_counter += 1
            try:
                temp_port=session.CreateResource("Bridge Port","Bridge Port Generic Model","P"+str(y),"1.1.1.1","","Br"+str(i))
            except:
                temp_port = session.GetResourceDetails("Br"+str(i)+"\\"+"P"+str(y))
                print "P"+str(y)+" resource allready exist"
            port_mapping_list.append(api.PhysicalConnectionUpdateRequest(temp_pp_port.Name,temp_port.Name,""))
    session.UpdatePhysicalConnections(port_mapping_list)
    print "Command ran successfully"




