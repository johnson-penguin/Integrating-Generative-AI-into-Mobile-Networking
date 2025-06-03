test_params = {
    "Num_Threads_PUSCH": {
        "original": 'Num_Threads_PUSCH = 8;',
        "variants": [
            # ❌ Type errors
            'Num_Threads_PUSCH = asdasfsad;',          # Undefined variable or keyword
            'Num_Threads_PUSCH = "string";',           # Quoted string instead of number
            'Num_Threads_PUSCH = true;',               # Boolean value
            'Num_Threads_PUSCH = 0xZZZZ;',             # Invalid hex format
            'Num_Threads_PUSCH = [8];',                # Array instead of scalar
            'Num_Threads_PUSCH = {};',                 # Object format

            # ❌ Syntax errors
            'Num_Threads_PUSCH = ;',                   # Missing value
            'Num_Threads_PUSCH 8;',                    # Missing '='
            'Num_Threads_PUSCH = 8',                   # Missing semicolon
            'Num_Threads_PUSCH = "8;',                 # Missing closing quote

            # ❌ Logic/Range errors
            'Num_Threads_PUSCH = -1;',                 # Negative thread count
            'Num_Threads_PUSCH = 0;',                  # Zero threads
            'Num_Threads_PUSCH = 999999999;',          # Excessively large number
            'Num_Threads_PUSCH = 1.5;',                # Non-integer value
        ]
    },
    "amf_ip_address": {
        "original": 'amf_ip_address = ({ ipv4 = "192.168.8.21" });',
        "variants": [
            # ❌ Syntax errors
            'amf_ip_address = amf_ip_address = ({ ipv4 = 1.2.3.4 });',  # Duplicate assignment, missing quotes
            'amf_ip_address = ({ ipv4 = "1.2.3.4" })',                  # Missing semicolon
            'amf_ip_address = ({ ipv4 = 192.168.8.21 });',              # Missing quotes around IP
            'amf_ip_address = ({ ipv4 = "192.168.8.21" }',              # Missing closing parenthesis
            'amf_ip_address = ({ ipv4: "192.168.8.21" });',             # Invalid key delimiter (colon instead of =)

            # ❌ Type errors
            'amf_ip_address = 1234;',                                   # Integer instead of object
            'amf_ip_address = true;',                                   # Boolean
            'amf_ip_address = [ "192.168.8.21" ];',                     # Array instead of object

            # ❌ Garbage / invalid strings
            'amf_ip_address = "";',                                     # Empty string
            'amf_ip_address = "sserdda_pi_fma";',                       # Reversed nonsense string
            'amf_ip_address = "@#$%^&*";',                              # Special characters
            'amf_ip_address = "192.168.8.21";',                         # Valid IP, but wrong format (should be inside object)

            # ❌ Semantically invalid IP addresses
            'amf_ip_address = ({ ipv4 = "300.400.500.600" });',         # Octets out of range
            'amf_ip_address = ({ ipv4 = "abcd.ef.gh.ij" });',           # Alphabetic
            'amf_ip_address = ({ ipv4 = "" });',                        # Empty IP value

            # ❌ Wrong structure
            'amf_ip_address = ();',                                     # Empty object
            'amf_ip_address = {};',                                     # Wrong bracket type
            'amf_ip_address = ({ });',                                  # Object with no keys

            # ✅ Valid alternatives
            'amf_ip_address = ({ ipv4 = "10.0.0.1" });',                # Different valid IP
            'amf_ip_address = ({ ipv4 = "127.0.0.1" });'                # Loopback address
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
            # ❌ Unsupported algorithm
            'ciphering_algorithms = ( "nea4" );',               # Unsupported value

            # ❌ Special characters or nonsensical strings
            'ciphering_algorithms = "@#$%^&*";',                # Garbage string without parentheses
            'ciphering_algorithms = "smhtirogla_gnirehpic";',   # Reversed nonsense string
            'ciphering_algorithms = "";',                       # Empty string
            'ciphering_algorithms = "nea1";',                   # Missing parentheses

            # ❌ Wrong type
            'ciphering_algorithms = 1234;',                     # Integer instead of string list
            'ciphering_algorithms = [ "nea1" ];',               # Array instead of tuple-like syntax
            'ciphering_algorithms = true;',                     # Boolean

            # ❌ Syntax errors
            'ciphering_algorithms = ( nea4 );',                 # Missing quotes
            'ciphering_algorithms = ( "nea1", );',              # Trailing comma
            'ciphering_algorithms = ( "nea1", "nea2", );',      # Extra trailing comma

            # ❌ Completely broken formats
            'ciphering_algorithms = ciphering_algorithms = ( "nea8" );',  # Duplicate assignment
            'ciphering_algorithms = ( "nea1", 1234 );',         # Mixed types inside list
        ]
    },

    "integrity_algorithms": {
        "original": 'integrity_algorithms = ( "nia2", "nia0" );',
        "variants": [
            # ❌ Duplicate assignment
            'integrity_algorithms = integrity_algorithms = ( nia8 );',    # No quotes, invalid syntax

            # ❌ Unsupported or malformed values
            'integrity_algorithms = ( "nia8" );',             # Unsupported algorithm
            'integrity_algorithms = ( "nia2", "nia8" );',     # One valid, one invalid
            'integrity_algorithms = ( "nia2", "" );',         # Empty item

            # ❌ Garbage / nonsense
            'integrity_algorithms = "@#$%^&*";',              # Special characters
            'integrity_algorithms = "smhtirogla_ytirgetni";', # Reversed junk string
            'integrity_algorithms = "";',                     # Empty string only

            # ❌ Wrong types
            'integrity_algorithms = 1234;',                   # Integer instead of list
            'integrity_algorithms = [ "nia1" ];',             # Array brackets
            'integrity_algorithms = true;',                   # Boolean

            # ❌ Syntax issues
            'integrity_algorithms = ( "nia1", "nia2", );',    # Trailing comma
            'integrity_algorithms = ( "nia1", 1234 );',       # Mixed types
            'integrity_algorithms = ( nia2 );',               # Missing quotes
        ]
    },

    "Active_gNBs": {
        "original": 'Active_gNBs = ( "gNB-Eurecom-CU");',
        "variants": [
            # ❌ Invalid type
            'Active_gNBs = 1234;',                          # Integer instead of string or list
            'Active_gNBs = true;',                          # Boolean
            'Active_gNBs = [ "gNB-Eurecom-CU" ];',          # Array with square brackets

            # ❌ Garbage / nonsense values
            'Active_gNBs = "@#$%^&*";',                     # Special characters
            'Active_gNBs = "sBNg_evitcA";',                 # Reversed nonsense
            'Active_gNBs = "";',                            # Empty string

            # ❌ Syntax errors
            'Active_gNBs = Active_gNBs = ( gNB-Eurecom-asdasASDA);',  # Duplicate assignment, missing quotes
            'Active_gNBs = ( "gNB-Eurecom-CU" )',           # Missing semicolon
            'Active_gNBs = ( gNB-Eurecom-CU );',            # Unquoted value
            'Active_gNBs = ( "gNB-1", );',                  # Trailing comma
            'Active_gNBs = ( "gNB-1", 1234 );',             # Mixed value types

            # ❌ Unknown or malformed values
            'Active_gNBs = ( "gNB-Eurecom-asdasASDA");',    # Random gNB name
            'Active_gNBs = ( "" );',                        # Empty element in list
            'Active_gNBs = ( );',                           # Empty parentheses
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
            # ❌ Nonsensical or garbage strings
            'local_s_if_name = "eman_fi_s_lacol";',             # Reversed nonsense string
            'local_s_if_name = "@#$%^&*";',                     # Special characters
            'local_s_if_name = "";',                            # Empty string

            # ❌ Syntax errors
            'local_s_if_name = local_s_if_name = eth0;',        # Duplicate assignment, unquoted value
            'local_s_if_name = eth0;',                          # Unquoted value
            'local_s_if_name = "lo"',                           # Missing semicolon
            'local_s_if_name = "eth0;',                         # Missing closing quote
            'local_s_if_name = ;',                              # Missing value

            # ❌ Type errors
            'local_s_if_name = 1234;',                          # Integer instead of string
            'local_s_if_name = true;',                          # Boolean value
            'local_s_if_name = [ "eth0" ];',                    # Array format
            'local_s_if_name = {};',                            # Object format

            # ❌ Invalid interface values (semantically invalid)
            'local_s_if_name = "loopback";',                    # Not a valid Linux interface
            'local_s_if_name = "invalid_iface_999";',           # Invalid naming format
            'local_s_if_name = " ";'                            # Whitespace-only string
        ]
    },

    "local_s_address": {
        "original": 'local_s_address = "127.0.0.5";',
        "variants": [
            # ❌ Empty or missing value
            'local_s_address = "";',                      # Empty string
            'local_s_address = ;',                        # Missing value

            # ❌ Syntax errors
            'local_s_address = local_s_address = 192.168.10.1;',  # Duplicate assignment without quotes
            'local_s_address = "127.0.0.5"',              # Missing semicolon
            'local_s_address = "192.168.10.1"',           # Missing semicolon
            'local_s_address = "192.168.10.1;',           # Missing closing quote

            # ❌ Invalid types
            'local_s_address = 1234;',                    # Integer instead of string
            'local_s_address = true;',                    # Boolean instead of string
            'local_s_address = [ "127.0.0.1" ];',         # Array instead of string

            # ❌ Nonsensical strings
            'local_s_address = "sserdda_s_lacol";',       # Reversed nonsense string
            'local_s_address = "@#$%^&*";',               # Special characters

            # ❌ Semantically invalid IPs
            'local_s_address = "127.000.000.256";',       # Octet out of range
            'local_s_address = "192.168.300.1";',         # Octet > 255

            # ❌ Valid syntax, but incorrect semantics
            'local_s_address = "localhost";',             # Not an IP address
            'local_s_address = "abc.def.ghi.jkl";',       # Alphabetic fake IP
            'local_s_address = "....";',                  # Dots only

            # ✅ Valid alternative
            'local_s_address = "192.168.10.1";'           # Correct syntax and valid IP
        ]
    },
    "local_s_portc": {
        "original": 'local_s_portc  = 501;',
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
        "original": 'local_s_portd  = 2152;',
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
        "original": 'GNB_IPV4_ADDRESS_FOR_NG_AMF              = "192.168.8.43";',
        "variants": [
            'GNB_IPV4_ADDRESS_FOR_NG_AMF = GNB_IPV4_ADDRESS_FOR_NG_AMF= 10.0.0.1;',
            'GNB_IPV4_ADDRESS_FOR_NG_AMF = "FMA_GN_ROF_SSERDDA_4VPI_BNG";',
            'GNB_IPV4_ADDRESS_FOR_NG_AMF = 1234;',
            'GNB_IPV4_ADDRESS_FOR_NG_AMF = "10.0.0.1";',
            'GNB_IPV4_ADDRESS_FOR_NG_AMF = "";',
            'GNB_IPV4_ADDRESS_FOR_NG_AMF = "@#$%^&*";',
        ]
    },
    "GNB_IPV4_ADDRESS_FOR_NGU": {
        "original": 'GNB_IPV4_ADDRESS_FOR_NGU                 = "192.168.8.43";',
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
        "original": 'GNB_PORT_FOR_S1U                         = 2152;',
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
        "original": 'SCTP_INSTREAMS  = 2;',
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
