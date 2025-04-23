+---------------------------------------------+-----------------------+
| 3GPP TS 28.541 V16.17.0 (2023-09)           |                       |
+=============================================+=======================+
| Technical Specificationt                    |                       |
+---------------------------------------------+-----------------------+
| 3rd Generation Partnership Project;         |                       |
|                                             |                       |
| Technical Specification Group Services and  |                       |
| System Aspects;                             |                       |
|                                             |                       |
| Management and orchestration;               |                       |
|                                             |                       |
| 5G Network Resource Model (NRM);            |                       |
|                                             |                       |
| Stage 2 and stage 3                         |                       |
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

Foreword 21

Introduction 22

1 Scope 23

2 References 23

3 Definitions and abbreviations 25

3.1 Definitions 25

3.2 Abbreviations 26

4 Information model definitions for NR NRM 28

4.1 Imported and associated information 28

4.1.1 Imported information entities and local labels 28

4.1.2 Associated information entities and local labels 28

4.2 Class diagram 28

4.2.1 Class diagram for gNB and en-gNB 28

4.2.1.1 Relationships 28

4.2.1.2 Inheritance 34

4.3 Class definitions 37

4.3.1 GNBDUFunction 37

4.3.1.1 Definition 37

4.3.1.2 Attributes 38

4.3.1.3 Attribute constraints 38

4.3.1.4 Notifications 38

4.3.2 GNBCUCPFunction 38

4.3.2.1 Definition 38

4.3.2.2 Attributes 38

4.3.2.3 Attribute constraints 39

4.3.2.4 Notifications 39

4.3.3 GNBCUUPFunction 39

4.3.3.1 Definition 39

4.3.3.2 Attributes 40

4.3.3.3 Attribute constraints 40

4.3.3.4 Notifications 40

4.3.4 NRCellCU 40

4.3.4.1 Definition 40

4.3.4.2 Attributes 40

4.3.4.3 Void 40

4.3.4.4 Notifications 40

4.3.5 NRCellDU 40

4.3.5.1 Definition 40

4.3.5.2 Attributes 41

4.3.5.3 Attribute constraints 42

4.3.5.4 Notifications 42

4.3.6 NRSectorCarrier 42

4.3.6.1 Definition 42

4.3.6.2 Attributes 42

4.3.6.3 Attribute constraints 43

4.3.6.4 Notifications 43

4.3.7 BWP 43

4.3.7.1 Definition 43

4.3.7.2 Attributes 43

4.3.7.3 Attribute constraints 43

4.3.7.4 Notifications 43

4.3.8 EP\_E1 43

4.3.8.1 Definition 43

4.3.8.2 Attributes 44

4.3.8.3 Attribute constraints 44

4.3.8.4 Notifications 44

4.3.9 EP\_XnU 44

4.3.9.1 Definition 44

4.3.9.2 Attributes 44

4.3.9.3 Attribute constraints 44

4.3.9.4 Notifications 44

4.3.10 EP\_NgC 44

4.3.10.1 Definition 44

4.3.10.2 Attributes 45

4.3.10.3 Attribute constraints 45

4.3.10.4 Notifications 45

4.3.11 EP\_NgU 45

4.3.11.1 Definition 45

4.3.11.2 Attributes 45

4.3.11.3 Attribute constraints 45

4.3.11.4 Notifications 45

4.3.12 EP\_F1C 45

4.3.12.1 Definition 45

4.3.12.2 Attributes 46

4.3.12.3 Attribute constraints 46

4.3.12.4 Notifications 46

4.3.13 EP\_F1U 46

4.3.13.1 Definition 46

4.3.13.2 Attributes 46

4.3.13.3 Attribute constraints 46

4.3.13.4 Notifications 46

4.3.14 EP\_S1U 46

4.3.14.1 Definition 46

4.3.14.2 Attributes 47

4.3.14.3 Attribute constraints 47

4.3.14.4 Notifications 47

4.3.15 EP\_X2C 47

4.3.15.1 Definition 47

4.3.15.2 Attributes 47

4.3.15.3 Attribute constraints 47

4.3.15.4 Notifications 47

4.3.16 EP\_X2U 47

4.3.16.1 Definition 47

4.3.16.2 Attributes 47

4.3.16.3 Attribute constraints 48

4.3.16.4 Notifications 48

4.3.17 EP\_XnC 48

4.3.17.1 Definition 48

4.3.17.2 Attributes 48

4.3.17.3 Attribute constraints 48

4.3.17.4 Notifications 48

4.3.18 ExternalGNBCUCPFunction 48

4.3.18.1 Definition 48

4.3.18.2 Attributes 48

4.3.18.3 Attribute constraints 48

4.3.18.4 Notifications 49

4.3.19 ExternalGNBCUUPFunction 49

4.3.19.1 Definition 49

4.3.19.2 Attributes 49

4.3.19.3 Attribute constraints 49

4.3.19.4 Notifications 49

4.3.20 ExternalGNBDUFunction 49

4.3.20.1 Definition 49

4.3.20.2 Attributes 49

4.3.20.3 Attribute constraints 49

4.3.20.4 Notifications 49

4.3.21 ExternalUPFFunction 50

4.3.21.1 Definition 50

4.3.21.2 Attributes 50

4.3.21.3 Attribute constraints 50

4.3.21.4 Notifications 50

4.3.22 ExternalAMFFunction 50

4.3.22.1 Definition 50

4.3.22.2 Attributes 50

4.3.22.3 Attribute constraints 50

4.3.22.4 Notifications 50

4.3.23 Void 50

4.3.24 ENBFunction \<\<ProxyClass\>\> 50

4.3.24.1 Definition 50

4.3.24.2 Attributes 51

4.3.24.3 Attribute constraints 51

4.3.24.4 Notifications 51

4.3.25 GNBCUCPFunction \<\<ProxyClass\>\> 51

4.3.25.1 Definition 51

4.3.25.2 Attributes 51

4.3.25.3 Attribute constraints 51

4.3.25.4 Notifications 51

4.3.26 GNBCUUPFunction \<\<ProxyClass\>\> 51

4.3.26.1 Definition 51

4.3.26.2 Attributes 51

4.3.26.3 Attribute constraints 51

4.3.26.4 Notifications 51

4.3.27 GNBDUFunction \<\<ProxyClass\>\> 51

4.3.27.1 Definition 51

4.3.27.2 Attributes 52

4.3.27.3 Attribute constraints 52

4.3.27.4 Notifications 52

4.3.28 ServingGWFFunction \<\<ProxyClass\>\> 52

4.3.28.1 Definition 52

4.3.28.2 Attributes 52

4.3.28.3 Attribute constraints 52

4.3.28.4 Notifications 52

4.3.29 UPFFunction \<\<ProxyClass\>\> 52

4.3.29.1 Definition 52

4.3.29.2 Attributes 52

4.3.29.3 Attribute constraints 52

4.3.29.4 Notifications 52

4.3.30 AMFFunction \<\<ProxyClass\>\> 52

4.3.30.1 Definition 52

4.3.30.2 Attributes 53

4.3.30.3 Attribute constraints 53

4.3.30.4 Notifications 53

4.3.31 Void 53

4.3.32 NRCellRelation 53

4.3.32.1 Definition 53

4.3.32.2 Attributes 53

4.3.32.3 Attribute constraints 53

4.3.32.4 Notifications 53

4.3.33 NRFreqRelation 54

4.3.33.1 Definition 54

