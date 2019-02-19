#!/usr/bin/env python
"""
vSphere Python SDK program for shutting down VMs
"""
from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim, vmodl

import argparse
import atexit
import getpass
import sys
import ssl



def GetArgs():
   """
   Supports the command-line arguments listed below.
   """

   parser = argparse.ArgumentParser(description='Process args for shutting down a Virtual Machine')
   parser.add_argument('-s', '--host', required=True, action='store', help='Remote host to connect to')
   parser.add_argument('-o', '--port', type=int, default=443, action='store', help='Port to connect on')
   parser.add_argument('-u', '--user', required=True, action='store', help='User name to use when connecting to host')
   parser.add_argument('-p', '--password', required=True, action='store', help='Password to use when connecting to host')
   args = parser.parse_args()
   return args


def main():

    args = GetArgs()
    service_instance = None
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    try:
        service_instance = SmartConnect(host=args.host,
                                                user=args.user,
                                                pwd=args.password,
                                                port=int(args.port),
                                                sslContext=context)
        if not service_instance:
            print("Could not authenticate with the specified ESXi host using "
                  "the supplied credentials")
            return -1

        atexit.register(Disconnect, service_instance)

        content = service_instance.RetrieveContent()
        # Search for all VMs
        objview = content.viewManager.CreateContainerView(content.rootFolder,
                                                          [vim.VirtualMachine],
                                                          True)
        vmList = objview.view
        objview.Destroy()

        for vm in vmList:
            if ('IPM' not in vm.name and 
                vm.runtime.powerState != vim.VirtualMachinePowerState.poweredOff):
                print("Shutting down VM: {vm_name}".format(vm_name=vm.name))
                vm.ShutdownGuest()
            
    except vmodl.MethodFault as error:
        print("Caught vmodl fault : " + error.msg)
        return -1

# Start program
if __name__ == "__main__":
    main()
