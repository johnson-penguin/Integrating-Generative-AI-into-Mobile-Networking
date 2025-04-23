+----------------------------------+----------------------------------+
| 3GPP TS 36.101 V16.18.0          |                                  |
| (2023-09)                        |                                  |
+==================================+==================================+
| Technical Specification          |                                  |
+----------------------------------+----------------------------------+
| 3rd Generation Partnership       |                                  |
| Project;                         |                                  |
|                                  |                                  |
| Technical Specification Group    |                                  |
| Radio Access Network;            |                                  |
|                                  |                                  |
| Evolved Universal Terrestrial    |                                  |
| Radio Access (E-UTRA);           |                                  |
|                                  |                                  |
| User Equipment (UE) radio        |                                  |
| transmission and reception       |                                  |
|                                  |                                  |
| (Release 16)                     |                                  |
+----------------------------------+----------------------------------+
|                                  |                                  |
+----------------------------------+----------------------------------+
| ![LTE-Adv                        | ![3GPP-logo\_web](media/image2.p |
| ancedPro\_largerTM\_cropped](med | ng){width="1.7708333333333333in" |
| ia/image1.jpeg){width="1.4375in" | height="1.03125in"}              |
| height="1.1458333333333333in"}   |                                  |
+----------------------------------+----------------------------------+
|                                  |                                  |
+----------------------------------+----------------------------------+
| The present document has been    |                                  |
| developed within the 3rd         |                                  |
| Generation Partnership Project   |                                  |
| (3GPP ^TM^) and may be further   |                                  |
| elaborated for the purposes of   |                                  |
| 3GPP.\                           |                                  |
| The present document has not     |                                  |
| been subject to any approval     |                                  |
| process by the 3GPP              |                                  |
| Organizational Partners and      |                                  |
| shall not be implemented.\       |                                  |
| This Specification is provided   |                                  |
| for future development work      |                                  |
| within 3GPP only. The            |                                  |
| Organizational Partners accept   |                                  |
| no liability for any use of this |                                  |
| Specification.\                  |                                  |
| Specifications and Reports for   |                                  |
| implementation of the 3GPP ^TM^  |                                  |
| system should be obtained via    |                                  |
| the 3GPP Organizational          |                                  |
| Partners\' Publications Offices. |                                  |
+----------------------------------+----------------------------------+

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