4.3.33.2 Attributes 54

4.3.33.3 Attribute constraints 54

4.3.33.4 Notifications 54

4.3.34 Void 54

4.3.35 ExternalNRCellCU 54

4.3.35.1 Definition 54

4.3.35.2 Attributes 55

4.3.35.3 Attribute constraints 55

4.3.35.4 Notifications 55

4.3.36 RRMPolicyRatio 55

4.3.36.1 Definition 55

4.3.36.2 Attributes 56

4.3.36.3 Attribute constraints 56

4.3.36.4 Notifications 56

4.3.37 S-NSSAI \<\<dataType\>\> 56

4.3.37.1 Definition 56

4.3.37.2 Attributes 56

4.3.37.3 Attribute constraints 56

4.3.37.4 Notifications 56

4.3.38 NRFrequency 57

4.3.38.1 Definition 57

4.3.38.2 Attributes 57

4.3.38.3 Attribute constraints 57

4.3.38.4 Notifications 57

4.3.39 CommonBeamformingFunction 57

4.3.39.1 Definition 57

4.3.39.2 Attributes 57

4.3.39.3 Attribute constraints 57

4.3.39.4 Notifications 58

4.3.40 Beam 58

4.3.40.1 Definition 58

4.3.40.2 Attributes 58

4.3.40.3 Attribute constraints 58

4.3.41 PLMNInfo \<\<dataType\>\> 58

4.3.41.1 Definition 58

4.3.41.2 Attributes 59

4.3.41.3 Attribute constraints 59

4.3.41.4 Notifications 59

4.3.42 RRMPolicyMember \<\<dataType\>\> 59

4.3.42.1 Definition 59

4.3.42.2 Attributes 59

4.3.42.3 Attribute constraints 59

4.3.42.4 Notifications 59

4.3.43 *RRMPolicy\_* 59

4.3.43.1 Definition 59

4.3.43.2 Attributes 60

4.3.43.3 Attribute constraints 60

4.3.43.4 Notifications 60

4.3.44 RRMPolicyManagedEntity \<\<ProxyClass\>\> 60

4.3.44.1 Definition 60

4.3.44.2 Attributes 60

4.3.44.3 Attribute constraints 60

4.3.44.4 Notifications 60

4.3.45 GNBCUCPNeighbour \<\<ProxyClass\>\> 61

4.3.45.1 Definition 61

4.3.45.2 Attributes 61

4.3.45.3 Attribute constraints 61

4.3.45.4 Notifications 61

4.3.46 GNBCUUPNeighbour \<\<ProxyClass\>\> 61

4.3.46.1 Definition 61

4.3.46.2 Attributes 61

4.3.46.3 Attribute constraints 61

4.3.46.4 Notifications 61

4.3.47 MappingSetIDBackhaulAddress \<\<dataType\>\> 61

4.3.47.1 Definition 61

4.3.47.2 Attributes 61

4.3.47.3 Attribute constraints 62

4.3.47.4 Notifications 62

4.3.48 BackhaulAddress \<\<dataType\>\> 62

4.3.48.1 Definition 62

4.3.48.2 Attributes 62

4.3.48.3 Attribute constraints 62

4.3.48.4 Notifications 62

4.3.49 Void 62

4.3.50 RimRSGlobal 62

4.3.50.1 Definition 62

4.3.50.2 Attributes 62

4.3.50.3 Attribute constraints 62

4.3.50.4 Notifications 63

4.3.51 FrequencyDomainPara \<\<dataType\>\> 63

4.3.51.1 Definition 63

4.3.51.2 Attributes 63

4.3.51.3 Attribute constraints 63

4.3.51.4 Notifications 63

4.3.52 SequenceDomainPara \<\<dataType\>\> 63

4.3.52.1 Definition 63

4.3.52.2 Attributes 63

4.3.52.3 Attribute constraints 64

4.3.52.4 Notifications 64

4.3.53 TimeDomainPara \<\<dataType\>\> 64

4.3.53.1 Definition 64

4.3.53.2 Attributes 64

4.3.53.3 Attribute constraints 64

4.3.53.4 Notifications 64

4.3.54 RimRSReportConf \<\<dataType\>\> 64

4.3.54.1 Definition 64

4.3.54.2 Attributes 64

4.3.54.3 Attribute constraints 65

4.3.54.4 Notifications 65

4.3.55 RimRSReportInfo \<\<dataType\>\> 65

4.3.55.1 Definition 65

4.3.55.2 Attributes 65

4.3.55.3 Attribute constraints 65

4.3.55.4 Notifications 65

4.3.57 DANRManagementFunction 66

4.3.57.1 Definition 66

4.3.57.2 Attributes 66

4.3.57.3 Attribute constraints 66

4.3.57.4 Notifications 66

4.3.58 DESManagementFunction 66

4.3.58.1 Definition 66

4.3.58.2 Attributes 66

4.3.58.3 Attribute constraints 67

4.3.58.4 Notification 67

4.3.59 DRACHOptimizationFunction 67

4.3.59.1 Definition 67

4.3.59.2 Attributes 67

4.3.59.3 Attribute constraints 68

4.3.59.4 Notifications 68

4.3.60 DMROFunction 68

4.3.60.1 Definition 68

4.3.60.2 Attributes 68

4.3.60.3 Attribute constraints 68

4.3.60.4 Notifications 68

4.3.61 DPCIConfigurationFunction 68

4.3.61.1 Definition 68

4.3.61.2 Attributes 68

4.3.61.3 Attribute constraints 69

4.3.61.4 Notifications 69

4.3.62 CPCIConfigurationFunction 69

4.3.62.1 Definition 69

4.3.62.2 Attributes 69

4.3.62.3 Attribute constraints 69

4.3.62.4 Notifications 69

4.3.63 CESManagementFunction 69

4.3.63.1 Definition 69

4.3.63.2 Attributes 69

4.3.63.3 Attribute constraints 70

4.3.63.4 Notification 70

4.3.64 AddressWithVlan \<\<dataType\>\> 70

4.3.64.1 Definition 70

4.3.64.2 Attributes 71

4.3.64.3 Attribute constraints 71

4.3.64.4 Notifications 71

4.3.65 TceIDMappingInfo \<\<dataType\>\> 71

4.3.65.1 Definition 71

4.3.65.2 Attributes 71

4.3.65.3 Attribute constraints 71

4.3.65.4 Notifications 71

4.4 Attribute definitions 71

4.4.1 Attribute properties 71

4.5 Common notifications 99

4.5.1 Alarm notifications 99

4.5.2 Configuration notifications 99

4.5.3 Threshold Crossing notifications 100

5 Information Model definitions for 5GC NRM 100

5.1 Imported information entities and local labels 100

5.2 Class diagram 100

5.2.1 Class diagram of 5GC NFs 100

5.2.1.1 Relationships 100

5.2.1.2 Inheritance 107

5.2.2 Class diagram of AMF Region/AMF Set 110

5.2.2.1 Relationships 110

5.2.2.2 Inheritance 111

5.3 Class definitions 111

5.3.1 AMFFunction 111

5.3.1.1 Definition 111

5.3.1.2 Attributes 112

5.3.1.3 Attribute constraints 112

5.3.1.4 Notifications 112

5.3.2 SMFFunction 112

5.3.2.1 Definition 112

5.3.2.2 Attributes 112

5.3.2.3 Attribute constraints 112

5.3.2.4 Notifications 112

5.3.3 UPFFunction 113

