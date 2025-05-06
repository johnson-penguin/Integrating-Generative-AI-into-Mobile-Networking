# 測試參數（param_name: (原始字串, 要替換的新字串)）
test_params = {
    "Active_gNBs": (
        'Active_gNBs = ( "gNB-Eurecom-DU");',
        'Active_gNBs = ( "gNB-Test-DU");'
    ),
    "Asn1_verbosity": (
        'Asn1_verbosity = "none";',
        'Asn1_verbosity = "info";'
    ),
    "gNB_ID": (
        'gNB_ID = 0xe00;',
        'gNB_ID = 0x1234;'
    ),
    "gNB_DU_ID": (
        'gNB_DU_ID = 0xe00;',
        'gNB_DU_ID = 0x5678;'
    ),
    "gNB_name": (
        'gNB_name  =  "gNB-Eurecom-DU";',
        'gNB_name  =  "gNB-Test-DU";'
    ),
    "tracking_area_code": (
        'tracking_area_code  =  1;',
        'tracking_area_code  =  42;'
    ),
    "plmn_list": (
        'plmn_list = ({ mcc = 001; mnc = 01; mnc_length = 2; snssaiList = ( { sst = 1;}); });',
        'plmn_list = ({ mcc = 208; mnc = 93; mnc_length = 2; snssaiList = ( { sst = 1; }); });'
    ),
    "nr_cellid": (
        'nr_cellid = 1;',
        'nr_cellid = 1001;'
    ),
    "min_rxtxtime": (
        'min_rxtxtime = 6;',
        'min_rxtxtime = 2;'
    ),
    "force_256qam_off": (
        'force_256qam_off = 1;',
        'force_256qam_off = 0;'
    ),
     "physCellId": (
        'physCellId = 0;',
        'physCellId = 100;'
    ),
    "absoluteFrequencySSB": (
        'absoluteFrequencySSB = 641280;',
        'absoluteFrequencySSB = 640000;'
    ),
    "dl_frequencyBand": (
        'dl_frequencyBand = 78;',
        'dl_frequencyBand = 77;'
    ),
    "dl_absoluteFrequencyPointA": (
        'dl_absoluteFrequencyPointA = 640008;',
        'dl_absoluteFrequencyPointA = 642000;'
    ),
    "dl_offstToCarrier": (
        'dl_offstToCarrier = 0;',
        'dl_offstToCarrier = 10;'
    ),
    "dl_subcarrierSpacing": (
        'dl_subcarrierSpacing = 1;',
        'dl_subcarrierSpacing = 2;'
    ),
    "dl_carrierBandwidth": (
        'dl_carrierBandwidth = 106;',
        'dl_carrierBandwidth = 100;'
    ),
    "initialDLBWPlocationAndBandwidth": (
        'initialDLBWPlocationAndBandwidth = 28875;',
        'initialDLBWPlocationAndBandwidth = 28000;'
    ),
        "initialDLBWPsubcarrierSpacing": (
        'initialDLBWPsubcarrierSpacing = 1;',
        'initialDLBWPsubcarrierSpacing = 0;'
    ),
    "initialDLBWPcontrolResourceSetZero": (
        'initialDLBWPcontrolResourceSetZero = 12;',
        'initialDLBWPcontrolResourceSetZero = 13;'
    ),
    "initialDLBWPsearchSpaceZero": (
        'initialDLBWPsearchSpaceZero = 0;',
        'initialDLBWPsearchSpaceZero = 1;'
    ),
    "ul_frequencyBand": (
        'ul_frequencyBand = 78;',
        'ul_frequencyBand = 77;'
    ),
    "ul_offstToCarrier": (
        'ul_offstToCarrier = 0;',
        'ul_offstToCarrier = 15;'
    ),
    "ul_subcarrierSpacing": (
        'ul_subcarrierSpacing = 1;',
        'ul_subcarrierSpacing = 0;'
    ),
    "ul_carrierBandwidth": (
        'ul_carrierBandwidth = 106;',
        'ul_carrierBandwidth = 50;'
    ),
    "pMax": (
        'pMax = 20;',
        'pMax = 23;'
    ),
    "initialULBWPlocationAndBandwidth": (
        'initialULBWPlocationAndBandwidth = 28875;',
        'initialULBWPlocationAndBandwidth = 28000;'
    ),
    "initialULBWPsubcarrierSpacing": (
        'initialULBWPsubcarrierSpacing = 1;',
        'initialULBWPsubcarrierSpacing = 2;'
    ),
    "prach_ConfigurationIndex": (
        'prach_ConfigurationIndex = 98;',
        'prach_ConfigurationIndex = 100;'
    ),
    "prach_msg1_FDM": (
        'prach_msg1_FDM = 0;',
        'prach_msg1_FDM = 1;'
    ),
    "prach_msg1_FrequencyStart": (
        'prach_msg1_FrequencyStart = 0;',
        'prach_msg1_FrequencyStart = 5;'
    ),
    "zeroCorrelationZoneConfig": (
        'zeroCorrelationZoneConfig = 13;',
        'zeroCorrelationZoneConfig = 10;'
    ),
    "preambleReceivedTargetPower": (
        'preambleReceivedTargetPower = -96;',
        'preambleReceivedTargetPower = -90;'
    ),
        "preambleTransMax": (
        'preambleTransMax = 6;',
        'preambleTransMax = 10;'
    ),
    "powerRampingStep": (
        'powerRampingStep = 1;',
        'powerRampingStep = 2;'
    ),
    "ra_ResponseWindow": (
        'ra_ResponseWindow = 4;',
        'ra_ResponseWindow = 8;'
    ),
    "ssb_perRACH_OccasionAndCB_PreamblesPerSSB_PR": (
        'ssb_perRACH_OccasionAndCB_PreamblesPerSSB_PR = 4;',
        'ssb_perRACH_OccasionAndCB_PreamblesPerSSB_PR = 2;'
    ),
    "ssb_perRACH_OccasionAndCB_PreamblesPerSSB": (
        'ssb_perRACH_OccasionAndCB_PreamblesPerSSB = 14;',
        'ssb_perRACH_OccasionAndCB_PreamblesPerSSB = 8;'
    ),
    "ra_ContentionResolutionTimer": (
        'ra_ContentionResolutionTimer = 7;',
        'ra_ContentionResolutionTimer = 16;'
    ),
    "rsrp_ThresholdSSB": (
        'rsrp_ThresholdSSB = 19;',
        'rsrp_ThresholdSSB = 25;'
    ),
    "prach_RootSequenceIndex_PR": (
        'prach_RootSequenceIndex_PR = 2;',
        'prach_RootSequenceIndex_PR = 0;'
    ),
    "prach_RootSequenceIndex": (
        'prach_RootSequenceIndex = 1;',
        'prach_RootSequenceIndex = 22;'
    ),
    "msg1_SubcarrierSpacing": (
        'msg1_SubcarrierSpacing = 1,',
        'msg1_SubcarrierSpacing = 0,'
    ),
    "restrictedSetConfig": (
        'restrictedSetConfig = 0,',
        'restrictedSetConfig = 1,'
    ),
    "msg3_DeltaPreamble": (
        'msg3_DeltaPreamble = 1;',
        'msg3_DeltaPreamble = 3;'
    ),
    "p0_NominalWithGrant": (
        'p0_NominalWithGrant =-90;',
        'p0_NominalWithGrant =-80;'
    ),
        "pucchGroupHopping": (
        'pucchGroupHopping = 0;',
        'pucchGroupHopping = 1;'
    ),
    "hoppingId": (
        'hoppingId = 40;',
        'hoppingId = 63;'
    ),
    "p0_nominal": (
        'p0_nominal = -90;',
        'p0_nominal = -80;'
    ),
    "ssb_PositionsInBurst_Bitmap": (
        'ssb_PositionsInBurst_Bitmap = 1;',
        'ssb_PositionsInBurst_Bitmap = 0;'
    ),
    "ssb_periodicityServingCell": (
        'ssb_periodicityServingCell = 2;',
        'ssb_periodicityServingCell = 1;'
    ),
    "dmrs_TypeA_Position": (
        'dmrs_TypeA_Position = 0;',
        'dmrs_TypeA_Position = 1;'
    ),
    "subcarrierSpacing": (
        'subcarrierSpacing = 1;',
        'subcarrierSpacing = 0;'
    ),
    "referenceSubcarrierSpacing": (
        'referenceSubcarrierSpacing = 1;',
        'referenceSubcarrierSpacing = 2;'
    ),
    "dl_UL_TransmissionPeriodicity": (
        'dl_UL_TransmissionPeriodicity = 6;',
        'dl_UL_TransmissionPeriodicity = 7;'
    ),
    "nrofDownlinkSlots": (
        'nrofDownlinkSlots = 7;',
        'nrofDownlinkSlots = 5;'
    ),
    "nrofDownlinkSymbols": (
        'nrofDownlinkSymbols = 6;',
        'nrofDownlinkSymbols = 7;'
    ),
    "nrofUplinkSlots": (
        'nrofUplinkSlots = 2;',
        'nrofUplinkSlots = 3;'
    ),
    "nrofUplinkSymbols": (
        'nrofUplinkSymbols = 4;',
        'nrofUplinkSymbols = 5;'
    ),
    "ssPBCH_BlockPower": (
        'ssPBCH_BlockPower = -25;',
        'ssPBCH_BlockPower = -20;'
    ),
    "SCTP_INSTREAMS": (
        'SCTP_INSTREAMS = 2;',
        'SCTP_INSTREAMS = 4;'
    ),
    "SCTP_OUTSTREAMS": (
        'SCTP_OUTSTREAMS = 2;',
        'SCTP_OUTSTREAMS = 4;'
    ),
    "num_cc": (
        'num_cc = 1;',
        'num_cc = 2;'
    ),
    "tr_s_preference": (
        'tr_s_preference = "local_L1";',
        'tr_s_preference = "f1";'
    ),
    "tr_n_preference": (
        'tr_n_preference = "f1";',
        'tr_n_preference = "e1";'
    ),
    "local_n_address": (
        'local_n_address = "127.0.0.3";',
        'local_n_address = "192.168.1.1";'
    ),
    "remote_n_address": (
        'remote_n_address = "127.0.0.5";',
        'remote_n_address = "192.168.1.2";'
    ),
    "local_n_portc": (
        'local_n_portc = 500;',
        'local_n_portc = 600;'
    ),
    "local_n_portd": (
        'local_n_portd = 2152;',
        'local_n_portd = 2160;'
    ),
    "remote_n_portc": (
        'remote_n_portc = 501;',
        'remote_n_portc = 601;'
    ),
    "remote_n_portd": (
        'remote_n_portd = 2152;',
        'remote_n_portd = 2170;'
    ),
    "num_cc": (
    'num_cc = 1;',
    'num_cc = 3;'
    ),
    "tr_n_preference": (
        'tr_n_preference = "local_mac";',
        'tr_n_preference = "f1";'
    ),
    "prach_dtx_threshold": (
        'prach_dtx_threshold = 120;',
        'prach_dtx_threshold = 200;'
    ),
    "pucch0_dtx_threshold": (
        'pucch0_dtx_threshold = 150;',
        'pucch0_dtx_threshold = 250;'
    ),
    "ofdm_offset_divisor": (
        'ofdm_offset_divisor = 8;',
        'ofdm_offset_divisor = 4;'
    ),
    "local_rf": (
        'local_rf = "yes";',
        'local_rf = "no";'
    ),
    "nb_tx": (
        'nb_tx = 1;',
        'nb_tx = 2;'
    ),
    "nb_rx": (
        'nb_rx = 1;',
        'nb_rx = 2;'
    ),
    "att_tx": (
        'att_tx = 0;',
        'att_tx = 10;'
    ),
    "att_rx": (
        'att_rx = 0;',
        'att_rx = 10;'
    ),
    "bands": (
        'bands = [78];',
        'bands = [77];'
    ),
    "max_pdschReferenceSignalPower": (
        'max_pdschReferenceSignalPower = -27;',
        'max_pdschReferenceSignalPower = -30;'
    ),
    "max_rxgain": (
        'max_rxgain = 114;',
        'max_rxgain = 120;'
    ),
    "eNB_instances": (
        'eNB_instances = [0];',
        'eNB_instances = [1];'
    ),
    "clock_src": (
        'clock_src = "internal";',
        'clock_src = "external";'
    )  
}