+---------------------------------------------+-----------------------+
| 3GPP TS 38.133 V16.17.0 (2023-09)           |                       |
+=============================================+=======================+
| Technical Specification                     |                       |
+---------------------------------------------+-----------------------+
| 3rd Generation Partnership Project;         |                       |
|                                             |                       |
| Technical Specification Group Radio Access  |                       |
| Network;                                    |                       |
|                                             |                       |
| NR;                                         |                       |
|                                             |                       |
| Requirements for support of radio resource  |                       |
| management                                  |                       |
|                                             |                       |
| (Release 16)                                |                       |
+---------------------------------------------+-----------------------+
|                                             |                       |
+---------------------------------------------+-----------------------+
| ![](media/image1.jpeg)                      | ![](media/image2.png) |
+---------------------------------------------+-----------------------+
|                                             |                       |
+---------------------------------------------+-----------------------+
| The present document has been developed     |                       |
| within the 3rd Generation Partnership       |                       |
| Project (3GPP ^TM^) and may be further      |                       |
| elaborated for the purposes of 3GPP.\       |                       |
| The present document has not been subject   |                       |
| to any approval process by the 3GPP         |                       |
| Organizational Partners and shall not be    |                       |
| implemented.\                               |                       |
| This Specification is provided for future   |                       |
| development work within 3GPP only. The      |                       |
| Organizational Partners accept no liability |                       |
| for any use of this Specification.\         |                       |
| Specifications and Reports for              |                       |
| implementation of the 3GPP ^TM^ system      |                       |
| should be obtained via the 3GPP             |                       |
| Organizational Partners\' Publications      |                       |
| Offices.                                    |                       |
+---------------------------------------------+-----------------------+