5.3.3.1 Definition 113

5.3.3.2 Attributes 113

5.3.3.3 Attribute constraints 113

5.3.3.4 Notifications 113

5.3.4 N3IWFFunction 113

5.3.4.1 Definition 113

5.3.4.2 Attributes 113

5.3.4.3 Attribute constraints 113

5.3.4.4 Notifications 113

5.3.5 PCFFunction 114

5.3.5.1 Definition 114

5.3.5.2 Attributes 114

5.3.5.3 Attribute constraints 114

5.3.5.4 Notifications 114

5.3.6 AUSFFunction 114

5.3.6.1 Definition 114

5.3.6.2 Attributes 114

5.3.6.3 Attribute constraints 114

5.3.6.4 Notifications 115

5.3.7 UDMFunction 115

5.3.7.1 Definition 115

5.3.7.2 Attributes 115

5.3.5.3 Attribute constraints 115

5.3.5.4 Notifications 115

5.3.8 UDRFunction 115

5.3.8.1 Definition 115

5.3.8.2 Attributes 115

5.3.8.3 Attribute constraints 115

5.3.8.4 Notifications 116

5.3.9 UDSFFunction 116

5.3.9.1 Definition 116

5.3.9.2 Attributes 116

5.3.9.3 Attribute constraints 116

5.3.9.4 Notifications 116

5.3.10 NRFFunction 116

5.3.10.1 Definition 116

5.3.10.2 Attributes 116

5.3.10.3 Attribute constraints 117

5.3.10.4 Notifications 117

5.3.11 NSSFFunction 117

5.3.11.1 Definition 117

5.3.11.2 Attributes 117

5.3.11.3 Attribute constraints 117

5.3.11.4 Notifications 117

5.3.12 AFFunction 117

5.3.12.1 Definition 117

5.3.13 DNFunction 117

5.3.13.1 Definition 117

5.3.14 SMSFFunction 118

5.3.14.1 Definition 118

5.3.14.2 Attributes 118

5.3.14.3 Attribute constraints 118

5.3.14.4 Notifications 118

5.3.15 LMFFunction 118

5.3.15.1 Definition 118

5.3.15.2 Attributes 118

5.3.15.3 Attribute constraints 118

5.3.15.4 Notifications 118

5.3.16 NGEIRFunction 118

5.3.16.1 Definition 118

5.3.16.2 Attributes 119

5.3.16.3 Attribute constraints 119

5.3.16.4 Notifications 119

5.3.17 SEPPFunction 119

5.3.17.1 Definition 119

5.3.17.2 Attributes 119

5.3.17.3 Attribute constraints 119

5.3.17.4 Notifications 119

5.3.18 NWDAFFunction 119

5.3.18.1 Definition 119

5.3.18.2 Attributes 119

5.3.18.3 Attribute constraints 120

5.3.18.4 Notifications 120

5.3.19 EP\_N2 120

5.3.19.1 Definition 120

5.3.19.2 Attributes 120

5.3.19.3 Attribute constraints 120

5.3.19.4 Notifications 120

5.3.20 EP\_N3 120

5.3.20.1 Definition 120

5.3.20.2 Attributes 120

5.3.20.3 Attribute constraints 121

5.3.20.4 Notifications 121

5.3.21 EP\_N4 121

5.3.21.1 Definition 121

5.3.21.2 Attributes 121

5.3.21.3 Attribute constraints 121

5.3.21.4 Notifications 121

5.3.22 EP\_N5 121

5.3.22.1 Definition 121

5.3.22.2 Attributes 121

5.3.22.3 Attribute constraints 121

5.3.22.4 Notifications 121

5.3.23 EP\_N6 122

5.3.23.1 Definition 122

5.3.23.2 Attributes 122

5.3.23.3 Attribute constraints 122

5.3.23.4 Notifications 122

5.3.24 EP\_N7 122

5.3.24.1 Definition 122

5.3.24.2 Attributes 122

5.3.24.3 Attribute constraints 122

5.3.24.4 Notifications 122

5.3.25 EP\_N8 122

5.3.25.1 Definition 122

5.3.25.2 Attributes 123

5.3.25.3 Attribute constraints 123

5.3.25.4 Notifications 123

5.3.26 EP\_N9 123

5.3.26.1 Definition 123

5.3.26.2 Attributes 123

5.3.26.3 Attribute constraints 123

5.3.26.4 Notifications 123

5.3.27 EP\_N10 123

5.3.27.1 Definition 123

5.3.27.2 Attributes 123

5.3.27.3 Attribute constraints 124

5.3.27.4 Notifications 124

5.3.28 EP\_N11 124

5.3.28.1 Definition 124

5.3.28.2 Attributes 124

5.3.28.3 Attribute constraints 124

5.3.28.4 Notifications 124

5.3.29 EP\_N12 124

5.3.29.1 Definition 124

5.3.29.2 Attributes 124

5.3.29.3 Attribute constraints 124

5.3.29.4 Notifications 124

5.3.30 EP\_N13 125

5.3.30.1 Definition 125

5.3.30.2 Attributes 125

5.3.30.3 Attribute constraints 125

5.3.30.4 Notifications 125

5.3.31 EP\_N14 125

5.3.31.1 Definition 125

5.3.31.2 Attributes 125

5.3.31.3 Attribute constraints 125

5.3.31.4 Notifications 125

5.3.32 EP\_N15 125

5.3.32.1 Definition 125

5.3.32.2 Attributes 126

5.3.32.3 Attribute constraints 126

5.3.32.4 Notifications 126

5.3.33 EP\_N16 126

5.3.33.1 Definition 126

5.3.33.2 Attributes 126

5.3.33.3 Attribute constraints 126

5.3.33.4 Notifications 126

5.3.34 EP\_N17 126

5.3.34.1 Definition 126

5.3.34.2 Attributes 126

5.3.34.3 Attribute constraints 127

5.3.34.4 Notifications 127

5.3.35 EP\_N20 127

5.3.35.1 Definition 127

5.3.35.2 Attributes 127

5.3.35.3 Attribute constraints 127

5.3.35.4 Notifications 127

5.3.36 EP\_N21 127

5.3.36.1 Definition 127

5.3.36.2 Attributes 127

5.3.36.3 Attribute constraints 127

5.3.36.4 Notifications 127

5.3.37 EP\_N22 128

5.3.37.1 Definition 128

5.3.37.2 Attributes 128

5.3.37.3 Attribute constraints 128

5.3.37.4 Notifications 128

5.3.38 EP\_N26 128

5.3.38.1 Definition 128

5.3.38.2 Attributes 128

5.3.38.3 Attribute constraints 128

5.3.38.4 Notifications 128

5.3.39 Void 129

5.3.40 Void 129

5.3.41 EP\_S5C 129

5.3.41.1 Definition 129

5.3.41.2 Attributes 129

5.3.41.3 Attribute constraints 129

5.3.41.4 Notifications 129

5.3.42 EP\_S5U 129

5.3.42.1 Definition 129

5.3.42.2 Attributes 129

5.3.42.3 Attribute constraints 129

5.3.42.4 Notifications 129

5.3.43 EP\_Rx 130

5.3.43.1 Definition 130

5.3.43.2 Attributes 130

5.3.43.3 Attribute constraints 130

5.3.43.4 Notifications 130

5.3.44 EP\_MAP\_SMSC 130

5.3.44.1 Definition 130

5.3.44.2 Attributes 130

