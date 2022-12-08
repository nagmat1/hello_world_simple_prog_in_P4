from netaddr import IPAddress

p4 = bfrt.simple_l3.pipe

# This function can clear all the tables and later on other fixed objects
# once bfrt support is added.
def clear_all(verbose=True, batching=True):
    global p4
    global bfrt

    # The order is important. We do want to clear from the top, i.e.
    # delete objects that use other objects, e.g. table entries use
    # selector groups and selector groups use action profile members

    for table_types in (['MATCH_DIRECT', 'MATCH_INDIRECT_SELECTOR'],
                        ['SELECTOR'],
                        ['ACTION_PROFILE']):
        for table in p4.info(return_info=True, print_info=False):
            if table['type'] in table_types:
                if verbose:
                    print("Clearing table {:<40} ... ".
                          format(table['full_name']), end='', flush=True)
                table['node'].clear(batch=batching)
                if verbose:
                    print('Done')

#clear_all(verbose=True)

dp = bfrt.port.port_hdl_info.get(CONN_ID=4, CHNL_ID = 0, print_ents=False).data[b'$DEV_PORT']
bfrt.port.port.add(DEV_PORT=dp, SPEED="BF_SPEED_10G", FEC="BF_FEC_TYP_NONE", AUTO_NEGOTIATION ="PM_AN_FORCE_DISABLE", PORT_ENABLE =True)
dp = bfrt.port.port_hdl_info.get(CONN_ID=20, CHNL_ID = 0, print_ents=False).data[b'$DEV_PORT']
bfrt.port.port.add(DEV_PORT=dp, SPEED="BF_SPEED_40G", FEC="BF_FEC_TYP_NONE", AUTO_NEGOTIATION ="PM_AN_FORCE_DISABLE", PORT_ENABLE =True)
dp = bfrt.port.port_hdl_info.get(CONN_ID=13, CHNL_ID = 0, print_ents=False).data[b'$DEV_PORT']
bfrt.port.port.add(DEV_PORT=dp, SPEED="BF_SPEED_40G", FEC="BF_FEC_TYP_NONE", AUTO_NEGOTIATION ="PM_AN_FORCE_DISABLE", PORT_ENABLE =True)



for qsfp_cage in [33]:
    for lane in range(0,4):
        dp = bfrt.port.port_hdl_info.get(CONN_ID=qsfp_cage, CHNL_ID = lane,
                print_ents=False).data[b'$DEV_PORT']
        bfrt.port.port.add(DEV_PORT=dp, SPEED="BF_SPEED_10G", FEC="BF_FEC_TYP_NONE", AUTO_NEGOTIATION ="PM_AN_FORCE_ENABLE", PORT_ENABLE =True)


ipv4_host = p4.Ingress.ipv4_host
ipv4_host.add_with_send(dst_addr=IPAddress('192.168.1.1'),   port=284)
ipv4_host.add_with_send(dst_addr=IPAddress('192.168.1.2'),   port=24)
ipv4_host.add_with_send(dst_addr=IPAddress('192.168.1.3'),   port=28)
ipv4_host.add_with_send(dst_addr=IPAddress('192.168.1.254'), port=64)
ipv4_host.add_with_drop(dst_addr=IPAddress('192.168.1.4'))


ipv4_lpm =  p4.Ingress.ipv4_lpm
ipv4_lpm.add_with_send(
    dst_addr=IPAddress('192.168.1.0'), dst_addr_p_length=24, port=1)
ipv4_lpm.add_with_drop(
    dst_addr=IPAddress('192.168.0.0'), dst_addr_p_length=16)
ipv4_lpm.add_with_send(
    dst_addr=IPAddress('0.0.0.0'),     dst_addr_p_length=0,  port=64)

bfrt.complete_operations()

# Final programming
print("""
******************* PROGAMMING RESULTS *****************
""")
print ("Table ipv4_host:")
ipv4_host.dump(table=True)
print ("Table ipv4_lpm:")
ipv4_lpm.dump(table=True)