+----------------------------------------------------------------------+
|                                                                      |
+======================================================================+
| > ***3GPP***                                                         |
| >                                                                    |
| > Postal address                                                     |
| >                                                                    |
| > 3GPP support office address                                        |
| >                                                                    |
| > 650 Route des Lucioles - Sophia Antipolis                          |
| >                                                                    |
| > Valbonne - FRANCE                                                  |
| >                                                                    |
| > Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16                     |
| >                                                                    |
| > Internet                                                           |
| >                                                                    |
| > http://www.3gpp.org                                                |
+----------------------------------------------------------------------+
| ***Copyright Notification***                                         |
|                                                                      |
| No part may be reproduced except as authorized by written            |
| permission.\                                                         |
| The copyright and the foregoing restriction extend to reproduction   |
| in all media.                                                        |
|                                                                      |
| © 2023, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, |
| TTA, TTC).                                                           |
|                                                                      |
| All rights reserved.                                                 |
|                                                                      |
| UMTS™ is a Trade Mark of ETSI registered for the benefit of its      |
| members                                                              |
|                                                                      |
| 3GPP™ is a Trade Mark of ETSI registered for the benefit of its      |
| Members and of the 3GPP Organizational Partners\                     |
| LTE™ is a Trade Mark of ETSI registered for the benefit of its       |
| Members and of the 3GPP Organizational Partners                      |
|                                                                      |
| GSM® and the GSM logo are registered and owned by the GSM            |
| Association                                                          |
+----------------------------------------------------------------------+

 Contents {#contents .TT}
========

Foreword 421 Scope 442 References 443 Definitions, symbols and
abbreviations 453.1 Definitions 453.2 Symbols 463.3 Abbreviations 473.4
Test tolerances 503.5 Frequency bands grouping 503.5.1 Introduction
503.5.2 NR operating bands in FR1 503.5.3 NR operating bands in FR2
513.6 Applicability of requirements in this specification version
513.6.1 RRC connected state requirements in DRX 523.6.2 Number of
serving carriers 523.6.2.1 Number of serving carriers for SA 523.6.2.2
Number of serving carriers for EN-DC 523.6.2.3 Number of serving
carriers for NE-DC 523.6.2.4 Number of serving carriers for NR-DC
533.6.3 Applicability for intra-band FR2 533.6.4 Applicability for FR2
UE power classes 533.6.5 Applicability for SDL bands 533.6.6
Applicability of requirements for NGEN-DC operation 533.6.7
Applicability of QCL 533.6.9 Applicability of requirements for
scheduling availability 543.6.10 Applicability of requirements for
measurement restrictions 544 SA: RRC\_IDLE state mobility 544.1 Cell
Selection 544.2 Cell Re-selection 544.2.1 Introduction 544.2.2
Requirements 554.2.2.1 UE measurement capability 554.2.2.2 Measurement
and evaluation of serving cell 554.2.2.3 Measurements of intra-frequency
NR cells 564.2.2.4 Measurements of inter-frequency NR cells 574.2.2.5
Measurements of inter-RAT E-UTRAN cells 594.2.2.6 Maximum interruption
in paging reception 614.2.2.7 General requirements 614.2.2.8 Minimum
requirement at transitions 614.2.2.9 Measurements of intra-frequency NR
cells for UE configured with relaxed measurement criterion 624.2.2.9.1
Introduction 624.2.2.9.2 Measurements for UE fulfilling low mobility
criterion 624.2.2.9.3 Measurements for UE fulfilling not-at-cell edge
criterion 634.2.2.9.4 Measurements for UE fulfilling low mobility and
not-at-cell edge criteria 644.2.2.10 Measurements of inter-frequency NR
cells for UE configured with relaxed measurement criterion 644.2.2.10.1
Introduction 644.2.2.10.2 Measurements for UE fulfilling low mobility
criterion 644.2.2.10.3 Measurements for UE fulfilling not-at-cell edge
criterion 654.2.2.10.4 Measurements for UE fulfilling low mobility and
not-at-cell edge criterion 664.2.2.11 Measurements of inter-RAT E-UTRAN
cells for UE configured with relaxed measurement criterion 674.2.2.11.1
Introduction 674.2.2.11.2 Measurements for UE fulfilling low mobility
criterion 674.2.2.11.3 Measurements for UE fulfilling with not-at-cell
edge criterion 684.2.2.11.4 Measurements for UE fulfilling low mobility
and not-at-cell edge criterion 694.2A Cell Re-selection when subject to
CCA 694.2A.1 Introduction 694.2A.2 Requirements 704.2A.2.1 UE
measurement capability 704.2A.2.2 Measurement and evaluation when
subject to CCA on the serving cell 704.2A.2.3 Measurements of
intra-frequency NR cells when subject to CCA on the serving cell and
target cell 714.2A.2.4 Measurements of inter-frequency NR cells when
subject to CCA on the target cell 724.2A.2.5 Measurements of inter-RAT
E-UTRAN cells when subject to CCA on the serving cell 744.2A.2.6 Maximum
interruption in paging reception when subject to CCA on the target cell
744.2A.2.7 General requirements 744.3 Minimization of Drive Tests (MDT)
754.3.1 Introduction 754.3.2 Measurement Requirements 754.3.3
Requirements for Relative Time Stamp Accuracy 754.3.4 Requirements for
Relative Time Stamp Accuracy for RRC Connection Establishment Failure
Log Reporting 764.3.5 Requirements for Relative Time Stamp Accuracy for
Radio Link Failure and Handover Failure Log Reporting 764.4 Idle Mode
CA/DC Measurements 764.4.1 Introduction 764.4.2 Measurement Requirements
764.4.2.1 Detected cell requirement during state transition and Idle
mode 764.4.2.2 Measurements of inter-frequency CA/DC candidate cells
774.4.2.3 Measurements on serving cell 784.4.2.4 Measurements of E-UTRAN
inter-RAT DC candidate cells 785 SA: RRC\_INACTIVE state mobility 805.1
Cell Re-selection 805.1.1 Introduction 805.1.2 Requirements 805.1.2.1 UE
measurement capability 805.1.2.2 Measurement and evaluation of serving
cell 805.1.2.3 Measurements of intra-frequency NR cells 805.1.2.4
Measurements of inter-frequency NR cells 805.1.2.5 Measurements of
inter-RAT E-UTRAN cells 805.1.2.6 Maximum interruption in paging
reception 805.1.2.7 General requirements 805.1A Cell Re-selection with
CCA 805.1A.1 Introduction 805.1A.2 Requirements 815.1A.2.1 UE
measurement capability 815.1A.2.2 Measurement and evaluation when CCA is
used on the serving cell 815.1A.2.3 Measurements of intra-frequency NR
cells when CCA is used on the serving cell and target cell 815.1A.2.4
Measurements of inter-frequency NR cells when CCA is used on the target
cell 815.1A.2.5 Measurements of inter-RAT E-UTRAN cells when CCA is used
on the serving cell 815.1A.2.6 Maximum interruption in paging reception
when CCA is used on the target cell 815.1A.2.7 General requirements
815.2 Void 815.3 Minimization of Drive Tests (MDT) 815.3.1 Introduction
815.3.2 Measurement Requirements 825.3.3 Requirements for Relative Time
Stamp Accuracy 825.3.4 Requirements for Relative Time Stamp Accuracy for
RRC Connection Establishment Failure Log Reporting 825.3.5 Requirements
for Relative Time Stamp Accuracy for Radio Link Failure and Handover
Failure Log Reporting 825.3.6 Requirements for Relative Time Stamp
Accuracy for RRC Resume Failure Log Reporting 825.4 Idle Mode CA/DC
Measurements 825.4.1 Introduction 825.4.2 Measurement Requirements
825.4.2.1 Detected cell requirement during state transition and Idle
mode 835.4.2.2 Measurements of inter-frequency CA/DC candidate cells
835.4.2.3 Measurements on serving cell 835.4.2.4 Measurements on E-UTRAN
inter-RAT DC candidate cells 836 RRC\_CONNECTED state mobility 836.1
Handover 836.1.1 NR Handover 836.1.1.1 Introduction 836.1.1.2 NR FR1 -
NR FR1 Handover 836.1.1.2.1 Handover delay 836.1.1.2.2 Interruption time
836.1.1.3 NR FR2- NR FR1 Handover 846.1.1.3.1 Handover delay 846.1.1.3.2
Interruption time 846.1.1.4 NR FR2- NR FR2 Handover 856.1.1.4.1 Handover
delay 856.1.1.4.2 Interruption time 856.1.1.5 NR FR1- NR FR2 Handover
866.1.1.5.1 Handover delay 866.1.1.5.2 Interruption time 866.1.2 NR
Handover to other RATs 876.1.2.1 NR -- E-UTRAN Handover 876.1.2.1.1
Introduction 876.1.2.1.2 Handover delay 876.1.2.1.3 Interruption time
876.1.2.2 NR -- UTRAN Handover 886.1.2.2.1 Introduction 886.1.2.2.2
Handover delay 886.1.2.2.3 Interruption time 886.1.3 NR DAPS Handover
896.1.3.1 Introduction 896.1.3.2 NR FR1 - NR FR1 DAPS Handover
896.1.3.2.1 DAPS handover delay 896.1.3.2.2 Interruption time 906.1.3.3
NR FR2- NR FR1 DAPS Handover 926.1.3.3.1 DAPS handover delay 926.1.3.3.2
Interruption time 926.1.3.4 NR FR1- NR FR2 DAPS Handover 936.1.3.4.1
DAPS handover delay 936.1.3.4.2 Interruption time 946.1.4 NR Conditional
Handover 946.1.4.1 Introduction 946.1.4.2 NR FR1 -- NR FR1 conditional
handover 946.1.4.3 NR FR2 -- NR FR1 conditional handover 956.1.4.4 NR
FR2 -- NR FR2 conditional handover 966.1.4.4.1 Handover delay
966.1.4.4.2 Measurement time 966.1.4.4.3 Preparation time 966.1.4.4.4
Interruption time 976.1.4.5 NR FR1 -- NR FR2 conditional handover 976.1A
Void 976.1A.1 Void 976.1A.1.1 Void 976.1A.1.2 Void 976.1A.1.2.1 Void
976.1A.1.2.2 Void 976.1B Handover to target cell using CCA 986.1B.1 NR
Handover 986.1B.1.1 Introduction 986.1B.1.2 NR FR1 - NR FR1 Handover
986.1B.1.2.1 Handover delay 986.1B.1.2.2 Interruption time 986.2 RRC
Connection Mobility Control 996.2.1 SA: RRC Re-establishment 996.2.1.1
Introduction 996.2.1.2 Requirements 996.2.1.2.1 UE Re-establishment
delay requirement 996.2.1A RRC Re-establishment with CCA 1016.2.1A.1
Introduction 1016.2.1A.2 Requirements 1016.2.1A.2.1 UE Re-establishment
with CCA delay requirement 1016.2.2 Random access 1036.2.2.1
Introduction 1036.2.2.2 Requirements for 4-step RA type 1036.2.2.2.1
Contention based random access 1046.2.2.2.2 Non-Contention based random
access 1046.2.2.2.3 UE behaviour when configured with supplementary UL
1056.2.2.3 Requirements for 2-step RA type 1056.2.2.3.1 Contention based
random access 1066.2.2.3.2 Non-Contention based random access
1076.2.2.3.3 UE behaviour when configured with supplementary UL
1076.2.2A Random access when CCA is used on target frequency 1076.2.2A.1
Introduction 1076.2.2A.2 Requirements for 4-step RA type 1086.2.2A.2.1
Contention based random access 1086.2.2A.2.2 Non-Contention based random
access 1096.2.2A.3 Requirements for 2-step RA type 1106.2.2A.3.1
Contention based random access 1106.2.2A.3.2 Non-Contention based random
access 1116.2.3 SA: RRC Connection Release with Redirection 1126.2.3.1
Introduction 1126.2.3.2 Requirements 1126.2.3.2.1 RRC connection release
with redirection to NR 1126.2.3.2.2 RRC connection release with
redirection to E-UTRAN 1136.2.3.2.3 RRC connection release with
redirection to NR carrier subject to CCA 1147 Timing 1157.1 UE transmit
timing 1157.1.1 Introduction 1157.1.2 Requirements 1157.1.2.1 Gradual
timing adjustment 1167.1.2.2 Void 1177.2 UE timer accuracy 1177.2.1
Introduction 1177.2.2 Requirements 1177.3 Timing advance 1187.3.1
Introduction 1187.3.2 Requirements 1187.3.2.1 Timing Advance adjustment
delay 1187.3.2.2 Timing Advance adjustment accuracy 1187.4 Cell phase
synchronization accuracy 1187.4.1 Definition 1187.4.2 Minimum
requirements 1187.5 Maximum Transmission Timing Difference 1187.5.1
Introduction 1187.5.2 Minimum Requirements for inter-band EN-DC
1197.5.2.1 Minimum Requirements for inter-band synchronous EN-DC
1197.5.3 Minimum Requirements for intra-band EN-DC 1197.5.4 Minimum
Requirements for NR Carrier Aggregation 1207.5.5 Minimum Requirements
for inter-band NE-DC 1207.5.5.1 Minimum Requirements for inter-band
synchronous NE-DC 1217.5.6 Minimum Requirements for inter-band NR DC
1217.6 Maximum Receive Timing Difference 1227.6.1 Introduction 1227.6.2
Minimum Requirements for inter-band EN-DC 1227.6.2.1 Minimum
Requirements for inter-band synchronous EN-DC 1227.6.3 Minimum
Requirements for intra-band EN-DC 1237.6.4 Minimum Requirements for NR
Carrier Aggregation 1237.6.5 Minimum Requirements for inter-band NE-DC
1247.6.5.1 Minimum Requirements for inter-band synchronous NE-DC
1247.6.6 Minimum Requirements for inter-band NR DC 1247.7
*deriveSSB-IndexFromCell* tolerance 1257.7.1 Minimum requirements 1257.8
Void 1258 Signalling characteristics 1258.1 Radio Link Monitoring
1258.1.1 Introduction 1258.1.2 Requirements for SSB based radio link
monitoring 1268.1.2.1 Introduction 1268.1.2.2 Minimum requirement
1278.1.2.3 Measurement restrictions for SSB based RLM 1298.1.3
Requirements for CSI-RS based radio link monitoring 1298.1.3.1
Introduction 1298.1.3.2 Minimum requirement 1308.1.3.3 Measurement
restrictions for CSI-RS based RLM 1328.1.4 Minimum requirement at
transitions 1338.1.5 Minimum requirement for UE turning off the
transmitter 1338.1.6 Minimum requirement for L1 indication 1338.1.7
Scheduling availability of UE during radio link monitoring 1348.1.7.1
Scheduling availability of UE performing radio link monitoring with a
same subcarrier spacing as PDSCH/PDCCH on FR1 1348.1.7.2 Scheduling
availability of UE performing radio link monitoring with a different
subcarrier spacing than PDSCH/PDCCH on FR1 1348.1.7.3 Scheduling
availability of UE performing radio link monitoring on FR2 1348.1.7.4
Scheduling availability of UE performing radio link monitoring on FR1 or
FR2 in case of FR1-FR2 inter-band CA and NR-DC 1358.1A Radio Link
Monitoring with CCA on Target Frequency 1358.1A.1 Introduction 1358.1A.2
Requirements for SSB Based Radio Link Monitoring 1368.1A.2.1
Introduction 1368.1A.2.2 Minimum Requirement 1378.1A.3 Minimum
requirement at transitions 1388.1A.4 Minimum requirement for UE turning
off the transmitter 1398.1A.5 Minimum requirement for L1 indication
1398.1A.6 Scheduling availability of UE during radio link monitoring
1398.1A.6.1 Scheduling availability of UE performing radio link
monitoring with the same subcarrier spacing as PDSCH/PDCCH 1398.1A.6.2
Scheduling availability of UE performing radio link monitoring with a
different subcarrier spacing than PDSCH/PDCCH 1398.2 Interruption
1408.2.1 EN-DC Interruption 1408.2.1.1 Introduction 1408.2.1.2
Requirements 1408.2.1.2.1 Interruptions at transitions between active
and non-active during DRX 1408.2.1.2.2 Interruptions at transitions from
non-DRX to DRX 1418.2.1.2.3 Interruptions at SCell addition/release
1418.2.1.2.4 Interruptions at SCell activation/deactivation 1428.2.1.2.5
Interruptions during measurements on SCC 1438.2.1.2.6 Interruptions at
UL carrier RRC reconfiguration 1458.2.1.2.7 Interruptions due to Active
BWP switching Requirement 1458.2.1.2.8 Interruptions at direct SCell
activation and hibernation 1468.2.1.2.9 Interruptions at SCell
hibernation 1478.2.1.2.10 Interruptions at SCell activation/deactivation
with multiple downlink SCells 1478.2.1.2.11 Interruptions due to
UE-specific CBW change 1478.2.1.2.12 Interruptions at NR SRS carrier
based switching 1488.2.1.2.13 Interruptions at E-UTRA SRS carrier based
switching 1498.2.1.2.14 DL Interruptions at switching between two uplink
carriers 1508.2.1.2.15 Interruptions due to SCell dormancy 1508.2.1.2.16
Interruptions when identifying CGI of an NR cell with autonomous gaps
1518.2.1.2.17 Interruptions when identifying CGI of an E-UTRA cell with
autonomous gaps 1518.2.2 SA: Interruptions with Standalone NR Carrier
Aggregation 1528.2.2.1 Introduction 1528.2.2.2 Requirements 1538.2.2.2.1
Interruptions at SCell addition/release 1538.2.2.2.2 Interruptions at
SCell activation/deactivation 1548.2.2.2.3 Interruptions during
measurements on deactivated SCC 1558.2.2.2.4 Interruptions at UL carrier
RRC reconfiguration 1568.2.2.2.5 Interruptions due to Active BWP
switching Requirement 1568.2.2.2.6 Interruptions at inter-frequency SFTD
measurement 1578.2.2.2.7 Interruptions at SCell activation/deactivation
with multiple downlink SCells 1588.2.2.2.8 Interruptions due to
UE-specific CBW change 1588.2.2.2.9 Interruptions at NR SRS carrier
based switching 1598.2.2.2.10 DL Interruptions at UE switching between
two uplink carriers 1608.2.2.2.11 Interruptions at direct SCell
activation 1618.2.2.2.12 Interruptions due to SCell dormancy
1618.2.2.2.13 Interruptions at transitions between active and non-active
during DRX 1618.2.2.2.14 Interruptions when identifying CGI of an NR
cell with autonomous gaps 1628.2.2.2.15 Interruptions when identifying
CGI of an E-UTRA cell with autonomous gaps 1628.2.3 NE-DC Interruptions
1638.2.3.1 Introduction 1638.2.3.2 Requirements 1638.2.3.2.1
Interruptions at transitions between active and non-active during DRX
1638.2.3.2.2 Interruptions at transitions from non-DRX to DRX
1648.2.3.2.3 Interruptions at PSCell/SCell addition/release 1648.2.3.2.4
Interruptions at SCell activation/deactivation 1658.2.3.2.5
Interruptions during measurements on SCC 1668.2.3.2.6 Interruptions at
UL carrier RRC reconfiguration 1678.2.3.2.7 Interruptions due to Active
BWP switching Requirement 1688.2.3.2.8 Interruptions at direct SCell
activation and hibernation 1688.2.3.2.9 Interruptions at SCell
hibernation 1688.2.3.2.10 Interruptions at SCell activation/deactivation
with multiple downlink SCells 1698.2.3.2.11 Interruptions at NR SRS
carrier based switching 1698.2.3.2.12 Interruptions at E-UTRA SRS
carrier based switching 1708.2.3.2.13 Interruptions due to SCell
dormancy 1718.2.3.2.14 Interruptions when identifying CGI of an NR cell
with autonomous gaps 1728.2.3.2.15 Interruptions when identifying CGI of
an E-UTRA cell with autonomous gaps 1728.2.3.2.16 Interruptions due to
UE-specific CBW change 1738.2.4 NR-DC: Interruptions 1738.2.4.1
Introduction 1738.2.4.2 Requirements 1748.2.4.2.1 Interruptions at
PSCell/SCell addition/release 1748.2.4.2.3 Interruptions during
measurements on SCC 1758.2.4.2.4 Interruptions at UL carrier RRC
reconfiguration 1758.2.4.2.5 Interruptions due to Active BWP switching
Requirement 1768.2.4.2.6 Interruptions at transitions between active and
non-active during DRX 1768.2.4.2.7 Interruptions at transitions from
non-DRX to DRX 1768.2.4.2.8 Interruptions at SCell
activation/deactivation with multiple downlink SCells 1778.2.4.2.9
Interruptions at NR SRS carrier based switching 1778.2.4.2.10
Interruptions at direct SCell activation 1788.2.4.2.11 Interruptions
when identifying CGI of an NR cell with autonomous gaps 1798.2.4.2.12
Interruptions when identifying CGI of an E-UTRA cell with autonomous
gaps 1798.2.4.2.13 Interruptions due to SCell dormancy 1808.2.4.2.14
Interruptions due to UE-specific CBW change 1808.2.4.2A Void
1818.2.4.2A.1 Void 1818.2.4.2A.2 Void 1818.2.4.2A.3 Void 1818.3 SCell
Activation and Deactivation Delay 1818.3.1 Introduction 1818.3.2 SCell
Activation Delay Requirement for Deactivated SCell 1818.3.3 SCell
Deactivation Delay Requirement for Activated SCell 1858.3.4 Direct SCell
Activation at SCell addition 1858.3.5 Direct SCell Activation at
Handover 1878.3.7 SCell Activation Delay Requirement for Deactivated
SCell with Multiple Downlink SCells 1898.3.8 SCell Deactivation Delay
Requirement for Activated SCell with Multiple Downlink SCells 1938.3.9
Direct SCell Activation of Multiple Downlink SCells at SCell addition
1938.3.10 Direct SCell Activation of Multiple Downlink SCells at
Handover 1948.3A SCell Activation and Deactivation Delay in Carriers
with CCA 1968.3A.1 Introduction 1968.3A.2 SCell Activation Delay
Requirement for Deactivated SCell 1968.3A.3 SCell Deactivation Delay
Requirement for Activated SCell 1998.4 UE UL carrier RRC reconfiguration
delay 1998.4.1 Introduction 1998.4.2 UE UL carrier configuration delay
requirement 1998.4.3 UE UL carrier deconfiguration delay requirement
1998.5 Link Recovery Procedures 2008.5.1 Introduction 2008.5.2
Requirements for SSB based beam failure detection 2018.5.2.1
Introduction 2018.5.2.2 Minimum requirement 2018.5.2.3 Measurement
restriction for SSB based beam failure detection 2038.5.3 Requirements
for CSI-RS based beam failure detection 2038.5.3.1 Introduction
2038.5.3.2 Minimum requirement 2048.5.3.3 Measurement restrictions for
CSI-RS beam failure detection 2068.5.4 Minimum requirement for L1
indication 2078.5.5 Requirements for SSB based candidate beam detection
2078.5.5.1 Introduction 2078.5.5.2 Minimum requirement 2078.5.5.3
Measurement restriction for SSB based candidate beam detection 2098.5.6
Requirements for CSI-RS based candidate beam detection 2108.5.6.1
Introduction 2108.5.6.2 Minimum requirement 2108.5.6.3 Measurement
restriction for CSI-RS based candidate beam detection 2128.5.7
Scheduling availability of UE during beam failure detection 2138.5.7.1
Scheduling availability of UE performing beam failure detection with a
same subcarrier spacing as PDSCH/PDCCH on FR1 2138.5.7.2 Scheduling
availability of UE performing beam failure detection with a different
subcarrier spacing than PDSCH/PDCCH on FR1 2138.5.7.3 Scheduling
availability of UE performing beam failure detection on FR2 2138.5.7.4
Scheduling availability of UE performing beam failure detection on FR1
or FR2 in case of FR1-FR2 inter-band CA and NR DC 2148.5.8 Scheduling
availability of UE during candidate beam detection 2148.5.8.1 Scheduling
availability of UE performing L1-RSRP measurement with a same subcarrier
spacing as PDSCH/PDCCH on FR1 2148.5.8.2 Scheduling availability of UE
performing L1-RSRP measurement with a different subcarrier spacing than
PDSCH/PDCCH on FR1 2148.5.8.3 Scheduling availability of UE performing
L1-RSRP measurement on FR2 2148.5.8.4 Scheduling availability of UE
performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2
inter-band CA and NR-DC 2158.5.9 Requirements for Beam Failure Recovery
in SCell 2158.5.9.1 Introduction 2158.5.9.2 Requirement 2158.5.10
Minimum requirement at transitions for beam failure detection 2158.5A
Link Recovery Procedures when CCA is used on target frequency 2168.5A.1
Introduction 2168.5A.2 Requirements for SSB based beam failure detection
2168.5A.2.1 Introduction 2168.5A.2.2 Minimum requirement 2178.5A.2.3
Measurement restriction for SSB based beam failure detection 2178.5A.4
Minimum requirement for L1 indication 2188.5A.5 Requirements for SSB
based candidate beam detection 2188.5A.5.1 Introduction 2188.5A.5.2
Minimum requirement 2188.5A.5.3 Measurement restriction for SSB based
candidate beam detection 2198.5A.7 Scheduling availability of UE during
beam failure detection 2198.5A.7.1 Scheduling availability of UE
performing beam failure detection with a same subcarrier spacing as
PDSCH/PDCCH 2198.5A.7.2 Scheduling availability of UE performing beam
failure detection with a different subcarrier spacing than PDSCH/PDCCH
2198.5A.8 Scheduling availability of UE during candidate beam detection
2198.5A.8.1 Scheduling availability of UE performing L1-RSRP measurement
with a same subcarrier spacing as PDSCH/PDCCH 2208.5A.8.2 Scheduling
availability of UE performing L1-RSRP measurement with a different
subcarrier spacing than PDSCH/PDCCH 2208.6 Active BWP switch delay
2208.6.1 Introduction 2208.6.2 DCI and timer based BWP switch delay on a
single CC 2208.6.2A DCI based BWP switch delay on multiple CCs
2218.6.2A.1 Simultaneous DCI based BWP switch delay on multiple CCs
2218.6.2A.2 Non-simultaneous DCI based BWP switch delay on multiple CCs
2238.6.2B Timer based BWP switch delay on multiple CCs 2238.6.2B.1
Simultaneous timer based BWP switch delay on multiple CCs 2238.6.2B.2
Non-simultaneous timer based BWP switch delay on multiple CCs 2248.6.3
RRC based BWP switch delay on a single CC 2248.6.3A RRC based BWP switch
delay on multiple CCs 2258.6.3A.1 Simultaneous RRC based BWP switch
delay on multiple CCs 2258.6.3A.2 Non-simultaneous RRC based BWP switch
delay on multiple CCs 2258.6.4 BWP switch delay on Consistent UL CCA
recovery 2268.7 Void 2268.8 NE-DC: E-UTRAN PSCell Addition and Release
Delay 2268.8.1 Introduction 2268.8.2 E-UTRAN PSCell Addition Delay
Requirement 2268.8.3 E-UTRAN PSCell Release Delay Requirement 2278.9
NR-DC: PSCell Addition and Release Delay 2278.9.1 Introduction 2278.9.2
PSCell Addition Delay Requirement 2278.9.3 PSCell Release Delay
Requirement 2288.10 Active TCI state switching delay 2288.10.4 DCI based
TCI state switch delay 2308.10.5 RRC based TCI state switch delay
2308.10.6 Active TCI state list update delay 2308.10A Active TCI state
switching delay with CCA 2318.10A.1 Introduction 2318.10A.2 Known
conditions for TCI state 2318.10A.3 MAC-CE based TCI state switch delay
2318.10A.4 DCI based TCI state switch delay 2328.10A.5 RRC based TCI
state switch delay 2328.10A.6 Active TCI state list update delay 2338.11
PSCell Change 2338.11A void 2348.11B Conditional PSCell Change
2348.11B.1 Introduction 2348.11B.2 Conditoinal PSCell Change delay
2348.11B.2.1 Measurement time 2348.12 Uplink spatial relation switch
delay 2358.12.1 Introduction 2358.12.2 Known conditions for spatial
relation when associated with DL-RS 2358.12.3 MAC-CE based spatial
relation switch delay 2358.12.4 DCI based spatial relation switch delay
2368.12.5 RRC based spatial relation switch delay 2368.13 UE-specific
CBW change 2378.13.1 Introduction 2378.13.2 UE-specific CBW change delay
2378.14 Pathloss reference signal switching delay 2378.14.1 Introduction
2378.14.2 Known conditions for pathloss reference signal 2378.14.3
MAC-CE based pathloss reference signal switch delay 2389 Measurement
Procedure 2399.1 General measurement requirement 2399.1.1 Introduction
2399.1.2 Measurement gap 2399.1.2.1 EN-DC: Measurement Gap Sharing
2509.1.2.1a SA: Measurement Gap Sharing 2509.1.2.1b NE-DC: Measurement
Gap Sharing 2519.1.2.1c NR-DC: Measurement Gap Sharing 2529.1.3 UE
Measurement capability 2539.1.3.1 EN-DC: Monitoring of multiple layers
using gaps 2539.1.3.1a SA: Monitoring of multiple layers using gaps
2539.1.3.1b NE-DC: Monitoring of multiple layers using gaps 2549.1.3.1c
NR-DC: Monitoring of multiple layers using gaps 2549.1.3.2 EN-DC:
Maximum allowed layers for multiple monitoring 2559.1.3.2a SA: Maximum
allowed layers for multiple monitoring 2569.1.3.2b NE-DC: Maximum
allowed layers for multiple monitoring 2569.1.3.2c NR-DC: Maximum
allowed layers for multiple monitoring 2579.1A.3.2 Void 2589.1.3A UE
Measurement capability under operation mode with CCA 2589.1.3A.1 EN-DC:
Monitoring of multiple layers using gaps under CCA 2589.1.3A.1A SA:
Monitoring of multiple layers using gaps under CCA 2589.1.3A.2 EN-DC:
Maximum allowed layers for multiple monitoring under CCA 2589.1A.3.2a
Void 2599.1.3A.2A SA: Maximum allowed layers for multiple monitoring
under CCA 2599.1.4 Capabilities for Support of Event Triggering and
Reporting Criteria 2599.1.4.1 Introduction 2599.1.4.2 Requirements
2599.1.5 Carrier-specific scaling factor 2639.1.5.1 Monitoring of
multiple layers outside gaps 2639.1.5.1.1 EN-DC mode: carrier-specific
scaling factor for SSB-based, CSI-RS based L3 measurements and RSSI and
channel occupancy measurements performed outside gaps 2659.1.5.1.2 SA
mode: carrier-specific scaling factor for SSB-based, CSI-RS based L3
measurements and RSSI and channel occupancy measurements performed
outside gaps 2669.1.5.1.3 NR-DC mode: carrier-specific scaling factor
for SSB-based and CSI-RS based L3 measurements performed outside gaps
2679.1.5.1.4 NE-DC mode: carrier-specific scaling factor for SSB-based
and CSI-RS based measurements performed outside gaps 2689.1.5.2
Monitoring of multiple layers within gaps 2699.1.5.2.1 EN-DC mode:
carrier-specific scaling factor for SSB, CSI-RS-based L3 measurements
and RSSI and channel occupancy measurements performed within gaps
2709.1.5.2.2 SA mode: carrier-specific scaling factor for SSB,
CSI-RS-based L3 measurements and RSSI and channel occupancy measurements
performed within gaps 2729.1.5.2.3 NE-DC: carrier-specific scaling
factor for SSB-based and CSI-RS based L3 measurements performed within
gaps 2749.1.5.2.4 NR-DC: carrier-specific scaling factor for SSB-based
and CSI-RS-based L3 measurements performed within gaps 2769.1.5.2.5 SA
mode: carrier-specific scaling factor for PRS-based measurements
performed within gaps 2779.1.5.2.6 NE-DC: carrier-specific scaling
factor for PRS-based measurements performed within gaps 2789.1.5.2.7
NR-DC: carrier-specific scaling factor for PRS-based measurements
performed within gaps 2789.1.6 Minimum requirement at transitions 2789.2
NR intra-frequency measurements 2789.2.1 Introduction 2789.2.2
Requirements applicability 2799.2.3 Number of cells and number of SSB
2799.2.3.1 Requirements for FR1 2799.2.3.2 Requirements for FR2 2799.2.4
Measurement Reporting Requirements 2809.2.4.1 Periodic Reporting
2809.2.4.2 Event-triggered Periodic Reporting 2809.2.4.3 Event Triggered
Reporting 2809.2.5 Intrafrequency measurements without measurement gaps
2819.2.5.1 Intrafrequency cell identification 2819.2.5.2 Measurement
period 2839.2.5.3 Scheduling availability of UE during intra-frequency
measurements 2859.2.5.3.1 Scheduling availability of UE performing
measurements in TDD bands on FR1 2859.2.5.3.2 Scheduling availability of
UE performing measurements with a different subcarrier spacing than
PDSCH/PDCCH on FR1 2859.2.5.3.3 Scheduling availability of UE performing
measurements on FR2 2869.2.5.3.4 Scheduling availability of UE
performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA
2879.2.5.4 SFTD Measurements between PCell and PSCell 2879.2.5.4.1
Introduction 2879.2.5.4.2 SFTD Measurement delay 2879.2.5.4.3 SFTD
Measurement Reporting Delay 2889.2.6 Intra-frequency measurements with
measurement gaps 2889.2.6.1 Void 2889.2.6.2 Intra-frequency cell
identification 2889.2.6.3 Intrafrequency Measurement Period 2909.2A NR
intra-frequency measurements with CCA 2919.2A.1 Introduction 2919.2A.2
Requirements applicability 2919.2A.3 Number of cells and number of SSB
2929.2A.4 Measurement Reporting Requirements 2929.2A.5 Intra-frequency
measurements without measurement gaps 2929.2A.5.2 Measurement period
2959.2A.5.3 Scheduling availability of UE during intra-frequency
measurements 2969.2A.5.3.1 Scheduling availability of UE performing
measurements in TDD bands 2969.2A.5.3.2 Scheduling availability of UE
performing measurements with a different subcarrier spacing than
PDSCH/PDCCH 2979.2A.6 Intra-frequency measurements with measurement gaps
2979.2A.6.1 Intra-frequency cell identification 2979.2A.6.2
Intra-frequency Measurement Period 2989.2A.7 Intra-frequency RSSI and
Channel occupancy measurements 2999.2A.7.1 Intra-frequency RSSI
measurements 2999.2A.7.2 Intra-frequency Channel occupancy measurements
3009.2A.7.3 Scheduling restriction during RSSI and Channel Occupancy
measurements 3019.3 NR inter-frequency measurements 3019.3.1
Introduction 3019.3.2 Requirements applicability 3029.3.2.1 Void
3029.3.2.2 Void 3029.3.3 Number of cells and number of SSB 3029.3.3.1
Requirements for FR1 3029.3.3.2 Requirements for FR2 3029.3.4
Inter-frequency measurement with measurement gaps 3029.3.4.1 Void
3049.3.4.2 Void 3049.3.5 Inter-frequency measurements 3049.3.5.1 Void
3049.3.5.2 Void 3049.3.5.3 Void 3049.3.6 Inter-frequency measurements
reporting requirements 3049.3.6.1 Periodic Reporting 3049.3.6.2
Event-triggered Periodic Reporting 3059.3.6.3 Event-triggered Reporting
3059.3.7 Void 3059.3.8 Inter-frequency SFTD measurement requirements
3059.3.8.1 Introduction 3059.3.8.2 SFTD Measurement delay 3059.3.8.3
SFTD Measurement reporting delay 3069.3.9 Inter frequency measurements
without measurement gaps 3079.3.9.1 Inter frequency Cell identification
3079.3.9.2 Measurement period 3089.3.9.3 Scheduling availability of UE
during inter-frequency measurements 3099.3.9.3.1 Scheduling availability
of UE performing measurements in TDD bands on FR1 3099.3.9.3.2
Scheduling availability of UE performing measurements with a different
subcarrier spacing than PDSCH/PDCCH on FR1 3109.3.9.3.3 Scheduling
availability of UE performing measurements on FR2 3109.3.9.3.4
Scheduling availability of UE performing measurements on FR1 or FR2 in
case of FR1-FR2 inter-band CA 3109.3A NR inter-frequency measurements in
carrier frequencies with CCA 3119.3A.1 Introduction 3119.3A.2
Requirements applicability 3119.3A.3 Number of cells and number of SSB
3119.3A.3.1 Requirements 3119.3A.4 Inter-frequency cell identification
3129.3A.5 Inter-frequency measurements 3139.3A.6 NR Inter-frequency
measurements reporting requirements 3149.3A.6.1 Periodic Reporting
3149.3A.6.2 Event-triggered Periodic Reporting 3149.3A.6.3
Event-triggered Reporting 3149.3A.8 Inter-frequency RSSI measurements
3149.3A.9 Inter-frequency channel occupancy measurements 3159.4
Inter-RAT measurements 3159.4.1 Introduction 3159.4.2 NR − E-UTRAN FDD
measurements 3179.4.2.1 Introduction 3179.4.2.2 Requirements when no DRX
is used 3179.4.2.3 Requirements when DRX is used 3189.4.2.4 Measurement
reporting requirements 3199.4.2.4.1 Periodic Reporting 3199.4.2.4.2
Event-Triggered Periodic Reporting 3199.4.2.4.3 Event-Triggered
Reporting 3199.4.3 NR − E-UTRAN TDD measurements 3199.4.3.1 Introduction
3199.4.3.2 Requirements when no DRX is used 3199.4.3.3 Requirements when
DRX is used 3209.4.3.4 Measurement reporting requirements 3229.4.3.4.1
Periodic Reporting 3229.4.3.4.2 Event-Triggered Periodic Reporting
3229.4.3.4.3 Event-Triggered Reporting 3229.4.4 Inter-RAT RSTD
measurements 3229.4.4.1 NR − E-UTRAN FDD RSTD measurements 3229.4.4.1.1
Introduction 3229.4.4.1.2 Requirements 3239.4.4.2 NR − E-UTRAN TDD RSTD
measurements 3269.4.4.2.1 Introduction 3269.4.4.2.2 Requirements
3279.4.5 Inter-RAT E-CID measurements 3309.4.5.1 NR−E-UTRAN FDD E-CID
RSRP and RSRQ measurements 3309.4.5.1.1 Introduction 3309.4.5.1.2
Requirements 3309.4.5.1.3 Measurement Reporting Delay 3309.4.5.2
NR−E-UTRAN TDD E-CID RSRP and RSRQ measurements 3309.4.5.2.1
Introduction 3309.4.5.2.2 Requirements 3309.4.5.2.3 Measurement
Reporting Delay 3319.4.6 NR − UTRAN FDD measurements 3319.4.6.1
Introduction 3319.4.6.2 Requirements when no DRX is used 3319.4.6.3
Requirements when DRX is used 3329.4.7 NR -- E-UTRAN measurements with
autonomous gaps 3349.4.7.1 CGI identification of an E-UTRA cell with
autonomous gaps 3349.4.7.2 CGI reporting delay 3349.5 L1-RSRP
measurements for Reporting 3359.5.1 Introduction 3359.5.2 Requirements
applicability 3359.5.3 Measurement Reporting Requirements 3359.5.3.1
Periodic Reporting 3369.5.3.2 Semi-Persistent Reporting 3369.5.3.3
Aperiodic Reporting 3369.5.4 L1-RSRP measurement requirements 3369.5.4.1
SSB based L1-RSRP Reporting 3369.5.4.2 CSI-RS based L1-RSRP Reporting
3389.5.4A Void 3419.5.4A.1 Void 3419.5.5 Measurement restriction for
CSI-RS and SSB for L1-RSRP measurement 3419.5.5.1 Measurement
restriction for SSB based L1-RSRP 3419.5.5.2 Measurement restriction for
CSI-RS based L1-RSRP 3419.5.6 Scheduling availability of UE during
L1-RSRP measurement 3429.5.6.1 Scheduling availability of UE performing
L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1
3429.5.6.2 Scheduling availability of UE performing L1-RSRP measurement
with a different subcarrier spacing than PDSCH/PDCCH on FR1 3429.5.6.3
Scheduling availability of UE performing L1-RSRP measurement on FR2
3439.5.6.4 Scheduling availability of UE performing L1-RSRP measurement
on FR1 or FR2 in case of FR1-FR2 inter-band CA 3439.5A L1-RSRP
measurements for Reporting under CCA 3449.5A.1 Introduction 3449.5A.2
Requirements applicability 3449.5A.3 Measurement Reporting Requirements
3449.5A.3.1 Periodic Reporting 3449.5A.3.2 Semi-Persistent Reporting
3459.5A.3.3 Aperiodic Reporting 3459.5A.4 L1-RSRP measurement
requirements 3459.5A.4.1 SSB based L1-RSRP Reporting 3459.5A.5
Measurement restriction for L1-RSRP measurement 3469.5A.5.1 Measurement
restriction for SSB based L1-RSRP 3469.5A.6 Scheduling availability of
UE during L1-RSRP measurement 3469.5A.6.1 Scheduling availability of UE
performing L1-RSRP measurement with a same subcarrier spacing as
PDSCH/PDCCH 3469.5A.6.2 Scheduling availability of UE performing L1-RSRP
measurement with a different subcarrier spacing than PDSCH/PDCCH
3479.5A.6.3 Scheduling availability of UE performing L1-RSRP measurement
in case of FR1-FR2 inter-band CA 3479.6 NE-DC: Measurements 3479.6.1
Introduction 3479.6.2 SFTD Measurements 3479.6.2.1 Introduction
3479.6.2.2 SFTD Measurement requirements 3479.7 Cross Link Interference
measurements 3489.7.1 Introduction 3489.7.2 SRS-RSRP measurements
3489.7.2.1 Introduction 3489.7.2.2 Requirements applicability 3489.7.2.3
Measurement Reporting Requirements 3499.7.2.3.1 Periodic Reporting
3499.7.2.3.2 Event-triggered Periodic Reporting 3499.7.2.3.3 Event
Triggered Reporting 3499.7.2.4 Measurement capability 3499.7.2.5
SRS-RSRP measurement period 3499.7.3 CLI-RSSI measurements 3509.7.3.1
Introduction 3509.7.3.2 Requirements applicability 3509.7.3.3
Measurement Reporting Requirements 3509.7.3.3.1 Periodic Reporting
3509.7.3.3.2 Event-triggered Periodic Reporting 3509.7.3.3.3 Event
Triggered Reporting 3509.7.3.4 Measurement capability 3519.7.3.5
CLI-RSSI measurement period 3519.7.4 Scheduling availability of UE
during CLI measurements 3519.7.4.1 Scheduling availability of UE
performing measurement on FR1 3519.7.4.2 Scheduling availability of UE
performing measurement on FR2 3519.8 L1-SINR measurements for Reporting
3529.8.1 Introduction 3529.8.2 Requirements applicability 3529.8.3
Measurement Reporting Requirements 3539.8.3.1 Periodic Reporting
3539.8.3.2 Semi-Persistent Reporting 3539.8.3.3 Aperiodic Reporting
3549.8.4 L1-SINR measurement requirements 3549.8.4.1 L1-SINR reporting
with CSI-RS based CMR and no dedicated IMR configured 3549.8.4.3 L1-SINR
reporting with CSI-RS based CMR and dedicated IMR configured 3579.8.5
Measurement restriction for L1-SINR measurement 3599.8.5.1 Measurement
restriction if SSB configured for L1-SINR Measurement 3599.8.5.2
Measurement restriction if CSI-RS configured for L1-SINR measurement
3609.8.5.3 Measurement restriction if CSI-IM configured for L1-SINR
measurement 3609.8.6 Scheduling availability of UE during L1-SINR
measurement 3619.8.6.1 Scheduling availability of UE performing L1-SINR
measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1
3619.8.6.2 Scheduling availability of UE performing L1-SINR measurement
with a different subcarrier spacing than PDSCH/PDCCH on FR1 3619.8.6.4
Scheduling availability of UE performing L1-SINR measurement on FR1 or
FR2 in case of FR1-FR2 inter-band CA 3629.9 NR measurements for
positioning 3629.9.1 Introduction 3629.9.2 RSTD measurements 3639.9.2.1
Introduction 3639.9.2.2 Requirements Applicability 3639.9.2.3
Measurement Capability 3639.9.2.4 Measurement Reporting Requirements
3639.9.2.4.1 Void 3639.9.2.4.2 Void 3639.9.2.4.3 Void 3639.9.2.5
Measurements Period Requirements 3639.9.2.6 Void 3659.9.3 PRS-RSRP
measurements 3659.9.3.1 Introduction 3659.9.3.2 Requirements
applicability 3659.9.3.3 Measurement Capability 3669.9.3.4 Measurement
Reporting Requirements 3669.9.3.5 Measurement Period Requirements
3669.9.4 UE Rx-Tx time difference measurements 3689.9.4.1 Introduction
3689.9.4.2 Requirements Applicability 3689.9.4.3 Measurement Capability
3689.9.4.4 Measurement Reporting Requirements 3689.9.4.5 Measurement
Period Requirements 3689.9.5 NR E-CID measurements 3719.9.5.1
Introduction 3719.9.5.2 Measurement Requirements 3719.9.5.2.1
Intra-frequency Measurement Requirements 3719.9.5.2.2 Inter-frequency
Measurement Requirements 3719.9.5.2.3 Measurement Reporting Delay
3729.10 CSI-RS based L3 measurements 3729.10.1 Introduction 3729.10.2
CSI-RS based intra-frequency measurements 3729.10.2.1 Introduction
3729.10.2.2 Requirements applicability 3739.10.2.3 Number of cells and
number of CSI-RS 3749.10.2.3.1 Requirements for FR1 3749.10.2.3.2
Requirements for FR2 3749.10.2.4 Measurement Reporting Requirements
3749.10.2.4.1 Periodic Reporting 3759.10.2.4.2 Event-triggered Periodic
Reporting 3759.10.2.4.3 Event Triggered Reporting 3759.10.2.5
Intra-frequency measurements without measurement gaps 3759.10.2.6
Scheduling availability of UE during CSI-RS based intra-frequency
measurements 3769.10.2.6.1 Scheduling availability of UE performing
CSI-RS based measurements in TDD bands 3769.10.2.6.2 Scheduling
availability of UE performing CSI-RS based measurements in FR2 3779.10.3
CSI-RS based Inter-frequency measurements 3779.10.3.1 Introduction
3779.10.3.2 Requirements applicability 3779.10.3.3 Number of cells and
number of CSI-RS resources 3789.10.3.3.1 Requirements for FR1
3789.10.3.3.2 Requirements for FR2 3789.10.3.4 Measurements reporting
requirements 3789.10.3.4.1 Periodic Reporting 3789.10.3.4.2
Event-triggered Periodic Reporting 3789.10.3.4.3 Event-triggered
Reporting 3799.10.3.5 Inter frequency measurements with measurement gaps
3799.11 NR measurements with autonomous gaps 3809.11.1 Introduction
3809.11.2 CGI identification of an NR cell with autonomous gaps
3809.11.3 CGI reporting delay 38110 Measurement Performance requirements
38110.1 NR measurements 38110.1.1 Introduction 38110.1.2 Intra-frequency
RSRP accuracy requirements for FR1 38210.1.2.1 Intra-frequency SS-RSRP
accuracy requirements 38210.1.2.1.1 Absolute SS-RSRP Accuracy
38210.1.2.1.2 Relative SS-RSRP Accuracy 38310.1.2.2 Void 38410.1.2.3
Intra-frequency CSI-RSRP accuracy requirements 38410.1.2.3.1 Absolute
CSI-RSRP Accuracy 38410.1.2.3.2 Relative CSI-RSRP Accuracy 38510.1.2B
Intra-frequency RSRP accuracy requirements for FR1 for CA/DC Idle Mode
Measurements 38610.1.2B.1 Intra-frequency SS-RSRP accuracy requirements
38610.1.2B.1.1 Absolute SS-RSRP Accuracy 38610.1.3 Intra-frequency RSRP
accuracy requirements for FR2 38710.1.3.1 Intra-frequency SS-RSRP
accuracy requirements 38710.1.3.1.1 Absolute SS-RSRP Accuracy
38710.1.3.1.2 Relative SS-RSRP Accuracy 38810.1.3.2 Void 38910.1.3.3
Intra-frequency CSI-RSRP accuracy requirements 38910.1.3.3.1 Absolute
CSI-RSRP Accuracy 38910.1.3.3.2 Relative CSI-RSRP Accuracy 38910.1.3B
Intra-frequency RSRP accuracy requirements for FR2 for CA/DC Idle Mode
Measurements 39010.1.3B.1 Intra-frequency SS-RSRP accuracy requirements
39010.1.3B.1.1 Absolute SS-RSRP Accuracy 39110.1.4 Inter-frequency RSRP
accuracy requirements for FR1 39110.1.4.1 Inter-frequency SS-RSRP
accuracy requirements 39110.1.4.1.1 Absolute Accuracy of SS-RSRP in FR1
39110.1.4.1.2 Relative Accuracy of SS-RSRP in FR1 39210.1.4.2 Void
39310.1.4.3 Inter-frequency CSI-RSRP accuracy requirements 39310.1.4.3.1
Absolute Accuracy of CSI-RSRP in FR1 39310.1.4.3.2 Relative Accuracy of
CS-RSRP in FR1 39410.1.4B Inter-frequency RSRP accuracy requirements for
FR1 for CA/DC Idle Mode Measurements 39510.1.4B.1 Inter-frequency
SS-RSRP accuracy requirements 39510.1.4B.1.1 Absolute Accuracy of
SS-RSRP in FR1 39510.1.5 Inter-frequency RSRP accuracy requirements for
FR2 39610.1.5.1 Inter-frequency SS-RSRP accuracy requirements
39610.1.5.1.1 Absolute SS-RSRP Accuracy 39610.1.5.1.2 Relative SS-RSRP
Accuracy 39710.1.5.2 Void 39810.1.5.3 Inter-frequency CSI-RSRP accuracy
requirements 39810.1.5.3.1 Absolute CSI-RSRP Accuracy 39810.1.5.3.2
Relative CSI-RSRP Accuracy 39810.1.5B Inter-frequency RSRP accuracy
requirements for FR2 for CA/DC Idle Mode Measurements 39910.1.6 RSRP
Measurement Report Mapping 40010.1.7 Intra-frequency RSRQ accuracy
requirements for FR1 40210.1.7.1 Intra-frequency SS-RSRQ accuracy
requirements in FR1 40210.1.7.1.1 Absolute SS-RSRQ Accuracy in FR1
40210.1.7.2 Intra-frequency CSI-RSRQ accuracy requirements 40310.1.7.2.1
Absolute CSI-RSRQ Accuracy 40310.1.7B Intra-frequency RSRQ accuracy
requirements for FR1 for CA/DC Idle Mode Measurements 40410.1.7B.1
Intra-frequency SS-RSRQ accuracy requirements in FR1 40410.1.7B.1.1
Absolute SS-RSRQ Accuracy in FR1 40410.1.8 Intra-frequency RSRQ accuracy
requirements for FR2 40510.1.8.1 Intra-frequency SS-RSRQ accuracy
requirements in FR2 40510.1.8.1.1 Absolute SS-RSRQ Accuracy in FR2
40510.1.8.2 Intra-frequency CSI-RSRQ accuracy requirements 40610.1.8.2.1
Absolute CSI-RSRQ Accuracy 40610.1.8B Intra-frequency RSRQ accuracy
requirements for FR2 for CA/DC Idle Mode Measurements 40710.1.8B.1
Intra-frequency SS-RSRQ accuracy requirements in FR2 40710.1.8B.1.1
Absolute SS-RSRQ Accuracy in FR2 40710.1.9 Inter-frequency RSRQ accuracy
requirements for FR1 40810.1.9.1 Inter-frequency SS-RSRQ accuracy
requirements in FR1 40810.1.9.1.1 Absolute Accuracy of SS-RSRQ in FR1
40810.1.9.1.2 Relative Accuracy of SS-RSRQ in FR1 40910.1.9.2
Inter-frequency CSI-RSRQ accuracy requirements 41010.1.9.2.1 Absolute
CSI-RSRQ Accuracy 41010.1.9.2.2 Relative CSI-RSRQ Accuracy 41110.1.9B
Inter-frequency RSRQ accuracy requirements for FR1 for CA/DC Idle Mode
Measurements 41210.1.9B.1 Inter-frequency SS-RSRQ accuracy requirements
in FR1 41210.1.9B.1.1 Absolute Accuracy of SS-RSRQ in FR1 41210.1.10
Inter-frequency RSRQ accuracy requirements for FR2 41310.1.10.2
Inter-frequency CSI-RSRQ accuracy requirements 41510.1.10.2.1 Absolute
CSI-RSRQ Accuracy 41510.1.10.2.2 Relative CSI-RSRQ Accuracy 41510.1.10B
Inter-frequency RSRQ accuracy requirements for FR2 for CA/DC Idle Mode
Measurements 41610.1.10B.1 Inter-frequency SS-RSRQ accuracy requirements
in FR2 41610.1.10B.1.1 Absolute Accuracy of SS-RSRQ in FR2 41610.1.11
RSRQ report mapping 41710.1.12 Intra-frequency SINR accuracy
requirements for FR1 41810.1.12.2 Intra-frequency CSI-SINR accuracy
requirements in FR1 41810.1.12.2.1 Absolute CSI-SINR Accuracy in FR1
41810.1.13 Intra-frequency SINR accuracy requirements for FR2
41910.1.13.2 Intra-frequency CSI-SINR accuracy requirements in FR2
42010.1.13.2.1 Absolute CSI-SINR Accuracy in FR2 42010.1.14
Inter-frequency SINR accuracy requirements for FR1 42110.1.14.2
Inter-frequency CSI-SINR accuracy requirements in FR1 42310.1.14.2.1
Aboslute Accuracy of CSI-SINR in FR1 42310.1.15 Inter-frequency SINR
accuracy requirements for FR2 42510.1.15.2 Inter-frequency CSI-SINR
accuracy requirements in FR2 42710.1.15.2.1 Aboslute Accuracy of
CSI-SINR in FR2 42710.1.15.2.2 Relative Accuracy of CSI-SINR in FR2
42710.1.16 SINR report mapping 42810.1.17 Power Headroom 42910.1.18
P~CMAX,c,f~ 43010.1.19 L1-RSRP accuracy requirements for FR1 43010.1.20
L1-RSRP accuracy requirements for FR2 43410.1.21 SFTD accuracy
requirements 43710.1.22 CLI measurement accuracy requirements
44110.1.24.3.1 Absolute PRS-RSRP Measurement Report Mapping
44510.1.24.3.2 Differential Report Mapping for PRS-RSRP Measurement
44510.1.23 RSTD Measurements 44710.1.23.1 Introduction 44710.1.23.2
Measurement Accuracy Requirements 44810.1.23.3 Report mapping
45410.1.23.3.1 Absolute DL RSTD Measurement Reporting 45410.1.23.3.2
Differential Reporting for DL RSTD Measurement 45610.1.23.3.3 Additional
Path Report Mapping for DL RSTD 45810.1.24 PRS-RSRP Measurements
46010.1.24.1 Introduction 46010.1.24.2 Measurement Accuracy Requirements
46010.1.24.2.1 Absolute PRS RSRP accuracy 46010.1.24.3 Report mapping
46410.1.24.3.1 Absolute PRS-RSRP Measurement Report Mapping
46410.1.24.3.2 Differential Report Mapping for PRS-RSRP Measurement
46510.1.25 UE Rx-Tx Time Difference Measurements 46710.1.25.1
Introduction 46710.1.25.2 Measurement Accuracy Requirements 46810.1.25.3
Report mapping 47410.1.25.3.1 Absolute UE Rx-Tx Measurement Report
Mapping 47410.1.25.3.2 Differential UE Rx-Tx Measurement Report Mapping
47610.1.25.3.3 Additional Path Report Mapping for UE Rx-Tx Time
Difference 47710.1.26 FR2 P-MPR report 47910.1.26.1 Report mapping
47910.1.27 L1-SINR accuracy requirements for FR1 47910.1.27.1 L1-SINR
accuracy requirements with CSI-RS based CMR and no dedicated IMR
configured 47910.1.27.1.1 Absolute Accuracy 47910.1.27.1.2 Relative
Accuracy 48010.1.27.2 L1-SINR accuracy requirements with SSB based CMR
and dedicated IMR configured 48110.1.27.2.1 Absolute Accuracy
48110.1.27.2.2 Relative Accuracy 48210.1.27.3 L1-SINR accuracy
requirements with CSI-RS based CMR and dedicated IMR configured
48410.1.27.3.1 Absolute Accuracy 48410.1.27.3.2 Relative Accuracy
48610.1.28 L1-SINR accuracy requirements for FR2 48710.1.28.1 L1-SINR
accuracy requirements with CSI-RS based CMR and no dedicated IMR
configured 48710.1.28.1.1 Absolute Accuracy 48710.1.28.1.2 Relative
Accuracy 48810.1.28.2 L1-SINR accuracy requirements with SSB based CMR
and dedicated IMR configured 48910.1.28.2.1 Absolute Accuracy
48910.1.28.2.2 Relative Accuracy 49010.1.28.3 L1-SINR accuracy
requirements with CSI-RS based CMR and dedicated IMR configured
49110.1.28.3.1 Absolute Accuracy 49110.1.28.3.2 Relative Accuracy
49210.1.29 Intra-frequency RSRQ accuracy requirements under CCA
49410.1.29.1 Intra-frequency SS-RSRQ accuracy requirements in FR1
49410.1.29.1.1 Absolute SS-RSRQ Accuracy 49410.1.30 Inter-frequency RSRQ
accuracy requirements under CCA 49510.1.30.1 Inter-frequency SS-RSRQ
accuracy requirements in FR1 49510.1.30.1.1 Aboslute Accuracy of SS-RSRQ
49510.1.30.1.2 Relative Accuracy of SS-RSRQ 49510.1.31 Intra-frequency
SINR accuracy requirements under CCA 49610.1.32 Inter-frequency SINR
accuracy requirements under CCA 49710.1.33 L1-RSRP accuracy requirements
under CCA 49810.1.34 RSSI measurements under CCA 49910.1.34.1
Intra-frequency absolute RSSI measurement accuracy requirements in FR1
49910.1.34.2 Inter-frequency absolute RSSI measurement accuracy
requirements in FR1 50010.1.34.3 RSSI measurement report mapping
50010.1.35 Channel occupancy measurements under CCA 50010.1.35.1
Intra-frequency channel occupancy measurement accuracy requirements in
FR1 50010.1.35.2 Inter-frequency channel occupancy measurement accuracy
requirements in FR1 50110.1.36 Intra-frequency RSRP accuracy
requirements under CCA 50110.1.36.1 Intra-frequency SS-RSRP accuracy
requirements in FR1 50110.1.36.1.1 Absolute SS-RSRP Accuracy
50110.1.36.1.2 Relative SS-RSRP Accuracy 50210.1.37 Inter-frequency RSRP
accuracy requirements under CCA 50210.1.37.1 Inter-frequency SS-RSRP
accuracy requirements in FR1 50210.1.37.1.1 Absolute Accuracy of SS-RSRP
50210.1.37.1.2 Relative Accuracy of SS-RSRP 50310.2 E-UTRAN measurements
50310.2.1 Introduction 50310.2.2 E-UTRAN RSRP measurements 50410.2.3
E-UTRAN RSRQ measurements 50410.2.4 E-UTRAN RSTD measurements 50410.2.5
E-UTRAN RS-SINR measurements 50510.2.6 E-UTRAN RSRP measurements for
CA/DC Idle Mode Measurements 50510.2.7 E-UTRAN RSRQ measurements for
CA/DC Idle Mode Measurements 50510.3 UTRAN FDD Measurements 50510.3.1
UTRAN FDD CPICH RSCP 50610.3.2 UTRAN FDD CPICH Ec/No 50610.4 V2X
measurements 50710.4.1 Introduction 50710.4.2 Intra-frequency PSBCH-RSRP
accuracy requirements for FR1 50710.4.2.1 PSBCH-RSRP Absolute Accuracy
50710.4.2.2 PSBCH-RSRP Relative Accuracy 50710.4.3 Intra-Frequency
SL-RSSI Measurement Accuracy Requirements for FR1 50810.4.3.1 Absolute
SL-RSSI Accuracy 50810.4.4 Intra-Frequency L1 SL-RSRP Measurement
Accuracy Requirements for FR1 50910.4.4.1 Absolute L1 SL-RSRP Accuracy
50911 Void 51012 V2X Requirements 51012.1 Introduction 51012.2 UE
Transmit Timing 51012.2.1 Introduction 51012.2.2 GNSS as synchronization
reference source 51012.2.3 NR Cell as synchronization reference source
51112.2.4 E-URTAN Cell as synchronization reference source 51112.2.5
SyncRef UE as synchronization reference source 51112.3 Initiation/Cease
of SLSS Transmissions 51212.3.1 Introduction 51212.3.1.1
Initiation/Cease of SLSS transmissions with NR cell as synchronization
reference source 51212.3.1.2 Initiation/Cease of SLSS transmissions with
EUTRAN cell as synchronization reference source 51312.3.1.3
Initiation/Cease of SLSS transmissions with GNSS as synchronization
reference source 51412.3.1.4 Initiation/Cease of SLSS transmissions with
SyncRef UE as synchronization reference source 51412.4 Selection /
Reselection of V2X Synchronization Reference Source 51412.5 L1 SL-RSRP
measurements 51512.5.1 Introduction 51512.5.2 SL-RSRP measurements
51512.6 Congestion Control measurements 51612.7 Interruption 51612.7.1
Interruptions to WAN due to V2X Sidelink Communication 51612.7.2 V2X
Sidelink Communication Dropping due to synchronization source change
51612.7.3 Interruptions to WAN due to switching between E-UTRA V2X
Sidelink and NR V2X Sidelink 51812.8 Reliability of GNSS signal 51812.9
Scheduling availability 51912.9.1 Scheduling availability of UE
switching between E-UTRA sidelink and NR sidelink 51913 Measurement
Performance Requirements for NR gNB 51913.1 UL-RTOA 51913.1.1 Report
mapping 51913.2 gNB Rx-Tx time difference 52113.2.1 Report mapping
52113.2.2 Measurement Accuracy Requirements 52313.2.2.1 Introduction
52313.2.2.2 Requirements 52413.3 UL SRS RSRP measurement 52513.3.1
Report mapping 52513.3.2 Measurement accuracy requirements 52513.3.2.1
Introduction 52513.3.2.2 Requirements 52613.4 AoA/ZoA 52713.4.1 Report
mapping 527Annex A (normative): Test Cases 423A.1 Purpose of annex
423A.2 Requirement classification for statistical testing 423A.2.1 Types
of requirements in TS 38.133 423A.2.1.1 Time and delay requirements on
UE higher layer actions 423A.2.1.2 Measurements of power levels,
relative powers and time 423A.2.1.3 Implementation requirements
424A.2.1.4 Physical layer timing requirements 424A.2.1.5 Requirements
under CCA 424A.3 RRM test configurations 425A.3.1 Reference measurement
channels 425A.3.1.1 PDSCH 425A.3.1.1.1 FDD 425A.3.1.1.2 TDD 426A.3.1A
Reference measurement channels under CCA 429A.3.1A.1 PDSCH 429A.3.1A.1.1
TDD 429A.3.1A.2 CORESET for RMSI scheduling 430A.3.1A.2.1 TDD
430A.3.1A.3 CORESET for RMC scheduling 431A.3.1A.3.1 TDD 431A.3.1A.4 TDD
UL/DL configuration 432A.3.1A.5 RMC burst transmission model 432A.3.1.2
CORESET for RMSI scheduling 433A.3.1.2.1 FDD 433A.3.1.2.2 TDD 434A.3.1.3
CORESET for RMC scheduling 437A.3.1.3.1 FDD 437A.3.1.3.2 TDD 438A.3.1.4
TDD UL/DL configuration 441A.3.2 OFDMA channel noise generator (OCNG)
442A.3.2.1 Generic OFDMA Channel Noise Generator (OCNG) 442A.3.2.1.1
OCNG pattern 1: Generic OCNG pattern for all unused REs 442A.3.2.1.2
OCNG pattern 2: Generic OCNG pattern for all unused REs for 2AoA setup
443A.3.2.1.3 OCNG pattern 3: Generic OCNG pattern for unused REs in the
same bandwidth as CORESET 443A.3.2.1.4 OCNG pattern 4: Generic OCNG
pattern for all unused REs outside SSB slot(s) 444A.3.2.2 Void 445A.3.3
Reference DRX configurations 445A.3.3.1 DRX Configuration 1: DRX cycle =
40 ms and TAT = 500 ms 445A.3.3.2 DRX Configuration 2: DRX cycle = 640
ms and TAT = 500 ms 445A.3.3.3 DRX Configuration 3: DRX cycle = 40 ms
and TAT = Infinity 445A.3.3.4 DRX Configuration 4: DRX cycle = 160 ms
and TAT = Infinity 446A.3.3.5 DRX Configuration 5: DRX cycle = 320 ms
and TAT = Infinity 446A.3.3.6 DRX Configuration 6: DRX cycle = 320 ms
and TAT = 500 ms 446A.3.3.7 DRX Configuration 7: DRX cycle = 640 ms and
TAT = Infinity 447A.3.3.8 DRX Configuration 8: DRX cycle = 320 ms and
TAT = Infinity 447A.3.3.9 DRX Configuration 9: DRX cycle = 40 ms and TAT
= 500 ms 447A.3.3.10 DRX Configuration 10: DRX cycle = 640 ms and TAT =
500 ms 448A.3.3.11 DRX Configuration 11: DRX cycle = 20 ms and TAT =
Infinity 448A.3.3.12 DRX Configuration 12: DRX cycle = 640 ms and TAT =
Infinity 448A.3.4 Test Cases with Different Channel Bandwidths
448A.3.4.1 Test Cases with Different E-UTRA Channel Bandwidths
448A.3.4.1.1 Introduction 448A.3.4.1.2 Principle of testing 449A.3.5
Test Cases for Synchronous and Asynchronous DC Operations 449A.3.5.1
EN-DC Test Cases for Synchronous and Asynchronous EN-DC Operations
449A.3.5.1.1 Introduction 449A.3.5.1.2 Principle of Testing 449A.3.6
Antenna configurations 449A.3.6.1 Antenna configurations for FR1
449A.3.6.1.1 Antenna connection for 4 Rx capable UEs 449A.3.6.1.1.1
Introduction 449A.3.6.1.1.2 Principle of testing 449A.3.6.2 Antenna
configurations for FR2 452A.3.6A Antenna configurations with unlicensed
bands 452A.3.6A.1 Antenna configurations for FR1 452A.3.6A.1.1 Antenna
connection for 4 Rx capable UEs 452A.3.6A.1.1.1 Introduction
452A.3.6A.1.1.2 Principle of testing 452A.3.7 EN-DC test setup
454A.3.7.1 Introduction 454A.3.7.2 E-UTRAN Serving Cell Parameters
454A.3.7.2.1 E-UTRAN Serving Cell Parameters for Tests with NR Cell(s)
in FR1 454A.3.7.2.2 E-UTRAN Serving Cell Parameters for Tests with NR
Cell(s) in FR2 455A.3.7A NR FR1-FR2 test setup 456A.3.7B EN-DC test
setup with unlicensed bands 457A.3.7B.1 Introduction 457A.3.7B.2 E-UTRAN
Serving Cell Parameters 457A.3.7B.2.1 E-UTRAN Serving Cell Parameters
for Tests with NR Cell(s) under CCA in FR1 457A.3.7C LTE-FR1/FR2 test
setup 458A.3.7D NE-DC test setup 458A.3.7D.1 Introduction 458A.3.7D.2
E-UTRAN Serving Cell Parameters 458A.3.7D.2.1 E-UTRAN Serving Cell
Parameters for Tests with NR Cell(s) in FR1 458A.3.7D.2.2 E-UTRAN
Serving Cell Parameters for Tests with NR Cell(s) in FR2 458A.3.8 PRACH
configurations 458A.3.8.1 Introduction 458A.3.8.2 PRACH configurations
in FR1 459A.3.8.2.1 FR1 PRACH configuration 1 459A.3.8.2.2 FR1 PRACH
configuration 2 459A.3.8.2.3 FR1 PRACH configuration 3 460A.3.8.2.4 FR1
PRACH configuration 4 461A.3.8.3 PRACH configurations in FR2
462A.3.8.3.1 FR2 PRACH configuration 1 462A.3.8.3.2 FR2 PRACH
configuration 2 463A.3.8.3.3 FR2 PRACH configuration 3 464A.3.8.3.4 FR2
PRACH configuration 4 465A.3.8A PRACH configurations under CCA
466A.3.8A.1 Introduction 466A.3.8A.2 PRACH configurations in FR1
466A.3.8A.2.1 FR1 PRACH configuration 1 under CCA 466A.3.8A.2.2 FR1
PRACH configuration 2 under CCA 467A.3.9 BWP configurations 468A.3.9.1
Introduction 468A.3.9.2 Downlink BWP configurations 469A.3.9.2.1 Initial
BWP 469A.3.9.2.2 Dedicated BWP 469A.3.9.3 Uplink BWP configurations
469A.3.9.3.1 Initial BWP 469A.3.9.3.2 Dedicated BWP 470A.3.10 SSB
Configurations 470A.3.10.1 SSB Configurations for FR1 470A.3.10.1.1 SSB
pattern 1 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz
470A.3.10.1.5 SSB pattern 5 in FR1: SSB allocation for SSB SCS=15 kHz
starting from odd SFN in 10 MHz 472A.3.10A SSB Configurations under CCA
477A.3.10A.1 SSB Configurations under CCA for FR1 477A.3.10A.1.1 SSB
pattern 1 under CCA for semi-static channel access: SSB allocation for
SSB SCS=30kHz in 40MHz 477A.3.10A.1.2 SSB pattern 2 under CCA for
dynamic channel access: SSB allocation for SSB SCS=30kHz in 40MHz
478A.3.10A.1.3 SSB pattern 3 under CCA for semi-static channel access:
SSB allocation for SSB SCS=30 kHz in 40 MHz 478A.3.10A.1.4 SSB pattern 4
under CCA for dynamic channel access: SSB allocation for SSB SCS=30 kHz
in 40 MHz 479A.3.11 SMTC Configurations 479A.3.11.1 SMTC pattern 1: SMTC
period = 20 ms with SMTC duration = 1 ms 479A.3.11.2 SMTC pattern 2:
SMTC period = 20 ms with SMTC duration = 5 ms 479A.3.11.3 SMTC pattern
3: SMTC period = 160 ms with SMTC duration = 1 ms 480A.3.11.4 SMTC
pattern 4: SMTC period = 20 ms with SMTC duration = 1 ms 480A.3.11.5
SMTC pattern 5: SMTC period = 20 ms with SMTC duration = 5 ms
480A.3.11.6 SMTC pattern 6: SMTC period = 20 ms with SMTC duration = 5
ms 480A.3.12 Test Cases with Different CC Configurations 480A.3.12.1
EN-DC Test Cases with Different EN-DC Configurations 480A.3.12.1.1
Introduction 480A.3.12.1.2 Principle of testing 481A.3.12.2 Carrier
Aggregation Test Cases with Different CA Configurations 481A.3.12.2.1
Introduction 481A.3.12.2.2 Principle of testing 481A.3.13 Test Cases in
SA and EN-DC Operations 481A.3.13.1 Introduction 481A.3.13.2 Principle
of Testing 481A.3.13A Test Cases involving E-UTRA/FR1 and FR2 carriers
482A.3.13A.1 Introduction 482A.3.13A.2 Principle of Testing in EN-DC
482A.3.13A.3 Principle of Testing in SA 482A.3.13B Test Cases for EN-DC
and NE-DC Operations 483A.3.13B.1 Active BWP switch Test Cases for EN-DC
and NE-DC Operations 483A.3.13B.1.1 Introduction 483A.3.13B.1.2
Principle of Testing 483A.3.13B.2 SFTD accuracy Test Cases for EN-DC and
NE-DC Operations 483A.3.13B.2.1 Introduction 483A.3.13B.2.2 Principle of
Testing 483A.3.14 CSI-RS configurations 484A.3.14.1 FDD 484A.3.14.2 TDD
486A.3.15 Angle of Arrival (AoA) for FR2 RRM test cases 491A.3.15.1
Setup 1: Single AoA in Rx beam peak direction 491A.3.15.2 Setup 2:
Single AoA in non Rx beam peak direction 491A.3.15.2.1 Setup 2a: Single
AoA in non Rx beam peak direction without change in direction
491A.3.15.2.2 Setup 2b: Single AoA in non Rx beam peak direction with
change in direction 492A.3.15.3 Setup 3: 2 AoAs 492A.3.15.4 Setup 4: 2
AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak
492A.3.15.4.1 Setup 4a: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in
non Rx beam peak without change in direction 492A.3.15.4.2 Setup 4b: 2
AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak with change
in direction 492A.3.16 TCI State Configuration 493A.3.16.1 Introduction
493A.3.16.2 TCI states 493A.3.17 Configurations of CSI-RS for tracking
493A.3.17.1 Configuration of CSI-RS for tracking for FR1 493A.3.17.1.1
FDD 493A.3.17.1.2 TDD 494A.3.17.2 Configuration of CSI-RS for tracking
for FR2 495A.3.17.2.1 TDD 495A.3.18 Additional definitions related to
OTA testing for FR2 RRM test cases 496A.3.18.1 Introduction 496A.3.18.2
PRACH Power Measurement 496A.3.19 Test applicability for DAPS handover
496A.3.19.1 Introduction 496A.3.19.2 Principle of testing 496A.3.20 MsgA
configurations 497A.3.20.1 Introduction 497A.3.20.2 MsgA configurations
in FR1 497A.3.20.2.1 FR1 MsgA configuration 1 497A.3.20.2.2 FR1 MsgA
configuration 2 498A.3.20.3 MsgA configurations in FR2 500A.3.20.3.1 FR2
MsgA configuration 1 500A.3.20.3.2 FR2 MsgA configuration 2 501A.3.20A
MsgA configurations under CCA 503A.3.20A.1 Introduction 503A.3.20A.2
MsgA configurations in FR1 503A.3.20A.2.1 FR1 MsgA configuration 1 under
CCA 503A.3.20A.2.2 FR1 MsgA configuration 2 under CCA 504A.3.21 V2X
sidelink communication 507A.3.21.1 Introduction 507A.3.21.2 Reference
resource pool configurations for V2X Sidelink Communication 507A.3.21.3
Reference measurement channels for V2X Sidelink Communication 511A.3.22
CSI-IM configurations 511A.3.22.1 FDD 511A.3.22.2 TDD 512A.3.23 Spatial
Relation Configuration 514A.3.23.1 Introduction 514A.3.23.2 Spatial
Relation 514A.3.24 SRS configuration 515A.3.25 Channel bandwidth (CBW)
configurations 517A.3.25.1 DL UE specific CBW 518A.3.26 CCA model
518A.3.26.1 Introduction 518A.3.26.2 CCA model for operation on a
carrier frequency with CCA in FR1 518A.3.26.2.1 DL CCA model
518A.3.26.2.2 UL CCA model 520A.3.27 Test Cases with at Least One Cell
on a Carrier Frequency with CCA 520A.3.27.1 Introduction 521A.3.27.2 NR
Standalone Tests with NR SCell under CCA and All Other NR Cells in FR1
521A.3.27.3 EN-DC Tests with NR PSCell under CCA and Other NR Cells in
FR1 521A.3.27.4 NR Standalone Tests with NR PCell under CCA and Other NR
Cells in FR1 521A.3.27.5 E-UTRA Standalone Tests with at Least One NR
Cell under CCA 521A.3.28 Discovery Burst Transmission Window
configuration under CCA 521A.3.28.1 DBT Window pattern 1: DBT Window
period = 20 ms with DBT Window duration = 1 ms 521A.3.29 Testing
principles for UE capable of only NR bands with shared spectrum access
521A.3.29.1 Introduction 521A.3.29.2 Principle of testing for UE capable
of EN-DC with only NR bands with shared spectrum access 522A.3.29.3
Principle of testing for UE capable of SA operation with only NR bands
with shared spectrum access 522A.3.30 CSI-RS configurations for RRM
523A.3.30.1 FDD 523A.3.30.2 TDD 524A.3.31 PRS Configurations
526A.3.31.1. PRS Configurations for FR1 526A.3.31.1.1. PRS pattern 1 in
FR1: SCS=15 KHz 526A.3.31.1.2. PRS pattern 2 in FR1: SCS=30 KHz
527A.3.31.2. PRS Configurations for FR2 527A.3.31.2.1. PRS pattern 1 in
FR2: SCS=120 KHz 527A.4 EN-DC tests with all NR cells in FR1 528A.4.1
Void 528A.4.2 Void 528A.4.3 RRC\_CONNECTED state mobility 528A.4.3.1
Void 528A.4.3.2 RRC Connection Mobility Control 528A.4.3.2.1 Void
528A.4.3.2.2 Random Access 528A.4.3.2.2.1 4-step RA type contention
based random access test in FR1 for PSCell in EN-DC 528A.4.3.2.2.2
4-step RA type non-contention based random access test in FR1 for PSCell
in EN-DC 532A.4.3.2.2.3 2-step RA type contention based random access
test in FR1 for PSCell in EN-DC 536A.4.3.2.2.4 2-step RA type
non-contention based random access test in FR1 for PSCell in EN-DC
540A.4.3.2.3 Void 544A.4.4 Timing 544A.4.4.1 UE transmit timing
544A.4.4.1.1 NR UE Transmit Timing Test for FR1 544A.4.4.1.1.1 Test
Purpose and environment 544A.4.4.1.1.2 Test requirements 548A.4.4.2 UE
timer accuracy 548A.4.4.3 Timing advance 548A.4.4.3.1 EN-DC FR1 timing
advance adjustment accuracy 548A.4.4.3.1.1 Test Purpose and Environment
548A.4.4.3.1.2 Test Parameters 548A.4.4.3.1.3 Test Requirements 552A.4.5
Signaling characteristics 552A.4.5.1 Radio link Monitoring 552A.4.5.1.1
Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with
SSB-based RLM RS in non-DRX mode 553A.4.5.1.1.1 Test Purpose and
Environment 553A.4.5.1.1.2 Test Requirements 557A.4.5.1.2 Radio Link
Monitoring In-sync Test for FR1 PSCell configured with SSB-based RLM RS
in non-DRX mode 557A.4.5.1.2.1 Test Purpose and Environment
557A.4.5.1.2.2 Test Requirements 563A.4.5.1.3 Radio Link Monitoring
Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in DRX
mode 563A.4.5.1.3.1 Test Purpose and Environment 563A.4.5.1.3.2 Test
Requirements 569A.4.5.1.4 Radio Link Monitoring In-sync Test for FR1
PSCell configured with SSB-based RLM RS in DRX mode 569A.4.5.1.4.1 Test
Purpose and Environment 569A.4.5.1.4.2 Test Requirements 574A.4.5.1.5
EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured
with CSI-RS-based RLM in non-DRX mode 574A.4.5.1.5.1 Test Purpose and
Environment 574A.4.5.1.5.2 Test Requirements 580A.4.5.1.6 EN-DC Radio
Link Monitoring In-sync Test for FR1 PSCell configured with CSI-RS-based
RLM in non-DRX mode 580A.4.5.1.6.1 Test Purpose and Environment
580A.4.5.1.6.2 Test Requirements 586A.4.5.1.7 EN-DC Radio Link
Monitoring Out-of-sync Test for FR1 PSCell configured with CSI-RS-based
RLM in DRX mode 586A.4.5.1.7.1 Test Purpose and Environment
586A.4.5.1.7.2 Test Requirements 591A.4.5.1.8 EN-DC Radio Link
Monitoring In-sync Test for FR1 PSCell configured with CSI-RS-based RLM
in DRX mode 592A.4.5.1.8.1 Test Purpose and Environment 592A.4.5.1.8.2
Test Requirements 597A.4.5.2 Interruption 597**A.4.5.2.1** E-UTRAN -- NR
FR1 interruptions at transitions between active and non-active during
DRX in synchronous EN-DC 597A.4.5.2.1.1 Test Purpose and Environment
597A.4.5.2.1.2 Test Requirements 601**A.4.5.2.2** E-UTRAN -- NR FR1
interruptions at transitions between active and non-active during DRX in
asynchronous EN-DC 601A.4.5.2.2.1 Test Purpose and Environment
601A.4.5.2.2.2 Test Requirements 605**A.4.5.2.3** E-UTRAN -- NR FR1
interruptions during measurements on deactivated NR SCC in synchronous
EN-DC 605A.4.5.2.3.1 Test Purpose and Environment 605A.4.5.2.3.2 Test
Requirements 610A.4.5.2.4 E-UTRAN -- NR FR1 interruptions during
measurements on deactivated NR SCC in asynchronous EN-DC 611A.4.5.2.4.1
Test Purpose and Environment 611A.4.5.2.4.2 Test Requirements
615**A.4.5.2.5** E-UTRAN -- NR FR1 interruptions during measurements on
deactivated E-UTRAN SCC in synchronous EN-DC 616A.4.5.2.5.1 Test Purpose
and Environment 616A.4.5.2.5.2 Test Requirements 620**A.4.5.2.6**
E-UTRAN -- NR FR1 interruptions during measurements on deactivated
E-UTRAN SCC in asynchronous EN-DC 620A.4.5.2.6.1 Test Purpose and
Environment 620A.4.5.2.6.2 Test Requirements 624A.4.5.2.7 Void
624**A.4.5.2.8** **E-UTRAN - NR FR1 i**nterruptions at NR SRS carrier
based switching in asynchronous EN-DC 624A.4.5.2.8.1 Test Purpose and
Environment 624A.4.5.2.8.2 Test Requirements 627**A.4.5.2.9** E-UTRAN --
NR interruptions at E-UTRA SRS carrier based switching 628A.4.5.2.9.1
Test Purpose and Environment 628A.4.5.2.9.2 Test Requirements 632A.4.5.3
SCell Activation and Deactivation Delay 633A.4.5.3.1 SCell Activation
and deactivation of known SCell in FR1 for 160ms SCell measurement cycle
633A.4.5.3.1.1 Test Purpose and Environment 633A.4.5.3.1.2 Test
Requirements 639A.4.5.3.2 SCell Activation and deactivation of known
SCell in FR1 for 640ms SCell measurement cycle 640A.4.5.3.2.1 Test
Purpose and Environment 640A.4.5.3.2.2 Test Requirements 640A.4.5.3.3
SCell Activation and deactivation of unknown SCell in FR1 640A.4.5.3.3.1
Test Purpose and Environment 640A.4.5.3.3.2 Test Requirements
641A.4.5.3.4 SCell Activation and deactivation of multiple unknown
SCells in FR1 with single activation/deactivation command 642A.4.5.3.4.1
Test Purpose and Environment 642A.4.5.3.4.2 Test Requirements
646A.4.5.3.5 Direct SCell activation at SCell addition of known SCell in
FR1 646A.4.5.3.5.1 Test Purpose and Environment 646A.4.5.3.5.2 Test
Requirements 654A.4.5.4 UE UL carrier RRC reconfiguration Delay
655A.4.5.4.1 UE UL carrier RRC reconfiguration Delay 655A.4.5.4.1.1 Test
Purpose and Environment 655A.4.5.4.1.2 Test Requirements 663A.4.5.5 Beam
Failure Detection and Link recovery procedures 664A.4.5.5.1 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 PSCell configured with
SSB-based BFD and LR in non-DRX mode 664A.4.5.5.1.1 Test Purpose and
Environment 664A.4.5.5.1.2 Test Requirements 669A.4.5.5.2 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 PSCell configured with
SSB-based BFD and LR in DRX mode 670A.4.5.5.2.1 Test Purpose and
Environment 670A.4.5.5.2.2 Test Requirements 675A.4.5.5.3 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 PSCell configured with
CSI-RS-based BFD and LR in non-DRX mode 676A.4.5.5.3.1 Test Purpose and
Environment 676A.4.5.5.3.2 Test Requirements 681A.4.5.5.4 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 PSCell configured with
CSI-RS-based BFD and LR in DRX mode 682A.4.5.5.4.1 Test Purpose and
Environment 682A.4.5.5.4.2 Test Requirements 687A.4.5.5.5 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 SCell configured with
CSI-RS-based BFD and SSB-based LR in non-DRX mode 688A.4.5.5.5.1 Test
Purpose and Environment 688A.4.5.5.5.2 Test Requirements 693A.4.5.5.6
EN-DC Beam Failure Detection and Link Recovery Test for FR1 SCell
configured with CSI-RS-based BFD and SSB-based LR in DRX mode
694A.4.5.5.6.1 Test Purpose and Environment 694A.4.5.5.6.2 Test
Requirements 700A.4.5.6 Active BWP switch 701A.4.5.6.1 DCI-based and
Timer-based Active BWP Switch 701A.4.5.6.1.1 E-UTRAN -- NR PSCell FR1 DL
active BWP switch in non-DRX in synchronous EN-DC 701A.4.5.6.1.2 E-UTRAN
-- NR PSCell FR1 DL active BWP switch with FR1 SCell in non-DRX in
synchronous EN-DC 706A.4.5.6.2 RRC-based Active BWP Switch 712A.4.5.6.3
Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs
716A.4.5.6.3.1 Simultaneous E-UTRAN -- NR PSCell FR1 DL active BWP
switch in non-DRX in EN-DC on multiple CCs 716A.4.5.6.3.1.2 Test
Requirements 722A.4.5.6.4 SCell dormancy switch 722A.4.5.6.4.1 E-UTRAN
-- NR FR1 PSCell SCell dormancy switch of single FR1 SCell outside
active time 722A.4.5.6.4.1.1 Test Purpose and Environment
722A.4.5.6.4.1.2 Test Requirements 730A.4.5.6.4.2 E-UTRAN -- NR FR1
PSCell SCell dormancy switch of two FR1 SCells inside active time
730A.4.5.6.4.2.1 Test Purpose and Environment 730A.4.5.6.4.2.2 Test
Requirements 742A.4.5.6.5 Simultaneous RRC-based Active BWP Switch on
multiple CCs 743A.4.5.6.5.1 E-UTRAN -- NR PSCell FR1 DL active BWP
switch in non-DRX in synchronous EN-DC on multiple CCs 743A.4.5.7 PSCell
addition and release delay 747A.4.5.7.1 Addition and Release Delay of
known NR PSCell 747A.4.5.7.1.1 Test purpose and environment
747A.4.5.7.1.2 Test Requirements 751A.4.5.8 DL Interruptions at
switching between two uplink carriers 752A.4.5.8.1 Test Purpose and
Environment 752A.4.5.8.2 Test Requirements 755A.4.5.9 UE specific CBW
change 756A.4.5.9.1 UE specific CBW change on FR1 NR PSCell with non-DRX
in synchronous EN- DC 756A.4.5.9.1.1 Test Purpose and Environment
756A.4.5.9.1.2 Test Requirements 760A.4.6 Measurement procedure
760A.4.6.1 Intra-frequency Measurements 760A.4.6.1.1 EN-DC event
triggered reporting tests without gap under non-DRX 760A.4.6.1.1.1 Test
purpose and Environment 760A.4.6.1.1.2 Test parameters 760A.4.6.1.1.3
Test Requirements 764A.4.6.1.2 EN-DC event triggered reporting tests
without gap under DRX 764A.4.6.1.2.1 Test purpose and Environment
764A.4.6.1.2.2 Test parameters 764A.4.6.1.2.2 Test Requirements
768A.4.6.1.3 EN-DC event triggered reporting tests with per-UE gaps
under non-DRX 768A.4.6.1.3.1 Test purpose and Environment 768A.4.6.1.3.2
Test parameters 768A.4.6.1.3.3 Test Requirements 772A.4.6.1.4 EN-DC
event triggered reporting tests with per-UE gaps under DRX
772A.4.6.1.4.1 Test purpose and Environment 772A.4.6.1.4.2 Test
parameters 772A.4.6.1.4.3 Test Requirements 776A.4.6.1.5 EN-DC event
triggered reporting tests without gap under non-DRX with SSB index
reading 776A.4.6.1.5.1 Test purpose and Environment 776A.4.6.1.5.2 Test
parameters 776A.4.6.1.5.3 Test Requirements 778A.4.6.1.6 EN-DC event
triggered reporting tests with SSB index reading with per-UE gaps
779A.4.6.1.6.1 Test purpose and Environment 779A.4.6.1.6.2 Test
parameters 779A.4.6.1.6.3 Test Requirements 781A.4.6.1.7 EN-DC event
triggered reporting tests under DRX for UE configured with
highSpeedMeasFlag-r16 782A.4.6.1.7.1 Test purpose and Environment
782A.4.6.1.7.2 Test parameters 782A.4.6.1.7.3 Test Requirements
786A.4.6.2 Inter-frequency Measurements 786A.4.6.2.1 EN-DC event
triggered reporting tests for FR1 cell without SSB time index detection
when DRX is not used 786A.4.6.2.1.1 Test Purpose and Environment
786A.4.6.2.1.2 Test Requirements 790A.4.6.2.2 EN-DC event triggered
reporting tests for FR1 cell without SSB time index detection when DRX
is used 790A.4.6.2.2.1 Test Purpose and Environment 790A.4.6.2.2.2 Test
Requirements 794A.4.6.2.3 Void 794A.4.6.2.4 Void 794A.4.6.2.5 EN-DC
event triggered reporting tests for FR1 cell with SSB time index
detection when DRX is not used 794A.4.6.2.5.1 Test Purpose and
Environment 794A.4.6.2.5.2 Test Requirements 799A.4.6.2.6 EN-DC event
triggered reporting tests for FR1 cell with SSB time index detection
when DRX is used 799A.4.6.2.6.1 Test Purpose and Environment
799A.4.6.2.6.2 Test Requirements 804A.4.6.2.7 Void 805A.4.6.2.8 Void
805A.4.6.3 Void 805A.4.6.4 L1-RSRP measurement for beam reporting
805A.4.6.4.1 SSB based L1-RSRP measurement when DRX is not used
805A.4.6.4.1.1 Test Purpose and Environment 805A.4.6.4.1.2 Test
parameters 805A.4.6.4.1.3 Test Requirements 808A.4.6.4.2 SSB based
L1-RSRP measurement when DRX is used 808A.4.6.4.2.1 Test Purpose and
Environment 808A.4.6.4.2.2 Test parameters 809A.4.6.4.2.3 Test
Requirements 812A.4.6.4.3 CSI-RS based L1-RSRP measurement when DRX is
not used 812A.4.6.4.3.1 Test Purpose and Environment 812A.4.6.4.3.2 Test
parameters 813A.4.6.4.3.3 Test Requirements 816A.4.6.4.4 CSI-RS based
L1-RSRP measurement when DRX is used 816A.4.6.4.4.1 Test Purpose and
Environment 816A.4.6.4.4.2 Test parameters 817A.4.6.4.4.3 Test
Requirements 819A.4.6.4.5 SSB based L1-RSRP measurement when DRX is used
for UE configured with *highSpeedMeasFlag-r16* 819A.4.6.4.5.1 Test
Purpose and Environment 819A.4.6.4.5.2 Test parameters 820A.4.6.4.5.3
Test Requirements 823A.4.6.5 CLI measurements 823A.4.6.5.1 SRS-RSRP
measurement with non-DRX 823A.4.6.5.1.1 Test Purpose and Environment
823A.4.6.5.1.2 Test Parameters 824A.4.6.5.1.3 Test Requirements
827A.4.6.5.2 CLI-RSSI measurement with non-DRX 827A.4.6.5.2.1 Test
Purpose and Environment 827A.4.6.5.2.2 Test Parameters 828A.4.6.5.2.3
Test Requirements 829A.4.6.6 Measurements with autonomous gaps
830A.4.6.6.1 EN-DC intra-frequency CGI identification of NR FR1 cell
with autonomous gaps in synchronous EN-DC 830A.4.6.6.1.1 Test Purpose
and Environment 830A.4.6.6.1.2 Test Requirements 834A.4.6.7 L1-SINR
measurement for beam reporting 834A.4.6.7.1 L1-SINR measurement with
CSI-RS based CMR and no dedicated IMR when DRX is not used
834A.4.6.7.1.1 Test Purpose and Environment 834A.4.6.7.1.2 Test
parameters 835A.4.6.7.1.3 Test Requirements 838A.4.6.7.2 L1-SINR
measurement with SSB based CMR and dedicated IMR when DRX is used
838A.4.6.7.2.1 Test Purpose and Environment 838A.4.6.7.2.2 Test
parameters 839A.4.6.7.2.3 Test Requirements 842A.4.6.7.3 L1-SINR
measurement with CSI-RS based CMR and dedicated IMR configured when DRX
is used 842A.4.6.7.3.1 Test Purpose and Environment 842A.4.6.7.3.2 Test
parameters 843A.4.6.7.3.3 Test Requirements 846A.4.6.8 CSI-RS based
intra-frequency Measurement 846A.4.6.8.1 EN-DC event triggered reporting
tests without gap under DRX 846A.4.6.8.1.1 Test purpose and Environment
846A.4.6.8.1.2 Test Requirements 849A.4.6.9 CSI-RS based inter-frequency
Measurement 850A.4.6.9.1 EN-DC event triggered reporting tests for FR1
cell when non-DRX is used 850A.4.6.9.1.1 Test Purpose and Environment
850A.4.6.9.1.2 Test Requirements 853A.4.7 Measurement Performance
requirements 854A.4.7.1 SS-RSRP 854A.4.7.1.1 EN-DC Intra-frequency
measurement accuracy with FR1 serving cell and FR1 target cell
854A.4.7.1.1.1 Test Purpose and Environment 854A.4.7.1.1.2 Test
parameters 854A.4.7.1.1.3 Test Requirements 858A.4.7.1.2 EN-DC
inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell 858A.4.7.1.2.1 Test Purpose and Environment 858A.4.7.1.2.2
Test parameters 859A.4.7.1.2.3 Test Requirements 863A.4.7.1.3 Void
863A.4.7.2 SS-RSRQ 863**A.4.7.2.1** **EN-DC Intra-frequency measurement
accuracy with FR1 serving cell and FR1 target cell** 863A.4.7.2.1.1 Test
Purpose and Environment 863A.4.7.2.1.2 Test Parameters 864A.4.7.2.1.3
Test Requirements 869A.4.7.2.2 EN-DC Inter-frequency measurement
accuracy with FR1 serving cell and FR1 target cell 869A.4.7.2.2.1 Test
Purpose and Environment 869A.4.7.2.2.2 Test Parameters 869A.4.7.2.2.3
Test Requirements 874A.4.7.3 SS-SINR 874A.4.7.3.1 EN-DC Intra-frequency
measurement accuracy with FR1 serving cell and FR1 target cell
874A.4.7.3.1.1 Test Purpose and Environment 874A.4.7.3.1.2 Test
Parameters 874A.4.7.3.1.3 Test Requirements 878A.4.7.3.2 EN-DC
Inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell 878A.4.7.3.2.1 Test Purpose and Environment 878A.4.7.3.2.2
Test Parameters 878A.4.7.3.2.3 Test Requirements 883A.4.7.4 L1-RSRP
measurement for beam reporting 883A.4.7.4.1 SSB based L1-RSRP
measurement 883A.4.7.4.1.1 Test Purpose and Environment 883A.4.7.4.1.2
Test parameters 884A.4.7.4.1.3 Test Requirements 887A.4.7.4.2 CSI-RS
based L1-RSRP measurement on resource set with repetition off
887A.4.7.4.2.1 Test Purpose and Environment 887A.4.7.4.2.2 Test
parameters 888A.4.7.4.2.3 Test Requirements 891A.4.7.5 SFTD accuracy
891A.4.7.5.1 SFTD accuracy 891A.4.7.5.1.1 Test Purpose and Environment
891A.4.7.5.1.2 Test Parameters 891A.4.7.5.1.3 Test Requirements
896A.4.7.5.2 Void 896A.4.7.5.3 Void 896A.4.7.6 CLI measurements
896A.4.7.6.1 EN-DC SRS-RSRP measurement accuracy with FR1 serving cell
896A.4.7.6.1.1 Test Purpose and Environment 896A.4.7.6.1.2 Test
parameters 897A.4.7.6.1.3 Test Requirements 902A.4.7.6.2 EN-DC CLI-RSSI
measurement accuracy with FR1 serving cell 902A.4.7.6.2.1 Test Purpose
and Environment 902A.4.7.6.2.2 Test parameters 903A.4.7.6.2.3 Test
Requirements 906A.4.7.7 L1-SINR measurement for beam reporting
906A.4.7.7.1 L1-SINR measurement with CSI-RS based CMR and no dedicated
IMR configured and CSI-RS resource set with repetition off
906A.4.7.7.1.1 Test Purpose and Environment 906A.4.7.7.1.2 Test
parameters 907A.4.7.7.1.3 Test Requirements 911A.4.7.7.2 L1-SINR
measurement with SSB based CMR and dedicated IMR 911A.4.7.7.2.1 Test
Purpose and Environment 911A.4.7.7.2.2 Test parameters 912A.4.7.7.2.3
Test Requirements 916A.4.7.7.3 L1-SINR measurement with CSI-RS based CMR
and dedicated IMR 916A.4.7.7.3.1 Test Purpose and Environment
916A.4.7.7.3.2 Test parameters 917A.4.7.7.3.3 Test Requirements
920A.4.7.8 CSI-RSRP 920A.4.7.8.1 EN-DC Intra-frequency measurement
accuracy with FR1 serving cell and FR1 target cell 920A.4.7.8.1.1 Test
Purpose and Environment 920A.4.7.8.1.2 Test parameters 921A.4.7.8.1.3
Test Requirements 924A.4.7.8.2 EN-DC inter-frequency measurement
accuracy with FR1 serving cell and FR1 target cell 924A.4.7.8.2.1 Test
Purpose and Environment 924A.4.7.8.2.2 Test parameters 925A.4.7.8.2.3
Test Requirements 928A.4.7.9 CSI-RSRQ 929A.4.7.9.1 EN-DC Intra-frequency
measurement accuracy with FR1 serving cell and FR1 target cell
929A.4.7.9.1.1 Test Purpose and Environment 929A.4.7.9.1.2 Test
Parameters 929A.4.7.9.1.3 Test Requirements 934A.4.7.9.2 EN-DC
Inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell 934A.4.7.9.2.1 Test Purpose and Environment 934A.4.7.9.2.2
Test Parameters 934A.4.7.2.2.3 Test Requirements 939A.4.7.10 CSI-SINR
939A.4.7.10.1 EN-DC Intra-frequency measurement accuracy with FR1
serving cell and FR1 target cell 939A.4.7.10.1.1 Test Purpose and
Environment 939A.4.7.10.1.2 Test Parameters 940A.4.7.10.1.3 Test
Requirements 943A.4.7.10.2 EN-DC Inter-frequency measurement accuracy
with FR1 serving cell and FR1 target cell 943A.4.7.10.2.1 Test Purpose
and Environment 943A.4.7.10.2.2 Test Parameters 943A.4.7.10.2.3 Test
Requirements 946A.4.8 Void 947A.4A NE-DC test with all NR cells in FR1
947A.4A.1 Signaling characteristics 947A.4A.1.1 E-UTRAN PSCell addition
947A.4A.1.1.1 Test purpose and environment 947A.4A.1.1.2 Test
Requirements 951A.4A.1.2 Active BWP switch 952A.4A.1.2.1 E-UTRAN PSCell
-- NR PCell FR1 DCI-based and Timer-based DL active BWP switch in
non-DRX in synchronous NE-DC 952A.4A.1.2.1.1 Test Purpose and
Environment 952A.4A.1.2.1.2 Test Requirements 956A.4A.2 Measurement
performance 957A.4A.2.1 SFTD accuracy 957A.4A.2.1.1 SFTD accuracy
957A.4A.2.1.1.1 Test Purpose 957A.4A.2.1.1.2 Test Environment
957A.4A.2.1.1.3 Test Requirements 960A.5 EN-DC tests with one or more NR
cells in FR2 961A.5.1 Void 961A.5.2 Void 961A.5.3 RRC\_CONNECTED state
mobility 961A.5.3.1 Void 961A.5.3.2 RRC Connection Mobility Control
961A.5.3.2.1 Void 961A.5.3.2.2 Random Access 961A.5.3.2.2.1 4-step RA
type contention based random access test in FR2 for PSCell/SCell in
EN-DC 961A.5.3.2.2.2 4-step RA type non-contention based random access
test in FR2 for PSCell/SCell in EN-DC 964A.5.3.2.2.3 2-step RA type
contention based random access test in FR2 for PSCell/SCell in EN-DC
970A.5.3.2.2.4 2-step RA type non-contention based random access test in
FR2 for PSCell/SCell in EN-DC 973A.5.3.2.3 Void 977A.5.4 Timing
977A.5.4.1 UE transmit timing 977A.5.4.1.1 NR UE Transmit Timing Test
for FR2 977A.5.4.1.1.1 Test Purpose and environment 977A.5.4.1.1.2 Test
requirements 980A.5.4.2 UE timer accuracy 981A.5.4.3 Timing advance
981A.5.4.3.1 EN-DC FR2 timing advance adjustment accuracy 981A.5.4.3.1.1
Test Purpose and Environment 981A.5.4.3.1.2 Test Parameters
981A.5.4.3.1.3 Test Requirements 985A.5.5 Signaling characteristics
985A.5.5.1 Radio link Monitoring 985A.5.5.1.1 Radio Link Monitoring
Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in
non-DRX mode 985A.5.5.1.1.1 Test Purpose and Environment 985A.5.5.1.1.2
Test Requirements 989A.5.5.1.2 Radio Link Monitoring In-sync Test for
FR2 PSCell configured with SSB-based RLM RS in non-DRX mode
990A.5.5.1.2.1 Test Purpose and Environment 990A.5.5.1.2.2 Test
Requirements 993A.5.5.1.3 Radio Link Monitoring Out-of-sync Test for FR2
PSCell configured with SSB-based RLM RS in DRX mode 994A.5.5.1.3.1 Test
Purpose and Environment 994A.5.5.1.3.2 Test Requirements 998A.5.5.1.4
Radio Link Monitoring In-sync Test for FR2 PSCell configured with
SSB-based RLM RS in DRX mode 998A.5.5.1.4.1 Test Purpose and Environment
998A.5.5.1.4.2 Test Requirements 1002A.5.5.1.5 EN-DC Radio Link
Monitoring Out-of-sync Test for FR2 PSCell configured with CSI-RS-based
RLM in non-DRX mode 1002A.5.5.1.6 EN-DC Radio Link Monitoring In-sync
Test for FR2 PSCell configured with CSI-RS-based RLM in non-DRX mode
1006A.5.5.1.7 EN-DC Radio Link Monitoring Out-of-sync Test for FR2
PSCell configured with CSI-RS-based RLM in DRX mode 1010A.5.5.1.8 EN-DC
Radio Link Monitoring In-sync Test for FR2 PSCell configured with
CSI-RS-based RLM in DRX mode 1015A.5.5.1.8.2 Test Requirements
1019A.5.5.1.9 EN-DC Radio Link Monitoring UE Scheduling Restrictions on
FR2 1020A.5.5.1.9.1 Test Purpose and Environment 1020A.5.5.1.9.2 Test
Requirements 1022A.5.5.2 Interruption 1022A.5.5.2.1 E-UTRAN -- NR FR2
interruptions at transitions between active and non-active during DRX in
synchronous EN-DC 1022A.5.5.2.1.1 Test Purpose and Environment
1022A.5.5.2.1.2 Test Requirements 1025A.5.5.2.2 E-UTRAN -- NR FR2
interruptions at transitions between active and non-active during DRX in
asynchronous EN-DC 1025A.5.5.2.2.1 Test Purpose and Environment
1025A.5.5.2.2.2 Test Requirements 1028**A.5.5.2.3** E-UTRAN -- NR FR2
interruptions during measurements on deactivated NR SCC in synchronous
EN-DC 1028A.5.5.2.3.1 Test Purpose and Environment 1028A.5.5.2.**3.2**
Test Requirements 1032**A.5.5.2.4** E-UTRAN -- NR FR2 interruptions
during measurements on deactivated NR SCC in asynchronous EN-DC
1032A.5.5.2.4.1 Test Purpose and Environment 1032A.5.5.2.**4.2** Test
Requirements 1035**A.5.5.2.5** E-UTRAN -- NR FR2 interruptions during
measurements on deactivated E-UTRAN SCC in synchronous EN-DC
1036A.5.5.2.5.1 Test Purpose and Environment 1036A.5.5.2.**5.2** Test
Requirements 1039**A.5.5.2.6** E-UTRAN -- NR FR2 interruptions during
measurements on deactivated E-UTRAN SCC in asynchronous EN-DC
1040A.5.5.2.6.1 Test Purpose and Environment 1040A.5.5.2.**6.2** Test
Requirements 1042**A.5.5.2.7** E-UTRAN -- NR FR2 interruptions at E-UTRA
SRS carrier based switching 1043A.5.5.2.7.1 Test Purpose and Environment
1043A.5.5.2.7.2 Test Requirements 1046A.5.5.2.8 E-UTRAN -- NR FR2
interruptions at NR SRS carrier based switching 1046A.5.5.2.8.1 Test
Purpose and Environment 1046A.5.5.2.8.3 Test Requirements 1049A.5.5.3
SCell Activation and Deactivation Delay 1049A.5.5.3.1 SCell Activation
and deactivation of SCell in FR2 intra-band 1049A.5.5.3.1.1 Test Purpose
and Environment 1049A.5.5.3.1.2 Test Requirements 1052A.5.5.3.2 SCell
Activation and deactivation of known SCell in FR1 for 160ms SCell
measurement cycle 1052A.5.5.3.2.1 Test Purpose and Environment
1052A.5.5.3.2.2 Test Requirements 1056A.5.5.3.3 Void 1056A.5.5.3.4 Void
1056A.5.5.3.5 SCell Activation and deactivation of SCell in FR2
1056A.5.5.3.5.1 Test Purpose and Environment 1056A.5.5.3.5.2 Test
Requirements 1060A.5.5.3.6 Multiple SCell Activation and deactivation of
one unknown SCell and one known SCell in FR2 1061A.5.5.3.6.1 Test
Purpose and Environment 1061A.5.5.3.6.2 Test Requirements 1064A.5.5.3.7
Direct SCell activation at SCell addition of known SCell in FR2
1065A.5.5.3.7.1 Test Purpose and Environment 1065A.5.5.3.7.2 Test
Requirements 1068A.5.5.4 Void 1068A.5.5.5 Beam Failure Detection and
Link recovery procedures 1068A.5.5.5.1 EN-DC Beam Failure Detection and
Link Recovery Test for FR2 PSCell configured with SSB-based BFD and LR
in non-DRX mode 1068A.5.5.5.1.1 Test Purpose and Environment
1068A.5.5.5.1.2 Test Requirements 1072A.5.5.5.2 EN-DC Beam Failure
Detection and Link Recovery Test for FR2 PSCell configured with
SSB-based BFD and LR in DRX mode 1073A.5.5.5.2.1 Test Purpose and
Environment 1073A.5.5.5.2.2 Test Requirements 1077A.5.5.5.3 EN-DC Beam
Failure Detection and Link Recovery Test for FR2 PSCell configured with
CSI-RS-based BFD and LR in non-DRX mode 1078A.5.5.5.3.1 Test Purpose and
Environment 1078A.5.5.5.3.2 Test Requirements 1082A.5.5.5.4 EN-DC Beam
Failure Detection and Link Recovery Test for FR2 PSCell configured with
CSI-RS-based BFD and LR in DRX mode 1083A.5.5.5.4.1 Test Purpose and
Environment 1083A.5.5.5.4.2 Test Requirements 1087A.5.5.5.5 EN-DC
scheduling availability restriction during Beam Failure Detection and
Link Recovery for FR2 PSCell configured with SSB-based BFD and LR in
non-DRX mode 1088A.5.5.5.5.1 Test Purpose and Environment
1088A.5.5.5.5.2 Test Requirements 1092A.5.5.5.6 EN-DC Beam Failure
Detection and Link Recovery Test for FR2 SCell configured with
CSI-RS-based BFD and LR in non-DRX mode 1093A.5.5.5.6.1 Test Purpose and
Environment 1093A.5.5.5.6.2 Test Requirements 1097A.5.5.5.7 EN-DC Beam
Failure Detection and Link Recovery Test for FR2 SCell configured with
CSI-RS-based BFD and LR in DRX mode 1098A.5.5.5.7.1 Test Purpose and
Environment 1098A.5.5.5.7.2 Test Requirements 1102A.5.5.6 Active BWP
switch 1103A.5.5.6.1 DCI-based and Timer-based Active BWP Switch
1103A.5.5.6.1.1 E-UTRAN -- NR PSCell FR2 DL active BWP switch with
non-DRX in synchronous EN-DC 1103A.5.5.6.1.1.1 Test Purpose and
Environment 1103A.**5.5.6.1.1**.2 Test Requirements 1106A.5.5.6.1.2
E-UTRAN -- NR PSCell FR2 with FR2 SCell DL active BWP switch in non-DRX
in synchronous EN-DC 1106A.5.5.6.2 RRC-based Active BWP Switch
1111A.5.5.6.3 Simultaneous DCI-based and Timer-based Active BWP Switch
on multiple CCs 1115A.5.5.6.3.1 E-UTRAN -- NR PSCell FR2 and NR SCell
FR2 DL active BWP switch on multiple CCs in synchronous EN-DC
1115A.5.5.6.3.1.1 Test Purpose and Environment 1115A.5.5.6.4 SCell
dormancy switch 1119A.5.5.6.4.1 E-UTRAN -- NR FR2 PSCell SCell dormancy
switch of single FR2 SCell inside active time 1119A.5.5.6.4.1.1 Test
Purpose and Environment 1119A.5.5.6.4.1.2 Test Requirements
1123A.5.5.6.4.2 E-UTRAN -- NR FR1 PSCell SCell dormancy switch of two
FR2 SCells outside active time 1123A.5.5.6.4.2.1 Test Purpose and
Environment 1123A.5.5.6.4.2.2 Test Requirements 1130A.5.5.6.5
Simultaneous RRC-based Active BWP Switch on multiple CCs 1130A.5.5.7
PSCell addition and release delay 1133A.5.5.7.1 Addition and Release
Delay of NR PSCell 1133A.5.5.7.1.1 Test purpose and environment
1133A.5.5.7.1.2 Test Requirements 1137A.5.5.8 Active TCI state switch
delay 1138A.5.5.8.1 MAC-CE based active TCI state switch 1138A.5.5.8.1.1
E-UTRAN -- NR PSCell FR2 active TCI state switch for a known TCI state
1138A.5.5.8.1.1.1 Test Purpose and Environment 1138A.5.5.8**.1.1**.2
Test Requirements 1141A.5.5.8.2 RRC based active TCI state switch
1141A.5.5.8.2.1 E-UTRAN -- NR PSCell FR2 active TCI state switch for a
known TCI state 1141A.5.5.8.2.1.1 Test Purpose and Environment
1141A.5.5.8.2**.1**.2 Test Requirements 1145A.5.5.9 Uplink spatial
relation switch delay 1145A.5.5.9.1 MAC-CE based uplink spatial relation
switch 1145A.5.5.9.1.1 E-UTRAN -- NR PSCell FR2 uplink spatial relation
switch for a known spatial relation 1145A.5.5.9.1.1.1 Test Purpose and
Environment 1145A.5.5.9**.1.1**.2 Test Requirements 1148A.5.5.9.2 RRC
based spatial relation switch 1148A.5.5.9.2.1 E-UTRAN -- NR PSCell FR2
spatial relation switch associated with a known DL-RS 1148A.5.5.9.2.1.1
Test Purpose and Environment 1148A.5.5.9.2**.1**.2 Test Requirements
1151A.5.5.10 UE specific CBW change 1151A.5.5.10.1 UE specific CBW
change on FR2 NR PSCell 1151A.5.5.10.1.1 Test Purpose and Environment
1151A.5.5.10.1.2 Test Requirements 1154A.5.6 Measurement procedure
1155A.5.6.1 Intra-frequency Measurements 1155A.5.6.1.1 EN-DC event
triggered reporting test without gap under non-DRX 1155A.5.6.1.1.1 Test
purpose and Environment 1155A.5.6.1.1.2 Test Requirements 1158A.5.6.1.2
EN-DC event triggered reporting test without gap under DRX
1158A.5.6.1.2.1 Test purpose and Environment 1158A.5.6.1.2.2 Test
Requirements 1160A.5.6.1.3 EN-DC event triggered reporting test with
per-UE gaps under non-DRX 1161A.5.6.1.3.1 Test purpose and Environment
1161A.5.6.1.3.2 Test Requirements 1165A.5.6.1.4 EN-DC event triggered
reporting test with per-UE gaps under DRX 1165A.5.6.1.4.1 Test purpose
and Environment 1165A.5.6.1.4.2 Test Requirements 1168A.5.6.2
Inter-frequency Measurements 1169A.5.6.2.1 EN-DC event triggered
reporting tests for FR2 cell without SSB time index detection when DRX
is not used 1169A.5.6.2.1.1 Test Purpose and Environment 1169A.5.6.2.1.2
Test Requirements 1172A.5.6.2.2 EN-DC event triggered reporting tests
for FR2 cell without SSB time index detection when DRX is used
1172A.5.6.2.2.1 Test Purpose and Environment 1172A.5.6.2.2.2 Test
Requirements 1176A.5.6.2.3 EN-DC event triggered reporting tests for FR2
cell with SSB time index detection when DRX is not used 1176A.5.6.2.3.1
Test Purpose and Environment 1176A.5.6.2.3.2 Test Requirements
1180A.5.6.2.4 EN-DC event triggered reporting tests for FR2 cell with
SSB time index detection when DRX is used 1180A.5.6.2.4.1 Test Purpose
and Environment 1180A.5.6.2.4.2 Test Requirements 1184A.5.6.2.5 EN-DC
event triggered reporting tests for FR2 cell without SSB time index
detection when DRX is not used 1184A.5.6.2.5.1 Test Purpose and
Environment 1184A.5.6.2.5.2 Test Requirements 1189A.5.6.2.6 EN-DC event
triggered reporting tests for FR2 cell without SSB time index detection
when DRX is used 1189A.5.6.2.6.1 Test Purpose and Environment
1189A.5.6.2.6.2 Test Requirements 1193A.5.6.2.7 EN-DC event triggered
reporting tests for FR2 cell with SSB time index detection when DRX is
not used 1193A.5.6.2.7.1 Test Purpose and Environment 1193A.5.6.2.7.2
Test Requirements 1198A.5.6.2.8 EN-DC event triggered reporting tests
for FR2 cell with SSB time index detection when DRX is used
1198A.5.6.2.8.1 Test Purpose and Environment 1198A.5.6.2.8.2 Test
Requirements 1203A.5.6.3 L1-RSRP measurement for beam reporting
1203A.5.6.3.1 SSB based L1-RSRP measurement when DRX is not used
1203A.5.6.3.1.1 Test Purpose and Environment 1203A.5.6.3.1.2 Test
parameters 1203A.5.6.3.1.3 Test Requirements 1205A.5.6.3.2 SSB based
L1-RSRP measurement when DRX is used 1205A.5.6.3.2.1 Test Purpose and
Environment 1205A.5.6.3.2.2 Test parameters 1206A.5.6.3.2.3 Test
Requirements 1208A.5.6.3.3 CSI-RS based L1-RSRP measurement when DRX is
not used 1208A.5.6.3.3.1 Test Purpose and Environment 1208A.5.6.3.3.2
Test parameters 1209A.5.6.3.3.3 Test Requirements 1211A.5.6.3.4 CSI-RS
based L1-RSRP measurement when DRX is used 1212A.5.6.3.4.1 Test Purpose
and Environment 1212A.5.6.3.4.2 Test parameters 1212A.5.6.3.4.3 Test
Requirements 1214A.5.6.4 CLI measurements 1215A.5.6.4.1 SRS-RSRP
measurement with DRX 1215A.5.6.4.1.1 Test Purpose and Environment
1215A.5.6.4.1.2 Test Parameters 1215A.5.6.4.1.3 Test Requirements
1217A.5.6.4.2 CLI-RSSI measurement with DRX 1217A.5.6.4.2.1 Test Purpose
and Environment 1217A.5.6.4.2.2 Test Parameters 1218A.5.6.4.2.3 Test
Requirements 1220A.5.6.5 Measurements with autonomous gaps 1220A.5.6.5.1
EN-DC inter-frequency CGI identification of NR neighbor cell in FR2
1220A.5.6.5.1.1 Test Purpose and Environment 1220A.5.6.5.1.2 Test
Requirements 1223A.5.6.6 L1-SINR measurement for beam reporting
1224A.5.6.6.1 L1-SINR measurement with CSI-RS based CMR and no dedicated
IMR configured when DRX is used 1224A.5.6.6.1.1 Test Purpose and
Environment 1224A.5.6.6.1.2 Test parameters 1224A.5.6.6.1.3 Test
Requirements 1226A.5.6.6.2 L1-SINR measurement with SSB based CMR and
dedicated IMR when DRX is not used 1226A.5.6.6.2.1 Test Purpose and
Environment 1226A.5.6.6.2.2 Test parameters 1227A.5.6.6.2.3 Test
Requirements 1230A.5.6.6.3 L1-SINR measurement with CSI-RS based CMR and
dedicated IMR configured when DRX is not used 1230A.5.6.6.3.1 Test
Purpose and Environment 1230A.5.6.6.3.2 Test parameters 1231A.5.6.6.3.3
Test Requirements 1233A.5.6.7 CSI-RS based Intra-frequency Measurements
1233A.5.6.7.1 EN-DC event triggered reporting test without gap under
non-DRX 1233A.5.6.7.1.1 Test purpose and Environment 1233A.5.6.7.1.2
Test Requirements 1236A.5.6.8 CSI-RS based Inter-frequency Measurements
1236A.5.6.8.1 EN-DC event triggered reporting tests for NR FR2 cell when
DRX is used 1236A.5.6.8.1.1 Test Purpose and Environment 1236A.5.6.8.1.2
Test Requirements 1240A.5.7 Measurement Performance requirements
1240A.5.7.1 SS-RSRP 1241A.5.7.1.1 EN-DC intra-frequency case measurement
accuracy with FR2 serving cell and FR2 target cell 1241A.5.7.1.1.1 Test
Purpose and Environment 1241A.5.7.1.1.2 Test parameters 1241A.5.7.1.1.3
Test Requirements 1243A.5.7.1.2 EN-DC inter-frequency case measurement
accuracy with FR2 serving cell and FR2 target cell 1244A.5.7.1.2.1 Test
Purpose and Environment 1244A.5.7.1.2.2 Test parameters 1244A.5.7.1.2.3
Test Requirements 1249A.5.7.1.3 EN-DC inter-frequency measurement
accuracy with FR1 serving cell and FR2 target cell 1250A.5.7.1.3.1 Test
Purpose and Environment 1250A.5.7.1.3.2 Test parameters 1250A.5.7.1.3.3
Test Requirements 1253A.5.7.2 SS-RSRQ 1254A.5.7.2.1 EN-DC
Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 1254A.5.7.2.1.1 Test Purpose and Environment 1254A.5.7.2.1.2
Test Parameters 1254A.5.7.2.1.3 Test Requirements 1256A.5.7.2.2 EN-DC
Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 1257A.5.7.2.2.1 Test Purpose and Environment 1257A.5.7.2.2.2
Test Parameters 1257A.5.7.2.2.3 Test Requirements 1259A.5.7.3 SS-SINR
1259A.5.7.3.1 EN-DC Intra-frequency measurement accuracy with FR2
serving cell and FR2 TDD target cell 1259A.5.7.3.1.1 Test Purpose and
Environment 1259A.5.7.3.1.2 Test Parameters 1259A.5.7.3.1.3 Test
Requirements 1261A.5.7.3.2 EN-DC Inter-frequency measurement accuracy
with FR2 serving cell and FR2 TDD target cell 1261A.5.7.3.2.1 Test
Purpose and Environment 1261A.5.7.3.2.2 Test Parameters 1261A.5.7.3.2.3
Test Requirements 1263A.5.7.4 L1-RSRP measurement for beam reporting
1263A.5.7.4.1 SSB based L1-RSRP measurement 1263A.5.7.4.1.1 Test Purpose
and Environment 1263A.5.7.4.1.2 Test parameters 1264A.5.7.4.1.3 Test
Requirements 1266A.5.7.4.2 CSI-RS based L1-RSRP measurement on resource
set with repetition off 1267A.5.7.4.2.1 Test Purpose and Environment
1267A.5.7.4.2.2 Test parameters 1267A.5.7.4.2.3 Test Requirements
1269A.5.7.5 CLI measurements 1270A.5.7.5.1 EN-DC SRS-RSRP measurement
accuracy with FR2 serving cell 1270A.5.7.5.1.1 Test Purpose and
Environment 1270A.5.7.5.1.2 Test parameters 1270A.5.7.5.1.3 Test
Requirements 1273A.5.7.5.2 EN-DC CLI-RSSI measurement accuracy with FR2
serving cell 1274A.5.7.5.2.1 Test Purpose and Environment
1274A.5.7.5.2.2 Test parameters 1274A.5.7.5.2.3 Test Requirements
1276A.5.7.6 L1-SINR measurement for beam reporting 1277A.5.7.6.1 L1-SINR
measurement with CSI-RS based CMR and no dedicated IMR configured and
CSI-RS resource set with repetition off 1277A.5.7.6.1.1 Test Purpose and
Environment 1277A.5.7.6.1.2 Test parameters 1277A.5.7.6.1.3 Test
Requirements 1279A.5.7.6.2 L1-SINR measurement with SSB based CMR and
dedicated IMR 1280A.5.7.6.2.1 Test Purpose and Environment
1280A.5.7.6.2.2 Test parameters 1280A.5.7.6.2.3 Test Requirements
1282A.5.7.6.3 L1-SINR measurement with CSI-RS based CMR and dedicated
IMR 1283A.5.7.6.3.1 Test Purpose and Environment 1283A.5.7.6.3.2 Test
parameters 1283A.5.7.6.3.3 Test Requirements 1285A.5.7.7 CSI-RSRP
1286A.5.7.7.1 EN-DC intra-frequency case measurement accuracy with FR2
serving cell and FR2 target cell 1286A.5.7.7.1.2 Test parameters
1286A.5.7.7.1.3 Test Requirements 1288A.5.7.7.2 EN-DC inter-frequency
case measurement accuracy with FR2 serving cell and FR2 target cell
1289A.5.7.7.2.1 Test Purpose and Environment 1289A.5.7.7.2.2 Test
parameters 1289A.5.7.7.2.3 Test Requirements 1293A.5.7.8 CSI-RSRQ
1294A.5.7.8.1 EN-DC Intra-frequency measurement accuracy with FR2
serving cell and FR2 target cell 1294A.5.7.8.1.1 Test Purpose and
Environment 1294A.5.7.8.1.2 Test Parameters 1294A.5.7.8.1.3 Test
Requirements 1296A.5.7.8.2 EN-DC Inter-frequency measurement accuracy
with FR2 serving cell and FR2 TDD target cell 1296A.5.7.8.2.1 Test
Purpose and Environment 1296A.5.7.8.2.2 Test Parameters 1296A.5.7.9
CSI-SINR 1298A.5.7.9.1 EN-DC Intra-frequency measurement accuracy with
FR2 serving cell and FR2 TDD target cell 1298A.5.7.9.1.1 Test Purpose
and Environment 1298A.5.7.9.1.2 Test Parameters 1298Table A.5.7.9.1.2-1:
CSI-SINR Intra frequency CSI-SINR supported test configurations
1299A.5.7.9.1.3 Test Requirements 1301A.5.7.9.2 EN-DC Inter-frequency
measurement accuracy with FR2 serving cell and FR2 TDD target cell
1301A.5.7.9.2.1 Test Purpose and Environment 1301A.5.7.9.2.2 Test
Parameters 1301A.5.7.9.2.3 Test Requirements 1304A.5.8 Void 1304A.6 NR
standalone tests with all NR cells in FR1 1011A.6.1 SA: RRC\_IDLE state
mobility 1011A.6.1.1 Cell re-selection to NR 1011A.6.1.1.1 Cell
reselection to FR1 intra-frequency NR case 1011A.6.1.1.1.1 Test Purpose
and Environment 1011A.6.1.1.1.2 Test Parameters 1011A.6.1.1.1.3 Test
Requirements 1015A.6.1.1.2 Cell reselection to FR1 inter-frequency NR
case 1015A.6.1.1.2.1 Test Purpose and Environment 1015A.6.1.1.2.2 Test
Parameters 1015A.6.1.1.2.3 Test Requirements 1019A.6.1.1.3 Cell
reselection to FR1 intra-frequency NR case for UE fulfilling low
mobility relaxed measurement criterion 1019A.6.1.1.3.1 Test Purpose and
Environment 1019A.6.1.1.3.2 Test Parameters 1019A.6.1.1.3.3 Test
Requirements 1024A.6.1.1.4 Cell reselection to FR1 intra-frequency NR
case for UE fulfilling not-at-cell edge relaxed measurement criterion
1024A.6.1.1.4.1 Test Purpose and Environment 1024A.6.1.1.4.2 Test
Parameters 1024A.6.1.1.4.3 Test Requirements 1028A.6.1.1.5 Cell
reselection to FR1 inter-frequency NR case for UE fulfilling low
mobility relaxed measurement criterion 1028A.6.1.1.5.1 Test Purpose and
Environment 1028A.6.1.1.5.2 Test Parameters 1028A.6.1.1.5.3 Test
Requirements 1032A.6.1.1.6 Cell reselection to FR1 inter-frequency NR
case for UE fulfilling not-at-cell edge relaxed measurement criterion
1033A.6.1.1.6.1 Test Purpose and Environment 1033A.6.1.1.6.2 Test
Parameters 1033A.6.1.1.6.3 Test Requirements 1037A.6.1.1.7 Cell
reselection to FR1 intra-frequency NR case for UE configured with
***highSpeedMeasFlag-r16*** 1038A.6.1.1.7.1 Test Purpose and Environment
1038A.6.1.1.7.2 Test Parameters 1038A.6.1.1.7.3 Test Requirements
1042A.6.1.2 Inter-RAT E-UTRAN cell re-selection 1042A.6.1.2.1 Cell
reselection to higher priority E-UTRAN 1042A.6.1.2.1.1 Test Purpose and
Environment 1042A.6.1.2.1.2 Test Parameters 1042A.6.1.2.1.3 Test
Requirements 1045A.6.1.2.2 Cell reselection to lower priority E-UTRAN
1046A.6.1.2.2.1 Test Purpose and Environment 1046A.6.1.2.2.2 Test
Parameters 1046A.6.1.2.2.3 Test Requirements 1049A.6.1.2.3 Cell
reselection to lower priority E-UTRAN for UE fulfilling low mobility
relaxed measurement criterion 1050A.6.1.2.3.1 Test Purpose and
Environment 1050A.6.1.2.3.2 Test Parameters 1050A.6.1.2.3.3 Test
Requirements 1053A.6.1.2.4 Cell reselection to lower priority E-UTRAN
for UE fulfilling not-at-cell edge relaxed measurement criterion
1054A.6.1.2.4.1 Test Purpose and Environment 1054A.6.1.2.4.2 Test
Parameters 1054A.6.1.2.4.3 Test Requirements 1057A.6.1.2.5.3 Test
Requirements 1061A.6.2 SA: RRC\_INACTIVE state mobility 1062A.6.3
RRC\_CONNECTED state mobility 1062A.6.3.1 Handover 1062A.6.3.1.1
Intra-frequency handover from FR1 to FR1; known target cell
1062A.6.3.1.1.1 Test Purpose and Environment 1062A.6.3.1.1.2 Test
Parameters 1062A.6.3.1.1.3 Test Requirements 1066A.6.3.1.2
Intra-frequency handover from FR1 to FR1; unknown target cell
1066A.6.3.1.2.1 Test Purpose and Environment 1066A.6.3.1.2.2 Test
Parameters 1066A.6.3.1.2.3 Test Requirements 1070A.6.3.1.3
Inter-frequency handover from FR1 to FR1; unknown target cell
1070A.6.3.1.3.1 Test Purpose and Environment 1070A.6.3.1.3.2 Test
Parameters 1070A.6.3.1.3.3 Test Requirements 1074A.6.3.1.4 SA NR -
E-UTRAN handover 1074A.6.3.1.4.1 Test Purpose and Environment
1074A.6.3.1.4.2 Test Requirements 1080A.6.3.1.5 SA NR - E-UTRAN handover
with unknown target cell 1080A.6.3.1.5.1 Test Purpose and Environment
1080A.6.3.1.5.2 Test Requirements 1086A.6.3.1.6 SA NR - UTRAN FDD
handover 1086A.6.3.1.6.1 Test Purpose and Environment 1086A.6.3.1.6.2
Test Requirements 1090A.6.3.1.7 Intra-frequency synchronous DAPS
handover in FR1 1090A.6.3.1.7.1 Test Purpose and Environment
1090A.6.3.1.7.2 Test Parameters 1090A.6.3.1.7.3 Test Requirements
1094A.6.3.1.8 Intra-frequency asynchronous DAPS handover in FR1
1095A.6.3.1.8.1 Test Purpose and Environment 1095A.6.3.1.8.2 Test
Parameters 1095A.6.3.1.8.3 Test Requirements 1099A.6.3.1.9 Intra-band
inter-frequency synchronous DAPS handover test in SA for FR1
1100A.6.3.1.9.1 Test Purpose and Environment 1100A.6.3.1.9.2 Test
Parameters 1100A.6.3.1.9.3 Test Requirements 1104A.6.3.1.10 Intra-band
inter-frequency asynchronous DAPS handover test in SA for FR1
1104A.6.3.1.10.1 Test Purpose and Environment 1104A.6.3.1.10.2 Test
Parameters 1104A.6.3.1.10.3 Test Requirements 1107A.6.3.1.11 Inter-band
inter-frequency synchronous DAPS handover from FR1 to FR1
1107A.6.3.1.11.1 Test Purpose and Environment 1107A.6.3.1.11.2 Test
Parameters 1107A.6.3.1.11.3 Test Requirements 1114A.6.3.1.12 Inter-band
inter-frequency asynchronous DAPS handover from FR1 to FR1
1114A.6.3.1.12.1 Test Purpose and Environment 1114A.6.3.1.12.2 Test
Parameters 1114A.6.3.1.12.3 Test Requirements 1122A.6.3.2 RRC Connection
Mobility Control 1122A.6.3.2.1 SA: RRC Re-establishment 1122A.6.3.2.1.1
Intra-frequency RRC Re-establishment in FR1 1122A.6.3.2.1.2
Inter-frequency RRC Re-establishment in FR1 1126A.6.3.2.1.3
Intra-frequency RRC Re-establishment in FR1 without serving cell timing
1130A.6.3.2.2 Random Access 1134A.6.3.2.2.1 4-step RA type contention
based random access test in FR1 for NR standalone 1134A.6.3.2.2.2 4-step
RA type non-contention based random access test in FR1 for NR standalone
1139A.6.3.2.2.3 2-step RA type contention based random access test in
FR1 for NR standalone 1143A.6.3.2.2.4 2-step RA type non-contention
based test in FR1 for NR standalone 1148A.6.3.2.3 SA: RRC Connection
Release with Redirection 1152A.6.3.2.3.1 Redirection from NR in FR1 to
NR in FR1 1152A.6.3.2.3.2 Redirection from NR in FR1 to E-UTRAN
1156A.6.3.3 Conditional handover 1163A.6.3.3.1 Intra-frequency
conditional handover from FR1 to FR1 1163A.6.3.3.1.1 Test Purpose and
Environment 1163A.6.3.3.1.2 Test Parameters 1163A.6.3.3.1.3 Test
Requirements 1167A.6.3.3.2 Inter-frequency conditional handover from FR1
to FR1 1167A.6.3.3.2.1 Test Purpose and Environment 1167A.6.3.3.2.2 Test
Parameters 1167A.6.3.3.2.3 Test Requirements 1171A.6.4 Timing
1171A.6.4.1 UE transmit timing 1171A.6.4.1.1 NR UE Transmit Timing Test
for FR1 1171A.6.4.1.1.1 Test Purpose and environment 1171A.6.4.1.1.2
Test requirements 1175A.6.4.2 UE timer accuracy 1175A.6.4.3 Timing
advance 1175A.6.4.3.1 SA FR1 timing advance adjustment accuracy
1175A.6.4.3.1.1 Test Purpose and Environment 1175A.6.4.3.1.2 Test
Parameters 1175A.6.4.3.1.3 Test Requirements 1179A.6.5 Signalling
characteristics 1179A.6.5.1 Radio link Monitoring 1179A.6.5.1.1 Radio
Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based
RLM RS in non-DRX mode 1180A.6.5.1.1.1 Test Purpose and Environment
1180A.6.5.1.1.2 Test Requirements 1185A.6.5.1.2 Radio Link Monitoring
In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX
mode 1185A.6.5.1.2.1 Test Purpose and Environment 1185A.6.5.1.2.2 Test
Requirements 1191A.6.5.1.3 Radio Link Monitoring Out-of-sync Test for
FR1 PCell configured with SSB-based RLM RS in DRX mode 1191A.6.5.1.3.1
Test Purpose and Environment 1191A.6.5.1.3.2 Test Requirements
1197A.6.5.1.4 Radio Link Monitoring In-sync Test for FR1 PCell
configured with SSB-based RLM RS in DRX mode 1197A.6.5.1.4.1 Test
Purpose and Environment 1197A.6.5.1.4.2 Test Requirements 1203A.6.5.1.5
Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with
CSI-RS-based RLM in non-DRX mode 1203A.6.5.1.5.1 Test Purpose and
Environment 1203A.6.5.1.5.2 Test Requirements 1209A.6.5.1.6 Radio Link
Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM
in non-DRX mode 1209A.6.5.1.6.1 Test Purpose and Environment
1209A.6.5.1.6.2 Test Requirements 1214A.6.5.1.7 Radio Link Monitoring
Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX
mode 1214A.6.5.1.7.1 Test Purpose and Environment 1214A.6.5.1.7.2 Test
Requirements 1218A.6.5.1.8 Radio Link Monitoring In-sync Test for FR1
PCell configured with CSI-RS-based RLM in DRX mode 1218A.6.5.1.8.1 Test
Purpose and Environment 1218A.6.5.1.8.2 Test Requirements 1224A.6.5.2
Interruption 1224**A.6.5.2.1** Interruptions during measurements on
deactivated NR SCC in FR1 1224**A.6.5.2.1**.2 Test Requirements
1228A.6.5.2.2 SA interruptions at NR SRS carrier based switching
1229A.6.5.2.2.1 Test Purpose and Environment 1229A.6.5.2.2.2 Test
Parameters 1229A.6.5.2.2.3 Test Requirements 1231A.6.5.3 SCell
Activation and Deactivation Delay 1232A.6.5.3.1 SCell Activation and
deactivation of known SCell in FR1 in non-DRX for 160ms SCell
measurement cycle 1232A.6.5.3.1.1 Test Purpose and Environment
1232A.6.5.3.1.2 Test Requirements 1237A.6.5.3.2 SCell Activation and
deactivation of known SCell in FR1 in non-DRX for 640 ms SCell
measurement cycle 1238A.6.5.3.2.1 Test Purpose and Environment
1238A.6.5.3.2.2 Test Requirements 1238A.6.5.3.3 SCell Activation and
deactivation of unknown SCell in FR1 in non-DRX 1238A.6.5.3.3.1 Test
Purpose and Environment 1238A.6.5.3.3.2 Test Requirements 1239A.6.5.3.4
Direct SCell activation at SCell addition of known SCell in FR1
1239A.6.5.3.4.1 Test Purpose and Environment 1239A.6.5.3.4.2 Test
Requirements 1244A.6.5.3.5 Direct SCell activation at handover with
known SCell in FR1 1244A.6.5.3.5.1 Test Purpose and Environment
1244A.6.5.3.5.2 Test Requirements 1249A.6.5.4 UE UL carrier RRC
reconfiguration Delay 1250A.6.5.4.1 UE UL carrier RRC reconfiguration
Delay 1250A.6.5.4.1.1 Test Purpose and Environment 1250A.6.5.4.1.2 Test
Requirements 1260A.6.5.4.2 Void 1261A.6.5.5 Beam Failure Detection and
Link recovery procedures 1261A.6.5.5.1 Beam Failure Detection and Link
Recovery Test for FR1 PCell configured with SSB-based BFD and LR in
non-DRX mode 1261A.6.5.5.1.1 Test Purpose and Environment
1261A.6.5.5.1.2 Test Requirements 1266A.6.5.5.2 Beam Failure Detection
and Link Recovery Test for FR1 PCell configured with SSB-based BFD and
LR in DRX mode 1267A.6.5.5.2.1 Test Purpose and Environment
1267A.6.5.5.2.2 Test Requirements 1273A.6.5.5.3 Beam Failure Detection
and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD
and LR in non-DRX mode 1274A.6.5.5.3.1 Test Purpose and Environment
1274A.6.5.5.3.2 Test Requirements 1279A.6.5.5.4 Beam Failure Detection
and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD
and LR in DRX mode 1280A.6.5.5.4.1 Test Purpose and Environment
1280A.6.5.5.4.2 Test Requirements 1285A.6.5.5.5 Beam Failure Detection
and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD
and SSB-based LR in non-DRX mode 1286A.6.5.5.5.1 Test Purpose and
Environment 1286A.6.5.5.5.2 Test Requirements 1290A.6.5.5.6 Beam Failure
Detection and Link Recovery Test for FR1 SCell configured with
CSI-RS-based BFD and SSB-based LR in DRX mode 1290A.6.5.5.6.1 Test
Purpose and Environment 1290A.6.5.5.6.2 Test Requirements 1294A.6.5.6
Active BWP switch 1295A.6.5.6.1 DCI-based and Timer-based Active BWP
Switch 1295A.6.5.6.1.1 NR FR1- NR FR1 DL active BWP switch of SCell with
non-DRX in SA 1295A.6.5.6.1.2 NR FR1 DL active BWP switch with non-DRX
in SA 1302A.6.5.6.2 RRC-based Active BWP Switch 1306A.6.5.6.2.1 NR FR1
DL active BWP switch of Cell with non-DRX in SA 1306A.6.5.6.3
Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs
1310A.6.5.6.3.1 NR FR1- NR FR1 DL active BWP switch on multiple CCs with
non-DRX in SA 1310A.6.5.6.4 SCell dormancy switch 1317A.6.5.6.4.1 NR FR1
PCell SCell dormancy switch of single FR1 SCell outside active time
1317A.6.5.6.4.2 NR FR1 PCell SCell dormancy switch of two FR1 SCells
inside active time 1323A.6.5.6.5 Simultaneous RRC-based Active BWP
Switch on multiple CCs 1330A.6.5.6.5.1 NR FR1- NR FR1 DL active BWP
switch on multiple CCs with non-DRX in SA 1330A.6.5.7 DL interruptions
at switching between two uplink carriers 1335A.6.5.7.1 DL interruptions
at switching between two uplink carriers in FDD-TDD CA 1335A.6.5.7.1.1
Test Purpose and Environment 1335A.6.5.7.1.2 Test Requirements
1339A.6.5.7.2 DL interruptions at switching between two uplink carriers
in TDD-TDD CA 1339A.6.5.7.2.1 Test Purpose and Environment
1339A.6.5.7.2.2 Test Requirements 1343A.6.5.8 UE specific CBW change
1343A.6.5.8.1 UE specific CBW change on PCell in FR1 in non-DRX
1343A.6.5.8.1.1 Test Purpose and Environment 1343A.6.5.8.1.2 Test
Requirements 1347A.6.5.9 Pathloss reference signal switching delay
1347A.6.5.9.1 MAC-CE based pathloss reference signal switch delay
1347A.6.5.9.1.1 Test Purpose and Environment 1347A.6.5.9.1.2 Test
Requirements 1350A.6.6 Measurement procedure 1351A.6.6.1 Intra-frequency
Measurements 1351A.6.6.1.1 SA event triggered reporting tests without
gap under non-DRX 1351A.6.6.1.1.1 Test purpose and Environment
1351A.6.6.1.1.2 Test parameters 1351A.6.6.1.1.3 Test Requirements
1355A.6.6.1.2 SA event triggered reporting tests without gap under DRX
1355A.6.6.1.2.1 Test purpose and Environment 1355A.6.6.1.2.2 Test
parameters 1355A.6.6.1.2.3 Test Requirements 1359A.6.6.1.3 SA event
triggered reporting tests with per-UE gaps under non-DRX 1359A.6.6.1.3.1
Test purpose and Environment 1359A.6.6.1.3.2 Test parameters
1359A.6.6.1.3.3 Test Requirements 1363A.6.6.1.4 SA event triggered
reporting tests with per-UE gaps under DRX 1363A.6.6.1.4.1 Test purpose
and Environment 1363A.6.6.1.4.2 Test parameters 1363A.6.6.1.4.3 Test
Requirements 1367A.6.6.1.5 SA event triggered reporting tests without
gap under non-DRX with SSB index reading 1367A.6.6.1.5.1 Test purpose
and Environment 1367A.6.6.1.5.2 Test parameters 1367A.6.6.1.5.3 Test
Requirements 1369A.6.6.1.6 SA event triggered reporting tests with
per-UE gaps under non-DRX with SSB index reading 1370A.6.6.1.6.1 Test
purpose and Environment 1370A.6.6.1.6.2 Test parameters 1370A.6.6.1.6.3
Test Requirements 1371A.6.6.1.7 SA event triggered reporting tests under
DRX for UE configured with highSpeedMeasFlag-r16 1372A.6.6.1.7.1 Test
purpose and Environment 1372A.6.6.1.7.2 Test parameters 1372A.6.6.1.7.3
Test Requirements 1376A.6.6.2 Inter-frequency Measurements 1376A.6.6.2.1
SA event triggered reporting tests for FR1 without SSB time index
detection when DRX is not used 1376A.6.6.2.1.1 Test Purpose and
Environment 1376A.6.6.2.1.2 Test Requirements 1380A.6.6.2.2 SA event
triggered reporting tests for FR1 without SSB time index detection when
DRX is used 1380A.6.6.2.2.1 Test Purpose and Environment 1380A.6.6.2.2.2
Test Requirements 1384A.6.6.2.3 Void 1385A.6.6.2.4 Void 1385A.6.6.2.5 SA
event triggered reporting tests for FR1 with SSB time index detection
when DRX is not used 1385A.6.6.2.5.1 Test Purpose and Environment
1385A.6.6.2.5.2 Test Requirements 1389A.6.6.2.6 SA event triggered
reporting tests for FR1 with SSB time index detection when DRX is used
1389A.6.6.2.6.1 Test Purpose and Environment 1389A.6.6.2.6.2 Test
Requirements 1393A.6.6.2.7 Void 1394A.6.6.2.8 Void 1394A.6.6.2.9 SA
event triggered reporting tests with additional mandatory gap pattern
1394A.6.6.2.9.1 Test Purpose and Environment 1394A.6.6.2.9.2 Test
Requirements 1397A.6.6.2.10 SA event triggered reporting tests for FR1
when DRX is used 1397A.6.6.2.10.1 Test Purpose and Environment
1397A.6.6.2.10.2 Test Requirements 1401A.6.6.2.11 SA event triggered
reporting tests for FR1 without gap when DRX is not used
1402A.6.6.2.11.1 Test Purpose and Environment 1402A.6.6.2.11.2 Test
Requirements 1405A.6.6.3 Inter-RAT Measurements 1405A.6.6.3.1 SA NR -
E-UTRAN event-triggered reporting in non-DRX in FR1 1405A.6.6.3.1.1 Test
Purpose and Environment 1405A.6.6.3.1.2 Test Requirements 1411A.6.6.3.2
SA NR - E-UTRAN event-triggered reporting in DRX in FR1 1411A.6.6.3.2.1
Test Purpose and Environment 1411A.6.6.3.2.2 Test Requirements
1418A.6.6.3.3 SA NR - E-UTRAN event-triggered reporting in DRX in FR1
for UE configured with highSpeedMeasFlag-r16 1418A.6.6.3.3.1 Test
Purpose and Environment 1418A.6.6.3.3.2 Test Requirements 1425A.6.6.4
L1-RSRP measurement for beam reporting 1425A.6.6.4.1 SSB based L1-RSRP
measurement when DRX is not used 1425A.6.6.4.1.1 Test Purpose and
Environment 1425A.6.6.4.1.2 Test parameters 1425A.6.6.4.1.3 Test
Requirements 1428A.6.6.4.2 SSB based L1-RSRP measurement when DRX is
used 1428A.6.6.4.2.1 Test Purpose and Environment 1428A.6.6.4.2.2 Test
parameters 1429A.6.6.4.2.3 Test Requirements 1432A.6.6.4.3 CSI-RS based
L1-RSRP measurement when DRX is not used 1432A.6.6.4.3.1 Test Purpose
and Environment 1432A.6.6.4.3.2 Test parameters 1433A.6.6.4.3.3 Test
Requirements 1436A.6.6.4.4 CSI-RS based L1-RSRP measurement when DRX is
used 1436A.6.6.4.4.1 Test Purpose and Environment 1436A.6.6.4.4.2 Test
parameters 1437A.6.6.4.4.3 Test Requirements 1440A.6.6.4.5 SSB based
L1-RSRP measurement when DRX is used for UE configured with
*highSpeedMeasFlag-r16* 1440A.6.6.4.5.1 Test Purpose and Environment
1440A.6.6.4.5.2 Test parameters 1441A.6.6.4.5.3 Test Requirements
1444A.6.6.5 1444A.6.6.5.1 SA NR - UTRAN FDD event-triggered reporting in
non-DRX in FR1 1444A.6.6.5.1.1 Test Purpose and Environment
1444A.6.6.5.1.2 Test Requirements 1448A.6.6.6 CLI measurements
1448A.6.6.6.1 SRS-RSRP measurement with DRX 1448A.6.6.6.1.1 Test Purpose
and Environment 1448A.6.6.6.1.2 Test Parameters 1449A.6.6.6.1.3 Test
Requirements 1452A.6.6.6.2 CLI-RSSI measurement with DRX 1452A.6.6.6.2.1
Test Purpose and Environment 1452A.6.6.6.2.2 Test Parameters
1453A.6.6.6.2.3 Test Requirements 1455A.6.6.7 NR measurements with
autonomous gaps 1455A.6.6.7.1 SA intra-frequency CGI identification of
NR neighbor cell in FR1 1455A.6.6.7.1.1 Test Purpose and Environment
1455A.6.6.7.1.2 Test Parameters 1455A.6.6.7.1.3 Test Requirements
1458A.6.6.7.2 Identification of a new CGI of inter-RAT E-UTRA cell using
autonomous gaps in NR SA 1458A.6.6.7.2.1 Test Purpose and Environment
1458A.6.6.7.2.2 Test Requirements 1461A.6.6.8 L1-SINR measurement for
beam reporting 1462A.6.6.8.1 L1-SINR measurement with CSI-RS based CMR
and no dedicated IMR configured when DRX is used 1462A.6.6.8.1.1 Test
Purpose and Environment 1462A.6.6.8.2 L1-SINR measurement with SSB based
CMR and dedicated IMR when DRX is not used 1465A.6.6.8.2.1 Test Purpose
and Environment 1465A.6.6.8.2.2 Test parameters 1466A.6.6.8.2.3 Test
Requirements 1470A.6.6.8.3 L1-SINR measurement with CSI-RS based CMR and
dedicated IMR configured when DRX is not used 1470A.6.6.8.3.1 Test
Purpose and Environment 1470A.6.6.8.3.2 Test parameters 1471A.6.6.8.3.3
Test Requirements 1474A.6.6.9 Idle Mode CA/DC Measurements 1474A.6.6.9.1
SA Idle mode CA/DC measurement for FR1 1474A.6.6.9.1.1 Test Purpose and
Environment 1474A.6.6.9.1.2 Test Requirements 1481A.6.6.10 CSI-RS based
intra-frequency Measurements 1481A.6.6.10.1 SA event triggered reporting
tests without gap under non-DRX 1481A.6.6.10.1.1 Test purpose and
Environment 1481A.6.6.10.1.2 Test Requirements 1484A.6.6.11 CSI-RS based
inter-frequency Measurements 1484A.6.6.11.1 SA event triggered reporting
tests with gap under DRX 1484A.6.6.11.1.1 Test Purpose and Environment
1484A.6.6.11.1.2 Test Requirements 1488A.6.6.12 RSTD measurements 1488A.
6.6.12.1 NR RSTD measurement reporting delay test case for single
positioning frequency layer in FR1 SA 1488A. 6.6.12.1.1 Test Purpose and
Environment 1488A.6.6.12.1.2 Test Requirements 1496A. 6.6.12.2 NR RSTD
measurement reporting delay test case for dual positioning frequency
layers in FR1 SA 1496A. 6.6.12.2.1 Test Purpose and Environment
1496A.6.6.12.2.2 Test Requirements 1503A.6.6.13 PRS-RSRP measurements
1503A.6.6.13.1 PRS-RSRP reporting delay test case for single positioning
frequency layer 1503A.6.6.13.1.1 Test purpose and Environment
1503A.6.6.13.1.2 Test Requirements 1507A.6.6.13.2 PRS-RSRP reporting
delay test case for dual positioning frequency layer 1507A.6.6.13.2.1
Test purpose and Environment 1507A.6.6.13.2.2 Test Requirements
1511A.6.6.14 UE Rx-Tx time difference measurements 1511A.6.6.14.1 UE
Rx-Tx time difference measurement for single positioning frequency layer
in FR1 SA 1511A.6.6.14.1.1 Test purpose and environment 1511A.6.6.14.1.2
Test requirements 1515A.6.6.14.2 UE Rx-Tx time difference measurement
for dual positioning frequency layers in FR1 SA 1515A.6.6.14.2.1 Test
purpose and environment 1515A.6.6.14.2.2 Test requirements 1519A.6.6.15
Idle Mode measurements of inter-RAT DC candidate cells for early
reporting 1519A.6.6.15.1 Test Purpose and Environment 1519A.6.6.15.2
Test Requirements 1526A.6.7 Measurement Performance requirements
1527A.6.7.1 SS-RSRP 1527A.6.7.1.1 SA: intra-frequency case measurement
accuracy with FR1 serving cell and FR1 target cell 1527A.6.7.1.1.1 Test
Purpose and Environment 1527A.6.7.1.1.2 Test parameters 1527A.6.7.1.1.3
Test Requirements 1532A.6.7.1.2 SA inter-frequency case measurement
accuracy with FR1 serving cell and FR1 target cell 1532A.6.7.1.2.1 Test
Purpose and Environment 1532A.6.7.1.2.2 Test parameters 1532A.6.7.1.2.3
Test Requirements 1536A.6.7.1.3 Void 1536A.6.7.2 SS-RSRQ 1536A.6.7.2.1
SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1
target cell 1536A.6.7.2.1.1 Test Purpose and Environment 1536A.6.7.2.1.2
Test Parameters 1537A.6.7.2.1.3 Test Requirements 1542A.6.7.2.2 SA
Inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell 1542A.6.7.2.2.1 Test Purpose and Environment 1542A.6.7.2.2.2
Test Parameters 1542A.6.7.2.2.3 Test Requirements 1547A.6.7.3 SS-SINR
1547A.6.7.3.1 SA intra-frequency measurement accuracy with FR1 serving
cell and FR1 target cell 1547A.6.7.3.1.1 Test Purpose and Environment
1547A.6.7.3.1.2 Test Parameters 1548A.6.7.3.1.3 Test Requirements
1552A.6.7.3.2 SA Inter-frequency measurement accuracy with FR1 serving
cell and FR1 target cell 1552A.6.7.3.2.1 Test Purpose and Environment
1552A.6.7.3.2.2 Test Parameters 1553A.6.7.3.2.3 Test Requirements
1558A.6.7.4 L1-RSRP measurement for beam reporting 1559A.6.7.4.1 SSB
based L1-RSRP measurement 1559A.6.7.4.1.1 Test Purpose and Environment
1559A.6.7.4.1.2 Test parameters 1559A.6.7.4.1.3 Test Requirements
1563A.6.7.4.2 CSI-RS based L1-RSRP measurement on resource set with
repetition off 1563A.6.7.4.2.1 Test Purpose and Environment
1563A.6.7.4.2.2 Test parameters 1564A.6.7.4.2.3 Test Requirements
1568A.6.7.5 E-UTRAN RSRP 1568A.6.7.5.1 SA: inter-RAT measurement
accuracy with FR1 serving cell 1568A.6.7.5.1.1 Test Purpose and
Environment 1568A.6.7.5.1.2 Test parameters 1569A.6.7.5.1.3 Test
Requirements 1575A.6.7.6 E-UTRAN RSRQ 1576A.6.7.6.1 SA: inter-RAT
measurement accuracy with FR1 serving cell 1576A.6.7.6.1.1 Test Purpose
and Environment 1576A.6.7.6.1.2 Test parameters 1576A.6.7.6.1.3 Test
Requirements 1581A.6.7.7 E-UTRAN RS-SINR 1582A.6.7.7.1 SA: inter-RAT
measurement accuracy with FR1 serving cell 1582A.6.7.7.1.1 Test Purpose
and Environment 1582A.6.7.7.1.2 Test parameters 1582A.6.7.7.1.3 Test
Requirements 1588A.6.7.8 CLI measurements 1589A.6.7.8.1 SA SRS-RSRP
measurement accuracy with FR1 serving cell 1589A.6.7.8.1.1 Test Purpose
and Environment 1589A.6.7.8.1.2 Test parameters 1589A.6.7.8.1.3 Test
Requirements 1595A.6.7.8.2 SA CLI-RSSI measurement accuracy with FR1
serving cell 1595A.6.7.8.2.1 Test Purpose and Environment
1595A.6.7.8.2.2 Test parameters 1596A.6.7.8.2.3 Test Requirements
1599A.6.7.9 L1-SINR measurement for beam reporting 1600A.6.7.9.1 L1-SINR
measurement with CSI-RS based CMR and no dedicated IMR configured and
CSI-RS resource set with repetition off 1600A.6.7.9.1.1 Test Purpose and
Environment 1600A.6.7.9.1.2 Test parameters 1600A.6.7.9.1.3 Test
Requirements 1604A.6.7.9.2 L1-SINR measurement with SSB based CMR and
dedicated IMR 1604A.6.7.9.2.1 Test Purpose and Environment
1604A.6.7.9.2.2 Test parameters 1605A.6.7.9.2.3 Test Requirements
1610A.6.7.9.3 L1-SINR measurement with CSI-RS based CMR and dedicated
IMR 1610A.6.7.9.3.1 Test Purpose and Environment 1610A.6.7.9.3.2 Test
parameters 1610A.6.7.9.3.3 Test Requirements 1615A.6.7.10 CSI-RSRP
1615A.6.7.10.1 SA: intra-frequency case measurement accuracy with FR1
serving cell and FR1 target cell 1615A.6.7.10.1.1 Test Purpose and
Environment 1615A.6.7.10.1.2 Test parameters 1616A.6.7.10.1.3 Test
Requirements 1621A.6.7.10.2 SA inter-frequency case measurement accuracy
with FR1 serving cell and FR1 target cell 1621A.6.7.10.2.1 Test Purpose
and Environment 1621A.6.7.10.2.2 Test parameters 1621A.6.7.10.2.3 Test
Requirements 1626A.6.7.11 CSI-RSRQ 1626A.6.7.11.1 SA: Intra-frequency
measurement accuracy with FR1 serving cell and FR1 target cell
1626A.6.7.11.1.1 Test Purpose and Environment 1626A.6.7.11.1.2 Test
Parameters 1626A.6.7.11.1.3 Test Requirements 1631A.6.7.11.2 SA
Inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell 1631A.6.7.11.2.1 Test Purpose and Environment
1631A.6.7.11.2.2 Test Parameters 1631A.6.7.11.2.3 Test Requirements
1636A.6.7.12 CSI-SINR 1637A.6.7.12.1 SA intra-frequency measurement
accuracy with FR1 serving cell and FR1 target cell 1637A.6.7.12.1.1 Test
Purpose and Environment 1637A.6.7.12.1.2 Test Parameters
1637A.6.7.12.1.3 Test Requirements 1641A.6.7.12.2 SA Inter-frequency
measurement accuracy with FR1 serving cell and FR1 target cell
1642A.6.7.12.2.1 Test Purpose and Environment 1642A.6.7.12.2.2 Test
Parameters 1642A.6.7.12.2.3 Test Requirements 1648A.6.7.13 RSTD
measurements 1648A.6.7.13.1 RSTD measurement accuracy test case for
single positioning frequency layer 1648A.6.7.13.1.1 Test purpose and
Environment 1648A.6.7.13.1.2 Test Requirements 1651A.6.7.13.2 RSTD
measurement accuracy test case for dual positioning frequency layer
1651A.6.7.13.2.1 Test purpose and Environment 1651A.6.7.13.2.2 Test
Requirements 1655A.6.7.14 PRS-RSRP measurements 1655A.6.7.14.1 SA:
measurement accuracy with PRS in FR1 1655A.6.7.14.1.1 Test Purpose and
Environment 1655A.6.7.14.1.2 Test parameters 1656A.6.7.14.1.3 Test
Requirements 1660A.6.7.15 UE Rx-Tx time difference measurements
1660A.6.7.15.1 UE Rx-Tx time difference measurement accuracy for single
positioning frequency layer in FR1 SA 1660A.6.7.15.1.1 Test purpose and
environment 1660A.6.7.15.1.2 Test parameters 1661A.6.7.15.1.3 Test
requirements 1664A.7.1 SA: RRC\_IDLE state mobility 1665A.7.1.1 Cell
re-selection to NR 1665A.7.1.1.1 Cell reselection to FR2 intra-frequency
NR case 1665A.7.1.1.1.1 Test Purpose and Environment 1665A.7.1.1.1.2
Test Parameters 1665A.7.1.1.1.3 Test Requirements 1668A.7.1.1.2 Cell
reselection to FR2 inter-frequency NR case 1668A.7.1.1.2.1 Test Purpose
and Environment 1668A.7.1.1.2.2 Test Parameters 1669A.7.1.1.2.3 Test
Requirements 1671A.7.1.1.3 Cell reselection to FR2 intra-frequency NR
case for UE fulfilling low mobility relaxed measurement criterion
1671A.7.1.1.3.1 Test Purpose and Environment 1671A.7.1.1.3.2 Test
Parameters 1671A.7.1.1.3.3 Test Requirements 1674A.7.1.1.4 Cell
reselection to FR2 intra-frequency NR case for UE fulfilling not-at-cell
edge relaxed measurement criterion 1674A.7.1.1.4.1 Test Purpose and
Environment 1674A.7.1.1.4.2 Test Parameters 1674A.7.1.1.4.3 Test
Requirements 1677A.7.1.1.5 Cell reselection to FR2 inter-frequency NR
case for UE fulfilling low mobility relaxed measurement criterion
1677A.7.1.1.5.1 Test Purpose and Environment 1677A.7.1.1.5.2 Test
Parameters 1677A.7.1.1.5.3 Test Requirements 1680A.7.1.1.6 Cell
reselection to FR2 inter-frequency NR case for UE fulfilling not-at-cell
edge relaxed measurement criterion 1680A.7.1.1.6.1 Test Purpose and
Environment 1680A.7.1.1.6.2 Test Parameters 1680A.7.1.1.6.3 Test
Requirements 1683A.7.2 SA: RRC\_INACTIVE state mobility 1683A.7.3
RRC\_CONNECTED state mobility 1683A.7.3.1 Handover 1683A.7.3.1.1
Inter-frequency handover from FR1 to FR2; unknown target cell
1683A.7.3.1.1.1 Test Purpose and Environment 1683A.7.3.1.1.2 Test
Parameters 1683A.7.3.1.1.3 Test Requirements 1687A.7.3.1.2
Intra-frequency handover from FR2 to FR2; unknown target cell
1687A.7.3.1.2.1 Test Purpose and Environment 1687A.7.3.1.2.2 Test
Parameters 1687A.7.3.1.2.3 Test Requirements 1690A.7.3.1.3
Inter-frequency handover from FR2 to FR2; unknown target cell
1690A.7.3.1.3.1 Test Purpose and Environment 1690A.7.3.1.3.2 Test
Parameters 1690A.7.3.1.3.3 Test Requirements 1691A.7.3.1.4 Inter-band
inter-frequency synchronous DAPS handover from FR1 to FR2
1692A.7.3.1.4.1 Test Purpose and Environment 1692A.7.3.1.4.2 Test
Parameters 1692A.7.3.1.4.3 Test Requirements 1699A.7.3.1.5 Inter-band
inter-frequency asynchronous DAPS handover from FR1 to FR2
1699A.7.3.1.5.1 Test Purpose and Environment 1699A.7.3.1.5.2 Test
Parameters 1699A.7.3.1.5.3 Test Requirements 1706A.7.3.2 RRC Connection
Mobility Control 1706A.7.3.2.1 SA: RRC Re-establishment 1706A.7.3.2.1.1
Intra-frequency RRC Re-establishment in FR2 1706A.7.3.2.1.2
Inter-frequency RRC Re-establishment in FR2 1709A.7.3.2.1.3
Intra-frequency RRC Re-establishment in FR2 without serving cell timing
1712A.7.3.2.1.3.1 Test Purpose and Environment 1712A.7.3.2.1.3.2 Test
Requirements 1714A.7.3.2.2 Random Access 1715A.7.3.2.2.1 4-step RA type
contention based random access test in FR2 for NR Standalone
1715A.7.3.2.2.2 4-step RA type non-contention based random access test
in FR2 for NR Standalone 1719A.7.3.2.2.3 2-step RA type contention based
random access test in FR2 for NR Standalone 1724A.7.3.2.2.4 2-step RA
type non-contention based random access test in FR2 for NR Standalone
1727A.7.3.2.3 SA: RRC Connection Release with Redirection
1730A.7.3.2.3.1 Redirection from NR in FR2 to NR in FR2 1730A.7.3.3
Conditional Handover 1734A.7.3.3.1 Intra-frequency conditional handover
from FR2 to FR2 1734A.7.3.3.1.1 Test Purpose and Environment
1734A.7.3.3.1.2 Test Parameters 1734A.7.3.3.1.2.3 Test Requirements
1737A.7.3.3.2 Inter-frequency conditional handover from FR2 to FR2;
unknown target cell 1737A.7.3.3.2.1 Test Purpose and Environment
1737A.7.3.3.2.2 Test Parameters 1737A.7.3.3.2.3 Test Requirements
1740A.7.4 Timing 1740A.7.4.1 UE transmit timing 1740A.7.4.1.1 NR UE
Transmit Timing Test for FR2 1740A.7.4.1.1.1 Test Purpose and
environment 1740A.7.4.1.1.2 Test requirements 1743A.7.4.2 UE timer
accuracy 1744A.7.4.3 Timing advance 1744A.7.4.3.1 SA FR2 timing advance
adjustment accuracy 1744A.7.4.3.1.1 Test Purpose and Environment
1744A.7.4.3.1.2 Test Parameters 1744A.7.4.3.1.3 Test Requirements
1747A.7.5 Signaling characteristics 1748A.7.5.1 Radio link Monitoring
1748A.7.5.1.1 Radio Link Monitoring Out-of-sync Test for FR2 PCell
configured with SSB-based RLM RS in non-DRX mode 1748A.7.5.1.1.1 Test
Purpose and Environment 1748A.7.5.1.1.2 Test Requirements 1751A.7.5.1.2
Radio Link Monitoring In-sync Test for FR2 PCell configured with
SSB-based RLM RS in non-DRX mode 1752A.7.5.1.2.1 Test Purpose and
Environment 1752A.7.5.1.2.2 Test Requirements 1756A.7.5.1.3 Radio Link
Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM
RS in DRX mode 1757A.7.5.1.3.1 Test Purpose and Environment
1757A.7.5.1.3.2 Test Requirements 1761A.7.5.1.4 Radio Link Monitoring
In-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode
1761A.7.5.1.4.1 Test Purpose and Environment 1761A.7.5.1.4.2 Test
Requirements 1766A.7.5.1.5 Radio Link Monitoring Out-of-sync Test for
FR2 PCell configured with CSI-RS-based RLM in non-DRX mode
1766A.7.5.1.5.1 Test Purpose and Environment 1766A.7.5.1.5.2 Test
Requirements 1771A.7.5.1.6 Radio Link Monitoring In-sync Test for FR2
PCell configured with CSI-RS-based RLM in non-DRX mode 1771A.7.5.1.6.1
Test Purpose and Environment 1771A.7.5.1.6.2 Test Requirements
1775A.7.5.1.7 Radio Link Monitoring Out-of-sync Test for FR2 PCell
configured with CSI-RS-based RLM in DRX mode 1775A.7.5.1.7.1 Test
Purpose and Environment 1775A.7.5.1.7.2 Test Requirements 1779A.7.5.1.8
Radio Link Monitoring In-sync Test for FR2 PCell configured with
CSI-RS-based RLM in DRX mode 1779A.7.5.1.8.1 Test Purpose and
Environment 1779A.7.5.1.8.2 Test Requirements 1784A.7.5.1.9 UE Radio
Link Monitoring Scheduling Restrictions on FR2 1784A.7.5.1.9.1 Test
Purpose and Environment 1784A.7.5.1.9.2 Test Requirements 1787A.7.5.2
Interruption 1787**A.7.5.2.1** Interruptions during measurements on
deactivated NR SCC in FR2 1787A.7.5.2.2 SA interruptions at NR SRS
carrier-based switching 1791A.7.5.2.2.1 Test Purpose and Environment
1791A.7.5.2.2.2 Test Parameters 1791A.7.5.2.2.3 Test Requirements
1793A.7.5.3 SCell Activation and Deactivation Delay 1793A.7.5.3.1 SCell
Activation and deactivation for SCell in FR2 intra-band in non-DRX
1793A.7.5.3.1.1 Test Purpose and Environment 1793A.7.5.3.1.2 Test
Requirements 1795A.7.5.3.2 SCell Activation and deactivation for FR1+FR2
inter-band with target SCell in FR2 1795A.7.5.3.2.1 Test Purpose and
Environment 1795A.7.5.3.2.2 Test Requirements 1799A.7.5.3.3 SCell
Activation and deactivation for SCell in FR2 inter-band in non-DRX
1800A.7.5.3.3.1 Test Purpose and Environment 1800A.7.5.3.3.2 Test
Requirements 1803A.7.5.3.4 Direct SCell activation at SCell addition of
known SCell in FR2 1804A.7.5.3.4.1 Test Purpose and Environment
1804A.7.5.3.4.2 Test Requirements 1807A.7.5.3.5 Direct SCell activation
at handover with known SCell in FR2 1808A.7.5.3.5.1 Test Purpose and
Environment 1808A.7.5.3.5.2 Test Requirements 1811A.7.5.4 Void
1812A.7.5.5 Beam Failure Detection and Link recovery procedures
1812A.7.5.5.1 Beam Failure Detection and Link Recovery Test for FR2
PCell configured with SSB-based BFD and LR in non-DRX mode
1812A.7.5.5.1.1 Test Purpose and Environment 1812A.7.5.5.1.2 Test
Requirements 1816A.7.5.5.2 Beam Failure Detection and Link Recovery Test
for FR2 PCell configured with SSB-based BFD and LR in DRX mode
1817A.7.5.5.2.1 Test Purpose and Environment 1817A.7.5.5.2.2 Test
Requirements 1820A.7.5.5.3 Beam Failure Detection and Link Recovery Test
for FR2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode
1821A.7.5.5.3.1 Test Purpose and Environment 1821A.7.5.5.3.2 Test
Requirements 1825A.7.5.5.4 Beam Failure Detection and Link Recovery Test
for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode
1826A.7.5.5.4.1 Test Purpose and Environment 1826A.7.5.5.4.2 Test
Requirements 1830A.7.5.5.5 Scheduling availability restriction during
Beam Failure Detection and Link Recovery for FR2 PCell configured with
SSB-based BFD and LR in non-DRX mode 1831A.7.5.5.5.1 Test Purpose and
Environment 1831A.7.5.5.5.2 Test Requirements 1834A.7.5.5.6 Beam Failure
Detection and Link Recovery Test for FR2 SCell configured with
CSI-RS-based BFD and LR in non-DRX mode 1835A.7.5.5.6.1 Test Purpose and
Environment 1835A.7.5.5.6.2 Test Requirements 1839A.7.5.5.7 Beam Failure
Detection and Link Recovery Test for FR2 SCell configured with
CSI-RS-based BFD and LR in DRX mode 1840A.7.5.5.7.1 Test Purpose and
Environment 1840A.7.5.5.7.2 Test Requirements 1844A.7.5.6 Active BWP
switch 1845A.7.5.6.1 DCI-based and Timer-based Active BWP Switch
1845A.7.5.6.1.1 NR FR2- NR FR2 DL active BWP switch of SCell with
non-DRX in SA 1845A.7.5.6.1.2 NR FR1- NR FR2 DL active BWP switch of
SCell with non-DRX in SA A.7.5.6.1.2.1 Test Purpose and Environment
1849A.7.5.6.1.3 NR FR2 DL active BWP switch with non-DRX in SA
1854A.7.5.6.1.3.1 Test Purpose and Environment 1854A.7.5.6.1.3.2 Test
Requirements 1857A.7.5.6.2 RRC-based Active BWP Switch 1857A.7.5.6.3
Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs
1861A.7.5.6.3.1 Active BWP switch on multiple SCells with non-DRX in SA
1861A.7.5.6.4 SCell dormancy switch 1864A.7.5.6.4.1 NR FR2 PCell SCell
dormancy switch of single FR2 SCell inside active time 1864A.7.5.6.4.2
NR FR1 PCell SCell dormancy switch of two FR2 SCells outside active time
1869A.7.5.6.4.2.2 Test Requirements 1874A.7.5.6.5 Simultaneous RRC-based
Active BWP Switch on multiple CCs 1874A.7.5.6.5.1 Active BWP switch on
multiple SCells with non-DRX in SA 1874A.7.5.7 PSCell addition and
release delay 1877A.7.5.7.1 Addition and Release Delay of known NR
PSCell 1877A.7.5.7.1.1 Test Purpose and Environment 1877A.7.5.7.2
Addition and Release Delay of unknown NR PSCell 1881A.7.5.7.2.1 Test
Purpose and Environment 1881A.7.5.7.2.2 Test Requirements 1884A.7.5.8
Active TCI state switch delay 1884A.7.5.8.1 MAC-CE based active TCI
state switch 1884A.7.5.8.2 RRC based active TCI state switch 1888A.7.5.9
Uplink spatial relation switch delay 1892A.7.5.9.1 MAC-CE based Spatial
Relation switch 1892A.7.5.9.1.1 NR PCell FR2 spatial relation associated
with known DL-RS 1892A.7.5.9.1.1.2 Test Requirements 1895A.7.5.9.2 RRC
based spatial relation switch 1895A.7.5.9.2.1 NR PCell FR2 spatial
relation switch associated with a known DL-RS 1895A.7.5.9.2.1.1 Test
Purpose and Environment 1895A.7.5.9.2**.1**.2 Test Requirements
1898A.7.5.10 UE specific CBW change 1898A.7.5.10.1 NR FR2 UE specific
CBW change of PCell with non-DRX in SA 1898A.7.5.10.1.1 Test Purpose and
Environment 1898A.7.5.10.1.2 Test Requirements 1901A.7.6 Measurement
procedure 1902A.7.6.1 Intra-frequency Measurements 1902A.7.6.1.1 SA
event triggered reporting test without gap under non-DRX 1902A.7.6.1.1.1
Test purpose and Environment 1902A.7.6.1.1.2 Test Requirements
1904A.7.6.1.2 SA event triggered reporting test without gap under DRX
1905A.7.6.1.2.1 Test purpose and Environment 1905A.7.6.1.2.2 Test
Requirements 1907A.7.6.1.3 SA event triggered reporting test with per-UE
gaps under non-DRX 1908A.7.6.1.3.1 Test purpose and Environment
1908A.7.6.1.3.2 Test Requirements 1910A.7.6.1.4 SA event triggered
reporting test with per-UE gaps under DRX 1911A.7.6.1.4.1 Test purpose
and Environment 1911A.7.6.1.4.2 Test Requirements 1914A.7.6.2
Inter-frequency Measurements 1915A.7.6.2.1 SA event triggered reporting
tests For FR2 without SSB time index detection when DRX is not used
(PCell in FR2) 1915A.7.6.2.1.1 Test Purpose and Environment
1915A.7.6.2.1.2 Test Requirements 1918A.7.6.2.2 SA event triggered
reporting tests For FR2 without SSB time index detection when DRX is
used (PCell in FR2) 1918A.7.6.2.2.1 Test Purpose and Environment
1918A.7.6.2.2.2 Test Requirements 1922A.7.6.2.3 SA event triggered
reporting tests For FR2 with SSB time index detection when DRX is not
used (PCell in FR2) 1922A.7.6.2.3.1 Test Purpose and Environment
1922A.7.6.2.3.2 Test Requirements 1926A.7.6.2.4 SA event triggered
reporting tests For FR2 with SSB time index detection when DRX is used
(PCell in FR2) 1926A.7.6.2.4.1 Test Purpose and Environment
1926A.7.6.2.4.2 Test Requirements 1930A.7.6.2.5 SA event triggered
reporting tests for FR2 without SSB time index detection when DRX is not
used (PCell in FR1) 1930A.7.6.2.5.1 Test Purpose and Environment
1930A.7.6.2.5.2 Test Requirements 1934A.7.6.2.6 SA event triggered
reporting tests for FR2 without SSB time index detection when DRX is
used (PCell in FR1) 1935A.7.6.2.6.1 Test Purpose and Environment
1935A.7.6.2.6.2 Test Requirements 1939A.7.6.2.7 SA event triggered
reporting tests for FR2 with SSB time index detection when DRX is not
used (PCell in FR1) 1940A.7.6.2.7.1 Test Purpose and Environment
1940A.7.6.2.7.2 Test Requirements 1944A.7.6.2.8 SA event triggered
reporting tests for FR2 with SSB time index detection when DRX is used
(PCell in FR1) 1945A.7.6.2.8.1 Test Purpose and Environment
1945A.7.6.2.8.2 Test Requirements 1949A.7.6.2.9 SA event triggered
reporting tests For FR2 without SSB time index detection when DRX is not
used (PCell in FR2) (rel16 additional mandatory gap pattern 17)
1950A.7.6.2.9.1 Test Purpose and Environment 1950A.7.6.2.9.2 Test
Requirements 1953A.7.6.2.10 SA event triggered reporting test without
gap under non-DRX 1953A.7.6.2.10.1 Test Purpose and Environment
1953A.7.6.2.10.2 Test Requirements 1955A.7.6.2.11 SA event triggered
reporting test without gap under DRX 1955A.7.6.2.11.1 Test Purpose and
Environment 1955A.7.6.2.11.2 Test Requirements 1958A.7.6.3 L1-RSRP
measurement for beam reporting 1959A.7.6.3.1 SSB based L1-RSRP
measurement when DRX is not used 1959A.7.6.3.1 SSB based L1-RSRP
measurement when DRX is not used 1959A.7.6.3.1.1 Test Purpose and
Environment 1959A.7.6.3.1.2 Test parameters 1959A.7.6.3.1.3 Test
Requirements 1961A.7.6.3.2 SSB based L1-RSRP measurement when DRX is
used 1961A.7.6.3.2.1 Test Purpose and Environment 1961A.7.6.3.2.2 Test
parameters 1962A.7.6.3.2.3 Test Requirements 1964A.7.6.3.3 CSI-RS based
L1-RSRP measurement when DRX is not used 1964A.7.6.3.3.1 Test Purpose
and Environment 1964A.7.6.3.3.2 Test parameters 1965A.7.6.3.3.3 Test
Requirements 1967A.7.6.3.4 CSI-RS based L1-RSRP measurement when DRX is
used 1968A.7.6.3.4.1 Test Purpose and Environment 1968A.7.6.3.4.2 Test
parameters 1968A.7.6.3.3.3 Test Requirements 1970A.7.6.4 CLI
measurements 1971A.7.6.4.1 SRS-RSRP measurement with non-DRX
1971A.7.6.4.1.1 Test Purpose and Environment 1971A.7.6.4.1.2 Test
Parameters 1971A.7.6.4.1.3 Test Requirements 1973A.7.6.4.2 CLI-RSSI
measurement with non-DRX 1973A.7.6.4.2.1 Test Purpose and Environment
1973A.7.6.4.2.2 Test Parameters 1974A.7.6.4.2.3 Test Requirements
1975A.7.6.5 NR Measurements with autonomous gaps 1976A.7.6.5.1 SA
interfrequency CGI reporting in autonomous gaps test (PCell in FR2)
1976A.7.6.5.1.1 Test Purpose and Environment 1976A.7.6.5.1.2 Test
Requirements 1979A.7.6.6 L1-SINR measurement for beam reporting
1979A.7.6.6.1 L1-SINR measurement with CSI-RS based CMR and no dedicated
IMR configured when DRX is not used 1979A.7.6.6.1.1 Test Purpose and
Environment 1979A.7.6.6.1.2 Test parameters 1979A.7.6.6.1.3 Test
Requirements 1981A.7.6.6.2 L1-SINR measurement with SSB based CMR and
dedicated IMR when DRX is used 1981A.7.6.6.2.1 Test Purpose and
Environment 1981A.7.6.6.2.2 Test parameters 1982A.7.6.6.2.3 Test
Requirements 1984A.7.6.6.3 L1-SINR measurement with CSI-RS based CMR and
dedicated IMR configured when DRX is used 1984A.7.6.6.3.1 Test Purpose
and Environment 1984A.7.6.6.3.2 Test parameters 1985A.7.6.6.3.3 Test
Requirements 1987A.7.6.7 CSI-RS based intra-frequency Measurements
1987A.7.6.7.1 SA event triggered reporting test without gap under DRX
for CSI-RS based intra-frequency measurement 1987A.7.6.7.1.1 Test
purpose and Environment 1987A.7.6.7.1.2 Test Requirements 1990A.7.6.8
CSI-RS based inter-frequency Measurements 1990A.7.6.8.1 SA event
triggered reporting tests for FR2 CSI-RS based measurement when non-DRX
is used (PCell in FR2) 1990A.7.6.8.1.1 Test Purpose and Environment
1990A.7.6.2.2.2 Test Requirements 1994A.7.6.9 RSTD measurements
1994A.7.6.9.1 NR RSTD measurement reporting delay test case for single
positioning frequency layer in FR2 SA 1994A.7.6.9.1.1 Test Purpose and
Environment 1994A.7.6.9.1.2 Test Requirements 2000A.7.6.9.2 NR RSTD
measurement reporting delay test case for dual positioning frequency
layers in FR2 SA 2000A.7.6.9.2.1 Test Purpose and Environment
2000A.7.6.9.2.2 Test Requirements 2007A.7.6.10 PRS-RSRP measurements
2007A.7.6.10.1 PRS-RSRP reporting delay test case for single positioning
frequency layer 2007A.7.6.10.1.1 Test Purpose and Environment
2007A.7.6.10.1.2 Test Requirements 2011A.7.6.10.2 PRS-RSRP reporting
delay test case for dual positioning frequency layer 2011A.7.6.10.2.1
Test Purpose and Environment 2011A.7.6.10.2.2 Test Requirements
2014A.7.6.11 UE Rx-Tx time difference measurements 2014A.7.6.11.1 UE
Rx-Tx time difference measurements for single positioning frequency
layer in FR2 SA 2014A.7.6.11.1.1 Test purpose and environment
2014A.7.6.11.1.2 Test requirements 2018A.7.6.11.2 UE Rx-Tx time
difference measurement period for dual positioning frequency layers in
FR2 SA 2018A.7.6.11.2.1 Test purpose and environment 2018A.7.6.11.2.2
Test requirements 2022A.7.7 Measurement Performance requirements
2022A.7.7.1 SS-RSRP 2022A.7.7.1.1 SA intra-frequency case measurement
accuracy with FR2 serving cell and FR2 target cell 2022A.7.7.1.1.1 Test
Purpose and Environment 2022A.7.7.1.1.2 Test parameters 2023A.7.7.1.1.3
Test Requirements 2027A.7.7.1.2 SA inter-frequency case measurement
accuracy with FR2 serving cell and FR2 target cell 2027A.7.7.1.2.1 Test
Purpose and Environment 2027A.7.7.1.2.2 Test parameters 2028A.7.7.1.2.3
Test Requirements 2032A.7.7.1.3 SA inter-frequency measurement accuracy
with FR1 serving cell and FR2 target cell 2033A.7.7.1.3.1 Test Purpose
and Environment 2033A.7.7.1.3.2 Test parameters 2033A.7.7.1.3.3 Test
Requirements 2037A.7.7.2 SS-RSRQ 2037A.7.7.2.1 SA intra-frequency
measurement accuracy with FR2 serving cell and FR2 target cell
2037A.7.7.2.1.1 Test Purpose and Environment 2037A.7.7.2.1.2 Test
Parameters 2037A.7.7.2.1.3 Test Requirements 2039A.7.7.2.2 SA
Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 2039A.7.7.2.2.1 Test Purpose and Environment 2039A.7.7.2.2.2
Test Parameters 2039A.7.7.2.2.3 Test Requirements 2041A.7.7.3 SS-SINR
2041A.7.7.3.1 SA intra-frequency case measurement accuracy with FR2
serving cell and FR2 target cell 2041A.7.7.3.1.1 Test Purpose and
Environment 2041A.7.7.3.1.2 Test Parameters 2041A.7.7.3.1.3 Test
Requirements 2044A.7.7.3.2 SA Inter-frequency measurement accuracy with
FR2 serving cell and FR2 TDD target cell 2044A.7.7.3.2.1 Test Purpose
and Environment 2044A.7.7.3.2.2 Test Parameters 2044A.7.7.3.2.3 Test
Requirements 2046A.7.7.4 L1-RSRP measurement for beam reporting
2046A.7.7.4.1 SSB based L1-RSRP measurement 2046A.7.7.4.1.1 Test Purpose
and Environment 2046A.7.7.4.1.2 Test parameters 2047A.7.7.4.1.3 Test
Requirements 2049A.7.7.4.2 CSI-RS based L1-RSRP measurement on resource
set with repetition off 2050A.7.7.4.2.1 Test Purpose and Environment
2050A.7.7.4.2.2 Test parameters 2050A.7.7.4.2.3 Test Requirements
2052A.7.7.5 CLI measurements 2053A.7.7.5.1 SA SRS-RSRP measurement
accuracy with FR2 serving cell 2053A.7.7.5.1.1 Test Purpose and
Environment 2053A.7.7.5.1.2 Test parameters 2053A.7.7.5.1.3 Test
Requirements 2056A.7.7.5.2 SA CLI-RSSI measurement accuracy with FR2
serving cell 2057A.7.7.5.2.1 Test Purpose and Environment
2057A.7.7.5.2.2 Test parameters 2057A.7.7.5.2.3 Test Requirements
2059A.7.7.6 L1-SINR measurement for beam reporting 2060A.7.7.6.1 L1-SINR
measurement with CSI-RS based CMR and no dedicated IMR configured and
CSI-RS resource set with repetition off 2060A.7.7.6.1.1 Test Purpose and
Environment 2060A.7.7.6.1.2 Test parameters 2060A.7.7.6.1.3 Test
Requirements 2062A.7.7.6.2 L1-SINR measurement with SSB based CMR and
dedicated IMR 2063A.7.7.6.2.1 Test Purpose and Environment
2063A.7.7.6.2.2 Test parameters 2063A.7.7.6.2.3 Test Requirements
2065A.7.7.6.3 L1-SINR measurement with CSI-RS based CMR and dedicated
IMR 2066A.7.7.6.3.1 Test Purpose and Environment 2066A.7.7.6.3.2 Test
parameters 2066A.7.7.6.3.3 Test Requirements 2068A.7.7.7 CSI-RSRP
2069A.7.7.7.1 SA intra-frequency case measurement accuracy with FR2
serving cell and FR2 target cell 2069A.7.7.7.1.1 Test Purpose and
Environment 2069A.7.7.7.1.2 Test parameters 2069A.7.7.7.1.3 Test
Requirements 2072A.7.7.7.2 SA inter-frequency case measurement accuracy
with FR2 serving cell and FR2 target cell 2073A.7.7.7.2.1 Test Purpose
and Environment 2073A.7.7.7.2.2 Test parameters 2073A.7.7.7.2.3 Test
Requirements 2076A.7.7.8 CSI-RSRQ 2077A.7.7.8.1 SA intra-frequency
measurement accuracy with FR2 serving cell and FR2 target cell
2077A.7.7.8.1.1 Test Purpose and Environment 2077A.7.7.8.1.2 Test
Parameters 2077A.7.7.8.1.3 Test Requirements 2079A.7.7.8.2 SA
Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 2079A.7.7.8.2.1 Test Purpose and Environment 2079A.7.7.8.2.2
Test Parameters 2079A.7.7.8.2.3 Test Requirements 2081A.7.7.9 CSI-SINR
2081A.7.7.9.1 SA intra-frequency case measurement accuracy with FR2
serving cell and FR2 target cell 2081A.7.7.9.1.1 Test Purpose and
Environment 2081A.7.7.9.1.2 Test Parameters 2081A.7.7.9.1.3 Test
Requirements 2084A.7.7.9.2 SA Inter-frequency measurement accuracy with
FR2 serving cell and FR2 TDD target cell 2084A.7.7.9.2.2 Test Parameters
2084A.7.7.9.2.3 Test Requirements 2086A.7.7.10 RSTD measurements
2086A.7.7.10.1 RSTD measurement accuracy test case for single
positioning frequency layer 2086A.7.7.10.1.1 Test purpose and
Environment 2086A.7.7.10.1.2 Test Requirements 2089A.7.7.10.2 RSTD
measurement accuracy test case for dual positioning frequency layer
2089A.7.7.10.2.1 Test purpose and Environment 2089A.7.7.10.2.2 Test
Requirements 2092A.7.7.11 PRS-RSRP measurements 2092A.7.7.11.1 SA
measurement accuracy with PRS in FR2 2092A.7.7.11.1.1 Test Purpose and
Environment 2092A.7.7.11.1.2 Test parameters 2092A.7.7.11.1.3 Test
Requirements 2096A.7.7.12 UE Rx-Tx time difference measurements
2097A.7.7.12.1 UE Rx-Tx time difference measurement accuracy for single
positioning frequency layer in FR2 SA 2097A.7.7.12.1.1 Test purpose and
environment 2097A.7.7.12.1.2 Test parameters 2097A.7.7.12.1.3 Test
requirements 2100A.8 E-UTRA standalone tests for NR RRM 2100A.8.1 Void
2101A.8.2 RRC\_IDLE state mobility 2101A.8.2.1 Inter-RAT NR Cell
re-selection 2101A.8.2.1.1 E-UTRA Cell reselection to higher priority NR
target Cell in FR1 2101A.8.2.1.1.1 Test Purpose and Environment
2101A.8.2.1.1.2 Test Requirements 2106A.8.2.1.2 E-UTRA Cell reselection
to lower priority NR target Cell in FR1 for UE configured with
highSpeedInterRAT-NR-r16 2107A.8.2.1.2.1 Test Purpose and Environment
2107A.8.2.1.2.2 Test Requirements 2112A.8.2.2 E-UTRA -- NR Inter-RAT
Early Measruement Reporting 2113A.8.2.2.1 E-UTRA -- NR Early Measurement
Reporting for NR in FR1 2113A.8.2.2.1.1 Test Purpose and Environment
2113A.8.2.2.1.2 Test Requirements 2118A.8.2.2.2 E-UTRA -- NR Early
Measurement Reporting for NR in FR2 2118A.8.2.2.2.1 Test Purpose and
Environment 2118A.8.2.2.2.2 Test Requirements 2121A.8.3 RRC\_CONNECTED
state mobility 2122A.8.3.1 Handover 2122A.8.3.1.1 E-UTRAN - NR handover
in FR1 2122A.8.3.1.1.1 Test Purpose and Environment 2122A.8.3.1.1.2 Test
Requirements 2127A.8.4 Measurement procedure 2127A.8.4.1 E-UTRA -- NR
Inter-RAT SFTD Measurement Delay 2127A.8.4.1.1 E-UTRA -- NR Inter-RAT
SFTD Measurement Delay in non-DRX 2127A.8.4.1.1.1 Test Purpose and
Environment 2127A.8.4.1.1.2 Test Requirements 2129A.8.4.1.2 E-UTRA -- NR
Inter-RAT SFTD Measurement Delay in DRX 2130A.8.4.1.2.1 Test Purpose and
Environment 2130A.8.4.1.2.2 Test Requirements 2131A.8.4.2 E-UTRA -- NR
Inter-RAT Measurements 2131A.8.4.2.1 NR Inter-RAT event triggered
reporting tests for FR1 without SSB time index detection when DRX is not
used 2131A.8.4.2.1.1 Test Purpose and Environment 2131A.8.4.2.1.2 Test
Requirements 2136A.8.4.2.2 NR Inter-RAT event triggered reporting tests
for FR1 without SSB time index detection when DRX is used
2136A.8.4.2.2.1 Test Purpose and Environment 2136A.8.4.2.2.2 Test
Requirements 2140A.8.4.2.3 NR Inter-RAT event triggered reporting tests
for FR1 with SSB time index detection when DRX is not used
2140A.8.4.2.3.1 Test Purpose and Environment 2140A.8.4.2.3.2 Test
Requirements 2145A.8.4.2.4 NR Inter-RAT event triggered reporting tests
for FR1 with SSB time index detection when DRX is used 2145A.8.4.2.4.1
Test Purpose and Environment 2145A.8.4.2.4.2 Test Requirements
2149A.8.4.2.5 NR Inter-RAT event triggered reporting tests for FR2
without SSB time index detection when DRX is not used 2149A.8.4.2.5.1
Test Purpose and Environment 2149A.8.4.2.5.2 Test Requirements
2151A.8.4.2.6 NR Inter-RAT event triggered reporting tests for FR2
without SSB time index detection when DRX is used 2152A.8.4.2.6.1 Test
Purpose and Environment 2152A.8.4.2.6.2 Test Requirements 2154A.8.4.2.7
NR Inter-RAT event triggered reporting tests for FR2 with SSB time index
detection when DRX is not used 2155A.8.4.2.7.1 Test Purpose and
Environment 2155A.8.4.2.7.2 Test Requirements 2157A.8.4.2.8 NR Inter-RAT
event triggered reporting tests for FR2 with SSB time index detection
when DRX is used 2158A.8.4.2.8.1 Test Purpose and Environment
2158A.8.4.2.8.2 Test Requirements 2160A.8.4.2.9 NR Inter-RAT event
triggered reporting tests for FR1 with SSB time index detection in DRX
for UE configured with highSpeedInterRAT-NR-r16 2161A.8.4.2.9.1 Test
Purpose and Environment 2161A.8.4.2.9.2 Test Requirements 2167A.8.5
Measurement performance 2167A.8.5.1 SFTD accuracy 2167A.8.5.1.1 SFTD
accuracy 2167A.8.5.1.1.1 Test Purpose 2167A.8.5.1.1.2 Test Environment
2167A.8.5.1.1.3 Test Requirements 2173A.8.5.2 E-UTRA -- NR Inter-RAT
Measurement Performance requirements 2173A.8.5.2.1.1 E-UTRAN -- NR
inter-RAT measurements with FR1 target cell 2173A.8.5.2.1.2 E-UTRAN --
NR inter-RAT measurements with FR2 target cell 2178A.8.5.2.1.2.1 Test
Purpose and Environment 2178A.8.5.2.1.2.2 Test Parameters
2178A.8.5.2.1.2.3 Test Requirements 2180A.8.5.2.2 SS-RSRQ
2180A.8.5.2.2.1 E-UTRAN -- NR inter-RAT measurements with FR1 target
cell 2180A.8.5.2.2.2 E-UTRAN -- NR inter-RAT measurements with FR2
target cell 2185A.8.5.2.2.2.1 Test Purpose and Environment
2185A.8.5.2.2.2.2 Test Parameters 2185A.8.5.2.2.2.3 Test Requirements
2187A.8.5.2.3 SS-SINR 2187A.8.5.2.3.1 E-UTRAN -- NR inter-RAT
measurements with FR1 target cell 2187A.8.5.2.3.2 E-UTRAN -- NR
inter-RAT measurements with FR2 target cell 2191A.8.5.2.3.2.1 Test
Purpose and Environment 2191A.8.5.2.3.2.2 Test Parameters
2191A.8.5.2.3.2.3 Test Requirements 2193A.9 V2X Tests 2194A.9.1 V2X
Tests in FR1 2194A.9.1.1 Test for V2X UE Transmit Timing 2194A.9.1.1.1
Test for GNSS as Synchronization Reference Source 2194A.9.1.1.1.1 Test
Purpose and Environment 2194A.9.1.1.1.2 Test requirements 2194A.9.1.1.2
Test for SyncRef UE as Synchronization Reference Source 2194A.9.1.1.2.1
Test Purpose and Environment 2194A.9.1.1.2.2 Test requirements
2195A.9.1.1.3 Test for FR1 NR Cell as Synchronization Reference Source
2195A.9.1.1.3.1 Test Purpose and Environment 2195A.9.1.1.3.2 Test
requirements 2198A.9.1.2 Test for Initiation/Cease of S-SSB Transmission
with V2X Sidelink Communication 2198A.9.1.2.1 Test for FR1 NR Cell as
synchronization reference source without gap under non-DRX
2198A.9.1.2.1.1 Test Purpose and Environment 2198A.9.1.2.1.2 Test
Requirements 2202A.9.1.2.2 Test for SyncRef UE as synchronization
reference source 2202A.9.1.2.2.1 Test Purpose and Environment
2202A.9.1.2.2.2 Test Requirements 2203A.9.1.3 Test for V2X
Synchronization Reference Selection/Reselection 2204A.9.1.3.1 Test for
GNSS configured as the highest priority 2204A.9.1.3.1.1 Test Purpose and
Environment 2204A.9.1.3.1.2 Test Requirements 2206A.9.1.3.2 Test for FR1
NR Cell configured as the highest priority 2208A.9.1.3.2.1 Test Purpose
and Environment 2208A.9.1.3.2.2 Test Requirements 2210A.9.1.4 Test for
L1 SL-RSRP Measurement 2211A.9.1.4.1 Test for V2X UE Autonomous Resource
Selection/Reselection 2211A.9.1.4.1.1 Test Purpose and Environment
2211A.9.1.4.1.2 Test Requirements 2214A.9.1.4.2 Test for V2X UE Resource
Pre-emption 2215A.9.1.4.2.1 Test Purpose and Environment 2215A.9.1.4.2.2
Test Requirements 2218A.9.1.4.3 Test for V2X UE Resource Re-evaluation
2218A.9.1.4.3.1 Test Purpose and Environment 2218A.9.1.4.3.2 Test
Requirements 2225A.9.1.5 Test for Congestion Control Measurement
2225A.9.1.5.1 Test Purpose and Environment 2225A.9.1.5.2 Test
Requirements 2231A.9.1.6 Test for Interruption 2231A.9.1.6.1 Test for
Interruption to WAN due to V2X Sidelink Communication 2231A.9.1.6.1.1
Test Purpose and Environment 2231A.9.1.6.1.2 Test Requirements 2234A.10
EN-DC Tests with NR PSCell under CCA and Other NR Cells in FR1
2234A.10.1 RRC\_CONNECTED state mobility 2234A.10.1.1 RRC connection
mobility control 2234A.10.1.1.1 Random Access 2234A.10.1.1.1.1 4-step RA
type contention-based random access for NR PSCell with CCA
2234A.10.1.1.1.1.1 Test Purpose and Environment 2234A.10.1.1.1.1.2 Test
Requirements 2237A.10.1.1.1.1.2.1 Random Access Preamble Transmission
2237A.10.1.1.1.1.2.2 Random Access Response Reception
2237A.10.1.1.1.1.2.3 No Random Access Response Reception
2238A.10.1.1.1.1.2.4 Receiving an UL grant for msg3 retransmission
2238A.10.1.1.1.1.2.5 Contention Resolution Timer expiry 2238A.10.1.1.1.2
4-step RA type non-contention based random access for NR PSCell with CCA
2239A.10.1.1.1.2.1 Test Purpose and Environment 2239A.10.1.1.1.2.2 Test
Requirements 2242A.10.1.1.1.2.2.1 SSB-based Random Access Preamble
Transmission 2242A.10.1.1.1.2.2.2 Random Access Response Reception
2243A.10.1.1.1.2.2.3 No Random Access Response Reception
2243A.10.1.1.1.3 2-step RA type contention-based random access for NR
PSCell with CCA 2243A.10.1.1.1.3.1 Test Purpose and Environment
2243A.10.1.1.1.3.2 Test Requirements 2247A.10.1.1.1.3.2.1 MsgA
Transmission 2247A.10.1.1.1.3.2.2 MsgB Reception 2247A.10.1.1.1.3.2.3 No
MsgB Reception 2248A.10.1.1.1.4 2-step RA type non-contention based
random access for NR PSCell with CCA 2248A.10.1.1.1.4.1 Test Purpose and
Environment 2248A.10.1.1.1.4.2 Test Requirements 2252A.10.1.1.1.4.2.1
MsgA Transmission 2252A.10.1.1.1.4.2.2 MsgB Reception
2253A.10.1.1.1.4.2.3 No MsgB Reception 2253A.10.2 Timing 2254A.10.2.1 UE
transmit timing 2254A.10.2.2 UE timing advance 2258A.10.3 Signalling
characteristics 2261A.10.3.1 Radio link monitoring 2261A.10.3.1.1
Introduction 2261A.10.3.1.2 Radio link monitoring out-of-sync test for
PSCell configured with SSB-based RLM RS in non-DRX mode 2262A.10.3.1.2.1
Test purpose and environment 2262A.10.3.1.2.2 Test requirements
2267A.10.3.1.3 Radio link monitoring in-sync test for PSCell configured
with SSB-based RLM RS in non-DRX mode 2267A.10.3.1.3.1 Test purpose and
environment 2267A.10.3.1.3.2 Test requirements 2273A.10.3.1.4 Void
2273A.10.3.1.4.1 Void 2273A.10.3.1.4.2 Void 2273A.10.3.1.5 Void
2273A.10.3.1.5.1 Void 2273A.10.3.1.5.2 Void 2273A.10.3.2 Interruption
2273A.10.3.2.1 E-UTRAN -- NR interruptions during SCell operations with
CCA 2273A.10.3.2.1.1 Test Purpose and Environment 2273A.10.3.2.1.2 Test
Requirements 2278A.10.3.3 SCell activation and deactivation delay
2278A.10.3.3.2 SCell Activation and Deactivation of known NR SCell with
NR PSCell and NR SCell under CCA, 640 ms SCell measurement cycle
2283A.10.3.3.2.1 Test Purpose and Environment 2283A.10.3.3.2.2 Test
Requirements 2284A.10.3.3.3 SCell Activation and Deactivation of unknown
NR SCell with NR PSCell and NR SCell under CCA 2284A.10.3.3.3.1 Test
Purpose and Environment 2284A.10.3.3.3.2 Test Requirements 2285A.10.3.4
Beam failure detection and link recovery procedures 2285A.10.3.4.1 EN-DC
Beam Failure Detection and Link Recovery Test for FR1 PSCell configured
with SSB-based BFD and LR in non-DRX mode 2285A.10.3.4.1.1 Test Purpose
and Environment 2285A.10.3.4.1.2 Test Requirements 2290A.10.3.4.2 EN-DC
Beam Failure Detection and Link Recovery Test for FR1 PSCell configured
with SSB-based BFD and LR in DRX mode 2290A.10.3.4.2.1 Test Purpose and
Environment 2290A.10.3.4.2.2 Test Requirements 2296A.10.3.5 Active BWP
switching 2296A.10.3.5.1 UL active BWP switch delay with consistent UL
LBT failure on PSCell subject to UL CCA in EN-DC 2296A.10.3.5.1.1 Test
Purpose and Environment 2296A.10.3.5.1.2 Test Requirements
2301A.10.3.5.2 DCI-based and Timer-based Active BWP Switch
2302A.10.3.5.2.1 E-UTRAN -- NR PSCell FR1 DL active BWP switch in
non-DRX in synchronous EN-DC 2302A.10.3.5.2.2 E-UTRAN -- NR PSCell FR1
DL active BWP switch with FR1 SCell in non-DRX in synchronous EN-DC
2305A.10.3.5.3 RRC-based Active BWP Switch 2309A.10.3.6 PSCell addition
and release delay 2313A.10.3.6.1 Addition and Release Delay of known NR
PSCell on the carrier under CCA 2313A.10.3.6.1.1 Test purpose and
environment 2313A.10.3.6.1.2 Test Requirements 2318A.10.3.7 Void
2319A.10.4 Measurement procedure 2319A.10.4.1 Intra-frequency
measurements 2319A.10.4.1.1 Event-triggered reporting tests on PSCC
without gaps under non-DRX 2319A.10.4.1.1.1 Test purpose and environment
2319A.10.4.1.1.2 Test parameters 2319A.10.4.1.1.3 Test Requirements
2319A.10.4.1.2 Event-triggered reporting tests on PSCC without gaps
under DRX 2320A.10.4.1.2.1 Test purpose and environment 2320A.10.4.1.2.2
Test parameters 2320A.10.4.1.2.3 Test Requirements 2320A.10.4.1.3
Event-triggered reporting tests on PSCC with per-UE gaps under non-DRX
2320A.10.4.1.3.1 Test purpose and environment 2320A.10.4.1.3.2 Test
parameters 2320A.10.4.1.3.3 Test Requirements 2320A.10.4.1.4
Event-triggered reporting tests on PSCC with per-UE gaps under DRX
2321A.10.4.1.4.1 Test purpose and environment 2321A.10.4.1.4.2 Test
parameters 2321A.10.4.1.4.3 Test Requirements 2321A.10.4.1.5
Event-triggered reporting tests on SCC without gaps under non-DRX
2321A.10.4.1.5.1 Test purpose and environment 2321A.10.4.1.5.2 Test
parameters 2321A.10.4.1.5.3 Test Requirements 2321A.10.4.1.6
Event-triggered reporting tests on SCC without gaps under DRX
2322A.10.4.1.6.1 Test purpose and environment 2322A.10.4.1.6.2 Test
parameters 2322A.10.4.1.6.3 Test Requirements 2322A.10.4.1.7
Event-triggered reporting tests on SCC with per-UE gaps under non-DRX
2322A.10.4.1.7.1 Test purpose and environment 2322A.10.4.1.7.2 Test
parameters 2322A.10.4.1.7.3 Test Requirements 2322A.10.4.1.8
Event-triggered reporting tests on SCC with per-UE gaps under DRX
2323A.10.4.1.8.1 Test purpose and environment 2323A.10.4.1.8.2 Test
parameters 2323A.10.4.1.8.3 Test Requirements 2323A.10.4.1.9 RSSI
measurement reporting on PSCC 2323A.10.4.1.9.1 Test purpose and
environment 2323A.10.4.1.9.2 Test parameters 2323A.10.4.1.10 Channel
occupancy measurement reporting on PSCC 2324A.10.4.1.10.1 Test purpose
and environment 2324A.10.4.1.10.2 Test parameters 2324A.10.4.1.11 RSSI
measurement reporting on SCC 2324A.10.4.1.11.1 Test purpose and
environment 2324A.10.4.1.11.2 Test parameters 2324A.10.4.1.12 Channel
occupancy measurement reporting on SCC 2325A.10.4.1.12.1 Test purpose
and environment 2325A.10.4.1.12.2 Test parameters 2325A.10.4.2
Inter-frequency measurements 2325A.10.4.2.1 RSSI measurement reporting
2325A.10.4.2.1.1 Test purpose and environment 2325A.10.4.2.1.2 Test
parameters 2325A.10.4.2.2 Channel occupancy measurement reporting
2326A.10.4.2.2.1 Test purpose and environment 2326A.10.4.2.2.2 Test
parameters 2326A.10.4.2.3 EN-DC event triggered reporting tests for FR1
with CCA cell without SSB time index detection when DRX is not used
2326A.10.4.2.3.1 Test Purpose and Environment 2326A.10.4.2.3.2 Test
Requirements 2331A.10.4.2.4 EN-DC event triggered reporting tests for
FR1 cell with CCA without SSB time index detection when DRX is used
2332A.10.4.2.4.1 Test Purpose and Environment 2332A.10.4.2.4.2 Test
Requirements 2336A.10.4.2.5 EN-DC event triggered reporting tests for
FR1 cell with CCA with SSB time index detection when DRX is not used
2337A.10.4.2.5.1 Test Purpose and Environment 2337A.10.4.2.5.2 Test
Requirements 2341A.10.4.2.6 EN-DC event triggered reporting tests for
FR1 cell with CCA with SSB time index detection when DRX is used
2342A.10.4.2.6.1 Test Purpose and Environment 2342A.10.4.2.6.2 Test
Requirements 2346A.10.4.2.7 EN-DC event triggered reporting tests for
FR1 cell without SSB time index detection when DRX is not used
2347A.10.4.2.7.1 Test Purpose and Environment 2347A.10.4.2.7.2 Test
Requirements 2353A.10.4.2.8 EN-DC event triggered reporting tests for
FR1 cell without SSB time index detection when DRX is used
2353A.10.4.2.8.1 Test Purpose and Environment 2353A.10.4.2.8.2 Test
Requirements 2359A.10.4.2.9 EN-DC event triggered reporting tests for
FR1 cell with SSB time index detection when DRX is not used
2360A.10.4.2.9.1 Test Purpose and Environment 2360A.10.4.2.9.2 Test
Requirements 2365A.10.4.2.10 EN-DC event triggered reporting tests for
FR1 cell with SSB time index detection when DRX is used
2365A.10.4.2.10.1 Test Purpose and Environment 2365A.10.4.2.10.2 Test
Requirements 2371A.10.4.3 L1-RSRP measurements for beam reporting
2372A.10.4.3.1 SSB based L1-RSRP measurement on PSCC when DRX is not
used 2372A.10.4.3.1.1 Test Purpose and Environment 2372A.10.4.3.1.2 Test
parameters 2372A.10.4.3.1.3 Test Requirements 2374A.10.4.3.2 SSB based
L1-RSRP measurement on PSCC when DRX is used 2375A.10.4.3.2.1 Test
Purpose and Environment 2375A.10.4.3.2.2 Test parameters
2375A.10.4.3.2.3 Test Requirements 2377A.10.4.3.3 SSB based L1-RSRP
measurement on SCC when DRX is not used 2378A.10.4.3.3.1 Test Purpose
and Environment 2378A.10.4.3.3.2 Test parameters 2378A.10.4.3.3.3 Test
Requirements 2381A.10.4.3.4 SSB based L1-RSRP measurement on SCC when
DRX is used 2382A.10.4.3.4.1 Test Purpose and Environment
2382A.10.4.3.4.2 Test parameters 2382A.10.4.3.4.3 Test Requirements
2385A.10.4.4 E-UTRAN−NR inter-RAT measurements on NR carrier frequency
under CCA 2386A.10.4.4.1 E-UTRA-NR inter-RAT event triggered reporting
tests for FR1 without SSB time index detection when DRX is not used
2386A.10.4.4.1.1 Test Purpose and Environment 2386A.10.4.4.1.2 Test
Requirements 2390A.10.4.4.2 E-UTRA-NR inter-RAT event triggered
reporting tests for FR1 without SSB time index detection when DRX is
used 2391A.10.4.4.2.1 Test Purpose and Environment 2391A.10.4.4.2.2 Test
Requirements 2396A.10.4.4.3 NR Inter-RAT event triggered reporting tests
for FR1 with SSB time index detection when DRX is not used
2397A.10.4.4.3.1 Test Purpose and Environment 2397A.10.4.4.3.2 Test
Requirements 2401A.10.4.4.4 NR Inter-RAT event triggered reporting tests
for FR1 with SSB time index detection when DRX is used 2402A.10.4.4.4.1
Test Purpose and Environment 2402A.10.4.4.4.2 Test Requirements
2407A.10.5 Measurement performance 2408A.10.5.1 SS-RSRP 2408A.10.5.1.1
Intra-frequency measurement accuracy on a CCA serving cell
2408A.10.5.1.1.1 Test Purpose and Environment 2408A.10.5.1.1.2 Test
parameters 2408A.10.5.1.1.3 Test Requirements 2411A.10.5.1.2
Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1
CCA target cell 2411A.10.5.1.2.1 Test Purpose and Environment
2411A.10.5.1.2.2 Test parameters 2411A.10.5.1.2.3 Test Requirements
2415A.10.5.2 SS-RSRQ 2415**A.10.5.2.1** **Intra-frequency measurement
accuracy with FR1 CCA serving cell and FR1 CCA target cell**
2415A.10.5.2.1.1 Test Purpose and Environment 2415A.10.5.2.1.2 Test
Parameters 2415A.10.5.2.1.3 Test Requirements 2418**A.10.5.2.2**
**Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1
CCA target cell** 2418A.10.5.2.2.1 Test Purpose and Environment
2418A.10.5.2.2.2 Test Parameters 2418A.10.5.2.2.3 Test Requirements
2421A.10.5.3 SS-SINR 2421A.10.5.3.1 Intra-frequency measurement accuracy
on PSCC 2421A.10.5.3.1.1 Test Purpose and Environment 2421A.10.5.3.1.2
Test Parameters 2421A.10.5.3.1.3 Test Requirements 2424A.10.5.3.2
Inter-frequency measurement accuracy on PSCC 2424A.10.5.3.2.1 Test
Purpose and Environment 2424A.10.5.3.2.2 Test Parameters
2424A.10.5.3.2.3 Test Requirements 2428A.10.5.3.3 Intra-frequency
measurement accuracy on SCC 2428A.10.5.3.3.1 Test Purpose and
Environment 2428A.10.5.3.3.2 Test Parameters 2428A.10.5.3.3.3 Test
Requirements 2431A.10.5.4 L1-RSRP measurement for beam reporting with
CCA serving cell 2431A.10.5.4.1 SSB based L1-RSRP measurement
2431A.10.5.4.1.1 Test Purpose and Environment 2431A.10.5.4.1.2 Test
parameters 2432A.10.5.4.1.3 Test Requirements 2434A.10.5.5 RSSI
2434A.10.5.5.1 RSSI measurement accuracy on PSCC with CCA
2434A.10.5.5.1.1 Test Purpose and Environment 2434A.10.5.5.1.2 Test
parameters 2434A.10.5.5.1.3 Test Requirements 2437A.10.5.5.2 RSSI
measurement accuracy on SCC with CCA 2437A.10.5.5.2.1 Test Purpose and
Environment 2437A.10.5.5.2.2 Test parameters 2437A.10.5.5.2.3 Test
Requirements 2440A.10.5.5.3 Inter-frequency RSSI measurement accuracy on
a carrier with CCA 2440A.10.5.5.3.1 Test Purpose and Environment
2440A.10.5.5.3.2 Test parameters 2440A.10.5.5.3.3 Test Requirements
2444A.10.5.6 Channel occupancy 2444A.10.5.6.1 Channel occupancy
measurement accuracy on PSCC with CCA 2444A.10.5.6.1.1 Test Purpose and
Environment 2444A.10.5.6.1.2 Test parameters 2444A.10.5.6.1.3 Test
Requirements 2448A.10.5.6.2 Channel occupancy measurement accuracy on
SCC with CCA 2448A.10.5.6.2.1 Test Purpose and Environment
2448A.10.5.6.2.2 Test parameters 2448A.10.5.6.2.3 Test Requirements
2451A.10.5.6.3 Inter-frequency channel occupancy measurement accuracy on
a carrier with CCA 2451A.10.5.6.3.1 Test Purpose and Environment
2451A.10.5.6.3.2 Test parameters 2451A.10.5.6.3.3 Test Requirements
2455A.11 NR Standalone Tests with NR PCell under CCA and Other NR Cells
in FR1 2455A.11.1 RRC\_IDLE state mobility 2455A.11.1.1 Cell
re-selection with both source and target NR carrier frequencies under
CCA 2455A.11.1.1.1 Cell reselection to FR1 intra-frequency NR cells when
subject to CCA on the serving and target cell 2455A.11.1.1.1.1 Test
Purpose and Environment 2455A.11.1.1.1.2 Test Parameters
2456A.11.1.1.1.3 Test Requirements 2459A.11.1.1.2 Cell reselection to
FR1 inter-frequency NR case when subject to CCA on the serving and
target cell 2459A.11.1.1.2.1 Test Purpose and Environment
2459A.11.1.1.2.2 Test Parameters 2459A.11.1.1.2.3 Test Requirements
2463A.11.1.2 Cell re-selection to NR with source NR carrier frequency
under CCA 2463A.11.1.2.1 Cell reselection to FR1 inter-frequency NR case
when serving cell is subject to CCA 2463A.11.1.2.1.1 Test Purpose and
Environment 2463A.11.1.2.1.2 Test Parameters 2464A.11.1.2.1.3 Test
Requirements 2470A.11.1.3 Cell re-selection from NR carrier with target
NR carrier frequency under CCA 2471A.11.1.3.1 Cell reselection to FR1
inter-frequency NR case when target cell is subject to CCA
2471A.11.1.3.1.1 Test Purpose and Environment 2471A.11.1.3.1.2 Test
Parameters 2471A.11.1.3.1.3 Test Requirements 2476A.11.1.4 Inter-RAT
cell re-selection to E-UTRAN with source NR carrier frequency under CCA
2477A.11.1.4.1 Cell reselection to higher priority E-UTRAN when serving
cell is subject to CCA 2477A.11.1.4.1.1 Test Purpose and Environment
2477A.11.1.4.1.2 Test Parameters 2477A.11.1.4.1.3 Test Requirements
2480A.11.1.4.2 Cell reselection to lower priority E-UTRAN when serving
cell is subject to CCA 2481A.11.1.4.2.1 Test Purpose and Environment
2481A.11.1.4.2.2 Test Requirements 2483A.11.2 RRC\_CONNECTED state
mobility 2484A.11.2.1 Handover 2484A.11.2.1.1 Intra-frequency handover
from FR1 carrier under CCA to FR1 carrier under CCA; known target cell
2484A.11.2.1.1.1 Test Purpose and Environment 2484A.11.2.1.1.2 Test
Parameters 2484A.11.2.1.1.3 Test Requirements 2487A.11.2.1.2
Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under
CCA; unknown target cell 2487A.11.2.1.2.1 Test Purpose and Environment
2487A.11.2.1.2.2 Test Parameters 2487A.11.2.1.2.3 Test Requirements
2490A.11.2.1.3 Inter-frequency handover from FR1 carrier under CCA to
FR1 carrier under CCA; unknown target cell 2490A.11.2.1.3.1 Test Purpose
and Environment 2490A.11.2.1.3.2 Test Parameters 2490A.11.2.1.3.3 Test
Requirements 2493A.11.2.1.4 Inter-frequency handover from FR1 carrier
under CCA to FR1; known target cell 2493A.11.2.1.4.1 Test Purpose and
Environment 2493A.11.2.1.4.2 Test Parameters 2493A.11.2.1.4.3 Test
Requirements 2497A.11.2.1.5 Inter-frequency handover from FR1 carrier
under CCA to FR1; unknown target cell 2498A.11.2.1.5.1 Test Purpose and
Environment 2498A.11.2.1.5.2 Test Parameters 2498A.11.2.1.5.3 Test
Requirements 2501A.11.2.1.6 Inter-frequency handover from FR1 to FR1
carrier under CCA; unknown target cell 2502A.11.2.1.6.1 Test Purpose and
Environment 2502A.11.2.1.6.2 Test Parameters 2502A.11.2.1.6.3 Test
Requirements 2505A.11.2.1.7 SA NR FR1 carrier under CCA - E-UTRAN
handover with known target cell 2506A.11.2.1.7.1 Test Purpose and
Environment 2506A.11.2.1.7.2 Test Requirements 2512A.11.2.1.8 SA NR FR1
carrier under CCA - E-UTRAN handover with unknown target cell
2512A.11.2.1.8.1 Test Purpose and Environment 2512A.11.2.1.8.2 Test
Requirements 2517A.11.2.2 RRC connection mobility control 2517A.11.2.2.1
RRC re-establishment 2517A.11.2.2.1.1 Intra-frequency RRC
Re-establishment with CCA in FR1 2517A.11.2.2.1.2 Inter-frequency RRC
Re-establishment with CCA in FR1 2520A.11.2.2.1.3 Intra-frequency RRC
Re-establishment with CCA in FR1 without serving cell timing
2524A.11.2.2.1.4 Inter-frequency RRC Re-establishment from NR FR1
carrier without CCA to NR FR1 carrier under CCA 2527A.11.2.2.2 Random
Access 2532A.11.2.2.2.1 4-step RA type contention-based random access
for NR PCell with CCA 2532A.11.2.2.2.1.1 Test Purpose and Environment
2532A.11.2.2.2.1.2 Test Requirements 2535A.11.2.2.2.1.2.1 Random Access
Preamble Transmission 2535A.11.2.2.2.1.2.2 Random Access Response
Reception 2535A.11.2.2.2.1.2.3 No Random Access Response Reception
2536A.11.2.2.2.1.2.4 Receiving an UL grant for msg3 retransmission
2536A.11.2.2.2.1.2.5 Reception of an Incorrect Message over Temporary
C-RNTI 2536A.11.2.2.2.1.2.6 Reception of a Correct Message over
Temporary C-RNTI 2537A.11.2.2.2.1.2.7 Contention Resolution Timer expiry
2537A.11.2.2.2.2 4-step RA type non-contention based random access for
NR PSCell with CCA 2537A.11.2.2.2.2.1 Test Purpose and Environment
2537A.11.2.2.2.2.2 Test Requirements 2540A.11.2.2.2.2.2.1 SSB-based
Random Access Preamble Transmission 2540A.11.2.2.2.2.2.2 Random Access
Response Reception 2541A.11.2.2.2.2.2.3 No Random Access Response
Reception 2541A.11.2.2.2.3 2-step RA type contention-based random access
for NR PCell with CCA 2541A.11.2.2.2.3.1 Test Purpose and Environment
2541A.11.2.2.2.3.2 Test Requirements 2545A.11.2.2.2.3.2.1 MsgA
Transmission 2545A.11.2.2.2.3.2.2 MsgB Reception 2545A.11.2.2.2.3.2.3 No
MsgB Reception 2546A.11.2.2.2.4 2-step RA type non-contention-based
random access for NR PCell with CCA 2546A.11.2.2.2.4.1 Test Purpose and
Environment 2546A.11.2.2.2.4.2 Test Requirements 2550A.11.2.2.2.4.2.1
MsgA Transmission 2550A.11.2.2.2.4.2.2 MsgB Reception
2551A.11.2.2.2.4.2.3 No MsgB Reception 2551A.11.2.2.3 RRC connection
release with redirection 2552A.11.2.2.3.1 Redirection from NR FR1
carrier under CCA to NR FR1 carrier under CCA 2552A.11.3 Timing
2560A.11.3.1 UE transmit timing 2560A.11.3.2 UE timing advance
2564A.11.3.2.1 UE Timing Advance Adjustment Accuracy with PCell under DL
CCA 2564A.11.3.2.1.1 Test Purpose and Environment 2564A.11.3.2.1.2 Test
Parameters 2564A.11.3.2.1.3 Test Requirements 2568A.11.4 Signalling
characteristics 2568A.11.4.1 Radio link monitoring 2568A.11.4.1.1
Introduction 2568A.11.4.1.2 Radio link monitoring out-of-sync test for
PCell configured with SSB-based RLM RS in non-DRX mode 2569A.11.4.1.2.1
Test purpose and environment 2569A.11.4.1.2.2 Test requirements
2573A.11.4.1.3 Radio link monitoring in-sync test for PCell configured
with SSB-based RLM RS in non-DRX mode 2573A.11.4.1.3.1 Test purpose and
environment 2573A.11.4.1.3.2 Test requirements 2579A.11.4.1.4 Void
2579A.11.4.1.4.1 Void 2579A.11.4.1.4.2 Void 2579A.11.4.1.5 Void
2579A.11.4.1.5.1 Void 2579A.11.4.1.5.2 Void 2579A.11.4.2 Interruption
2579A.11.4.2.1 NR interruptions during Scell operations with CCA on
PCell and SCell 2579A.11.4.2.1.1 Test Purpose and Environment
2579A.11.4.2.1.2 Test Requirements 2583A.11.4.3 SCell activation and
deactivation delay 2583A.11.4.3.2 SCell Activation and Deactivation of
known SCell with PCell and SCell under CCA, 640 ms SCell measurement
cycle 2588A.11.4.3.2.1 Test Purpose and Environment 2588A.11.4.3.2.2
Test Requirements 2589A.11.4.4 Beam failure detection and link recovery
procedures 2590A.11.4.4.1 Beam Failure Detection and Link Recovery Test
for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode
2590A.11.4.4.1.1 Test Purpose and Environment 2590A.11.4.4.1.2 Test
Requirements 2596A.11.4.4.2 Beam Failure Detection and Link Recovery
Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode
2596A.11.4.4.2.1 Test Purpose and Environment 2596A.11.4.4.2.2 Test
Requirements 2602A.11.4.5 Active BWP switching 2602A.11.4.5.1 UL active
BWP switch delay with consistent UL LBT failure on PCell subject to UL
CCA 2602A.11.4.5.1.1 Test Purpose and Environment 2602A.11.4.5.1.2 Test
Requirements 2606A.11.4.6 Void 2616A.11.5 Measurement procedure
2616A.11.5.1 Intra-frequency measurements 2616A.11.5.1.1 Event-triggered
reporting tests on PCC without gaps under non-DRX 2616A.11.5.1.1.1 Test
purpose and environment 2616A.11.5.1.1.2 Test parameters
2616A.11.5.1.1.3 Test Requirements 2620A.11.5.1.2 Event-triggered
reporting tests on PCC without gaps under DRX 2620A.11.5.1.2.1 Test
purpose and environment 2620A.11.5.1.2.2 Test parameters
2620A.11.5.1.2.3 Test Requirements 2624A.11.5.1.3 Event-triggered
reporting tests on PCC with per-UE gaps under non-DRX 2624A.11.5.1.3.1
Test purpose and environment 2624A.11.5.1.3.2 Test parameters
2624A.11.5.1.3.3 Test Requirements 2624A.11.5.1.4 Event-triggered
reporting tests on PCC with per-UE gaps under DRX 2624A.11.5.1.4.1 Test
purpose and environment 2624A.11.5.1.4.2 Test parameters
2625A.11.5.1.4.3 Test Requirements 2625A.11.5.1.5 Event-triggered
reporting tests on SCC without gaps under non-DRX 2625A.11.5.1.5.1 Test
purpose and environment 2625A.11.5.1.5.2 Test parameters 2625A.11.5.1.6
Event-triggered reporting tests on SCC without gaps under DRX
2625A.11.5.1.6.1 Test purpose and environment 2625A.11.5.1.6.2 Test
parameters 2625A.11.5.1.6.3 Test Requirements 2625A.11.5.1.7
Event-triggered reporting tests on SCC with per-UE gaps under non-DRX
2626A.11.5.1.7.1 Test purpose and environment 2626A.11.5.1.7.2 Test
parameters 2626A.11.5.1.7.3 Test Requirements 2626A.11.5.1.8
Event-triggered reporting tests on SCC with per-UE gaps under DRX
2626A.11.5.1.8.1 Test purpose and environment 2626A.11.5.1.8.2 Test
parameters 2626A.11.5.1.8.3 Test Requirements 2626A.11.5.1.9 RSSI
measurement reporting on PCC 2627A.11.5.1.9.1 Test purpose and
environment 2627A.11.5.1.9.2 Test parameters 2627A.11.5.1.10 Channel
occupancy measurement reporting on PCC 2627A.11.5.1.10.1 Test purpose
and environment 2627A.11.5.1.10.2 Test parameters 2627A.11.5.1.11 RSSI
measurement reporting on SCC 2628A.11.5.1.11.1 Test purpose and
environment 2628A.11.5.1.11.2 Test parameters 2628A.11.5.1.12 Channel
occupancy measurement reporting on SCC 2628A.11.5.1.12.1 Test purpose
and environment 2628A.11.5.1.12.2 Test parameters 2628A.11.5.2
Inter-frequency measurements 2629A.11.5.2.1 RSSI measurement reporting
2629A.11.5.2.1.1 Test purpose and environment 2629A.11.5.2.1.2 Test
parameters 2629A.11.5.2.2 Channel occupancy measurement reporting
2629A.11.5.2.2.1 Test purpose and environment 2629A.11.5.2.2.2 Test
parameters 2629A.11.5.2.3 Event triggered reporting tests for FR1 with
CCA without SSB time index detection when DRX is not used
2630A.11.5.2.3.1 Test Purpose and Environment 2630A.11.5.2.3.2 Test
Requirements 2634A.11.5.2.4 Event triggered reporting tests for FR1 with
CCA without SSB time index detection when DRX is used 2635A.11.5.2.4.1
Test Purpose and Environment 2635A.11.5.2.4.2 Test Requirements
2640A.11.5.2.5 Event triggered reporting tests for FR1 with CCA with SSB
time index detection when DRX is not used 2640A.11.5.2.5.1 Test Purpose
and Environment 2640A.11.5.2.5.2 Test Requirements 2644A.11.5.2.6 Event
triggered reporting tests for FR1 with CCA with SSB time index detection
when DRX is used 2645A.11.5.2.6.1 Test Purpose and Environment
2645A.11.5.2.6.2 Test Requirements 2650A.11.5.2.7 Event triggered
reporting tests for FR1 without SSB time index detection when DRX is not
used 2650A.11.5.2.7.1 Test Purpose and Environment 2650A.11.5.2.7.2 Test
Requirements 2654A.11.5.2.8 Event triggered reporting tests for FR1
without SSB time index detection when DRX is used 2655A.11.5.2.8.1 Test
Purpose and Environment 2655A.11.5.2.8.2 Test Requirements
2660A.11.5.2.9 Event triggered reporting tests for FR1 with SSB time
index detection when DRX is not used 2660A.11.5.2.9.1 Test Purpose and
Environment 2660A.11.5.2.9.2 Test Requirements 2665A.11.5.2.10 Event
triggered reporting tests for FR1 with SSB time index detection when DRX
is used 2666A.11.5.2.10.1 Test Purpose and Environment 2666A.11.5.2.10.2
Test Requirements 2671A.11.5.3 Inter-RAT E-UTRAN measurements
2672A.11.5.3.1 SA NR - E-UTRAN event-triggered reporting in non-DRX in
FR1 2672A.11.5.3.1.1 Test Purpose and Environment 2672A.11.5.3.1.2 Test
Requirements 2676A.11.5.3.2 SA NR - E-UTRAN event-triggered reporting in
DRX in FR1 2676A.11.5.3.2.1 Test Purpose and Environment
2676A.11.5.3.2.2 Test Requirements 2681A.11.5.4 L1-RSRP measurements for
beam reporting 2681A.11.5.4.1 SSB based L1-RSRP measurement when DRX is
not used 2681A.11.5.4.1.1 Test Purpose and Environment 2681A.11.5.4.1.2
Test parameters 2681A.11.5.4.1.3 Test Requirements 2683A.11.5.4.2 SSB
based L1-RSRP measurement when DRX is used 2683A.11.5.4.2.1 Test Purpose
and Environment 2683A.11.5.4.2.2 Test parameters 2684A.11.5.4.2.3 Test
Requirements 2686A.11.5.4.3 SSB based L1-RSRP measurement on SCC when
DRX is not used 2686A.11.5.4.3.1 Test Purpose and Environment
2686A.11.5.4.3.2 Test parameters 2687A.11.5.4.3.3 Test Requirements
2690A.11.5.4.4 SSB based L1-RSRP measurement on SCC when DRX is used
2691A.11.5.4.4.1 Test Purpose and Environment 2691A.11.5.4.4.2 Test
parameters 2691A.11.5.4.4.3 Test Requirements 2694A.11.6 Measurement
performance 2695A.11.6.1 SS-RSRP 2695A.11.6.1.1 Intra-frequency
measurement accuracy on a carrier frequency with CCA 2695A.11.6.1.1.1
Test Purpose and Environment 2695A.11.6.1.1.2 Test parameters
2695A.11.6.1.1.3 Test Requirements 2697A.11.6.1.2 Intra-frequency
measurement accuracy on SCC on a carrier frequency with CCA
2697A.11.6.1.2.1 Test Purpose and Environment 2697A.11.6.1.2.2 Test
parameters 2697A.11.6.1.2.3 Test Requirements 2699A.11.6.2 SS-RSRQ
2699A.11.6.2.1 Intra-frequency measurement accuracy 2699A.11.6.2.1.1
Test Purpose and Environment 2699A.11.6.2.1.2 Test Parameters
2699A.11.6.2.1.3 Test Requirements 2702A.11.6.2.2 Inter-frequency
measurement accuracy 2702A.11.6.2.2.1 Test Purpose and Environment
2702A.11.6.2.2.2 Test Parameters 2702A.11.6.2.2.3 Test Requirements
2705A.11.6.2.3 Intra-frequency measurement accuracy on SCC
2705A.11.6.2.3.1 Test Purpose and Environment 2705A.11.6.2.3.2 Test
Parameters 2705A.11.6.2.3.3 Test Requirements 2708A.11.6.2.4
Inter-frequency measurement accuracy 2708A.11.6.2.4.1 Test Purpose and
Environment 2708A.11.6.2.4.2 Test Parameters 2708A.11.6.2.4.3 Test
Requirements 2717A.11.6.3 SS-SINR 2717A.11.6.3.1 Intra-frequency
measurement accuracy 2717A.11.6.3.1.1 Test Purpose and Environment
2717A.11.6.3.1.2 Test Parameters 2717A.11.6.3.1.3 Test Requirements
2720A.11.6.3.2 Inter-frequency measurement accuracy 2720A.11.6.3.2.1
Test Purpose and Environment 2720A.11.6.3.2.2 Test Parameters
2720A.11.6.3.2.3 Test Requirements 2723A.11.6.3.3 Intra-frequency
measurement accuracy on SCC 2723A.11.6.3.3.1 Test Purpose and
Environment 2723A.11.6.3.3.2 Test Parameters 2723A.11.6.3.3.3 Test
Requirements 2726A.11.6.3.4 Inter-frequency measurement accuracy
2726A.11.6.3.4.1 Test Purpose and Environment 2726A.11.6.3.4.2 Test
Parameters 2726A.11.6.3.4.3 Test Requirements 2734A.11.6.4 L1-RSRP
measurement for beam reporting with CCA serving cell 2734A.11.6.4.1 SSB
based L1-RSRP measurement 2734A.11.6.4.1.1 Test Purpose and Environment
2734A.11.6.4.1.2 Test parameters 2735A.11.6.4.1.3 Test Requirements
2738A.11.6.5 RSSI 2738A.11.6.5.1 Intra-frequency RSSI measurement
accuracy on PCC with CCA 2738A.11.6.5.1.1 Test Purpose and Environment
2738A.11.6.5.1.2 Test parameters 2738A.11.6.5.1.3 Test Requirements
2741A.11.6.5.2 Intra-frequency RSSI measurement accuracy on SCC with CCA
2741A.11.6.5.2.1 Test Purpose and Environment 2741A.11.6.5.2.2 Test
parameters 2741A.11.6.5.2.3 Test Requirements 2744A.11.6.5.3
Inter-frequency RSSI measurement accuracy on a carrier with CCA
2744A.11.6.5.3.1 Test Purpose and Environment 2744A.11.6.5.3.2 Test
parameters 2744A.11.6.5.3.3 Test Requirements 2747A.11.6.6 Channel
occupancy 2747A.11.6.6.1 Intra-frequency channel occupancy measurement
accuracy on PCC with CCA 2747A.11.6.6.1.1 Test Purpose and Environment
2747A.11.6.6.1.2 Test parameters 2747A.11.6.6.1.3 Test Requirements
2751A.11.6.6.2 Intra-frequency channel occupancy measurement accuracy on
SCC with CCA 2751A.11.6.6.2.1 Test Purpose and Environment
2751A.11.6.6.2.2 Test parameters 2751A.11.6.6.2.3 Test Requirements
2754A.11.6.6.3 Inter-frequency channel occupancy measurement accuracy on
a carrier with CCA 2754A.11.6.6.3.1 Test Purpose and Environment
2754A.11.6.6.3.2 Test parameters 2754A.11.6.6.3.3 Test Requirements
2757A.11.6.7 E-UTRAN RSRP 2757A.11.6.8 E-UTRAN RSRQ 2757A.11.6.9 E-UTRAN
SINR 2757A.12 E-UTRA Standalone Tests with at Least One NR Cell under
CCA 2757A.12.1 RRC\_IDLE state mobility 2757A.12.1.1 Inter-RAT cell
re-selection to NR on a carrier frequency with CCA 2757A.12.1.1.1 E-UTRA
Cell reselection to higher priority NR target Cell in FR1 when target
cell is subject to CCA 2757A.12.1.1.1.1 Test Purpose and Environment
2757A.12.1.1.1.2 Test Requirements 2763A.12.2 RRC\_CONNECTED state
mobility 2764A.12.2.1 Handover 2764A.12.2.1.1 E-UTRAN - NR with CCA
handover 2764A.12.2.1.1.1 Test Purpose and Environment 2764A.12.2.1.1.2
Test Requirements 2769A.12.3 Signalling characteristics 2770A.12.3.1
Interruptions 2770A.12.4 Measurement procedure 2770A.12.4.1 E-UTRAN−NR
inter-RAT SFTD measurements 2770A.12.4.1.1 E-UTRA -- NR Inter-RAT SFTD
Measurement Delay with NR under CCA in non-DRX 2770A.12.4.1.1.1 Test
Purpose and Environment 2770A.12.4.1.1.2 Test Requirements 2774A.12.4.2
E-UTRAN−NR inter-RAT measurements on NR carrier frequency under CCA
2774A.12.4.2.1 E-UTRA-NR inter-RAT event triggered reporting tests for
FR1 without SSB time index detection when DRX is not used
2774A.12.4.2.1.1 Test Purpose and Environment 2774A.12.4.2.1.2 Test
Requirements 2778A.12.4.2.2 E-UTRA-NR inter-RAT event triggered
reporting tests for FR1 without SSB time index detection when DRX is
used 2779A.12.4.2.2.1 Test Purpose and Environment 2779A.12.4.2.2.2 Test
Requirements 2783A.12.4.2.3 NR Inter-RAT event triggered reporting tests
for FR1 with SSB time index detection when DRX is not used
2784A.12.4.2.3.1 Test Purpose and Environment 2784A.12.4.2.3.2 Test
Requirements 2788A.12.4.2.4 NR Inter-RAT event triggered reporting tests
for FR1 with SSB time index detection when DRX is used 2789A.12.4.2.4.1
Test Purpose and Environment 2789A.12.4.2.4.2 Test Requirements
2793A.12.4.2.5 RSSI measurement reporting 2794A.12.4.2.5.1 Test purpose
and environment 2794A.12.4.2.5.2 Test parameters 2794A.12.4.2.5.3 Test
Requirements 2797A.12.4.2.6 Channel occupancy measurement reporting
2797A.12.4.2.6.1 Test purpose and environment 2797A.12.4.2.6.2 Test
parameters 2797A.12.4.2.6.3 Test Requirements 2801A.12.5 Measurement
performance 2801A.12.5.1 E-UTRAN−NR SFTD 2801A.12.5.2 E-UTRAN−NR SS-RSRP
2807A.12.5.3 E-UTRAN−NR SS-RSRQ 2807A.12.5.4 E-UTRAN−NR SS-SINR
2807A.12.5.5 E-UTRAN−NR RSSI 2807A.12.5.6 E-UTRAN−NR channel occupancy
2807A.13 NR Standalone Tests with NR SCell under CCA and All Other NR
Cells in FR1 2807A.13.1 Timing 2807A.13.1.1 UE transmit timing
2807A.13.1.2 Timing advance 2807A.13.2 Signalling characteristics
2807A.13.2.1 Interruption 2807A.13.2.1.1 NR interruptions during SCell
operations with CCA on SCell 2807A.13.2.1.1.1 Test Purpose and
Environment 2807A.13.2.1.1.2 Test Requirements 2811A.13.2.2 SCell
activation and deactivation delay 2811A.13.2.2.2 SCell Activation and
Deactivation of known SCell under CCA, 640 ms SCell measurement cycle
2816A.13.2.2.2.1 Test Purpose and Environment 2816A.13.2.2.2.2 Test
Requirements 2817A.13.2.2.3 SCell Activation and Deactivation of unknown
SCell under CCA 2817A.13.2.2.3.1 Test Purpose and Environment
2817A.13.2.2.3.2 Test Requirements 2818A.13.2.3 Void 2818A.13.3
Measurement procedure 2818A.13.3.1 Intra-frequency measurements
2818A.13.3.1.1 Event-triggered reporting tests on SCC without gaps under
non-DRX 2818A.13.3.1.1.1 Test purpose and environment 2818A.13.3.1.1.2
Test parameters 2818A.13.3.1.1.3 Test Requirements 2823A.13.3.1.2
Event-triggered reporting tests on SCC without gaps under DRX
2823A.13.3.1.2.1 Test purpose and environment 2823A.13.3.1.2.2 Test
parameters 2823A.13.3.1.2.3 Test Requirements 2828A.13.3.1.3
Event-triggered reporting tests on SCC with per-UE gaps under non-DRX
2828A.13.3.1.3.1 Test purpose and environment 2828A.13.3.1.3.2 Test
parameters 2828A.13.3.1.3.3 Test Requirements 2833A.13.3.1.4
Event-triggered reporting tests on SCC with per-UE gaps under DRX
2833A.13.3.1.4.1 Test purpose and environment 2833A.13.3.1.4.2 Test
parameters 2833A.13.3.1.4.3 Test Requirements 2838A.13.3.1.5 RSSI
measurement reporting on SCC 2838A.13.3.1.5.1 Test purpose and
environment 2838A.13.3.1.5.2 Test parameters 2838A.13.3.1.6 Channel
occupancy measurement reporting on SCC 2840A.13.3.1.6.1 Test purpose and
environment 2840A.13.3.1.6.2 Test parameters 2841A.13.3.2
Inter-frequency measurements 2841A.13.3.2.1 RSSI measurement reporting
2841A.13.3.2.1.1 Test purpose and environment 2841A.13.3.2.1.2 Test
parameters 2841A.13.3.2.2 Channel occupancy measurement reporting
2842A.13.3.2.2.1 Test purpose and environment 2842A.13.3.2.2.2 Test
parameters 2842A.13.3.2.3 Event triggered reporting tests for FR1 with
CCA without SSB time index detection when DRX is not used
2842A.13.3.2.3.1 Test Purpose and Environment 2842A.13.3.2.3.2 Test
Requirements 2848A.13.3.2.4 Event triggered reporting tests for FR1 with
CCA without SSB time index detection when DRX is used 2848A.13.3.2.4.1
Test Purpose and Environment 2848A.13.3.2.4.2 Test Requirements
2853A.13.3.2.5 Event triggered reporting tests for FR1 with CCA with SSB
time index detection when DRX is not used 2854A.13.3.2.5.1 Test Purpose
and Environment 2854A.13.3.2.5.2 Test Requirements 2859A.13.3.2.6 Event
triggered reporting tests for FR1 with CCA with SSB time index detection
when DRX is used 2859A.13.3.2.6.1 Test Purpose and Environment
2859A.13.3.2.6.2 Test Requirements 2865A.13.3.3 L1-RSRP measurements for
beam reporting 2866A.13.3.3.1 SSB based L1-RSRP measurement when DRX is
not used 2866A.13.3.3.1.1 Test Purpose and Environment 2866A.13.3.3.1.2
Test parameters 2866A.13.3.3.1.3 Test Requirements 2871A.13.3.3.2 SSB
based L1-RSRP measurement when DRX is used 2871A.13.3.3.2.1 Test Purpose
and Environment 2871A.13.3.3.2.2 Test parameters 2871A.13.3.3.2.3 Test
Requirements 2875A.13.4 Measurement performance 2875A.13.4.1 SS-RSRP
2875A.13.4.1.1 Intra-frequency measurement accuracy on a carrier
frequency with CCA 2875A.13.4.1.1.1 Test Purpose and Environment
2875A.13.4.1.1.2 Test parameters 2875A.13.4.1.1.3 Test Requirements
2877A.13.4.2 SS-RSRQ 2877A.13.4.2.1 Intra-frequency measurement accuracy
on SCC 2877A.13.4.2.1.1 Test Purpose and Environment 2877A.13.4.2.1.2
Test Parameters 2877A.13.4.2.1.3 Test Requirements 2885A.13.4.3 SS-SINR
2885A.13.4.3.1 Intra-frequency measurement accuracy on SCC
2885A.13.4.3.1.1 Test Purpose and Environment 2885A.13.4.3.1.2 Test
Parameters 2885A.13.4.3.1.3 Test Requirements 2891A.13.4.4 L1-RSRP
measurement for beam reporting with CCA serving cell 2892A.13.4.4.1 SSB
based L1-RSRP measurement 2892A.13.4.4.1.1 Test Purpose and Environment
2892A.13.4.4.1.2 Test parameters 2892A.13.4.4.1.3 Test Requirements
2896A.13.4.5 RSSI 2896A.13.4.5.1 Intra-frequency RSSI measurement
accuracy on a carrier with CCA 2896A.13.4.5.1.1 Test Purpose and
Environment 2896A.13.4.5.1.2 Test parameters 2896A.13.4.5.1.3 Test
Requirements 2900A.13.4.5.2 Inter-frequency RSSI measurement accuracy on
a carrier with CCA 2900A.13.4.5.2.1 Test Purpose and Environment
2900A.13.4.5.2.2 Test parameters 2900A.13.4.5.2.3 Test Requirements
2904A.13.4.6 Channel occupancy 2904A.13.4.6.1 Intra-frequency channel
occupancy measurement accuracy on SCC with CCA 2904A.13.4.6.1.1 Test
Purpose and Environment 2904A.13.4.6.1.2 Test parameters
2904A.13.4.6.1.3 Test Requirements 2908A.13.4.6.2 Inter-frequency
channel occupancy measurement accuracy on a carrier with CCA
2908A.13.4.6.2.1 Test Purpose and Environment 2908A.13.4.6.2.2 Test
parameters 2908A.13.4.6.2.3 Test Requirements 2912Annex B (normative):
Conditions for RRM requirements applicability for operating bands
2914B.1 Conditions for NR RRC\_IDLE state mobility 2914B.1.1
Introduction 2914B.1.2 Conditions for measurements on NR intra-frequency
cells for cell re-selection 2914B.1.3 Conditions for measurements on NR
inter-frequency cells for cell re-selection 2915B.2 Conditions for UE
measurements procedures and performance requirements in RRC\_CONNECTED
state 2916B.2.1 Introduction 2916B.2.1.1 General 2916B.2.1.2 Derivation
of Minimum SSB\_RP values for FR1 2916B.2.1.3 Derivation of Minimum
SSB\_RP values for FR2 2916B.2.1.3.1 Minimum SSB\_RP values for Rx Beam
Peak angle of arrival 2916B.2.1.3.2 Minimum SSB\_RP values for angle of
arrival within Spherical coverage 2917B.2.1.4 Gain to SS-RSRP and
CSI-RSRP measurement point for FR1 2917B.2.1.5 Gain to SS-RSRP and
CSI-RSRP measurement point for FR2 2918B.2.1.5.1 Gain to SS-RSRP and
CSI-RSRP measurement point for Rx Beam Peak angle of arrival
2918B.2.1.5.2 Gain to SS-RSRP measurement point for different frequency
2918B.2.1.5.3 Alignment of Rough beam to Rx beam Peak 2918B.2.1.6 Gain
to PRS-RSRP measurement point for FR2 2919B.2.1.6.1 Gain to PRS-RSRP
measurement point for Rx Beam Peak angle of arrival 2919B.2.2 Conditions
for NR intra-frequency measurements 2920B.2.3 Conditions for NR
inter-frequency measurements 2921B.2.4 Conditions for NR L1-RSRP
reporting 2922B.2.4.1 Conditions for SSB based L1-RSRP reporting
2922B.2.4.2 Conditions for CSI-RS based L1-RSRP reporting 2923B.2.5
Conditions for RRC connection release with redirection to NR 2925B.2.6
Void 2926B.2.6.1 Void 2926B.2.6.2 Void 2926B.2.7 Conditions for SRS-RSRP
measurements 2926B.2.8 Conditions for NR L1-SINR reporting 2927B.2.8.1
Conditions for L1-SINR reporting with CSI-RS based CMR and no dedicated
IMR configured 2927B.2.8.2 Conditions for L1-SINR reporting with SSB
based CMR and dedicated IMR configured 2928B.2.8.2.1 L1-SINR reporting
with SSB based CMR and dedicated ZP-IMR configured 2928B.2.8.2.2 L1-SINR
reporting with SSB based CMR and dedicated NZP-IMR configured
2928B.2.8.3 Conditions for L1-SINR reporting with CSI-RS based CMR and
dedicated IMR configured 2930B.2.8.3.1 L1-SINR reporting with CSI-RS
based CMR and dedicated ZP-IMR configured 2930B.2.8.3.2 L1-SINR
reporting with CSI-RS based CMR and dedicated NZP-IMR configured
2931B.2.9 Conditions for NR intra-frequency measurements under CCA
2932B.2.10 Conditions for NR inter-frequency measurements under CCA
2932B.2.11 Conditions for NR L1-RSRP reporting under CCA 2932B.2.11.1
Conditions for SSB based L1-RSRP reporting 2932B.2.12 Conditions for NR
CSI-RS based intra-frequency measurements 2933B.2.13 Conditions for NR
CSI-RS based inter-frequency measurements 2934B.2.14 Conditions for NR
PRS-based measurements 2936B.3 RRM Requirements Exceptions 2937B.3.1
Introduction 2937B.3.2 Receiver sensitivity relaxation for CA
2937B.3.2.1 Receiver sensitivity relaxation for UE supporting CA in FR1
2937B.3.2.2 Receiver sensitivity relaxation for UE configured with CA in
FR1 2938B.3.2.2.1 Inter-band carrier aggregation 2938B.3.2.2.2 Reference
sensitivity exceptions due to UL harmonic interference for CA
2938B.3.2.2.3 Reference sensitivity exceptions due to intermodulation
interference due to 2UL CA 2938B.3.2.3 Receiver sensitivity relaxation
for UE supporting CA in FR2 2938B.3.2.4 Receiver sensitivity relaxation
for UE configured with CA in FR2 2938B.3.2.4.1 Intra-band contiguous
carrier aggregation 2938B.3.2.4.2 Intra-band non-contiguous carrier
aggregation 2939B.3.3 Receiver sensitivity relaxation for DC 2939B.3.3.1
Receiver sensitivity relaxation for EN-DC 2939B.3.3.2 Receiver
sensitivity relaxation for NE-DC 2939B.3.4 Receiver sensitivity
relaxation for SUL 2939B.3.4.1 Receiver sensitivity relaxation for UE
supporting SUL in FR1 2939B.3.4.2 Receiver sensitivity relaxation for UE
configured with SUL in FR1 2939B.3.4.2.1 Reference sensitivity
exceptions due to UL harmonic interference for SUL 2939B.4 Conditions
for V2X 2939B.4.1 Test parameters for GNSS signals 2939B.4.2 Conditions
for PSBCH-RSRP Accuracy Requirements 2940B.4.3 Conditions for
Selection/Reselection to Intra-frequency SyncRef UE 2940B.4.4 Conditions
for L1 SL-RSRP Accuracy Requirements 2940Annex C (informative): Change
history 2942