5.3.44.3 Attribute constraints 130

5.3.44.4 Notifications 130

5.3.45 EP\_NLS 130

5.3.45.1 Definition 130

5.3.45.2 Attributes 131

5.3.45.3 Attribute constraints 131

5.3.45.4 Notifications 131

5.3.46 EP\_NLG 131

5.3.46.1 Definition 131

5.3.46.2 Attributes 131

5.3.46.3 Attribute constraints 131

5.3.46.4 Notifications 131

5.3.47 EP\_N27 131

5.3.47.1 Definition 131

5.3.47.2 Attributes 131

5.3.47.3 Attribute constraints 132

5.3.47.4 Notifications 132

5.3.48 EP\_N31 132

5.3.48.1 Definition 132

5.3.48.2 Attributes 132

5.3.48.3 Attribute constraints 132

5.3.48.4 Notifications 132

5.3.49 ExternalNRFFunction 132

5.3.49.1 Definition 132

5.3.49.2 Attributes 132

5.3.49.3 Attribute constraints 132

5.3.49.4 Notifications 132

5.3.50 ExternalNSSFFunction 133

5.3.50.1 Definition 133

5.3.50.2 Attributes 133

5.3.50.3 Attribute constraints 133

5.3.50.4 Notifications 133

5.3.51 AMFSet 133

5.3.51.1 Definition 133

5.3.51.2 Attributes 133

5.3.51.3 Attribute constraints 133

5.3.51.4 Notifications 133

5.3.52 AMFRegion 134

5.3.52.1 Definition 134

5.3.52.2 Attributes 134

5.3.52.3 Attribute constraints 134

5.3.52.4 Notifications 134

5.3.53 ExternalAMFFunction 134

5.3.53.1 Definition 134

5.3.53.2 Attributes 134

5.3.53.3 Attribute constraints 134

5.3.53.4 Notifications 134

5.3.54 ManagedNFProfile \<\<dataType\>\> 135

5.3.54.1 Definition 135

5.3.54.2 Attributes 135

5.3.54.3 Attribute constraints 135

5.3.54.4 Notifications 135

5.3.55 HostAddr \<\<choice\>\> 135

5.3.55.1 Definition 135

5.3.56 NFInfo \<\<choice\>\> 135

5.3.56.1 Definition 135

5.3.57 UdmInfo \<\<dataType\>\> 136

5.3.57.1 Definition 136

5.3.57.2 Attributes 136

5.3.57.3 Attribute constraints 136

5.3.57.4 Notifications 136

5.3.58 AusfInfo \<\<dataType\>\> 136

5.3.58.1 Definition 136

5.3.58.2 Attributes 136

5.3.58.3 Attribute constraints 136

5.3.58.4 Notifications 137

5.3.59 UpfInfo \<\<dataType\>\> 137

5.3.59.1 Definition 137

5.3.59.2 Attributes 137

5.3.59.3 Attribute constraints 137

5.3.59.4 Notifications 137

5.3.60 AmfInfo \<\<dataType\>\> 137

5.3.60.1 Definition 137

5.3.60.2 Attributes 137

5.3.60.3 Attribute constraints 137

5.3.60.4 Notifications 137

5.3.61 Udrinfo \<\<dataType\>\> 137

5.3.61.1 Definition 137

5.3.61.2 Attributes 138

5.3.61.3 Attribute constraints 138

5.3.61.4 Notifications 138

5.3.62 EP\_N32 138

5.3.62.1 Definition 138

5.3.62.2 Attributes 138

5.3.62.3 Attribute constraints 138

5.3.62.4 Notifications 138

5.3.63 ExternalSEPPFunction 138

5.3.63.1 Definition 138

5.3.63.2 Attributes 138

5.3.63.3 Attribute constraints 139

5.3.63.4 Notifications 139

5.3.64 SEPPFunction \<\<ProxyClass\>\> 139

5.3.64.1 Definition 139

5.3.64.2 Attributes 139

5.3.64.3 Attribute constraints 139

5.3.64.4 Notifications 139

5.3.65 NEFFunction 139

5.3.65.1 Definition 139

5.3.65.2 Attributes 139

5.3.65.3 Attribute constraints 139

5.3.65.4 Notifications 140

5.3.66 SCPFunction 140

5.3.67.1 Definition 140

5.3.67.2 Attributes 140

5.3.67.3 Attribute constraints 140

5.3.67.4 Notifications 140

5.3.68 SupportedFunction \<\<dataType\>\> 140

5.3.68.1 Definition 140

5.3.68.2 Attributes 140

5.3.68.3 Attribute constraints 140

5.3.68.4 Notifications 140

5.3.69 CommModel \<\<dataType\>\> 140

5.3.69.1 Definition 140

5.3.69.2 Attributes 141

5.3.69.3 Attribute constraints 141

5.3.69.4 Notifications 141

5.3.70 QFQoSMonitoringControl 141

5.3.70.1 Definition 141

5.3.70.2 Attributes 141

5.3.70.3 Attribute constraints 141

5.3.70.4 Notifications 141

5.3.71 QFDelayThresholdsType \<\<dataType\>\> 142

5.3.71.1 Definition 142

5.3.71.2 Attributes 142

5.3.71.3 Attribute constraints 142

5.3.71.4 Notifications 142

5.3.72 GtpUPathQoSMonitoringControl 142

5.3.72.1 Definition 142

5.3.72.2 Attributes 142

5.3.72.3 Attribute constraints 143

5.3.72.4 Notifications 143

5.3.73 GtpUPathDelayThresholdsType \<\<dataType\>\> 143

5.3.73.1 Definition 143

5.3.73.2 Attributes 143

5.3.73.3 Attribute constraints 143

5.3.73.4 Notifications 143

5.3.75 Configurable5QISet 143

5.3.75.1 Definition 143

5.3.75.2 Attributes 143

5.3.75.3 Attribute constraints 144

5.3.75.4 Notifications 144

5.3.76 FiveQICharacteristics \<\<dataType\>\> 144

5.3.76.1 Definition 144

5.3.76.2 Attributes 144

5.3.76.3 Attribute constraints 144

5.3.76.4 Notifications 144

5.3.77 PacketErrorRate \<\<dataType\>\> 144

5.3.77.1 Definition 144

5.3.77.2 Attributes 144

5.3.77.3 Attribute constraints 144

5.3.77.4 Notifications 145

5.3.78 FiveQiDscpMappingSet 145

5.3.78.1 Definition 145

5.3.78.2 Attributes 145

5.3.78.3 Attribute constraints 145

5.3.78.4 Notifications 145

5.3.79 FiveQiDscpMapping \<\<dataType\>\> 145

5.3.79.1 Definition 145

5.3.79.2 Attributes 145

5.3.79.3 Attribute constraints 145

5.3.79.4 Notifications 145

5.3.80 PredefinedPccRuleSet 145

5.3.80.1 Definition 145

5.3.80.2 Attributes 146

5.3.80.3 Attribute constraints 146

5.3.80.4 Notifications 146

5.3.81 PccRule \<\<dataType\>\> 146

5.3.81.1 Definition 146

5.3.81.2 Attributes 146

5.3.81.3 Attribute constraints 146

5.3.81.4 Notifications 146

5.3.82 FlowInformation \<\<dataType\>\> 147

5.3.82.1 Definition 147

5.3.82.2 Attributes 147

5.3.82.3 Attribute constraints 147

5.3.82.4 Notifications 147

