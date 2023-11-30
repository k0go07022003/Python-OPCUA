# Python-OPCUA
How to connect Python script to PLC via OPCUA

If u want do this with security connection you need to set this:

client.set_security_string("Basic256Sha256,SignAndEncrypt,cert.der,key.pem")

client.set_user("twoja_nazwa_użytkownika")

client.set_password("twoje_hasło")

That is all :)

    client = Client("opc.tcp://127.0.0.1:4840") //Codesys OPCUA server address

    tag_struct = Tags.TestTags //Import array of variables 
    varpath = Tags.TestPath //Import array with path to OPCUA tags

    delay_time = 2
    reset_tag = tag_struct[3]

    def test_init_prg():
      OPC.Connect(client) //Connecting to Codesys OPCUA server
  
      OPC.end_test(client, tag_struct, varpath, reset_tag) //Reseting all tags after test


    def test_u_gd_00():
      OPC.Connect(client) //Connecting to Codesys OPCUA server
      objects = OPC.getvar(client) //Reading list of objects
  
      OPC.write_opc_var(objects,varpath, tag_struct[2], True) //Writing value to the tag
      time.sleep(delay_time) //Delay
      data=OPC.read_opc_var(objects, varpath, tag_struct[0]) //Reading the tag
      assert data==1 //Checking error exist
      print (f"{tag_struct[0]} = {data}") //Writing tag and his value on console
      OPC.end_test(client, tag_struct, varpath, reset_tag) //Reseting all tags after test

    def test_disconnect():
      OPC.Disconnect(client)
      exit()

    test_init_prg()
    test_u_gd_00()
    test_disconnect()

