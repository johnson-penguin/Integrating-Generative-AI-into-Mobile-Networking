test_params = {
    "Num_Threads_PUSCH": (
        'Num_Threads_PUSCH = 8;',
        'Num_Threads_PUSCH = asdasfsad;'
    ),
    "amf_ip_address": (
        'amf_ip_address = ({ ipv4 = "192.168.8.00" });',
        'amf_ip_address = ({ ipv4 = "1.2.3.4" });'
    ),
    "remote_s_address": (
        'remote_s_address = "127.0.0.3";',
        'remote_s_address = "10.10.10.10";'
    ),
    "ciphering_algorithms": (
        'ciphering_algorithms = ( "nea0" );',
        'ciphering_algorithms = ( "nea4" );'
    ),
    "integrity_algorithms": (
        'integrity_algorithms = ( "nia2", "nia0" );',
        'integrity_algorithms = ( "nia8" );'
    ),
    "Active_gNBs": (
        'Active_gNBs = ( "gNB-Eurecom-CU");',
        'Active_gNBs = ( "gNB-Eurecom-asdasASDA");'
    ),
    "gNB_name": (
        'gNB_name  =  "gNB-Eurecom-CU";',
        'gNB_name  =  "gNB-Eurecom-CASDASDASDASDAS12312U";'
    ),
    "gNB_ID": (
        'gNB_ID = 0xe00;',
        'gNB_ID = 0xFFFFFFFFF;'
    ),
    "local_s_if_name": (
        'local_s_if_name = "lo";',
        'local_s_if_name = "eth0";'
    ),
    "local_s_address": (
        'local_s_address = "127.0.0.5";',
        'local_s_address = "192.168.10.1";'
    ),
    "remote_s_address": (
        'remote_s_address = "127.0.0.3";',
        'remote_s_address = "192.168.10.2";'
    ),
    "local_s_portc": (
        'local_s_portc = 501;',
        'local_s_portc = 550;'
    ),
    "local_s_portd": (
        'local_s_portd = 2152;',
        'local_s_portd = 2210;'
    ),
    "remote_s_portc": (
        'remote_s_portc = 500;',
        'remote_s_portc = 540;'
    ),
    "remote_s_portd": (
        'remote_s_portd = 2152;',
        'remote_s_portd = 2222;'
    ),
    "GNB_IPV4_ADDRESS_FOR_NG_AMF": (
        'GNB_IPV4_ADDRESS_FOR_NG_AMF = "192.168.8.43";',
        'GNB_IPV4_ADDRESS_FOR_NG_AMF = "10.0.0.1";'
    ),
    "GNB_IPV4_ADDRESS_FOR_NGU": (
        'GNB_IPV4_ADDRESS_FOR_NGU = "192.168.8.43";',
        'GNB_IPV4_ADDRESS_FOR_NGU = "10.0.0.2";'
    ),
    "GNB_PORT_FOR_S1U": (
        'GNB_PORT_FOR_S1U = 2152;',
        'GNB_PORT_FOR_S1U = 2160;'
    ),
     "SCTP_INSTREAMS": (
        'SCTP_INSTREAMS = 2;',
        'SCTP_INSTREAMS = 4;'
    ),
    "SCTP_OUTSTREAMS": (
        'SCTP_OUTSTREAMS = 2;',
        'SCTP_OUTSTREAMS = 4;'
    ),
    "tr_s_preference": (
        'tr_s_preference = "f1";',
        'tr_s_preference = "e1";'
    ),
    "nr_cellid": (
        'nr_cellid = 1;',
        'nr_cellid = 65535;'
    ),
    "plmn_list": (
        'plmn_list = ({ mcc = 001; mnc = 01; mnc_length = 2; snssaiList = ( { sst = 1;}); });',
        'plmn_list = ({ mcc = 208; mnc = 93; mnc_length = 2; snssaiList = ( { sst = 1; }); });'
    )
    
}