5.3.83 EthFlowDescription \<\<dataType\>\> 147

5.3.83.1 Definition 147

5.3.83.2 Attributes 147

5.3.83.3 Attribute constraints 147

5.3.83.4 Notifications 147

5.3.84 QoSData \<\<dataType\>\> 148

5.3.84.1 Definition 148

5.3.84.2 Attributes 148

5.3.84.3 Attribute constraints 148

5.3.84.4 Notifications 148

5.3.85 ARP \<\<dataType\>\> 148

5.3.85.1 Definition 148

5.3.85.2 Attributes 148

5.3.85.3 Attribute constraints 148

5.3.85.4 Notifications 148

5.3.86 TrafficControlData \<\<dataType\>\> 149

5.3.86.1 Definition 149

5.3.86.2 Attributes 149

5.3.86.3 Attribute constraints 149

5.3.86.4 Notifications 149

5.3.87 RedirectInformation \<\<dataType\>\> 149

5.3.87.1 Definition 149

5.3.87.2 Attributes 149

5.3.87.3 Attribute constraints 149

5.3.87.4 Notifications 149

5.3.88 RouteToLocation \<\<dataType\>\> 150

5.3.88.1 Definition 150

5.3.88.2 Attributes 150

5.3.88.3 Attribute constraints 150

5.3.88.4 Notifications 150

5.3.89 RouteInformation \<\<dataType\>\> 150

5.3.89.1 Definition 150

5.3.89.2 Attributes 150

5.3.89.3 Attribute constraints 150

5.3.89.4 Notifications 150

5.3.90 UpPathChgEvent \<\<dataType\>\> 150

5.3.90.1 Definition 150

5.3.90.2 Attributes 151

5.3.90.3 Attribute constraints 151

5.3.90.4 Notifications 151

5.3.91 SteeringMode \<\<dataType\>\> 151

5.3.91.1 Definition 151

5.3.91.2 Attributes 151

5.3.91.3 Attribute constraints 151

5.3.91.4 Notifications 151

5.3.92 ConditionData \<\<dataType\>\> 151

5.3.92.1 Definition 151

5.3.92.2 Attributes 152

5.3.92.3 Attribute constraints 152

5.3.92.4 Notifications 152

5.3.93 TscaiInputContainer \<\<dataType\>\> 152

5.3.93.1 Definition 152

5.3.93.2 Attributes 152

5.3.93.3 Attribute constraints 152

5.3.93.4 Notifications 152

5.3.94 Dynamic5QISet 152

5.3.94.1 Definition 152

5.3.94.2 Attributes 153

5.3.94.3 Attribute constraints 153

5.3.94.4 Notifications 153

5.4 Attribute definitions 153

5.4.1 Attribute properties 153

5.5 Common notifications 172

5.5.1 Alarm notifications 172

5.5.2 Configuration notifications 172

5.5.3 Threshold Crossing notifications 172

6 Information model definitions for network slice NRM 172

6.1 Imported information entities and local labels 172

6.2 Class diagram 173

6.2.1 Relationships 173

6.2.2 Inheritance 174

6.3 Class definitions 174

6.3.1 NetworkSlice 174

6.3.1.1 Definition 174

6.3.1.2 Attributes 175

6.3.1.3 Attribute constraints 175

6.3.1.4 Notifications 175

6.3.2 NetworkSliceSubnet 175

6.3.2.1 Definition 175

6.3.2.2 Attributes 175

6.3.2.3 Attribute constraints 175

6.3.2.4 Notifications 175

6.3.3 ServiceProfile \<\<dataType\>\> 176

6.3.3.1 Definition 176

6.3.3.2 Attributes 176

6.3.3.3 Attribute constraints 176

6.3.3.4 Notifications 176

6.3.4 SliceProfile \<\<dataType\>\> 176

6.3.4.1 Definition 176

6.3.4.2 Attributes 177

6.3.4.3 Attribute constraints 177

6.3.4.4 Notifications 177

6.3.5 NsInfo \<\<dataType\>\> 177

6.3.5.1 Definition 177

6.3.5.2 Attributes 177

6.3.5.3 Attribute constraints 177

6.3.5.4 Notifications 177

6.3.6 ServAttrCom \<\<dataType\>\> 177

6.3.6.1 Definition 177

6.3.6.2 Attributes 177

6.3.6.3 Attribute constraints 178

6.3.6.4 Notifications 178

6.3.7 DelayTolerance\<\<dataType\>\> 178

6.3.7.1 Definition 178

6.3.7.2 Attributes 178

6.3.7.3 Attribute constraints 178

6.3.7.4 Notifications 178

6.3.8 DeterministicComm \<\<dataType\>\> 178

6.3.8.1 Definition 178

6.3.8.2 Attributes 178

6.3.8.3 Attribute constraints 178

6.3.8.4 Notifications 178

6.3.9 DLThpt\<\<dataType\>\> 179

6.3.9.1 Definition 179

6.3.9.2 Attributes 179

6.3.9.3 Attribute constraints 179

6.3.9.4 Notifications 179

6.3.10 ULThpt\<\<dataType\>\> 179

6.3.10.1 Definition 179

6.3.10.2 Attributes 179

6.3.10.3 Attribute constraints 179

6.3.10.4 Notifications 179

6.3.11 MaxPktSize \<\<dataType\>\> 179

6.3.11.1 Definition 179

6.3.11.2 Attributes 180

6.3.11.3 Attribute constraints 180

6.3.11.4 Notifications 180

6.3.12 MaxNumberofConns \<\<dataType\>\> 180

6.3.12.1 Definition 180

6.3.12.2 Attributes 180

6.3.12.3 Attribute constraints 180

6.3.12.4 Notifications 180

6.3.13 Void 180

6.3.14 KPIMonitoring \<\<dataType\>\> 180

6.3.14.1 Definition 180

6.3.14.2 Attributes 180

6.3.14.3 Attribute constraints 180

6.3.14.4 Notifications 181

6.3.15 UserMgmtOpen\<\<dataType\>\> 181

6.3.15.1 Definition 181

6.3.15.2 Attributes 181

6.3.15.3 Attribute constraints 181

6.3.15.4 Notifications 181

6.3.16 V2XCommMode\<\<dataType\>\> 181

6.3.16.1 Definition 181

6.3.16.2 Attributes 181

6.3.16.3 Attribute constraints 181

6.3.16.4 Notifications 181

6.3.17 TermDensity\<\<dataType\>\> 181

6.3.17.1 Definition 181

6.3.17.2 Attributes 182

6.3.17.3 Attribute constraints 182

6.3.17.4 Notifications 182

6.3.18 EP\_Transport 182

6.3.18.1 Definition 182

6.3.18.2 Attributes 182

6.3.18.3 Attribute constraints 182

6.3.18.4 Notifications 182

6.3.19 EP\_Application \<\<ProxyClass\>\> 182

6.3.19.1 Definition 182

6.3.19.2 Attributes 182

6.3.19.3 Attribute constraints 183

6.3.19.4 Notifications 183

6.4 Attribute definition 183

6.4.1 Attribute properties 183

6.5 Common notifications 191

6.5.1 Alarm notifications 191

6.5.2 Configuration notifications 191

6.5.3 Threshold Crossing notifications 191

7 Solution Set (SS) 191

Annex A (normative): Cell state handling 194

A.1 Relation between the administrative state and the \"Pre-operation
state of the gNB-DU Cell\" 194

A.2 Combined state diagram for gNB cell 194

