test_params = {
    "Num_Threads_PUSCH": {
        "original": 'Num_Threads_PUSCH = 8;',
        "variants": [
            'Num_Threads_PUSCH = asdasfsad;',
            'Num_Threads_PUSCH = "string";',
            'Num_Threads_PUSCH = 999999999;',
            'Num_Threads_PUSCH = ;',
            'Num_Threads_PUSCH = 0xZZZZ;',
            'Num_Threads_PUSCH = -1;',
        ]
    },
    "amf_ip_address": {
        "original": 'amf_ip_address = ({ ipv4 = "192.168.8.00" });',
        "variants": [
            'amf_ip_address = amf_ip_address = ({ ipv4 = 1.2.3.4 });',
            'amf_ip_address = "";',
            'amf_ip_address = "sserdda_pi_fma";',
            'amf_ip_address = "@#$%^&*";',
            'amf_ip_address = ({ ipv4 = "1.2.3.4" });',
            'amf_ip_address = 1234;',
        ]
    },
    "remote_s_address": {
        "original": 'remote_s_address = "127.0.0.3";',
        "variants": [
            'remote_s_address = remote_s_address = 192.168.10.2;',
            'remote_s_address = 1234;',
            'remote_s_address = "@#$%^&*";',
            'remote_s_address = "192.168.10.2";',
            'remote_s_address = "";',
            'remote_s_address = "sserdda_s_etomer";',
        ]
    },
    "ciphering_algorithms": {
        "original": 'ciphering_algorithms = ( "nea0" );',
        "variants": [
            'ciphering_algorithms = ( "nea4" );',
            'ciphering_algorithms = "@#$%^&*";',
            'ciphering_algorithms = "smhtirogla_gnirehpic";',
            'ciphering_algorithms = "";',
            'ciphering_algorithms = 1234;',
            'ciphering_algorithms = ciphering_algorithms = ( nea4 );',
        ]
    },
    "integrity_algorithms": {
        "original": 'integrity_algorithms = ( "nia2", "nia0" );',
        "variants": [
            'integrity_algorithms = integrity_algorithms = ( nia8 );',
            'integrity_algorithms = ( "nia8" );',
            'integrity_algorithms = "@#$%^&*";',
            'integrity_algorithms = "smhtirogla_ytirgetni";',
            'integrity_algorithms = "";',
            'integrity_algorithms = 1234;',
        ]
    },
    "Active_gNBs": {
        "original": 'Active_gNBs = ( "gNB-Eurecom-CU");',
        "variants": [
            'Active_gNBs = 1234;',
            'Active_gNBs = "@#$%^&*";',
            'Active_gNBs = Active_gNBs = ( gNB-Eurecom-asdasASDA);',
            'Active_gNBs = "sBNg_evitcA";',
            'Active_gNBs = "";',
            'Active_gNBs = ( "gNB-Eurecom-asdasASDA");',
        ]
    },
    "gNB_name": {
        "original": 'gNB_name  =  "gNB-Eurecom-CU";',
        "variants": [
            'gNB_name = "@#$%^&*";',
            'gNB_name = gNB_name  =  gNB-Eurecom-CASDASDASDASDAS12312U;',
            'gNB_name = 1234;',
            'gNB_name = "eman_BNg";',
            'gNB_name = "";',
            'gNB_name  =  "gNB-Eurecom-CASDASDASDASDAS12312U";',
        ]
    },
    "gNB_ID": {
        "original": 'gNB_ID = 0xe00;',
        "variants": [
            'gNB_ID = 999999999;',
            'gNB_ID = -1;',
            'gNB_ID = "string";',
            'gNB_ID = ;',
            'gNB_ID = 0xFFFFFFFFF;',
            'gNB_ID = 0xZZZZ;',
        ]
    },
    "local_s_if_name": {
        "original": 'local_s_if_name = "lo";',
        "variants": [
            'local_s_if_name = "eth0";',
            'local_s_if_name = "eman_fi_s_lacol";',
            'local_s_if_name = "@#$%^&*";',
            'local_s_if_name = "";',
            'local_s_if_name = local_s_if_name = eth0;',
            'local_s_if_name = 1234;',
        ]
    },
    "local_s_address": {
        "original": 'local_s_address = "127.0.0.5";',
        "variants": [
            'local_s_address = "";',
            'local_s_address = local_s_address = 192.168.10.1;',
            'local_s_address = "sserdda_s_lacol";',
            'local_s_address = "@#$%^&*";',
            'local_s_address = "192.168.10.1";',
            'local_s_address = 1234;',
        ]
    },
    "local_s_portc": {
        "original": 'local_s_portc = 501;',
        "variants": [
            'local_s_portc = 0xZZZZ;',
            'local_s_portc = "string";',
            'local_s_portc = -1;',
            'local_s_portc = 999999999;',
            'local_s_portc = ;',
            'local_s_portc = 550;',
        ]
    },
    "local_s_portd": {
        "original": 'local_s_portd = 2152;',
        "variants": [
            'local_s_portd = 999999999;',
            'local_s_portd = 2210;',
            'local_s_portd = -1;',
            'local_s_portd = "string";',
            'local_s_portd = 0xZZZZ;',
            'local_s_portd = ;',
        ]
    },
    "remote_s_portc": {
        "original": 'remote_s_portc = 500;',
        "variants": [
            'remote_s_portc = 540;',
            'remote_s_portc = ;',
            'remote_s_portc = -1;',
            'remote_s_portc = 0xZZZZ;',
            'remote_s_portc = 999999999;',
            'remote_s_portc = "string";',
        ]
    },
    "remote_s_portd": {
        "original": 'remote_s_portd = 2152;',
        "variants": [
            'remote_s_portd = -1;',
            'remote_s_portd = ;',
            'remote_s_portd = 2222;',
            'remote_s_portd = 999999999;',
            'remote_s_portd = "string";',
            'remote_s_portd = 0xZZZZ;',
        ]
    },
    "GNB_IPV4_ADDRESS_FOR_NG_AMF": {
        "original": 'GNB_IPV4_ADDRESS_FOR_NG_AMF = "192.168.8.43";',
        "variants": [
            'GNB_IPV4_ADDRESS_FOR_NG_AMF = GNB_IPV4_ADDRESS_FOR_NG_AMF = 10.0.0.1;',
            'GNB_IPV4_ADDRESS_FOR_NG_AMF = "FMA_GN_ROF_SSERDDA_4VPI_BNG";',
            'GNB_IPV4_ADDRESS_FOR_NG_AMF = 1234;',
            'GNB_IPV4_ADDRESS_FOR_NG_AMF = "10.0.0.1";',
            'GNB_IPV4_ADDRESS_FOR_NG_AMF = "";',
            'GNB_IPV4_ADDRESS_FOR_NG_AMF = "@#$%^&*";',
        ]
    },
    "GNB_IPV4_ADDRESS_FOR_NGU": {
        "original": 'GNB_IPV4_ADDRESS_FOR_NGU = "192.168.8.43";',
        "variants": [
            'GNB_IPV4_ADDRESS_FOR_NGU = "@#$%^&*";',
            'GNB_IPV4_ADDRESS_FOR_NGU = "";',
            'GNB_IPV4_ADDRESS_FOR_NGU = 1234;',
            'GNB_IPV4_ADDRESS_FOR_NGU = "10.0.0.2";',
            'GNB_IPV4_ADDRESS_FOR_NGU = "UGN_ROF_SSERDDA_4VPI_BNG";',
            'GNB_IPV4_ADDRESS_FOR_NGU = GNB_IPV4_ADDRESS_FOR_NGU = 10.0.0.2;',
        ]
    },
    "GNB_PORT_FOR_S1U": {
        "original": 'GNB_PORT_FOR_S1U = 2152;',
        "variants": [
            'GNB_PORT_FOR_S1U = ;',
            'GNB_PORT_FOR_S1U = 999999999;',
            'GNB_PORT_FOR_S1U = "string";',
            'GNB_PORT_FOR_S1U = -1;',
            'GNB_PORT_FOR_S1U = 2160;',
            'GNB_PORT_FOR_S1U = 0xZZZZ;',
        ]
    },
    "SCTP_INSTREAMS": {
        "original": 'SCTP_INSTREAMS = 2;',
        "variants": [
            'SCTP_INSTREAMS = 4;',
            'SCTP_INSTREAMS = "string";',
            'SCTP_INSTREAMS = ;',
            'SCTP_INSTREAMS = -1;',
            'SCTP_INSTREAMS = 999999999;',
            'SCTP_INSTREAMS = 0xZZZZ;',
        ]
    },
    "SCTP_OUTSTREAMS": {
        "original": 'SCTP_OUTSTREAMS = 2;',
        "variants": [
            'SCTP_OUTSTREAMS = -1;',
            'SCTP_OUTSTREAMS = "string";',
            'SCTP_OUTSTREAMS = ;',
            'SCTP_OUTSTREAMS = 0xZZZZ;',
            'SCTP_OUTSTREAMS = 999999999;',
            'SCTP_OUTSTREAMS = 4;',
        ]
    },
    "tr_s_preference": {
        "original": 'tr_s_preference = "f1";',
        "variants": [
            'tr_s_preference = tr_s_preference = e1;',
            'tr_s_preference = "ecnereferp_s_rt";',
            'tr_s_preference = "@#$%^&*";',
            'tr_s_preference = "e1";',
            'tr_s_preference = 1234;',
            'tr_s_preference = "";',
        ]
    },
    "nr_cellid": {
        "original": 'nr_cellid = 1;',
        "variants": [
            'nr_cellid = 0xZZZZ;',
            'nr_cellid = -1;',
            'nr_cellid = 65535;',
            'nr_cellid = ;',
            'nr_cellid = 999999999;',
            'nr_cellid = "string";',
        ]
    },
    "plmn_list": {
        "original": 'plmn_list = ({ mcc = 001; mnc = 01; mnc_length = 2; snssaiList = ( { sst = 1;}); });',
        "variants": [
            'plmn_list = -1;',
            'plmn_list = "string";',
            'plmn_list = 0xZZZZ;',
            'plmn_list = 999999999;',
            'plmn_list = ({ mcc = 208; mnc = 93; mnc_length = 2; snssaiList = ( { sst = 1; }); });',
            'plmn_list = ;',
        ]
    },
}
