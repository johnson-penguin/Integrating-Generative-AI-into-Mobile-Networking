Compliance template for 3GPP 5G NR RIT (Release 15 and beyond)
--------------------------------------------------------------

The compliance templates provided by 3GPP are for the assessment of the
compliance of 5G[^1] developed by 3GPP. It includes one compliance
template for SRIT (encompassing NR and LTE), and one compliance template
for NR RIT.

This document provides the compliance template for the NR RIT based on
3GPP Rel-15 and Rel-16 work.

#### 5.2.4.1 Compliance template **for** services[^2]

+----------------------+----------------------+----------------------+
|                      | Service capability   | Evaluator's comments |
|                      | requirements         |                      |
+======================+======================+======================+
| **5.2.4.1.1**        | **Support for wide   | *The assessment of   |
|                      | range of services**  | service requirement  |
|                      |                      | follows the          |
|                      | Is the proposal able | evaluation method as |
|                      | to support a range   | defined in Section   |
|                      | of services across   | 7.3.3 in Report      |
|                      | different usage      | ITU-R M.2412.*       |
|                      | scenarios (eMBB,     |                      |
|                      | URLLC, and mMTC)?:   |                      |
|                      | *YES*                |                      |
|                      |                      |                      |
|                      | Specify which usage  |                      |
|                      | scenarios (eMBB,     |                      |
|                      | URLLC, and mMTC) the |                      |
|                      | candidate RIT or     |                      |
|                      | candidate SRIT can   |                      |
|                      | support.^(1)^        |                      |
|                      |                      |                      |
|                      | *The NR RIT can      |                      |
|                      | support eMBB, URLLC  |                      |
|                      | and mMTC usage       |                      |
|                      | scenarios.*          |                      |
+----------------------+----------------------+----------------------+
| ^(1)^ Refer to the   |                      |                      |
| process requirements |                      |                      |
| in IMT-2020/2.       |                      |                      |
+----------------------+----------------------+----------------------+

#### 5.2.4.2 Compliance **template** for spectrum3

+---------------+-----------------------------------------------------+
|               | Spectrum capability requirements                    |
+===============+=====================================================+
| **5.2.4.2.1** | **Frequency bands identified for IMT**              |
|               |                                                     |
|               | Is the proposal able to utilize at least one        |
|               | frequency band identified for IMT in the ITU Radio  |
|               | Regulations?: *YES*                                 |
|               |                                                     |
|               | Specify in which band(s) the candidate RIT or       |
|               | candidate SRIT can be deployed.                     |
|               |                                                     |
|               | *The supported frequency bands identified for IMT   |
|               | are provided in item 5.2.3.2.8.3 in characteristics |
|               | template for NR RIT. See the table for frequency    |
|               | range 1 (FR1).*                                     |
+---------------+-----------------------------------------------------+
| **5.2.4.2.2** | **Higher Frequency range/band(s)**                  |
|               |                                                     |
|               | Is the proposal able to utilize the higher          |
|               | frequency range/band(s) above 24.25 GHz?: *YES*     |
|               |                                                     |
|               | Specify in which band(s) the candidate RIT or       |
|               | candidate SRIT can be deployed.                     |
|               |                                                     |
|               | NOTE 1 -- In the case of the candidate SRIT, at     |
|               | least one of the component RITs need to fulfil this |
|               | requirement.                                        |
|               |                                                     |
|               | *The supported frequency bands above 24.25 GHz are  |
|               | provided in item 5.2.3.2.8.3 in characteristics     |
|               | template for NR RIT. See the table for frequency    |
|               | range 2 (FR2).*                                     |
+---------------+-----------------------------------------------------+

#### 5.2.4.3 Compliance template for **technical** performance3

##### *For NR RIT:*

***NOTE : The following values are derived based on the employed
evaluation configurations. Higher performance might be achieved by using
other evaluation configurations.***

*See self evaluation report for detailed analysis, results and specific
assumptions (e.g. duplexing schemes, antenna configurations, etc.).*