Annex B (normative): NSI and NSSI state handling 197

B.1 NSI state handling 197

B.2 State handling of NSSI 198

Annex C (normative): XML definitions for NR NRM 200

C.1 General 200

C.2 Architectural features 200

C.3 Mapping 200

C.3.1 General mapping 200

C.3.2 Information Object Class (IOC) mapping 200

C.4 Solution Set definitions 200

C.4.1 XML definition structure 200

C.4.2 Graphical representation 200

C.4.3 XML schema \"nRNrm.xsd\" 201

Annex D (normative): OpenAPI definition of the NR NRM 225

D.1 General 225

D.2 Void 225

D.3 Void 225

D.4 Solution Set (SS) definitions 225

D.4.1 Void 225

D.4.2 Void 225

D.4.3 OpenAPI document \"TS28541\_NrNrm.yaml\" 225

Annex E (normative): YANG definitions for NR NRM 250

E.1 General 250

E.2 Void 250

E.3 Void 250

E.4 Void 250

E.5 Modules 250

E.5.1 module \_3gpp-nr-nrm-beam.yang 250

E.5.1a module \_3gpp-nr-nrm-bwp.yang 252

E.5.1b module \_3gpp-nr-nrm-commonbeamformingfunction.yang 253

E.5.2 module\_3gpp-nr-nrm-ep.yang 254

E.5.3 module \_3gpp-nr-nrm-eutrancellrelation.yang 257

E.5.4 module \_3gpp-nr-nrm-eutranetwork.yang 260

E.5.5 module \_3gpp-nr-nrm-eutranfreqrelation.yang 261

E.5.6 module \_3gpp-nr-nrm-eutranfrequency.yang 263

E.5.7 module \_3gpp-nr-nrm-externalamffunction.yang 264

E.5.8 module \_3gpp-nr-nrm-externalenbfunction.yang 265

E.5.9 module\_3gpp-nr-nrm-externaleutrancell.yang 266

E.5.10 module \_3gpp-nr-nrm-externalgnbcucpfunction.yang 268

E.5.11 module \_3gpp-nr-nrm-externalgnbcuupfunction.yang 269

E.5.12 module \_3gpp-nr-nrm-externalgnbdufunction.yang 270

E.5.13 module \_3gpp-nr-nrm-externalnrcellcu.yang 271

E.5.14 module \_3gpp-nr-nrm-externalservinggwfunction.yang 272

E.5.15 module \_3gpp-nr-nrm-externalupffunction.yang 273

E.5.16 module \_3gpp-nr-nrm-gnbcucpfunction.yang 274

E.5.17 module \_3gpp-nr-nrm-gnbcuupfunction.yang 276

E.5.18 module\_3gpp-nr-nrm-gnbdufunction.yang 278

E.5.19 module \_3gpp-nr-nrm-nrcellcu.yang 279

E.5.20 module \_3gpp-nr-nrm-nrcelldu.yang 280

E.5.21 module \_3gpp-nr-nrm-nrcellrelation.yang 283

E.5.22 module \_3gpp-nr-nrm-nrfreqrelation.yang 285

E.5.23 module \_3gpp-nr-nrm-nrfrequency.yang 288

E.5.24 module \_3gpp-nr-nrm-nrnetwork.yang 289

E.5.25 module \_3gpp-nr-nrm-nrsectorcarrier.yang 290

E.5.26 module \_3gpp-nr-nrm-rrmpolicy.yang 292

E.5.27 Void 293

E.5.28 module \_3gpp-nr-nrm-danrmanagementfunction.yang 293

E.5.29 module \_3gpp-nr-nrm-desmanagementfunction.yang 294

E.5.30 module \_3gpp-nr-nrm-drachoptimizationfunction.yang 297

E.5.31 module \_3gpp-nr-nrm-dmrofunction.yang 298

E.5.32 module \_3gpp-nr-nrm-dpciconfigurationfunction.yang 299

E.5.33 module \_3gpp-nr-nrm-cpciconfigurationfunction.yang 301

E.5.34 module \_3gpp-nr-nrm-cesmanagementfunction.yang 302

E.6 Void 305

E.7 Mount information 305

Annex F (normative): XML definitions for 5GC NRM 306

F.1 General 306

F.2 Architectural features 306

F.3 Mapping 306

F.3.1 General mapping 306

F.3.2 Information Object Class (IOC) mapping 306

F.4 Solution Set definitions 306

F.4.1 XML definition structure 306

F.4.2 Graphical representation 306

F.4.3 XML schema \"ngcNrm.xsd\" 307

Annex G (normative): OpenAPI definition of the 5GC NRM 337

G.1 General 337

G.2 Void 337

G.3 Void 337

G.4 Solution Set (SS) definitions 337

G.4.1 Void 337

G.4.2 Void 337

G.4.3 OpenAPI document \"TS28541\_5GcNrm.yaml\" 337

Annex H (normative): YANG definitions for 5GC 364

H.1 General 364

H.2 Void 364

H.3 Void 364

H.4 Void 364

H.5 Modules 364

H.5.1 module \_3gpp-5g-common-yang-types.yang 364

H.5.1a module \_3gpp-5gc-nrm-affunction.yang 366

H.5.2 module \_3gpp-5gc-nrm-amffunction.yang 367

H.5.3 module \_3gpp-5gc-nrm-amfregion.yang 368

H.5.4 module \_3gpp-5gc-nrm-amfset.yang 369

H.5.5 module \_3gpp-5gc-nrm-ausffunction.yang 370

H.5.6 module \_3gpp-5gc-nrm-dnfunction.yang 371

H.5.7 module \_3gpp-5gc-nrm-ep.yang 372

H.5.8 module \_3gpp-5gc-nrm-externalnrffunction.yang 380

H.5.9 module \_3gpp-5gc-nrm-externalnssffunction.yang 381

H.5.10 module \_3gpp-5gc-nrm-lmffunction.yang 381

H.5.11 module \_3gpp-5gc-nrm-n3iwffunction.yang 382

H.5.12 module \_3gpp-5gc-nrm-nfprofile.yang 383

H.5.13 module \_3gpp-5gc-nrm-nfservice.yang 398

H.5.14 module \_3gpp-5gc-nrm-ngeirfunction.yang 402

H.5.15 module \_3gpp-5gc-nrm-nrffunction.yang 403

H.5.16 module \_3gpp-5gc-nrm-nssffunction.yang 404

H.5.17 module \_3gpp-5gc-nrm-nwdaffunction.yang 406

H.5.18 module \_3gpp-5gc-nrm-pcffunction.yang 407

H.5.19 module \_3gpp-5gc-nrm-seppfunction.yang 408

H.5.19a module \_3gpp-5gc-nrm- externalseppfunction.yang 409

H.5.20 module \_3gpp-5gc-nrm-smffunction 410

H.5.21 module \_3gpp-5gc-nrm-smsffunction.yang 411

H.5.22 module \_3gpp-5gc-nrm-udmfunction.yang 412

H.5.23 module \_3gpp-5gc-nrm-udrfunction.yang 413

H.5.24 module \_3gpp-5gc-nrm-udsffunction.yang 414

H.5.25 module \_3gpp-5gc-nrm-upffunction.yang 416

H.5.26 module \_3gpp-5gc-nrm-scpfunction.yang 417

H.5.27 module \_3gpp-5gc-nrm-neffunction.yang 417

H.5.28 module \_3gpp-5gc-nrm-QFQoSMonitoringControl.yang 418

