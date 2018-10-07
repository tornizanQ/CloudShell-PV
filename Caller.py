import Create_Cloud_providers as clp_creator
import create_bridges_and_patch_panel_demand as bridge_constructor
import Create_Users_From_List as user_creator
from optparse import OptionParser
import ImportPacks
import sys

def main():

    parser = OptionParser(usage="usage: %prog [options] filename",version="%prog 1.0")
    parser.add_option("-c", "--create",
                      action="store",  # optional because action defaults to "store"
                      dest="action",
                      default="create",
                      help="Choose the action you would like to do: Create, Delete, Autoload", )
    parser.add_option("-s", "--server",
                      action="store",  # optional because action defaults to "store"
                      dest="server_ip",
                      default="localhost",
                      help="Choose the Cloudshell server IP", )
    parser.add_option("-z", "--cloudprovider",
                      action="store",  # optional because action defaults to "store"
                      dest="clp",
                      default="None",
                      help="Choose the cloud providers testing:\nVC - vCenter\nOS - OpenStack\nMA - Microsoft Azure\nAWS - AWS EC2", )
    parser.add_option("-b", "--bridgeconstructor",
                      action="store",  # optional because action defaults to "store"
                      dest="construct_bridges",
                      default="None",
                      help="Choose the number of bridges you want to create format Num_of_bridges/Num_of_ports/Use_Patch_Panel",)
    parser.add_option("-u", "--users",
                      action="store",  # optional because action defaults to "store"
                      dest="users",
                      default="None",
                      help="-u <path to a json file contain the user list>", )
    parser.add_option("-a", "--add",
                      action="store",  # optional because action defaults to "store"
                      dest="add_apps",
                      default="None",
                      help="-a <path to a json file contain the user list>", )
    (options, args) = parser.parse_args()

    print"************"
    print options
    print args
    print"***********"
    if options.action=="create":
        if options.clp!="None":
            clp_creator.Update_server_ip(options.server_ip)
            clp_creator.clp_selector(options.clp)
        elif options.construct_bridges!="None":
            bridge_construct_params=options.construct_bridges.split("/")
            if len(bridge_construct_params)!= 3:
              print "The bridge constructor demands exactly 3 parameters"
            else:
                print "creating bridges"
                bridge_constructor.Update_server_ip(options.server_ip)
                bridge_constructor.construct_bridges(int(bridge_construct_params[0]),int(bridge_construct_params[1]),bridge_construct_params[2])
        elif options.users != "None":
            user_creator.Update_server_ip(options.server_ip)
            user_creator.update_user_data_dest(options.users)
        elif options.add_apps != "None":
            try:
                ImportPacks.selected_clp_app(options.add_apps)
            except Exception as e:
                print "please type VC AWS MA or OS only"



    return



if __name__ == '__main__':
    main()