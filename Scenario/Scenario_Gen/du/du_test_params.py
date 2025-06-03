# 測試參數（param_name: (原始字串, 要替換的新字串)）
test_params = {
    "Active_gNBs": {
    "original": 'Active_gNBs = ( "gNB-Eurecom-DU");',
    "variants": [
        'Active_gNBs = ( "gNB-Test-DU");',
        'Active_gNBs = "";',
        'Active_gNBs = ( "1234");',
        'Active_gNBs = "@#$%^&*";',
        'Active_gNBs = ( "DU-Mock-Test");',
        'Active_gNBs = ( );'
    ]
    },
    "Asn1_verbosity": {
        "original": 'Asn1_verbosity = "none";',
        "variants": [
            'Asn1_verbosity = "info";',
            'Asn1_verbosity = "";',
            'Asn1_verbosity = "debug";',
            'Asn1_verbosity = 1234;',
            'Asn1_verbosity = "@#$%^&*";',
            'Asn1_verbosity = none;'
        ]
    },
    "gNB_ID": {
    "original": 'gNB_ID = 0xe00;',
    "variants": [
        'gNB_ID = 0x1234;',
        'gNB_ID = "";',
        'gNB_ID = -1;',
        'gNB_ID = 12345678901234567890;',
        'gNB_ID = "@#$%^&*";',
        'gNB_ID = gNB_ID = 0xe00;'
        ]
    },
    "gNB_DU_ID": {
        "original": 'gNB_DU_ID = 0xe00;',
        "variants": [
            'gNB_DU_ID = 0x5678;',
            'gNB_DU_ID = "";',
            'gNB_DU_ID = 999999;',
            'gNB_DU_ID = "@invalid";',
            'gNB_DU_ID = -42;',
            'gNB_DU_ID = gNB_DU_ID = 0xe00;'
        ]
    },
    "gNB_name": {
        "original": 'gNB_name  =  "gNB-Eurecom-DU";',
        "variants": [
            'gNB_name  =  "gNB-Test-DU";',
            'gNB_name  =  "";',
            'gNB_name  =  "@#$%^&*";',
            'gNB_name  =  1234;',
            'gNB_name  =  gNB_name;',
            'gNB_name  =  "invalid-name";'
        ]
    },
    "tracking_area_code": {
        "original": 'tracking_area_code  =  1;',
        "variants": [
            'tracking_area_code  =  42;',
            'tracking_area_code  =  "";',
            'tracking_area_code  =  -1;',
            'tracking_area_code  =  "@@";',
            'tracking_area_code  =  65536;',
            'tracking_area_code  = tracking_area_code = 1;'
        ]
    },
    "plmn_list": {
        "original": 'plmn_list = ({ mcc = 001; mnc = 01; mnc_length = 2; snssaiList = ( { sst = 1;}); });',
        "variants": [
            'plmn_list = ({ mcc = 208; mnc = 93; mnc_length = 2; snssaiList = ( { sst = 1; }); });',
            'plmn_list = "";',
            'plmn_list = ({ mcc = "abc"; mnc = "xx"; });',
            'plmn_list = malformed_entry;',
            'plmn_list = ({ mcc = 999; mnc = 999; });',
            'plmn_list = @#*&!@#;'
        ]
    },
    "nr_cellid": {
        "original": 'nr_cellid = 1;',
        "variants": [
            'nr_cellid = 1001;',
            'nr_cellid = "";',
            'nr_cellid = -10;',
            'nr_cellid = "cell";',
            'nr_cellid = 0xFFFFFFFF;',
            'nr_cellid = nr_cellid;'
        ]
    },
    "min_rxtxtime": {
        "original": 'min_rxtxtime                                              = 6;',
        "variants": [
            'min_rxtxtime = 2;',
            'min_rxtxtime = "";',
            'min_rxtxtime = -5;',
            'min_rxtxtime = "time";',
            'min_rxtxtime = 10000;',
            'min_rxtxtime = @@@;'
        ]
    },
    "force_256qam_off": {
        "original": 'force_256qam_off = 1;',
        "variants": [
            'force_256qam_off = 0;',
            'force_256qam_off = 2;',
            'force_256qam_off = "";',
            'force_256qam_off = true;',
            'force_256qam_off = -1;',
            'force_256qam_off = @#$;'
        ]
    },
    "physCellId": {
        "original": 'physCellId                                                    = 0;',
        "variants": [
            'physCellId = 100;',
            'physCellId = "";',
            'physCellId = -1;',
            'physCellId = "id";',
            'physCellId = 0xFFFF;',
            'physCellId = physCellId;'
        ]
    },
    "absoluteFrequencySSB": {
        "original": 'absoluteFrequencySSB                                          = 641280;',
        "variants": [
            'absoluteFrequencySSB = 640000;',
            'absoluteFrequencySSB = "";',
            'absoluteFrequencySSB = -100;',
            'absoluteFrequencySSB = "freq";',
            'absoluteFrequencySSB = 999999999;',
            'absoluteFrequencySSB = @@@;'
        ]
    },
    "dl_frequencyBand": {
        "original": 'dl_frequencyBand                                                 = 78;',
        "variants": [
            'dl_frequencyBand = 77;',
            'dl_frequencyBand = "";',
            'dl_frequencyBand = -1;',
            'dl_frequencyBand = "band";',
            'dl_frequencyBand = 999;',
            'dl_frequencyBand = @@@;'
        ]
    },
    "dl_absoluteFrequencyPointA": {
    "original": 'dl_absoluteFrequencyPointA                                       = 640008;',
    "variants": [
        'dl_absoluteFrequencyPointA = 642000;',
        'dl_absoluteFrequencyPointA = "";',
        'dl_absoluteFrequencyPointA = -100;',
        'dl_absoluteFrequencyPointA = "freq";',
        'dl_absoluteFrequencyPointA = 999999999;',
        'dl_absoluteFrequencyPointA = ???;'
    ]
    },
    "dl_offstToCarrier": {
        "original": 'dl_offstToCarrier                                              = 0;',
        "variants": [
            'dl_offstToCarrier = 10;',
            'dl_offstToCarrier = "";',
            'dl_offstToCarrier = -1;',
            'dl_offstToCarrier = "offset";',
            'dl_offstToCarrier = 9999;',
            'dl_offstToCarrier = @@@;'
        ]
    },
    "dl_subcarrierSpacing": {
        "original": 'dl_subcarrierSpacing                                           = 1;',
        "variants": [
            'dl_subcarrierSpacing = 2;',
            'dl_subcarrierSpacing = "";',
            'dl_subcarrierSpacing = -1;',
            'dl_subcarrierSpacing = "space";',
            'dl_subcarrierSpacing = 100;',
            'dl_subcarrierSpacing = #!$;'
        ]
    },
    "dl_carrierBandwidth": {
        "original": 'dl_carrierBandwidth                                            = 106;',
        "variants": [
            'dl_carrierBandwidth = 100;',
            'dl_carrierBandwidth = "";',
            'dl_carrierBandwidth = -10;',
            'dl_carrierBandwidth = "wide";',
            'dl_carrierBandwidth = 100000;',
            'dl_carrierBandwidth = $$;'
        ]
    },
    "initialDLBWPlocationAndBandwidth": {
        "original": 'initialDLBWPlocationAndBandwidth                               = 28875;',
        "variants": [
            'initialDLBWPlocationAndBandwidth = 28000;',
            'initialDLBWPlocationAndBandwidth = "";',
            'initialDLBWPlocationAndBandwidth = -1;',
            'initialDLBWPlocationAndBandwidth = "value";',
            'initialDLBWPlocationAndBandwidth = 999999;',
            'initialDLBWPlocationAndBandwidth = @@;'
        ]
    },
    "initialDLBWPsubcarrierSpacing": {
        "original": 'initialDLBWPsubcarrierSpacing                                           = 1;',
        "variants": [
            'initialDLBWPsubcarrierSpacing = 0;',
            'initialDLBWPsubcarrierSpacing = "";',
            'initialDLBWPsubcarrierSpacing = "spacing";',
            'initialDLBWPsubcarrierSpacing = -2;',
            'initialDLBWPsubcarrierSpacing = 5;',
            'initialDLBWPsubcarrierSpacing = #@;'
        ]
    },
    "initialDLBWPcontrolResourceSetZero": {
        "original": 'initialDLBWPcontrolResourceSetZero                              = 12;',
        "variants": [
            'initialDLBWPcontrolResourceSetZero = 13;',
            'initialDLBWPcontrolResourceSetZero = "";',
            'initialDLBWPcontrolResourceSetZero = -1;',
            'initialDLBWPcontrolResourceSetZero = "zero";',
            'initialDLBWPcontrolResourceSetZero = 100;',
            'initialDLBWPcontrolResourceSetZero = $$;'
        ]
    },
    "initialDLBWPsearchSpaceZero": {
        "original": 'initialDLBWPsearchSpaceZero                                             = 0;',
        "variants": [
            'initialDLBWPsearchSpaceZero = 1;',
            'initialDLBWPsearchSpaceZero = "";',
            'initialDLBWPsearchSpaceZero = "ss";',
            'initialDLBWPsearchSpaceZero = -2;',
            'initialDLBWPsearchSpaceZero = 10;',
            'initialDLBWPsearchSpaceZero = %%@@;'
        ]
    },
    "ul_frequencyBand": {
        "original": 'ul_frequencyBand                                                 = 78;',
        "variants": [
            'ul_frequencyBand = 77;',
            'ul_frequencyBand = "";',
            'ul_frequencyBand = "uplink";',
            'ul_frequencyBand = -1;',
            'ul_frequencyBand = 999;',
            'ul_frequencyBand = @#;'
        ]
    },
    "ul_offstToCarrier": {
        "original": 'ul_offstToCarrier                                              = 0;',
        "variants": [
            'ul_offstToCarrier = 15;',
            'ul_offstToCarrier = "";',
            'ul_offstToCarrier = "offset";',
            'ul_offstToCarrier = -5;',
            'ul_offstToCarrier = 9999;',
            'ul_offstToCarrier = !!;'
        ]
    },
    "ul_subcarrierSpacing": {
        "original": 'ul_subcarrierSpacing                                           = 1;',
        "variants": [
            'ul_subcarrierSpacing = 0;',
            'ul_subcarrierSpacing = "";',
            'ul_subcarrierSpacing = -1;',
            'ul_subcarrierSpacing = "spacing";',
            'ul_subcarrierSpacing = 100;',
            'ul_subcarrierSpacing = #!;'
        ]
    },
    "ul_carrierBandwidth": {
        "original": 'ul_carrierBandwidth                                            = 106;',
        "variants": [
            'ul_carrierBandwidth = 50;',
            'ul_carrierBandwidth = "";',
            'ul_carrierBandwidth = -50;',
            'ul_carrierBandwidth = "bandwidth";',
            'ul_carrierBandwidth = 100000;',
            'ul_carrierBandwidth = @@@;'
        ]
    },
    "pMax": {
        "original": 'pMax                                                          = 20;',
        "variants": [
            'pMax = 23;',
            'pMax = "";',
            'pMax = -100;',
            'pMax = "max";',
            'pMax = 999;',
            'pMax = $$;'
        ]
    },
    "initialULBWPlocationAndBandwidth": {
        "original": 'initialULBWPlocationAndBandwidth                            = 28875;',
        "variants": [
            'initialULBWPlocationAndBandwidth = 28000;',
            'initialULBWPlocationAndBandwidth = "";',
            'initialULBWPlocationAndBandwidth = -1;',
            'initialULBWPlocationAndBandwidth = "ulbw";',
            'initialULBWPlocationAndBandwidth = 1000000;',
            'initialULBWPlocationAndBandwidth = ***;'
        ]
    },
    "initialULBWPsubcarrierSpacing": {
        "original": 'initialULBWPsubcarrierSpacing                                           = 1;',
        "variants": [
            'initialULBWPsubcarrierSpacing = 2;',
            'initialULBWPsubcarrierSpacing = "";',
            'initialULBWPsubcarrierSpacing = "spacing";',
            'initialULBWPsubcarrierSpacing = -5;',
            'initialULBWPsubcarrierSpacing = 20;',
            'initialULBWPsubcarrierSpacing = $@;'
        ]
    },
    "prach_ConfigurationIndex": {
        "original": 'prach_ConfigurationIndex                                  = 98;',
        "variants": [
            'prach_ConfigurationIndex = 100;',
            'prach_ConfigurationIndex = "";',
            'prach_ConfigurationIndex = "pci";',
            'prach_ConfigurationIndex = -10;',
            'prach_ConfigurationIndex = 999;',
            'prach_ConfigurationIndex = @#;'
        ]
    },
    "prach_msg1_FDM": {
        "original": 'prach_msg1_FDM                                            = 0;',
        "variants": [
            'prach_msg1_FDM = 1;',
            'prach_msg1_FDM = "";',
            'prach_msg1_FDM = "fdm";',
            'prach_msg1_FDM = -1;',
            'prach_msg1_FDM = 999;',
            'prach_msg1_FDM = $$;'
        ]
    },
    "prach_msg1_FrequencyStart": {
        "original": 'prach_msg1_FrequencyStart                                 = 0;',
        "variants": [
            'prach_msg1_FrequencyStart = 5;',
            'prach_msg1_FrequencyStart = "";',
            'prach_msg1_FrequencyStart = -1;',
            'prach_msg1_FrequencyStart = "start";',
            'prach_msg1_FrequencyStart = @#@#;'
        ]
    },
    "zeroCorrelationZoneConfig": {
        "original": 'zeroCorrelationZoneConfig                                 = 13;',
        "variants": [
            'zeroCorrelationZoneConfig = 10;',
            'zeroCorrelationZoneConfig = "";',
            'zeroCorrelationZoneConfig = -5;',
            'zeroCorrelationZoneConfig = "zone";',
            'zeroCorrelationZoneConfig = ***;'
        ]
    },
    "preambleReceivedTargetPower": {
        "original": 'preambleReceivedTargetPower                               = -96;',
        "variants": [
            'preambleReceivedTargetPower = -90;',
            'preambleReceivedTargetPower = "";',
            'preambleReceivedTargetPower = "power";',
            'preambleReceivedTargetPower = -999;',
            'preambleReceivedTargetPower = $$$;'
        ]
    },
    "preambleTransMax": {
        "original": 'preambleTransMax                                          = 6;',
        "variants": [
            'preambleTransMax = 10;',
            'preambleTransMax = "";',
            'preambleTransMax = -1;',
            'preambleTransMax = "max";',
            'preambleTransMax = @@@;'
        ]
    },
    "powerRampingStep": {
        "original": 'powerRampingStep                                            = 1;',
        "variants": [
            'powerRampingStep = 2;',
            'powerRampingStep = "";',
            'powerRampingStep = -10;',
            'powerRampingStep = "step";',
            'powerRampingStep = ***;'
        ]
    },
    "ra_ResponseWindow": {
        "original": 'ra_ResponseWindow                                           = 4;',
        "variants": [
            'ra_ResponseWindow = 8;',
            'ra_ResponseWindow = "";',
            'ra_ResponseWindow = -3;',
            'ra_ResponseWindow = "window";',
            'ra_ResponseWindow = 999;'
        ]
    },
    "ssb_perRACH_OccasionAndCB_PreamblesPerSSB_PR": {
        "original": 'ssb_perRACH_OccasionAndCB_PreamblesPerSSB_PR                = 4;',
        "variants": [
            'ssb_perRACH_OccasionAndCB_PreamblesPerSSB_PR = 2;',
            'ssb_perRACH_OccasionAndCB_PreamblesPerSSB_PR = "";',
            'ssb_perRACH_OccasionAndCB_PreamblesPerSSB_PR = -1;',
            'ssb_perRACH_OccasionAndCB_PreamblesPerSSB_PR = @@@;'
        ]
    },
    "ssb_perRACH_OccasionAndCB_PreamblesPerSSB": {
        "original": 'ssb_perRACH_OccasionAndCB_PreamblesPerSSB                   = 14;',
        "variants": [
            'ssb_perRACH_OccasionAndCB_PreamblesPerSSB = 8;',
            'ssb_perRACH_OccasionAndCB_PreamblesPerSSB = "";',
            'ssb_perRACH_OccasionAndCB_PreamblesPerSSB = -10;',
            'ssb_perRACH_OccasionAndCB_PreamblesPerSSB = "pream";'
        ]
    },
    "ra_ContentionResolutionTimer": {
        "original": 'ra_ContentionResolutionTimer                                = 7;',
        "variants": [
            'ra_ContentionResolutionTimer = 16;',
            'ra_ContentionResolutionTimer = "";',
            'ra_ContentionResolutionTimer = -3;',
            'ra_ContentionResolutionTimer = "timer";'
        ]
    },
    "rsrp_ThresholdSSB": {
        "original": 'rsrp_ThresholdSSB                                           = 19;',
        "variants": [
            'rsrp_ThresholdSSB = 25;',
            'rsrp_ThresholdSSB = "";',
            'rsrp_ThresholdSSB = -100;',
            'rsrp_ThresholdSSB = "rsrp";'
        ]
    },
    "prach_RootSequenceIndex_PR": {
        "original": 'prach_RootSequenceIndex_PR                                  = 2;',
        "variants": [
            'prach_RootSequenceIndex_PR = 0;',
            'prach_RootSequenceIndex_PR = "";',
            'prach_RootSequenceIndex_PR = -1;',
            'prach_RootSequenceIndex_PR = "root";'
        ]
    },
    "prach_RootSequenceIndex": {
        "original": 'prach_RootSequenceIndex                                     = 1;',
        "variants": [
            'prach_RootSequenceIndex = 22;',
            'prach_RootSequenceIndex = "";',
            'prach_RootSequenceIndex = -1;',
            'prach_RootSequenceIndex = "index";'
        ]
    },
    "msg1_SubcarrierSpacing": {
        "original": 'msg1_SubcarrierSpacing                                      = 1,',
        "variants": [
            'msg1_SubcarrierSpacing = 0,',
            'msg1_SubcarrierSpacing = "";',
            'msg1_SubcarrierSpacing = -1,',
            'msg1_SubcarrierSpacing = "spacing",'
        ]
    },
    "restrictedSetConfig": {
        "original": 'restrictedSetConfig                                         = 0,',
        "variants": [
            'restrictedSetConfig = 1,',
            'restrictedSetConfig = "";',
            'restrictedSetConfig = -1,',
            'restrictedSetConfig = "config",'
        ]
    },
    "msg3_DeltaPreamble": {
        "original": 'msg3_DeltaPreamble                                          = 1;',
        "variants": [
            'msg3_DeltaPreamble = 3;',
            'msg3_DeltaPreamble = "";',
            'msg3_DeltaPreamble = -1;',
            'msg3_DeltaPreamble = "delta";'
        ]
    },
    "p0_NominalWithGrant": {
        "original": 'p0_NominalWithGrant                                         =-90;',
        "variants": [
            'p0_NominalWithGrant =-80;',
            'p0_NominalWithGrant = "";',
            'p0_NominalWithGrant = -999;',
            'p0_NominalWithGrant = "p0";'
        ]
    },
    "pucchGroupHopping": {
        "original": 'pucchGroupHopping                                           = 0;',
        "variants": [
            'pucchGroupHopping = 1;',
            'pucchGroupHopping = "";',
            'pucchGroupHopping = -1;',
            'pucchGroupHopping = "hop";'
        ]
    },
    "hoppingId": {
        "original": 'hoppingId                                                   = 40;',
        "variants": [
            'hoppingId = 63;',
            'hoppingId = "";',
            'hoppingId = -1;',
            'hoppingId = "id";'
        ]
    },
    "p0_nominal": {
        "original": 'p0_nominal                                                  = -90;',
        "variants": [
            'p0_nominal = -80;',
            'p0_nominal = "";',
            'p0_nominal = "p0";',
            'p0_nominal = -999;',
            'p0_nominal = ???;'
        ]
    },
    "ssb_PositionsInBurst_Bitmap": {
        "original": 'ssb_PositionsInBurst_Bitmap                                   = 1;',
        "variants": [
            'ssb_PositionsInBurst_Bitmap = 0;',
            'ssb_PositionsInBurst_Bitmap = "";',
            'ssb_PositionsInBurst_Bitmap = -1;',
            'ssb_PositionsInBurst_Bitmap = "bitmap";'
        ]
    },
    "ssb_periodicityServingCell": {
        "original": 'ssb_periodicityServingCell                                    = 2;',
        "variants": [
            'ssb_periodicityServingCell = 1;',
            'ssb_periodicityServingCell = "";',
            'ssb_periodicityServingCell = -1;',
            'ssb_periodicityServingCell = "period";'
        ]
    },
    "dmrs_TypeA_Position": {
        "original": 'dmrs_TypeA_Position                                           = 0;',
        "variants": [
            'dmrs_TypeA_Position = 1;',
            'dmrs_TypeA_Position = "";',
            'dmrs_TypeA_Position = -1;',
            'dmrs_TypeA_Position = "type";'
        ]
    },
    "subcarrierSpacing": {
        "original": 'subcarrierSpacing                                             = 1;',
        "variants": [
            'subcarrierSpacing = 0;',
            'subcarrierSpacing = "";',
            'subcarrierSpacing = -1;',
            'subcarrierSpacing = "space";'
        ]
    },
    "referenceSubcarrierSpacing": {
        "original": 'referenceSubcarrierSpacing                                    = 1;',
        "variants": [
            'referenceSubcarrierSpacing = 2;',
            'referenceSubcarrierSpacing = "";',
            'referenceSubcarrierSpacing = -1;',
            'referenceSubcarrierSpacing = "ref";'
        ]
    },
    "dl_UL_TransmissionPeriodicity": {
        "original": 'dl_UL_TransmissionPeriodicity                                 = 6;',
        "variants": [
            'dl_UL_TransmissionPeriodicity = 7;',
            'dl_UL_TransmissionPeriodicity = "";',
            'dl_UL_TransmissionPeriodicity = -1;',
            'dl_UL_TransmissionPeriodicity = "period";'
        ]
    },
    "nrofDownlinkSlots": {
        "original": 'nrofDownlinkSlots                                             = 7;',
        "variants": [
            'nrofDownlinkSlots = 5;',
            'nrofDownlinkSlots = "";',
            'nrofDownlinkSlots = -1;',
            'nrofDownlinkSlots = "slot";'
        ]
    },
    "nrofDownlinkSymbols": {
        "original": 'nrofDownlinkSymbols                                           = 6;',
        "variants": [
            'nrofDownlinkSymbols = 7;',
            'nrofDownlinkSymbols = "";',
            'nrofDownlinkSymbols = -1;',
            'nrofDownlinkSymbols = "sym";'
        ]
    },
    "nrofUplinkSlots": {
        "original": 'nrofUplinkSlots                                               = 2;',
        "variants": [
            'nrofUplinkSlots = 3;',
            'nrofUplinkSlots = "";',
            'nrofUplinkSlots = -1;',
            'nrofUplinkSlots = "ulslot";'
        ]
    },
    "nrofUplinkSymbols": {
        "original": 'nrofUplinkSymbols                                             = 4;',
        "variants": [
            'nrofUplinkSymbols = 5;',
            'nrofUplinkSymbols = "";',
            'nrofUplinkSymbols = -1;',
            'nrofUplinkSymbols = "ulsym";'
        ]
    },
    "ssPBCH_BlockPower": {
        "original": 'ssPBCH_BlockPower                                             = -25;',
        "variants": [
            'ssPBCH_BlockPower = -20;',
            'ssPBCH_BlockPower = "";',
            'ssPBCH_BlockPower = "power";',
            'ssPBCH_BlockPower = -999;'
        ]
    },
    "SCTP_INSTREAMS": {
        "original": 'SCTP_INSTREAMS  = 2;',
        "variants": [
            'SCTP_INSTREAMS = 4;',
            'SCTP_INSTREAMS = "";',
            'SCTP_INSTREAMS = -1;',
            'SCTP_INSTREAMS = "stream";'
        ]
    },
    "SCTP_OUTSTREAMS": {
        "original": 'SCTP_OUTSTREAMS = 2;',
        "variants": [
            'SCTP_OUTSTREAMS = 4;',
            'SCTP_OUTSTREAMS = "";',
            'SCTP_OUTSTREAMS = -1;',
            'SCTP_OUTSTREAMS = "stream";'
        ]
    },
    "num_cc": {
        "original": 'num_cc = 1;',
        "variants": [
            'num_cc = 2;',
            'num_cc = 3;',
            'num_cc = "";',
            'num_cc = -1;',
            'num_cc = "cc";'
        ]
    },
    "tr_s_preference": {
        "original": 'tr_s_preference  = "local_L1";',
        "variants": [
            'tr_s_preference = "f1";',
            'tr_s_preference = "";',
            'tr_s_preference = 123;',
            'tr_s_preference = "@#L1";',
            'tr_s_preference = "local-f1";'
        ]
    },
    "tr_n_preference": {
        "original": 'tr_n_preference = "f1";',
        "variants": [
            'tr_n_preference = "e1";',
            'tr_n_preference = "";',
            'tr_n_preference = 456;',
            'tr_n_preference = "wrong";',
            'tr_n_preference = @@@;'
        ]
    },
    "local_n_address": {
        "original": 'local_n_address = "127.0.0.3";',
        "variants": [
            'local_n_address = "192.168.1.1";',
            'local_n_address = "";',
            'local_n_address = "abc.def.ghi.jkl";',
            'local_n_address = 127001;',
            'local_n_address = "@IP@";'
        ]
    },
    "remote_n_address": {
        "original": 'remote_n_address = "127.0.0.5";',
        "variants": [
            'remote_n_address = "192.168.1.2";',
            'remote_n_address = "";',
            'remote_n_address = 987654;',
            'remote_n_address = "invalid_ip";',
            'remote_n_address = "***";'
        ]
    },
    "local_n_portc": {
        "original": 'local_n_portc   = 500;',
        "variants": [
            'local_n_portc = 600;',
            'local_n_portc = "";',
            'local_n_portc = -1;',
            'local_n_portc = "port";',
            'local_n_portc = 65536;'
        ]
    },
    "local_n_portd": {
        "original": 'local_n_portd   = 2152;',
        "variants": [
            'local_n_portd = 2160;',
            'local_n_portd = "";',
            'local_n_portd = -500;',
            'local_n_portd = "udp";',
            'local_n_portd = 999999;'
        ]
    },
    "remote_n_portc": {
        "original": 'remote_n_portc  = 501;',
        "variants": [
            'remote_n_portc = 601;',
            'remote_n_portc = "";',
            'remote_n_portc = -10;',
            'remote_n_portc = "abc";',
            'remote_n_portc = 65536;'
        ]
    },
    "remote_n_portd": {
        "original": 'remote_n_portd  = 2152;',
        "variants": [
            'remote_n_portd = 2170;',
            'remote_n_portd = "";',
            'remote_n_portd = -1;',
            'remote_n_portd = "port";',
            'remote_n_portd = 999999;'
        ]
    },
    "num_cc": {
        "original": 'num_cc = 1;',
        "variants": [
            'num_cc = 3;',
            'num_cc = "";',
            'num_cc = -1;',
            'num_cc = "two";',
            'num_cc = @@@;'
        ]
    },
    "tr_n_preference": {
        "original": 'tr_n_preference = "local_mac";',
        "variants": [
            'tr_n_preference = "f1";',
            'tr_n_preference = "";',
            'tr_n_preference = 0;',
            'tr_n_preference = "???";'
        ]
    },
    "prach_dtx_threshold": {
        "original": 'prach_dtx_threshold = 120;',
        "variants": [
            'prach_dtx_threshold = 200;',
            'prach_dtx_threshold = "";',
            'prach_dtx_threshold = -1;',
            'prach_dtx_threshold = "delay";',
            'prach_dtx_threshold = 99999;'
        ]
    },
    "pucch0_dtx_threshold": {
        "original": 'pucch0_dtx_threshold = 150;',
        "variants": [
            'pucch0_dtx_threshold = 250;',
            'pucch0_dtx_threshold = "";',
            'pucch0_dtx_threshold = -5;',
            'pucch0_dtx_threshold = "dtxt";',
            'pucch0_dtx_threshold = ***;'
        ]
    },
    "ofdm_offset_divisor": {
        "original": 'ofdm_offset_divisor = 8;',
        "variants": [
            'ofdm_offset_divisor = 4;',
            'ofdm_offset_divisor = "";',
            'ofdm_offset_divisor = -1;',
            'ofdm_offset_divisor = "off";',
            'ofdm_offset_divisor = 99999;'
        ]
    },
    "local_rf": {
        "original": 'local_rf       = "yes"',
        "variants": [
            'local_rf = "no";',
            'local_rf = "";',
            'local_rf = 1;',
            'local_rf = "yess";',
            'local_rf = "RF";'
        ]
    },
    "nb_tx": {
        "original": 'nb_tx          = 1',
        "variants": [
            'nb_tx = 2;',
            'nb_tx = "";',
            'nb_tx = -1;',
            'nb_tx = "tx";',
            'nb_tx = @@@;'
        ]
    },
    "nb_rx": {
        "original": 'nb_rx          = 1',
        "variants": [
            'nb_rx = 2;',
            'nb_rx = "";',
            'nb_rx = -1;',
            'nb_rx = "rx";',
            'nb_rx = ***;'
        ]
    },
    "att_tx": {
        "original": 'att_tx         = 0',
        "variants": [
            'att_tx = 10;',
            'att_tx = "";',
            'att_tx = -5;',
            'att_tx = "tx_att";',
            'att_tx = ???;'
        ]
    },
    "att_rx": {
        "original": 'att_rx         = 0',
        "variants": [
            'att_rx = 10;',
            'att_rx = "";',
            'att_rx = -5;',
            'att_rx = "rx_att";',
            'att_rx = ###;'
        ]
    },
    "bands": {
        "original": 'bands          = [78];',
        "variants": [
            'bands = [77];',
            'bands = "";',
            'bands = [0];',
            'bands = [-1];',
            'bands = [abc];'
        ]
    },
    "max_pdschReferenceSignalPower": {
        "original": 'max_pdschReferenceSignalPower = -27;',
        "variants": [
            'max_pdschReferenceSignalPower = -30;',
            'max_pdschReferenceSignalPower = "";',
            'max_pdschReferenceSignalPower = "low";',
            'max_pdschReferenceSignalPower = 0;',
            'max_pdschReferenceSignalPower = ***;'
        ]
    },
    "max_rxgain": {
        "original": 'max_rxgain                    = 114;',
        "variants": [
            'max_rxgain = 120;',
            'max_rxgain = "";',
            'max_rxgain = -1;',
            'max_rxgain = "gain";',
            'max_rxgain = $$$;'
        ]
    },
    "eNB_instances": {
        "original": 'eNB_instances  = [0];',
        "variants": [
            'eNB_instances = [1];',
            'eNB_instances = "";',
            'eNB_instances = [-1];',
            'eNB_instances = [abc];',
            'eNB_instances = 1;'
        ]
    },
    "clock_src": {
        "original": 'clock_src = "internal";',
        "variants": [
            'clock_src = "external";',
            'clock_src = "";',
            'clock_src = 0;',
            'clock_src = "clk";',
            'clock_src = ***;'
        ]
    }
}