H.5.29 module \_3gpp-5gc-nrm-GtpUPathQoSMonitoringControl.yang 420

H.5.30 module \_3gpp-5gc-nrm-Configurable5QISet.yang 422

H.5.31 module \_3gpp-5gc-nrm-FiveQiDscpMappingSet.yang 424

H.5.32 module \_3gpp-5gc-nrm-PredefinedPccRuleSet.yang 425

H.5.33 module \_3gpp-5gc-nrm-dynamic5QISet.yang 433

H.6 Void 434

H.7 Mount information 434

Annex I (normative): XML definitions for network slice 435

I.1 General 435

I.2 Architectural features 435

I.3 Mapping 435

I.3.1 General mapping 435

I.3.2 Information Object Class (IOC) mapping 435

I.4 Solution Set (SS) definitions 435

I.4.1 XML definition structure 435

I.4.2 Graphical representation 435

I.4.3 XML schema \"sliceNrm.xsd\" 436

Annex J (normative): OpenAPI definition of the Slice NRM 440

J.1 General 440

J.2 Void 440

J.3 Void 440

J.4 Solution Set (SS) definitions 440

J.4.1 Void 440

J.4.2 Void 440

J.4.3 OpenAPI document \"TS28541\_SliceNrm.yaml\" 440

\- \$ref: \'\#/components/schemas/EP\_Transport-Single\' 446

Annex K (normative): Void 447

Annex L (normative): Relation of GSMA GST, ServiceProfile and
SliceProfile 448

L.1 General 448

L.2 GSMA GST, ServiceProfile and sliceProfile 448

Annex M (normative): Managed NF Service state handling 449

M.1 Combined state diagram for a Managed NF Service 449

Annex N (informative): Mapping between GSMA GST and ServiceProfile 451

Annex O (informative): Change history 453

 Foreword
========

This Technical Specification has been produced by the 3rd Generation
Partnership Project (3GPP).

The contents of the present document are subject to continuing work
within the TSG and may change following formal TSG approval. Should the
TSG modify the contents of the present document, it will be re-released
by the TSG with an identifying change of release date and an increase in
version number as follows:

Version x.y.z

where:

x the first digit:

1 presented to TSG for information;

2 presented to TSG for approval;

3 or greater indicates TSG approved document under change control.

y the second digit is incremented for all changes of substance, i.e.
technical enhancements, corrections, updates, etc.

z the third digit is incremented when editorial only changes have been
incorporated in the document.

In the present document, modal verbs have the following meanings:

**shall** indicates a mandatory requirement to do something

**shall not** indicates an interdiction (prohibition) to do something

The constructions \"shall\" and \"shall not\" are confined to the
context of normative provisions, and do not appear in Technical Reports.

The constructions \"must\" and \"must not\" are not used as substitutes
for \"shall\" and \"shall not\". Their use is avoided insofar as
possible, and they are not used in a normative context except in a
direct citation from an external, referenced, non-3GPP document, or so
as to maintain continuity of style when extending or modifying the
provisions of such a referenced document.

**should** indicates a recommendation to do something

**should not** indicates a recommendation not to do something

**may** indicates permission to do something

**need not** indicates permission not to do something

The construction \"may not\" is ambiguous and is not used in normative
elements. The unambiguous constructions \"might not\" or \"shall not\"
are used instead, depending upon the meaning intended.

**can** indicates that something is possible

**cannot** indicates that something is impossible

The constructions \"can\" and \"cannot\" are not substitutes for \"may\"
and \"need not\".

**will** indicates that something is certain or expected to happen as a
result of action taken by an agency the behaviour of which is outside
the scope of the present document

**will not** indicates that something is certain or expected not to
happen as a result of action taken by an agency the behaviour of which
is outside the scope of the present document

**might** indicates a likelihood that something will happen as a result
of action taken by some agency the behaviour of which is outside the
scope of the present document

**might not** indicates a likelihood that something will not happen as a
result of action taken by some agency the behaviour of which is outside
the scope of the present document

In addition:

**is** (or any other verb in the indicative mood) indicates a statement
of fact

**is not** (or any other negative verb in the indicative mood) indicates
a statement of fact

The constructions \"is\" and \"is not\" do not indicate requirements.

Introduction
============

The present document is part of a TS-family covering the 3rd Generation
Partnership Project Technical Specification Group Services and System
Aspects Management and orchestration of networks, as identified below:

> 3GPP TS 28.540: Management and orchestration of 5G networks; Network
> Resource Model (NRM); Stage 1.
>
> **3GPP TS 28.541: Management and orchestration of 5G networks; Network
> Resource Model (NRM); Stage 2 and stage 3.**

 1 Scope
=======

The present document specifies the Information Model and Solution Set
for the Network Resource Model (NRM) definitions of NR, NG-RAN, 5G Core
Network (5GC) and network slice, to fulfil the requirements identified
in 3GPP TS 28.540 \[10\].

The Information Model defines the semantics and behaviour of information
object class attributes and relations visible on the management
interfaces in a protocol and technology neutral way. And Solution Set
defines one or more solution set(s) with specific protocol(s) according
to the Information Model definitions.

2 References
============

The following documents contain provisions which, through reference in
this text, constitute provisions of the present document.

\- References are either specific (identified by date of publication,
edition number, version number, etc.) or non‑specific.

\- For a specific reference, subsequent revisions do not apply.

\- For a non-specific reference, the latest version applies. In the case
of a reference to a 3GPP document (including a GSM document), a
non-specific reference implicitly refers to the latest version of that
document *in the same Release as the present document*.

\[1\] 3GPP TR 21.905: \"Vocabulary for 3GPP Specifications\".

\[2\] 3GPP TS 23.501: \"System Architecture for the 5G System\".

\[3\] 3GPP TS 38.300: \"NR; Overall description; Stage-2\".

\[4\] 3GPP TS 38.401: \"NG-RAN; Architecture description\".

\[5\] 3GPP TS 38.413: \"NG-RAN; NG Application Protocol (NGAP)\".

\[6\] 3GPP TS 38.420: \"NG-RAN; Xn general aspects and principles\".

\[7\] 3GPP TS 38.470: \"NG-RAN; F1 general aspects and principles\".

\[8\] 3GPP TS 38.473: \"NG-RAN; F1 application protocol (F1AP)\".

\[9\] 3GPP TS 37.340: \"NR; Multi-connectivity; Overall description;
Stage 2\".

\[10\] 3GPP TS 28.540: \"Management and orchestration; 5G Network
Resource Model (NRM);Stage 1\".

\[11\] 3GPP TS 28.662: \"Telecommunication management; Generic Radio
Access Network (RAN) Network Resource Model (NRM) Integration Reference
Point (IRP); Information Service (IS) \".

\[12\] 3GPP TS 38.104: \"NR; Base Station (BS) radio transmission and
reception\".

\[13\] 3GPP TS 23.003: \"Numbering, Addressing and Identification\".

\[14\] 3GPP TS 36.410: \"Evolved Universal Terrestrial Radio Access
Network (E-UTRAN); S1 general aspects and principles\".

\[15\] 3GPP TS 36.423: \"Evolved Universal Terrestrial Radio Access
Network (E-UTRAN); X2 application protocol\".

\[16\] 3GPP TS 36.425: \"Evolved Universal Terrestrial Radio Access
Network (E-UTRAN); X2 interface user plane protocol\".

