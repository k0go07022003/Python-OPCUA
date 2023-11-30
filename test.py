import opc as OPC
from opcua import Client
import Tags
import time

client = Client("opc.tcp://127.0.0.1:4840")

tag_struct = Tags.TestTags
varpath = Tags.TestPath

delay_time = 2
reset_tag = tag_struct[3]

def test_init_prg():
    OPC.Connect(client)

    OPC.end_test(client, tag_struct, varpath, reset_tag)


def test_u_gd_00():
    OPC.Connect(client)
    objects = OPC.getvar(client)

    OPC.write_opc_var(objects,varpath, tag_struct[2], True)
    time.sleep(delay_time)
    data=OPC.read_opc_var(objects, varpath, tag_struct[0])
    assert data==1
    print (f"{tag_struct[0]} = {data}")
    OPC.end_test(client, tag_struct, varpath, reset_tag)

def test_disconnect():
    OPC.Disconnect(client)
    exit()

test_init_prg()
test_u_gd_00()
test_disconnect()