+-------+-------+-------+-------+-------+-------+-------+-------+
| Mi    | Cat   | Req   | Value | R     | Comm  |       |       |
| nimum | egory | uired | ^(2)^ | equir | ents\ |       |       |
| tech  |       | value |       | ement | ^(3)^ |       |       |
| nical |       |       |       | met?  |       |       |       |
| p     |       |       |       |       |       |       |       |
| erfor |       |       |       |       |       |       |       |
| mance |       |       |       |       |       |       |       |
| re    |       |       |       |       |       |       |       |
| quire |       |       |       |       |       |       |       |
| ments |       |       |       |       |       |       |       |
| item  |       |       |       |       |       |       |       |
| (5    |       |       |       |       |       |       |       |
| .2.4. |       |       |       |       |       |       |       |
| 3.x), |       |       |       |       |       |       |       |
| u     |       |       |       |       |       |       |       |
| nits, |       |       |       |       |       |       |       |
| and   |       |       |       |       |       |       |       |
| Re    |       |       |       |       |       |       |       |
| port\ |       |       |       |       |       |       |       |
| ITU-R |       |       |       |       |       |       |       |
| M.2   |       |       |       |       |       |       |       |
| 410-0 |       |       |       |       |       |       |       |
| se    |       |       |       |       |       |       |       |
| ction |       |       |       |       |       |       |       |
| refe  |       |       |       |       |       |       |       |
| rence |       |       |       |       |       |       |       |
| ^(1)^ |       |       |       |       |       |       |       |
+=======+=======+=======+=======+=======+=======+=======+=======+
|       | Usage | Test  | Dow   |       |       |       |       |
|       | sce   | e     | nlink |       |       |       |       |
|       | nario | nviro | or    |       |       |       |       |
|       |       | nment | u     |       |       |       |       |
|       |       |       | plink |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| **5.  | eMBB  | Not   | Dow   | 20    | *21   | *Yes* | *The  |
| 2.4.3 |       | appli | nlink |       | .1\~1 |       | v     |
| .1**\ |       | cable |       |       | 40.2* |       | alues |
| Peak  |       |       |       |       |       |       | are   |
| data  |       |       |       |       |       |       | ach   |
| rate  |       |       |       |       |       |       | ieved |
| (Gbi  |       |       |       |       |       |       | by    |
| t/s)\ |       |       |       |       |       |       | using |
| *(    |       |       |       |       |       |       | 16    |
| 4.1)* |       |       |       |       |       |       | ca    |
|       |       |       |       |       |       |       | rrier |
|       |       |       |       |       |       |       | agg   |
|       |       |       |       |       |       |       | regat |
|       |       |       |       |       |       |       | ion.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | U     | 10    | *1    | *Yes* |       |
|       |       |       | plink |       | 6.6\~ |       |       |
|       |       |       |       |       | 64.6* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| **5.  | eMBB  | Not   | Dow   | 30    | *3    | *Yes* |       |
| 2.4.3 |       | appli | nlink |       | 0.4\~ |       |       |
| .2**\ |       | cable |       |       | 48.9* |       |       |
| Peak  |       |       |       |       |       |       |       |
| spe   |       |       |       |       |       |       |       |
| ctral |       |       |       |       |       |       |       |
| effic |       |       |       |       |       |       |       |
| iency |       |       |       |       |       |       |       |
| (     |       |       |       |       |       |       |       |
| bit/s |       |       |       |       |       |       |       |
| /Hz)\ |       |       |       |       |       |       |       |
| *(    |       |       |       |       |       |       |       |
| 4.2)* |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | U     | 15    | *1    | *Yes* |       |
|       |       |       | plink |       | 8.2\~ |       |       |
|       |       |       |       |       | 25.8* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| **5.  | eMBB  | Dense | Dow   | 100   | *     | *Yes* | *For  |
| 2.4.3 |       | Urban | nlink |       | 100.8 |       | evalu |
| .3**\ |       | --    |       |       | 7\~14 |       | ation |
| User  |       | eMBB  |       |       | 9.29* |       | con   |
| e     |       |       |       |       |       |       | figur |
| xperi |       |       |       |       |       |       | ation |
| enced |       |       |       |       |       |       | A (4  |
| data  |       |       |       |       |       |       | GHz)  |
| rate  |       |       |       |       |       |       | and C |
| (Mbi  |       |       |       |       |       |       | (mul  |
| t/s)\ |       |       |       |       |       |       | ti-ba |
| *(    |       |       |       |       |       |       | nd/la |
| 4.3)* |       |       |       |       |       |       | yer), |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | U     | 50    | *50.  | *Yes* |       |
|       |       |       | plink |       | 06\~7 |       |       |
|       |       |       |       |       | 3.15* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| **5.  | eMBB  | I     | Dow   | 0.3   | *0    | *Yes* | *For  |
| 2.4.3 |       | ndoor | nlink |       | .31\~ |       | evalu |
| .4**\ |       | Ho    |       |       | 0.59* |       | ation |
| 5^th^ |       | tspot |       |       |       |       | con   |
| perce |       | --    |       |       |       |       | figur |
| ntile |       | eMBB  |       |       |       |       | ation |
| user  |       |       |       |       |       |       | A (4  |
| spe   |       |       |       |       |       |       | GHz), |
| ctral |       |       |       |       |       |       | Ch    |
| effic |       |       |       |       |       |       | annel |
| iency |       |       |       |       |       |       | model |
| (     |       |       |       |       |       |       | A/B,  |
| bit/s |       |       |       |       |       |       | with  |
| /Hz)\ |       |       |       |       |       |       | 12    |
| *(    |       |       |       |       |       |       | TRxP  |
| 4.4)* |       |       |       |       |       |       | and   |
|       |       |       |       |       |       |       | 36    |
|       |       |       |       |       |       |       | T     |
|       |       |       |       |       |       |       | RxP.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | U     | 0.21  | *0    | *Yes* |       |
|       |       |       | plink |       | .27\~ |       |       |
|       |       |       |       |       | 0.63* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | Dow   | 0.3   | *0    | *Yes* | *For  |
|       |       |       | nlink |       | .31\~ |       | evalu |
|       |       |       |       |       | 1.18* |       | ation |
|       |       |       |       |       |       |       | con   |
|       |       |       |       |       |       |       | figur |
|       |       |       |       |       |       |       | ation |
|       |       |       |       |       |       |       | B (30 |
|       |       |       |       |       |       |       | GHz), |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B,  |
|       |       |       |       |       |       |       | with  |
|       |       |       |       |       |       |       | 12    |
|       |       |       |       |       |       |       | TRxP  |
|       |       |       |       |       |       |       | and   |
|       |       |       |       |       |       |       | 36    |
|       |       |       |       |       |       |       | T     |
|       |       |       |       |       |       |       | RxP.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | U     | 0.21  | *0    | *Yes* |       |
|       |       |       | plink |       | .30\~ |       |       |
|       |       |       |       |       | 0.43* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       | eMBB  | Dense | Dow   | 0.225 | *0    | *Yes* | *For  |
|       |       | Urban | nlink |       | .23\~ |       | evalu |
|       |       | --    |       |       | 0.81* |       | ation |
|       |       | eMBB  |       |       |       |       | con   |
|       |       |       |       |       |       |       | figur |
|       |       |       |       |       |       |       | ation |
|       |       |       |       |       |       |       | A (4  |
|       |       |       |       |       |       |       | GHz), |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | U     | 0.15  | *0    | *Yes* |       |
|       |       |       | plink |       | .16\~ |       |       |
|       |       |       |       |       | 0.60* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       | Rural | Dow   | 0.12  | *0    | *Yes* | *For  |
|       |       | --    | nlink |       | .13\~ |       | evalu |
|       |       | eMBB  |       |       | 0.57* |       | ation |
|       |       |       |       |       |       |       | con   |
|       |       |       |       |       |       |       | figur |
|       |       |       |       |       |       |       | ation |
|       |       |       |       |       |       |       | A     |
|       |       |       |       |       |       |       | (700  |
|       |       |       |       |       |       |       | MHz), |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | U     | 0.045 | *0    | *Yes* |       |
|       |       |       | plink |       | .09\~ |       |       |
|       |       |       |       |       | 0.63* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | Dow   | 0.12  | *0    | *Yes* | *For  |
|       |       |       | nlink |       | .12\~ |       | evalu |
|       |       |       |       |       | 2.11* |       | ation |
|       |       |       |       |       |       |       | con   |
|       |       |       |       |       |       |       | figur |
|       |       |       |       |       |       |       | ation |
|       |       |       |       |       |       |       | B (4  |
|       |       |       |       |       |       |       | GHz), |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | U     | 0.045 | *0    | *Yes* |       |
|       |       |       | plink |       | .02\~ |       |       |
|       |       |       |       |       | 0.34* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| **5.  | eMBB  | I     | Dow   | 9     | *8.   | *Yes* | *For  |
| 2.4.3 |       | ndoor | nlink |       | 77\~1 |       | evalu |
| .5**\ |       | Ho    |       |       | 6.88* |       | ation |
| Av    |       | tspot |       |       |       |       | con   |
| erage |       | --    |       |       |       |       | figur |
| spe   |       | eMBB  |       |       |       |       | ation |
| ctral |       |       |       |       |       |       | A (4  |
| effic |       |       |       |       |       |       | GHz), |
| iency |       |       |       |       |       |       | Ch    |
| (bit/ |       |       |       |       |       |       | annel |
| s/Hz/ |       |       |       |       |       |       | model |
| T     |       |       |       |       |       |       | A/B,  |
| RxP)\ |       |       |       |       |       |       | with  |
| *(    |       |       |       |       |       |       | 12    |
| 4.5)* |       |       |       |       |       |       | TRxP  |
|       |       |       |       |       |       |       | and   |
|       |       |       |       |       |       |       | 36    |
|       |       |       |       |       |       |       | T     |
|       |       |       |       |       |       |       | RxP.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | U     | 6.75  | *6.   | *Yes* |       |
|       |       |       | plink |       | 95\~1 |       |       |
|       |       |       |       |       | 5.17* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | Dow   | 9     | *8    | *Yes* | *For  |
|       |       |       | nlink |       | .5\~1 |       | evalu |
|       |       |       |       |       | 9.91* |       | ation |
|       |       |       |       |       |       |       | con   |
|       |       |       |       |       |       |       | figur |
|       |       |       |       |       |       |       | ation |
|       |       |       |       |       |       |       | B (30 |
|       |       |       |       |       |       |       | GHz), |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B,  |
|       |       |       |       |       |       |       | with  |
|       |       |       |       |       |       |       | 12    |
|       |       |       |       |       |       |       | TRxP  |
|       |       |       |       |       |       |       | and   |
|       |       |       |       |       |       |       | 36    |
|       |       |       |       |       |       |       | T     |
|       |       |       |       |       |       |       | RxP.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | U     | 6.75  | *6    | *Yes* |       |
|       |       |       | plink |       | .9\~1 |       |       |
|       |       |       |       |       | 1.44* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       | eMBB  | Dense | Dow   | 7.8   | *7.   | *Yes* | *For  |
|       |       | Urban | nlink |       | 87\~2 |       | evalu |
|       |       | --    |       |       | 2.33* |       | ation |
|       |       | eMBB  |       |       |       |       | con   |
|       |       |       |       |       |       |       | figur |
|       |       |       |       |       |       |       | ation |
|       |       |       |       |       |       |       | A (4  |
|       |       |       |       |       |       |       | GHz), |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | U     | 5.4   | *5.   | *Yes* |       |
|       |       |       | plink |       | 51\~2 |       |       |
|       |       |       |       |       | 2.48* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       | eMBB  | Rural | Dow   | 3.3   | *5.   | *Yes* | *For  |
|       |       | --    | nlink |       | 04\~1 |       | evalu |
|       |       | eMBB  |       |       | 7.37* |       | ation |
|       |       |       |       |       |       |       | con   |
|       |       |       |       |       |       |       | figur |
|       |       |       |       |       |       |       | ation |
|       |       |       |       |       |       |       | A     |
|       |       |       |       |       |       |       | (700  |
|       |       |       |       |       |       |       | MHz), |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | U     | 1.6   | *3.   | *Yes* |       |
|       |       |       | plink |       | 75\~1 |       |       |
|       |       |       |       |       | 5.55* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | Dow   | 3.3   | *5.   | *Yes* | *For  |
|       |       |       | nlink |       | 96\~2 |       | evalu |
|       |       |       |       |       | 1.11* |       | ation |
|       |       |       |       |       |       |       | con   |
|       |       |       |       |       |       |       | figur |
|       |       |       |       |       |       |       | ation |
|       |       |       |       |       |       |       | B (4  |
|       |       |       |       |       |       |       | GHz), |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | U     | 1.6   | *     | *Yes* |       |
|       |       |       | plink |       | 2.7\~ |       |       |
|       |       |       |       |       | 21.3* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | Dow   | 3.3   | *3    | *Yes* | *For  |
|       |       |       | nlink |       | .9\~1 |       | evalu |
|       |       |       |       |       | 9.29* |       | ation |
|       |       |       |       |       |       |       | con   |
|       |       |       |       |       |       |       | figur |
|       |       |       |       |       |       |       | ation |
|       |       |       |       |       |       |       | C     |
|       |       |       |       |       |       |       | (L    |
|       |       |       |       |       |       |       | MLC), |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | U     | 1.6   | *3.   | *Yes* |       |
|       |       |       | plink |       | 31\~1 |       |       |
|       |       |       |       |       | 0.59* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| **5.  | eMBB  | Indo  | Dow   | 10    | *10.  | *Yes* | *For  |
| 2.4.3 |       | or-Ho | nlink |       | 00\~1 |       | evalu |
| .6**\ |       | tspot |       |       | 5.04* |       | ation |
| Area  |       | --    |       |       |       |       | con   |
| tr    |       | eMBB  |       |       |       |       | figur |
| affic |       |       |       |       |       |       | ation |
| cap   |       |       |       |       |       |       | A (4  |
| acity |       |       |       |       |       |       | GHz), |
| (Mbi  |       |       |       |       |       |       | Ch    |
| t/s/m |       |       |       |       |       |       | annel |
| ^2^)\ |       |       |       |       |       |       | model |
| *(    |       |       |       |       |       |       | A/B,  |
| 4.6)* |       |       |       |       |       |       | with  |
|       |       |       |       |       |       |       | 12    |
|       |       |       |       |       |       |       | TRxP  |
|       |       |       |       |       |       |       | and   |
|       |       |       |       |       |       |       | 36    |
|       |       |       |       |       |       |       | T     |
|       |       |       |       |       |       |       | RxP.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | Dow   | 10    | *10.  | *Yes* | *For  |
|       |       |       | nlink |       | 22\~2 |       | evalu |
|       |       |       |       |       | 2.76* |       | ation |
|       |       |       |       |       |       |       | con   |
|       |       |       |       |       |       |       | figur |
|       |       |       |       |       |       |       | ation |
|       |       |       |       |       |       |       | B (30 |
|       |       |       |       |       |       |       | GHz), |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B,  |
|       |       |       |       |       |       |       | with  |
|       |       |       |       |       |       |       | 12    |
|       |       |       |       |       |       |       | TRxP  |
|       |       |       |       |       |       |       | and   |
|       |       |       |       |       |       |       | 36    |
|       |       |       |       |       |       |       | T     |
|       |       |       |       |       |       |       | RxP.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
| **5.  | eMBB  | Not   | Dow   | 4     | *0    | *Yes* |       |
| 2.4.3 |       | appli | nlink |       | .28\~ |       |       |
| .7**\ |       | cable |       |       | 3.19* |       |       |
| User  |       |       |       |       |       |       |       |
| plane |       |       |       |       |       |       |       |
| lat   |       |       |       |       |       |       |       |
| ency\ |       |       |       |       |       |       |       |
| (ms)\ |       |       |       |       |       |       |       |
| *(4.  |       |       |       |       |       |       |       |
| 7.1)* |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | U     | 4     | *0    | *Yes* |       |
|       |       |       | plink |       | .28\~ |       |       |
|       |       |       |       |       | 3.84* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       | URLLC | Not   | Dow   | 1     | *0    | *Yes* |       |
|       |       | appli | nlink |       | .23\~ |       |       |
|       |       | cable |       |       | 0.99* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | U     | 1     | *0    | *Yes* |       |
|       |       |       | plink |       | .24\~ |       |       |
|       |       |       |       |       | 0.98* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| **5.  | eMBB  | Not   | Not   | 20    | *1    | *Yes* |       |
| 2.4.3 |       | appli | appli |       | 1.3\~ |       |       |
| .8**\ |       | cable | cable |       | 18.8* |       |       |
| Co    |       |       |       |       |       |       |       |
| ntrol |       |       |       |       |       |       |       |
| plane |       |       |       |       |       |       |       |
| la    |       |       |       |       |       |       |       |
| tency |       |       |       |       |       |       |       |
| (ms)\ |       |       |       |       |       |       |       |
| *(4.  |       |       |       |       |       |       |       |
| 7.2)* |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       | URLLC | Not   | Not   | 20    | *1    | *Yes* |       |
|       |       | appli | appli |       | 1.3\~ |       |       |
|       |       | cable | cable |       | 18.8* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| **5.  | mMTC  | Urban | U     | 1 000 | *3    | *Yes* | *For  |
| 2.4.3 |       | Macro | plink | 000   | 6,008 |       | evalu |
| .9**\ |       | --    |       |       | ,000/ |       | ation |
| Conne |       | mMTC  |       |       | 180   |       | con   |
| ction |       |       |       |       | k     |       | figur |
| de    |       |       |       |       | Hz\~\ |       | ation |
| nsity |       |       |       |       | 3     |       | A     |
| (     |       |       |       |       | 6,324 |       | (ISD= |
| devic |       |       |       |       | ,000/ |       | 500m) |
| es/km |       |       |       |       | 180   |       | with  |
| ^2^)\ |       |       |       |       | kHz*  |       | full  |
| *(    |       |       |       |       |       |       | b     |
| 4.8)* |       |       |       |       |       |       | uffer |
|       |       |       |       |       |       |       | s     |
|       |       |       |       |       |       |       | ystem |
|       |       |       |       |       |       |       | level |
|       |       |       |       |       |       |       | simul |
|       |       |       |       |       |       |       | ation |
|       |       |       |       |       |       |       | fol   |
|       |       |       |       |       |       |       | lowed |
|       |       |       |       |       |       |       | by    |
|       |       |       |       |       |       |       | link  |
|       |       |       |       |       |       |       | level |
|       |       |       |       |       |       |       | s     |
|       |       |       |       |       |       |       | imula |
|       |       |       |       |       |       |       | tion; |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | U     | 1 000 | *1,26 | *Yes* | *For  |
|       |       |       | plink | 000   | 7,000 |       | evalu |
|       |       |       |       |       | / 180 |       | ation |
|       |       |       |       |       | k     |       | con   |
|       |       |       |       |       | Hz\~\ |       | figur |
|       |       |       |       |       | 1,50  |       | ation |
|       |       |       |       |       | 3,000 |       | B     |
|       |       |       |       |       | / 180 |       | (     |
|       |       |       |       |       | kHz*  |       | ISD=1 |
|       |       |       |       |       |       |       | 732m) |
|       |       |       |       |       |       |       | with  |
|       |       |       |       |       |       |       | full  |
|       |       |       |       |       |       |       | b     |
|       |       |       |       |       |       |       | uffer |
|       |       |       |       |       |       |       | s     |
|       |       |       |       |       |       |       | ystem |
|       |       |       |       |       |       |       | level |
|       |       |       |       |       |       |       | simul |
|       |       |       |       |       |       |       | ation |
|       |       |       |       |       |       |       | fol   |
|       |       |       |       |       |       |       | lowed |
|       |       |       |       |       |       |       | by    |
|       |       |       |       |       |       |       | link  |
|       |       |       |       |       |       |       | level |
|       |       |       |       |       |       |       | s     |
|       |       |       |       |       |       |       | imula |
|       |       |       |       |       |       |       | tion; |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
| **5.2 | eMBB  | Not   | Not   | Capab | *     | *Yes* | *Ne   |
| .4.3. |       | appli | appli | ility | Sleep |       | twork |
| 10**\ |       | cable | cable | to    | r     |       | side* |
| E     |       |       |       | su    | atio: |       |       |
| nergy |       |       |       | pport | 80    |       |       |
| e     |       |       |       | a     | %\~99 |       |       |
| ffici |       |       |       | high  | .87%* |       |       |
| ency\ |       |       |       | sleep |       |       |       |
| *(    |       |       |       | ratio | *     |       |       |
| 4.9)* |       |       |       | and   | Sleep |       |       |
|       |       |       |       | long  | durat |       |       |
|       |       |       |       | sleep | ion:* |       |       |
|       |       |       |       | dur   |       |       |       |
|       |       |       |       | ation | *Up   |       |       |
|       |       |       |       |       | to    |       |       |
|       |       |       |       |       | 1     |       |       |
|       |       |       |       |       | 59ms* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       |       |       | *     | *Yes* | *D    |
|       |       |       |       |       | Sleep |       | evice |
|       |       |       |       |       | r     |       | side* |
|       |       |       |       |       | atio: |       |       |
|       |       |       |       |       | 84.   |       |       |
|       |       |       |       |       | 2%\~9 |       |       |
|       |       |       |       |       | 9.5%* |       |       |
|       |       |       |       |       |       |       |       |
|       |       |       |       |       | *     |       |       |
|       |       |       |       |       | Sleep |       |       |
|       |       |       |       |       | durat |       |       |
|       |       |       |       |       | ion:* |       |       |
|       |       |       |       |       |       |       |       |
|       |       |       |       |       | *2.56 |       |       |
|       |       |       |       |       | s\~10 |       |       |
|       |       |       |       |       | .24s* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| **5.2 | URLLC | Urban | Dow   | 1-1   | *99   | *Yes* | *For  |
| .4.3. |       | Macro | nlink | 0^−5^ | .9996 |       | evalu |
| 11**\ |       | --    |       | su    | 5%\~\ |       | ation |
| Re    |       | URLLC |       | ccess | 99.99 |       | con   |
| liabi |       |       |       | p     | 999%* |       | figur |
| lity\ |       |       |       | robab |       |       | ation |
| *(4   |       |       |       | ility |       |       | A (4  |
| .10)* |       |       |       | of    |       |       | GHz), |
|       |       |       |       | tr    |       |       | Ch    |
|       |       |       |       | ansmi |       |       | annel |
|       |       |       |       | tting |       |       | model |
|       |       |       |       | a     |       |       | A/B.* |
|       |       |       |       | layer |       |       |       |
|       |       |       |       | 2 PDU |       |       |       |
|       |       |       |       | (pro  |       |       |       |
|       |       |       |       | tocol |       |       |       |
|       |       |       |       | data  |       |       |       |
|       |       |       |       | unit) |       |       |       |
|       |       |       |       | of    |       |       |       |
|       |       |       |       | size  |       |       |       |
|       |       |       |       | 32    |       |       |       |
|       |       |       |       | bytes |       |       |       |
|       |       |       |       | w     |       |       |       |
|       |       |       |       | ithin |       |       |       |
|       |       |       |       | 1 ms  |       |       |       |
|       |       |       |       | in    |       |       |       |
|       |       |       |       | ch    |       |       |       |
|       |       |       |       | annel |       |       |       |
|       |       |       |       | qu    |       |       |       |
|       |       |       |       | ality |       |       |       |
|       |       |       |       | of    |       |       |       |
|       |       |       |       | cov   |       |       |       |
|       |       |       |       | erage |       |       |       |
|       |       |       |       | edge  |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | Dow   |       | *9    | *Yes* | *For  |
|       |       |       | nlink |       | 9.999 |       | evalu |
|       |       |       |       |       | 4%\~\ |       | ation |
|       |       |       |       |       | 99.*  |       | con   |
|       |       |       |       |       | *9999 |       | figur |
|       |       |       |       |       | 991%* |       | ation |
|       |       |       |       |       |       |       | B     |
|       |       |       |       |       |       |       | (700  |
|       |       |       |       |       |       |       | MHz), |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | U     |       | *9    | *Yes* | *For  |
|       |       |       | plink |       | 9.999 |       | evalu |
|       |       |       |       |       | 2%\~\ |       | ation |
|       |       |       |       |       | 99.99 |       | con   |
|       |       |       |       |       | 99999 |       | figur |
|       |       |       |       |       | 992%* |       | ation |
|       |       |       |       |       |       |       | A (4  |
|       |       |       |       |       |       |       | GHz), |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       | U     |       | *9    | *Yes* | *For  |
|       |       |       | plink |       | 9.999 |       | evalu |
|       |       |       |       |       | 2%\~\ |       | ation |
|       |       |       |       |       | 99.   |       | con   |
|       |       |       |       |       | 99999 |       | figur |
|       |       |       |       |       | 999%* |       | ation |
|       |       |       |       |       |       |       | B     |
|       |       |       |       |       |       |       | (700  |
|       |       |       |       |       |       |       | MHz), |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
| **5.2 | eMBB  | I     | U     | S     | *S    | *Yes* | *For  |
| .4.3. |       | ndoor | plink | tatio | tatio |       | evalu |
| 12**\ |       | Ho    |       | nary, | nary, |       | ation |
| Mob   |       | tspot |       | Pedes | P     |       | conf  |
| ility |       | --    |       | trian | edest |       | igura |
| cla   |       | eMBB  |       |       | rian* |       | tions |
| sses\ |       |       |       |       |       |       | A (4  |
| *(4   |       |       |       |       |       |       | GHz)  |
| .11)* |       |       |       |       |       |       | and B |
|       |       |       |       |       |       |       | (30   |
|       |       |       |       |       |       |       | GHz)  |
|       |       |       |       |       |       |       | in    |
|       |       |       |       |       |       |       | I     |
|       |       |       |       |       |       |       | ndoor |
|       |       |       |       |       |       |       | Ho    |
|       |       |       |       |       |       |       | tspot |
|       |       |       |       |       |       |       | --    |
|       |       |       |       |       |       |       | e     |
|       |       |       |       |       |       |       | MBB.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       | eMBB  | Dense | U     | S     | *S    | *Yes* | *For  |
|       |       | Urban | plink | tatio | tatio |       | evalu |
|       |       | --    |       | nary, | nary, |       | ation |
|       |       | eMBB  |       | P     | Pe    |       | conf  |
|       |       |       |       | edest | destr |       | igura |
|       |       |       |       | rian, | ian,* |       | tions |
|       |       |       |       |       |       |       | A (4  |
|       |       |       |       | Vehi  | *Vehi |       | GHz)  |
|       |       |       |       | cular | cular |       | and B |
|       |       |       |       | (up   | (up   |       | (30   |
|       |       |       |       | to 30 | to 30 |       | GHz)  |
|       |       |       |       | km/h) | k     |       | in    |
|       |       |       |       |       | m/h)* |       | Dense |
|       |       |       |       |       |       |       | Urban |
|       |       |       |       |       |       |       | --    |
|       |       |       |       |       |       |       | eMBB* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       | eMBB  | Rural | U     | P     | *P    | *Yes* | *For  |
|       |       | --    | plink | edest | edest |       | evalu |
|       |       | eMBB  |       | rian, | rian, |       | ation |
|       |       |       |       | Vehic | Vehic |       | conf  |
|       |       |       |       | ular, | ular, |       | igura |
|       |       |       |       | High  | High  |       | tions |
|       |       |       |       | speed | speed |       | A     |
|       |       |       |       | vehi  | vehic |       | (700  |
|       |       |       |       | cular | ular* |       | MHz)  |
|       |       |       |       |       |       |       | and B |
|       |       |       |       |       |       |       | (4    |
|       |       |       |       |       |       |       | GHz)  |
|       |       |       |       |       |       |       | in    |
|       |       |       |       |       |       |       | Rural |
|       |       |       |       |       |       |       | -     |
|       |       |       |       |       |       |       | eMBB* |
+-------+-------+-------+-------+-------+-------+-------+-------+
| **5.  | eMBB  | I     | U     | 1.5   | *1    | *Yes* | *For  |
| 2.4.3 |       | ndoor | plink | (10   | .59\~ |       | evalu |
| .13** |       | Ho    |       | km/h) | 3.85* |       | ation |
|       |       | tspot |       |       |       |       | con   |
| Mobi  |       | --    |       |       |       |       | figur |
| lity\ |       | eMBB  |       |       |       |       | ation |
| Tr    |       |       |       |       |       |       | A (4  |
| affic |       |       |       |       |       |       | GHz), |
| ch    |       |       |       |       |       |       | Ch    |
| annel |       |       |       |       |       |       | annel |
| link  |       |       |       |       |       |       | model |
| data  |       |       |       |       |       |       | A/B,  |
| rates |       |       |       |       |       |       | LOS   |
| (     |       |       |       |       |       |       | and   |
| bit/s |       |       |       |       |       |       | N     |
| /Hz)\ |       |       |       |       |       |       | LOS.* |
| *(4   |       |       |       |       |       |       |       |
| .11)* |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       |       | 1.5   | *2    | *Yes* | *For  |
|       |       |       |       | (10   | .14\~ |       | evalu |
|       |       |       |       | km/h) | 4.76* |       | ation |
|       |       |       |       |       |       |       | con   |
|       |       |       |       |       |       |       | figur |
|       |       |       |       |       |       |       | ation |
|       |       |       |       |       |       |       | B (30 |
|       |       |       |       |       |       |       | GHz), |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B,  |
|       |       |       |       |       |       |       | LOS   |
|       |       |       |       |       |       |       | and   |
|       |       |       |       |       |       |       | N     |
|       |       |       |       |       |       |       | LOS.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       | eMBB  | Dense | U     | 1.12  | *1    | *Yes* | *For  |
|       |       | Urban | plink | (30   | .28\~ |       | evalu |
|       |       | --    |       | km/h) | 4.58* |       | ation |
|       |       | eMBB  |       |       |       |       | con   |
|       |       |       |       |       |       |       | figur |
|       |       |       |       |       |       |       | ation |
|       |       |       |       |       |       |       | A (4  |
|       |       |       |       |       |       |       | GHz), |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B,  |
|       |       |       |       |       |       |       | LOS   |
|       |       |       |       |       |       |       | and   |
|       |       |       |       |       |       |       | N     |
|       |       |       |       |       |       |       | LOS.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       |       | 1.12  | *1    | *Yes* | *For  |
|       |       |       |       | (30   | .23\~ |       | evalu |
|       |       |       |       | km/h) | 3.22* |       | ation |
|       |       |       |       |       |       |       | con   |
|       |       |       |       |       |       |       | figur |
|       |       |       |       |       |       |       | ation |
|       |       |       |       |       |       |       | B (30 |
|       |       |       |       |       |       |       | GHz), |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B,  |
|       |       |       |       |       |       |       | LOS   |
|       |       |       |       |       |       |       | and   |
|       |       |       |       |       |       |       | N     |
|       |       |       |       |       |       |       | LOS.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       | eMBB  | Rural | U     | 0.8   | *0    | *Yes* | *For  |
|       |       | --    | plink | (120  | .85\~ |       | evalu |
|       |       | eMBB  |       | km/h) | 2.91* |       | ation |
|       |       |       |       |       |       |       | con   |
|       |       |       |       |       |       |       | figur |
|       |       |       |       |       |       |       | ation |
|       |       |       |       |       |       |       | A     |
|       |       |       |       |       |       |       | (700  |
|       |       |       |       |       |       |       | MHz), |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B,  |
|       |       |       |       |       |       |       | LOS   |
|       |       |       |       |       |       |       | and   |
|       |       |       |       |       |       |       | N     |
|       |       |       |       |       |       |       | LOS.* |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       |       | 0.45  | *0    | *Yes* |       |
|       |       |       |       | (500  | .60\~ |       |       |
|       |       |       |       | km/h) | 2.73* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       |       | 0.8   | *1    | *Yes* | *For  |
|       |       |       |       | (120  | .02\~ |       | evalu |
|       |       |       |       | km/h) | 2.75* |       | ation |
|       |       |       |       |       |       |       | con   |
|       |       |       |       |       |       |       | figur |
|       |       |       |       |       |       |       | ation |
|       |       |       |       |       |       |       | B (4  |
|       |       |       |       |       |       |       | GHz), |
|       |       |       |       |       |       |       | Ch    |
|       |       |       |       |       |       |       | annel |
|       |       |       |       |       |       |       | model |
|       |       |       |       |       |       |       | A/B,  |
|       |       |       |       |       |       |       | LOS   |
|       |       |       |       |       |       |       | and   |
|       |       |       |       |       |       |       | N     |
|       |       |       |       |       |       |       | LOS.* |
|       |       |       |       |       |       |       |       |
|       |       |       |       |       |       |       | *.*   |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       |       | 0.45  | *0    | *Yes* |       |
|       |       |       |       | (500  | .64\~ |       |       |
|       |       |       |       | km/h) | 2.09* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| **5   | eMBB  | Not   | Not   | 0     | *0*   | *Yes* |       |
| .2.4. | and   | appli | appli |       |       |       |       |
| 3.14\ | URLLC | cable | cable |       |       |       |       |
| **Mob |       |       |       |       |       |       |       |
| ility |       |       |       |       |       |       |       |
| in    |       |       |       |       |       |       |       |
| terru |       |       |       |       |       |       |       |
| ption |       |       |       |       |       |       |       |
| time  |       |       |       |       |       |       |       |
| (ms)\ |       |       |       |       |       |       |       |
| *(4   |       |       |       |       |       |       |       |
| .12)* |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| **5.2 | Not   | Not   | Not   | At    | *800  | *Yes* |       |
| .4.3. | appli | appli | appli | least | MHz   |       |       |
| 15**\ | cable | cable | cable | 10    | \~    |       |       |
| Band  |       |       |       | 0 MHz | 6.4   |       |       |
| width |       |       |       |       | GHz*  |       |       |
| and   |       |       |       |       |       |       |       |
| Sc    |       |       |       |       |       |       |       |
| alabi |       |       |       |       |       |       |       |
| lity\ |       |       |       |       |       |       |       |
| *(4   |       |       |       |       |       |       |       |
| .13)* |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       |       | Up to |       | *Yes* |       |
|       |       |       |       | 1 GHz |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
|       |       |       |       | Su    | *     | *Yes* |       |
|       |       |       |       | pport | 3\~13 |       |       |
|       |       |       |       | of    | diff  |       |       |
|       |       |       |       | mul   | erent |       |       |
|       |       |       |       | tiple | comp  |       |       |
|       |       |       |       | diff  | onent |       |       |
|       |       |       |       | erent | ca    |       |       |
|       |       |       |       | band  | rrier |       |       |
|       |       |       |       | width | band  |       |       |
|       |       |       |       | v     | width |       |       |
|       |       |       |       | alues | va    |       |       |
|       |       |       |       | ^(4)^ | lues* |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| ^(1)^ |       |       |       |       |       |       |       |
| As    |       |       |       |       |       |       |       |
| de    |       |       |       |       |       |       |       |
| fined |       |       |       |       |       |       |       |
| in    |       |       |       |       |       |       |       |
| R     |       |       |       |       |       |       |       |
| eport |       |       |       |       |       |       |       |
| ITU-R |       |       |       |       |       |       |       |
| M.24  |       |       |       |       |       |       |       |
| 10-0. |       |       |       |       |       |       |       |
|       |       |       |       |       |       |       |       |
| ^(2)^ |       |       |       |       |       |       |       |
| Acco  |       |       |       |       |       |       |       |
| rding |       |       |       |       |       |       |       |
| to    |       |       |       |       |       |       |       |
| the   |       |       |       |       |       |       |       |
| evalu |       |       |       |       |       |       |       |
| ation |       |       |       |       |       |       |       |
| m     |       |       |       |       |       |       |       |
| ethod |       |       |       |       |       |       |       |
| ology |       |       |       |       |       |       |       |
| spec  |       |       |       |       |       |       |       |
| ified |       |       |       |       |       |       |       |
| in    |       |       |       |       |       |       |       |
| R     |       |       |       |       |       |       |       |
| eport |       |       |       |       |       |       |       |
| ITU-R |       |       |       |       |       |       |       |
| M.24  |       |       |       |       |       |       |       |
| 12-0. |       |       |       |       |       |       |       |
|       |       |       |       |       |       |       |       |
| ^(3)^ |       |       |       |       |       |       |       |
| Propo |       |       |       |       |       |       |       |
| nents |       |       |       |       |       |       |       |
| s     |       |       |       |       |       |       |       |
| hould |       |       |       |       |       |       |       |
| r     |       |       |       |       |       |       |       |
| eport |       |       |       |       |       |       |       |
| their |       |       |       |       |       |       |       |
| sel   |       |       |       |       |       |       |       |
| ected |       |       |       |       |       |       |       |
| evalu |       |       |       |       |       |       |       |
| ation |       |       |       |       |       |       |       |
| m     |       |       |       |       |       |       |       |
| ethod |       |       |       |       |       |       |       |
| ology |       |       |       |       |       |       |       |
| of    |       |       |       |       |       |       |       |
| the   |       |       |       |       |       |       |       |
| Conne |       |       |       |       |       |       |       |
| ction |       |       |       |       |       |       |       |
| den   |       |       |       |       |       |       |       |
| sity, |       |       |       |       |       |       |       |
| the   |       |       |       |       |       |       |       |
| ch    |       |       |       |       |       |       |       |
| annel |       |       |       |       |       |       |       |
| model |       |       |       |       |       |       |       |
| va    |       |       |       |       |       |       |       |
| riant |       |       |       |       |       |       |       |
| used, |       |       |       |       |       |       |       |
| and   |       |       |       |       |       |       |       |
| evalu |       |       |       |       |       |       |       |
| ation |       |       |       |       |       |       |       |
| c     |       |       |       |       |       |       |       |
| onfig |       |       |       |       |       |       |       |
| urati |       |       |       |       |       |       |       |
| on(s) |       |       |       |       |       |       |       |
| with  |       |       |       |       |       |       |       |
| their |       |       |       |       |       |       |       |
| exact |       |       |       |       |       |       |       |
| v     |       |       |       |       |       |       |       |
| alues |       |       |       |       |       |       |       |
| (e.g. |       |       |       |       |       |       |       |
| an    |       |       |       |       |       |       |       |
| tenna |       |       |       |       |       |       |       |
| el    |       |       |       |       |       |       |       |
| ement |       |       |       |       |       |       |       |
| nu    |       |       |       |       |       |       |       |
| mber, |       |       |       |       |       |       |       |
| bandw |       |       |       |       |       |       |       |
| idth, |       |       |       |       |       |       |       |
| etc.) |       |       |       |       |       |       |       |
| per   |       |       |       |       |       |       |       |
| test  |       |       |       |       |       |       |       |
| en    |       |       |       |       |       |       |       |
| viron |       |       |       |       |       |       |       |
| ment, |       |       |       |       |       |       |       |
| and   |       |       |       |       |       |       |       |
| could |       |       |       |       |       |       |       |
| pr    |       |       |       |       |       |       |       |
| ovide |       |       |       |       |       |       |       |
| other |       |       |       |       |       |       |       |
| rel   |       |       |       |       |       |       |       |
| evant |       |       |       |       |       |       |       |
| i     |       |       |       |       |       |       |       |
| nform |       |       |       |       |       |       |       |
| ation |       |       |       |       |       |       |       |
| as    |       |       |       |       |       |       |       |
| well. |       |       |       |       |       |       |       |
| For   |       |       |       |       |       |       |       |
| det   |       |       |       |       |       |       |       |
| ails, |       |       |       |       |       |       |       |
| refer |       |       |       |       |       |       |       |
| to    |       |       |       |       |       |       |       |
| R     |       |       |       |       |       |       |       |
| eport |       |       |       |       |       |       |       |
| ITU-R |       |       |       |       |       |       |       |
| M.24  |       |       |       |       |       |       |       |
| 12-0, |       |       |       |       |       |       |       |
| in    |       |       |       |       |       |       |       |
| p     |       |       |       |       |       |       |       |
| artic |       |       |       |       |       |       |       |
| ular, |       |       |       |       |       |       |       |
| §     |       |       |       |       |       |       |       |
| 7.1.3 |       |       |       |       |       |       |       |
| for   |       |       |       |       |       |       |       |
| the   |       |       |       |       |       |       |       |
| evalu |       |       |       |       |       |       |       |
| ation |       |       |       |       |       |       |       |
| meth  |       |       |       |       |       |       |       |
| odolo |       |       |       |       |       |       |       |
| gies, |       |       |       |       |       |       |       |
| § 8.4 |       |       |       |       |       |       |       |
| for   |       |       |       |       |       |       |       |
| the   |       |       |       |       |       |       |       |
| evalu |       |       |       |       |       |       |       |
| ation |       |       |       |       |       |       |       |
| conf  |       |       |       |       |       |       |       |
| igura |       |       |       |       |       |       |       |
| tions |       |       |       |       |       |       |       |
| per   |       |       |       |       |       |       |       |
| each  |       |       |       |       |       |       |       |
| test  |       |       |       |       |       |       |       |
| en    |       |       |       |       |       |       |       |
| viron |       |       |       |       |       |       |       |
| ment, |       |       |       |       |       |       |       |
| and   |       |       |       |       |       |       |       |
| Annex |       |       |       |       |       |       |       |
| 1 on  |       |       |       |       |       |       |       |
| the   |       |       |       |       |       |       |       |
| ch    |       |       |       |       |       |       |       |
| annel |       |       |       |       |       |       |       |
| model |       |       |       |       |       |       |       |
| vari  |       |       |       |       |       |       |       |
| ants. |       |       |       |       |       |       |       |
|       |       |       |       |       |       |       |       |
| ^(4)^ |       |       |       |       |       |       |       |
| Refer |       |       |       |       |       |       |       |
| to §  |       |       |       |       |       |       |       |
| 7.3.1 |       |       |       |       |       |       |       |
| of    |       |       |       |       |       |       |       |
| R     |       |       |       |       |       |       |       |
| eport |       |       |       |       |       |       |       |
| ITU-R |       |       |       |       |       |       |       |
| M.24  |       |       |       |       |       |       |       |
| 12-0. |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+

[^1]: Developed by 3GPP as 5G, Release 15 and beyond.

[^2]: If a proponent determines that a specific question does not apply,
    the proponent should indicate that this is the case and provide a
    rationale for why it does not apply.