\[17\] 3GPP TS 28.625: \"State Management Data Definition Integration
Reference Point (IRP); Information Service (IS)\".

\[18\] Recommendation ITU-T X.731: \"Information technology - Open
Systems Interconnection - Systems Management: State management
function\".

\[19\] 3GPP TS 28.658: \"Telecommunications management; Evolved
Universal Terrestrial Radio Access Network (E-UTRAN) Network Resource
Model (NRM) Integration Reference Point (IRP): Information Service
(IS)\".

\[20\] 3GPP TS 28.702: \"Core Network (CN) Network Resource Model (NRM)
Integration Reference Point (IRP); Information Service (IS)\".

\[21\] 3GPP TS 28.708: \"**Telecommunication management; Evolved Packet
Core (EPC) Network Resource Model (NRM) Integration Reference Point
(IRP): Information Service (IS)\".**

\[22\] 3GPP TS 23.040: \"Technical realization of the Short Message
Service (SMS)\".

\[23\] 3GPP TS 29.510: \"5G system; Network Function Repository
Services; Stage 3\".

\[24\] 3GPP TS 29.531: \"5G System; Network Slice Selection Services
Stage 3\".

\[25\] Void.

\[26\] 3GPP TS 28.531: \"Management and orchestration; Provisioning\".

\[27\] 3GPP TS 28.554: \"Management and orchestration; 5G End to end Key
Performance Indicators (KPI)\".

\[28\] 3GPP TS 22.261: \"Service requirements for next generation new
services and markets\".

\[29\] ETSI GS NFV-IFA 013 (V2.4.1) (2018-02) \"Network Function
Virtualisation (NFV); Management and Orchestration; Os-Ma-nfvo Reference
Point - Interface and Information Model Specification\".

\[30\] 3GPP TS 28.622: \"Telecommunication management; Generic Network
Resource Model (NRM) Integration Reference Point (IRP); Information
Service (IS)\".

\[31\] Void.

\[32\] 3GPP TS 38.211: \"NR; Physical channels and modulation\".

\[33\] 3GPP TS 32.616: \"Telecommunication management; Configuration
Management (CM); Bulk CM Integration Reference Point (IRP); Solution Set
(SS) definitions\".

\[34\] Void .

\[35\] 3GPP TS 28.532: \"Management and orchestration; Management
services\".

\[36\] Void.

\[37\] IETF  RFC 791: \"Internet Protocol\".

\[38\] IETF RFC 2373: \"IP Version 6 Addressing Architecture\".

\[39\] IEEE 802.1Q^TM^: \"Media Access Control Bridges and Virtual
Bridged Local Area Networks\".

\[40\] ETSI GR NFV-IFA 015 (V2.4.1): \"Network Function Virtualisation
(NFV) Release 2; Management and Orchestration; Report on NFV Information
Model\".

\[41\] 3GPP TS 38.213: \"NR; Physical layer procedures for control\".

\[42\] 3GPP TS 38.101-1: \"NR; User Equipment (UE) radio transmission
and reception; Part 1: Range 1 Standalone\".

\[43\] 3GPP TS 32.156: \"Telecommunication management; Fixed Mobile
Convergence (FMC) model repertoire\".

\[44\] IETF RFC 4122: \"A Universally Unique IDentifier (UUID) URN
Namespace\".

\[45\] IETF RFC 8528: \"YANG Schema Mount\".

\[46\] Void

\[47\] 3GPP TS 32.160: \"Management and orchestration; Management
Service Template\".

\[48\] 3GPP TS 38.463: \"NG-RAN; E1 application protocol (E1AP)\".

\[49\] 3GPP TS 38.304: \"NR; User Equipment (UE) procedures in Idle mode
and RRC Inactive state\".

\[50\] GSMA NG.116 - Generic Network Slice Template Version 2.0
(2019-10-16).

\[51\] 3GPP TS 22.104: \"Service requirements for cyber-physical control
applications in vertical domains; Stage 1\".

\[52\] 3GPP TS 33.501: \" Security architecture and procedures for the
5G System\".

\[53\] 3GPP TS 38.901: \"Study on channel model for frequencies from 0.5
to 100 GHz \".

\[54\] 3GPP TS 38.331: \"NR; Radio Resource Control (RRC) protocol
specification\".

\[55\] 3GPP TS 38.215: \"NR; Physical layer measurements\".

\[56\] 3GPP TS 29.244: \"Technical Specification Group Core Network and
Terminals; Interface between the Control Plane and the User Plane Nodes;
Stage 3\".

\[57\] 3GPP TS 28.313: \"Self-Organizing Networks (SON) for 5G
networks\".

\[58\] 3GPP TS 38.423: \"NR; Xn application protocol (XnAP)\".

\[59\] 3GPP TS 23.503: \"Policy and Charging Control Framework for the
5G System; Stage 2\".

\[60\] 3GPP TS 29.512: \"5G System; Session Management Policy Control
Service; Stage 3\".

\[61\] 3GPP TS 29.571: \"5G System; Common Data Types for Service Based
Interfaces; Stage 3\".

\[62\] 3GPP TS 29.214: \"Policy and Charging Control over Rx reference
point\".

\[63\] IETF RFC 7042: \"IANA Considerations and IETF Protocol and
Documentation Usage for IEEE 802 Parameters\".

\[64\] IEEE 802.3-2015^TM^: \"IEEE Standard for Ethernet\".

\[65\] IEEE 802.1Q-2014^TM^: \"Bridges and Bridged Networks\".

\[66\] IETF RFC 4301: \"Security Architecture for the Internet
Protocol\".

\[67\] 3GPP TS 29.514: \"5G System; Policy Authorization Service; Stage
3\".

\[68\] 3GPP TS 32.422: \"Telecommunication management; Subscriber and
equipment trace; Trace control and configuration management\"

\[69\] 3GPP TS 28.530: \"Management and orchestration; Concepts, use
cases and requirements\".

\[70\] 3GPP TS 28.310: \"Management and orchestration; Energy efficiency
of 5G\".

3 Definitions and abbreviations
===============================

3.1 Definitions
---------------

For the purposes of the present document, the terms and definitions
given in 3GPP TR 21.905 \[1\], 3GPP TS 28.540 \[10\] and the following
apply. A term defined in the present document takes precedence over the
definition of the same term, if any, in 3GPP TR 21.905 \[1\] and 3GPP
TS 28.540 \[10\].

3.2 Abbreviations
-----------------

For the purposes of the present document, the abbreviations given in
3GPP TR 21.905 \[1\], 3GPP TS 23.501 \[2\], 3GPP TS 38.401 \[4\], 3GPP
TS 28.540 \[10\] and the following apply. An abbreviation defined in the
present document takes precedence over the definition of the same
abbreviation, if any, in 3GPP TR 21.905 \[1\], 3GPP TS 23.501 \[2\],
3GPP TS 38.401 \[4\] and TS 28.540 \[10\].

BWP Bandwidth Part

CM Configuration Management

DN Distinguished Name

IOC Information Object Class

JSON JavaScript Object Notation

NFV Network Functions Virtualisation

NRM Network Resource Model

NS Network Service

NSI Network Slice Instance

NSSAI Network Slice Selection Assistance Information

NSSI Network Slice Subnet Instance

PNF Physical Network Function

RIM Remote Interference Management

RIM-RS Remote Interference Management Reference Signal

SBA Service Based Architecture

SS Solution Set

TN Transport Network

VNF Virtualised Network Function
