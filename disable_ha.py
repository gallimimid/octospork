import atexit 
import ssl

from pyVmomi import vim, vmodl 
from pyVim import connect 
from pyVim.connect import Disconnect 
 
inputs = {'vcenter_ip': '10.130.19.10', 
          'vcenter_password': 'Password1!', 
          'vcenter_user': 'administrator@vsphere.local',
          'cluster' : 'Lab1_Cluster'    
          } 

def get_obj(content, vimtype, name): 
    """ 
     Get the vsphere object associated with a given text name 
    """     
    obj = None 
    container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True) 
    for c in container.view: 
        if c.name == name: 
            obj = c 
            break 
    return obj 

def main(): 
    try: 
        si = None 
        try: 
            s=ssl.SSLContext(ssl.PROTOCOL_TLSv1)
            s.verify_mode=ssl.CERT_NONE
            si = connect.Connect(inputs['vcenter_ip'], 443, inputs['vcenter_user'], inputs['vcenter_password'],sslContext=s) 
        except IOError as e:
            pass 
            atexit.register(Disconnect, si) 
 
        content = si.RetrieveContent() 

        cluster = get_obj(content, [vim.ClusterComputeResource], inputs['cluster'])

        cluster_spec = vim.cluster.ConfigSpecEx()

        config_info = vim.cluster.DasConfigInfo() 
        config_info.enabled = False

        cluster_spec.dasConfig = config_info

        task = cluster.ReconfigureComputeResource_Task(cluster_spec, True) 

    except vmodl.MethodFault as e:
            msg = e.msg 
            if(msg.startswith("The setting of vmConfig is invalid")): 
                print("Couldn't disable HA for %s" % vm.name)
                print("Please turn off and turn on HA from Cluster settings.")
            else: 
                self.logger.error("Caught vmodl fault: %s" % e.msg) 
                return 1 
    except Exception as e:
        print("Caught exception: %s" % str(e))
        return 1 
     
# Start program 
if __name__ == "__main__": 
    main() 