Foreword 321 Scope 342 References 343 Definitions, symbols and
abbreviations 343.1 Definitions 343.2 Symbols 363.3 Abbreviations 394
General 414.1 Relationship between minimum requirements and test
requirements 414.2 Applicability of minimum requirements 414.3 Void
414.3A Applicability of minimum requirements (CA, UL-MIMO, ProSe, Dual
Connectivity, UE category 0, UE category M1, UE category M2, UE category
1bis, UE category NB1 and NB2, V2X Communication, MBMS UE) 414.4 RF
requirements in later releases 435 Operating bands and channel
arrangement 435.1 General 435.2 Void 435.3 Void 435.4 Void 435.5
Operating bands 435.5A Operating bands for CA 465.5B Operating bands for
UL-MIMO 655.5C Operating bands for Dual Connectivity 655.5D Operating
bands for ProSe 685.5E Operating bands for UE category 0, UE category M1
and M2 and UE category 1bis 695.5F Operating bands for category NB1 and
NB2 695.5G Operating bands for V2X Communication 695.6 Channel bandwidth
705.6.1 Channel bandwidths per operating band 715.6A Channel bandwidth
for CA 745.6A.1 Channel bandwidths per operating band for CA 765.6B
Channel bandwidth for UL-MIMO 1785.6B.1 Void 1785.6C Channel bandwidth
for Dual Connectivity 1785.6C.1 Void 1785.6D Channel bandwidth for ProSe
1785.6D.1 Channel bandwidths per operating band for ProSe 1785.6F
Channel bandwidth for category NB1 and NB2 1795.6G Channel bandwidth for
V2X Communication 1805.6G.1 Channel bandwidths per operating band for
V2X Communication 1805.7 Channel arrangement 1825.7.1 Channel spacing
1825.7.1A Channel spacing for CA 1825.7.1F Channel spacing for category
NB1 and NB2 1835.7.2 Channel raster 1835.7.2A Channel raster for CA
1835.7.2F Channel raster for category NB1 and NB2 1835.7.3 Carrier
frequency and EARFCN 1835.7.3F Carrier frequency and EARFCN for category
NB1 and NB2 1865.7.4 TX--RX frequency separation 1865.7.4A TX--RX
frequency separation for CA 1875.7.4E TX--RX frequency separation for
category M1 and M2 1875.7.4F TX--RX frequency separation for category
NB1 and NB2 1886 Transmitter characteristics 1886.1 General 1886.2
Transmit power 1886.2.1 Void 1886.2.2 UE maximum output power 1886.2.2A
UE maximum output power for CA 1916.2.2B UE maximum output power for
UL-MIMO 1966.2.2C Void 1996.2.2D UE maximum output power for ProSe
1996.2.2E UE maximum output power for Category M1 and M2 UE 1996.2.2F UE
maximum output power for category NB1 and NB2 2006.2.2G UE maximum
output power for V2X Communication 2016.2.3 UE maximum output power for
modulation / channel bandwidth 2036.2.3A UE Maximum Output power for
modulation / channel bandwidth for CA 2046.2.3B UE maximum output power
for modulation / channel bandwidth for UL-MIMO 2096.2.3D UE maximum
output power for modulation / channel bandwidth for ProSe 2096.2.3E UE
maximum output power for modulation / channel bandwidth for category M1
and M2 2106.2.3F UE maximum output power for modulation / channel
bandwidth for category NB1 and NB2 2126.2.3G UE maximum output power for
modulation / channel bandwidth for V2X Communication 2126.2.3G.1 MPR for
Power class 3 V2X UE 2126.2.3G.2 MPR for Power class 2 V2X UE 2146.2.4
UE maximum output power with additional requirements 2146.2.4A UE
maximum output power with additional requirements for CA 2336.2.4A.1
A-MPR for CA\_NS\_01 for CA\_1C 2356.2.4A.2 A-MPR for CA\_NS\_02 for
CA\_1C 2366.2.4A.3 A-MPR for CA\_NS\_03 for CA\_1C 2366.2.4A.4 A-MPR for
CA\_NS\_04 2376.2.4A.5 A-MPR for CA\_NS\_05 for CA\_38C 2406.2.4A.6
A-MPR for CA\_NS\_06 2416.2.4A.7 A-MPR for CA\_NS\_07 2426.2.4A.8 A-MPR
for CA\_NS\_08 2436.2.4A.9 Void 2446.2.4A.10 A-MPR for CA\_NS\_10
2446.2.4B UE maximum output power with additional requirements for
UL-MIMO 2496.2.4D UE maximum output power with additional requirements
for ProSe 2496.2.4E UE maximum output power with additional requirements
for category M1 and M2 UE 2496.2.4F UE maximum output power with
additional requirements for category NB1 and NB2 UE 2586.2.4G UE maximum
output power with additional requirements for V2X Communication 2596.2.5
Configured transmitted power 2616.2.5A Configured transmitted power for
CA 2926.2.5B Configured transmitted power for UL-MIMO 2966.2.5C
Configured transmitted power for Dual Connectivity 2966.2.5D Configured
transmitted power for ProSe 2986.2.5F Configured transmitted Power for
category NB1 and NB2 2996.2.5G Configured transmitted power for V2X
Communication 3006.3 Output power dynamics 3046.3.1 (Void) 3046.3.2
Minimum output power 3046.3.2.1 Minimum requirement 3046.3.2A UE Minimum
output power for CA 3046.3.2A.1 Minimum requirement for CA 3056.3.2B UE
Minimum output power for UL-MIMO 3056.3.2B.1 Minimum requirement
3056.3.2C Void 3056.3.2D UE Minimum output power for ProSe 3056.3.2F UE
Minimum output power for category NB1 and NB2 3066.3.2G UE Minimum
output power for V2X Communication 3066.3.3 Transmit OFF power
3066.3.3.1. Minimum requirement 3066.3.3A UE Transmit OFF power for CA
3076.3.3A.1 Minimum requirement for CA 3076.3.3B UE Transmit OFF power
for UL-MIMO 3076.3.3B.1 Minimum requirement 3076.3.3D Transmit OFF power
for ProSe 3086.3.3F Transmit OFF power for category NB1 and NB2
3086.3.3G Transmit OFF power for V2X Communication 3086.3.4 ON/OFF time
mask 3096.3.4.1 General ON/OFF time mask 3096.3.4.2 PRACH and SRS time
mask 3106.3.4.2.1 PRACH time mask 3106.3.4.2.2 SRS time mask 3116.3.4.3
Slot / Sub frame boundary time mask for subframe TTI 3136.3.4.4 PUCCH /
PUSCH / SRS time mask for subframe TTI 3156.3.4.5 Symbol / Subslot
boundary time mask for subslot TTI 3176.3.4.6 Subslot PUCCH / subslot
PUSCH / SRS time mask for subslot TTI 3186.3.4.7 Symbol / Slot boundary
time mask for slot TTI 3216.3.4.8 Slot PUCCH / slot PUSCH / SRS time
mask for slot TTI 3226.3.4.9 Consecutive subslot and slot TTI or
consecutive subslot and subframe TTI time mask 3226.3.4.10 Consecutive
subframe and subslot TTI or consecutive slot and subslot TTI time mask
3226.3.4.11 Consecutive TTI and slot TTI or consecutive slot TTI and TTI
time mask 3236.3.4A ON/OFF time mask for CA 3246.3.4B ON/OFF time mask
for UL-MIMO 3246.3.4D ON/OFF time mask for ProSe 3246.3.4D.1 General
time mask for ProSe 3246.3.4D.2 PSSS/SSSS time mask 3256.3.4D.3 PSSS /
SSSS / PSBCH time mask 3266.3.4D.4 PSSCH / SRS time mask 3266.3.4F
ON/OFF time mask for category NB1 and NB2 3266.3.4F.1 General ON/OFF
time mask 3266.3.4F.2 NPRACH time mask 3276.3.4G ON/OFF time mask for
V2X Communication 3276.3.4G.1 PSSS / SSSS / PSBCH time mask 3286.3.5
Power Control 3286.3.5.1 Absolute power tolerance 3286.3.5.1.1 Minimum
requirements 3286.3.5.2 Relative Power tolerance 3296.3.5.2.1 Minimum
requirements 3296.3.5.3 Aggregate power control tolerance 3306.3.5.3.1
Minimum requirement 3306.3.5A Power control for CA 3306.3.5A.1 Absolute
power tolerance 3306.3.5A.1.1 Minimum requirements 3306.3.5A.2 Relative
power tolerance 3316.3.5A.2.1 Minimum requirements 3316.3.5A.3 Aggregate
power control tolerance 3316.3.5A.3.1 Minimum requirements 3316.3.5B
Power control for UL-MIMO 3326.3.5D Power Control for ProSe 3326.3.5D.1
Absolute power tolerance 3326.3.5E Power control for category M1 and M2
3326.3.5E.1 Absolute power tolerance 3326.3.5E.2 Relative Power
tolerance 3326.3.5E.3 Aggregate power control tolerance 3336.3.5E.3.1
Minimum requirement 3336.3.5F Power Control for category NB1 and NB2
3336.3.5F.1 Absolute power tolerance 3346.3.5F.2 Relative power
tolerance 3346.3.5F.3 Aggregate power control tolerance for category NB1
and NB2 3356.3.5F.3.1 Minimum requirement 3356.3.5G Power Control for
V2X Communication 3356.3.5G.1 Absolute power tolerance 3356.4 Void
3366.5 Transmit signal quality 3366.5.1 Frequency error 3366.5.1A
Frequency error for CA 3366.5.1B Frequency error for UL-MIMO 3366.5.1D
Frequency error for ProSe 3366.5.1E Frequency error for UE category M1
and M2 3366.5.1F Frequency error for UE category NB1 and NB2 3376.5.1G
Frequency error for V2X Communication 3376.5.2 Transmit modulation
quality 3376.5.2.1 Error Vector Magnitude 3386.5.2.1.1 Minimum
requirement 3386.5.2.2 Carrier leakage 3386.5.2.2.1 Minimum requirements
3396.5.2.3 In-band emissions 3396.5.2.3.1 Minimum requirements
3396.5.2.4 EVM equalizer spectrum flatness 3406.5.2.4.1 Minimum
requirements 3406.5.2A Transmit modulation quality for CA 3416.5.2A.1
Error Vector Magnitude 3426.5.2A.2 Carrier leakage for CA 3426.5.2A.2.1
Minimum requirements 3426.5.2A.3 In-band emissions 3426.5.2A.3.1 Minimum
requirement for CA 3426.5.2B Transmit modulation quality for UL-MIMO
3456.5.2B.1 Error Vector Magnitude 3456.5.2B.2 Carrier leakage
3456.5.2B.3 In-band emissions 3456.5.2B.4 EVM equalizer spectrum
flatness for UL-MIMO 3456.5.2D Transmit modulation quality for ProSe
3456.5.2D.1 Error Vector Magnitude 3456.5.2D.2 Carrier leakage
3466.5.2D.3 In-band emissions 3466.5.2D.4 EVM equalizer spectrum
flatness for ProSe 3466.5.2E Transmit modulation quality for category M1
and M2 3466.5.2E.1 Error Vector Magnitude 3466.5.2E.2 Carrier leakage
3466.5.2E.2.1 Minimum requirements 3466.5.2E.3 In-band emissions
3466.5.2E.3.1 Minimum requirements 3466.5.2F Transmit modulation quality
for Category NB1 and NB2 3486.5.2F.1 Error Vector Magnitude 3486.5.2F.2
Carrier leakage 3486.5.2F.3 In-band emissions 3486.5.2G Transmit
modulation quality for V2X Communication 3496.5.2G.1 Error Vector
Magnitude 3496.5.2G.2 Carrier leakage 3506.5.2G.3 In-band emissions
3506.5.2G.4 EVM equalizer spectrum flatness 3506.6 Output RF spectrum
emissions 3506.6.1 Occupied bandwidth 3506.6.1.1 Additional minimum
requirement for E-UTRA (network signalled value "NS\_29") 3516.6.1A
Occupied bandwidth for CA 3516.6.1B Occupied bandwidth for UL-MIMO
3516.6.1F Occupied bandwidth for category NB1 and NB2 3526.6.1G Occupied
bandwidth for V2X Communication 3526.6.2 Out of band emission 3526.6.2.1
Spectrum emission mask 3526.6.2.1.1 Minimum requirement 3526.6.2.1A
Spectrum emission mask for CA 3536.6.2.2 Additional spectrum emission
mask 3546.6.2.2.1 Minimum requirement (network signalled value
\"NS\_03\", "NS\_11", \"NS\_20\", and "NS\_21") 3546.6.2.2.2 Minimum
requirement (network signalled value \"NS\_04\") 3556.6.2.2.3 Minimum
requirement (network signalled value \"NS\_06\" or "NS\_07")
3556.6.2.2.4 Minimum requirement (network signalled value \"NS\_33\" or
"NS\_34") 3566.6.2.2.5 Minimum requirement (network signalled value
"NS\_27" and "NS\_43") 3566.6.2.2.6 Minimum requirement (network
signalled value \"NS\_28") 3576.6.2.2.7 Minimum requirement (network
signalled value \"NS\_35\") 3576.6.2.2A Additional Spectrum Emission
Mask for CA 3586.6.2.2A.1 Minimum requirement (network signalled value
\"CA\_NS\_04\") 3586.6.2.2A.2 Minimum requirement CA\_66B (network
signalled value \"CA\_NS\_09\") 3586.6.2.2A.3 Minimum requirement
CA\_66C (network signalled value \"CA\_NS\_09\") 3596.6.2.2A.4 Minimum
requirement CA\_48B and CA\_48C (network signalled value \"CA\_NS\_10\")
3596.6.2.3 Adjacent Channel Leakage Ratio 3606.6.2.3.1 Minimum
requirement E-UTRA 3606.6.2.3.1a Additional minimum requirement for
E-UTRA (network signalled value "NS\_29") 3616.6.2.3.1A Void
3626.6.2.3.1Aa Void 3626.6.2.3.2 Minimum requirements UTRA 3626.6.2.3.2A
Minimum requirement UTRA for CA 3636.6.2.3.3A Minimum requirements for
CA E-UTRA 3656.6.2.4 Void 3666.6.2.4.1 Void 3666.6.2A Void 3666.6.2B Out
of band emission for UL-MIMO 3666.6.2C Void 3666.6.2D Out of band
emission for ProSe 3666.6.2F Out of band emission for category NB1 and
NB2 3676.6.2F.1 Spectrum emission mask 3676.6.2F.2 Additional Spectrum
Emission Mask for Category NB1 and NB2 3676.6.2F.2.1 Minimum requirement
(network signalled value \"NS\_02\") 3676.6.2F.2.2 Minimum requirement
(network signalled value \"NS\_03\") 3676.6.2F.3 Adjacent Channel
Leakage Ratio for category NB1 and NB2 3686.6.2G Out of band emission
for V2X Communication 3686.6.3 Spurious emissions 3696.6.3.1 Minimum
requirements 3696.6.3.1A Minimum requirements for CA 3706.6.3.2 Spurious
emission band UE co-existence 3716.6.3.2A Spurious emission band UE
co-existence for CA 3816.6.3.3 Additional spurious emissions
3896.6.3.3.1 Minimum requirement (network signalled value \"NS\_05\")
3906.6.3.3.2 Minimum requirement (network signalled value "NS\_07")
3906.6.3.3.3 Minimum requirement (network signalled value "NS\_08")
3906.6.3.3.4 Minimum requirement (network signalled value "NS\_09")
3906.6.3.3.5 Minimum requirement (network signalled value \"NS\_12\")
3916.6.3.3.6 Minimum requirement (network signalled value "NS\_13")
3916.6.3.3.7 Minimum requirement (network signalled value "NS\_14")
3916.6.3.3.8 Minimum requirement (network signalled value "NS\_15")
3926.6.3.3.9 Minimum requirement (network signalled value "NS\_16")
3926.6.3.3.10 Minimum requirement (network signalled value "NS\_17")
3926.6.3.3.11 Minimum requirement (network signalled value "NS\_18")
3926.6.3.3.12 Minimum requirement (network signalled value "NS\_19")
3936.6.3.3.13 Minimum requirement (network signalled value "NS\_11")
3936.6.3.3.14 Minimum requirement (network signalled value "NS\_20")
3936.6.3.3.15 Minimum requirement (network signalled value "NS\_21")
3946.6.3.3.16 Minimum requirement (network signalled value \"NS\_22\")
3946.6.3.3.17 Minimum requirement (network signalled value "NS\_23")
3946.6.3.3.18 Void 3956.6.3.3.19 Minimum requirement (network signalled
value \"NS\_04\") 3956.6.3.3.20 Minimum requirement (network signalled
value "NS\_24") 3956.6.3.3.21 Minimum requirement (network signalled
value "NS\_25") 3966.6.3.3.22 Minimum requirement (network signalled
value "NS\_26") 3966.6.3.3.23 Minimum requirement (network signalled
value "NS\_27" and "NS\_43") 3966.6.3.3.24 Minimum requirement (network
signalled value "NS\_28") 3966.6.3.3.25 Minimum requirement (network
signalled value "NS\_29") 3976.6.3.3.26 Minimum requirement (network
signalled value "NS\_30") 3976.6.3.3.27 Minimum requirement (network
signalled value "NS\_31") 3986.6.3.3.28 Minimum requirement (network
signalled value "NS\_36") 3996.6.3.3.29 Minimum requirement (network
signalled value "NS\_38") 3996.6.3.3.30 Minimum requirement (network
signalled value "NS\_39") 3996.6.3.3.31 Minimum requirement (network
signalled value "NS\_40" and "NS\_41") 4006.6.3.3.32 Minimum requirement
(network signalled value "NS\_42") 4006.6.3.3.33 Minimum requirement
(network signalled value "NS\_44") 4006.6.3.3.34 Minimum requirement
(network signalled value "NS\_45") 4006.6.3.3.35 Minimum requirement
(network signalled value "NS\_56") 4016.6.3.3A Additional spurious
emissions for CA 4016.6.3.3A.1 Minimum requirement for CA\_1C (network
signalled value \"CA\_NS\_01\") 4026.6.3.3A.2 Minimum requirement for
CA\_1C (network signalled value \"CA\_NS\_02\") 4026.6.3.3A.3 Minimum
requirement for CA\_1C (network signalled value \"CA\_NS\_03\")
4026.6.3.3A.4 Minimum requirement for CA\_38C (network signalled value
\"CA\_NS\_05\") 4036.6.3.3A.5 Minimum requirement for CA\_7C (network
signalled value \"CA\_NS\_06\") 4036.6.3.3A.6 Minimum requirement for
CA\_39C and CA\_39C-41A (network signalled value \"CA\_NS\_07\")
4036.6.3.3A.7 Minimum requirement for CA\_42C (network signalled value
\"CA\_NS\_08\") 4036.6.3.3A.8 Minimum requirement for CA\_41C and
CA\_41D (network signalled value \"CA\_NS\_04\") 4046.6.3.3A.9 Void
4046.6.3.3A.10 Minimum requirement for CA\_48B and CA\_48C (network
signalled value \"CA\_NS\_10\") 4046.6.3A Void 4046.6.3B Spurious
emission for UL-MIMO 4056.6.3C Void 4056.6.3D Spurious emission for
ProSe 4056.6.3F Spurious emission for category NB1 and NB2 4056.6.3G
Spurious emission for V2X Communication 4056.6A Void 4096.6B Void 4096.7
Transmit intermodulation 4096.7.1 Minimum requirement 4096.7.1A Minimum
requirement for CA 4106.7.1B Minimum requirement for UL-MIMO 4106.7.1F
Minimum requirement for category NB1 and NB2 4116.7.1G Minimum
requirement for V2X Communication 4116.8 Void 4116.8A Void 4116.8B Time
alignment error for UL-MIMO 4116.8B.1 Minimum Requirements 4116.8C Void
4126.8D Void 4126.8E Void 4126.8F Void 4126.8G Time alignment error 4127
Receiver characteristics 4127.1 General 4127.2 Diversity characteristics
4137.3 Reference sensitivity power level 4137.3.1 Minimum requirements
(QPSK) 4137.3.1A Minimum requirements (QPSK) for CA 4487.3.1B Minimum
requirements (QPSK) for UL-MIMO 5487.3.1D Minimum requirements (QPSK)
for ProSe 5487.3.1E Minimum requirements (QPSK) for UE category 0, M1,
M2 and 1bis 5507.3.1F Minimum requirements for UE category NB1 and NB2
5597.3.1F.1 Reference sensitivity for UE category NB1 and NB2
5597.3.1F.2 Void 5607.3.1G Minimum requirements (QPSK) for V2X 5607.3.2
Void 5627.4 Maximum input level 5627.4.1 Minimum requirements 5637.4.1A
Minimum requirements for CA 5637.4.1B Minimum requirements for UL-MIMO
5647.4.1D Minimum requirements for ProSe 5647.4.1F Minimum requirements
for category NB1 and NB2 5657.4.1G Minimum requirements for V2X 5657.4A
Void 5667.4A.1 Void 5667.5 Adjacent Channel Selectivity (ACS) 5667.5.1
Minimum requirements 5667.5.1A Minimum requirements for CA 5677.5.1B
Minimum requirements for UL-MIMO 5717.5.1D Minimum requirements for
ProSe 5717.5.1F Minimum requirements for category NB1 and NB2 5727.5.1G
Minimum requirements for V2X 5737.6 Blocking characteristics 5757.6.1
In-band blocking 5757.6.1.1 Minimum requirements 5757.6.1.1A Minimum
requirements for CA 5777.6.1.1D Minimum requirements for ProSe
5807.6.1.1F Minimum requirements for category NB1 and NB2 5817.6.1.1G
Minimum requirements for V2X 5817.6.2 Out-of-band blocking 5837.6.2.1
Minimum requirements 5837.6.2.1A Minimum requirements for CA 5857.6.2.1D
Minimum requirements for ProSe 5887.6.2.1F Minimum requirements for
category NB1 and NB2 5887.6.2.1G Minimum requirements for V2X 5897.6.3
Narrow band blocking 5907.6.3.1 Minimum requirements 5907.6.3.1A Minimum
requirements for CA 5917.6.3.1D Minimum requirements for ProSe 5927.6A
Void 5937.6B Blocking characteristics for UL-MIMO 5937.7 Spurious
response 5937.7.1 Minimum requirements 5937.7.1A Minimum requirements
for CA 5947.7.1B Minimum requirements for UL-MIMO 5957.7.1D Minimum
requirements for ProSe 5957.7.1F Minimum requirements for UE category
NB1 and NB2 5967.7.1G Minimum requirements for V2X 5967.8
Intermodulation characteristics 5977.8.1 Wide band intermodulation
5977.8.1.1 Minimum requirements 5977.8.1A Minimum requirements for CA
5987.8.1B Minimum requirements for UL-MIMO 6017.8.1D Minimum
requirements for ProSe 6017.8.1F Minimum requirements for category NB1
and NB2 6027.8.1G Minimum requirements 6027.8.2 Void 6037.9 Spurious
emissions 6037.9.1 Minimum requirements 6047.9.1A Minimum requirements
6047.10 Receiver image 6057.10.1 Void 6057.10.1A Minimum requirements
for CA 6057.10.1G Minimum requirements for V2X Communication 6058
Performance requirement 6128.1 General 6128.1.1 Receiver antenna
capability 6128.1.1.1 Simultaneous unicast and MBMS operations
6138.1.1.2 Dual-antenna receiver capability in idle mode 6138.1.2
Applicability of requirements 6138.1.2.1 Applicability of requirements
for different channel bandwidths 6138.1.2.2 Definition of CA capability
6138.1.2.2A Definition of dual connectivity capability 6188.1.2.3
Applicability and test rules for different CA configurations and
bandwidth combination sets 6198.1.2.3A Applicability and test rules for
different dual connectivity configuration and bandwidth combination set
6218.1.2.3B Applicability and test rules for different TDD-FDD CA
configurations and bandwidth combination sets 6228.1.2.3C Applicability
and test rules for SDR tests for 4Rx capable UEs 6248.1.2.3D
Applicability and test rules for different CA with LAA SCell(s)
configurations and bandwidth combination sets 6248.1.2.3E Applicability
and test rules for SDR tests for 8Rx capable UEs 6258.1.2.4 Test
coverage for different number of component carriers 6268.1.2.5
Applicability of performance requirements for Type B receiver 6278.1.2.6
Applicability of performance requirements for 4Rx capable UEs
6278.1.2.6.1 Applicability rule and antenna connection for single
carrier tests with 2Rx 6278.1.2.6.2 Applicability rule and antenna
connection for CA and DC tests with 2Rx 6298.1.2.6.3 Applicability rule
and antenna connection for single carrier tests with 4Rx 6298.1.2.6.4
Applicability rule for 256QAM tests 6308.1.2.6.5 Applicability rule and
antenna connection for CA and DC tests with 4Rx 6308.1.2.6.6
Applicability rule for Type C with 4Rx 6348.1.2.6.7 Applicability rule
for 1024QAM tests 6348.1.2.7 Applicability of Enhanced Downlink Control
Channel Performance Requirements 6348.1.2.8 Applicability of performance
requirements for CDM-multiplexed DM RS with interfering simultaneous
transmission (FRC) with multiple CSI-RS configurations 6368.1.2.8A
Applicability of performance requirements for UE supporting coverage
enhancement 6368.1.2.9 Applicability of SDR requirements for CA and LAA
6378.1.2.10 Applicability of performance requirements for Multi-user
Superposed Transmission 6388.1.2.11 Applicability CRS interference
mitigation receivers performance requirements 6388.1.2.12 Applicability
of performance requirements for 8Rx capable UEs 6398.1.2.12.1
Applicability rule and antenna connection for single carrier PDSCH tests
6398.1.2.12.2 Applicability rule and antenna connection for control
channel tests 6458.1.2.12.3 Applicability rule and antenna connection
for CA and DC tests 6458.1.3 UE category and UE DL category 6468.2
Demodulation of PDSCH (Cell-Specific Reference Symbols) 6468.2.1 FDD
(Fixed Reference Channel) 6468.2.1.1 Single-antenna port performance
6478.2.1.1.1 Minimum Requirement 6478.2.1.1.2 Void 6538.2.1.1.3 Void
6538.2.1.1.4 Minimum Requirement 1 PRB allocation in presence of MBSFN
6538.2.1.1.4A Minimum Requirement 1 PRB allocation in presence of FeMBMS
Unicast-mixed Cell under CA 6538.2.1.2 Transmit diversity performance
6548.2.1.2.1 Minimum Requirement 2 Tx Antenna Port 6548.2.1.2.2 Minimum
Requirement 4 Tx Antenna Port 6558.2.1.2.3 Minimum Requirement 2 Tx
Antenna Port (demodulation subframe overlaps with aggressor cell ABS)
6558.2.1.2.3A Minimum Requirement 2 Tx Antenna Ports (demodulation
subframe overlaps with aggressor cell ABS and CRS assistance information
are configured) 6578.2.1.2.4 Enhanced Performance Requirement Type A - 2
Tx Antenna Ports with TM3 interference model 6598.2.1.2.5 Enhanced
Performance Requirement Type B - 2 Tx Antenna Ports with TM2
interference model 6618.2.1.2.6 Enhanced Performance Requirement Type B
- 2 Tx Antenna Ports with TM9 interference model 6628.2.1.2.7 Minimum
Requirement 2 Tx Antenna Port (Superposed transmission) 6638.2.1.3
Open-loop spatial multiplexing performance 6638.2.1.3.1 Minimum
Requirement 2 Tx Antenna Port 6638.2.1.3.1A Soft buffer management test
6678.2.1.3.1B Enhanced Performance Requirement Type C --2Tx Antenna
Ports 6688.2.1.3.1C Enhanced Performance Requirement Type C - 2 Tx
Antenna Ports with TM1 interference 6698.2.1.3.2 Minimum Requirement 4
Tx Antenna Port 6708.2.1.3.3 Minimum Requirement 2 Tx Antenna Port
(demodulation subframe overlaps with aggressor cell ABS) 6708.2.1.3.4
Minimum Requirement 2 Tx Antenna Port (demodulation subframe overlaps
with aggressor cell ABS and CRS assistance information are configured)
6748.2.1.3.5 Minimum Requirement 2 Tx Antenna Port (Superposed
transmission) 6768.2.1.3.6 Minimum Requirement 2 Tx Antenna Port
(network-based CRS interference mitigation) 6778.2.1.4 Closed-loop
spatial multiplexing performance 6788.2.1.4.1 Minimum Requirement
Single-Layer Spatial Multiplexing 2 Tx Antenna Port 6788.2.1.4.1A
Minimum Requirement Single-Layer Spatial Multiplexing 4 Tx Antenna Port
6798.2.1.4.1B Enhanced Performance Requirement Type A - Single-Layer
Spatial Multiplexing 2 Tx Antenna Port with TM4 interference model
6798.2.1.4.1C Minimum Requirement Single-Layer Spatial Multiplexing 2 Tx
Antenna Ports (demodulation subframe overlaps with aggressor cell ABS
and CRS assistance information are configured) 6818.2.1.4.1D Enhanced
Performance Requirement Type B - Single-layer Spatial Multiplexing 2 Tx
Antenna Port with TM4 interference model 6848.2.1.4.1E Minimum
Requirement Single-Layer Spatial Multiplexing 2 Tx Antenna Ports with
CRS assistance information 6868.2.1.4.1F Minimum Requirement
Single-Layer Spatial Multiplexing 4 Tx Antenna Ports with CRS assistance
information 6878.2.1.4.2 Minimum Requirement Multi-Layer Spatial
Multiplexing 2 Tx Antenna Port 6888.2.1.4.2A Enhanced Performance
Requirement Type C -- Multi-layer Spatial Multiplexing 2Tx Antenna Ports
6898.2.1.4.3 Minimum Requirement Multi-Layer Spatial Multiplexing 4 Tx
Antenna Port 6898.2.1.4.3A Minimum Requirement Multi-Layer Spatial
Multiplexing 4 Tx Antenna Port for dual connectivity 6948.2.1.4.4
Minimum Requirement Multi-Layer Spatial Multiplexing 2 Tx Antenna Port
(Superposed transmission) 6968.2.1.5 MU-MIMO 6978.2.1.6 \[Control
channel performance: D-BCH and PCH\] 6978.2.1.7 Carrier aggregation with
power imbalance 6978.2.1.7.1 Minimum Requirement 6978.2.1.8 Intra-band
non-contiguous carrier aggregation with timing offset 6988.2.1.8.1
Minimum Requirement 6988.2.1.9 HST-SFN performance 6998.2.1.9.1 Minimum
Requirement 6998.2.1.9.2 Minimum Requirement for Rel-16 further enhanced
HST 7028.2.1.10 Intra-band contiguous carrier aggregation with minimum
channel spacing 7028.2.1.10.1 Minimum Requirement 7038.2.2 TDD (Fixed
Reference Channel) 7038.2.2.1 Single-antenna port performance
7048.2.2.1.1 Minimum Requirement 7048.2.2.1.2 Void 7098.2.2.1.3 Void
7098.2.2.1.4 Minimum Requirement 1 PRB allocation in presence of MBSFN
7098.2.2.2 Transmit diversity performance 7098.2.2.2.1 Minimum
Requirement 2 Tx Antenna Port 7098.2.2.2.2 Minimum Requirement 4 Tx
Antenna Port 7108.2.2.2.3 Minimum Requirement 2 Tx Antenna Port
(demodulation subframe overlaps with aggressor cell ABS) 7118.2.2.2.3A
Minimum Requirement 2 Tx Antenna Ports (demodulation subframe overlaps
with aggressor cell ABS and CRS assistance information are configured)
7138.2.2.2.4 Enhanced Performance Requirement Type A -- 2 Tx Antenna
Ports with TM3 interference model 7158.2.2.2.5 Minimum Requirement 2 Tx
Antenna Port (when *EIMTA-MainConfigServCell-r12* is configured)
7178.2.2.2.6 Enhanced Performance Requirement Type B - 2 Tx Antenna
Ports with TM2 interference model 7178.2.2.2.7 Enhanced Performance
Requirement Type B - 2 Tx Antenna Ports with TM9 interference model
7198.2.2.2.8 Minimum Requirement 2 Tx Antenna Port (Superposed
transmission) 7208.2.2.3 Open-loop spatial multiplexing performance
7218.2.2.3.1 Minimum Requirement 2 Tx Antenna Port 7218.2.2.3.1A Soft
buffer management test 7248.2.2.3.1B Enhanced Performance Requirement
Type C - 2Tx Antenna Ports 7248.2.2.3.1C Enhanced Performance
Requirement Type C - 2 Tx Antenna Ports with TM1 interference
7258.2.2.3.2 Minimum Requirement 4 Tx Antenna Port 7268.2.2.3.3 Minimum
Requirement 2Tx antenna port (demodulation subframe overlaps with
aggressor cell ABS) 7278.2.2.3.4 Minimum Requirement 2 Tx Antenna Port
(demodulation subframe overlaps with aggressor cell ABS and CRS
assistance information are configured) 7318.2.2.3.5 Minimum Requirement
2 Tx Antenna Port (Superposed transmission) 7338.2.2.3.6 Minimum
Requirement 2 Tx Antenna Port (network-based CRS interference
mitigation) 7348.2.2.4 Closed-loop spatial multiplexing performance
7358.2.2.4.1 Minimum Requirement Single-Layer Spatial Multiplexing 2 Tx
Antenna Port 7358.2.2.4.1A Minimum Requirement Single-Layer Spatial
Multiplexing 4 Tx Antenna Port 7368.2.2.4.1B Enhanced Performance
Requirement Type A -- Single-Layer Spatial Multiplexing 2 Tx Antenna
Port with TM4 interference model 7368.2.2.4.1C Minimum Requirement
Single-Layer Spatial Multiplexing 2 Tx Antenna Ports (demodulation
subframe overlaps with aggressor cell ABS and CRS assistance information
are configured) 7388.2.2.4.1D Enhanced Performance Requirement Type B -
Single-layer Spatial Multiplexing 2 Tx Antenna Port with TM4
interference model 7408.2.2.4.1E Minimum Requirement Single-Layer
Spatial Multiplexing 2 Tx Antenna Ports with CRS assistance information
7428.2.2.4.1F Minimum Requirement Single-Layer Spatial Multiplexing 4 Tx
Antenna Ports with CRS assistance information 7438.2.2.4.2 Minimum
Requirement Multi-Layer Spatial Multiplexing 2 Tx Antenna Port
7458.2.2.4.2A Enhanced Performance Requirement Type C Multi-Layer
Spatial Multiplexing 2 Tx Antenna Port 7458.2.2.4.3 Minimum Requirement
Multi-Layer Spatial Multiplexing 4 Tx Antenna Port 7468.2.2.4.3A Minimum
Requirement Multi-Layer Spatial Multiplexing 4 Tx Antenna Port for dual
connectivity 7508.2.2.4.4 Void 7518.2.2.4.5 Minimum Requirement
Multi-Layer Spatial Multiplexing 2 Tx Antenna Port (Superposed
transmission) 7518.2.2.5 MU-MIMO 7528.2.2.6 \[Control channel
performance: D-BCH and PCH\] 7528.2.2.7 Carrier aggregation with power
imbalance 7528.2.2.7.1 Minimum Requirement 7528.2.2.8 Intra-band
contiguous carrier aggregation with minimum channel spacing 7538.2.2.8.1
Minimum Requirement 7538.2.2.9 HST-SFN performance 7548.2.2.9.1 Minimum
Requirement 7548.2.2.9.2 Minimum Requirement for Rel-16 further enhanced
HST 7568.2.3 TDD FDD CA (Fixed Reference Channel) 7578.2.3.1
Single-antenna port performance 7588.2.3.1.1 Minimum Requirement for FDD
PCell 7588.2.3.1.2 Minimum Requirement for TDD PCell 7628.2.3.2
Open-loop spatial multiplexing performance 2Tx Antenna port 7668.2.3.2.1
Minimum Requirement for FDD PCell 7668.2.3.2.1A Soft buffer management
test for FDD PCell 7708.2.3.2.2 Minimum Requirement for TDD PCell
7718.2.3.2.2A Soft buffer management test for TDD PCell 7758.2.3.3
Closed-loop spatial multiplexing performance 4Tx Antenna Port
7768.2.3.3.1 Minimum Requirement for FDD PCell 7768.2.3.3.2 Minimum
Requirement for TDD PCell 7808.2.3.4 Minimum Requirement for Closed-loop
spatial multiplexing performance 4Tx Antenna Port for dual connectivity
7848.2.3.5 HST-SFN performance 7868.2.3.5.0 General 7868.2.3.5.1 Minimum
Requirement for FDD PCell 7868.2.3.5.2 Minimum Requirement for TDD PCell
7898.2.4 LAA 7928.2.4.1 Closed-loop spatial multiplexing performance 4Tx
Antenna Port 7928.2.4.1.1 FDD PCell (FDD single carrier) 7928.2.4.1.2
TDD PCell (TDD single carrier) 7968.3 Demodulation of PDSCH
(User-Specific Reference Symbols) 7998.3.1 FDD 7998.3.1.1 Single-layer
Spatial Multiplexing 8008.3.1.1A Enhanced Performance Requirement Type A
-- Single-layer Spatial Multiplexing with TM9 interference model
8028.3.1.1B Single-layer Spatial Multiplexing (demodulation subframe
overlaps with aggressor cell ABS and CRS assistance information are
configured) 8058.3.1.1C Enhanced Performance Requirement Type B --
Single-layer Spatial Multiplexing with TM9 interference model
8088.3.1.1D Enhanced Performance Requirement Type B -- Single-layer
Spatial Multiplexing with CRS interference model 8108.3.1.1E Enhanced
Performance Requirement Type B -- Single-layer Spatial Multiplexing with
TM3 interference model 8118.3.1.1F Enhanced Performance Requirement Type
B -- Single-layer Spatial Multiplexing with TM10 serving cell
configuration and TM9 interference model 8128.3.1.1G Single-layer
Spatial Multiplexing (CRS assistance information is configured)
8148.3.1.1H Single-layer Spatial Multiplexing (With Enhanced DMRS table
configured) 8168.3.1.1I Single-layer Spatial Multiplexing (with
assistance information for simultaneous transmition interfering PDSCH)
8188.3.1.2 Dual-Layer Spatial Multiplexing 8198.3.1.2A Enhanced
Performance Requirement Type C - Dual-Layer Spatial Multiplexing
8208.3.1.3 Performance requirements for DCI format 2D and non Quasi
Co-located Antenna Ports 8218.3.1.3.1 Minimum requirement with Same Cell
ID (with single NZP CSI-RS resource) 8218.3.1.3.2 Minimum requirements
with Same Cell ID (with multiple NZP CSI-RS resources) 8238.3.1.3.3
Minimum requirement with Different Cell ID and Colliding CRS (with
single NZP CSI-RS resource) 8258.3.1.3.4 Minimum requirement with
Different Cell ID and non-colliding CRS (with single NZP CSI-RS resource
and CRS assistance information is configured) 8278.3.1.3.5 Minimum
requirements with different Cell ID and non-colliding CRS (with multiple
NZP CSI-RS resources and CRS assistance information is configured)
8298.3.1.3.6 Minimum requirements for QCL Type C and 2 Layers Spatial
Multiplexing 8328.3.1.4 Performance Requirements for semiOpenLoop
transmission 8348.3.2 TDD 8368.3.2.1 Single-layer Spatial Multiplexing
8368.3.2.1A Single-layer Spatial Multiplexing (with multiple CSI-RS
configurations) 8388.3.2.1B Enhanced Performance Requirement Type A --
Single-layer Spatial Multiplexing with TM9 interference model
8408.3.2.1C Single-layer Spatial Multiplexing (demodulation subframe
overlaps with aggressor cell ABS and CRS assistance information are
configured) 8438.3.2.1D Enhanced Performance Requirement Type B --
Single-layer Spatial Multiplexing with TM9 interference 8468.3.2.1E
Enhanced Performance Requirement Type B -- Single-layer Spatial
Multiplexing with CRS interference model 8488.3.2.1F Enhanced
Performance Requirement Type B -- Single-layer Spatial Multiplexing with
TM3 interference 8508.3.2.1G Enhanced Performance Requirement Type B --
Single-layer Spatial Multiplexing with TM10 serving cell configuration
and TM9 interference model 8518.3.2.1H Single-layer Spatial Multiplexing
(CRS assistance information is configured) 8538.3.2.1I Single-layer
Spatial Multiplexing (With Enhanced DMRS table configured) 8558.3.2.1J
Single-layer Spatial Multiplexing (with assistance information for
simultaneous transmition interfering PDSCH) 8568.3.2.2 Dual-Layer
Spatial Multiplexing 8588.3.2.2A Enhanced Performance Requirement Type C
- Dual-Layer Spatial Multiplexing 8588.3.2.3 Dual-Layer Spatial
Multiplexing (with multiple CSI-RS configurations) 8598.3.2.4
Performance requirements for DCI format 2D and non Quasi Co-located
Antenna Ports 8608.3.2.4.1 Minimum requirement with Same Cell ID (with
single NZP CSI-RS resource) 8608.3.2.4.2 Minimum requirements with Same
Cell ID (with multiple NZP CSI-RS resources) 8628.3.2.4.3 Minimum
requirement with Different Cell ID and Colliding CRS (with single NZP
CSI-RS resource) 8648.3.2.4.4 Minimum requirement with Different Cell ID
and non-Colliding CRS (with single NZP CSI-RS resource and CRS
assistance information is configured) 8668.3.2.4.5 Minimum requirements
with different Cell ID and non-colliding CRS (with multiple NZP CSI-RS
resources and CRS assistance information is configured) 8688.3.2.4.6
Minimum requirements for QCL Type C and 2 Layers Spatial Multiplexing
8718.3.2.5 Performance Requirements for semiOpenLoop transmission
8738.3.3 LAA 8758.3.3.1 Dual-Layer Spatial Multiplexing with DM-RS
8758.3.3.1.1 FDD PCell (FDD single carrier) 8758.3.3.1.2 TDD Pcell (TDD
single carrier) 8808.4 Demodulation of PDCCH/PCFICH 8848.4.1 FDD
8848.4.1.1 Single-antenna port performance 8858.4.1.2 Transmit diversity
performance 8858.4.1.2.1 Minimum Requirement 2 Tx Antenna Port
8858.4.1.2.2 Minimum Requirement 4 Tx Antenna Port 8858.4.1.2.3 Minimum
Requirement 2 Tx Antenna Port (demodulation subframe overlaps with
aggressor cell ABS) 8868.4.1.2.4 Minimum Requirement 2 Tx Antenna Port
(demodulation subframe overlaps with aggressor cell ABS and CRS
assistance information are configured) 8918.4.1.2.5 Enhanced Downlink
Control Channel Performance Requirement Type A - 2 Tx Antenna Port under
Asynchronous Network 8978.4.1.2.6 Enhanced Downlink Control Channel
Performance Requirement Type A - 2 Tx Antenna Port with Non-Colliding
CRS Dominant Interferer 8988.4.1.2.7 Enhanced Downlink Control Channel
Performance Requirement Type B - 2 Tx Antenna Port with Colliding CRS
Dominant Interferer 8998.4.1.2.8 Enhanced Downlink Control Channel
Performance Requirement Type B - 2 Tx Antenna Port with Non-Colliding
CRS Dominant Interferer 9008.4.1.2.9 Enhanced Downlink Control Channel
Performance Requirement Type A - 4 Tx Antenna Port with Non-Colliding
CRS Dominant Interferer 9018.4.2 TDD 9028.4.2.1 Single-antenna port
performance 9038.4.2.2 Transmit diversity performance 9038.4.2.2.1
Minimum Requirement 2 Tx Antenna Port 9038.4.2.2.2 Minimum Requirement 4
Tx Antenna Port 9048.4.2.2.3 Minimum Requirement 2 Tx Antenna Port
(demodulation subframe overlaps with aggressor cell ABS) 9048.4.2.2.4
Minimum Requirement 2 Tx Antenna Port (demodulation subframe overlaps
with aggressor cell ABS and CRS assistance information are configured)
9088.4.2.2.5 Enhanced Downlink Control Channel Performance Requirement
Type A - 2 Tx Antenna Port with Colliding CRS Dominant Interferer
9128.4.2.2.6 Enhanced Downlink Control Channel Performance Requirement
Type A - 2 Tx Antenna Port with Non-Colliding CRS Dominant Interferer
9138.4.2.2.7 Enhanced Downlink Control Channel Performance Requirement
Type B - 2 Tx Antenna Port with Colliding CRS Dominant Interferer
9148.4.2.2.8 Enhanced Downlink Control Channel Performance Requirement
Type B - 2 Tx Antenna Port with Non-Colliding CRS Dominant Interferer
9158.4.2.2.9 Enhanced Downlink Control Channel Performance Requirement
Type A - 4 Tx Antenna Port with Non-Colliding CRS Dominant Interferer
9168.4.3 LAA 9178.4.3.1 Transmit diversity performance 9178.4.3.1.1 FDD
Pcell (FDD single carrier) 9178.4.3.1.2 TDD Pcell (TDD single carrier)
9188.5 Demodulation of PHICH 9198.5.1 FDD 9208.5.1.1 Single-antenna port
performance 9208.5.1.2 Transmit diversity performance 9208.5.1.2.1
Minimum Requirement 2 Tx Antenna Port 9208.5.1.2.2 Minimum Requirement 4
Tx Antenna Port 9218.5.1.2.3 Minimum Requirement 2 Tx Antenna Port
(demodulation subframe overlaps with aggressor cell ABS) 9218.5.1.2.4
Minimum Requirement 2 Tx Antenna Port (demodulation subframe overlaps
with aggressor cell ABS and CRS assistance information are configured)
9238.5.1.2.5 Enhanced Downlink Control Channel Performance Requirement
Type A - 2 Tx Antenna Ports under Asynchronous Network 9268.5.1.2.6
Enhanced Downlink Control Channel Performance Requirement Type A - 2 Tx
Antenna Ports with Non-Colliding CRS Dominant Interferer 9278.5.1.2.7
Enhanced Downlink Control Channel Performance Requirement Type B - 2 Tx
Antenna Ports with Colliding CRS Dominant Interferer 9288.5.1.2.8
Enhanced Downlink Control Channel Performance Requirement Type B - 2 Tx
Antenna Ports with Non-Colliding CRS Dominant Interferer 9298.5.2 TDD
9308.5.2.1 Single-antenna port performance 9318.5.2.2 Transmit diversity
performance 9318.5.2.2.1 Minimum Requirement 2 Tx Antenna Port
9318.5.2.2.2 Minimum Requirement 4 Tx Antenna Port 9328.5.2.2.3 Minimum
Requirement 2 Tx Antenna Port (demodulation subframe overlaps with
aggressor cell ABS) 9328.5.2.2.4 Minimum Requirement 2 Tx Antenna Port
(demodulation subframe overlaps with aggressor cell ABS and CRS
assistance information are configured) 9348.5.2.2.5 Enhanced Downlink
Control Channel Performance Requirement Type A - 2 Tx Antenna Ports with
Colliding CRS Dominant Interferer 9368.5.2.2.6 Enhanced Downlink Control
Channel Performance Requirement Type A - 2 Tx Antenna Ports with
Non-Colliding CRS Dominant Interferer 9378.5.2.2.7 Enhanced Downlink
Control Channel Performance Requirement Type B - 2 Tx Antenna Ports with
Colliding CRS Dominant Interferer 9388.5.2.2.8 Enhanced Downlink Control
Channel Performance Requirement Type B - 2 Tx Antenna Ports with
Non-Colliding CRS Dominant Interferer 9398.6 Demodulation of PBCH
9408.6.1 FDD 9408.6.1.1 Single-antenna port performance 9408.6.1.2
Transmit diversity performance 9418.6.1.2.1 Minimum Requirement 2 Tx
Antenna Port 9418.6.1.2.2 Minimum Requirement 4 Tx Antenna Port
9418.6.1.2.3 Minimum Requirement 2 Tx Antenna Port under Time Domain
Measurement Resource Restriction with CRS Assistance Information
9418.6.2 TDD 9438.6.2.1 Single-antenna port performance 9438.6.2.2
Transmit diversity performance 9438.6.2.2.1 Minimum Requirement 2 Tx
Antenna Port 9438.6.2.2.2 Minimum Requirement 4 Tx Antenna Port
9438.6.2.2.3 Minimum Requirement 2 Tx Antenna Port under Time Domain
Measurement Resource Restriction with CRS Assistance Information 9448.7
Sustained downlink data rate provided by lower layers 9458.7.1 FDD
(single carrier and CA) 9458.7.2 TDD (single carrier and CA) 9628.7.3
FDD (EPDCCH scheduling) 9668.7.4 TDD (EPDCCH scheduling) 9688.7.5 TDD
FDD CA 9708.7.5.1 Minimum Requirement FDD PCell 9718.7.5.2 Minimum
Requirement TDD PCell 9798.7.6 FDD (DC) 9888.7.7 TDD (DC) 9958.7.8 TDD
FDD (DC) 9988.7.9 FDD (4 Rx) 10018.7.10 TDD (4 Rx) 10038.7.11 TDD FDD CA
(4 Rx) 10058.7.11.1 Void 10078.7.12 LAA 10078.7.12.1 FDD CA in licensed
bands 10078.7.12.2 TDD CA in licensed bands 10098.7.12.3 TDD-FDD CA in
licensed bands 10118.7.13 FDD DC (4 Rx) 10148.7.14 TDD DC (4 Rx)
10158.7.15 TDD FDD DC (4 Rx) 10178.7.16 FDD (1024QAM and up to 4Rx
supported) 10198.7.17 TDD (1024QAM and up to 4 Rx supported) 10228.7.18
TDD FDD CA (1024QAM and up to 4 Rx supported) 10248.7.19 TDD (8 Rx)
10268.8 Demodulation of EPDCCH 10288.8.1 Distributed Transmission
10288.8.1.1 FDD 10288.8.1.1.1 Void 10298.8.1.2 TDD 10298.8.1.2.1 Void
10308.8.2 Localized Transmission with TM9 10308.8.2.1 FDD 10308.8.2.1.1
Void 10318.8.2.1.2 Void 10328.8.2.2 TDD 10328.8.2.2.1 Void 10338.8.2.2.2
Void 10338.8.3 Localized transmission with TM10 Type B quasi co-location
type 10338.8.3.1 FDD 10338.8.3.2 TDD 10368.8.4 Enhanced Downlink Control
Channel Performance Requirements Type A - Localized Transmission with
CRS Interference Model 10398.8.4.1 FDD 10398.8.4.2 TDD 10408.8.5
Enhanced Downlink Control Channel Performance Requirements Type A -
Distributed Transmission with TM9 Interference Model 10428.8.5.1 TDD
10428.8.6 Enhanced Downlink Control Channel Performance Requirements
Type A - Distributed Transmission with TM3 Interference Model
10438.8.6.1 FDD 10438.9 Demodulation (single receiver antenna) 10448.9.1
PDSCH 10448.9.1.1 FDD and half-duplex FDD (Fixed Reference Channel)
10448.9.1.1.1 Transmit diversity performance (Cell-Specific Reference
Symbols) 10448.9.1.1.2 Closed-loop spatial multiplexing performance
(Cell-Specific Reference Symbols) 10458.9.1.1.3 Closed-loop spatial
multiplexing performance (User-Specific Reference Symbols) 10478.9.1.2
TDD (Fixed Reference Channel) 10508.9.1.2.1 Transmit diversity
performance (Cell-Specific Reference Symbols) 10508.9.1.2.2 Closed-loop
spatial multiplexing performance (Cell-Specific Reference Symbols)
10518.9.1.2.3 Closed-loop spatial multiplexing performance
(User-Specific Reference Symbols) 10548.9.2 PHICH 10568.9.2.1 FDD and
half-duplex FDD 10568.9.2.1.1 Transmit diversity performance 10568.9.2.2
TDD 10568.9.2.2.1 Transmit diversity performance 10568.9.3 PBCH
10578.9.3.1 FDD and half-duplex FDD 10578.9.3.1.1 Transmit diversity
performance 10578.9.3.2 TDD 10578.9.3.2.1 Transmit diversity performance
10578.9.4 PDCCH/PCFICH 10578.9.4.1 FDD and half-duplex FDD 10578.9.4.1.1
Enhanced Downlink Control Channel Performance Requirement Type A - 2 Tx
Antenna Port with Non-Colliding CRS Dominant Interferer 10578.9.4.1.2
Enhanced Downlink Control Channel Performance Requirement Type A - 4 Tx
Antenna Port with Non-Colliding CRS Dominant Interferer 10588.9.4.2 TDD
10598.9.4.2.1 Enhanced Downlink Control Channel Performance Requirement
Type A - 2 Tx Antenna Port with Non-Colliding CRS Dominant Interferer
10598.9.4.2.2 Enhanced Downlink Control Channel Performance Requirement
Type A - 4 Tx Antenna Port with Non-Colliding CRS Dominant Interferer
10608.10 Demodulation (4 receiver antenna ports) 10618.10.1 PDSCH
10618.10.1.1 FDD (Fixed Reference Channel) 10618.10.1.1.1 Transmit
diversity performance with 2Tx Antenna Ports (Cell-Specific Reference
Symbols) 10628.10.1.1.1A Transmit diversity performance wit Enhanced
Performance Requirement Type A - 2 Tx Antenna Ports with TM3
interference model 10638.10.1.1.2 Open-loop spatial multiplexing
performance with 2Tx Antenna Ports (Cell-Specific Reference Symbols)
10648.10.1.1.3 Closed-loop spatial multiplexing Enhanced Performance
Requirements Type A - Single-Layer Spatial Multiplexing 2 Tx Antenna
Port with TM4 interference model (Cell-Specific Reference Symbols)
10648.10.1.1.4 Closed-loop spatial multiplexing performance, Dual-Layer
Spatial Multiplexing 4 Tx Antenna Port (Cell-Specific Reference Symbols)
10658.10.1.1.4A Enhanced Performance Requirement Type C - Dual-Layer
Spatial Multiplexing with 2Tx Antenna Ports 10668.10.1.1.5 Enhanced
Performance Requirement Type A -- Single-layer Spatial Multiplexing with
TM9 interference model (User-Specific Reference Symbols) 10678.10.1.1.5A
Single-layer Spatial Multiplexing (User-Specific Reference Symbols)
10708.10.1.1.5B Single-layer Spatial Multiplexing (With Enhanced DMRS
table configured) 10718.10.1.1.6 Dual-Layer Spatial Multiplexing
(User-Specific Reference Symbols) 10728.10.1.1.6A Enhanced Performance
Requirement Type C - Dual-Layer Spatial Multiplexing 10748.10.1.1.6B
Dual-Layer Spatial Multiplexing with altCQI-Table-1024QAM configured
(User-Specific Reference Symbols) 10758.10.1.1.7 Open-loop spatial
multiplexing, 3 Layer Multiplexing with 4 Tx Antenna Ports
(Cell-Specific Reference Symbols) 10768.10.1.1.7A Enhanced Performance
Requirement Type C - Open-loop spatial multiplexing, 3 Layer
Multiplexing with 4 Tx Antenna Ports (Cell-Specific Reference Symbols)
10768.10.1.1.8 Closed-loop spatial multiplexing performance, 4 Layers
spatial multiplexing 4 Tx antennas (Cell-Specific Reference Symbols)
10778.10.1.1.9 4 Layer Spatial Multiplexing (User-Specific Reference
Symbols) 10778.10.1.1.9A Enhanced Performance Requirement Type C - 4
Layer Spatial Multiplexing (User-Specific Reference Symbols)
10798.10.1.1.10 Closed loop spatial multiplexing performance -
Single-Layer Spatial Multiplexing 2 Tx Antenna Port with CRS assistance
information (Cell-Specific Reference Symbols) 10808.10.1.1.11 Closed
loop spatial multiplexing performance - Single-Layer Spatial
Multiplexing 4 Tx Antenna Port with CRS assistance information
(Cell-Specific Reference Symbols) 10818.10.1.1.12 Closed loop spatial
multiplexing performance - Single-Layer Spatial Multiplexing with CRS
assistance information (User-Specific Reference Symbols) 10828.10.1.1.13
Performance requirements for DCI format 2D and non Quasi Co-located
Antenna Ports 10838.10.1.1.14 HST-SFN performance 10878.10.1.2 TDD
(Fixed Reference Channel) 10878.10.1.2.1 Transmit diversity performance
with 2Tx Antenna Ports (Cell-Specific Reference Symbols) 10888.10.1.2.1A
Transmit diversity performance with Enhanced Performance Requirement
Type A -- 2 Tx Antenna Ports with TM3 interference model 10898.10.1.2.2
Open-loop spatial multiplexing performance with 2Tx Antenna Ports
(Cell-Specific Reference Symbols) 10908.10.1.2.3 Closed-loop spatial
multiplexing Enhanced Performance Requirements Type A - Single-Layer
Spatial Multiplexing 2 Tx Antenna Port with TM4 interference model
(Cell-Specific Reference Symbols) 10908.10.1.2.4 Closed-loop spatial
multiplexing performance, Dual-Layer Spatial Multiplexing 4 Tx Antenna
Ports (Cell-Specific Reference Symbols) 10918.10.1.2.4A Enhanced
Performance Requirement Type C - Dual-Layer Spatial Multiplexing with
2Tx Antenna Ports 10928.10.1.2.5 Enhanced Performance Requirement Type A
-- Single-layer Spatial Multiplexing with TM9 interference model
(User-Specific Reference Symbols) 10938.10.1.2.5A Single-layer Spatial
Multiplexing (with multiple CSI-RS configurations) 10968.10.1.2.5B
Single-layer Spatial Multiplexing (With Enhanced DMRS table configured)
10978.10.1.2.6 Dual-Layer Spatial Multiplexing (User-Specific Reference
Symbols) 10988.10.1.2.6A Enhanced Performance Requirement Type C -
Dual-Layer Spatial Multiplexing 11008.10.1.2.6B Dual-Layer Spatial
Multiplexing with altCQI-Table-1024QAM configured (User-Specific
Reference Symbols) 11018.10.1.2.7 Open-loop spatial multiplexing, 3
Layer Multiplexing with 4 Tx Antenna Ports (Cell-Specific Reference
Symbols) 11028.10.1.2.7A Enhanced Performance Requirement Type C -
Open-loop spatial multiplexing, 3 Layer Multiplexing with 4 Tx Antenna
Ports (Cell-Specific Reference Symbols) 11028.10.1.2.8 Closed-loop
spatial multiplexing performance, 4 Layers spatial multiplexing 4 Tx
antennas 11038.10.1.2.9 4 Layer Spatial Multiplexing (User-Specific
Reference Symbols) 11048.10.1.2.9A Enhanced Performance Requirement Type
C - 4 Layer Spatial Multiplexing (User-Specific Reference Symbols)
11058.10.1.2.10 Closed loop spatial multiplexing performance -
Single-Layer Spatial Multiplexing 2 Tx Antenna Port with CRS assistance
information (Cell-Specific Reference Symbols) 11068.10.1.2.11 Closed
loop spatial multiplexing performance - Single-Layer Spatial
Multiplexing 4 Tx Antenna Port with CRS assistance information
(Cell-Specific Reference Symbols) 11088.10.1.2.12 Closed loop spatial
multiplexing performance - Single-Layer Spatial Multiplexing with CRS
assistance information (User-Specific Reference Symbols) 11098.10.1.2.13
Performance requirements for DCI format 2D and non Quasi Co-located
Antenna Ports 11118.10.1.2.14 HST-SFN performance 11158.10.2
PDCCH/PCFICH 11168.10.2.1 FDD 11168.10.2.1.1 Single-antenna port
performance 11168.10.2.1.2 Transmit diversity performance with 2 Tx
Antenna Ports 11168.10.2.1.3 Transmit diversity performance with 4 Tx
Antenna Ports 11168.10.2.1.4 Enhanced Downlink Control Channel
Performance Requirement Type A - 4 Tx Antenna Port with Non-Colliding
CRS Dominant Interferer 11178.10.2.2 TDD 11188.10.2.2.1 Single-antenna
port performance 11188.10.2.2.2 Transmit diversity performance with 2 Tx
Antenna Ports 11198.10.2.2.3 Transmit diversity performance with 4 Tx
Antenna Ports 11198.10.2.2.4 Enhanced Downlink Control Channel
Performance Requirement Type A - 4 Tx Antenna Port with Non-Colliding
CRS Dominant Interferer 11198.10.3 PHICH 11208.10.3.1 FDD 11208.10.3.1.1
Single Tx Antenna Port performance 11218.10.3.1.2 Transmit diversity
performance with 2 Tx Antenna Ports 11218.10.3.1.3 Transmit diversity
performance with 4 Tx Antenna Ports 11218.10.3.2 TDD 11228.10.3.2.1
Single Tx Antenna Port performance 11228.10.3.2.2 Transmit diversity
performance with 2 Tx Antenna Ports 11238.10.3.2.3 Transmit diversity
performance with 4 Tx Antenna Ports 11238.10.4 ePDCCH 11238.10.4.1
Distributed Transmission with 4Rx 11238.10.4.1.1 FDD 11238.10.4.1.2 TDD
11248.10.4.2 Localized Transmission with TM9 and 4Rx 11258.10.4.2.1 FDD
11258.10.4.2.2 TDD 11268.11 Demodulation (UE supporting coverage
enhancement) 11278.11.1 PDSCH 11288.11.1.1 FDD and half-duplex FDD
(Fixed Reference Channel) 11288.11.1.1.1 Closed-loop spatial
multiplexing performance (Cell-Specific Reference Symbols)
11288.11.1.1.2 Closed-loop spatial multiplexing performance
(User-Specific Reference Symbols) 11328.11.1.1.3 Transmit diversity
performance (Cell-Specific Reference Symbols) 11348.11.1.2 TDD (Fixed
Reference Channel) 11398.11.1.2.1 Closed-loop spatial multiplexing
performance (Cell-Specific Reference Symbols) 11398.11.1.2.2 Closed-loop
spatial multiplexing performance (User-Specific Reference Symbols)
11448.11.1.2.3 Transmit diversity performance (Cell-Specific Reference
Symbols) 11468.11.2 MPDCCH 11508.11.2.1 FDD and half-duplex FDD
11518.11.2.1.1 CE Mode A 11528.11.2.1.2 CE Mode B 11538.11.2.1.3 CE Mode
A with TM9 interference model 11538.11.2.1.4 CE Mode A with CRS
interference model 11558.11.2.1.5 CE Mode A and CE Mode B when
CRS-ChEstMPDCCH-Config is configured 11568.11.2.2.5 CE Mode A and CE
Mode B when CRS-ChEstMPDCCH-Config is configured 11578.11.2.2 TDD
11598.11.2.2.1 CE Mode A 11608.11.2.2.2 CE Mode B 11618.11.2.2.3 CE Mode
A with TM9 interference model 11618.11.2.2.4 CE Mode A with CRS
interference model 11628.11.3 PBCH 11638.11.3.1 FDD and half-duplex FDD
11648.11.3.1.1 Transmit diversity performance 11648.11.3.2 TDD
11658.11.3.2.1 Transmit diversity performance 11658.12 Demodulation of
Narrowband IoT 11658.12.1 NPDSCH 11658.12.1.1.1 Minimum Requirements for
In-band 11668.12.1.1.2 Minimum Requirements for Standalone/Guard-band
11678.12.1.1.3 Minimum Requirements for Standalone for UE Category NB2
11688.12.1.1.4 Minimum Requirements for Standalone for UE with multiple
TBs interleaved transmission 11698.12.1.2 TDD 11708.12.1.2.1 Minimum
Requirements for In-band 11708.12.1.2.2 Minimum Requirements for
Standalone/Guard-band 11718.12.1.2.3 Minimum Requirements for Standalone
for UE Category NB2 11728.12.2 NPDCCH 11728.12.2.1 Half-duplex FDD
11728.12.2.1.1 Single-antenna performance 11738.12.2.1.2 Transmit
diversity performance 11748.12.2.2 TDD 11748.12.2.2.1 Single-antenna
performance 11768.12.2.2.2 Transmit diversity performance 11768.12.3
Demodulation of NPBCH 11768.12.3.1 HD-FDD 11778.12.3.1.1 Single-antenna
port performance with single NPBCH TTI 11778.12.3.1.2 Transmit diversity
performance 11778.12.3.2 TDD 11778.12.3.2.1 Single-antenna port
performance with single NPBCH TTI 11788.12.3.2.2 Transmit diversity
performance 11788.13 Demodulation of PDSCH CA and DC(4 receiver antenna
ports) 11788.13.1 FDD (CA and DC) 11788.13.1.1 Closed-loop spatial
multiplexing performance 11788.13.1.1.1 Minimum Requirement Multi-Layer
Spatial Multiplexing 4 Tx Antenna Port 11788.13.1.1.2 Minimum
Requirement Multi-Layer Spatial Multiplexing 4 Tx Antenna Port for dual
connectivity 11828.13.1.1.3 Minimum Requirement Multi-Layer Spatial
Multiplexing 4 Tx Antenna Port with 256QAM 11848.13.1.1.4 Minimum
Requirement Four-Layer Spatial Multiplexing 4 Tx Antenna Port
11868.13.1.2 Dual-Layer Spatial Multiplexing (User-Specific Reference
Symbols) 11878.13.1.2.1 Minimum Requirement Dual-Layer Spatial
Multiplexing 2 Tx Antenna Port 11878.13.1.3 Enhanced Performance
Requirements Type A Closed-loop spatial multiplexing 11908.13.1.3.1
Minimum Requirement Single-Layer Spatial Multiplexing 2 Tx Antenna Port
with TM4 interference model (Cell-Specific Reference Symbols)
11908.13.1.4 Enhanced Performance Requirement Type A - Single-layer
Spatial Multiplexing (User-Specific Reference Symbols) 11928.13.1.4.1
Minimum Requirement Enhanced Performance Requirement Type A --
Single-layer Spatial Multiplexing with TM9 interference model
(User-Specific Reference Symbols) 11928.13.2 TDD (CA and DC)
11958.13.2.1 Closed-loop spatial multiplexing performance 11968.13.2.1.1
Minimum Requirement Multi-Layer Spatial Multiplexing 4 Tx Antenna Port
11968.13.2.1.2 Minimum Requirement Multi-Layer Spatial Multiplexing 4 Tx
Antenna Port for dual connectivity 11988.13.2.1.3 Minimum Requirement
Multi-Layer Spatial Multiplexing 4 Tx Antenna Port with 256QAM
11998.13.2.1.4 Minimum Requirement Four-Layer Spatial Multiplexing 4 Tx
Antenna Port 12008.13.2.2 Dual-Layer Spatial Multiplexing (User-Specific
Reference Symbols) 12028.13.2.2.1 Minimum Requirement Dual-Layer Spatial
Multiplexing 2 Tx Antenna Port 12028.13.2.4 Enhanced Performance
Requirement Type A - Single-layer Spatial Multiplexing (User-Specific
Reference Symbols) 12068.13.2.4.1 Minimum Requirement Enhanced
Performance Requirement Type A -- Single-layer Spatial Multiplexing with
TM9 interference model (User-Specific Reference Symbols) 12068.13.3
TDD-FDD (CA and DC) 12088.13.3.1 Closed-loop spatial multiplexing
performance 4Tx Antenna Port 12088.13.3.1.1 Minimum Requirement for FDD
PCell 12088.13.3.1.2 Minimum Requirement for TDD PCell 12128.13.3.2
Dual-Layer Spatial Multiplexing (User-Specific Reference Symbols)
12168.13.3.2.1 Minimum Requirement Dual-Layer Spatial Multiplexing 2 Tx
Antenna Port for FDD PCell 12168.13.3.2.2 Minimum Requirement Dual-Layer
Spatial Multiplexing 2 Tx Antenna Port for TDD PCell 12198.13.3.3
Enhanced Performance Requirements Type A Closed-loop spatial
multiplexing 12228.13.3.3.1 Minimum Requirement Single-Layer Spatial
Multiplexing 2 Tx Antenna Port with TM4 interference model
(Cell-Specific Reference Symbols) for FDD PCell 12228.13.3.3.2 Minimum
Requirement Single-Layer Spatial Multiplexing 2 Tx Antenna Port with TM4
interference model (Cell-Specific Reference Symbols) for TDD PCell
12248.13.3.4 Enhanced Performance Requirement Type A - Single-layer
Spatial Multiplexing (User-Specific Reference Symbols) 12268.13.3.4.1
Minimum Requirement Enhanced Performance Requirement Type A --
Single-layer Spatial Multiplexing with TM9 interference model
(User-Specific Reference Symbols) for FDD PCell 12268.13.3.4.2 Minimum
Requirement Enhanced Performance Requirement Type A -- Single-layer
Spatial Multiplexing with TM9 interference model (User-Specific
Reference Symbols) for TDD PCell 12298.13.3.5 Closed-loop spatial
multiplexing performance 4Tx Antenna Port for DC 12328.13.3.5.1 Minimum
Requirement for FDD PCell 12328.13.3.5.2 Minimum Requirement for TDD
PCell 12348.13.3.6 Closed-loop spatial multiplexing performance 4Tx
Antenna Port with 256QAM 12368.13.3.6.1 Minimum Requirement for FDD
PCell 12368.13.3.6.2 Minimum Requirement for TDD PCell 12388.13.3.7
Closed-loop spatial multiplexing performance 4Tx Antenna Port with Four
layers 12398.13.3.7.1 Minimum Requirement for FDD PCell 12398.13.3.7.2
Minimum Requirement for TDD PCell 12418.14 Demodulation (UE supporting
Short TTI) 12438.14.1 Slot-PDSCH and Subslot-PDSCH 12438.14.1.1 FDD
(Fixed Reference Channel) 12438.14.1.1.1 Open-loop spatial multiplexing
performance 12438.14.1.1.2 Closed-loop spatial multiplexing performance
(User-Specific Reference Signals) 12448.14.1.2 TDD (Fixed Reference
Channel) 12468.14.1.2.1 Open-loop spatial multiplexing performance
12468.14.1.2.2 Closed-loop spatial multiplexing performance
(User-Specific Reference Signals) 12478.14.2 SPDCCH 12488.14.2.1 FDD
12488.14.2.1.1 Mimimum requirement 12498.14.2.2 TDD 12498.14.2.2.1
Mimimum requirement 12508.15 Demodulation (8 receiver antenna ports)
12518.15.1 PDSCH 12518.15.1.1 Void 12518.15.1.2 TDD (Fixed Reference
Channel) 12518.15.1.2.1 Transmit diversity performance with 2Tx Antenna
Ports (Cell-Specific Reference Symbols) 12518.15.1.2.2 Open-loop spatial
multiplexing performance with 2Tx Antenna Ports (Cell-Specific Reference
Symbols) 12528.15.1.2.3 8 Layer Spatial Multiplexing (User-Specific
Reference Symbols) 12528.15.2 CA 12548.15.2.1 Void 12548.15.2.2 TDD
12548.15.2.2.1 Eight Layer Spatial Multiplexing (User-Specific Reference
Symbols) 12549 Reporting of Channel State Information 12569.1 General
12569.1.1 Applicability of requirements 12569.1.1.1 Applicability of
requirements for different channel bandwidths 12569.1.1.2 Applicability
and test rules for different CA configurations and bandwidth combination
sets 12569.1.1.2A Applicability and test rules for different TDD-FDD CA
configurations and bandwidth combination sets 12579.1.1.3 Test coverage
for different number of componenet carriers 12589.1.1.4 Applicability of
performance requirements for 4Rx capable UEs 12589.1.1.4.1 Applicability
rule and antenna connection for single carrier tests with 2Rx
12589.1.1.4.2 Applicability rule and antenna connection for CA tests
with 2Rx 12609.1.1.4.3 Applicability rule and antenna connection for
single carrier tests with 4Rx 12619.1.1.5 Applicability of requirements
for UEs supporting coverage enhancement 12619.2 CQI reporting definition
under AWGN conditions 12619.2.1 Minimum requirement PUCCH 1-0
(Cell-Specific Reference Symbols) 12619.2.1.1 FDD 12619.2.1.2 TDD
12629.2.1.3 FDD (CSI measurements in case two CSI subframe sets are
configured) 12639.2.1.4 TDD (CSI measurements in case two CSI subframe
sets are configured) 12669.2.1.5 FDD (CSI measurements in case two CSI
subframe sets are configured and with CRS assistance information)
12699.2.1.6 TDD (CSI measurements in case two CSI subframe sets are
configured and with CRS assistance information) 12729.2.1.7 FDD
(Modulation and TBS index Table 2 and 4-bit CQI Table 2 are used)
12759.2.1.8 TDD (Modulation and TBS index Table 2 and 4-bit CQI Table 2
are used) 12769.2.1.9 FDD (Modulation and TBS index Table 3 and 4-bit
CQI Table 4 are used) 12769.2.1.10 TDD (Modulation and TBS index Table 3
and 4-bit CQI Table 4 are used) 12779.2.2 Minimum requirement PUCCH 1-1
(Cell-Specific Reference Symbols) 12789.2.2.1 FDD 12789.2.2.2 TDD
12799.2.3 Minimum requirement PUCCH 1-1 (CSI Reference Symbols)
12809.2.3.1 FDD 12809.2.3.1A FDD (With *channelMeasRestriction*
configured) 12819.2.3.2 TDD 12829.2.3.2A TDD (With
*channelMeasRestriction* configured) 12839.2.4 Minimum requirement PUCCH
1-1 (With Single CSI Process) 12849.2.4.1 FDD 12859.2.4.1A FDD (With
*interferenceMeasRestriction* configured) 12879.2.4.2 TDD 12909.2.4.2A
TDD (With *interferenceMeasRestriction* configured) 12939.2.5 Minimum
requirement PUCCH 1-1 (when *csi-SubframeSet --r12* and
*EIMTA-MainConfigServCell-r12* are configured) 12969.2.6 Minimum
requirement PUSCH 3-0 (Cell-Specific Reference Symbols) 12999.2.6.1
Frame structure type 3 with FDD Pcell 12999.2.6.2 Frame structure type 3
with TDD Pcell 13019.2.7 Minimum requirement PUSCH 3-1 (CSI Reference
Symbol) 13039.2.7.1 Frame structure type 3 wth FDD Pcell 13039.2.7.2
Frame structure type 3 wth TDD Pcell 13059.3 CQI reporting under fading
conditions 13099.3.1 Frequency-selective scheduling mode 13099.3.1.1
Minimum requirement PUSCH 3-0 (Cell-Specific Reference Symbols)
13099.3.1.1.1 FDD 13099.3.1.1.2 TDD 13109.3.1.1.3 FDD (CSI measurements
in case two CSI subframe sets are configured and with CRS assistance
information) 13119.3.1.1.4 TDD (CSI measurements in case two CSI
subframe sets are configured and with CRS assistance information)
13159.3.1.1.5 TDD (when *csi-SubframeSet --r12* is configured)
13189.3.1.2 Minimum requirement PUSCH 3-1 (CSI Reference Symbol)
13209.3.1.2.1 FDD 13209.3.1.2.2 TDD 13219.3.1.2.3 FDD (Modulation and
TBS index Table 2 and 4-bit CQI Table 2 are used) 13239.3.1.2.4 TDD
(Modulation and TBS index Table 2 and 4-bit CQI Table 2 are used)
13249.3.1.2.5 Void 13259.3.1.2.6 TDD (when *csi-SubframeSet --r12* is
configured with one CSI process) 13259.3.2 Frequency non-selective
scheduling mode 13299.3.2.1 Minimum requirement PUCCH 1-0 (Cell-Specific
Reference Symbol) 13299.3.2.1.1 FDD 13299.3.2.1.2 TDD 13319.3.2.2
Minimum requirement PUCCH 1-1 (CSI Reference Symbol) 13339.3.2.2.1 FDD
13339.3.2.2.2 TDD 13349.3.3 Frequency-selective interference 13369.3.3.1
Minimum requirement PUSCH 3-0 (Cell-Specific Reference Symbol)
13369.3.3.1.1 FDD 13369.3.3.1.2 TDD 13379.3.3.2 Void 13389.3.3.2.1 Void
13389.3.3.2.2 Void 13389.3.4 UE-selected subband CQI 13389.3.4.1 Minimum
requirement PUSCH 2-0 (Cell-Specific Reference Symbols) 13389.3.4.1.1
FDD 13389.3.4.1.2 TDD 13399.3.4.2 Minimum requirement PUCCH 2-0
(Cell-Specific Reference Symbols) 13409.3.4.2.1 FDD 13409.3.4.2.2 TDD
13429.3.5 Additional requirements for enhanced receiver Type A
13449.3.5.1 Minimum requirement PUCCH 1-0 (Cell-Specific Reference
Symbol) 13449.3.5.1.1 FDD 13449.3.5.1.2 TDD 13459.3.5.2 Minimum
requirement PUCCH 1-1 (CSI Reference Symbol) 13479.3.5.2.1 FDD
13479.3.5.2.2 TDD 13509.3.6 Minimum requirement (With multiple CSI
processes) 13539.3.6.1 FDD 13539.3.6.2 TDD 13589.3.7 Minimum requirement
PUSCH 3-2 13629.3.7.1 FDD 13629.3.7.2 TDD 13639.3.8 Additional
requirements for enhanced receiver Type B 13659.3.8.1 Minimum
requirement PUCCH 1-1 (Cell-Specific Reference Symbols) 13659.3.8.1.1
FDD 13659.3.8.1.2 TDD 13669.3.8.2 Minimum requirement PUCCH 1-1 (CSI
Reference Symbols) 13689.3.8.2.1 FDD 13689.3.8.2.2 TDD 13709.3.8.3
Minimum requirement with CSI process 13739.3.8.3.1 FDD 13739.3.8.3.2 TDD
13769.4 Reporting of Precoding Matrix Indicator (PMI) 13799.4.1 Single
PMI 13809.4.1.1 Minimum requirement PUSCH 3-1 (Cell-Specific Reference
Symbols) 13809.4.1.1.1 FDD 13809.4.1.1.2 TDD 13819.4.1.2 Minimum
requirement PUCCH 2-1 (Cell-Specific Reference Symbols) 13829.4.1.2.1
FDD 13829.4.1.2.2 TDD 13849.4.1.3 Minimum requirement PUSCH 3-1 (CSI
Reference Symbol) 13859.4.1.3.1 FDD 13859.4.1.3.2 TDD 13889.4.1.3.3 FDD
(with Class A 12Tx codebook) 13919.4.1.3.4 TDD (with Class A 12Tx
codebook) 13939.4.1.3.5 FDD (with Class A 24Tx codebook) 13969.4.1.3.6
TDD (with Class A 24Tx codebook) 13989.4.1.4 Minimum requirement PUCCH
1-1 (CSI Reference Symbol) 14019.4.1.4.1 FDD (with 4Tx enhanced
codebook) 14019.4.1.4.2 TDD (with 4Tx enhanced codebook) 14039.4.1.4.3
FDD (with Class B alternative codebook for one CSI-RS resource
configured) 14069.4.1.4.4 TDD (with Class B alternative codebook for one
CSI-RS resource configured) 14089.4.1a Void 14119.4.1a.1 Void
14119.4.1a.1.1 Void 14119.4.1a.1.2 Void 14119.4.2 Multiple PMI
14119.4.2.1 Minimum requirement PUSCH 1-2 (Cell-Specific Reference
Symbols) 14119.4.2.1.1 FDD 14119.4.2.1.2 TDD 14129.4.2.2 Minimum
requirement PUSCH 2-2 (Cell-Specific Reference Symbols) 14139.4.2.2.1
FDD 14139.4.2.2.2 TDD 14149.4.2.3 Minimum requirement PUSCH 1-2 (CSI
Reference Symbol) 14159.4.2.3.1 FDD 14159.4.2.3.2 TDD 14179.4.2.3.3 FDD
(with 4Tx enhanced codebook) 14209.4.2.3.4 TDD (with 4Tx enhanced
codebook) 14229.4.2.3.5 FDD (with Class A 16Tx codebook) 14249.4.2.3.6
TDD (with Class A 16Tx codebook) 14279.4.2.3.7 FDD (with Class A 32Tx
codebook) 14309.4.2.3.8 TDD (with Class A 32Tx codebook) 14339.4.2.3.9
FDD (with Class A 16Tx advanced codebook) 14369.4.2.3.10 TDD (with Class
A 16Tx advanced codebook) 14399.4.3 Void 14429.5 Reporting of Rank
Indicator (RI) 14429.5.1 Minimum requirement (Cell-Specific Reference
Symbols) 14429.5.1.1 FDD 14429.5.1.2 TDD 14439.5.2 Minimum requirement
(CSI Reference Symbols) 14449.5.2.1 FDD 14449.5.2.2 TDD 14469.5.3
Minimum requirement (CSI measurements in case two CSI subframe sets are
configured) 14489.5.3.1 FDD 14489.5.3.2 TDD 14519.5.4 Minimum
requirement (CSI measurements in case two CSI subframe sets are
configured and CRS assistance information are configured) 14549.5.4.1
FDD 14549.5.4.2 TDD 14579.5.5 Minimum requirement (with CSI process)
14609.5.5.1 FDD 14619.5.5.2 TDD 14649.6 Additional requirements for
carrier aggregation 14679.6.1 Periodic reporting on multiple cells
(Cell-Specific Reference Symbols) 14679.6.1.1 FDD 14679.6.1.2 TDD
14739.6.1.3 TDD-FDD CA with FDD PCell 14799.6.1.4 TDD-FDD CA with TDD
PCell 14849.7 CSI reporting (Single receiver antenna) 14909.7.1 CQI
reporting definition under AWGN conditions 14919.7.1.1 FDD and
half-duplex FDD 14919.7.1.2 TDD 14919.7.1.3 FDD (Category 1bis UE)
14929.7.1.4 TDD (Category 1bis UE) 14939.7.2 CQI reporting under fading
conditions 14949.7.2.1 FDD and half-duplex FDD 14949.7.2.2 TDD
14959.7.2.3 FDD (Category 1bis UE) 14969.7.2.4 TDD (Category 1bis UE)
14979.8 CSI reporting (UE supporting coverage enhancement) 14989.8.1 CQI
reporting definition under AWGN conditions 14989.8.1.1 FDD and
half-duplex FDD 14989.8.1.2 TDD 14999.8.2 UE-selected subband CQI
15009.8.2.1 FDD and half-duplex FDD 15009.8.2.2 TDD 15049.8.3 CQI
reporting definition for UE supporting 64QAM under AWGN 15079.8.3.1 FDD
and half-duplex FDD 15079.8.3.2 TDD 15089.8.4 CQI reporting definition
for UE supporting alternative table under AWGN 15099.8.4.1 FDD and
half-duplex FDD 15099.8.4.2 TDD 15109.8.5 PMI reporting with PUCCH 1-1
(CSI Reference Symbol) 15119.8.5.1 FDD 15129.8.5.2 TDD 15139.9 CSI
reporting for 4Rx UE 15149.9.1 CQI reporting definition under AWGN
conditions 15149.9.1.1 Minimum requirement PUCCH 1-0 with Rank 1
(Cell-Specific Reference Symbols) 15159.9.1.1.1 FDD 15159.9.1.1.2 TDD
15159.9.1.2 Minimum requirement PUCCH 1-1 with Rank 2 (CSI Reference
Symbols) 15169.9.1.2.1 FDD 15169.9.1.2.2 TDD 15179.9.1.3 Minimum
requirement PUCCH 1-1 with Rank 4 (Cell-Specific Reference Symbols)
15189.9.1.3.1 FDD 15199.9.1.3.2 TDD 15199.9.1.4 Minimum requirement
PUCCH 1-1 with Rank 3 (CSI Reference Symbols) 15209.9.1.4.1 FDD
15209.9.1.4.2 TDD 15219.9.2 CQI reporting definition under fading
conditions 15229.9.2.1 Minimum requirement PUCCH 1-0 (Cell-Specific
Reference Symbol) for enhanced receiver Type A 15229.9.2.1.1 FDD
15239.9.2.1.2 TDD 15249.9.2.2 Minimum requirement PUCCH 1-1 (CSI
Reference Symbol) for enhanced receiver Type A 15269.9.2.2.1 FDD
15269.9.2.2.2 TDD 15299.9.3 Reporting of Precoding Matrix Indicator
(PMI) for 4Rx UE 15329.9.3.1 Minimum requirement PUSCH 3-1 (CSI
Reference Symbol) 15339.9.3.1.1 TDD 15339.9.4 Reporting of Rank
Indicator (RI) 15359.9.4.1 Minimum requirement (Cell-Specific Reference
Symbols) 15359.9.4.1.1 FDD 15359.9.4.1.2 TDD 15379.9.4.2 Minimum
requirement (CSI Reference Symbols) 15389.9.4.2.1 FDD 15389.9.4.2.2 TDD
15409.10 Reporting of CSI-RS Resource Indicator (CRI) 15429.10.1 Minimum
requirement (PUSCH 3-1) 15439.10.1.1 FDD 15439.10.1.2 TDD 15459.10.2
Minimum requirement (PUSCH 3-1, QCL Type C) 15479.10.2.1 FDD
15479.10.2.2 TDD 15509.11 Reporting of Hybrid Channel state information
15539.11.1 Minimum requirement (with eMIMO-Type configured as Class B
with more than one CSI-RS resource configured and eMIMO-Type2 as Class B
with one CSI-RS resource configured) 15539.11.1.1 FDD 15549.11.1.2 TDD
15569.12 CSI reporting (UE supporting Short TTI) 15589.12.1 CQI
reporting under fading conditions (Cell-Specific Reference Symbol)
15589.12.1.1 FDD 15589.12.1.2 TDD 15619.12.2 CQI reporting under fading
conditions (CSI Reference Symbol) 15629.12.2.1 FDD 15629.12.2.2 TDD
15659.13 CSI reporting for 8Rx UE 15679.13.1 CQI reporting definition
under AWGN conditions 15679.13.1.1 Minimum requirement PUCCH 1-1 with
Rank 4 (CSI Reference Symbols) 15679.13.1.2.1 Void 15679.13.1.2.2 TDD
156710 Performance requirement (MBMS) 156810.1 FDD (Fixed Reference
Channel) 156810.1.1 Minimum requirement 156910.2 TDD (Fixed Reference
Channel) 157010.2.1 Minimum requirement 157010.3 FDD (Fixed Reference
Channel) with FeMBMS 157110.3.1 Minimum requirement for FeMBMS
Unicast-mixed Cell under CA 157110.3.1.1 Minimum requirement with
1.25kHz subcarrier spacing 157110.3.1.2 Minimum requirement with 7.5kHz
subcarrier spacing 157210.3.2 Minimum requirement for FeMBMS
Unicast-mixed Cell as Non-Serving Cell 157310.3.2.1 Minimum requirement
with 1.25kHz subcarrier spacing 157310.3.2.2 Minimum requirement with
7.5kHz subcarrier spacing 157410.3.3 Minimum requirement for MBMS
Dedicated cell 157510.3.3.1 Minimum requirement with 1.25kHz subcarrier
spacing 157510.3.3.2 Minimum requirement with 7.5kHz subcarrier spacing
157610.3.3.3 Minimum requirement with 15kHz subcarrier spacing 157710.4
FDD with 5G terrestrial broadcast 157810.4.1 Minimum requirement for
PMCH decoding 157810.4.1.1 Minimum requirement with 0.37kHz subcarrier
spacing 157810.4.1.2 Minimum requirement with 2.5kHz subcarrier spacing
157910.4.2 Minimum requirement for CAS detection 158010.4.2.1 Minimum
requirement for PBCH detection 158011 Performance requirement (ProSe
Direct Discovery) 158011.1 General 158111.1.1 Applicability of
requirements 158111.1.2 Reference DRX configuration 158111.2
Demodulation of PSDCH (single link performance) 158111.2.1 FDD
(in-coverage) 158111.2.2 TDD (in-coverage) 158211.2.3 FDD
(out-of-coverage) 158311.3 Power imbalance performance with two links
158411.3.1 FDD 158411.3.2 TDD 158511.4 Multiple timing reference test
158611.4.1 FDD 158711.5 Maximum Sidelink processes test 158811.5.1 FDD
158811.5.2 TDD 158912 Performance requirement (ProSe Direct
Communication) 159112.1 General 159112.1.1 Applicability of requirements
159112.1.1.1 Applicability of requirements for different channel
bandwidths 159112.1.1.2 Test coverage for different number of component
carriers 159112.1.1.3 Applicability and test rules for different CA
configurations and bandwidth combination sets 159112.1.2 Reference DRX
configuration 159212.2 Demodulation of PSSCH 159212.2.1 FDD 159212.3
Demodulation of PSCCH 159312.3.1 FDD 159412.4 Demodulation of PSBCH
159512.4.1 FDD 159512.5 Power imbalance performance with two links
159512.5.1 FDD 159512.6 Multiple timing reference test 159712.6.1 FDD
159712.7 Maximum Sidelink processes test 160012.7.1 FDD 160012.8
Sustained downlink data rate with active Sidelink 160113 Void 160314
Performance requirement (V2X Sidelink Communication) 160314.1 General
160314.1.1 Applicability of requirements 160314.2 Demodulation of PSSCH
160414.3 Demodulation of PSCCH 160514.4 Power imbalance performance with
two links 160514.5 Demodulation of PSBCH 160614.6 Demodulation of PSSCH
with eNB based synchronization 160714.7 Soft buffer test 160714.8 PSCCH
decoding capability test 160814.9 Sustained downlink data rate with
active sidelink 160914.10 Soft buffer test (CA) 161014.11 PSCCH/PSSCH
decoding capability test (CA) 1611Annex A (normative): Measurement
channels 1614A.1 General 1614A.2 UL reference measurement channels
1614A.2.1 General 1614A.2.1.1 Applicability and common parameters
1614A.2.1.2 Determination of payload size 1614A.2.1.3 Overview of UL
reference measurement channels 1615A.2.2 Reference measurement channels
for FDD 1638A.2.2.1 Full RB allocation 1638A.2.2.1.1 QPSK 1638A.2.2.1.2
16-QAM 1640A.2.2.1.3 64-QAM 1642A.2.2.1.4 256 QAM 1643A.2.2.2 Partial RB
allocation 1643A.2.2.2.1 QPSK 1644A.2.2.2.2 16-QAM 1647A.2.2.2.3 64-QAM
1649A.2.2.2.4 256 QAM 1651A.2.2.3 Void 1651A.2.2.4 subPRB allocation
1652A.2.3 Reference measurement channels for TDD 1652A.2.3.1 Full RB
allocation 1652A.2.3.1.1 QPSK 1652A.2.3.1.2 16-QAM 1655A.2.3.1.3 64-QAM
1658A.2.3.1.4 256 QAM 1658A.2.3.2 Partial RB allocation 1658A.2.3.2.1
QPSK 1659A.2.3.2.2 16-QAM 1663A.2.3.2.3 64-QAM 1668A.2.3.2.4 256 QAM
1670A.2.3.3 Void 1670A.2.3.4 subPRB allocation 1671A.2.4 Reference
measurement channels for UE category NB1 1671A.2.5 Reference measurement
channels for LAA 1672A.2.5.1 Full RB allocation 1672A.2.5.1.1 QPSK
1672A.2.5.1.2 16QAM 1673A.2.5.1.3 64QAM 1673A.2.5.2 Partial RB
allocation 1673A.2.5.2.1 QPSK 1674A.2.5.2.2 16QAM 1674A.2.5.2.3 64QAM
1675A.3 DL reference measurement channels 1675A.3.1 General 1675A.3.1.1
Overview of DL reference measurement channels 1676A.3.2 Reference
measurement channel for receiver characteristics 1701A.3.3 Reference
measurement channels for PDSCH performance requirements (FDD)
1731A.3.3.1 Single-antenna transmission (Common Reference Symbols)
1731A.3.3.2 Multi-antenna transmission (Common Reference Symbols)
1736A.3.3.2.1 Two antenna ports 1736A.3.3.2.2 Four antenna ports
1744A.3.3.3 Reference Measurement Channel for UE-Specific Reference
Symbols 1749A.3.3.3.0 Two antenna ports (no CSI-RS) 1749A.3.3.3.1 Two
antenna port (CSI-RS) 1750A.3.3.3.2 Four antenna ports (CSI-RS)
1753A.3.3.3.2A Eight antenna ports (CSI-RS) 1760A.3.3.3.3 Twelve antenna
port (CSI-RS) 1762A.3.3.3.4 Sixteen antenna port (CSI-RS) 1763A.3.3.3.5
Twenty-four antenna port (CSI-RS) 1764A.3.3.3.6 Thirty-two antenna port
(CSI-RS) 1765A.3.4 Reference measurement channels for PDSCH performance
requirements (TDD) 1767A.3.4.1 Single-antenna transmission (Common
Reference Symbols) 1767A.3.4.2 Multi-antenna transmission (Common
Reference Signals) 1775A.3.4.2.1 Two antenna ports 1775A.3.4.2.2 Four
antenna ports 1788A.3.4.3 Reference Measurement Channels for UE-Specific
Reference Symbols 1795A.3.4.3.1 Single antenna port (Cell Specific)
1795A.3.4.3.2 Two antenna ports (Cell Specific) 1796A.3.4.3.3 Two
antenna ports (CSI-RS) 1798A.3.4.3.4 Four antenna ports (CSI-RS)
1806A.3.4.3.5 Eight antenna ports (CSI-RS) 1813A.3.4.3.6 Twelve antenna
ports (CSI-RS) 1819A.3.4.3.7 Sixteen antenna ports (CSI-RS)
1820A.3.4.3.8 Twenty-four antenna ports (CSI-RS) 1821A.3.4.3.9
Thirty-two antenna ports (CSI-RS) 1822A.3.5 Reference measurement
channels for PDCCH/PCFICH performance requirements 1824A.3.5.1 FDD
1824A.3.5.2 TDD 1824A.3.5.3 LAA 1825A.3.6 Reference measurement channels
for PHICH performance requirements 1825A.3.7 Reference measurement
channels for PBCH performance requirements 1825A.3.8 Reference
measurement channels for MBMS performance requirements 1826A.3.8.1 FDD
1826A.3.8.2 TDD 1831A.3.9 Reference measurement channels for sustained
downlink data rate provided by lower layers 1833A.3.9.1 FDD 1833A.3.9.2
TDD 1837A.3.9.3 FDD (EPDCCH scheduling) 1851A.3.9.4 TDD (EPDCCH
scheduling) 1852A.3.9.5 LAA 1854A.3.10 Reference Measurement Channels
for EPDCCH performance requirements 1856A.3.10.1 FDD 1856A.3.10.2 TDD
1856A.3.11 Reference Measurement Channels for MPDCCH performance
requirements 1856A.3.11.1 FDD and half-duplex FDD 1856A.3.11.2 TDD
1857A.3.12 Reference measurement channels for NPDSCH performance
requirements 1858A.3.12.1 In-band 1858A.3.12.1.2 Two-antenna
transmission 1858A.3.12.2 Standalone/Guard-band 1860A.3.12.2.1
Single-antenna transmission 1860A.3.13 Reference measurement channels
for NPDCCH performance requirements 1863A.3.13.1 Half-duplex FDD
1863A.3.13.2 TDD 1864A.3.14 Reference measurement channels for NPBCH
performance requirements for Cat NB1 UEs 1864A.3.15 Reference
Measurement Channels for LAA SCell with frame structure Type-3
1865A.3.15.1 Multi-antenna transmission (Common Reference Symbols)
1865A.3.15.1.1 Four antenna ports 1865A.3.15.2 Reference Measurement
Channel for UE-Specific Reference Symbols 1865A.3.15.2.1 Two antenna
ports (CSI-RS) 1865A.3.16 Reference measurement channels for Slot-PDSCH
and Subslot-PDSCH performance requirements 1867A.3.16.1 FDD 1867A.3.16.2
TDD 1871A.3.17 Reference measurement channels for SPDCCH performance
requirements 1872A.3.17.1 FDD 1872A.3.17.2 TDD 1873A.4 CSI reference
measurement channels 1873A.5 OFDMA Channel Noise Generator (OCNG)
1888A.5.1 OCNG Patterns for FDD 1888A.5.1.1 OCNG FDD pattern 1: One
sided dynamic OCNG FDD pattern 1888A.5.1.2 OCNG FDD pattern 2: Two sided
dynamic OCNG FDD pattern 1889A.5.1.3 OCNG FDD pattern 3: 49 RB OCNG
allocation with MBSFN in 10 MHz 1889A.5.1.3A OCNG FDD pattern 3A: 49 RB
OCNG allocation with MBSFN enhancement in 10 MHz 1890A.5.1.4 OCNG FDD
pattern 4: One sided dynamic OCNG FDD pattern for MBMS transmission
1890A.5.1.4A OCNG FDD pattern 4A: One sided dynamic OCNG FDD pattern for
enhanced MBMS transmission 1891A.5.1.5 OCNG FDD pattern 5: One sided
dynamic 16QAM modulated OCNG FDD pattern 1892A.5.1.6 OCNG FDD pattern 6:
dynamic OCNG FDD pattern when user data is in 2 non-contiguous blocks
1893A.5.1.8 OCNG FDD pattern 8: Dynamic OCNG FDD pattern for TM10
transmission 1894A.5.2 OCNG Patterns for TDD 1895A.5.2.1 OCNG TDD
pattern 1: One sided dynamic OCNG TDD pattern 1895A.5.2.2 OCNG TDD
pattern 2: Two sided dynamic OCNG TDD pattern 1896A.5.2.3 OCNG TDD
pattern 3: 49 RB OCNG allocation with MBSFN in 10 MHz 1897A.5.2.4 OCNG
TDD pattern 4: One sided dynamic OCNG TDD pattern for MBMS transmission
1897A.5.2.5 OCNG TDD pattern 5: One sided dynamic 16QAM modulated OCNG
TDD pattern 1898A.5.2.6 OCNG TDD pattern 6: dynamic OCNG TDD pattern
when user data is in 2 non-contiguous blocks 1899A.5.2.8 OCNG TDD
pattern 8: Dynamic OCNG TDD pattern for TM10 transmission 1900A.5.3 OCNG
Patterns for Narrowband IoT 1901A.5.3.1 Narrowband IoT OCNG pattern 1
1901A.5.4 OCNG Patterns for frame structure type 3 1902A.5.4.1 OCNG FS3
pattern 1: One sided dynamic OCNG frame structure type 3 pattern
1902A.5.4.2 OCNG FS3 pattern 2: Two sided dynamic OCNG frame structure 3
pattern 1903A.6 Sidelink reference measurement channels 1904A.6.1
General 1904A.6.1.1 Overview of ProSe reference measurement channels
1904A.6.2 Reference measurement channel for receiver characteristics
1905A.6.3 Reference measurement channels for PSDCH performance
requirements 1907A.6.4 Reference measurement channels for PSCCH
performance requirements 1908A.6.5 Reference measurement channels for
PSSCH performance requirements 1908A.6.6 Reference measurement channels
for PSBCH performance requirements 1909A.7 Sidelink reference resource
pool configurations 1910A.7.1 Reference resource pool configurations for
ProSe Direct Discovery demodulation tests 1910A.7.1.1 FDD 1910A.7.1.2
TDD 1913A.7.2 Reference resource pool configurations for ProSe Direct
Communication demodulation tests 1915A.7.2.1 FDD 1915A.8 V2X reference
measurement channels 1920A.8.1 General 1920A.8.1.1 Overview of V2X
reference measurement channels 1921A.8.2 Reference measurement channel
for receiver characteristics 1921A.8.3 Reference measurement channel for
transmitter characteristics 1923A.8.4 Reference measurement for PSCCH
performance requirements 1926A.8.5 Reference measurement for PSSCH
performance requirements 1927A.8.6 Reference measurement for PSBCH
performance requirements 1927A.9 V2X reference resource pool
configurations 1928Annex B (normative): Propagation conditions 1931B.1
Static propagation condition 1931B.1.1 UE Receiver with 2Rx 1931B.1.2 UE
Receiver with 4Rx 1931B.1.3 UE Receiver with 8Rx 1932B.2 Multi-path
fading propagation conditions 1933B.2.1 Delay profiles 1933B.2.2
Combinations of channel model parameters 1934B.2.3 MIMO Channel
Correlation Matrices 1935B.2.3.1 Definition of MIMO Correlation Matrices
1935B.2.3.2 MIMO Correlation Matrices at High, Medium and Low Level
1941B.2.3A MIMO Channel Correlation Matrices using cross polarized
antennas 1944B.2.3A.1 Definition of MIMO Correlation Matrices using
cross polarized antennas 1945B.2.3A.2 Spatial Correlation Matrices using
cross polarized antennas at eNB and UE sides 1945B.2.3A.2.1 Spatial
Correlation Matrices at eNB side 1945B.2.3A.2.2 Spatial Correlation
Matrices at UE side 1946B.2.3A.4 Beam steering approach 1949B.2.3B MIMO
Channel Correlation Matrices using two-dimension cross polarized
antennas at eNB and cross polarized antennas at UE 1949B.2.3B.1
Definition of MIMO Correlation Matrices using two-dimension cross
polarized antennas at eNB and cross polarized antennas at UE
1950B.2.3B.2 Spatial Correlation Matrices using two-dimension cross
polarized antennas at eNB and cross polarized antennas at UE
1951B.2.3B.2.1 Spatial Correlation Matrices at eNB side 1951B.2.3B.2.2
Spatial Correlation Matrices at UE side 1951B.2.3B.3 MIMO Correlation
Matrices using two-dimension cross polarized antennas at eNB and cross
polarized antennas at UE 1951B.2.3B.4 Beam steering approach
1954B.2.3B.4A Beam steering approach with dual cluster beams 1955B.2.4
Propagation conditions for CQI tests 1956B.2.4.1 Propagation conditions
for CQI tests with multiple CSI processes 1956B.2.5 Void 1956B.2.6 MBSFN
Propagation Channel Profile 1956B.2.6.1 Subcarrier spacing 15kHz or
7.5kHz 1956B.2.6.2 Subcarrier spacing 1.25kHz 1957B.2.6.3 Subcarrier
spacing 0.37kHz 1958B.2.6.4 Subcarrier spacing 2.5kHz 1958B.3 High speed
train scenario 1959B.3A HST-SFN scenario 1960B.3B HST-SFN scenario for
500 km/h speed 1964B.3C HST scenario for 500 km/h speed 1964B.4
Beamforming Model 1964B.4.1 Single-layer random beamforming (Antenna
port 5, 7, or 8) 1964B.4.1A Single-layer random beamforming (Antenna
port 7, 8, 11 or 13 with enhanced DMRS table configured) 1965B.4.2
Dual-layer random beamforming (antenna ports 7 and 8) 1965B.4.3 Generic
beamforming model (antenna ports 7-14) 1966B.4.4 Random beamforming for
EPDCCH distributed transmission (Antenna port 107 and 109) 1966B.4.5
Random beamforming for EPDCCH localized transmission (Antenna port 107,
108, 109 or 110) 1967B.4.6 Beamforming model for CRI test 1967B.5
Interference models for enhanced performance requirements Type-A
1968B.5.1 Dominant interferer proportion 1968B.5.2 Transmission mode 3
interference model 1969B.5.3 Transmission mode 4 interference model
1969B.5.4 Transmission mode 9 interference model 1970B.6 Interference
models for enhanced performance requirements Type-B 1970B.6.1
Transmission mode 2 interference model 1970B.6.2 Transmission mode 3
interference model 1970B.6.3 Transmission mode 4 interference model
1971B.6.4 Transmission mode 9 interference model 1971B.6.5 CRS
interference model 1972B.6.6 Random interference model 1972B.7
Interference models for enhanced downlink control channel performance
requirements Type A and B 1973B.7.1 PDCCH, PCFICH and PHICH interference
model 1973B.8 Burst transmission models for Frame structure type 3
1974B.8.1 Burst transmission model for one LAA SCell 1974B.8.2 Burst
transmission model for multiple LAA SCell(s) 1974Annex C (normative):
Downlink Physical Channels 1976C.1 General 1976C.2 Set-up 1976C.3
Connection 1976C.3.1 Measurement of Receiver Characteristics 1976C.3.2
Measurement of Performance requirements 1977C.3.3 Aggressor cell power
allocation for Measurement of Performance Requirements when ABS is
Configured 1978C.3.4 Power Allocation for Measurement of Performance
Requirements when Quasi Co-location Type B: same Cell ID 1979C.3.5
Simplified CA testing method 1979C.3.6 Measurement of Receiver
Characteristics for Narrowband IoT 1980Annex D (normative):
Characteristics of the interfering signal 1981D.1 General 1981D.2
Interference signals 1981Annex E (normative): Environmental conditions
1982E.1 General 1982E.2 Environmental 1982E.2.1 Temperature 1982E.2.2
Voltage 1982E.2.3 Vibration 1983Annex F (normative): Transmit modulation
1984F.1 Measurement Point 1984F.2 Basic Error Vector Magnitude
measurement 1984F.3 Basic in-band emissions measurement 1985F.4 Modified
signal under test 1985F.5 Window length 1987F.5.1 Timing offset
1987F.5.2 Window length 1987F.5.3 Window length for normal CP 1987F.5.4
Window length for Extended CP 1988F.5.5 Window length for PRACH
1988F.5.F Window length for category NB1 1989F.6 Averaged EVM 1989F.6.F
Averaged EVM for category NB1 1990F.7 Spectrum Flatness 1990Annex G
(informative): Reference sensitivity level in lower SNR 1991G.1 General
1991G.2 Typical receiver sensitivity performance (QPSK) 1991G.3
Reference measurement channel for REFSENSE in lower SNR 1997Annex H
(normative): Modified MPR behavior 2000H.1 Indication of modified MPR
behavior 2000Annex I (normative): Supported Post Antenna Gain 2001I.1
Declared Supported Post Antenna Gain for UE 2001Annex J (informative):
Change history 2002
