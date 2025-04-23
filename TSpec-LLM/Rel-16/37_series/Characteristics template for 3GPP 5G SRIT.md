Characteristics template for 3GPP 5G SRIT (Release 15 and beyond)
-----------------------------------------------------------------

The description templates provided by 3GPP are for the description of
the characteristics of 5G[^1] developed by 3GPP. It includes one
characteristics template for SRIT (encompassing NR and LTE), and one
characteristics template for NR RIT.

This document provides the characteristics template for the description
of the characteristics of the SRIT which consists of two component RITs
"NR" and "LTE", based on 3GPP Rel-15 and Rel-16 work.

For this characteristics template, 3GPP has addressed all of the
characteristics, and it is expected that these descriptions are helpful
to assist in evaluation activities for independent evaluation groups, as
well as to facilitate the understanding of the state-of-art of 3GPP
development on the SRIT.

+------------------+--------------------------------------------------+
| Item             | Item to be described                             |
+==================+==================================================+
| **5.2.3.2.1**    | **Test environment(s)**                          |
+------------------+--------------------------------------------------+
| 5.2.3.2.1.1      | What test environments (described in Report      |
|                  | ITU-R M.2412-0) does this technology description |
|                  | template address?                                |
|                  |                                                  |
|                  | *This proposal addresses all the five test       |
|                  | environments across the three usage scenarios    |
|                  | (eMBB, mMTC, and URLLC) as described in Report   |
|                  | ITU-R M.2412-0.*                                 |
+------------------+--------------------------------------------------+
| **5.2.3.2.2**    | **Radio interface functional aspects**           |
+------------------+--------------------------------------------------+
| 5.2.3.2.2.1      | *Multiple access schemes*                        |
|                  |                                                  |
|                  | Which access scheme(s) does the proposal use?    |
|                  | Describe in detail the multiple access schemes   |
|                  | employed with their main parameters.             |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | -   ***Downlink and Uplink:***                   |
|                  |                                                  |
|                  | > *The multiple access is a combination of*      |
|                  |                                                  |
|                  | -   ***OFDMA**: Synchronous/scheduling-based;    |
|                  |     > the transmission to/from different UEs     |
|                  |     > uses mutually orthogonal frequency         |
|                  |     > assignments.* *Granularity in frequency    |
|                  |     > assignment: One resource block consisting  |
|                  |     > of 12 subcarriers. Multiple sub-carrier    |
|                  |     > spacings are supported including 15kHz,    |
|                  |     > 30kHz, 60kHz and 120kHz for data (see Item |
|                  |     > 5.2.3.2.7 and reference therein).*         |
|                  |                                                  |
|                  |     -   *CP-OFDM is applied for both downlink    |
|                  |         and uplink. DFT-spread OFDM can also be  |
|                  |         configured for uplink.*                  |
|                  |                                                  |
|                  |     -   *Spectral confinement technique(s) (e.g. |
|                  |         filtering, windowing, etc.) for a        |
|                  |         waveform at the transmitter is           |
|                  |         transparent to the receiver. When such   |
|                  |         confinement techniques are used, the     |
|                  |         spectral utilization ratio can be        |
|                  |         enhanced.*                               |
|                  |                                                  |
|                  | -   ***TDMA**: Transmission to/from different    |
|                  |     > UEs with separation in time. Granularity:  |
|                  |     > One slot consisting of 14 OFDM symbols, or |
|                  |     > 2\~13 OFDM symbols non-slot (for DL) or    |
|                  |     > 1\~13 OFDM symbols (for UL) within one     |
|                  |     > slot. The physical length of one slot      |
|                  |     > ranges from 0.125ms to 1ms depending on    |
|                  |     > the sub-carrier spacing (for more details  |
|                  |     > on the frame structure, see Item 5.2.3.2.7 |
|                  |     > and the references therein).*              |
|                  |                                                  |
|                  | -   ***CDMA**: Inter-cell interference           |
|                  |     > suppressed by processing gain of channel   |
|                  |     > coding allowing for a frequency reuse of   |
|                  |     > one (for more details on channel-coding,   |
|                  |     > see Item 5.2.3.2.2.3 and the reference     |
|                  |     > therein).*                                 |
|                  |                                                  |
|                  | -   ***SDMA**: Possibility to transmit to/from   |
|                  |     > multiple users using the same              |
|                  |     > time/frequency resource (SDMA a.k.a.       |
|                  |     > "multi-user MIMO") as part of the          |
|                  |     > advanced-antenna capabilities (for more    |
|                  |     > details on the advanced-antenna            |
|                  |     > capabilities, see Item 5.2.3.2.9 and the   |
|                  |     > reference therein)*                        |
|                  |                                                  |
|                  | > *At least an UL transmission scheme without    |
|                  | > scheduling grant is supported.*                |
|                  |                                                  |
|                  | *(Note: Synchronous means that timing offset     |
|                  | between UEs is within cyclic prefix by e.g.      |
|                  | timing alignment.)*                              |
|                  |                                                  |
|                  | [***For LTE*** ***component RIT:***]{.underline} |
|                  |                                                  |
|                  | -   ***Downlink and Uplink:***                   |
|                  |                                                  |
|                  | > *The multiple access is a combination of*      |
|                  |                                                  |
|                  | -   ***OFDMA**: Synchronous/scheduling-based is  |
|                  |     > supported for both DL and UL; the          |
|                  |     > transmission to/from different UEs uses    |
|                  |     > mutually orthogonal frequency assignments. |
|                  |     > In addition, non-orthogonal multiple       |
|                  |     > access is supported for DL (known as MUST, |
|                  |     > see \[36.211\] sub-clause 7.1.2 for more   |
|                  |     > details). Granularity in frequency         |
|                  |     > assignment: For the UL: 3, 6 or 12         |
|                  |     > sub-carriers with a sub-carrier spacing of |
|                  |     > 15 kHz. For the DL: One resource block     |
|                  |     > consisting of 12 subcarriers. Sub-carrier  |
|                  |     > spacings of 15kHz is supported for         |
|                  |     > uni-cast data and subcarrier spacings of   |
|                  |     > 15kHz, 7.5kHz and 1.25kHz are supported    |
|                  |     > for multi-cast data (see Item 5.2.3.2.7    |
|                  |     > and reference therein).*                   |
|                  |                                                  |
|                  |     -   *CP-OFDM is applied for downlink.        |
|                  |         DFT-spread OFDM is applied for uplink.*  |
|                  |                                                  |
|                  | -   ***TDMA**: Transmission to/from different    |
|                  |     > UEs with separation in time. Granularity:  |
|                  |     > One subframe of length 1 ms, or slot of 7  |
|                  |     > OFDM symbols (0.5ms), or sub-slot of       |
|                  |     > length 2\~3 OFDM symbols                   |
|                  |     > (0.143ms\~0.214ms) (for more details on    |
|                  |     > the frame structure, see Item 5.2.3.2.7    |
|                  |     > and the references therein). Repetition of |
|                  |     > a transmission is supported.*              |
|                  |                                                  |
|                  | -   ***CDMA**: Inter-cell interference           |
|                  |     > suppressed by processing gain of channel   |
|                  |     > coding allowing for a frequency reuse of   |
|                  |     > one (for more details on channel-coding,   |
|                  |     > see Item 5.2.3.2.2.3 and the reference     |
|                  |     > therein).*                                 |
|                  |                                                  |
|                  | -   ***SDMA**: Possibility to transmit to/from   |
|                  |     > multiple users using the same              |
|                  |     > time/frequency resource (SDMA a.k.a.       |
|                  |     > "multi-user MIMO") as part of the          |
|                  |     > advanced-antenna capabilities (for more    |
|                  |     > details on the advanced-antenna            |
|                  |     > capabilities, see Item 5.2.3.2.9 and the   |
|                  |     > reference therein)*                        |
|                  |                                                  |
|                  | > *For NB-IoT, the multiple access is a          |
|                  | > combination of OFDMA, TDMA and CDMA, where     |
|                  | > OFDMA and TDMA are as follows*                 |
|                  |                                                  |
|                  | -   ***OFDMA:***                                 |
|                  |                                                  |
|                  |     -   *UL: DFT-spread OFDM. Granularity in     |
|                  |         frequency domain: A single sub-carrier   |
|                  |         with either 3.75 kHz or 15 kHz           |
|                  |         sub-carrier spacing, or 3, 6, or 12      |
|                  |         sub-carriers with a sub-carrier spacing  |
|                  |         of 15 kHz. A resource block consists of  |
|                  |         12 sub-carriers with 15 kHz sub-carrier  |
|                  |         spacing, or 48 sub-carriers with 3.75    |
|                  |         kHz sub-carrier spacing → 180 kHz.*      |
|                  |                                                  |
|                  |     -   *DL: Granularity in frequency domain:    |
|                  |         one resource block consisting of 6 or 12 |
|                  |         subcarriers with 15 kHz sub-carrier      |
|                  |         spacing→90 or 180 kHz*                   |
|                  |                                                  |
|                  | -   ***TDMA:** Transmission to/from different    |
|                  |     > UEs with separation in time*               |
|                  |                                                  |
|                  |     -   *UL: Granularity: One resource unit of 1 |
|                  |         ms, 2 ms, 4 ms, 8 ms, with 15 kHz        |
|                  |         sub-carrier spacing, depending on        |
|                  |         allocated number of sub-carrier(s); or   |
|                  |         32 ms with 3.75 kHz sub-carrier spacing  |
|                  |         (for more details on the frame           |
|                  |         structure, see Item 5.2.3.2.7 and the    |
|                  |         references therein)*                     |
|                  |                                                  |
|                  |     -   *DL: Granularity: One resource unit      |
|                  |         (subframe) of length 1 ms.*              |
|                  |                                                  |
|                  |     -   *Repetition of a transmission is         |
|                  |         supported.*                              |
+------------------+--------------------------------------------------+
| 5.2.3.2.2.2      | *Modulation scheme*                              |
+------------------+--------------------------------------------------+
| 5.2.3.2.2.2.1    | What is the baseband modulation scheme? If both  |
|                  | data modulation and spreading modulation are     |
|                  | required, describe in detail.                    |
|                  |                                                  |
|                  | Describe the modulation scheme employed for data |
|                  | and control information.                         |
|                  |                                                  |
|                  | What is the symbol rate after modulation?        |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | -   ***Downlink:***                              |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   *For both data and higher-layer control      |
|                  |     > information: QPSK, 16QAM, 64QAM and 256QAM |
|                  |     > (see \[38.211\] sub-clause 7.3.1.2).*      |
|                  |                                                  |
|                  | -   *L1/L2 control: QPSK (see \[38.211\]         |
|                  |     > sub-clause 7.3.2.4).*                      |
|                  |                                                  |
|                  | -   *Symbol rate: 1344ksymbols/s per 1440kHz     |
|                  |     > resource block (equivalently 168ksymbols/s |
|                  |     > per 180kHz resource block)*                |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   ***Uplink:***                                |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   *For both data and higher-layer control      |
|                  |     > information: π/2-BPSK (when precoding is   |
|                  |     > enabled), QPSK, 16QAM, 64QAM and 256QAM    |
|                  |     > (see \[38.211\] sub-clause 6.3.1.2).*      |
|                  |                                                  |
|                  | -   *L1/L2 control: BPSK, π/2-BPSK, QPSK (see    |
|                  |     > \[38.211\] sub-clause 6.3.2).*             |
|                  |                                                  |
|                  | -   *Symbol rate: 1344ksymbols/s per 1440kHz     |
|                  |     > resource block (equivalently 168ksymbols/s |
|                  |     > per 180kHz resource block)*                |
|                  |                                                  |
|                  | *The above is at least applied to eMBB.*         |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | -   ***Downlink:***                              |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   *For both data and higher-layer control      |
|                  |     > information: QPSK, 16QAM, 64QAM and 256QAM |
|                  |     > (see \[36.211\] sub-clause 6.3.2). 1024QAM |
|                  |     > is being specified.*                       |
|                  |                                                  |
|                  | -   *L1/L2 control: QPSK (see \[36.211\]         |
|                  |     > sub-clauses 6.7.2, 6.8.3, and 6.8A.3)*     |
|                  |                                                  |
|                  | -   *Symbol rate: 168ksymbols/s per 180kHz       |
|                  |     > resource block*                            |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   ***Uplink:***                                |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   *For both data and higher-layer control      |
|                  |     > information: π/2-BPSK, QPSK, 16QAM, 64QAM  |
|                  |     > and 256QAM are supported (see \[36.211\]   |
|                  |     > sub-clause 5.3.2).*                        |
|                  |                                                  |
|                  | -   *L1/L2 control: BPSK, QPSK (see \[36.211\]   |
|                  |     > sub-clause 5.4)*                           |
|                  |                                                  |
|                  | -   *Symbol rate: 168ksymbols/s per 180kHz       |
|                  |     > resource block. For UL, less than one      |
|                  |     > resource block may be allocated.*          |
|                  |                                                  |
|                  | *For NB-IoT, the modulation scheme is as         |
|                  | follows.*                                        |
|                  |                                                  |
|                  | -   *Data and higher-layer control: π/2-BPSK     |
|                  |     (uplink only), π/4-QPSK (uplink only), QPSK* |
|                  |                                                  |
|                  | -   *L1/L2 control: π/2-BPSK (uplink), QPSK      |
|                  |     (downlink)*                                  |
|                  |                                                  |
|                  | *Symbol rate: 168 ksymbols/s per 180 kHz         |
|                  | resource block. For UL, less than one resource   |
|                  | block may be allocated.*                         |
+------------------+--------------------------------------------------+
| 5.2.3.2.2.2.2    | *PAPR*                                           |
|                  |                                                  |
|                  | What is the RF peak to average power ratio after |
|                  | baseband filtering (dB)? Describe the PAPR       |
|                  | (peak-to-average power ratio) reduction          |
|                  | algorithms if they are used in the proposed      |
|                  | RIT/SRIT.                                        |
|                  |                                                  |
|                  | *The PAPR depends on the waveform and the number |
|                  | of component carriers. The single component      |
|                  | carrier transmission is assumed herein when      |
|                  | providing the PAPR. For DFT-spread OFDM, PAPR    |
|                  | would depend on modulation scheme as well.*      |
|                  |                                                  |
|                  | *For uplink using DFT-spread OFDM, the cubic     |
|                  | metric (CM) can also be used as one of the       |
|                  | methods of predicting the power de-rating from   |
|                  | signal modulation characteristics, if needed.*   |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | -   ***Downlink:***                              |
|                  |                                                  |
|                  | > *The PAPR is 8.4dB (99.9%)*                    |
|                  |                                                  |
|                  | -   ***Uplink:***                                |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   *For CP-OFDM:*                               |
|                  |                                                  |
|                  | > *The PAPR is 8.4dB (99.9%)*                    |
|                  |                                                  |
|                  | -   *For DFT-spread OFDM:*                       |
|                  |                                                  |
|                  | > *The PAPR is provided in the table below.*     |
|                  |                                                  |
|                  | <table>                                          |
|                  | <thead>                                          |
|                  | <tr class="header">                              |
|                  | <th>Modulation</th>                              |
|                  | <th><em>π</em>/2 BPSK</th>                       |
|                  | <th>QPSK</th>                                    |
|                  | <th>16QAM</th>                                   |
|                  | <th>64QAM</th>                                   |
|                  | <th>256QAM</th>                                  |
|                  | </tr>                                            |
|                  | </thead>                                         |
|                  | <tbody>                                          |
|                  | <tr class="odd">                                 |
|                  | <td>PAPR (99.9%)</td>                            |
|                  | <td>4.5 dB</td>                                  |
|                  | <td>5.8 dB</td>                                  |
|                  | <td>6.5 dB</td>                                  |
|                  | <td>6.6 dB</td>                                  |
|                  | <td>6.7 dB</td>                                  |
|                  | </tr>                                            |
|                  | <tr class="even">                                |
|                  | <td><p>CM</p>                                    |
|                  | <p>(99.9%)</p></td>                              |
|                  | <td>0.3 dB</td>                                  |
|                  | <td>1.2 dB</td>                                  |
|                  | <td>2.1 dB</td>                                  |
|                  | <td>2.3 dB</td>                                  |
|                  | <td>2.4 dB</td>                                  |
|                  | </tr>                                            |
|                  | </tbody>                                         |
|                  | </table>                                         |
|                  |                                                  |
|                  | > *Note: The above values are derived without    |
|                  | > spectrum shaping. When spectrum shaping is     |
|                  | > considered for π/2 BPSK, lower PAPR and CM     |
|                  | > values can be derived, e.g., 1.75dB PAPR for   |
|                  | > π/2 BPSK, based on the trade-off between PAPR  |
|                  | > and demodulation performance.*                 |
|                  |                                                  |
|                  | *Spectrum shaping can be used for a user with    |
|                  | π/2 BPSK DFT-S-OFDM for above 24 GHz.*           |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | -   ***Downlink:***                              |
|                  |                                                  |
|                  | > *The PAPR is 8.4dB (99.9%).*                   |
|                  |                                                  |
|                  | -   ***Uplink:***                                |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   *For DFT-spread OFDM:*                       |
|                  |                                                  |
|                  | > *The PAPR is provided in the table below.*     |
|                  |                                                  |
|                  | <table>                                          |
|                  | <thead>                                          |
|                  | <tr class="header">                              |
|                  | <th>Modulation</th>                              |
|                  | <th><em>π</em>/2 BPSK</th>                       |
|                  | <th>QPSK</th>                                    |
|                  | <th>16QAM</th>                                   |
|                  | <th>64QAM</th>                                   |
|                  | <th>256QAM</th>                                  |
|                  | </tr>                                            |
|                  | </thead>                                         |
|                  | <tbody>                                          |
|                  | <tr class="odd">                                 |
|                  | <td>PAPR (99.9%)</td>                            |
|                  | <td>0.3 dB</td>                                  |
|                  | <td>5.8 dB</td>                                  |
|                  | <td>6.5 dB</td>                                  |
|                  | <td>6.6 dB</td>                                  |
|                  | <td>6.7 dB</td>                                  |
|                  | </tr>                                            |
|                  | <tr class="even">                                |
|                  | <td><p>CM</p>                                    |
|                  | <p>(99.9%)</p></td>                              |
|                  | <td></td>                                        |
|                  | <td>1.2 dB</td>                                  |
|                  | <td>2.1 dB</td>                                  |
|                  | <td>2.3 dB</td>                                  |
|                  | <td>2.4 dB</td>                                  |
|                  | </tr>                                            |
|                  | </tbody>                                         |
|                  | </table>                                         |
|                  |                                                  |
|                  | *For NB-IoT,*                                    |
|                  |                                                  |
|                  | -   ***Downlink:***                              |
|                  |                                                  |
|                  | > *The PAPR is 8.0dB (99.9%) on 180kHz           |
|                  | > resource.*                                     |
|                  |                                                  |
|                  | -   ***Uplink:***                                |
|                  |                                                  |
|                  | > *The PAPR is 0.23 -- 5.6 dB (99.9 %) depending |
|                  | > on sub-carriers allocated for available NB-IoT |
|                  | > UL modulation.*                                |
|                  |                                                  |
|                  | ***[PAPR-reduction algorithm for NR and          |
|                  | LTE:]{.underline}***                             |
|                  |                                                  |
|                  | *Any PAPR-reduction algorithm is                 |
|                  | transmitter-implementation specific for uplink   |
|                  | and downlink.*                                   |
+------------------+--------------------------------------------------+
| 5.2.3.2.2.3      | *Error control coding scheme and interleaving*   |
+------------------+--------------------------------------------------+
| 5.2.3.2.2.3.1    | Provide details of error control coding scheme   |
|                  | for both downlink and uplink.                    |
|                  |                                                  |
|                  | For example,                                     |
|                  |                                                  |
|                  | -- FEC or other schemes?                         |
|                  |                                                  |
|                  | The proponents can provide additional            |
|                  | information on the decoding schemes.             |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | -   ***Downlink and Uplink:***                   |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   *For data: BG\#1 and BG\#2 based Low density |
|                  |     > parity check (LDPC) coding, combined with  |
|                  |     > rate matching based on                     |
|                  |     > shortening/puncturing/repetition to        |
|                  |     > achieve a desired overall code rate (For   |
|                  |     > more details, see \[38.212\] sub-clauses   |
|                  |     > 5.3.2). LDPC channel coder facilitates     |
|                  |     > low-latency and high-throughput decoder    |
|                  |     > implementations.*                          |
|                  |                                                  |
|                  | -   *For L1/L2 control: For DCI (Downlink        |
|                  |     > Control Information)/UCI (Uplink Control   |
|                  |     > Information) size larger than 11 bits,     |
|                  |     > Polar coding, combined with rate matching  |
|                  |     > based on shortening/puncturing/repetition  |
|                  |     > to achieve a desired overall code rate     |
|                  |     > (For more details, see \[38.212\]          |
|                  |     > sub-clauses 5.3.1). Otherwise, repetition  |
|                  |     > for 1-bit; simplex coding for 2-bit;       |
|                  |     > Reed-Muller coding for 3\~11-bit DCI/UCI   |
|                  |     > size.*                                     |
|                  |                                                  |
|                  | *The above scheme is at least applied to eMBB.*  |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | -   ***Downlink and Uplink:***                   |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   *For data:* *Rate 1/3 Turbo coding, combined |
|                  |     > with rate matching based on                |
|                  |     > puncturing/repetition to achieve a desired |
|                  |     > overall code rate. One transport block can |
|                  |     > be mapped to one or multiple resource      |
|                  |     > units. (For more details, see \[36.212\]   |
|                  |     > sub-clauses 5.1.3.2)*                      |
|                  |                                                  |
|                  | -   *For L1/L2 control: Rate-1/3 tail-biting     |
|                  |     > convolutional coding. Special block codes  |
|                  |     > for some L1/L2 control signaling (For more |
|                  |     > details, see \[36.212\] sub-clauses        |
|                  |     > 5.1.3.1)*                                  |
|                  |                                                  |
|                  | *For NB-IoT, the coding scheme is as follows:*   |
|                  |                                                  |
|                  | -   *For data: Rate 1/3 Turbo coding in UL, and  |
|                  |     > rate-1/3 tail-biting convolutional coding  |
|                  |     > in DL, each combined with rate matching    |
|                  |     > based on puncturing/repetition to achieve  |
|                  |     > a desired overall code rate; one transport |
|                  |     > block can be mapped to one or multiple     |
|                  |     > resource units (for more details, see      |
|                  |     > \[36.212\] sub-clause 6.2)*                |
|                  |                                                  |
|                  | -   *For L1/L2 control: The same as above.*      |
|                  |                                                  |
|                  | ***[Decoding schemes for NR and                  |
|                  | LTE:]{.underline}***                             |
|                  |                                                  |
|                  | *Decoding mechanism is receiver-implementation   |
|                  | specific. Example of information on the decoding |
|                  | mechanism will be provided together with self    |
|                  | evaluation.*                                     |
+------------------+--------------------------------------------------+
| 5.2.3.2.2.3.2    | Describe the bit interleaving scheme for both    |
|                  | uplink and downlink.                             |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | -   ***Downlink:***                              |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   *For data:* *bit interleaver is performed    |
|                  |     > for LDPC coding after rate-matching (For   |
|                  |     > more details, see \[38.212\] sub-clauses   |
|                  |     > 5.4.2.2)*                                  |
|                  |                                                  |
|                  | -   *For L1/L2 control: Bit interleaving is      |
|                  |     > performed as part of the encoding process  |
|                  |     > for Polar coding (For more details, see    |
|                  |     > \[38.212\] sub-clauses 5.4.1.1)*           |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   ***Uplink:***                                |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   *For data: bit interleaver is performed for  |
|                  |     > LDPC coding after rate-matching (For more  |
|                  |     > details, see \[38.212\] sub-clauses        |
|                  |     > 5.4.2.2)*                                  |
|                  |                                                  |
|                  | -   *For L1/L2 control: Bit interleaving is      |
|                  |     > performed for Polar coding after           |
|                  |     > rate-matching (For more details, see       |
|                  |     > \[38.212\] sub-clauses 5.4.1.3)*           |
|                  |                                                  |
|                  | *The above scheme is at least applied to eMBB.*  |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | -   ***Downlink and Uplink:***                   |
|                  |                                                  |
|                  | > *Bit interleaving is performed as part of the  |
|                  | > encoding/rate-matching process, see \[36.212\] |
|                  | > sub-clauses 5.1.3 and 5.1.4 for more details.* |
|                  |                                                  |
|                  | *Additional interleaving is performed in uplink, |
|                  | see \[36.212\] sub-clause 5.2.2.8 for more       |
|                  | details.*                                        |
+------------------+--------------------------------------------------+
| **5.2.3.2.3**    | **Describe channel tracking capabilities         |
|                  | (e.g. channel tracking algorithm, pilot symbol   |
|                  | configuration, etc.) to accommodate rapidly      |
|                  | changing delay spread profile.**                 |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | ***To support channel tracking, different types  |
|                  | of reference signals can be transmitted on       |
|                  | downlink and uplink respectively.***             |
|                  |                                                  |
|                  | -   ***Downlink:***                              |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   ***Primary and Secondary Synchronization     |
|                  |     signals (PSS and SSS)** are transmitted      |
|                  |     periodically to the cell. The periodicity of |
|                  |     these signals is network configurable. UEs   |
|                  |     can detect and maintain the cell timing      |
|                  |     based on these signals. If the gNB           |
|                  |     implements hybrid beamforming, then the PSS  |
|                  |     and SSS are transmitted separately to each   |
|                  |     analogue beam.* *Network can configure       |
|                  |     multiple PSS and SSS in frequency domain.*   |
|                  |                                                  |
|                  | -   ***UE-specific Demodulation RS (DM-RS)** for |
|                  |     PDCCH can be used for downlink channel       |
|                  |     estimation for coherent demodulation of      |
|                  |     PDCCH (Physical Downlink Control Channel).   |
|                  |     DM-RS for PDCCH is transmitted together with |
|                  |     the PDCCH.*                                  |
|                  |                                                  |
|                  | -   ***UE-specific Demodulation RS (DM-RS)** for |
|                  |     PDSCH can be used for downlink channel       |
|                  |     estimation for coherent demodulation of      |
|                  |     PDSCH (Physical Downlink Shared Channel).    |
|                  |     DM-RS for PDSCH is transmitted together with |
|                  |     the PDSCH.*                                  |
|                  |                                                  |
|                  | -   ***UE-specific Phase Tracking RS (PT-RS)**   |
|                  |     can be used in addition to the DM-RS for     |
|                  |     PDSCH for correcting common phase error      |
|                  |     between PDSCH symbols not containing DM-RS.  |
|                  |     It may also be used for Doppler and time     |
|                  |     varying channel tracking. PT-RS for PDSCH is |
|                  |     transmitted together with the PDSCH upon     |
|                  |     need.*                                       |
|                  |                                                  |
|                  | -   ***UE-specific Channel State Information RS  |
|                  |     (CSI-RS)** can be used for estimation of     |
|                  |     channel-state information (CSI) to further   |
|                  |     prepare feedback reporting to gNB to assist  |
|                  |     in MCS selection, beamforming, MIMO rank     |
|                  |     selection and resource allocation. CSI-RS    |
|                  |     transmissions are transmitted periodically,  |
|                  |     aperiodically, and semi-persistently on a    |
|                  |     configurable rate by the gNB. CSI-RS also    |
|                  |     can be used for interference measurement and |
|                  |     fine frequency/time tracking purposes.*      |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   ***Uplink:***                                |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   ***UE-specific Demodulation RS (DM-RS)** for |
|                  |     PUCCH can be used for uplink channel         |
|                  |     estimation for coherent demodulation of      |
|                  |     PUCCH (Physical Uplink Control Channel).     |
|                  |     DM-RS for PUCCH is transmitted together with |
|                  |     the PUCCH.*                                  |
|                  |                                                  |
|                  | -   ***UE-specific Demodulation RS (DM-RS)** for |
|                  |     PUSCH can be used for uplink channel         |
|                  |     estimation for coherent demodulation of      |
|                  |     PUSCH (Physical Uplink Shared Channel).      |
|                  |     DM-RS for PUSCH is transmitted together with |
|                  |     the PUSCH.*                                  |
|                  |                                                  |
|                  | -   ***UE-specific Phase Tracking RS (PT-RS)**   |
|                  |     can be used in addition to the DM-RS for     |
|                  |     PUSCH for correcting common phase error      |
|                  |     between PUSCH symbols not containing DM-RS.  |
|                  |     It may also be used for Doppler and time     |
|                  |     varying channel tracking. DM-RS for PUSCH is |
|                  |     transmitted together with the PUSCH upon     |
|                  |     need.*                                       |
|                  |                                                  |
|                  | -   ***UE-specific Sounding RS (SRS)** can be    |
|                  |     used for estimation of uplink channel-state  |
|                  |     information to assist uplink scheduling,     |
|                  |     uplink power control, as well as assist the  |
|                  |     downlink transmission (e.g. the downlink     |
|                  |     beamforming in the scenario with UL/DL       |
|                  |     reciprocity). SRS transmissions are          |
|                  |     transmitted periodically,* *aperiodically,   |
|                  |     and semi-persistently by the UE on a gNB     |
|                  |     configurable rate.*                          |
|                  |                                                  |
|                  | *Details of channel-tracking/estimation          |
|                  | algorithms are receiver-implementation specific, |
|                  | and not part of the specification.*              |
|                  |                                                  |
|                  | [***For LTE*** ***component RIT:***]{.underline} |
|                  |                                                  |
|                  | -   ***Downlink:***                              |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   ***[Cell-specific RS]{.underline}** (CRS)    |
|                  |     are transmitted in every non-MBSFN subframe  |
|                  |     and over the entire frequency band unless    |
|                  |     Discovery Reference Signals are transmitted. |
|                  |     Up to four different CRS can be transmitted  |
|                  |     within a cell, with each CRS corresponding   |
|                  |     to one of up to four cell-specific antenna   |
|                  |     ports, referred to antenna port 0 to 3       |
|                  |     respectively.  The CRS can be used for       |
|                  |     downlink channel estimation for coherent     |
|                  |     demodulation of physical channels            |
|                  |     transmitted from antenna ports 0 to 3. The   |
|                  |     CRS can also be used to derive channel-state |
|                  |     information (CSI) for the corresponding      |
|                  |     antenna ports. The CSI can e.g. be used to   |
|                  |     assist scheduling (including link            |
|                  |     adaptation, precoder-matrix/vector           |
|                  |     selection, etc.). For the detailed structure |
|                  |     of CRS, see \[36.211\] sub-clause 6.10.1.*   |
|                  |                                                  |
|                  | -   ***[UE-specific RS]{.underline}** can be     |
|                  |     used for downlink channel estimation for     |
|                  |     coherent demodulation of PDSCH (Physical     |
|                  |     Downlink Shared Channel). Up to eight        |
|                  |     different UE-specific reference signals      |
|                  |     corresponding to up to eight layers can be   |
|                  |     transmitted from a UE point-of-view. In a    |
|                  |     given subframe, the UE-specific reference    |
|                  |     signals are only transmitted within the      |
|                  |     resource blocks that are used for PDSCH      |
|                  |     transmission to the specific UE within this  |
|                  |     subframe. For the detailed structure of      |
|                  |     UE-specific RS for the case of transmission  |
|                  |     from a single antenna port (a.k.a. antenna   |
|                  |     port 5), see \[36.211\] sub-clause 6.10.3.   |
|                  |     The structure for the case of transmission   |
|                  |     from multiple antenna ports is an extension  |
|                  |     of the structure for the case of a single    |
|                  |     antenna port.*                               |
|                  |                                                  |
|                  | -   ***[CSI-RS]{.underline}** can be used for    |
|                  |     estimation of channel-state information      |
|                  |     (CSI) to further prepare feedback reporting  |
|                  |     to eNB (CQI for link adaptation,             |
|                  |     precoder-matrix/vector selection, etc.) to   |
|                  |     assist beamforming and scheduling for up to  |
|                  |     eight layers of transmission. CSI-RS are     |
|                  |     transmitted periodically and aperiodically   |
|                  |     by the eNB. Periodic CSI-RS are transmitted  |
|                  |     in every Nth subframe, where N is            |
|                  |     configurable.*                               |
|                  |                                                  |
|                  | -   *[**Discovery Reference Signals**            |
|                  |     (DRS)]{.underline} are a combination of      |
|                  |     Primary and Secondary Synchronization        |
|                  |     Signals (PSS and SSS), CRS, and possibly     |
|                  |     CSI-RS. Discovery Reference Signals are      |
|                  |     transmitted in every Nth subframe, where N   |
|                  |     is configurable. Discovery Reference Signals |
|                  |     can be used for link-adaptation, precoder    |
|                  |     selection, and radio resource management     |
|                  |     related measurements in cases where CRS are  |
|                  |     not transmitted in every subframe to e.g.    |
|                  |     save power or reduce interference.*          |
|                  |                                                  |
|                  | -   *[**Narrowband Reference signals**           |
|                  |     (NRS)]{.underline} are used in NB-IoT. NRS   |
|                  |     are transmitted in a certain minimum set of  |
|                  |     subframes which depends on the in-band,      |
|                  |     guard-band, or standalone nature of the      |
|                  |     deployment, and additionally in a configured |
|                  |     set of subframes. NRS associated with        |
|                  |     paging, random access response, and          |
|                  |     multicast transmissions on non-anchor NB-IoT |
|                  |     carriers do not have to be transmitted on    |
|                  |     subframes far away from the associated       |
|                  |     transmissions, even if they are in the       |
|                  |     configured set of subframes. Up to two       |
|                  |     different NRS can be transmitted within a    |
|                  |     cell, with each NRS corresponding to one of  |
|                  |     up to two cell-specific antenna ports,       |
|                  |     referred to as antenna port 2000 to 2001     |
|                  |     respectively. The NRS can be used for        |
|                  |     downlink channel estimation for coherent     |
|                  |     demodulation of physical channels            |
|                  |     transmitted from antenna ports 2000 to 2001. |
|                  |     For the detailed structure of NRS, see       |
|                  |     \[36.211\] sub-clause 10.2.6.*               |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   ***Uplink:***                                |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   ***[Demodulation RS]{.underline}** (DMRS)    |
|                  |     can be used for channel estimation for       |
|                  |     coherent demodulation of the Physical Uplink |
|                  |     Shared Channel (PUSCH), and the Physical     |
|                  |     Uplink Control Channel (PUCCH). Uplink DMRS  |
|                  |     for demodulation of PUSCH are transmitted    |
|                  |     once every slot (twice every subframe) in    |
|                  |     the subframes in which PUSCH is being        |
|                  |     transmitted. Up to four uplink DMRS can be   |
|                  |     transmitted from a UE. The instantaneous     |
|                  |     bandwidth of the uplink DMRS equals the      |
|                  |     instantaneous bandwidth of the corresponding |
|                  |     PUSCH transmission.*                         |
|                  |                                                  |
|                  |     -   *For the detailed structure of uplink    |
|                  |         DMRS for PUSCH transmission for the case |
|                  |         of single antenna transmission, see      |
|                  |         \[36.211\] sub-clause 5.5.2.1. The       |
|                  |         structure for the case of transmission   |
|                  |         from multiple antenna ports is an        |
|                  |         extension of the structure for the case  |
|                  |         of a single antenna port.*               |
|                  |                                                  |
|                  | -   *For NB-IoT, uplink DMRS for demodulation of |
|                  |     NPUSCH are transmitted once every slot       |
|                  |     (twice every subframe) in the subframes in   |
|                  |     which NPUSCH is being transmitted. The       |
|                  |     instantaneous bandwidth of the uplink DMRS   |
|                  |     equals the instantaneous bandwidth of the    |
|                  |     corresponding NPUSCH transmission. One DMRS  |
|                  |     for NPUSCH transmission can be transmitted   |
|                  |     from a UE. For the detailed structure of     |
|                  |     uplink DMRS for NPUSCH transmission, see     |
|                  |     \[36.211\] sub-clause 10.1.4.*               |
|                  |                                                  |
|                  | -   ***[Sounding RS]{.underline}** (SRS) can be  |
|                  |     used for estimation of uplink channel-state  |
|                  |     information to assist uplink scheduling,     |
|                  |     uplink power control, and also assist        |
|                  |     downlink transmissions (e.g. downlink        |
|                  |     beamforming in scenarios with UL/DL          |
|                  |     reciprocity). Uplink SRS are transmitted     |
|                  |     either periodically every Nth subframe,      |
|                  |     where N is configurable, or aperiodically    |
|                  |     when triggered by the network. For the       |
|                  |     detailed structure of uplink SRS see         |
|                  |     \[36.211\] sub-clause 5.5.3.*                |
|                  |                                                  |
|                  | *Details of channel-tracking/estimation          |
|                  | algorithms are receiver-implementation specific, |
|                  | e.g. MMSE-based channel estimation with          |
|                  | appropriate interpolation in time and frequency  |
|                  | domain could be used.*                           |
+------------------+--------------------------------------------------+
| **5.2.3.2.4**    | **Physical channel structure and multiplexing**  |
+------------------+--------------------------------------------------+
| 5.2.3.2.4.1      | What is the physical channel bit rate (M or      |
|                  | Gbit/s) for supported bandwidths?                |
|                  |                                                  |
|                  | i.e., the product of the modulation symbol rate  |
|                  | (in symbols per second), bits per modulation     |
|                  | symbol, and the number of streams supported by   |
|                  | the antenna system.                              |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | ***The physical channel bit rate depends on the  |
|                  | modulation scheme, number of                     |
|                  | spatial-multiplexing layer, number of resource   |
|                  | blocks in the channel bandwidth and the          |
|                  | subcarrier spacing used. The physical channel    |
|                  | bit rate per layer can be expressed as***        |
|                  |                                                  |
|                  | ***R~layer~ = N**~mod~* x *N~RB~* *x* 2*^µ^* x   |
|                  | 168 *kbps*                                       |
|                  |                                                  |
|                  | *where*                                          |
|                  |                                                  |
|                  | -   ***N~mod~ is the number of bits per          |
|                  |     modulation symbol for the applied modulation |
|                  |     scheme (QPSK: 2, 16QAM: 4, 64QAM: 6,         |
|                  |     256QAM: 8)***                                |
|                  |                                                  |
|                  | -   ***N~RB~ is the number of resource blocks in |
|                  |     the aggregated frequency domain which        |
|                  |     depends on the channel bandwidth.***         |
|                  |                                                  |
|                  | -   ***µ depends on the subcarrier spacing,***   |
|                  |     $\mathrm{\Delta}f$*, given by*               |
|                  |     $\mat                                        |
|                  | hrm{\Delta}f = 2^{\mu} \bullet 15\ \left\lbrack  |
|                  | \text{kHz} \right\rbrack,\ \ \mu = 0,1,\ldots 3$ |
|                  |                                                  |
|                  | ***For example, a 400 MHz carrier with 264       |
|                  | resource blocks using 120 kHz subcarrier         |
|                  | spacing,*** $\mu = 3$*, and 256QAM modulation    |
|                  | results in a physical channel bit rate of 2.8    |
|                  | Gbit/s per layer.*                               |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | ***The physical channel bit rate depends on the  |
|                  | modulation scheme, number of                     |
|                  | spatial-multiplexing layers and number of        |
|                  | resource blocks in the channel bandwidth. and    |
|                  | the subcarrier spacing used. When the subcarrier |
|                  | spacing is 15 kHz, the physical channel bit rate |
|                  | per layer can be expressed as***                 |
|                  |                                                  |
|                  | ***R~layer~ = N**~mod~* x *N~RB~* x *168 kbps*   |
|                  |                                                  |
|                  | *where*                                          |
|                  |                                                  |
|                  | -   ***N~mod~ is the number of bits per          |
|                  |     modulation symbol for the applied modulation |
|                  |     scheme (QPSK: 2, 16QAM: 4, 64QAM: 6, 256QAM: |
|                  |     8, 1024QAM: 10)***                           |
|                  |                                                  |
|                  | -   ***N~RB~ is the number of resource blocks in |
|                  |     the aggregated frequency domain which        |
|                  |     depends on the channel bandwidth (e.g. N~RB~ |
|                  |     =25 for 5 MHz, N~RB~ =50 for 10 MHz, and     |
|                  |     N~RB~ =100 for 20 MHz. For channel bandwidth |
|                  |     larger than 20 MHz (carrier aggregation),    |
|                  |     the channel bit rate will scale              |
|                  |     accordingly.***                              |
|                  |                                                  |
|                  | ***NB-IoT only supports transmission of a single |
|                  | layer and the physical channel bit rate is as    |
|                  | above, but with N~mod~ limited to 1(BPSK) or 2   |
|                  | (QPSK) and** N~RB~**= 1. For MBMS, 1.25 kHz and  |
|                  | 7.5 kHz subcarrier spacing are also supported,   |
|                  | scaling the physical channel bit rate            |
|                  | accordingly.***                                  |
+------------------+--------------------------------------------------+
| 5.2.3.2.4.2      | *Layer 1 and Layer 2 overhead estimation.*       |
|                  |                                                  |
|                  | Describe how the RIT/SRIT accounts for all layer |
|                  | 1 (PHY) and layer 2 (MAC) overhead and provide   |
|                  | an accurate estimate that includes static and    |
|                  | dynamic overheads.                               |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | -   ***Downlink***                               |
|                  |                                                  |
|                  | *The downlink L1/L2 overhead includes:*          |
|                  |                                                  |
|                  | 1.  *Different types of reference signals*       |
|                  |                                                  |
|                  |     a.  *Demodulation reference signals for      |
|                  |         PDSCH (DMRS-PDSCH)*                      |
|                  |                                                  |
|                  |     b.  *Phase-tracking reference signals for    |
|                  |         PDSCH (PTRS-PDSCH)*                      |
|                  |                                                  |
|                  |     c.  *Demodulation reference signals for      |
|                  |         PDCCH*                                   |
|                  |                                                  |
|                  |     d.  *Reference signals specifically          |
|                  |         targeting estimation of channel-state    |
|                  |         information (CSI-RS)*                    |
|                  |                                                  |
|                  |     e.  *Tracking reference signals (TRS)*       |
|                  |                                                  |
|                  | 2.  *L1/L2 control signalling transmitted on the |
|                  |     up to three first OFDM symbols of each slot* |
|                  |                                                  |
|                  | 3.  *Synchronization signals and physical        |
|                  |     broadcast control channel including          |
|                  |     demodulation reference signals included in   |
|                  |     the SS/PBCH block*                           |
|                  |                                                  |
|                  | 4.  *PDU headers in L2 sub-layers                |
|                  |     (MAC/RLC/PDCP)*                              |
|                  |                                                  |
|                  | *The overhead due to different type of reference |
|                  | signals is given in the table below. Note that   |
|                  | demodulation reference signals for PDCCH is      |
|                  | included in the PDCCH overhead.*                 |
|                  |                                                  |
|                  |                                                  |
|                  | *Reference signal type*   *Example configuration |
|                  | s*                                               |
|                  |                                                  |
|                  |            *Overhead for example configurations* |
|                  |                                                  |
|                  | ------------------------- ---------------------- |
|                  | ------------------------------------------------ |
|                  | ------------------------------------------------ |
|                  | ---------- ------------------------------------- |
|                  | ------------------------------------------------ |
|                  |   *DMRS-PDSCH*                                   |
|                  | *As examples, DMRS can occupy 1/3, ½, or one ful |
|                  | l OFDM symbol. 1, 2, 3 or 4 symbols per slot can |
|                  |  be configured to carry DMRS.*   *2.4 % to 29 %* |
|                  |   *PTRS- PDSCH*             *1 resource eleme    |
|                  | nts in frequency domain every second or fourth r |
|                  | esource block. PTRS is mainly intended for FR2.* |
|                  |                 *0.2% or 0.5 % when configured.* |
|                  |   *CSI-RS*                  *1 resource element  |
|                  | per resource block per antenna port per CSI-RS p |
|                  | eriodicity*                                      |
|                  |              *0.25 % for 8 antenna ports transmi |
|                  | tted every 20 ms with 15 kHz subcarrier spacing* |
|                  |   *TRS*                                          |
|                  |   *2 slots with 1/2 symbol in each slot per tran |
|                  | smission period*                                 |
|                  |                                    *0.36 % or 0. |
|                  | 18% respectively for 20 ms and 40ms periodicity* |
|                  |                                                  |
|                  | *The overhead due to the L1/L2 control           |
|                  | signalling is depending on the size and          |
|                  | periodicity of the configured CORESET in the     |
|                  | cell and includes the overhead from the PDCCH    |
|                  | demodulation reference signals. If the CORESET   |
|                  | is transmitted in every slot, maximum control    |
|                  | channel overhead is 21% assuming three symbols   |
|                  | and whole carrier bandwidth used for CORESET,    |
|                  | while a more typical overhead is 7% when 1/3 of  |
|                  | the time and frequency resources in the first    |
|                  | three symbols of a slot is allocated to PDCCH.*  |
|                  |                                                  |
|                  | *The overhead due to the SS/PBCH block is given  |
|                  | by the number of SS/PBCH blocks transmitted      |
|                  | within the SS/PBCH block period, the SS/PBCH     |
|                  | block periodicity and the subcarrier spacing.    |
|                  | Assuming a 100 resource block wide carrier, the  |
|                  | overhead for 20 ms periodicity is in the range   |
|                  | of 0.6 % to 2.3 % if the maximum number of       |
|                  | SS/PBCH blocks are transmitted.*                 |
|                  |                                                  |
|                  | -   ***Uplink***                                 |
|                  |                                                  |
|                  | *[L1/L2 overhead includes:]{.underline}*         |
|                  |                                                  |
|                  | 1.  *Different types of reference signals*       |
|                  |                                                  |
|                  |     a.  *Demodulation reference signal for       |
|                  |         PUSCH*                                   |
|                  |                                                  |
|                  |     b.  *Demodulation reference signal for       |
|                  |         PUCCH*                                   |
|                  |                                                  |
|                  |     c.  *Phase-tracking reference signals*       |
|                  |                                                  |
|                  |     ```{=html}                                   |
|                  |     <!-- -->                                     |
|                  |     ```                                          |
|                  |     a.  *Sounding reference signal (SRS) used    |
|                  |         for uplink channel-state estimation at   |
|                  |         the network side*                        |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | 1.  *L1/L2 control signalling transmitted on a   |
|                  |     configurable amount of resources (see also   |
|                  |     Item 4.2.3.2.4.5)*                           |
|                  |                                                  |
|                  | 2.  *L2 control overhead due to e.g., random     |
|                  |     access, uplink time-alignment control, power |
|                  |     headroom reports and buffer-status reports*  |
|                  |                                                  |
|                  | 3.  *PDU headers in L2 layers (MAC/RLC/PDCP)*    |
|                  |                                                  |
|                  | *The overhead due to due to demodulation         |
|                  | reference signal for PUSCH is the same as the    |
|                  | overhead for demodulation reference signal for   |
|                  | PDSCH, i.e. 4 % to 29 % depending on number of   |
|                  | symbols configured. Also, the phase-tracking     |
|                  | reference signal overhead is the same in UL as   |
|                  | in DL.*                                          |
|                  |                                                  |
|                  | *The overhead due to periodic SRS is depending   |
|                  | on the number of symbols configured subcarrier   |
|                  | spacing and periodicity. For 20 ms periodicity,  |
|                  | the overhead is in the range of 0.4% to 1.4%     |
|                  | assuming15 kHz subcarrier spacing.*              |
|                  |                                                  |
|                  | *Amount of uplink resources reserved for random  |
|                  | access depends on the configuration.*            |
|                  |                                                  |
|                  | *The relative overhead due to uplink             |
|                  | time-alignment control depends on the            |
|                  | configuration and the number of active UEs       |
|                  | within a cell.*                                  |
|                  |                                                  |
|                  | *The amount of overhead for buffer status        |
|                  | reports depends on the configuration.*           |
|                  |                                                  |
|                  | *The amount of overhead caused by 4 highly       |
|                  | depends on the data packet size.*                |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | -   ***Downlink***                               |
|                  |                                                  |
|                  | *The downlink L1/L2 overhead includes:*          |
|                  |                                                  |
|                  | 1.  *Different types of reference signals*       |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | a)  *Cell-specific RS (CRS) transmitted within   |
|                  |     each resource block*                         |
|                  |                                                  |
|                  | b)  *UE-specific demodulation RS*                |
|                  |                                                  |
|                  | c)  *Reference signals specifically targeting    |
|                  |     estimation of channel-state information      |
|                  |     (CSI-RS)*                                    |
|                  |                                                  |
|                  | d)  *MBSFN reference signal*                     |
|                  |                                                  |
|                  | e)  *Positioning reference signals*              |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | 2.  *L1/L2 control signalling transmitted on the |
|                  |     up to three (four in case of 1.4 MHz         |
|                  |     bandwidth) first OFDM symbols of each        |
|                  |     subframe, except for short TTI operation     |
|                  |     where L1/L2 control signaling is also        |
|                  |     transmitted in OFDM symbols associated with  |
|                  |     the short TTI.*                              |
|                  |                                                  |
|                  | 3.  *Synchronization signal and physical         |
|                  |     > broadcast control channel*                 |
|                  |                                                  |
|                  | 4.  *PDU headers in L2 sub-layers                |
|                  |     > (MAC/RLC/PDCP)*                            |
|                  |                                                  |
|                  | *The combined overhead due to CRS (1a) and L1/L2 |
|                  | control signaling (2) depends on the number of   |
|                  | cell-specific antenna ports and the number of    |
|                  | OFDM symbols used for the L1/L2 control          |
|                  | signaling. Some examples, for the case of no     |
|                  | CSI-RS and no UE-specific RS, see 4.2.3.2.3      |
|                  | above, are shown below:*                         |
|                  |                                                  |
|                  | -   *1 antenna port for CRS and 1 symbol for     |
|                  |     > L1/L2 control: 10.7%*                      |
|                  |                                                  |
|                  | -   *1 antenna port for CRS and 3 symbols for    |
|                  |     > L1/L2 control: 25%*                        |
|                  |                                                  |
|                  | -   *4 antenna ports for CRS and 1 symbol for    |
|                  |     > L1/L2 control: 19%*                        |
|                  |                                                  |
|                  | -   *4 antenna ports for CRS and 3 symbols for   |
|                  |     > L1/L2 control: 31%*                        |
|                  |                                                  |
|                  | *The amount of overhead caused by                |
|                  | synchronization signals and broadcast            |
|                  | channel depends on operation bandwidth, and is   |
|                  | approximately 0.7% and 0.35%, for 10 and 20MHz   |
|                  | operation bandwidth, respectively.*              |
|                  |                                                  |
|                  | *The amount of overhead caused by L2 highly      |
|                  | depends on the data packet size, and is          |
|                  | approximately 2.7%, 0.51% and 0.32% for L1 data  |
|                  | rates of 1, 10 and 100 Mbit/s, respectively.*    |
|                  |                                                  |
|                  | *In a typical case, the relative overhead for    |
|                  | CSI-RS (if present) is estimated to 0.06% per    |
|                  | antenna port (0.48% for eight antenna ports).*   |
|                  |                                                  |
|                  | *The relative overhead due to UE-specific RS (if |
|                  | present) is estimated to be approximately 7% in  |
|                  | case of Rank 1 and Rank 2 transmission, and 14%  |
|                  | for Rank 3-8 transmission.*                      |
|                  |                                                  |
|                  | *In the case of operation with short TTI there   |
|                  | will be some additional overhead due to control  |
|                  | and reference signals.*                          |
|                  |                                                  |
|                  | *For eMTC*[^3]*, there will be some additional   |
|                  | overhead due to eMTC specific narrowband control |
|                  | channel and the need to accommodate wideband LTE |
|                  | control signalling.*                             |
|                  |                                                  |
|                  | *For NB-IoT, the overhead from Narrowband RS     |
|                  | (NRS) is dependent on the number of              |
|                  | cell-specific antenna ports N (1 or 2) and       |
|                  | equals 8 x N / 168 %.*                           |
|                  |                                                  |
|                  | *The overhead from NB-IoT downlink control       |
|                  | signaling is dependent on the amount of data to  |
|                  | be transmitted. For small infrequent data        |
|                  | transmissions, the downlink transmissions are    |
|                  | dominated by the L2 signaling during the         |
|                  | connection setup. The overhead from L1 signaling |
|                  | is dependent on the configured scheduling        |
|                  | cycle.*                                          |
|                  |                                                  |
|                  | *The overhead due to Narrowband synchronization  |
|                  | signal and Narrowband system information         |
|                  | broadcast messages is only applicable to the     |
|                  | NB-IoT anchor carrier. The actual overhead       |
|                  | depends on the broadcasted system information    |
|                  | messages and their periodicity. The overhead can |
|                  | be estimated to be around 26.25%.*               |
|                  |                                                  |
|                  | -   ***Uplink***                                 |
|                  |                                                  |
|                  | *[L1/L2 overhead includes:]{.underline}*         |
|                  |                                                  |
|                  | 1.  *Demodulation reference symbols used e.g.    |
|                  |     for uplink channel estimation for uplink     |
|                  |     coherent demodulation, transmitted once      |
|                  |     every 0.5 ms slot.*                          |
|                  |                                                  |
|                  | 2.  *Sounding reference signal (SRS) used for    |
|                  |     uplink channel-state estimation at the       |
|                  |     network side*                                |
|                  |                                                  |
|                  | 3.  *L1/L2 control signalling transmitted on     |
|                  |     configurable amount of resource blocks (see  |
|                  |     also Item 5.2.3.2.4.5)*                      |
|                  |                                                  |
|                  | 4.  *L2 control overhead due to e.g., random     |
|                  |     access, uplink time-alignment control, power |
|                  |     headroom reports and buffer-status reports*  |
|                  |                                                  |
|                  | 5.  *PDU headers in L2 layers (MAC/RLC/PDCP)*    |
|                  |                                                  |
|                  | *The amount of overhead caused by 1 is           |
|                  | approximately 14%, corresponding to one          |
|                  | DFTS-OFDM symbol in each slot. The relative      |
|                  | overhead is estimated to be independent of the   |
|                  | rank of the transmission. With short TTI the     |
|                  | DMRS overhead may increase.*                     |
|                  |                                                  |
|                  | *The amount of SRS overhead depends on the SRS   |
|                  | transmission interval, SRS bandwidth and the     |
|                  | usage of UpPTS for SRS. With a 10 msec SRS       |
|                  | transmission interval and full band SRS, the     |
|                  | relative overhead is approximately 0.7%*         |
|                  |                                                  |
|                  | *Amount of uplink resources reserved for random  |
|                  | access depends on the configuration.*            |
|                  |                                                  |
|                  | *A typical case with PRACH format 0 is six       |
|                  | resource blocks per radio frame, implying a      |
|                  | relative overhead of 0.6%, 1.2%, and 2.4% for a  |
|                  | channel bandwidth of 20 MHz, 10 MHz, and 5 MHz   |
|                  | respectively.*                                   |
|                  |                                                  |
|                  | *The relative overhead due to uplink             |
|                  | time-alignment control depends on the            |
|                  | configuration and the number of active UEs       |
|                  | within a cell. The absolute overhead is          |
|                  | typically less than 32 bps per UE.*              |
|                  |                                                  |
|                  | *The amount of overhead for buffer status        |
|                  | reports depends on the configuration. With       |
|                  | continuous data and a 10 - 20 ms reporting       |
|                  | interval the absolute overhead is 0.8-3.2 kbps.* |
|                  |                                                  |
|                  | *The amount of overhead caused by 5 highly       |
|                  | depends on the data packet size, and is          |
|                  | approximately 2.7%, 0,51% and 0,32% for L1 data  |
|                  | rates of 1, 10 and 100 Mbit/s, respectively.*    |
|                  |                                                  |
|                  | *Above overhead calculations are based on normal |
|                  | CP length.*                                      |
|                  |                                                  |
|                  | *For NB-IoT UL, data and control is sharing the  |
|                  | same resources and the overhead from L1/L2       |
|                  | control signaling depend on the scheduled        |
|                  | traffic in the DL. The UL control signaling is   |
|                  | dominated by RLC and HARQ positive or negative   |
|                  | acknowledgments. A typical NB-IoT NPRACH         |
|                  | overhead is in the order of 5 %.*                |
+------------------+--------------------------------------------------+
| 5.2.3.2.4.3      | *Variable bit rate capabilities:*                |
|                  |                                                  |
|                  | Describe how the proposal supports different     |
|                  | applications and services with various bit rate  |
|                  | requirements.                                    |
|                  |                                                  |
|                  | ***[For NR and LTE component                     |
|                  | RIT:]{.underline}***                             |
|                  |                                                  |
|                  | *For a given combination of modulation scheme,   |
|                  | code rate, and number of spatial-multiplexing    |
|                  | layers, the data rate available to a user can be |
|                  | controlled by the scheduler by assigning         |
|                  | different number of resource blocks for the      |
|                  | transmission. In case of multiple services, the  |
|                  | available/assigned resource, and thus the        |
|                  | available data rate, is shared between the       |
|                  | services.*                                       |
+------------------+--------------------------------------------------+
| 5.2.3.2.4.4      | *Variable payload capabilities:*                 |
|                  |                                                  |
|                  | Describe how the RIT/SRIT supports IP-based      |
|                  | application layer protocols/services (e.g.,      |
|                  | VoIP, video-streaming, interactive gaming, etc.) |
|                  | with variable-size payloads.                     |
|                  |                                                  |
|                  | *See also 5.2.3.2.4.3.*                          |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *The transport-block size can vary between X     |
|                  | bits and Y bits. The number of bits per          |
|                  | transport block can be set with a fine           |
|                  | granularity.*                                    |
|                  |                                                  |
|                  | *See \[38.214\] sub-clause 5.1.3.2 for details.* |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *The transport-block size can vary between 16    |
|                  | bits and 2\*391656 bits. The number of bits per  |
|                  | transport block can be assigned with a fine      |
|                  | granularity.*                                    |
|                  |                                                  |
|                  | *For eMTC, the maximum transport block size is   |
|                  | 1000 bits in both UL and DL(optionally 2984      |
|                  | bits) for the lowest UE category dedicated to    |
|                  | eMTC and 4008 bits and 6968 bits for DL and UL   |
|                  | respectively for the highest UE category         |
|                  | dedicated to eMTC.*                              |
|                  |                                                  |
|                  | *See \[36.213\] sub-clause 7.1.7.2.1 for         |
|                  | details.*                                        |
|                  |                                                  |
|                  | *For NB-IoT, the maximum transport block size is |
|                  | 680 bits in the DL and 1000 bits in UL for the   |
|                  | lowest UE category and 2536 bits for both DL and |
|                  | UL for the highest UE category.*                 |
|                  |                                                  |
|                  | *See \[36.213\] sub-clause 16.4.1.5.1 for        |
|                  | details.*                                        |
+------------------+--------------------------------------------------+
| 5.2.3.2.4.5      | *Signalling transmission scheme:*                |
|                  |                                                  |
|                  | Describe how transmission schemes are different  |
|                  | for signalling/control from that of user data.   |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | -   ***Downlink***                               |
|                  |                                                  |
|                  | > *L1/L2 control signalling is transmitted in    |
|                  | > assigned resources time and frequency          |
|                  | > multiplexed with data within the bandwidth     |
|                  | > part (BWP, see item 5.2.3.2.8.1). Control      |
|                  | > signalling is limited to QPSK modulation       |
|                  | > (QPSK, 16QAM, 64QAM and 256QAM for data).      |
|                  | > Control signalling error correcting codes are  |
|                  | > polar codes (LDPC codes for data).*            |
|                  |                                                  |
|                  | -   ***Uplink***                                 |
|                  |                                                  |
|                  | > *L1/L2 control signalling transmitted in       |
|                  | > assigned resources and can be time and         |
|                  | > frequency multiplexed with data within the     |
|                  | > BWP. L1/L2 control signalling can also be      |
|                  | > multiplexed with data on the PUSCH. Modulation |
|                  | > schemes for L1/L2 control signalling is        |
|                  | > π/2-BPSK, BPSK and QPSK*                       |
|                  | >                                                |
|                  | > *Control signalling error correcting codes are |
|                  | > block codes for small payload and polar codes  |
|                  | > for larger payloads (LDPC codes for data).*    |
|                  | >                                                |
|                  | > *For both downlink and uplink, higher-layer    |
|                  | > signalling (e.g. MAC, RLC, PDCP headers and    |
|                  | > RRC signalling) is carried within transport    |
|                  | > blocks and thus transmitted using the same     |
|                  | > physical-layer transmitter processing as user  |
|                  | > data.*                                         |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | -   ***Downlink***                               |
|                  |                                                  |
|                  | > *L1/L2 control signalling is time-multiplexed  |
|                  | > with data and transmitted in the first up to   |
|                  | > three OFDM symbols of each subframe.* *In case |
|                  | > of short TTI, the L1/L2 control signaling can  |
|                  | > be both time and frequency multiplexed with    |
|                  | > data and transmitted in the associated short   |
|                  | > TTI. Control signalling is not confined to a   |
|                  | > certain set of resource blocks but is spread   |
|                  | > over the overall system bandwidths. Control    |
|                  | > signalling is limited to QPSK modulation       |
|                  | > (QPSK, 16QAM, and 64QAM for data). Control     |
|                  | > signalling relies on tail-biting convolutional |
|                  | > coding. Turbo-codes are used for data with the |
|                  | > exception for NB-IoT where also data           |
|                  | > transmission uses tail-biting convolutional    |
|                  | > coding.*                                       |
|                  | >                                                |
|                  | > *In case of eMTC and NB-IoT the L1/L2 control  |
|                  | > signaling is confined to a configured set of   |
|                  | > resource blocks and can be time multiplexed    |
|                  | > with data and are transmitted in scheduled     |
|                  | > subframes.*                                    |
|                  |                                                  |
|                  | -   ***Uplink***                                 |
|                  |                                                  |
|                  | > *L1/L2 control signalling transmitted in one   |
|                  | > or multiple resource blocks typically at the   |
|                  | > edge of the system bandwidth and frequency     |
|                  | > multiplexed with data. For NB-IoT the L1       |
|                  | > control signaling is time and frequency        |
|                  | > multiplexed with data.*                        |
|                  | >                                                |
|                  | > *For both downlink and uplink, higher-layer    |
|                  | > signalling (e.g. MAC, RLC, PDCP headers and    |
|                  | > RRC signalling) is carried within transport    |
|                  | > blocks and thus transmitted using the same     |
|                  | > physical-layer transmitter processing as user  |
|                  | > data.*                                         |
+------------------+--------------------------------------------------+
| 5.2.3.2.4.6      | *Small signalling overhead*                      |
|                  |                                                  |
|                  | Signalling overhead refers to the radio resource |
|                  | that is required by the signalling divided by    |
|                  | the total radio resource which is used to        |
|                  | complete a transmission of a packet. The         |
|                  | signalling includes necessary messages exchanged |
|                  | in DL and UL directions during a signalling      |
|                  | mechanism, and Layer 2 protocol header for the   |
|                  | data packet.                                     |
|                  |                                                  |
|                  | Describe how the RIT/SRIT supports efficient     |
|                  | mechanism to provide small signalling overhead   |
|                  | in case of small packet transmissions.           |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *In case of small data packet transmission, the  |
|                  | L1/L2 control signalling during the connection   |
|                  | setup procedure is dominating the uplink and     |
|                  | downlink transmissions (e.g. setup of security,  |
|                  | setup of SRB1 and DRBs done with different       |
|                  | messages). To minimize this overhead NR relies   |
|                  | on RRC Inactive state that allows a UE to resume |
|                  | an earlier connection (possibly relying on delta |
|                  | signalling based on stored configurations) that  |
|                  | has been suspended.*                             |
|                  |                                                  |
|                  | *Once a terminal is in RRC connected,            |
|                  | dynamically scheduling radio resources consumes  |
|                  | DL control resources. To minimize this usage, NR |
|                  | specifies semi-persistent scheduling (SPS) in DL |
|                  | and configured grant (CG) in UL. In both         |
|                  | features a terminal is preconfigured with DL     |
|                  | (SPS) or UL (CG) data resources and can use them |
|                  | without DL control information scheduling the    |
|                  | resources.*                                      |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *In case of small data packet transmission, the  |
|                  | L1/L2 control signalling during the connection   |
|                  | setup procedure is dominating the uplink and     |
|                  | downlink transmissions. To minimize this         |
|                  | overhead LTE, including NB-IoT, allows a UE to   |
|                  | resume of an earlier connection. As an           |
|                  | alternative, the data can be transmitted over    |
|                  | the control plane, which eliminates the need to  |
|                  | setup the data plane connection.*                |
|                  |                                                  |
|                  | *Also LTE specifies DL SPS and UL CG to reduce   |
|                  | overhead related to scheduling of radio          |
|                  | resources.*                                      |
+------------------+--------------------------------------------------+
| **5.2.3.2.5**    | **Mobility management (Handover)**               |
+------------------+--------------------------------------------------+
| 5.2.3.2.5.1      | Describe the handover mechanisms and procedures  |
|                  | which are associated with                        |
|                  |                                                  |
|                  | -- Inter-System handover including the ability   |
|                  | to support mobility between the\                 |
|                  | RIT/SRIT and at least one other IMT system       |
|                  |                                                  |
|                  | -- Intra-System handover                         |
|                  |                                                  |
|                  | 1 Intra-frequency and Inter-frequency            |
|                  |                                                  |
|                  | 2 Within the RIT or between component RITs       |
|                  | within one SRIT (if applicable)                  |
|                  |                                                  |
|                  | Characterize the type of handover strategy or    |
|                  | strategies (for example, UE or base station      |
|                  | assisted handover, type of handover              |
|                  | measurements).                                   |
|                  |                                                  |
|                  | What other IMT system (other than IMT-2020)      |
|                  | could be supported by the handover mechanism?    |
|                  |                                                  |
|                  | ***[Terminology:]{.underline}***                 |
|                  |                                                  |
|                  | *To ease understanding of specific               |
|                  | terms/abbreviations used in this item here       |
|                  | after, few main acronyms and definitions are     |
|                  | introduced:*                                     |
|                  |                                                  |
|                  | -   *NR: NR Radio Access*                        |
|                  |                                                  |
|                  | -   *NG-RAN: NG Radio Access Network (connected  |
|                  |     to 5GC; it may use the E-UTRA or NR radio    |
|                  |     access)*                                     |
|                  |                                                  |
|                  | -   *5GC: 5G Core Network*                       |
|                  |                                                  |
|                  | -   *gNB, NG-RAN node providing NR user and      |
|                  |     control plane terminations towards the UE;*  |
|                  |                                                  |
|                  | -   *ng-eNB: NG-RAN node providing E-UTRA user   |
|                  |     and control plane terminations to the UE*    |
|                  |                                                  |
|                  | -   *en-gNB: NG-RAN node providing NR user plane |
|                  |     and control plane protocol terminations      |
|                  |     towards the UE, and acting as Secondary Node |
|                  |     in EN-DC.*                                   |
|                  |                                                  |
|                  | -   *eNB: E-UTRAN node, connecting to EPC*       |
|                  |                                                  |
|                  | -   *MN: Master Node*                            |
|                  |                                                  |
|                  | -   *SN: Secondary Node*                         |
|                  |                                                  |
|                  | -   *MR-DC: Multi-RAT Dual Connectivity*         |
|                  |                                                  |
|                  | -   *NE-DC: NR-E-UTRA Dual Connectivity          |
|                  |     (connected to EPC)*                          |
|                  |                                                  |
|                  | -   *EN-DC: E-UTRA-NR Dual Connectivity          |
|                  |     (connected to EPC)*                          |
|                  |                                                  |
|                  | -   *NGEN-DC: NG-RAN E-UTRA-NR Dual Connectivity |
|                  |     (Connected to 5GC)*                          |
|                  |                                                  |
|                  | ***[Inter-System handover:]{.underline}***       |
|                  |                                                  |
|                  | *Inter-system handover is supported between 5G   |
|                  | Core Network (5GC) and EPC.*                     |
|                  |                                                  |
|                  | > *- Handover between NR in 5GC and E-UTRA in    |
|                  | > EPC is supported via inter-RAT handover.*      |
|                  | >                                                |
|                  | > *- Handover between E-UTRA in 5GC and E-UTRA   |
|                  | > in EPC is supported via intra-E-UTRA handover  |
|                  | > with change of CN type.* *The source           |
|                  | > eNB/ng-eNB decides handover procedure to       |
|                  | > trigger (e.g. via the same CN type or to the   |
|                  | > other CN type). UE has to know the target CN   |
|                  | > type from the handover command during          |
|                  | > intra-LTE inter-system HO, intra-LTE           |
|                  | > intra-system HO.*                              |
|                  |                                                  |
|                  | ***[Intra-System handover:]{.underline}***       |
|                  |                                                  |
|                  | *[**For NR component RIT**:]{.underline}*        |
|                  |                                                  |
|                  | *1) Intra-NR handover: Network controlled        |
|                  | mobility applies to UEs in RRC\_CONNECTED and is |
|                  | categorized into two types of mobility:*         |
|                  |                                                  |
|                  | -   *Cell level mobility requires explicit RRC   |
|                  |     signalling to be triggered, i.e. handover.   |
|                  |     For inter-gNB handover, handover request,    |
|                  |     handover acknowledgement, handover command,  |
|                  |     handover complete procedure are supported    |
|                  |     between source gNB and target gNB. The       |
|                  |     release of the resources at the source gNB   |
|                  |     during the handover completion phase is      |
|                  |     triggered by the target gNB.*                |
|                  |                                                  |
|                  | -   *Beam level mobility does not require        |
|                  |     explicit RRC signalling to be triggered - it |
|                  |     is dealt with at lower layers - and RRC is   |
|                  |     not required to know which beam is being     |
|                  |     used at a given point in time.*              |
|                  |                                                  |
|                  | *Data forwarding, in-sequence delivery and       |
|                  | duplication avoidance at handover can be         |
|                  | guaranteed between target gNB and source gNB.*   |
|                  |                                                  |
|                  | *2) Inter-RAT handover: Intra 5GC inter RAT      |
|                  | mobility is supported between NR and E-UTRA.     |
|                  | Inter RAT measurements in NR are limited to      |
|                  | E-UTRA and the source RAT should be able to      |
|                  | support and configure Target RAT measurement and |
|                  | reporting. The in-sequence and lossless handover |
|                  | is supported for the handover between gNB and    |
|                  | ng-eNB. Both Xn and NG based inter-RAT handover  |
|                  | between NG-RAN nodes is supported. Whether the   |
|                  | handover is over Xn or CN is transparent to the  |
|                  | UE. The target RAT receives the UE NG-C context  |
|                  | information and based on this information        |
|                  | configures the UE with a complete RRC message    |
|                  | and Full configuration (not delta).*             |
|                  |                                                  |
|                  | *[Measurement]{.underline}*                      |
|                  |                                                  |
|                  | *In RRC\_CONNECTED, the UE measures multiple     |
|                  | beams (at least one) of a cell and the           |
|                  | measurements results (power values) are averaged |
|                  | to derive the cell quality. In doing so, the UE  |
|                  | is configured to consider a subset of the        |
|                  | detected beams: the N best beams above an        |
|                  | absolute threshold. Filtering takes place at two |
|                  | different levels: at the physical layer to       |
|                  | derive beam quality and then at RRC level to     |
|                  | derive cell quality from multiple beams. Cell    |
|                  | quality from beam measurements is derived in the |
|                  | same way for the serving cell(s) and for the     |
|                  | non-serving cell(s). Measurement reports may     |
|                  | contain the measurement results of the X best    |
|                  | beams if the UE is configured to do so by the    |
|                  | gNB.*                                            |
|                  |                                                  |
|                  | *For more details, refer to \[38.300\]           |
|                  | sub-clauses 9.2.3 & 9.3*                         |
|                  |                                                  |
|                  | *[**For LTE component RIT**:]{.underline}*       |
|                  |                                                  |
|                  | *In E-UTRAN RRC\_CONNECTED state,                |
|                  | network-controlled UE-assisted handovers and DC  |
|                  | specific activities are performed and various    |
|                  | DRX cycles are supported.*                       |
|                  |                                                  |
|                  | *Handover procedures, like processes that        |
|                  | precede the final HO decision on the source      |
|                  | network side (control and evaluation of UE and   |
|                  | eNB measurements taking into account certain UE  |
|                  | specific roaming and access restrictions),       |
|                  | preparation of resources on the target network   |
|                  | side, commanding the UE to the new radio         |
|                  | resources and finally releasing resources on the |
|                  | (old) source network side. It contains           |
|                  | mechanisms to transfer context data between      |
|                  | evolved nodes, and to update node relations on   |
|                  | C-plane and U-plane.*                            |
|                  |                                                  |
|                  | *[Measurement]{.underline}*                      |
|                  |                                                  |
|                  | *Measurements to be performed by a UE for        |
|                  | intra/inter-frequency mobility can be controlled |
|                  | by E-UTRAN, using broadcast or dedicated         |
|                  | control. In RRC\_IDLE state, a UE shall follow   |
|                  | the measurement parameters defined for cell      |
|                  | reselection specified by the E-UTRAN broadcast.  |
|                  | The use of dedicated measurement control for     |
|                  | RRC\_IDLE state is possible through the          |
|                  | provision of UE specific priorities. In          |
|                  | RRC\_CONNECTED state, a UE shall follow the      |
|                  | measurement configurations specified by RRC      |
|                  | directed from the E-UTRAN (e.g. as in UTRAN      |
|                  | MEASUREMENT\_CONTROL).*                          |
|                  |                                                  |
|                  | *In RRC\_IDLE and RRC\_CONNECTED the UE may be   |
|                  | configured to monitor some UTRA or E-UTRA        |
|                  | carriers according to reduced performance        |
|                  | requirements as specified in \[36.133\].*        |
|                  |                                                  |
|                  | *For CSI-RS based discovery signals              |
|                  | measurements, \"cell\" should be interpreted as  |
|                  | \"transmission point of the concerned cell\" in  |
|                  | the following descriptions.*                     |
|                  |                                                  |
|                  | *Intra-frequency neighbour (cell) measurements   |
|                  | and inter-frequency neighbour (cell)             |
|                  | measurements are defined as follows:*            |
|                  |                                                  |
|                  | -   *Intra-frequency neighbour (cell)            |
|                  |     measurements: Neighbour cell measurements    |
|                  |     performed by the UE are intra-frequency      |
|                  |     measurements when the current and target     |
|                  |     cell operates on the same carrier            |
|                  |     frequency.*                                  |
|                  |                                                  |
|                  | -   *Inter-frequency neighbour (cell)            |
|                  |     measurements: Neighbour cell measurements    |
|                  |     performed by the UE are inter-frequency      |
|                  |     measurements when the neighbour cell         |
|                  |     operates on a different carrier frequency,   |
|                  |     compared to the current cell.*               |
|                  |                                                  |
|                  | *For more details, refer to \[36.300\]           |
|                  | sub-clauses 10.1 & 10.2*                         |
+------------------+--------------------------------------------------+
| 5.2.3.2.5.2      | Describe the handover mechanisms and procedures  |
|                  | to meet the simultaneous handover requirements   |
|                  | of a large number of users in high speed         |
|                  | scenarios (up to 500km/h moving speed) with high |
|                  | handover success rate.                           |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *In NR, the physical layer supports random       |
|                  | access channel (RACH) sequences with 15 kHz and  |
|                  | 30 kHz subcarrier spacing for frequencies        |
|                  | between 410 MHz and 7125 MHz, and 60 kHz and 120 |
|                  | kHz subcarrier spacing for frequency between     |
|                  | 24250 MHz and 52600 MHz, which have high         |
|                  | tolerance to Doppler effects. The physical layer |
|                  | also support RACH sequences with 1.25 kHz        |
|                  | subcarrier spacing and sequence restriction      |
|                  | rules that enable use of RACH sequences in high  |
|                  | Doppler scenarios. NR additionally supports      |
|                  | multiple RACH resource multiplexing in frequency |
|                  | and time domain that allows large multiplexing   |
|                  | of users that enable large number of users to    |
|                  | perform handover. Radio resource management      |
|                  | (RRM) are designed to work properly in high      |
|                  | speed scenarios. Specifically for the            |
|                  | simultaneous handover requirements of a large    |
|                  | number of users, the existing handover mechanism |
|                  | in NR can provide sufficient resource (RACH,     |
|                  | uplink and downlink data channels) for handover  |
|                  | purposes.*                                       |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *LTE performance for high speed scenario was     |
|                  | enhanced in Rel-14 WI "Performance enhancements  |
|                  | for high speed scenario". In addition, High      |
|                  | Speed Dedicated Network (HSDN) was introduced in |
|                  | LTE Rel-15. As a result, in LTE, the physical    |
|                  | layer supports RACH sequences with sequence      |
|                  | restriction rules that enable use of RACH        |
|                  | sequences in high Doppler scenarios, and RRM are |
|                  | designed to work properly in high speed          |
|                  | scenarios. Specifically for the simultaneous     |
|                  | handover requirements of a large number of       |
|                  | users, the existing handover mechanism in LTE    |
|                  | can provide sufficient resource (RACH, uplink    |
|                  | and downlink data channels) for handover         |
|                  | purposes.*                                       |
+------------------+--------------------------------------------------+
| **5.2.3.2.6**    | **Radio resource management**                    |
+------------------+--------------------------------------------------+
| 5.2.3.2.6.1      | Describe the radio resource management, for      |
|                  | example support of:                              |
|                  |                                                  |
|                  | -- centralised and/or distributed RRM            |
|                  |                                                  |
|                  | -- dynamic and flexible radio resource           |
|                  | management                                       |
|                  |                                                  |
|                  | -- efficient load balancing.                     |
|                  |                                                  |
|                  | *RRM mechanism in the following is supported in  |
|                  | both LTE and NR component RIT commonly.*         |
|                  |                                                  |
|                  | *[General\                                       |
|                  | ]{.underline}LTE/NR performs radio resource      |
|                  | management to ensure the efficient use of the    |
|                  | available radio resource. RRM functions          |
|                  | include:*                                        |
|                  |                                                  |
|                  | -   *Radio bearer control (RBC): the             |
|                  |     establishment, maintenance and release of    |
|                  |     radio bearer involves the configuration of   |
|                  |     radio resource. This is located in           |
|                  |     gNB/ng-eNB.*                                 |
|                  |                                                  |
|                  | -   *Radio Admission Control (RAC): RAC is to    |
|                  |     admit or reject the establishment of new     |
|                  |     radio bearer. It considers QoS requirement,  |
|                  |     the priority level, overall resource         |
|                  |     situation. This is located in gNB/ng-eNB.*   |
|                  |                                                  |
|                  | -   *Connection Mobility Control (CMC): it       |
|                  |     controls the number of UEs in idle mode and  |
|                  |     connected mode. In idle mode, cell           |
|                  |     reselection algorithm is controlled by       |
|                  |     parameter setting and in the connected mode, |
|                  |     gNB controls UE mobility via handover and    |
|                  |     RRC connection release with redirection.*    |
|                  |                                                  |
|                  | *[Dynamic/flexible radio resource                |
|                  | management]{.underline}*                         |
|                  |                                                  |
|                  | *LTE/NR supports dynamic and flexible radio      |
|                  | resource management by packet scheduling that    |
|                  | allocates and de-allocates resources to user and |
|                  | control plane packets.*                          |
|                  |                                                  |
|                  | *[Load balancing(LB)]{.underline}*               |
|                  |                                                  |
|                  | *Load balancing has the task to handle uneven    |
|                  | distribution of the traffic load over multiple   |
|                  | cells. The purpose of LB is thus to influence    |
|                  | the load distribution for the higher resource    |
|                  | utilization and QoS. LB is achieved in NR with   |
|                  | hand-over, redirection or cell reselection.*     |
+------------------+--------------------------------------------------+
| 5.2.3.2.6.2      | *Inter-RIT interworking*                         |
|                  |                                                  |
|                  | Describe the functional blocks and mechanisms    |
|                  | for interworking (such as a network architecture |
|                  | model) between component RITs within a SRIT, if  |
|                  | supported.                                       |
|                  |                                                  |
|                  | ***[Multi-RAT Dual Connectivity:]{.underline}*** |
|                  |                                                  |
|                  | *Tight inter-working between E-UTRA and NR is    |
|                  | supported with Multi-RAT Dual Connectivity       |
|                  | (MR-DC) operation using E-UTRA and NR. The       |
|                  | following type of MR-DC is supported:*           |
|                  |                                                  |
|                  | -   *MR-DC with the EPC: E-UTRA-NR Dual          |
|                  |     Connectivity (EN-DC). eNB is master node     |
|                  |     (MN) and gNB is acting as secondary node     |
|                  |     (SN)*                                        |
|                  |                                                  |
|                  | -   *MR-DC with the 5GC:*                        |
|                  |                                                  |
|                  |     -   *NG-RAN E-UTRA-NR Dual Connectivity      |
|                  |         (NGEN-DC): eNB is MN and gNB is SN.*     |
|                  |                                                  |
|                  |     -   *NR-E-UTRA Dual Connectivity (NE-DC):    |
|                  |         gNB is MN and eNB is SN.*                |
|                  |                                                  |
|                  | *Similar to LTE dual connectivity, MN is         |
|                  | responsible for handover and SN provides         |
|                  | offloading to increase overall data rate.*       |
|                  |                                                  |
|                  | *Control plane architecture: For MR-DC           |
|                  | operation, eNB and gNB is communicated via X2-C  |
|                  | interface for EN-DC and Xn-C for MR-DC with the  |
|                  | 5GC. Single RRC state is maintained but both MN  |
|                  | and SN has two RRC entities and can generate     |
|                  | full RRC messages.*                              |
|                  |                                                  |
|                  | *User plane architecture: MR-DC supports MCG,    |
|                  | SCG and split bearer. In case of split bearer,   |
|                  | both MN and SN support RLC for the same radio    |
|                  | bearer.*                                         |
|                  |                                                  |
|                  | *For more details, refer to \[37.340\]; see also |
|                  | item 5.2.3.2.13.1*                               |
+------------------+--------------------------------------------------+
| 5.2.3.2.6.3      | *Connection/session management*                  |
|                  |                                                  |
|                  | The mechanisms for connection/session management |
|                  | over the air-interface should be described. For  |
|                  | example:                                         |
|                  |                                                  |
|                  | -- The support of multiple protocol states with  |
|                  | fast and dynamic transitions.                    |
|                  |                                                  |
|                  | -- The signalling schemes for allocating and     |
|                  | releasing resources.                             |
|                  |                                                  |
|                  | *NG-RAN support the following states:*           |
|                  |                                                  |
|                  | ***RRC\_IDLE**:*                                 |
|                  |                                                  |
|                  | *- PLMN selection;*                              |
|                  |                                                  |
|                  | *- Broadcast of system information;*             |
|                  |                                                  |
|                  | *- Cell re-selection mobility;*                  |
|                  |                                                  |
|                  | *- Paging for mobile terminated data is          |
|                  | initiated by 5GC;*                               |
|                  |                                                  |
|                  | *- Paging for mobile terminated data area is     |
|                  | managed by 5GC;*                                 |
|                  |                                                  |
|                  | *- DRX for CN paging configured by NAS.*         |
|                  |                                                  |
|                  | *- **RRC\_INACTIVE**:*                           |
|                  |                                                  |
|                  | *- Broadcast of system information;*             |
|                  |                                                  |
|                  | *- Cell re-selection mobility;*                  |
|                  |                                                  |
|                  | *- Paging is initiated by NG-RAN (RAN paging);*  |
|                  |                                                  |
|                  | *- RAN-based notification area (RNA) is managed  |
|                  | by NG- RAN;*                                     |
|                  |                                                  |
|                  | *- DRX for RAN paging configured by NG-RAN;*     |
|                  |                                                  |
|                  | *- 5GC - NG-RAN connection (both C/U-planes) is  |
|                  | established for UE;*                             |
|                  |                                                  |
|                  | *- The UE AS context is stored in NG-RAN and the |
|                  | UE;*                                             |
|                  |                                                  |
|                  | *- NG-RAN knows the RNA which the UE belongs     |
|                  | to.*                                             |
|                  |                                                  |
|                  | *- **RRC\_CONNECTED**:*                          |
|                  |                                                  |
|                  | *- 5GC - NG-RAN connection (both C/U-planes) is  |
|                  | established for UE;*                             |
|                  |                                                  |
|                  | *- The UE AS context is stored in NG-RAN and the |
|                  | UE;*                                             |
|                  |                                                  |
|                  | *- NG-RAN knows the cell which the UE belongs    |
|                  | to;*                                             |
|                  |                                                  |
|                  | *- Transfer of unicast data to/from the UE;*     |
|                  |                                                  |
|                  | *- Network controlled mobility including         |
|                  | measurements.*                                   |
|                  |                                                  |
|                  | *Transition between RRC states:*                 |
|                  |                                                  |
|                  | -   *From RRC\_IDLE to RRC\_CONNECTED: RRC       |
|                  |     connection setup*                            |
|                  |                                                  |
|                  | -   *From RRC\_CONNECTED to RRC\_IDLE: RRC       |
|                  |     connection release*                          |
|                  |                                                  |
|                  | -   *From RRC\_INACTIVE to RRC\_CONNECTED: RRC   |
|                  |     connection resume*                           |
|                  |                                                  |
|                  | -   *From RRC\_CONNECTED to RRC\_INACTIVE: RRC   |
|                  |     connection suspension*                       |
|                  |                                                  |
|                  | -   *From RRC\_INACTIVE to RRC\_IDLE: RRC        |
|                  |     connection release (TBC)*                    |
|                  |                                                  |
|                  | -   *From RRC\_IDLE to RRC\_INACTIVE: not        |
|                  |     supported*                                   |
|                  |                                                  |
|                  | *For more details, refer to \[38.300\]*          |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *RRC\_IDLE and RRC\_CONNECTED are supported,     |
|                  | with similar functionality as described above    |
|                  | for NR.*                                         |
|                  |                                                  |
|                  | *For more details, refer to \[36.300\]*          |
+------------------+--------------------------------------------------+
| **5.2.3.2.7**    | **Frame structure**                              |
+------------------+--------------------------------------------------+
| 5.2.3.2.7.1      | Describe the frame structure for downlink and    |
|                  | uplink by providing sufficient information such  |
|                  | as:                                              |
|                  |                                                  |
|                  | -- frame length,                                 |
|                  |                                                  |
|                  | -- the number of time slots per frame,           |
|                  |                                                  |
|                  | -- the number and position of switch points per  |
|                  | frame for TDD                                    |
|                  |                                                  |
|                  | -- guard time or the number of guard bits,       |
|                  |                                                  |
|                  | -- user payload information per time slot,       |
|                  |                                                  |
|                  | -- sub-carrier spacing                           |
|                  |                                                  |
|                  | -- control channel structure and multiplexing,   |
|                  |                                                  |
|                  | -- power control bit rate.                       |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | -   ***Frame length, sub-carrier spacing, and    |
|                  |     time slots:***                               |
|                  |                                                  |
|                  | *One radio frame of length 10 ms consisting of   |
|                  | 10 subframes, each of length 1 ms. Each subframe |
|                  | consists of an OFDM sub-carrier spacing          |
|                  | dependent number of slots. Each slot consists of |
|                  | 14 OFDM symbols (twelve OFDM symbols in case of  |
|                  | extended cyclic prefix)*                         |
|                  |                                                  |
|                  | -   *15 kHz SCS: 1 ms slot, 1 slot per           |
|                  |     sub-frame*                                   |
|                  |                                                  |
|                  | -   *30 kHz SCS: 0.5 ms slot, 2 slots per        |
|                  |     sub-frame*                                   |
|                  |                                                  |
|                  | -   *60 kHz SCS: 0.25 ms slot, 4 slots per       |
|                  |     sub-frame*                                   |
|                  |                                                  |
|                  | -   *120 kHz SCS: 0.125 ms slot, 8 slots per     |
|                  |     sub-frame*                                   |
|                  |                                                  |
|                  | -   *240 kHz SCS: 0.0625 ms slot (only used for  |
|                  |     synchronization, not for data)*              |
|                  |                                                  |
|                  | *Data transmissions can be scheduled on a slot   |
|                  | basis, as well as on a partial slot basis, where |
|                  | the partial slot transmissions may occur several |
|                  | times within one slot. The supported partial     |
|                  | slot allocations and scheduling intervals are 2, |
|                  | 4 and 7 symbols for DL and 1-14 symbols for UL   |
|                  | for normal cyclic prefix, and 2, 4 and 6 symbols |
|                  | for DL and 1-12 symbols for UL for extended      |
|                  | cyclic prefix.*                                  |
|                  |                                                  |
|                  | *The slot structure supports zero, one or two    |
|                  | DL/UL switches per slot, and dynamic selection   |
|                  | of the link direction for each slot              |
|                  | independently. Typically one symbol would be     |
|                  | allocated as guard, but different number of      |
|                  | symbols, or even full slot could be allocated as |
|                  | guard.*                                          |
|                  |                                                  |
|                  | -   ***Downlink control channel structure:***    |
|                  |                                                  |
|                  | *Downlink control signaling is time and          |
|                  | frequency multiplexed with data on a scheduling  |
|                  | interval basis. The control region can span over |
|                  | 1-3 OFDM symbols in the beginning of the         |
|                  | allocation, flexibly allocating 1-14 symbols (at |
|                  | least 2 symbols for DL) for data transmission,   |
|                  | including the time and frequency part of the     |
|                  | control region that was not used for control     |
|                  | signaling.*                                      |
|                  |                                                  |
|                  | -   ***Uplink control channel structure:***      |
|                  |                                                  |
|                  | *Uplink control signaling can be both            |
|                  | time-multiplexed with the data of the same UE    |
|                  | and time and frequency multiplexed with control  |
|                  | and data of other UEs when the UE has no data to |
|                  | be transmitted. Uplink control signaling is      |
|                  | piggy-backed with data i.e. transmitted with     |
|                  | data on the PUSCH when the UE has data to be     |
|                  | transmitted.*                                    |
|                  |                                                  |
|                  | -   ***Power control bit rate:***                |
|                  |                                                  |
|                  | *No specific power-control rate is defined, but  |
|                  | a power control command can be sent at any slot, |
|                  | leading to a sub-carrier spacing specific        |
|                  | maximum power control rate of 1/2/4/8 kHz for    |
|                  | SCS of 15/30/60/120 kHz respectively.*           |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | -   ***Frame length, sub-carrier spacing, and    |
|                  |     time slots:***                               |
|                  |                                                  |
|                  | *Both FDD and TDD frame structures are           |
|                  | supported. One radio frame of length 10 ms       |
|                  | consisting of 10 subframes, each of length 1 ms. |
|                  | Each subframe consists of two slots, each of     |
|                  | length 0.5 ms. Each slot consists of seven OFDM  |
|                  | symbols (six OFDM symbols in case of extended    |
|                  | cyclic prefix). A minimum time unit for          |
|                  | transmission is either a TTI, which has a        |
|                  | duration of one subframe, or a short TTI, having |
|                  | a duration of one slot (with FDD and TDD) or 2/3 |
|                  | OFDM symbols (only with FDD). Sub-carrier        |
|                  | spacings of 15kHz is supported for uni-cast data |
|                  | and subcarrier spacings of 15kHz, 7.5kHz and     |
|                  | 1.25kHz are supported for multi-cast data.*      |
|                  |                                                  |
|                  | *For the frame structure of TDD, it is possible  |
|                  | to have two DL/UL switching points (one downlink |
|                  | part and one uplink part) or four DL/UL          |
|                  | switching points (two downlink parts and two     |
|                  | uplink parts) per frame. Switching downlink to   |
|                  | uplink takes place in a special subframe which   |
|                  | consists of the three fields DwPTS, GP and       |
|                  | UpPTS, see \[36.211\] subclause 4.2.*            |
|                  |                                                  |
|                  | *The guard time can be flexibly configured from  |
|                  | a minimum of approximately 70 μs to a maximum of |
|                  | approximately 700 μs in case of TDD.*            |
|                  |                                                  |
|                  | *For NB-IoT, the minimum time unit for           |
|                  | transmission is a subframe in the downlink and a |
|                  | resource unit in the uplink. The length of a     |
|                  | resource unit is dependent on the subcarrier     |
|                  | spacing and number of subcarriers. Up to ten     |
|                  | subframes or resource units can be assigned to   |
|                  | the UE for one transmission. Sub-carrier         |
|                  | spacings of 15kHz is supported for DL, and       |
|                  | sub-carrier spacings of 3.75kHz and 15kHz is     |
|                  | supported for UL (see item 5.2.3.2.2.1 for more  |
|                  | details).*                                       |
|                  |                                                  |
|                  | *For eMTC half-duplex FDD operation and NB-IoT,  |
|                  | a guard period of 1ms is used for the switching  |
|                  | time.*                                           |
|                  |                                                  |
|                  | *For more details on the frame structure         |
|                  | including DL/UL switching and guard times in     |
|                  | case of TDD operation., see \[36.211\]           |
|                  | sub-clause 4.*                                   |
|                  |                                                  |
|                  | -   ***Downlink control channel structure:***    |
|                  |                                                  |
|                  | *Downlink control signalling can be either time  |
|                  | or time and frequency multiplexed with data on a |
|                  | subframe TTI or short TTI basis. With time       |
|                  | multiplexing, control signaling is transmitted   |
|                  | in the first up to three OFDM symbols of each    |
|                  | subframe and data transmitted in the remaining   |
|                  | part of the subframe (up to 13 OFDM symbols).*   |
|                  |                                                  |
|                  | *For eMTC and NB-IoT, downlink control           |
|                  | signalling and data transmission to the same UE  |
|                  | are time multiplexed on different subframes.*    |
|                  |                                                  |
|                  | -   ***Uplink control channel structure:***      |
|                  |                                                  |
|                  | *Uplink control signalling is                    |
|                  | frequency-multiplexed with data for other UEs    |
|                  | (no time separation) when the UE has no data to  |
|                  | be transmitted. Uplink control signalling is     |
|                  | typically transmitted at the edges of the        |
|                  | overall system bandwidth. Uplink control         |
|                  | signalling is piggy-backed with data i.e.        |
|                  | transmitted with data on the PUSCH when the UE   |
|                  | has data to be transmitted.*                     |
|                  |                                                  |
|                  | -   ***Power control bit rate:***                |
|                  |                                                  |
|                  | *There is no specific power-control rate. At     |
|                  | most one power-control command per subframe,     |
|                  | implying 1 kHz maximum power-control rate.*      |
|                  |                                                  |
|                  | *For more details on the (uplink) power control, |
|                  | see \[36.213\] sub-clause 5.1.*                  |
|                  |                                                  |
|                  | *For NB-IoT, only open-loop power control is     |
|                  | supported.*                                      |
+------------------+--------------------------------------------------+
| **5.2.3.2.8**    | **Spectrum capabilities and duplex               |
|                  | technologies**                                   |
|                  |                                                  |
|                  | NOTE 1 -- Parameters for both downlink and       |
|                  | uplink should be described separately, if        |
|                  | necessary.                                       |
+------------------+--------------------------------------------------+
| 5.2.3.2.8.1      | *Spectrum sharing and flexible spectrum use*     |
|                  |                                                  |
|                  | Does the RIT/SRIT support flexible spectrum use  |
|                  | and/or spectrum sharing? Provide the detail.     |
|                  |                                                  |
|                  | Description such as capability to flexibly       |
|                  | allocate the spectrum resources in an adaptive   |
|                  | manner for paired and un-paired spectrum to      |
|                  | address the uplink and downlink traffic          |
|                  | asymmetry.                                       |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | -   *NR supports flexible spectrum use through   |
|                  |     mechanisms including the following:*         |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   *Multiple component carriers can be          |
|                  |     aggregated to achieve up to 6.4 GHz of       |
|                  |     transmission bandwidth. The aggregated       |
|                  |     component carriers can be either contiguous  |
|                  |     or non-contiguous in the frequency domain,   |
|                  |     including be located in separate spectrum    |
|                  |     ("spectrum aggregation").*                   |
|                  |                                                  |
|                  | -   *In addition, within one component carrier,  |
|                  |     bandwidth part (BWP) is supported on         |
|                  |     downlink and uplink. The bandwidth of the    |
|                  |     component carrier can be divided into        |
|                  |     several bandwidth parts. From network        |
|                  |     perspective, different bandwidth parts can   |
|                  |     be associated with different numerologies    |
|                  |     (subcarrier spacing, cyclic prefix). UEs     |
|                  |     with smaller bandwidth support capability    |
|                  |     can work within a bandwidth part with an     |
|                  |     associated numerology. By this means UEs     |
|                  |     with different bandwidth support capability  |
|                  |     can work on large bandwidth component        |
|                  |     carrier. NR supports UE bandwidth part       |
|                  |     adaptation for UE power saving and           |
|                  |     numerology switching. The network can        |
|                  |     operate on a wide bandwidth carrier while it |
|                  |     is not required for the UE to support the    |
|                  |     whole bandwidth carrier, but can work over   |
|                  |     activated bandwidth parts, thereby           |
|                  |     optimizing the use of radio resources to the |
|                  |     traffic demand and minimizing interference   |
|                  |     to/from other systems.*                      |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   *NR supports spectrum sharing with LTE. The  |
|                  |     operating carrier of NR and LTE can be       |
|                  |     overlapped or adjacent. From network         |
|                  |     perspective, NR users and LTE users can      |
|                  |     share / co-exist on the overlapped carrier   |
|                  |     in frequency division multiplexing (FDM) or  |
|                  |     time division multiplexing (TDM) manner,     |
|                  |     with dynamic scheduling or semi-static       |
|                  |     configurations. When LTE and NR spectrum     |
|                  |     overlaps, resources can be shared by LTE DL  |
|                  |     carrier and NR DL carrier, or by LTE UL      |
|                  |     carrier and NR UL carrier. OFDM symbol       |
|                  |     durations of NR and LTE can be aligned. The  |
|                  |     system allows aligning sub-carriers of LTE   |
|                  |     and NR to enable more efficient sharing of   |
|                  |     overlapped resources.*                       |
|                  |                                                  |
|                  | -   *NR can operate on a TDD band with a         |
|                  |     supplementary UL (SUL) band. In this case,   |
|                  |     NR can flexibly allocate users on either TDD |
|                  |     band or the SUL band for uplink              |
|                  |     transmission. It is beneficial for the users |
|                  |     at cell edge where the coverage might be     |
|                  |     limited for those users on TDD band (usually |
|                  |     higher carrier frequency than SUL band, see  |
|                  |     item 5.2.3.2.8.3). In this case, such users  |
|                  |     can be allocated to SUL band with lower      |
|                  |     propagation loss for uplink transmission.*   |
|                  |                                                  |
|                  | -   *NR addresses the uplink and downlink        |
|                  |     traffic asymmetry with flexible spectrum     |
|                  |     resource allocation by allowing FDD          |
|                  |     operation on a paired spectrum, different    |
|                  |     transmission directions in either part of a  |
|                  |     paired spectrum, TDD operation on an         |
|                  |     unpaired spectrum where the transmission     |
|                  |     direction of time resources is not           |
|                  |     dynamically changed, and TDD operation on an |
|                  |     unpaired spectrum where the transmission     |
|                  |     direction of most time resources can be      |
|                  |     dynamically changing. DL and UL transmission |
|                  |     directions for data can be dynamically       |
|                  |     assigned on a per-slot basis.*               |
|                  |                                                  |
|                  | *NR can be configured to co-exist with           |
|                  | NB-IoT/eMTC using frequency division             |
|                  | multiplexing (FDM) way.*                         |
|                  |                                                  |
|                  | -   *For NB-IoT,*                                |
|                  |                                                  |
|                  |     -   *The downlink co-existence can be made   |
|                  |         by NR by configuring reserved resource   |
|                  |         blocks (RBs) which are declared as not   |
|                  |         available for PDSCH for NR users. These  |
|                  |         reserved resource blocks can be used by  |
|                  |         NB-IoT anchor and non-anchor carriers.   |
|                  |         For NR users that are scheduled on the   |
|                  |         resource block group (RBG) which         |
|                  |         includes the reserved RB, NR will        |
|                  |         configure the rate match pattern for     |
|                  |         those users using dynamic or semi-static |
|                  |         indication.*                             |
|                  |                                                  |
|                  |     -   *For uplink, NR can use appropriate      |
|                  |         uplink resource allocation to "reserve"  |
|                  |         RBs for NB-IoT users. For example, if    |
|                  |         some of the RBs are reserved for NB-IoT, |
|                  |         NR will allocate other RBs to its users, |
|                  |         by either frequency domain resource      |
|                  |         allocation type 0 or type 1. By the      |
|                  |         above means, NR and NB-IoT can co-exist  |
|                  |         without any impact to each other.*       |
|                  |                                                  |
|                  | -   *For eMTC,*                                  |
|                  |                                                  |
|                  |     -   *The downlink co-existence can be made   |
|                  |         by NR by configuring reserved resources  |
|                  |         for eMTC. It can be achieved by resource |
|                  |         element (RE) level and RB level resource |
|                  |         reservation indication.*                 |
|                  |                                                  |
|                  |     -   *Similar mechanism to NB-IoT can be      |
|                  |         employed for uplink to enable NR         |
|                  |         co-existence with eMTC for uplink.*      |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | -   *LTE supports flexible spectrum use by using |
|                  |     one or multiple component carriers. Multiple |
|                  |     component carriers can be aggregated to      |
|                  |     achieve up to 640 MHz of transmission        |
|                  |     bandwidth. The aggregated component carriers |
|                  |     can be either contiguous or non-contiguous   |
|                  |     in the frequency domain, including be        |
|                  |     located in separate spectrum ("spectrum      |
|                  |     aggregation").*                              |
|                  |                                                  |
|                  | -   *LTE addresses the uplink and downlink       |
|                  |     traffic asymmetry with flexible allocating   |
|                  |     spectrum resources by allowing TDD operation |
|                  |     on an unpaired spectrum where the            |
|                  |     transmission direction of time resources is  |
|                  |     not dynamically changed, and TDD operation   |
|                  |     on an unpaired spectrum where the            |
|                  |     transmission direction of most time          |
|                  |     resources can be changing among the seven    |
|                  |     DL/UL configurations per as low as radio     |
|                  |     frame basis.*                                |
|                  |                                                  |
|                  | *For NB-IoT,*                                    |
|                  |                                                  |
|                  | -   *Flexible spectrum use is supported by using |
|                  |     one or multiple NB-IoT carriers.*            |
|                  |                                                  |
|                  |     -   *A single, anchor, NB-IoT carrier of 180 |
|                  |         kHz each for UL and DL in FDD is the     |
|                  |         minimum required spectrum.*              |
|                  |                                                  |
|                  |     -   *Additional non-anchor NB-IoT            |
|                  |         carrier(s), each of 180 kHz can be       |
|                  |         associated to the same NB-IoT cell, and  |
|                  |         a UE uses either the anchor or one       |
|                  |         non-anchor NB-IoT carrier.*              |
|                  |                                                  |
|                  |     -   *The anchor carrier and non-anchor       |
|                  |         carrier(s) can be either contiguous or   |
|                  |         non-contiguous in the frequency domain.* |
|                  |                                                  |
|                  | -   *An NB-IoT carrier can be in-band with LTE,  |
|                  |     in an LTE guard-band, or in spectrum where   |
|                  |     no LTE is present. These are termed in-band, |
|                  |     guard-band, and standalone operation         |
|                  |     respectively. All combinations of carrier    |
|                  |     types (standalone, in-band, guard-band) are  |
|                  |     allowed.*                                    |
|                  |                                                  |
|                  | *For eMTC, there is no aggregation of multiple   |
|                  | component carriers.*                             |
+------------------+--------------------------------------------------+
| 5.2.3.2.8.2      | *Channel bandwidth scalability*                  |
|                  |                                                  |
|                  | Describe how the proposed RIT/SRIT supports      |
|                  | channel bandwidth scalability, including the     |
|                  | supported bandwidths.                            |
|                  |                                                  |
|                  | Describe whether the proposed RIT/SRIT supports  |
|                  | extensions for scalable bandwidths wider than    |
|                  | 100 MHz.                                         |
|                  |                                                  |
|                  | Describe whether the proposed RIT/SRIT supports  |
|                  | extensions for scalable bandwidths wider than 1  |
|                  | GHz, e.g., when operated in higher frequency     |
|                  | bands noted in § 5.2.4.2.                        |
|                  |                                                  |
|                  | Consider, for example:                           |
|                  |                                                  |
|                  | -- The scalability of operating bandwidths.      |
|                  |                                                  |
|                  | -- The scalability using single and/or multiple  |
|                  | RF carriers.                                     |
|                  |                                                  |
|                  | Describe multiple contiguous (or non-contiguous) |
|                  | band aggregation capabilities, if any. Consider  |
|                  | for example the aggregation of multiple channels |
|                  | to support higher user bit rates.                |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *One component carrier supports a scalable       |
|                  | bandwidth, 5, 10, 15, 20, 25, 40, 50, 60, 80,    |
|                  | 100MHz for frequency range 450 MHz to 6000 MHz   |
|                  | (see \[38.101\] for the actual support of        |
|                  | bandwidth for each band), with guard band ratio  |
|                  | from 20% to 2%; and a scalable bandwidth, 50,    |
|                  | 100, 200, 400MHz for frequency range 24250 --    |
|                  | 52600 MHz (see \[38.101\] for the actual support |
|                  | of bandwidth for each band), with guard band     |
|                  | ratio from 8% to 5%. By aggregating multiple     |
|                  | component carriers, transmission bandwidths up   |
|                  | to 6.4 GHz are supported to provide high data    |
|                  | rates. Component carriers can be either          |
|                  | contiguous or non-contiguous in the frequency    |
|                  | domain. The number of component carriers         |
|                  | transmitted and/or received by a mobile terminal |
|                  | can vary over time depending on the              |
|                  | instantaneous data rate.*                        |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *One component carrier supports a scalable       |
|                  | bandwidth, 1.4, 3, 5, 10, 15 and 20 MHz, with    |
|                  | guard band ratio from 23% to 10% (see \[36.101\] |
|                  | sub-clause 5.6 for more details). By aggregating |
|                  | multiple component carriers, transmission        |
|                  | bandwidths up to 640 MHz are supported to        |
|                  | provide the high data rates. Component carriers  |
|                  | can be either contiguous or non-contiguous in    |
|                  | the frequency domain. The number of component    |
|                  | carriers transmitted and/or received by a mobile |
|                  | terminal can vary over time depending on the     |
|                  | instantaneous data rate.*                        |
|                  |                                                  |
|                  | *For NB-IoT, the channel bandwidth is not        |
|                  | scalable. There is not aggregation of multiple   |
|                  | NB-IoT carriers -- see item 5.2.3.2.8.1 for more |
|                  | details.*                                        |
|                  |                                                  |
|                  | *For eMTC, the above scalable bandwidth from 1.4 |
|                  | to 20 MHz is supported. The eMTC UE can have a   |
|                  | narrower RF bandwidth than the cell is           |
|                  | configured with. Category M1 UE has a bandwidth  |
|                  | of 1.4 MHz, and category M2 UE has 5 MHz         |
|                  | bandwidth.*                                      |
+------------------+--------------------------------------------------+
| 5.2.3.2.8.3      | What are the frequency bands supported by the    |
|                  | RIT/SRIT? Please list.                           |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *The following frequency bands will be           |
|                  | supported, in accordance with spectrum           |
|                  | requirements defined by Report ITU-R M.2411-0.   |
|                  | Introduction of other ITU-R IMT identified bands |
|                  | are not precluded in the future. 3GPP            |
|                  | technologies are also defined as appropriate to  |
|                  | operate in other frequency arrangements and      |
|                  | bands.*                                          |
|                  |                                                  |
|                  | *[450 -- 6000 MHz:]{.underline}*                 |
|                  |                                                  |
|                  | +----------+----------+----------+----------+    |
|                  | | NR       | Uplink   | Downlink | Duplex   |    |
|                  | | *o       | (UL)     | (DL)     | Mode     |    |
|                  | | perating | *o       | *o       |          |    |
|                  | | band*    | perating | perating |          |    |
|                  | |          | band*\   | band*\   |          |    |
|                  | |          | BS       | BS       |          |    |
|                  | |          | receive  | transmit |          |    |
|                  | |          | / UE     | / UE     |          |    |
|                  | |          | transmit | receive  |          |    |
|                  | |          |          |          |          |    |
|                  | |          | F~       | F~       |          |    |
|                  | |          | UL\_low~ | DL\_low~ |          |    |
|                  | |          | --       | --       |          |    |
|                  | |          | F~U      | F~D      |          |    |
|                  | |          | L\_high~ | L\_high~ |          |    |
|                  | +==========+==========+==========+==========+    |
|                  | | n1       | 1920 MHz | 2110 MHz | FDD      |    |
|                  | |          | -- 1980  | -- 2170  |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n2       | 1850 MHz | 1930 MHz | FDD      |    |
|                  | |          | -- 1910  | -- 1990  |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n3       | 1710 MHz | 1805 MHz | FDD      |    |
|                  | |          | -- 1785  | -- 1880  |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n5       | 824 MHz  | 869 MHz  | FDD      |    |
|                  | |          | -- 849   | -- 894   |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n7       | 2500 MHz | 2620 MHz | FDD      |    |
|                  | |          | -- 2570  | -- 2690  |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n8       | 880 MHz  | 925 MHz  | FDD      |    |
|                  | |          | -- 915   | -- 960   |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n12      | 699 MHz  | 729 MHz  | FDD      |    |
|                  | |          | -- 716   | -- 746   |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n20      | 832 MHz  | 791 MHz  | FDD      |    |
|                  | |          | -- 862   | -- 821   |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n25      | 1850 MHz | 1930 MHz | FDD      |    |
|                  | |          | -- 1915  | -- 1995  |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n28      | 703 MHz  | 758 MHz  | FDD      |    |
|                  | |          | -- 748   | -- 803   |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n34      | 2010 MHz | 2010 MHz | TDD      |    |
|                  | |          | -- 2025  | -- 2025  |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n38      | 2570 MHz | 2570 MHz | TDD      |    |
|                  | |          | -- 2620  | -- 2620  |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n39      | 1880 MHz | 1880 MHz | TDD      |    |
|                  | |          | -- 1920  | -- 1920  |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n40      | 2300 MHz | 2300 MHz | TDD      |    |
|                  | |          | -- 2400  | -- 2400  |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n41      | 2496 MHz | 2496 MHz | TDD      |    |
|                  | |          | -- 2690  | -- 2690  |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n50      | 1432 MHz | 1432 MHz | TDD      |    |
|                  | |          | -- 1517  | -- 1517  |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n51      | 1427 MHz | 1427 MHz | TDD      |    |
|                  | |          | -- 1432  | -- 1432  |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n66      | 1710 MHz | 2110 MHz | FDD      |    |
|                  | |          | -- 1780  | -- 2200  |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n70      | 1695 MHz | 1995 MHz | FDD      |    |
|                  | |          | -- 1710  | -- 2020  |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n71      | 663 MHz  | 617 MHz  | FDD      |    |
|                  | |          | -- 698   | -- 652   |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n74      | 1427 MHz | 1475 MHz | FDD      |    |
|                  | |          | -- 1470  | -- 1518  |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n75      | N/A      | 1432 MHz | SDL      |    |
|                  | |          |          | -- 1517  |          |    |
|                  | |          |          | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n76      | N/A      | 1427 MHz | SDL      |    |
|                  | |          |          | -- 1432  |          |    |
|                  | |          |          | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n77      | 3300 MHz | 3300 MHz | TDD      |    |
|                  | |          | -- 4200  | -- 4200  |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n78      | 3300 MHz | 3300 MHz | TDD      |    |
|                  | |          | -- 3800  | -- 3800  |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n79      | 4400 MHz | 4400 MHz | TDD      |    |
|                  | |          | -- 5000  | -- 5000  |          |    |
|                  | |          | MHz      | MHz      |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n80      | 1710 MHz | N/A      | SUL      |    |
|                  | |          | -- 1785  |          |          |    |
|                  | |          | MHz      |          |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n81      | 880 MHz  | N/A      | SUL      |    |
|                  | |          | -- 915   |          |          |    |
|                  | |          | MHz      |          |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n82      | 832 MHz  | N/A      | SUL      |    |
|                  | |          | -- 862   |          |          |    |
|                  | |          | MHz      |          |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n83      | 703 MHz  | N/A      | SUL      |    |
|                  | |          | -- 748   |          |          |    |
|                  | |          | MHz      |          |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n84      | 1920 MHz | N/A      | SUL      |    |
|                  | |          | -- 1980  |          |          |    |
|                  | |          | MHz      |          |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | | n86      | 1710 MHz | N/A      | SUL      |    |
|                  | |          | -- 1780  |          |          |    |
|                  | |          | MHz      |          |          |    |
|                  | +----------+----------+----------+----------+    |
|                  |                                                  |
|                  | *[24250 -- 52600 MHz:]{.underline}*              |
|                  |                                                  |
|                  | +--------------+--------------+-------------+    |
|                  | | NR           | Uplink (UL)  | Duplex Mode |    |
|                  | | *operating   | and Downlink |             |    |
|                  | | band*        | (DL)         |             |    |
|                  | |              | *operating   |             |    |
|                  | |              | band*\       |             |    |
|                  | |              | BS           |             |    |
|                  | |              | trans        |             |    |
|                  | |              | mit/receive\ |             |    |
|                  | |              | UE           |             |    |
|                  | |              | tran         |             |    |
|                  | |              | smit/receive |             |    |
|                  | |              |              |             |    |
|                  | |              | F~UL\_low~   |             |    |
|                  | |              | --           |             |    |
|                  | |              | F~UL\_high~  |             |    |
|                  | |              |              |             |    |
|                  | |              | F~DL\_low~   |             |    |
|                  | |              | --           |             |    |
|                  | |              | F~DL\_high~  |             |    |
|                  | +==============+==============+=============+    |
|                  | | n257         | 26500 MHz -- | TDD         |    |
|                  | |              | 29500 MHz    |             |    |
|                  | +--------------+--------------+-------------+    |
|                  | | n258         | 24250 MHz -- | TDD         |    |
|                  | |              | 27500 MHz    |             |    |
|                  | +--------------+--------------+-------------+    |
|                  | | n260         | 37000 MHz -- | TDD         |    |
|                  | |              | 40000 MHz    |             |    |
|                  | +--------------+--------------+-------------+    |
|                  | | n261         | 27500 MHz -- | TDD         |    |
|                  | |              | 28350 MHz    |             |    |
|                  | +--------------+--------------+-------------+    |
|                  |                                                  |
|                  | *Additional frequency bands can be introduced in |
|                  | the future in release independent manner.        |
|                  | Support for frequency bands above 52600 MHz is   |
|                  | under study, and the support for frequency bands |
|                  | within 6000 MHz to 24250 MHz is planned to be    |
|                  | studied.*                                        |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *The following frequency bands are currently     |
|                  | specified, in accordance with spectrum           |
|                  | requirements defined by Report ITU-R M.2411-0.   |
|                  | Introduction of other ITU-R IMT identified bands |
|                  | are not precluded in the future. 3GPP            |
|                  | technologies are also defined as appropriate to  |
|                  | operate in other frequency arrangements and      |
|                  | bands. Detailed information on the following     |
|                  | bands can be found in \[36.101\] sub-clause      |
|                  | 5.5.*                                            |
|                  |                                                  |
|                  | *[450 -- 6000 MHz:]{.underline}*                 |
|                  |                                                  |
|                  |   ----------------------------                   |
|                  | ------------------------ ----------------------- |
|                  | ------ ------------------------------- --------- |
|                  | ---- ------------ -------- ------------ -------- |
|                  |   LTE (E‑UTRA) Operati                           |
|                  | ng Band                          Uplink (UL) ope |
|                  | rating band\   Downlink (DL) operating band\   D |
|                  | uplex Mode                                       |
|                  |                                                  |
|                  |                                  BS receive\     |
|                  |                BS transmit\                      |
|                  |                                                  |
|                  |                                                  |
|                  |                                  UE transmit     |
|                  |                UE receive                        |
|                  |                                                  |
|                  |                                                  |
|                  |                                                  |
|                  |                                  F~UL\_low~ -- F |
|                  | ~UL\_high~     F~DL\_low~ -- F~DL\_high~         |
|                  |                                                  |
|                  |                                                  |
|                  |   1                                              |
|                  |                               1920 MHz           |
|                  |             --                              1980 |
|                  |  MHz      2110 MHz     --       2170 MHz     FDD |
|                  |                                                  |
|                  |   2                                              |
|                  |                               1850 MHz           |
|                  |             --                              1910 |
|                  |  MHz      1930 MHz     --       1990 MHz     FDD |
|                  |                                                  |
|                  |   3                                              |
|                  |                               1710 MHz           |
|                  |             --                              1785 |
|                  |  MHz      1805 MHz     --       1880 MHz     FDD |
|                  |                                                  |
|                  |   4                                              |
|                  |                               1710 MHz           |
|                  |             --                              1755 |
|                  |  MHz      2110 MHz     --       2155 MHz     FDD |
|                  |                                                  |
|                  |   5                                              |
|                  |                               824 MHz            |
|                  |             --                              849  |
|                  | MHz       869 MHz      --       894MHz       FDD |
|                  |                                                  |
|                  |   6^1^                                           |
|                  |                               830 MHz            |
|                  |             --                              840  |
|                  | MHz       875 MHz      --       885 MHz      FDD |
|                  |                                                  |
|                  |   7                                              |
|                  |                               2500 MHz           |
|                  |             --                              2570 |
|                  |  MHz      2620 MHz     --       2690 MHz     FDD |
|                  |                                                  |
|                  |   8                                              |
|                  |                               880 MHz            |
|                  |             --                              915  |
|                  | MHz       925 MHz      --       960 MHz      FDD |
|                  |                                                  |
|                  |   9                                              |
|                  |                               1749.9 MHz         |
|                  |             --                              1784 |
|                  | .9 MHz    1844.9 MHz   --       1879.9 MHz   FDD |
|                  |                                                  |
|                  |   10                                             |
|                  |                               1710 MHz           |
|                  |             --                              1770 |
|                  |  MHz      2110 MHz     --       2170 MHz     FDD |
|                  |                                                  |
|                  |   11                                             |
|                  |                               1427.9 MHz         |
|                  |             --                              1447 |
|                  | .9 MHz    1475.9 MHz   --       1495.9 MHz   FDD |
|                  |                                                  |
|                  |   12                                             |
|                  |                               699 MHz            |
|                  |             --                              716  |
|                  | MHz       729 MHz      --       746 MHz      FDD |
|                  |                                                  |
|                  |   13                                             |
|                  |                               777 MHz            |
|                  |             --                              787  |
|                  | MHz       746 MHz      --       756 MHz      FDD |
|                  |                                                  |
|                  |   14                                             |
|                  |                               788 MHz            |
|                  |             --                              798  |
|                  | MHz       758 MHz      --       768 MHz      FDD |
|                  |                                                  |
|                  |   17                                             |
|                  |                               704 MHz            |
|                  |             --                              716  |
|                  | MHz       734 MHz      --       746 MHz      FDD |
|                  |                                                  |
|                  |   18                                             |
|                  |                               815 MHz            |
|                  |             --                              830  |
|                  | MHz       860 MHz      --       875 MHz      FDD |
|                  |                                                  |
|                  |   19                                             |
|                  |                               830 MHz            |
|                  |             --                              845  |
|                  | MHz       875 MHz      --       890 MHz      FDD |
|                  |                                                  |
|                  |   20                                             |
|                  |                               832 MHz            |
|                  |             --                              862  |
|                  | MHz       791 MHz      --       821 MHz      FDD |
|                  |                                                  |
|                  |   21                                             |
|                  |                               1447.9 MHz         |
|                  |             --                              1462 |
|                  | .9 MHz    1495.9 MHz   --       1510.9 MHz   FDD |
|                  |                                                  |
|                  |   22                                             |
|                  |                               3410 MHz           |
|                  |             --                              3490 |
|                  |  MHz      3510 MHz     --       3590 MHz     FDD |
|                  |                                                  |
|                  |   23^1^                                          |
|                  |                               2000 MHz           |
|                  |             --                              2020 |
|                  |  MHz      2180 MHz     --       2200 MHz     FDD |
|                  |                                                  |
|                  |   24                                             |
|                  |                               1626.5 MHz         |
|                  |             --                              1660 |
|                  | .5 MHz    1525 MHz     --       1559 MHz     FDD |
|                  |                                                  |
|                  |   25                                             |
|                  |                               1850 MHz           |
|                  |             --                              1915 |
|                  |  MHz      1930 MHz     --       1995 MHz     FDD |
|                  |                                                  |
|                  |   26                                             |
|                  |                               814 MHz            |
|                  |             --                              849  |
|                  | MHz       859 MHz      --       894 MHz      FDD |
|                  |                                                  |
|                  |   27                                             |
|                  |                               807 MHz            |
|                  |             --                              824  |
|                  | MHz       852 MHz      --       869 MHz      FDD |
|                  |                                                  |
|                  |   28                                             |
|                  |                               703 MHz            |
|                  |             --                              748  |
|                  | MHz       758 MHz      --       803 MHz      FDD |
|                  |                                                  |
|                  |   29                                             |
|                  |                                  N/A             |
|                  |                717 MHz                         - |
|                  | -            728 MHz      FDD^1^                 |
|                  |                                                  |
|                  |   30^15^                                         |
|                  |                               2305 MHz           |
|                  |             --                              2315 |
|                  |  MHz      2350 MHz     --       2360 MHz     FDD |
|                  |                                                  |
|                  |   31                                             |
|                  |                               452.5 MHz          |
|                  |             --                              457. |
|                  | 5 MHz     462.5 MHz    --       467.5 MHz    FDD |
|                  |                                                  |
|                  |   32                                             |
|                  |                                                  |
|                  |          N/A                                     |
|                  |        1452 MHz     --       1496 MHz     FDD^1^ |
|                  |                                                  |
|                  |   33                                             |
|                  |                               1900 MHz           |
|                  |             --                              1920 |
|                  |  MHz      1900 MHz     --       1920 MHz     TDD |
|                  |                                                  |
|                  |   34                                             |
|                  |                               2010 MHz           |
|                  |             --                              2025 |
|                  |  MHz      2010 MHz     --       2025 MHz     TDD |
|                  |                                                  |
|                  |   35                                             |
|                  |                               1850 MHz           |
|                  |             --                              1910 |
|                  |  MHz      1850 MHz     --       1910 MHz     TDD |
|                  |                                                  |
|                  |   36                                             |
|                  |                               1930 MHz           |
|                  |             --                              1990 |
|                  |  MHz      1930 MHz     --       1990 MHz     TDD |
|                  |                                                  |
|                  |   37                                             |
|                  |                               1910 MHz           |
|                  |             --                              1930 |
|                  |  MHz      1910 MHz     --       1930 MHz     TDD |
|                  |                                                  |
|                  |   38                                             |
|                  |                               2570 MHz           |
|                  |             --                              2620 |
|                  |  MHz      2570 MHz     --       2620 MHz     TDD |
|                  |                                                  |
|                  |   39                                             |
|                  |                               1880 MHz           |
|                  |             --                              1920 |
|                  |  MHz      1880 MHz     --       1920 MHz     TDD |
|                  |                                                  |
|                  |   40                                             |
|                  |                               2300 MHz           |
|                  |             --                              2400 |
|                  |  MHz      2300 MHz     --       2400 MHz     TDD |
|                  |                                                  |
|                  |   41                                             |
|                  |                               2496 MHz           |
|                  |                                             2690 |
|                  |  MHz      2496 MHz              2690 MHz     TDD |
|                  |                                                  |
|                  |   42                                             |
|                  |                               3400 MHz           |
|                  |             --                              3600 |
|                  |  MHz      3400 MHz     --       3600 MHz     TDD |
|                  |                                                  |
|                  |   43                                             |
|                  |                               3600 MHz           |
|                  |             --                              3800 |
|                  |  MHz      3600 MHz     --       3800 MHz     TDD |
|                  |                                                  |
|                  |   44                                             |
|                  |                               703 MHz            |
|                  |             --                              803  |
|                  | MHz       703 MHz      --       803 MHz      TDD |
|                  |                                                  |
|                  |   45                                             |
|                  |                               1447 MHz           |
|                  |             --                              1467 |
|                  |  MHz      1447 MHz     --       1467 MHz     TDD |
|                  |                                                  |
|                  |   46                                             |
|                  |                            5150 MHz              |
|                  |          --                              5925 MH |
|                  | z      5150 MHz     --       5925 MHz     TDD^1^ |
|                  |                                                  |
|                  |   47                                             |
|                  |                            5855 MHz              |
|                  |          --                              5925 MH |
|                  | z      5855 MHz     --       5925 MHz     TDD^1^ |
|                  |                                                  |
|                  |   48                                             |
|                  |                               3550 MHz           |
|                  |             --                              3700 |
|                  |  MHz      3550 MHz     --       3700 MHz     TDD |
|                  |                                                  |
|                  |   49                                             |
|                  |                            3550 MHz              |
|                  |          --                              3700 MH |
|                  | z      3550 MHz     --       3700 MHz     TDD^1^ |
|                  |                                                  |
|                  |   50                                             |
|                  |                            1432 MHz              |
|                  |          \-                              1517 MH |
|                  | z      1432 MHz     \-       1517 MHz     TDD^1^ |
|                  |                                                  |
|                  |   51                                             |
|                  |                            1427 MHz              |
|                  |          \-                              1432 MH |
|                  | z      1427 MHz     \-       1432 MHz     TDD^1^ |
|                  |                                                  |
|                  |   52                                             |
|                  |                               3300 MHz           |
|                  |             \-                              3400 |
|                  |  MHz      3300 MHz     \-       3400 MHz     TDD |
|                  |                                                  |
|                  |   65                                             |
|                  |                               1920 MHz           |
|                  |             --                              2010 |
|                  |  MHz      2110 MHz     --       2200 MHz     FDD |
|                  |                                                  |
|                  |   66                                             |
|                  |                            1710 MHz              |
|                  |          --                              1780 MH |
|                  | z      2110 MHz     --       2200 MHz     FDD^1^ |
|                  |                                                  |
|                  |   67                                             |
|                  |                                                  |
|                  |          N/A                                     |
|                  |        738 MHz      --       758 MHz      FDD^1^ |
|                  |                                                  |
|                  |   68                                             |
|                  |                               698 MHz            |
|                  |             --                              728  |
|                  | MHz       753 MHz      --       783 MHz      FDD |
|                  |                                                  |
|                  |   69                                             |
|                  |                                  N/A             |
|                  |                2570 MHz                        - |
|                  | -            2620 MHz     FDD^1^                 |
|                  |                                                  |
|                  |   70                                             |
|                  |                            1695 MHz              |
|                  |          --                              1710 MH |
|                  | z      1995 MHz     --       2020 MHz     FDD^1^ |
|                  |                                                  |
|                  |   71                                             |
|                  |                               663 MHz            |
|                  |             --                              698  |
|                  | MHz       617 MHz      --       652 MHz      FDD |
|                  |                                                  |
|                  |   72                                             |
|                  |                               451 MHz            |
|                  |             --                              456  |
|                  | MHz       461 MHz      --       466 MHz      FDD |
|                  |                                                  |
|                  |   73                                             |
|                  |                               450 MHz            |
|                  |             --                              455  |
|                  | MHz       460 MHz      --       465 MHz      FDD |
|                  |                                                  |
|                  |   74                                             |
|                  |                               1427 MHz           |
|                  |             --                              1470 |
|                  |  MHz      1475 MHz     --       1518 MHz     FDD |
|                  |                                                  |
|                  |   75                                             |
|                  |                                                  |
|                  |          N/A                                     |
|                  |        1432 MHz     --       1517 MHz     FDD^1^ |
|                  |                                                  |
|                  |   76                                             |
|                  |                                                  |
|                  |          N/A                                     |
|                  |        1427 MHz     --       1432 MHz     FDD^1^ |
|                  |                                                  |
|                  |   85                                             |
|                  |                               698 MHz            |
|                  |             --                              716  |
|                  | MHz       728 MHz      --       746 MHz      FDD |
|                  |                                                  |
|                  |   NOTE 1: See details                            |
|                  | in Table 8.2.2-1 in TS 36.101.                   |
|                  |                                                  |
|                  |                                                  |
|                  |   ----------------------------                   |
|                  | ------------------------ ----------------------- |
|                  | ------ ------------------------------- --------- |
|                  | ---- ------------ -------- ------------ -------- |
|                  |                                                  |
|                  | *For NB-IoT, Category NB1 and NB2 are designed   |
|                  | to operate in band 1, 2, 3, 4, 5, 8, 11, 12, 13, |
|                  | 17, 18, 19, 20, 21, 25, 26, 28, 31, 41, 66, 70,  |
|                  | 71, 72 and 74 in the above table. See more       |
|                  | details in \[36.101\] sub-clause 5.5F.*          |
|                  |                                                  |
|                  | *For eMTC, UE category M1 and M2 is designed to  |
|                  | operate in band 1, 2, 3, 4, 5, 7, 8, 11, 12, 13, |
|                  | 14, 18, 19, 20, 21, 25, 26, 27, 28, 31, 39, 40,  |
|                  | 41, 66, 71, 72 and 74 in the above table. See    |
|                  | more details in \[36.101\] sub-clause 5.5E.*     |
|                  |                                                  |
|                  | *For V2X communication, the bands can be found   |
|                  | in \[36.101\] sub-clause 5.5G.*                  |
+------------------+--------------------------------------------------+
| 5.2.3.2.8.4      | What is the minimum amount of spectrum required  |
|                  | to deploy a contiguous network, including        |
|                  | guardbands (MHz)?                                |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *The minimum amount of paired spectrum is 2 x 5  |
|                  | MHz. The minimum amount of unpaired spectrum is  |
|                  | 5 MHz.*                                          |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *The minimum amount of paired spectrum is 2 x    |
|                  | 1.4 MHz, and the minimum amount of unpaired      |
|                  | spectrum is 1.4 MHz, except for NB-IoT.*         |
|                  |                                                  |
|                  | *For NB-IoT, the minimum amount of unpaired      |
|                  | spectrum is 0.2 MHz.*                            |
+------------------+--------------------------------------------------+
| 5.2.3.2.8.5      | What are the minimum and maximum transmission    |
|                  | bandwidth (MHz) measured at the 3 dB down        |
|                  | points?                                          |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *The 3 dB bandwidth is not part of the           |
|                  | specifications, however:*                        |
|                  |                                                  |
|                  | -   *The minimum 99% channel bandwidth (occupied |
|                  |     bandwidth of single component carrier) is*   |
|                  |                                                  |
|                  |     -   *5 MHz for frequency range 450 -- 6000   |
|                  |         MHz;*                                    |
|                  |                                                  |
|                  |     -   *50 MHz for frequency range 24250 --     |
|                  |         52600 MHz*                               |
|                  |                                                  |
|                  | -   *The maximum 99% channel bandwidth (occupied |
|                  |     bandwidth of single component carrier) is*   |
|                  |                                                  |
|                  |     -   *100 MHz for frequency range 450 -- 6000 |
|                  |         MHz;*                                    |
|                  |                                                  |
|                  |     -   *400 MHz for frequency range 24250 --    |
|                  |         52600 MHz.*                              |
|                  |                                                  |
|                  | -   *Multiple component carriers can be          |
|                  |     aggregated to achieve up to 6.4 GHz of       |
|                  |     transmission bandwidth.*                     |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *The 3 dB bandwidth is not part of the           |
|                  | specifications, however:*                        |
|                  |                                                  |
|                  | -   *The minimum 99% channel bandwidth (occupied |
|                  |     bandwidth of single component carrier) is    |
|                  |     1.4 MHz.*                                    |
|                  |                                                  |
|                  | -   *The maximum 99% channel bandwidth (occupied |
|                  |     bandwidth of single component carrier) is 20 |
|                  |     MHz.*                                        |
|                  |                                                  |
|                  | -   *Multiple component carriers can be          |
|                  |     aggregated to achieve up to 640 MHz of       |
|                  |     transmission bandwidth.*                     |
|                  |                                                  |
|                  | *For NB-IoT, the 99% channel bandwidth is 0.2    |
|                  | MHz.*                                            |
+------------------+--------------------------------------------------+
| 5.2.3.2.8.6      | What duplexing scheme(s) is (are) described in   |
|                  | this template?\                                  |
|                  | (e.g. TDD, FDD or half-duplex FDD).              |
|                  |                                                  |
|                  | Provide the description such as:                 |
|                  |                                                  |
|                  | -- What duplexing scheme(s) can be applied to    |
|                  | paired spectrum? Provide the details (see below  |
|                  | as some examples).                               |
|                  |                                                  |
|                  | -- What duplexing scheme(s) can be applied to    |
|                  | un-paired spectrum? Provide the details (see     |
|                  | below as some examples).                         |
|                  |                                                  |
|                  | Describe details such as:                        |
|                  |                                                  |
|                  | -- What is the minimum (up/down) frequency       |
|                  | separation in case\                              |
|                  | of full- and half-duplex FDD?                    |
|                  |                                                  |
|                  | -- What is the requirement of transmit/receive   |
|                  | isolation in case\                               |
|                  | of full- an half-duplex FDD? Does the RIT        |
|                  | require a duplexer\                              |
|                  | in either the UE or base station?                |
|                  |                                                  |
|                  | -- What is the minimum (up/down) time separation |
|                  | in case of TDD?                                  |
|                  |                                                  |
|                  | -- Whether the DL/UL ratio variable for TDD?     |
|                  | What is the DL/UL ratio supported? If the DL/UL  |
|                  | ratio for TDD is variable, what would be the     |
|                  | coexistence criteria for adjacent cells?         |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *NR supports paired and unpaired spectrum and    |
|                  | allows FDD operation on a paired spectrum,       |
|                  | different transmission directions in either part |
|                  | of a paired spectrum, TDD operation on an        |
|                  | unpaired spectrum where the transmission         |
|                  | direction of time resources is not dynamically   |
|                  | changed, and TDD operation on an unpaired        |
|                  | spectrum where the transmission direction of     |
|                  | most time resources can be dynamically changing. |
|                  | DL and UL transmission directions for data can   |
|                  | be dynamically assigned on a per-slot basis.*    |
|                  |                                                  |
|                  | -   *For FDD operation, it supports full-duplex  |
|                  |     FDD.*                                        |
|                  |                                                  |
|                  |     -   *For both base station and terminal, a   |
|                  |         duplexer is needed for full-duplex FDD.* |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   *For full-duplex FDD, the required           |
|                  |     transmit/receive isolation is a UE function  |
|                  |     of; the Tx emission mask (emission level on  |
|                  |     the Rx frequency) , the TX-Rx frequency      |
|                  |     spacing , the Tx- Rx duplex filter           |
|                  |     isolation, the TX and RX configuration (RB   |
|                  |     location, RB power and RB allocation) and    |
|                  |     the required Rx desense criteria. For the    |
|                  |     supported operating bands, the parameters    |
|                  |     including the minimum (up/down) Tx to Rx     |
|                  |     frequency separation and the minimum Tx-Rx   |
|                  |     band gap are being defined in 3GPP.*         |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   *For different transmission directions in    |
|                  |     either part of a paired spectrum, a duplexer |
|                  |     is needed for both base station and the      |
|                  |     terminal. The required frequency separation  |
|                  |     between the paired spectrum is the same as   |
|                  |     full-duplex FDD. The supported DL/UL         |
|                  |     resource assignment configurations for TDD   |
|                  |     can be applied.*                             |
|                  |                                                  |
|                  | -   *For TDD operation, it supports variable     |
|                  |     DL/UL resource assignment ranging in a radio |
|                  |     frame from 10/0 (ten downlink slots and no   |
|                  |     uplink slot) to 0/10 (no downlink slot and   |
|                  |     ten uplink slots). It also supports a slot   |
|                  |     with DL part and UL part. DL and UL          |
|                  |     transmission directions for data can be      |
|                  |     dynamically assigned on a per-slot basis.    |
|                  |     Adjacent cells using the same carrier        |
|                  |     frequency can use the same or different      |
|                  |     DL/UL resource assignment configuration.*    |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   *For both the base station and the terminal, |
|                  |     duplexer is not needed.*                     |
|                  |                                                  |
|                  | -   *The TDD guard time is configurable to meet  |
|                  |     different deployment scenarios.*             |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *LTE supports paired and unpaired spectrum and   |
|                  | allows FDD operation on a paired spectrum and    |
|                  | TDD operation on an unpaired spectrum.*          |
|                  |                                                  |
|                  | -   *For FDD operation, it supports both         |
|                  |     half-duplex and full-duplex FDD.*            |
|                  |                                                  |
|                  |     -   *For the base station, a duplexer is     |
|                  |         needed for half-duplex/full-duplex FDD.  |
|                  |         For the terminal, a duplexer is needed   |
|                  |         for full-duplex FDD only.*               |
|                  |                                                  |
|                  |     -   *For full-duplex FDD, the required       |
|                  |         transmit/receive isolation is a UE       |
|                  |         function of; the Tx emission mask        |
|                  |         (emission level on the Rx frequency) ,   |
|                  |         the TX-Rx frequency spacing , the Tx- Rx |
|                  |         duplex filter isolation, the TX and RX   |
|                  |         configuration (RB location, RB power and |
|                  |         RB allocation) and the required Rx       |
|                  |         desense criteria. For the supported RIT  |
|                  |         operating bands, the following           |
|                  |         parameters are defined in \[36.101\]:*   |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   *the minimum (up/down) Tx to Rx frequency    |
|                  |     separation is 10 MHz*                        |
|                  |                                                  |
|                  | -   *the minimum Tx-Rx band gap is 10 MHz*       |
|                  |                                                  |
|                  |     -   *For half-duplex FDD, for the UE there   |
|                  |         is no specified transmit / receive       |
|                  |         isolation due half duplex mode.*         |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   *For TDD operation, it supports variable     |
|                  |     DL/UL ratio ranging from 9/1 (nine downlink  |
|                  |     subframes and one uplink subframe) to 4/6    |
|                  |     (four downlink subframes and six uplink      |
|                  |     subframes\*). Adjacent cells using the same  |
|                  |     carrier frequency can use the same or        |
|                  |     different DL/UL configuration.*              |
|                  |                                                  |
|                  | *\* This is based on an assumption that the      |
|                  | "special subframe (see \[36.211\] sub-clause     |
|                  | 4.2) is counted as a DL subframe.*               |
|                  |                                                  |
|                  | -   *For both the base station and the terminal, |
|                  |     duplexer is not needed.*                     |
|                  |                                                  |
|                  | -   *The TDD guard time is configurable in the   |
|                  |     range from one to ten OFDM symbols           |
|                  |     (approximately 70 to 700 µs) to meet         |
|                  |     different deployment scenarios.*             |
|                  |                                                  |
|                  | *For NB-IoT, Half-duplex FDD and TDD are         |
|                  | supported. The terminal does not need a          |
|                  | duplexer, and there is no specified transmit /   |
|                  | receive isolation due to half-duplex mode.*      |
+------------------+--------------------------------------------------+
| **5.2.3.2.9**    | **Support of Advanced antenna capabilities**     |
+------------------+--------------------------------------------------+
| 5.2.3.2.9.1      | Fully describe the multi-antenna systems (e.g.   |
|                  | massive MIMO) supported in the UE, base station, |
|                  | or both that can be used and/or must be used;    |
|                  | characterize their impacts on systems            |
|                  | performance; e.g., does the RIT have the         |
|                  | capability for the use of:                       |
|                  |                                                  |
|                  | -- spatial multiplexing techniques,              |
|                  |                                                  |
|                  | -- spatial transmit diversity techniques,        |
|                  |                                                  |
|                  | -- beam-forming techniques (e.g., analog,        |
|                  | digital, hybrid).                                |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *The multi-antenna systems in NR supports the    |
|                  | following MIMO transmission schemes at both the  |
|                  | UE and the base station:*                        |
|                  |                                                  |
|                  | -   *Spatial multiplexing with DM-RS based       |
|                  |     closed loop and semi-open loop transmission  |
|                  |     schemes are supported. For DL, codebook and  |
|                  |     reciprocity based precoding are supported.   |
|                  |     For UL, codebook and non-codebook based      |
|                  |     transmission are supported.*                 |
|                  |                                                  |
|                  | -   *Specification transparent diversity schemes |
|                  |     can also be supported by gNB                 |
|                  |     implementations.*                            |
|                  |                                                  |
|                  | -   *Hybrid beamforming including both digital   |
|                  |     and analog beamforming is supported at the   |
|                  |     UE and at the base station.*                 |
|                  |                                                  |
|                  | ***[For LTE component RIT]{.underline}***        |
|                  |                                                  |
|                  | *The multi-antenna systems in LTE supports the   |
|                  | following MIMO transmission scheme at both the   |
|                  | UE and the base station:*                        |
|                  |                                                  |
|                  | -   *Spatial multiplexing with CRS and UE        |
|                  |     specific RS based closed loop, open loop and |
|                  |     semi-open loop transmission schemes are      |
|                  |     supported. Codebook and reciprocity based    |
|                  |     transmission is supported in DL. Codebook    |
|                  |     based transmission is supported in UL.*      |
|                  |                                                  |
|                  | -   *Spatial transmit diversity is supported     |
|                  |     based on space frequency block coding,       |
|                  |     frequency switched transmit diversity.       |
|                  |     Specification transparent diversity schemes  |
|                  |     are also supported by eNB implementations.*  |
|                  |                                                  |
|                  | -   *Hybrid beamforming including both digital   |
|                  |     and analog beamforming is supported at the   |
|                  |     base station. Digital beamforming is         |
|                  |     supported at the UE..*                       |
+------------------+--------------------------------------------------+
| 5.2.3.2.9.2      | How many antenna elements are supported by the   |
|                  | base station and UE for transmission and         |
|                  | reception? What is the antenna spacing (in       |
|                  | wavelengths)?                                    |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *NR supports {1, 2, 4, 8, 12, 16, 24, 32}        |
|                  | antenna ports in the DL and {1, 2, 4} antenna    |
|                  | ports in the UL.*                                |
|                  |                                                  |
|                  | *Base Station and UE support rectangular antenna |
|                  | arrays. The rectangular panel array antenna can  |
|                  | be described by the following tuple*             |
|                  | $(M_{g},N_{g},\ M,N,\ P)$*, where* $M_{g}$ *is   |
|                  | the number of panels in a column,* $N_{g}$ *is   |
|                  | the number of panels in row,* $M,N$ *are the     |
|                  | number of vertical, horizontal antenna elements  |
|                  | within a panel and* $P$ *is number of            |
|                  | polarizations per antenna element. The spacing   |
|                  | in vertical and horizontal dimensions between    |
|                  | the panels is specified by* $d_{g,V},\ d_{g,H}$  |
|                  | *and between antenna elements                    |
|                  | by*$\text{\ d}_{V},\ d_{H}$*.*                   |
|                  |                                                  |
|                  | *NR specification is flexible to support various |
|                  | antenna spacing, number of antenna elements,     |
|                  | antenna port layouts and antenna virtualization  |
|                  | approaches.*                                     |
|                  |                                                  |
|                  | ***[For LTE component RIT]{.underline}***        |
|                  |                                                  |
|                  | *LTE supports {1, 2, 4, 8, 12, 16, 20, 24, 28,   |
|                  | 32} antenna ports in the DL and {1, 2, 4}        |
|                  | antenna ports in the UL. Base Station and UE     |
|                  | support e.g. rectangular antenna arrays          |
|                  | described by the tuple*$\ (M,N,P)$*.*            |
|                  |                                                  |
|                  | ![                                               |
|                  | ](media/image2.emf){width="1.5916666666666666in" |
|                  | height="1.8833333333333333in"}                   |
|                  |                                                  |
|                  | $M,\ N$ *are the number of antenna elements in   |
|                  | the vertical and horizontal dimensions.* $P$ *is |
|                  | the number of polarizations per antenna element. |
|                  | Antenna elements are uniformly spaced in the     |
|                  | horizontal direction with a spacing of dH and in |
|                  | the vertical direction with a spacing of dV.*    |
|                  |                                                  |
|                  | *LTE supports various antenna spacing, antenna   |
|                  | port layouts and antenna virtualization          |
|                  | approaches.*                                     |
+------------------+--------------------------------------------------+
| 5.2.3.2.9.3      | Provide details on the antenna configuration     |
|                  | that is used in the self-evaluation.             |
|                  |                                                  |
|                  | *The information will be provided with self      |
|                  | evaluation results.*                             |
+------------------+--------------------------------------------------+
| 5.2.3.2.9.4      | If spatial multiplexing (MIMO) is supported,     |
|                  | does the proposal support (provide details if    |
|                  | supported)                                       |
|                  |                                                  |
|                  | -- Single-codeword (SCW) and/or multi-codeword   |
|                  | (MCW)                                            |
|                  |                                                  |
|                  | -- Open and/or closed loop MIMO                  |
|                  |                                                  |
|                  | -- Cooperative MIMO                              |
|                  |                                                  |
|                  | -- Single-user MIMO and/or multi-user MIMO.      |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *In NR, spatial multiplexing is supported with   |
|                  | the following options:*                          |
|                  |                                                  |
|                  | *Single codeword is supported for 1-4 layer      |
|                  | transmissions and two codewords are supported    |
|                  | for 5-8 layer transmissions in DL. Only single   |
|                  | codeword is supported for 1- 4 layer             |
|                  | transmissions in UL*                             |
|                  |                                                  |
|                  | *Closed loop MIMO is supported in NR, where for  |
|                  | demodulation of data, receiver does not require  |
|                  | knowledge of the precoding matrix used at the    |
|                  | transmitter.*                                    |
|                  |                                                  |
|                  | *Both single-user and multi-user MIMO are        |
|                  | supported. For the case of single-user MIMO      |
|                  | transmissions, up to 8 layers are supported in   |
|                  | DL and up to 4 layers are supported in UL. For   |
|                  | both DL and UL, multi-user MIMO up to 12         |
|                  | orthogonal DM-RS ports with up to 4 orthogonal   |
|                  | ports per UE are supported.*                     |
|                  |                                                  |
|                  | *NR supports coordinated multipoint              |
|                  | transmission/reception, which could be used to   |
|                  | implement different forms of cooperative         |
|                  | multi-antenna (MIMO) transmission schemes.*      |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *In LTE, spatial multiplexing is supported with  |
|                  | the following options:*                          |
|                  |                                                  |
|                  | *Single codeword is supported for single layer   |
|                  | transmissions and two codewords are supported    |
|                  | for 2-8 layer transmissions in DL. Single        |
|                  | codeword is supported for single layer           |
|                  | transmissions and two codewords are supported    |
|                  | for 2-4 layer transmissions in UL.*              |
|                  |                                                  |
|                  | *Both open and closed loop MIMO are supported in |
|                  | LTE*                                             |
|                  |                                                  |
|                  | *LTE supports single user MIMO with up to 8      |
|                  | layers per UE in DL and up to 4 layers per UE in |
|                  | UL. In DL, LTE supports MU-MIMO with up to       |
|                  | 4orthogonal UE specific RS ports and up to 2     |
|                  | orthogonal UE specific RS ports per UE. In UL,   |
|                  | up to 8 orthogonal UE specific RS ports and up   |
|                  | to 2 orthogonal UE specific RS ports per UE.*    |
|                  |                                                  |
|                  | *LTE supports coordinated multipoint             |
|                  | transmission/reception, which could be used to   |
|                  | implement different forms of cooperative         |
|                  | multi-antenna (MIMO) transmission schemes.*      |
+------------------+--------------------------------------------------+
| 5.2.3.2.9.5      | Other antenna technologies                       |
|                  |                                                  |
|                  | Does the RIT/SRIT support other antenna          |
|                  | technologies, for example:                       |
|                  |                                                  |
|                  | -- remote antennas,                              |
|                  |                                                  |
|                  | -- distributed antennas.                         |
|                  |                                                  |
|                  | If so, please describe.                          |
|                  |                                                  |
|                  | *The use of remote antennas and distributed      |
|                  | antennas is supported by NR and LTE.*            |
+------------------+--------------------------------------------------+
| 5.2.3.2.9.6      | Provide the antenna tilt angle used in the       |
|                  | self-evaluation.                                 |
|                  |                                                  |
|                  | *The information will be provided with self      |
|                  | evaluation results.*                             |
+------------------+--------------------------------------------------+
| **5.2.3.2.10**   | **Link adaptation and power control**            |
+------------------+--------------------------------------------------+
| 5.2.3.2.10.1     | Describe link adaptation techniques employed by  |
|                  | RIT/SRIT, including:                             |
|                  |                                                  |
|                  | -- the supported modulation and coding schemes,  |
|                  |                                                  |
|                  | -- the supporting channel quality measurements,  |
|                  | the reporting of these measurements, their       |
|                  | frequency and granularity.                       |
|                  |                                                  |
|                  | Provide details of any adaptive modulation and   |
|                  | coding schemes, including:                       |
|                  |                                                  |
|                  | -- Hybrid ARQ or other retransmission            |
|                  | mechanisms?                                      |
|                  |                                                  |
|                  | -- Algorithms for adaptive modulation and        |
|                  | coding, which are used in the self-evaluation.   |
|                  |                                                  |
|                  | -- Other schemes?                                |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *For data, the RIT supports dynamic indication   |
|                  | of*                                              |
|                  |                                                  |
|                  | 1.  *combinations of modulation scheme and       |
|                  |     target code rate and,*                       |
|                  |                                                  |
|                  | 2.  *the resource allocation in frequency and    |
|                  |     time (The resource allocation in frequency   |
|                  |     is within BWP)*                              |
|                  |                                                  |
|                  | *that the UE uses to determine the transport     |
|                  | block size where the possible combinations cover |
|                  | a large range of possible data and channel       |
|                  | coding rates. 28 different target coding rates   |
|                  | can be indicated (29 if 256QAM is not enabled)   |
|                  | and the target code rate range is 0.0293 to      |
|                  | 0.896.*                                          |
|                  |                                                  |
|                  | *In both downlink and uplink, link adaptation    |
|                  | (selection of modulation scheme and code rate)   |
|                  | is controlled by the base station. In the        |
|                  | downlink, the network selection of               |
|                  | modulation-scheme/code-rate combination can e.g. |
|                  | be based on channel state information (CSI)      |
|                  | reported by the terminals. The RIT features a    |
|                  | flexible CSI framework where the type of CSI,    |
|                  | reporting quantity, frequency-granularity and    |
|                  | time-domain behaviour can be configured. Both    |
|                  | periodic and aperiodic(triggered) reporting      |
|                  | modes are supported, controlled by the base      |
|                  | station, where the aperiodic reporting allows    |
|                  | the network to request which CSI-RS resources to |
|                  | report the CSI for. More details can be found in |
|                  | \[38.214\] section 5.2. In the uplink the base   |
|                  | station may measure either the traffic channel   |
|                  | or sounding reference signals and use this as    |
|                  | input to the link adaptation. More details can   |
|                  | be found in \[38.214\] section 6.2.1.*           |
|                  |                                                  |
|                  | *On the MAC layer, hybrid ARQ with               |
|                  | soft-combining between transmissions is          |
|                  | supported. Different redundancy versions can be  |
|                  | used for different transmissions. The modulation |
|                  | and coding scheme may be changed for             |
|                  | retransmissions. In order to minimize delay and  |
|                  | feedback, a set of parallel stop-and-wait        |
|                  | protocols are used. To correct possible residual |
|                  | errors, the MAC ARQ is complemented by a robust  |
|                  | selective-repeat ARQ protocol on the RLC layer.  |
|                  | More details are found in \[38.321\] and         |
|                  | \[38.322\].*                                     |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *For data, the RIT supports the modulation       |
|                  | schemes π*/2-*BPSK, QPSK, 16 QAM, 64 QAM, 256QAM |
|                  | and 1024QAM, and code rates between              |
|                  | approximately 0.1 and 0.9. Some 27 different     |
|                  | modulation-scheme/code-rate combinations exist.  |
|                  | This is valid for both downlink and uplink.*     |
|                  |                                                  |
|                  | *In both downlink and uplink, link adaptation    |
|                  | (selection of modulation scheme, code rate and   |
|                  | repetition number) is controlled by the base     |
|                  | station. In the downlink the network selection   |
|                  | of modulation-scheme/code-rate combination can   |
|                  | e.g. be based on Channel Quality Indicators      |
|                  | (CQIs) reported by the terminals. Several        |
|                  | different CQI modes exist, including             |
|                  | frequency-selective and wideband modes, periodic |
|                  | and aperiodic modes. The CQI mode is controlled  |
|                  | by the base station. In the uplink the base      |
|                  | station may measure either the traffic channel   |
|                  | or sounding reference signals and use this as    |
|                  | input to link adaptation. More details are found |
|                  | in \[36.213\]. UE reports its headroom to its    |
|                  | maximum power to assist the base station with    |
|                  | uplink link adaptation.*                         |
|                  |                                                  |
|                  | *On the MAC layer, hybrid ARQ with               |
|                  | soft-combining between transmissions is          |
|                  | supported. Different redundancy versions can be  |
|                  | used for different transmissions. The modulation |
|                  | scheme may be changed for retransmissions. In    |
|                  | order to minimize delay and feedback, a set of   |
|                  | parallel stop-and-wait protocols are used. To    |
|                  | correct possible residual errors, the MAC HARQ   |
|                  | is complemented by a robust selective-repeat ARQ |
|                  | protocol on the RLC layer. More details are      |
|                  | found in \[36.321\] and \[36.322\].*             |
|                  |                                                  |
|                  | *For NB-IoT π/2BPSK and QPSK modulation schemes  |
|                  | are supported. Transmissions of a transport      |
|                  | block can be mapped to between 1 and 10          |
|                  | subframes to adapt the code rate of the          |
|                  | transmission. In its most basic form the link    |
|                  | adaptation supports 116 alternative              |
|                  | modulation-scheme/code-rate combinations for the |
|                  | UL and 104 alternatives for the DL. To further   |
|                  | enhance the link robustness NB-IoT supports      |
|                  | repetition based transmission scheme using up to |
|                  | 2048 repetitions of each                         |
|                  | modulation-scheme/code-rate combination.*        |
|                  |                                                  |
|                  | *During the connection setup procedure NB-IoT    |
|                  | supports a basic UE feedback mechanism which     |
|                  | allows the base station to access the coupling   |
|                  | loss experienced by a UE. In connected mode HARQ |
|                  | and ARQ RLC/MAC feedback is supported in         |
|                  | similarity to LTE.*                              |
+------------------+--------------------------------------------------+
| 5.2.3.2.10.2     | Provide details of any power control scheme      |
|                  | included in the proposal, for example:           |
|                  |                                                  |
|                  | -- Power control step size (dB)                  |
|                  |                                                  |
|                  | -- Power control cycles per second               |
|                  |                                                  |
|                  | -- Power control dynamic range (dB)              |
|                  |                                                  |
|                  | -- Minimum transmit power level with power       |
|                  | control                                          |
|                  |                                                  |
|                  | -- Associated signalling and control messages.   |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *Uplink power control is independent for uplink  |
|                  | data(PUSCH), uplink control(PUCCH) and sounding  |
|                  | reference signal SRS. The uplink power control   |
|                  | is based on both signal-strength measurements    |
|                  | done by the terminal itself (open-loop power     |
|                  | control), as well as measurements by the base    |
|                  | station. The latter measurements are used to     |
|                  | generate power-control commands that are         |
|                  | subsequently fed back to the terminals as part   |
|                  | of the downlink control signaling (closed-loop   |
|                  | power control). Both absolute and relative       |
|                  | power-control commands are supported. There are  |
|                  | four available relative power adjustments ("step |
|                  | size") in case of relative power control, TBD.   |
|                  | For uplink data, multiple closed loop power      |
|                  | control processes can be configured, including   |
|                  | the possibility separate processes with          |
|                  | transmission beam indication. The time between   |
|                  | power-control commands for PUSCH and PUCCH is    |
|                  | the same as the scheduling periodicity for the   |
|                  | PUSCH and the PDSCH, respectively. More details  |
|                  | about uplink power control are found in          |
|                  | \[38.213\] section 7.*                           |
|                  |                                                  |
|                  | *Downlink power control is                       |
|                  | network-implementation specific and thus outside |
|                  | the scope of the specification. A simple and     |
|                  | efficient power control strategy is to transmit  |
|                  | with a constant output power. Variations in      |
|                  | channel conditions and interference levels are   |
|                  | adapted to by means of scheduling and link       |
|                  | adaptation.*                                     |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *The RIT uplink power control is based on both   |
|                  | signal-strength measurements done by the         |
|                  | terminal itself (open-loop power control), as    |
|                  | well as measurements by the base station. The    |
|                  | later measurements are used to generate          |
|                  | power-control commands that are subsequently fed |
|                  | back to the terminals as part of the downlink    |
|                  | control signaling (closed-loop power control).   |
|                  | Both absolute and relative power-control         |
|                  | commands are supported. The available relative   |
|                  | power adjustments ("step size") in case of       |
|                  | relative power control are \[-1 dB, 0 dB, +1 dB, |
|                  | +3 dB\]. The time between power-control commands |
|                  | can be down to 1ms, but even down to roughly 140 |
|                  | µs for sTTI. The minimum transmit power          |
|                  | requirement, -- 40dBm, yields a dynamic range of |
|                  | -40 to 23=63dB for a terminal with maximum power |
|                  | 23dBm. Higher power terminals with 26 dBm and 31 |
|                  | dBm maximum power are also supported increasing  |
|                  | the dynamic range accordingly. For eMTC and      |
|                  | NB-IoT maximum UE power supported are 14 dBm, 20 |
|                  | dBm and 23 dBm. NB-IoT only supports the         |
|                  | open-loop power control, with a constraint that  |
|                  | full power is used when the UE is commanded to   |
|                  | use 2 or more repetitions of a physical channel. |
|                  | More details about uplink power control are      |
|                  | found in \[36.213\].*                            |
|                  |                                                  |
|                  | *Downlink power control is, with the exception   |
|                  | for NB-IoT, network-implementation specific and  |
|                  | thus outside the scope of the specification. A   |
|                  | simple and efficient power control strategy is   |
|                  | to transmit with a constant output power.        |
|                  | Variations in channel conditions and             |
|                  | interference levels are adapted to by means of   |
|                  | scheduling and link adaptation rather than with  |
|                  | power control. For NB-IoT the network is         |
|                  | mandated to support at least 6 dB power boosting |
|                  | of the PRB carrying the synchronization and      |
|                  | broadcast signaling. The configured power        |
|                  | boosting value is signaled by the base station   |
|                  | to the terminals.*                               |
+------------------+--------------------------------------------------+
| **5.2.3.2.11**   | **Power classes**                                |
+------------------+--------------------------------------------------+
| 5.2.3.2.11.1     | *UE emitted power*                               |
+------------------+--------------------------------------------------+
| 5.2.3.2.11.1.1   | What is the radiated antenna power measured at   |
|                  | the antenna (dBm)?                               |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *For frequency range 1, the maximum output power |
|                  | is measured as the sum of the maximum output     |
|                  | power at each UE antenna connector. The maximum  |
|                  | output power is defined by UE power class as     |
|                  | following table.*                                |
|                  |                                                  |
|                  | \<UE maximum output power for frequency range    |
|                  | 1\>                                              |
|                  |                                                  |
|                  |   Power class                                    |
|                  |                                                  |
|                  |                  P~PowerClass~ (dBm)   Tolerance |
|                  |   -------------------------------------          |
|                  | ------------------------------------------------ |
|                  | -------------- --------------------- ----------- |
|                  |   2                                              |
|                  |                                                  |
|                  |                      26                    +2/-3 |
|                  |   3                                              |
|                  |                                                  |
|                  |                  23                    +2/-3\~-2 |
|                  |   Note 1: P~PowerClass~ is t                     |
|                  | he maximum UE power specified without taking int |
|                  | o account the tolerance                          |
|                  |                                                  |
|                  | *For frequency range 2, the maximum output power |
|                  | radiated by the UE for any transmission          |
|                  | bandwidth of NR carrier is defined as TRP (Total |
|                  | Radiated Power) and EIRP(Equivalent              |
|                  | Isotropically Radiated Power). Unlike UE power   |
|                  | class for frequency range 1, where each UE power |
|                  | class is specified as a nominal value with +/-   |
|                  | tolerance, UE power class for frequency range 2  |
|                  | specifies a UE minimum peak EIRP, minimum        |
|                  | spherical coverage EIRP, and UE maximum output   |
|                  | power limits for each power class as following   |
|                  | table. In particular, Power class 1 UE is used   |
|                  | for fixed wireless access (FWA).*                |
|                  |                                                  |
|                  | \<UE minimum peak EIRP for frequency range 2\>   |
|                  |                                                  |
|                  |                                                  |
|                  |                                           Min pe |
|                  | ak EIRP (dBm)                                    |
|                  |   -                                              |
|                  | ------------------------------------------------ |
|                  | -------------------------- --------------------- |
|                  |  --------------- --------------- --------------- |
|                  |                                                  |
|                  |  Operating band                                  |
|                  |                              Power class 1       |
|                  |    Power class 2   Power class 3   Power class 4 |
|                  |   n257                                           |
|                  |                                         40.0     |
|                  |               29              22.4            34 |
|                  |   n258                                           |
|                  |                                         40.0     |
|                  |               29              22.4            34 |
|                  |   n260                                           |
|                  |                                         38.0     |
|                  |                               20.6            31 |
|                  |   n261                                           |
|                  |                                         40.0     |
|                  |               29              22.4            34 |
|                  |   NOTE 1: Minimum peak EIRP is defin             |
|                  | ed as the lower limit without tolerance          |
|                  |                                                  |
|                  |                                                  |
|                  | \<UE minimum spherical coverage EIRP for         |
|                  | frequency range 2\>                              |
|                  |                                                  |
|                  |                                                  |
|                  |                                                  |
|                  |                                                  |
|                  |                                                  |
|                  |                             Min spherical covera |
|                  | ge EIRP (dBm)                                    |
|                  |   ----------------------                         |
|                  | ------------------------------------------------ |
|                  | ------------------------------------------------ |
|                  | ------------------------------------------------ |
|                  | ------------ ----------------------------------- |
|                  |  --------------- --------------- --------------- |
|                  |   Operating band                                 |
|                  |                                                  |
|                  |                                                  |
|                  |                                                  |
|                  |                Power class 1                     |
|                  |    Power class 2   Power class 3   Power class 4 |
|                  |   n257                                           |
|                  |                                                  |
|                  |                                                  |
|                  |                                                  |
|                  |                      32.0\@85%                   |
|                  |          18\@60%         11.5\@50%       25\@20% |
|                  |   n258                                           |
|                  |                                                  |
|                  |                                                  |
|                  |                                                  |
|                  |                      32.0\@85%                   |
|                  |          18\@60%         11.5\@50%       25\@20% |
|                  |   n260                                           |
|                  |                                                  |
|                  |                                                  |
|                  |                                                  |
|                  |                      30.0\@85%                   |
|                  |                          8\@50%          19\@20% |
|                  |   n261                                           |
|                  |                                                  |
|                  |                                                  |
|                  |                                                  |
|                  |                      32.0\@85%                   |
|                  |          18\@60%         11.5\@50%       25\@20% |
|                  |   NOTE 1:                                        |
|                  |  Minimum spherical coverage EIRP is defined as t |
|                  | he lower limit without tolerance at x% of the di |
|                  | stribution of radiated power measured over the f |
|                  | ull sphere around the UE.                        |
|                  |                                                  |
|                  |                                                  |
|                  | \<UE maximum output power limits for frequency   |
|                  | range 2\>                                        |
|                  |                                                  |
|                  | <table>                                          |
|                  | <thead>                                          |
|                  | <tr class="header">                              |
|                  | <th>Operating band</th>                          |
|                  | <th>Power class 1</th>                           |
|                  | <th>Power class 2</th>                           |
|                  | <th>Power class 3</th>                           |
|                  | <th>Power class 4</th>                           |
|                  | <th></th>                                        |
|                  | <th></th>                                        |
|                  | <th></th>                                        |
|                  | <th></th>                                        |
|                  | </tr>                                            |
|                  | </thead>                                         |
|                  | <tbody>                                          |
|                  | <tr class="odd">                                 |
|                  | <td></td>                                        |
|                  | <td>Max TRP (dBm)</td>                           |
|                  | <td><p>Max EIRP</p>                              |
|                  | <p>(dBm)</p></td>                                |
|                  | <td>Max TRP (dBm)</td>                           |
|                  | <td><p>Max EIRP</p>                              |
|                  | <p>(dBm)</p></td>                                |
|                  | <td>Max TRP (dBm)</td>                           |
|                  | <td><p>Max EIRP</p>                              |
|                  | <p>(dBm)</p></td>                                |
|                  | <td>Max TRP (dBm)</td>                           |
|                  | <td><p>Max EIRP</p>                              |
|                  | <p>(dBm)</p></td>                                |
|                  | </tr>                                            |
|                  | <tr class="even">                                |
|                  | <td>n257</td>                                    |
|                  | <td>35</td>                                      |
|                  | <td>55</td>                                      |
|                  | <td>23</td>                                      |
|                  | <td>43</td>                                      |
|                  | <td>23</td>                                      |
|                  | <td>43</td>                                      |
|                  | <td>23</td>                                      |
|                  | <td>43</td>                                      |
|                  | </tr>                                            |
|                  | <tr class="odd">                                 |
|                  | <td>n258</td>                                    |
|                  | <td>35</td>                                      |
|                  | <td>55</td>                                      |
|                  | <td>23</td>                                      |
|                  | <td>43</td>                                      |
|                  | <td>23</td>                                      |
|                  | <td>43</td>                                      |
|                  | <td>23</td>                                      |
|                  | <td>43</td>                                      |
|                  | </tr>                                            |
|                  | <tr class="even">                                |
|                  | <td>n260</td>                                    |
|                  | <td>35</td>                                      |
|                  | <td>55</td>                                      |
|                  | <td></td>                                        |
|                  | <td></td>                                        |
|                  | <td>23</td>                                      |
|                  | <td>43</td>                                      |
|                  | <td>23</td>                                      |
|                  | <td>43</td>                                      |
|                  | </tr>                                            |
|                  | <tr class="odd">                                 |
|                  | <td>n261</td>                                    |
|                  | <td>35</td>                                      |
|                  | <td>55</td>                                      |
|                  | <td>23</td>                                      |
|                  | <td>43</td>                                      |
|                  | <td>23</td>                                      |
|                  | <td>43</td>                                      |
|                  | <td>23</td>                                      |
|                  | <td>43</td>                                      |
|                  | </tr>                                            |
|                  | </tbody>                                         |
|                  | </table>                                         |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *The maximum output power less than or equal to  |
|                  | 23 dBm is measured at antenna connector assuming |
|                  | a 0 dBi antenna gain with omni-direction for     |
|                  | horizontal plain.*                               |
|                  |                                                  |
|                  | -   *For eMTC UE, UE power class with the        |
|                  |     maximum output power of 20dBm and 14dBm is   |
|                  |     defined in addition to UE power class with   |
|                  |     23dBm maximum output power*                  |
|                  |                                                  |
|                  | *For NB-IoT UE, UE power classes with the        |
|                  | maximum output power of 20dBm and 14dBm are      |
|                  | additionally defined in addition to UE power     |
|                  | class with 23dBm maximum output power.*          |
+------------------+--------------------------------------------------+
| 5.2.3.2.11.1.2   | What is the maximum peak power transmitted while |
|                  | in active or busy state?                         |
|                  |                                                  |
|                  | *See item 5.2.3.2.11.1.1.*                       |
+------------------+--------------------------------------------------+
| 5.2.3.2.11.1.3   | What is the time averaged power transmitted      |
|                  | while in active or busy state? Provide a         |
|                  | detailed explanation used to calculate this time |
|                  | average power.                                   |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *The time averaged power transmitted in active   |
|                  | state is subject to the type of signal/channel,  |
|                  | UE channel condition, allocated bandwidth, and   |
|                  | deployment scenario, etc. One example of         |
|                  | estimate averaged transmit power is to take      |
|                  | median of minimum UE output power and maximum UE |
|                  | output power (e.g. around -10dBm). It is noted   |
|                  | that NR minimum UE output power is defined in    |
|                  | TS38.101, as the power in the channel bandwidth  |
|                  | for all transmit bandwidth configurations        |
|                  | (resource blocks).*                              |
|                  |                                                  |
|                  | \<Minimum UE output power for frequency range    |
|                  | 1\>                                              |
|                  |                                                  |
|                  | +--------------+--------------+--------------+   |
|                  | | Channel      | Minimum      | Measurement  |   |
|                  | | bandwidth    | output power | bandwidth    |   |
|                  | |              |              |              |   |
|                  | | (MHz)        | (dBm)        | (MHz)        |   |
|                  | +==============+==============+==============+   |
|                  | | 5            | -40          | 4.515        |   |
|                  | +--------------+--------------+--------------+   |
|                  | | 10           | -40          | 9.375        |   |
|                  | +--------------+--------------+--------------+   |
|                  | | 15           | -40          | 14.235       |   |
|                  | +--------------+--------------+--------------+   |
|                  | | 20           | -40          | 19.095       |   |
|                  | +--------------+--------------+--------------+   |
|                  | | 25           | -39          | 23.955       |   |
|                  | +--------------+--------------+--------------+   |
|                  | | 30           | -38.2        | 28.815       |   |
|                  | +--------------+--------------+--------------+   |
|                  | | 40           | -37          | 38.895       |   |
|                  | +--------------+--------------+--------------+   |
|                  | | 50           | -36          | 48.615       |   |
|                  | +--------------+--------------+--------------+   |
|                  | | 60           | -35.2        | 58.35        |   |
|                  | +--------------+--------------+--------------+   |
|                  | | 80           | -34          | 78.15        |   |
|                  | +--------------+--------------+--------------+   |
|                  | | 90           | -33.5        | 88.23        |   |
|                  | +--------------+--------------+--------------+   |
|                  | | 100          | -33          | 98.31        |   |
|                  | +--------------+--------------+--------------+   |
|                  |                                                  |
|                  | \<Minimum UE output power for frequency range    |
|                  | 2\>                                              |
|                  |                                                  |
|                  | +----------+----------+----------+----------+    |
|                  | | UE power | Channel  | Minimum  | Mea      |    |
|                  | | class    | b        | output   | surement |    |
|                  | |          | andwidth | power    | b        |    |
|                  | |          |          |          | andwidth |    |
|                  | |          | (MHz)    | (dBm)    |          |    |
|                  | |          |          |          | (MHz)    |    |
|                  | +==========+==========+==========+==========+    |
|                  | | Power    | 50       | 4        | 47.52    |    |
|                  | | class 1  |          |          |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | |          | 100      | 4        | 95.04    |    |
|                  | +----------+----------+----------+----------+    |
|                  | |          | 200      | 4        | 190.08   |    |
|                  | +----------+----------+----------+----------+    |
|                  | |          | 400      | 4        | 380.16   |    |
|                  | +----------+----------+----------+----------+    |
|                  | | Power    | 50       | -13      | 47.52    |    |
|                  | | class 2, |          |          |          |    |
|                  | | 3, 4     |          |          |          |    |
|                  | +----------+----------+----------+----------+    |
|                  | |          | 100      | -13      | 95.04    |    |
|                  | +----------+----------+----------+----------+    |
|                  | |          | 200      | -13      | 190.08   |    |
|                  | +----------+----------+----------+----------+    |
|                  | |          | 400      | -13      | 380.16   |    |
|                  | +----------+----------+----------+----------+    |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *In TR36.942, the UE transmit power with         |
|                  | different power control parameters was shown in  |
|                  | RAN4 feasibility study. One example of estimate  |
|                  | averaged transmit power is to take median of the |
|                  | results which is around -10\~-5dBm.*             |
|                  |                                                  |
|                  | !                                                |
|                  | [](media/image3.emf){width="4.782133639545057in" |
|                  | height="2.874504593175853in"}                    |
|                  |                                                  |
|                  | ![                                               |
|                  | ](media/image4.emf){width="3.6707436570428698in" |
|                  | height="2.7478258967629046in"}                   |
+------------------+--------------------------------------------------+
| 5.2.3.2.11.2     | *Base station emitted power*                     |
+------------------+--------------------------------------------------+
| 5.2.3.2.11.2.1   | What is the base station transmit power per RF   |
|                  | carrier?                                         |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *For the BS type 1-C and BS type 1-H, the BS     |
|                  | conducted output power is measured at antenna    |
|                  | connector for BS type 1-C, or at TAB connector   |
|                  | for BS type 1-H.*                                |
|                  |                                                  |
|                  | *For the BS type 1-O and BS type 2-O, radiated   |
|                  | transmit power is defined as the EIRP level for  |
|                  | a declared beam at a specific beam peak          |
|                  | direction*                                       |
|                  |                                                  |
|                  | -   *For a declared beam and beam direction      |
|                  |     pair, the rated beam EIRP level is the       |
|                  |     maximum power that the base station is       |
|                  |     declared to radiate at the associated beam   |
|                  |     peak direction during the transmitter ON     |
|                  |     period.*                                     |
|                  |                                                  |
|                  | *Base Stations intended for general-purpose      |
|                  | applications do not have limits on the maximum   |
|                  | transmit power. However, there may exist         |
|                  | regional regulatory requirements which limit the |
|                  | maximum transmit power.*                         |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *The base station transmit power of one          |
|                  | component carrier is the mean power delivered to |
|                  | a load with resistance equal to the nominal load |
|                  | impedance of the transmitter.*                   |
|                  |                                                  |
|                  | *The base station maximum transmit power of one  |
|                  | component carrier is the mean power level        |
|                  | measured at the base station antenna connector   |
|                  | in a specified reference condition.*             |
|                  |                                                  |
|                  | *The transmit power of multiple component        |
|                  | carriers can be aggregated.*                     |
|                  |                                                  |
|                  | *Base Stations intended for general-purpose      |
|                  | applications do not have limits on the maximum   |
|                  | transmit power. However, there may exist         |
|                  | regional regulatory requirements which limit the |
|                  | maximum transmit power.*                         |
+------------------+--------------------------------------------------+
| 5.2.3.2.11.2.2   | What is the maximum peak transmitted power per   |
|                  | RF carrier radiated from antenna?                |
|                  |                                                  |
|                  | *Base Stations intended for general-purpose      |
|                  | applications do not have limits on the maximum   |
|                  | transmit power. However, there may exist         |
|                  | regional regulatory requirements which limit the |
|                  | maximum transmit power.*                         |
+------------------+--------------------------------------------------+
| 5.2.3.2.11.2.3   | What is the average transmitted power per RF     |
|                  | carrier radiated from antenna?                   |
|                  |                                                  |
|                  | *The averaged transmitted carrier power is       |
|                  | subject to the type of signal/channel to be      |
|                  | transmitted, bandwidth, and deployment scenario, |
|                  | etc.*                                            |
+------------------+--------------------------------------------------+
| **5.2.3.2.12**   | **Scheduler, QoS support and management, data    |
|                  | services**                                       |
+------------------+--------------------------------------------------+
| 5.2.3.2.12.1     | QoS support                                      |
|                  |                                                  |
|                  | -- What QoS classes are supported?               |
|                  |                                                  |
|                  | -- How QoS classes associated with each service  |
|                  | flow can be negotiated.                          |
|                  |                                                  |
|                  | -- QoS attributes, for example:                  |
|                  |                                                  |
|                  | • data rate (ranging from the lowest supported   |
|                  | data rate to maximum data rate supported by the  |
|                  | MAC/PHY);                                        |
|                  |                                                  |
|                  | • control plane and user plane latency (delivery |
|                  | delay);                                          |
|                  |                                                  |
|                  | • packet error ratio (after all corrections      |
|                  | provided by the MAC/PHY layers), and delay       |
|                  | variation (jitter).                              |
|                  |                                                  |
|                  | -- Is QoS supported when handing off between     |
|                  | radio access networks? If so, describe the       |
|                  | corresponding procedures.                        |
|                  |                                                  |
|                  | -- How users may utilize several applications    |
|                  | with differing QoS requirements at the same      |
|                  | time.                                            |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *In NR, QoS model is based on QoS Flows, and     |
|                  | both GBR QoS Flows and non-GBR QoS Flows are     |
|                  | supported*. *At NAS level, the QoS flow is the   |
|                  | finest granularity of QoS differentiation in a   |
|                  | PDU session. Each QoS Flow is associated with a  |
|                  | QoS profile which contains QoS parameters        |
|                  | including a 5G QoS Identifier (5QI), an          |
|                  | Allocation/ Retention Priority (ARP), Reflective |
|                  | QoS Attribute (RQA) for non-GBR Flows,           |
|                  | Guaranteed Flow Bit Rate (GFBR) and Maximum Flow |
|                  | Bit Rate (MFBR) for GBR QoS Flows, and           |
|                  | optionally with Notification Control and Maximum |
|                  | Packet Loss Rate for GBR QoS Flows. The 5QI is   |
|                  | an index representing the resource type,         |
|                  | priority, packet delay budget, packet error      |
|                  | rate, maximum data burst volume, and averaging   |
|                  | window of a QoS Flow, and up to 256 5QIs could   |
|                  | be defined by the operator (22 of which is       |
|                  | standardised). For each UE, one or multiple PDU  |
|                  | sessions can be established, and within one PDU  |
|                  | session, up to 64 QoS Flows can be allocated. At |
|                  | AS level, for each UE, one or multiple data      |
|                  | bearers can be established, and QoS Flow to data |
|                  | bearer mapping is controlled by NG-RAN. Up to 29 |
|                  | data bearers can be established in parallel for  |
|                  | a UE. One or more QoS flows can be mapped to a   |
|                  | data bearer. Reflective mapping (UE applies the  |
|                  | DL mapping rule to UL packets) is supported in   |
|                  | both NAS level and AS level. QoS profile is      |
|                  | provided by 5GC to NG-RAN and is used by NG-RAN  |
|                  | to determine the treatment on the radio          |
|                  | interface. The ARP as well as other QoS          |
|                  | parameters could be used to determine which      |
|                  | bearers to prioritise at handover. By using      |
|                  | multiple QoS Flows / data bearers having         |
|                  | different QoS profiles, multiple application     |
|                  | flows with different QoS requirements could be   |
|                  | accommodated.*                                   |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *In LTE, a bearer is the level of granularity    |
|                  | for QoS control. Up to 15 data bearers can be    |
|                  | established in parallel for a UE. Each bearer is |
|                  | associated with a QoS class index (QCI), and an  |
|                  | Allocation/ Retention Priority (ARP), and        |
|                  | optionally with guaranteed bitrate (GBR) and     |
|                  | maximum bit rate (MBR). The QCI is an index      |
|                  | representing the priority, allowable delay, and  |
|                  | packet error rate of a bearer, and up to 256     |
|                  | QCIs could be defined by the operator (21 of     |
|                  | which is standardised). The QCI, MBR, GBR and    |
|                  | ARP are signalled from the CN to the RAN when    |
|                  | the bearer is established or modified, so that   |
|                  | the scheduler in the RAN could ensure the QoS    |
|                  | for each bearer. The ARP as well as other QoS    |
|                  | parameters could be used to determine which      |
|                  | bearers to prioritise at handover. By using      |
|                  | multiple bearers having different QoS profiles,  |
|                  | multiple application flows with different QoS    |
|                  | requirements could be accommodated.*             |
+------------------+--------------------------------------------------+
| 5.2.3.2.12.2     | *Scheduling mechanisms*                          |
|                  |                                                  |
|                  | -- Exemplify scheduling algorithm(s) that may be |
|                  | used for full buffer and non-full buffer traffic |
|                  | in the technology proposal for evaluation        |
|                  | purposes.                                        |
|                  |                                                  |
|                  | Describe any measurements and/or reporting       |
|                  | required for scheduling.                         |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *In NR physical control and shared channels can  |
|                  | be separately and dynamically scheduled for both |
|                  | uplink and downlink. A scheduling unit for       |
|                  | downlink shared channel may span from 2-14       |
|                  | symbols and for uplink shared channel from 1-14  |
|                  | symbols (14 symbols comprise a "slot").          |
|                  | Sub-carrier spacing for different physical       |
|                  | channels may be dynamically changed by switching |
|                  | bandwidth-parts (BWP).*                          |
|                  |                                                  |
|                  | *Typically, NR scheduling is based on the        |
|                  | instantaneous radio-link quality as seen by the  |
|                  | different users, and the traffic demand and      |
|                  | quality-of-service requirements of individual    |
|                  | users and in the cell as a whole. The former is  |
|                  | based on CQI reports from the terminals          |
|                  | (downlink) or measurements of sounding signals   |
|                  | from the terminals (uplink). Based on this the   |
|                  | base station may e.g. apply a proportional fair  |
|                  | scheduling algorithm. The QoS assessment is      |
|                  | supported by means of receiving QoS information  |
|                  | from the "higher layers".*                       |
|                  |                                                  |
|                  | *For non-full buffer traffic like VOIP (or any   |
|                  | traffic having similar characteristics)          |
|                  | semi-persistent scheduling in DL can be applied, |
|                  | by which a user can be allocated time-frequency  |
|                  | resources in a semi-persistent manner, i.e.,     |
|                  | fixed resources are allocated at certain         |
|                  | intervals without L1/L2 control signaling each   |
|                  | time. This is especially useful to reduce the    |
|                  | L1/L2 control signaling overhead and to increase |
|                  | VoIP capacity. In addition, with UL Configured   |
|                  | Grants, the scheduler can allocate uplink        |
|                  | resources to users. When a configured uplink     |
|                  | grant is active, if the user cannot find an      |
|                  | uplink grant assigned via downlink control       |
|                  | channel an uplink transmission according to the  |
|                  | configured uplink grant can be made. Otherwise,  |
|                  | if the user finds an uplink grant assigned via   |
|                  | downlink control channel, this assignment        |
|                  | overrides the configured uplink grant.*          |
|                  |                                                  |
|                  | *In general for TDD operation a slot may be used |
|                  | for dynamically allocating DL or UL              |
|                  | transmissions or both.*                          |
|                  |                                                  |
|                  | *NR supports slot aggregation in downlink and    |
|                  | uplink, by which time-frequency resources can be |
|                  | allocated consecutively to a user for a longer   |
|                  | period than a slot by a single L1/L2 control     |
|                  | signaling. A larger transport block size or a    |
|                  | lower coding rate can be supported by this       |
|                  | technique. This is especially useful when the    |
|                  | coverage needs to be extended.*                  |
|                  |                                                  |
|                  | *As another option to extend coverage or improve |
|                  | reliability in addition to slot aggregation, a   |
|                  | set of MCS tables supporting very low code rate  |
|                  | for both DL and UL can be used.*                 |
|                  |                                                  |
|                  | *The scheduler may pre-empt an ongoing           |
|                  | transmission to one user with a latency-critical |
|                  | transmission to another user. The scheduler can  |
|                  | configure users to monitor interrupted           |
|                  | transmission indications. If a user receives the |
|                  | interrupted transmission indication, the user    |
|                  | may assume that no useful information to that    |
|                  | user was carried by the resource elements        |
|                  | included in the indication, even if some of      |
|                  | those resource elements were already scheduled   |
|                  | to this user. Alternatively, instead of          |
|                  | transmitting interruption indication, the        |
|                  | scheduler may retransmit only the preempted code |
|                  | blocks to a UE and instruct to do proper         |
|                  | transport block decoding with other already      |
|                  | received code blocks.*                           |
|                  |                                                  |
|                  | *For the downlink and the uplink,                |
|                  | intercell-interference coordination can be       |
|                  | realized by the scheduler that is transparent to |
|                  | the physical layer.*                             |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *In LTE dynamic scheduling on a 1 ms (subframe)  |
|                  | basis is applied to both uplink and downlink if  |
|                  | short TTI is not configured. Typically, LTE      |
|                  | scheduling is based on the instantaneous         |
|                  | radio-link quality as seen by the different      |
|                  | users, and the traffic demand and                |
|                  | quality-of-service requirements of individual    |
|                  | users and in the cell as a whole. The former is  |
|                  | based on CQI reports from the terminals          |
|                  | (downlink) or measurements of sounding signals   |
|                  | from the terminals (uplink). Based on this the   |
|                  | base station may e.g. apply a proportional fair  |
|                  | scheduling algorithm. The QoS assessment is      |
|                  | supported by means of receiving QoS information  |
|                  | from the "higher layers".*                       |
|                  |                                                  |
|                  | *If short TTI is configured, a scheduler may     |
|                  | allocate DL and UL shared channel transmission   |
|                  | durations of either slots (7 OFDM/SC-FDMA        |
|                  | symbols) or subslots (2 OFDM/SC-FDMA symbols).*  |
|                  | *The DL and UL transmission duration does not    |
|                  | have to be the same.*                            |
|                  |                                                  |
|                  | *For VoIP traffic (or any traffic having similar |
|                  | characteristics) semi-persistent scheduling can  |
|                  | be applied, by which a user can be allocated     |
|                  | time-frequency resources in a semi-persistent    |
|                  | manner, i.e., fixed resources are allocated at   |
|                  | certain intervals without L1/L2 control          |
|                  | signaling each time. This is especially useful   |
|                  | to reduce the L1/L2 control signaling overhead   |
|                  | and to increase VoIP capacity.*                  |
|                  |                                                  |
|                  | *Moreover, LTE supports TTI bundling, by which   |
|                  | time-frequency resources can be allocated        |
|                  | consecutively to a user for a longer period than |
|                  | 1 ms by a single L1/L2 control signaling. A      |
|                  | larger transport block size or a lower coding    |
|                  | rate can be supported by this technique. This is |
|                  | especially useful when the coverage needs to be  |
|                  | extended.*                                       |
|                  |                                                  |
|                  | *For TDD operation in general a subframe is      |
|                  | semi-statically configured for DL or UL          |
|                  | transmission. However, dynamic reconfiguration   |
|                  | of certain subframes is also possible to adapt   |
|                  | to traffic and interference conditions.*         |
|                  |                                                  |
|                  | *Intercell-interference coordination mechanisms  |
|                  | may also be realized by the scheduler. To aid    |
|                  | inter-cell coordination, LTE defines two         |
|                  | indicators exchanged between base stations: The  |
|                  | High-interference Indicator (HI) provides        |
|                  | information to neighboring cells about the part  |
|                  | of the cell bandwidth upon which the cell        |
|                  | intends to schedule its cell-edge users. The     |
|                  | Overload Indicator (OI) provides information on  |
|                  | the uplink interference level experienced in     |
|                  | each part of the cell bandwidth.*                |
|                  |                                                  |
|                  | *For the downlink, intercell-interference        |
|                  | coordination can be realized using a Relative    |
|                  | Narrowband TX Power (RNTP) indicator.*           |
|                  |                                                  |
|                  | *For NB-IoT the scheduler controls the           |
|                  | transmission duration of control channels in     |
|                  | number of subframes in a semi-static fashion     |
|                  | while the transmission duration of shared        |
|                  | channels can be varied dynamically. This is      |
|                  | beneficial for extending coverage.*              |
|                  |                                                  |
|                  | *For a user capable of V2X communication, two    |
|                  | sidelink resource allocation modes are defined:  |
|                  | eNB-controlled and UE-Autonomous resource        |
|                  | allocation modes. In eNB controlled mode, all    |
|                  | sidelink transmissions (i.e. sidelink control    |
|                  | and shared channel transmissions) are scheduled  |
|                  | by the base station. In UE-Autonomous resource   |
|                  | allocation mode, UE autonomously selects         |
|                  | resources for sidelink transmission within       |
|                  | preconfigured sidelink resource pools based on   |
|                  | predefined sensing and resource selection        |
|                  | procedures. In both modes, either dynamic or     |
|                  | semi-persistent resource allocations can be      |
|                  | used.*                                           |
|                  |                                                  |
|                  | *For a user capable of V2X communication         |
|                  | multiple semi-persistent configurations can be   |
|                  | configured in uplink and sidelink, regardless of |
|                  | the specific services the UE is operating. This, |
|                  | along with sidelink resource selection           |
|                  | procedures conditioned on sensing sidelink       |
|                  | transmissions from other users reduces           |
|                  | probability of collisions and improve system     |
|                  | performance.*                                    |
|                  |                                                  |
|                  | *See \[36.423\] for details.*                    |
+------------------+--------------------------------------------------+
| **5.2.3.2.13**   | **Radio interface architecture and protocol      |
|                  | stack**                                          |
+------------------+--------------------------------------------------+
| 5.2.3.2.13.1     | Describe details of the radio interface          |
|                  | architecture and protocol stack such as:         |
|                  |                                                  |
|                  | -- Logical channels                              |
|                  |                                                  |
|                  | -- Control channels                              |
|                  |                                                  |
|                  | -- Traffic channels                              |
|                  |                                                  |
|                  | Transport channels and/or physical channels.     |
|                  |                                                  |
|                  | ***[SRIT RAN/Radio                               |
|                  | Architectures:]{.underline}***                   |
|                  |                                                  |
|                  | *This SRIT contains NR and LTE "standalone"      |
|                  | architectures. Besides NR and LTE "standalone"   |
|                  | architectures and operation, certain NR-LTE      |
|                  | interworking options are defined, using          |
|                  | "multi-RAT dual connectivity" (MR-DC) operation, |
|                  | e.g. (ref. to \[37.340\]):*                      |
|                  |                                                  |
|                  | -   ***E-UTRA-NR Dual Connectivity (EN-DC),** in |
|                  |     which a UE is connected to one eNB (MN) and  |
|                  |     one en-gNB (SN). The eNB is connected to the |
|                  |     EPC and the en-gNB is connected to the eNB   |
|                  |     via the X2 interface.*                       |
|                  |                                                  |
|                  | -   ***NG-RAN E-UTRA-NR Dual Connectivity        |
|                  |     (NGEN-DC),** similar architecture to EN-DC,  |
|                  |     but the eNB is connected to 5GC.*            |
|                  |                                                  |
|                  | -   ***NR-E-UTRA Dual Connectivity (NE-DC),** in |
|                  |     which a UE is connected to one gNB (MN) and  |
|                  |     one ng-eNB (SN). The gNB is connected to 5GC |
|                  |     and the ng-eNB is connected to the gNB via   |
|                  |     the Xn interface.*                           |
|                  |                                                  |
|                  | ***[High-level summary of radio interface        |
|                  | protocols:]{.underline}***                       |
|                  |                                                  |
|                  | *The following paragraphs provide a high level   |
|                  | summary of radio interface protocols and         |
|                  | channels, with focus on NR standalone and        |
|                  | LTE/E-UTRA standalone (covering also some        |
|                  | specific aspects of eMTC/NB-IOT, as well as      |
|                  | EN-DC).*                                         |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *[Radio Protocols]{.underline}:*                 |
|                  |                                                  |
|                  | *The protocol stack for the user plane includes  |
|                  | the following: SDAP, PDCP, RLC, MAC, and PHY     |
|                  | sublayers (terminated in UE and gNB).*           |
|                  |                                                  |
|                  | *On the Control plane, the following protocols   |
|                  | are defined:*                                    |
|                  |                                                  |
|                  | > \- *RRC, PDCP, RLC, MAC and PHY sublayers      |
|                  | > (terminated in UE and gNB);*                   |
|                  | >                                                |
|                  | > *- NAS protocol (terminated in UE and AMF)*    |
|                  |                                                  |
|                  | [ ]{.underline}                                  |
|                  |                                                  |
|                  | *For details on protocol services and functions, |
|                  | please refer to 3GPP specifications (e.g.        |
|                  | \[38.300\]).*                                    |
|                  |                                                  |
|                  | *[Radio Channels (Physical, Transport and        |
|                  | Logical Channels)]{.underline}*                  |
|                  |                                                  |
|                  | *The physical layer offers service to the MAC    |
|                  | sublayer transport channels. The MAC sublayer    |
|                  | offers service to the RLC sublayer logical       |
|                  | channels. The RLC sublayer offers service to the |
|                  | PDCP sublayer RLC channels. The PDCP sublayer    |
|                  | offers service to the SDAP and RRC sublayer      |
|                  | radio bearers: data radio bearers (DRB) for user |
|                  | plane data and signalling radio bearers (SRB)    |
|                  | for control plane data.*                         |
|                  |                                                  |
|                  | *The SDAP sublayer offers 5GC QoS flows and DRBs |
|                  | mapping function.*                               |
|                  |                                                  |
|                  | *The physical channels defined in the downlink   |
|                  | are:*                                            |
|                  |                                                  |
|                  | > *- the Physical Downlink Shared Channel        |
|                  | > (PDSCH),*                                      |
|                  | >                                                |
|                  | > *- the Physical Downlink Control Channel       |
|                  | > (PDCCH),*                                      |
|                  | >                                                |
|                  | > *- the Physical Broadcast Channel (PBCH),*     |
|                  |                                                  |
|                  | *The physical channels defined in the uplink     |
|                  | are:*                                            |
|                  |                                                  |
|                  | > *- the Physical Random Access Channel          |
|                  | > (PRACH),*                                      |
|                  | >                                                |
|                  | > *- the Physical Uplink Shared Channel          |
|                  | > (PUSCH),*                                      |
|                  | >                                                |
|                  | > *- and the Physical Uplink Control Channel     |
|                  | > (PUCCH).*                                      |
|                  |                                                  |
|                  | *In addition to the physical channels above, PHY |
|                  | layer signals are defined, which an be reference |
|                  | signals, primary and secondary synchronization   |
|                  | signals.*                                        |
|                  |                                                  |
|                  | *The following transport channels, and their     |
|                  | mapping to PHY channels, are defined:*           |
|                  |                                                  |
|                  | *Uplink:*                                        |
|                  |                                                  |
|                  | -   *Uplink Shared Channel (UL-SCH), mapped to   |
|                  |     PUSCH*                                       |
|                  |                                                  |
|                  | -   *Random Access Channel (RACH), mapped to     |
|                  |     PRACH*                                       |
|                  |                                                  |
|                  | *Downlink:*                                      |
|                  |                                                  |
|                  | -   *Downlink Shared Channel (DL-SCH), mapped to |
|                  |     PDSCH*                                       |
|                  |                                                  |
|                  | -   *Broadcast channel (BCH), mapped to PBCH*    |
|                  |                                                  |
|                  | -   *Paging channel (PCH), mapped to (TBD)*      |
|                  |                                                  |
|                  | *Logical channels are classified into two        |
|                  | groups: Control Channels and Traffic Channels.   |
|                  | Control channels:*                               |
|                  |                                                  |
|                  | -   *Broadcast Control Channel (BCCH): a         |
|                  |     downlink channel for broadcasting system     |
|                  |     control information.*                        |
|                  |                                                  |
|                  | -   *Paging Control Channel (PCCH): a downlink   |
|                  |     channel that transfers paging information    |
|                  |     and system information change                |
|                  |     notifications.*                              |
|                  |                                                  |
|                  | -   *Common Control Channel (CCCH): channel for  |
|                  |     transmitting control information between UEs |
|                  |     and network.*                                |
|                  |                                                  |
|                  | -   *Dedicated Control Channel (DCCH): a         |
|                  |     point-to-point bi-directional channel that   |
|                  |     transmits dedicated control information      |
|                  |     between a UE and the network.*               |
|                  |                                                  |
|                  | *Traffic channels: Dedicated Traffic Channel     |
|                  | (DTCH), which can exist in both UL and DL.*      |
|                  |                                                  |
|                  | *In Downlink, the following connections between  |
|                  | logical channels and transport channels exist:*  |
|                  |                                                  |
|                  | -   *BCCH can be mapped to BCH, or DL-SCH;*      |
|                  |                                                  |
|                  | -   *PCCH can be mapped to PCH;*                 |
|                  |                                                  |
|                  | -   *CCCH, DCCH, DTCH can be mapped to DL-SCH;*  |
|                  |                                                  |
|                  | *In Uplink, the following connections between    |
|                  | logical channels and transport channels exist:*  |
|                  |                                                  |
|                  | > *- CCCH,DCCH, DTCH can be mapped to UL-SCH.*   |
|                  |                                                  |
|                  | *[Other aspects]{.underline}*                    |
|                  |                                                  |
|                  | *- NR QoS architecture*                          |
|                  |                                                  |
|                  | *The QoS architecture in NG-RAN (connected to    |
|                  | 5GC), can be summarized as follows:*             |
|                  |                                                  |
|                  | > *For each UE, 5GC establishes one or more PDU  |
|                  | > Sessions.*                                     |
|                  |                                                  |
|                  | *For each UE, the NG-RAN establishes one or more |
|                  | Data Radio Bearers (DRB) per PDU Session. The    |
|                  | NG-RAN maps packets belonging to different PDU   |
|                  | sessions to different DRBs. Hence, the NG-RAN    |
|                  | establishes at least one default DRB for each    |
|                  | PDU Session.*                                    |
|                  |                                                  |
|                  | *NAS level packet filters in the UE and in the   |
|                  | 5GC associate UL and DL packets with QoS Flows.* |
|                  |                                                  |
|                  | *AS-level mapping rules in the UE and in the     |
|                  | NG-RAN associate UL and DL QoS Flows with DRBs*  |
|                  |                                                  |
|                  | *-* *Carrier Aggregation (CA)*                   |
|                  |                                                  |
|                  | *In case of CA, the multi-carrier nature of the  |
|                  | physical layer is only exposed to the MAC layer  |
|                  | for which one HARQ entity is required per        |
|                  | serving cell.*                                   |
|                  |                                                  |
|                  | *-                                               |
|                  |  Dual Connectivity (DC)* {#dual-connectivity-dc} |
|                  | --------------------------                       |
|                  |                                                  |
|                  | *In DC, the radio protocol architecture that a   |
|                  | radio bearer uses depends on how the radio       |
|                  | bearer is setup. Four bearer types exist: MCG    |
|                  | bearer, MCG split bearer, SCG bearer and SCG     |
|                  | split bearer. The following                      |
|                  | terminology/definitions apply:*                  |
|                  |                                                  |
|                  | -   *Master gNB: in dual connectivity, the gNB   |
|                  |     which terminates at least NG-C.*             |
|                  |                                                  |
|                  | -   *Secondary gNB: in dual connectivity, the    |
|                  |     gNB that is providing additional radio       |
|                  |     resources for the UE but is not the Master   |
|                  |     node.*                                       |
|                  |                                                  |
|                  | -   *Master Cell Group (MCG): in dual            |
|                  |     connectivity, a group of serving cells       |
|                  |     associated with the MgNB*                    |
|                  |                                                  |
|                  | -   *Secondary Cell Group (SCG): in dual         |
|                  |     connectivity, a group of serving cells       |
|                  |     associated with the SgNB*                    |
|                  |                                                  |
|                  | -   *MCG bearer: in dual connectivity, a bearer  |
|                  |     whose radio protocols are only located in    |
|                  |     the MCG.*                                    |
|                  |                                                  |
|                  | -   *MCG split bearer: in dual connectivity, a   |
|                  |     bearer whose radio protocols are split at    |
|                  |     the MgNB and belong to both MCG and SCG.*    |
|                  |                                                  |
|                  | -   *SCG bearer: in dual connectivity, a bearer  |
|                  |     whose radio protocols are only located in    |
|                  |     the SCG.*                                    |
|                  |                                                  |
|                  | -   *SCG split bearer: in dual connectivity, a   |
|                  |     bearer whose radio protocols are split at    |
|                  |     the SgNB and belong to both SCG and MCG.*    |
|                  |                                                  |
|                  | *In case of DC, the UE is configured with two    |
|                  | MAC entities: one MAC entity for the MCG and one |
|                  | MAC entity for the SCG. For a split bearer, UE   |
|                  | is configured over which link (or both) the UE   |
|                  | transmits UL PDCP PDUs. On the link which is not |
|                  | responsible for UL PDCP PDUs transmission, the   |
|                  | RLC layer only transmits corresponding ARQ       |
|                  | feedback for the downlink data.*                 |
|                  |                                                  |
|                  | *For more details on NR Radio Protocol           |
|                  | architecture and channels, refer to:*            |
|                  |                                                  |
|                  | *\[38.300\], \[38.401\], \[38.201\], \[37.340\]* |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *NOTE: eMTC/NB-IoT uses optimized physical layer |
|                  | and radio procedures (e.g. for very low power    |
|                  | consumption), thus a number of E-UTRA protocol   |
|                  | mechanisms and functions are either not used, or |
|                  | are specific to eMTC/NB-IOT only.\               |
|                  | Some examples of functionalities not specified   |
|                  | for NB-IOT are: inter-RAT mobility, handover,    |
|                  | measurement reports, carrier aggregation, dual   |
|                  | connectivity.\                                   |
|                  | Only few exceptions/variations are highlighted   |
|                  | below; for details please refer to stage-3       |
|                  | specifications.*                                 |
|                  |                                                  |
|                  | *[Radio Protocol stack]{.underline}*             |
|                  |                                                  |
|                  | *The protocol stack for the user plane includes  |
|                  | PDCP, RLC, MAC, and PHY sublayers (terminated in |
|                  | UE and eNB).\                                    |
|                  | For NB-IoT, the user plane is not used when      |
|                  | transferring user data over NAS.*                |
|                  |                                                  |
|                  | *On the Control plane, the following protocols   |
|                  | are defined:*                                    |
|                  |                                                  |
|                  | > \- *RRC, PDCP, RLC, MAC and PHY sublayers      |
|                  | > (terminated in UE and eNB);*                   |
|                  | >                                                |
|                  | > *- NAS protocol (terminated in UE and Core     |
|                  | > Network)*                                      |
|                  |                                                  |
|                  | *For NB-IoT, if certain optimizations are        |
|                  | supported, PDCP can be bypassed (at all, or      |
|                  | until AS security is activated)*                 |
|                  |                                                  |
|                  | *For details on protocol services and functions, |
|                  | please refer to 3GPP specifications (e.g. TS     |
|                  | 36.300).*                                        |
|                  |                                                  |
|                  | *[Radio Channels (Physical, Transport and        |
|                  | Logical Channels)]{.underline}*                  |
|                  |                                                  |
|                  | *The main E-UTRA physical channels, and mapped   |
|                  | transport channels, are:*                        |
|                  |                                                  |
|                  | *DL:*                                            |
|                  |                                                  |
|                  | -   *Physical broadcast channel (PBCH)*          |
|                  |                                                  |
|                  |     -   *Carries the BCH transport channel*      |
|                  |                                                  |
|                  | -   *Physical downlink shared channel (PDSCH)*   |
|                  |                                                  |
|                  |     -   *Carries the DL-SCH and PCH transport    |
|                  |         channels*                                |
|                  |                                                  |
|                  | -   *Physical control format indicator channel   |
|                  |     (PCFICH)*                                    |
|                  |                                                  |
|                  | -   *Physical downlink control channel (PDCCH)*  |
|                  |                                                  |
|                  | -   *Enhanced physical downlink control channel  |
|                  |     (EPDCCH)*                                    |
|                  |                                                  |
|                  | -   *Physical Hybrid ARQ Indicator Channel       |
|                  |     (PHICH)*                                     |
|                  |                                                  |
|                  | *UL:*                                            |
|                  |                                                  |
|                  | -   *Physical uplink control channel (PUCCH)*    |
|                  |                                                  |
|                  | -   *Physical uplink shared channel (PUSCH)*     |
|                  |                                                  |
|                  |     -   *Carries the UL-SCH transport channel*   |
|                  |                                                  |
|                  | -   *Physical random access channel (PRACH)*     |
|                  |                                                  |
|                  |     -   *Carries the RACH transport channel*     |
|                  |                                                  |
|                  | *eMTC specific physical channels:*               |
|                  |                                                  |
|                  | -   *MTC physical downlink control channel       |
|                  |     (MPDCCH)*                                    |
|                  |                                                  |
|                  | -   *Resynchronization Signal (RSS)*             |
|                  |                                                  |
|                  | *NB-IOT specific physical channels:*             |
|                  |                                                  |
|                  | -   *Narrowband Physical broadcast channel       |
|                  |     (NPBCH)*                                     |
|                  |                                                  |
|                  | -   *Narrowband Physical downlink shared channel |
|                  |     (NPDSCH)*                                    |
|                  |                                                  |
|                  | -   *Narrowband Physical downlink control        |
|                  |     channel (NPDCCH)*                            |
|                  |                                                  |
|                  | -   *Narrowband Physical uplink shared channel   |
|                  |     Format 1 (NPUSCH F1)*                        |
|                  |                                                  |
|                  | -   *Narrowband Physical uplink shared channel   |
|                  |     Format 2 (NPUSCH F2)*                        |
|                  |                                                  |
|                  | -                                                |
|                  |                                                  |
|                  | -   *Narrowband Physical random access channel   |
|                  |     (NPRACH)*                                    |
|                  |                                                  |
|                  | *In addition to the above channels, two types of |
|                  | physical signals are defined: reference or       |
|                  | synchronization signals.*                        |
|                  |                                                  |
|                  | *E-UTRA Logical channels (at MAC/RLC sublayer)   |
|                  | are:*                                            |
|                  |                                                  |
|                  | *- Control Channels (for the transfer of control |
|                  | plane information), e.g.:*                       |
|                  |                                                  |
|                  | *- Broadcast Control Channel (BCCH)*             |
|                  |                                                  |
|                  | > *- For eMTC, Bandwidth Reduced Broadcast       |
|                  | > Control Channel (BR-BCCH)*                     |
|                  |                                                  |
|                  | *- Paging Control Channel (PCCH)*                |
|                  |                                                  |
|                  | *- Common Control Channel (CCCH)*                |
|                  |                                                  |
|                  | *- Dedicated Control Channel (DCCH)*             |
|                  |                                                  |
|                  | *- Traffic Channels (for the transfer of user    |
|                  | plane information), e.g..*                       |
|                  |                                                  |
|                  | *- Dedicated Traffic Channel (DTCH)*             |
|                  |                                                  |
|                  | *The following mapping between logical channels  |
|                  | and transport channels is defined:*              |
|                  |                                                  |
|                  | *In Uplink, CCCH, DCCH and DTCH can be mapped to |
|                  | UL-SCH;\                                         |
|                  | In Downlink,*                                    |
|                  |                                                  |
|                  | > *- BCCH can be mapped to BCH, or DL-SCH;*      |
|                  | >                                                |
|                  | > *- BR-BCCH can be mapped to DL-SCH;*           |
|                  | >                                                |
|                  | > *- PCCH can be mapped to PCH;*                 |
|                  | >                                                |
|                  | > *- CCCH, DCCH and DTCH can be mapped to        |
|                  | > DL-SCH*                                        |
|                  |                                                  |
|                  | *[Other Aspects]{.underline}*                    |
|                  |                                                  |
|                  | *- Carrier Aggregation (CA)*                     |
|                  |                                                  |
|                  | *In Carrier Aggregation (CA), two or more        |
|                  | Component Carriers (CCs) are aggregated in order |
|                  | to support wider transmission bandwidths. A UE   |
|                  | may simultaneously receive or transmit on one or |
|                  | multiple CCs depending on its capabilities.*     |
|                  |                                                  |
|                  | *The multi-carrier nature of the physical layer  |
|                  | is only exposed to the MAC layer for which one   |
|                  | HARQ entity is required per serving cell.*       |
|                  |                                                  |
|                  | > *- In both uplink and downlink, there is one   |
|                  | > independent hybrid-ARQ entity per serving cell |
|                  | > and one transport block is generated per TTI   |
|                  | > per serving cell (in the absence of spatial    |
|                  | > multiplexing). Each transport block and its    |
|                  | > potential HARQ retransmissions are mapped to a |
|                  | > single serving cell;*                          |
|                  |                                                  |
|                  | *- Dual Connectivity (DC)*                       |
|                  |                                                  |
|                  | *In DC, the configured set of serving cells for  |
|                  | a UE consists of two subsets: the Master Cell    |
|                  | Group (MCG) containing the serving cells of the  |
|                  | MeNB, and the Secondary Cell Group (SCG)         |
|                  | containing the serving cells of the SeNB*\       |
|                  | *The DC UE is configured with two MAC entities:  |
|                  | one MAC entity for MeNB and one MAC entity for   |
|                  | SeNB.*                                           |
|                  |                                                  |
|                  | *- E-UTRA-NR Dual Connectivity (EN-DC)*          |
|                  |                                                  |
|                  | *E-UTRAN supports also Multi-RAT Dual            |
|                  | Connectivity (MR-DC) with NR, e.g. one MR-DC     |
|                  | architecture is E-UTRA-NR Dual Connectivity      |
|                  | (EN-DC), in which a UE is connected to one eNB   |
|                  | that acts as a MN and one en-gNB that acts as a  |
|                  | SN. The eNB is connected to the EPC and the      |
|                  | en-gNB is connected to the eNB via the X2        |
|                  | interface.*                                      |
|                  |                                                  |
|                  | *- NB-IOT\                                       |
|                  | For NB-IoT, CA and DC are not supported; only a  |
|                  | specific multi-carrier operation is defined      |
|                  | (e.g. a RRC\_CONNECTED UE can be configured to a |
|                  | non-anchor carrier, for all unicast              |
|                  | transmissions).*                                 |
|                  |                                                  |
|                  | *For more details on LTE Radio Protocol          |
|                  | architecture and channels, refer to:*            |
|                  |                                                  |
|                  | *\[36.300\], \[36.401\], \[36.201\], \[37.340\]* |
+------------------+--------------------------------------------------+
| 5.2.3.2.13.2     | What is the bit rate required for transmitting   |
|                  | feedback information?                            |
|                  |                                                  |
|                  | *[**For NR and LTE component                     |
|                  | RIT:**]{.underline}*                             |
|                  |                                                  |
|                  | *As described in other sections (e.g. 5.2.3.2.3, |
|                  | 5.2.3.2.10, 5.2.3.2.13.1), from a Layer1 point   |
|                  | of view (PHY/MAC), few control (feedback/HARQ)   |
|                  | channels are defined (in UL and DL), with        |
|                  | specific characteristics and transmission        |
|                  | schemes/rates.*                                  |
|                  |                                                  |
|                  | *At Layer2 level (i.e. RLC ARQ), assuming an RLC |
|                  | AM Status report is sent every 50 ms             |
|                  | (configurable), with a size of few octets, e.g.  |
|                  | 32 bits (including RLC/MAC header overhead),     |
|                  | this results in a rate of 32/0.05= 640 bit/s.*   |
+------------------+--------------------------------------------------+
| 5.2.3.2.13.3     | *Channel access:*                                |
|                  |                                                  |
|                  | Describe in details how RIT/SRIT accomplishes    |
|                  | initial channel access, (e.g. contention or      |
|                  | non-contention based).                           |
|                  |                                                  |
|                  | *[**For NR and LTE component RIT (**Common       |
|                  | principles)]{.underline}*                        |
|                  |                                                  |
|                  | *Initial channel access is typically             |
|                  | accomplished via the "random access procedure"   |
|                  | (assuming no dedicated/scheduled resources are   |
|                  | allocated).*                                     |
|                  |                                                  |
|                  | *The random access procedure can be contention   |
|                  | based (e.g. at initial connection from idle      |
|                  | mode) or non-contention based (e.g. during       |
|                  | Handover to a new cell). Random access resources |
|                  | and parameters are configured by the network and |
|                  | signalled to the UE (via broadcast or dedicated  |
|                  | signaling).*                                     |
|                  |                                                  |
|                  | *Contention based random access procedure        |
|                  | encompasses the transmission of a random access  |
|                  | preamble by the UE (subject to possible          |
|                  | contention with other UEs), followed by a random |
|                  | access response (RAR) in DL (including           |
|                  | allocating specific radio resources for the      |
|                  | uplink transmission). Afterwards, the UE         |
|                  | transmits the initial UL message (e.g. RRC       |
|                  | connection Request) using the allocated          |
|                  | resources, and wait for a contention resolution  |
|                  | message in DL (to confirming access to that UE). |
|                  | The UE could perform multiple attempts until it  |
|                  | is successful in accessing the channel or until  |
|                  | a timer (supervising the procedure) elapses.*    |
|                  |                                                  |
|                  | *Non-contention based random access procedure    |
|                  | foresees the assignment of a dedicated random    |
|                  | access resource/preamble to a UE (e.g. part of   |
|                  | an HO command). This avoids the contention       |
|                  | resolution phase, i.e. only the random access    |
|                  | preamble and random access response messages are |
|                  | needed to get channel access.*                   |
|                  |                                                  |
|                  | *From a L1 perspective, a random access preamble |
|                  | is transmitted (UL) in a PRACH, random access    |
|                  | response (DL) in a PDSCH, UL transmission in a   |
|                  | PUSCH, and contention resolution message (DL) in |
|                  | a PDSCH.*                                        |
|                  |                                                  |
|                  | *[Other/specific RIT aspects]{.underline}*       |
|                  |                                                  |
|                  | *Detailed aspects and mechanisms of the random   |
|                  | access procedure are specific/different for each |
|                  | RIT (NR and LTE), e.g. physical                  |
|                  | resources/channels, timing, messages/parameters, |
|                  | etc.*                                            |
|                  |                                                  |
|                  | *For eMTC/NB-IOT, there are also specific        |
|                  | differences, e.g.*                               |
|                  |                                                  |
|                  | *- For eMTC: PRACH configuration/repetition,     |
|                  | decoding/interpretation of Random Access         |
|                  | Response (RAR), etc.*                            |
|                  |                                                  |
|                  | *- For NB-IOT: dedicated NPRACH channel,         |
|                  | configuration, RAR decoding, etc.*               |
|                  |                                                  |
|                  | *For more details, refer to:*                    |
|                  |                                                  |
|                  | *- NR: \[38.300\], \[38.321\] and \[38.213\]*    |
|                  |                                                  |
|                  | *- LTE: \[36.300\], \[36.321\] and \[36.213\]*   |
+------------------+--------------------------------------------------+
| **5.2.3.2.14**   | **Cell selection**                               |
+------------------+--------------------------------------------------+
| 5.2.3.2.14.1     | Describe in detail how the RIT/SRIT accomplishes |
|                  | cell selection to determine the serving cell for |
|                  | the users.                                       |
|                  |                                                  |
|                  | ***[For NR and LTE component                     |
|                  | RIT:]{.underline}***                             |
|                  |                                                  |
|                  | *Cell selection is based on the following        |
|                  | principles, [common for NR and                   |
|                  | LTE]{.underline}:*                               |
|                  |                                                  |
|                  | *- The UE NAS layer identifies a selected PLMN   |
|                  | (and equivalent PLMNs, if any);*                 |
|                  |                                                  |
|                  | *- The UE searches the supported frequency bands |
|                  | (RIT specific) and for each carrier frequency it |
|                  | searches and identifies the strongest cell. It   |
|                  | reads cell broadcast information to identify its |
|                  | PLMN(s) and other relevant parameters (e.g.      |
|                  | related to cell restrictions);*                  |
|                  |                                                  |
|                  | *- The UE seeks to identify a suitable cell; if  |
|                  | it is not able to identify a "suitable" cell it  |
|                  | seeks to identify an "acceptable" cell.*         |
|                  |                                                  |
|                  | > *- A cell is "suitable" if: the measured cell  |
|                  | > attributes satisfy the cell selection criteria |
|                  | > (based on DL radio signal strength/quality);   |
|                  | > the cell belongs to the selected/equivalent    |
|                  | > PLMN; cell is not restricted (e.g. cell is not |
|                  | > barred/reserved or part of \"forbidden\"       |
|                  | > roaming areas);*                               |
|                  | >                                                |
|                  | > *- An "acceptable" cell is one for which the   |
|                  | > measured cell attributes satisfy the cell      |
|                  | > selection criteria and the cell is not         |
|                  | > barred.*                                       |
|                  |                                                  |
|                  | *Among the identified suitable (or acceptable)   |
|                  | cells, the UE selects the strongest cell,        |
|                  | (technically it "camps" on that cell).*          |
|                  |                                                  |
|                  | *As signalled/configured by the radio network,   |
|                  | certain frequencies or RITs could be prioritized |
|                  | for camping.*                                    |
|                  |                                                  |
|                  | *[Other/specific RIT aspects]{.underline}*       |
|                  |                                                  |
|                  | *Detailed aspects and mechanisms of cell         |
|                  | selection are specific/different for each RIT    |
|                  | (NR and LTE), e.g.:*                             |
|                  |                                                  |
|                  | *- frequency/cell search (using different DL     |
|                  | sync signals and search procedures)*             |
|                  |                                                  |
|                  | *- broadcast system information                  |
|                  | acquisition/signalling*                          |
|                  |                                                  |
|                  | *- RF measurement and metrics/thresholds for     |
|                  | selection criteria*                              |
|                  |                                                  |
|                  | *Few specific mechanisms/restrictions apply to   |
|                  | eMTC/NB-IOT, e.g.:*                              |
|                  |                                                  |
|                  | *- NB-IOT and eMTC uses specific DL signals and  |
|                  | (optimized/limited) cell search and measurement  |
|                  | procedures*                                      |
|                  |                                                  |
|                  | *- Specific cell selection criteria may apply to |
|                  | eMTC*                                            |
|                  |                                                  |
|                  | *For more details, refer to:*                    |
|                  |                                                  |
|                  | *- NR: \[38.300\] sub-clause 9.2.1.1 and         |
|                  | \[38.304\] sub-clause 5.2*                       |
|                  |                                                  |
|                  | *- LTE: \[36.300\] sub-clause 10.1.1.1 and       |
|                  | \[36.304\] sub-clause 5.2*                       |
+------------------+--------------------------------------------------+
| **5.2.3.2.15**   | **Location determination mechanisms**            |
+------------------+--------------------------------------------------+
| 5.2.3.2.15.1     | Describe any location determination mechanisms   |
|                  | that may be used, e.g., to support location      |
|                  | based services.                                  |
|                  |                                                  |
|                  | [*** For NR component RIT:***]{.underline}       |
|                  |                                                  |
|                  | *NG RAN provides mechanisms to support or assist |
|                  | the determination of the geographical position   |
|                  | of a UE. UE position knowledge can be used for   |
|                  | Radio Resource Management, location based        |
|                  | services for operators, subscribers, and third   |
|                  | party service providers. User plane (U-plane)    |
|                  | based solution (SUPL) as well as control plane   |
|                  | (C-plane) based techniques are supported and     |
|                  | adapted from capabilities already supported for  |
|                  | E-UTRAN, UTRAN and GERAN, etc.*                  |
|                  |                                                  |
|                  | *The standard positioning methods supported for  |
|                  | NG-RAN access include:*                          |
|                  |                                                  |
|                  | \- *network-assisted GNSS methods;*              |
|                  |                                                  |
|                  | *- observed time difference of arrival (OTDOA)   |
|                  | positioning;*                                    |
|                  |                                                  |
|                  | *- enhanced cell ID methods;*                    |
|                  |                                                  |
|                  | *- barometric pressure sensor positioning;*      |
|                  |                                                  |
|                  | *- WLAN positioning;*                            |
|                  |                                                  |
|                  | *- Bluetooth positioning;*                       |
|                  |                                                  |
|                  | *- terrestrial beacon system (TBS) positioning.* |
|                  |                                                  |
|                  | *Use of one or more methods from the list above  |
|                  | and hybrid positioning using multiple methods is |
|                  | supported using either UE-based,                 |
|                  | UE-assisted/LMF-based, and NG-RAN node assisted  |
|                  | versions.*                                       |
|                  |                                                  |
|                  | *In future releases, the work on NG-RAN          |
|                  | RAT-dependent and RAT-independent positioning    |
|                  | solutions is expected to continue and further    |
|                  | enrich the location determination mechanisms     |
|                  | that may be used to support location based       |
|                  | services.*                                       |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *EUTRAN provides mechanisms to support or assist |
|                  | the determination of the geographical position   |
|                  | of a UE. UE position knowledge can be used for   |
|                  | Radio Resource Management, location based        |
|                  | services for operators, subscribers, and third   |
|                  | party service providers. User plane (U-plane)    |
|                  | based solution (SUPL) as well as control plane   |
|                  | (C-plane) based techniques are supported and     |
|                  | adapted from capabilities already supported for  |
|                  | UTRAN and GERAN, etc.*                           |
|                  |                                                  |
|                  | *The standard positioning methods supported by   |
|                  | E-UTRAN access include:*                         |
|                  |                                                  |
|                  | *- network-assisted GNSS methods;*               |
|                  |                                                  |
|                  | *- downlink positioning;*                        |
|                  |                                                  |
|                  | *- enhanced cell ID method;*                     |
|                  |                                                  |
|                  | *- uplink positioning;*                          |
|                  |                                                  |
|                  | *- barometric pressure sensor method;*           |
|                  |                                                  |
|                  | *- WLAN method;*                                 |
|                  |                                                  |
|                  | *- Bluetooth method;*                            |
|                  |                                                  |
|                  | *- Terrestrial Beacon System method.*            |
|                  |                                                  |
|                  | *Hybrid positioning using multiple methods from  |
|                  | the list of positioning methods above is also    |
|                  | supported.*                                      |
+------------------+--------------------------------------------------+
| **5.2.3.2.16**   | **Priority access mechanisms**                   |
+------------------+--------------------------------------------------+
| 5.2.3.2.16.1     | Describe techniques employed to support          |
|                  | prioritization of access to radio or network     |
|                  | resources for specific services or specific      |
|                  | users (e.g., to allow access by emergency        |
|                  | services).                                       |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *NR supports overload and access control         |
|                  | functionality such as RACH back off, RRC         |
|                  | Connection Reject, RRC Connection Release and UE |
|                  | based access barring mechanisms. One unified     |
|                  | access control framework as specified in 3GPP TS |
|                  | 22.261 section 6.22 is applied for NR. For each  |
|                  | access attempt one Access Category and one or    |
|                  | more Access Identities are selected.*            |
|                  |                                                  |
|                  | *NR broadcasts barring control information       |
|                  | associated with Access Categories and Access     |
|                  | Identities and the UE determines whether an      |
|                  | identified access attempt is authorized or not,  |
|                  | based on the broadcasted barring information and |
|                  | the selected Access Category and Access          |
|                  | Identities. In the case of multiple core         |
|                  | networks sharing the same RAN, the RAN provides  |
|                  | broadcasted barring control information for each |
|                  | PLMN individually.*                              |
|                  |                                                  |
|                  | *The unified access control framework is         |
|                  | applicable to all UE states (RRC\_IDLE,          |
|                  | RRC\_INACTIVE and RRC\_CONNECTED state).*        |
|                  |                                                  |
|                  | *For NAS triggered requests, the UE NAS          |
|                  | determines one access category and access        |
|                  | identity(ies) for the given access attempt and   |
|                  | provides them to RRC for access control check.   |
|                  | The RRC performs access barring check based on   |
|                  | the access control information and the           |
|                  | determined access category and access            |
|                  | identities. The RRC indicates whether the access |
|                  | attempt is allowed or not to NAS layer. The NAS  |
|                  | also performs the mapping of the access category |
|                  | and access identity(ies) associated with the     |
|                  | access attempt to establishment cause and        |
|                  | provides the establishment cause to RRC for      |
|                  | inclusion in connection request to enable the    |
|                  | gNB to decide whether to reject the request.*    |
|                  |                                                  |
|                  | *For AS triggered request (i.e. RNA update), the |
|                  | RRC determines the resume cause value and the    |
|                  | corresponding access category.*                  |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *LTE defines a range of access control           |
|                  | mechanisms described in TS 22.011 section 4 that |
|                  | can be used to restrict UEs' access attempts to  |
|                  | the system. These mechanisms are detailed in the |
|                  | bulleted list below. In addition, the LTE        |
|                  | specification defines mechanisms for the network |
|                  | to prioritize access attempts after the overall  |
|                  | access control mechanism defined for the UEs has |
|                  | passed and the UE has initiated RRC connection   |
|                  | establishment, at which point the network can    |
|                  | allocate relative priority to the request        |
|                  | relative to other requests based on the provided |
|                  | RRC Establishment cause.*                        |
|                  |                                                  |
|                  | *The specified mechanisms that can be used to    |
|                  | restrict UEs' access attempts to the system      |
|                  | defined in different 3GPP releases:*             |
|                  |                                                  |
|                  | -   *3GPP Release 8: Access Class Barring (ACB)* |
|                  |                                                  |
|                  | > *If the UE is a member of at least one Access  |
|                  | > Class which corresponds to the permitted       |
|                  | > classes broadcast in the system information,   |
|                  | > and the Access Class is applicable in the      |
|                  | > serving network, access attempts are allowed.  |
|                  | > Additionally, in the case of the access        |
|                  | > network being UTRAN the serving network can    |
|                  | > indicate that UEs are allowed to respond to    |
|                  | > paging and perform location registration even  |
|                  | > if their access class is not permitted.        |
|                  | > Otherwise access attempts are not allowed. Any |
|                  | > number of these classes may be barred at any   |
|                  | > one time, and in case of multiple core         |
|                  | > networks sharing the same access network, the  |
|                  | > access network is able to apply Access Class   |
|                  | > Barring for the different core networks        |
|                  | > individually. The network operator can take    |
|                  | > the network load into account when allowing    |
|                  | > UEs access to the network.*                    |
|                  | >                                                |
|                  | > *Access Classes are applicable as follows:*    |
|                  | >                                                |
|                  | > *Classes 0 - 9 - Home and Visited PLMNs;*      |
|                  | >                                                |
|                  | > *Class 10 - This bit's presence in the access  |
|                  | > class barring information broadcast to the     |
|                  | > cell indicates whether Emergency Calls are     |
|                  | > allowed for UEs with access classes 0 to 9 and |
|                  | > UEs without an IMSI. For UEs with access       |
|                  | > classes 11 to 15, Emergency Calls are not      |
|                  | > allowed if both \"Access class 10\" and the    |
|                  | > relevant Access Class (11 to 15) are barred.*  |
|                  | >                                                |
|                  | > *Classes 11 and 15 - Home PLMN only if the     |
|                  | > EHPLMN list is not present or any EHPLMN;*     |
|                  | >                                                |
|                  | > *Classes 12, 13, 14 - Home PLMN and visited    |
|                  | > PLMNs of home country only. For this purpose   |
|                  | > the home country is defined as the country of  |
|                  | > the MCC part of the IMSI.*                     |
|                  |                                                  |
|                  | -   *3GPP Release 9: Service Specific Access     |
|                  |     Control (SSAC)*                              |
|                  |                                                  |
|                  | > *SSAC provides a mechanism to minimize service |
|                  | > availability degradation (i.e. radio resource  |
|                  | > shortage) due to the mass simultaneous mobile  |
|                  | > originating session requests and maximize the  |
|                  | > availability of the wireless access resources  |
|                  | > for non-barred services by applying            |
|                  | > independent access control for telephony       |
|                  | > services (MMTEL) for mobile originating        |
|                  | > session requests from idle-mode and            |
|                  | > connected-mode. EPS provides a capability to   |
|                  | > assign a service probability factor and mean   |
|                  | > duration of access control for each of MMTEL   |
|                  | > voice and MMTEL video by broadcasting system   |
|                  | > information parameters for:*                   |
|                  |                                                  |
|                  | -   *assigning a barring rate (percentage)       |
|                  |     commonly applicable for Access Classes 0-9,* |
|                  |                                                  |
|                  | -   *assigning a flag barring status (barred     |
|                  |     /unbarred) for each Access Class in the      |
|                  |     range 11-15,*                                |
|                  |                                                  |
|                  | -   *SSAC does not apply to Access Class 10.*    |
|                  |                                                  |
|                  | ```{=html}                                       |
|                  | <!-- -->                                         |
|                  | ```                                              |
|                  | -   *3GPP Release 10: Access Control for Circuit |
|                  |     Switched Fallback (AC for CSFB)*             |
|                  |                                                  |
|                  | > *AC for CSFB provides a mechanism to prohibit  |
|                  | > UEs to access E-UTRAN to perform CSFB. It      |
|                  | > minimizes service availability degradation     |
|                  | > (i.e. radio resource shortage, congestion of   |
|                  | > fallback network) caused by mass simultaneous  |
|                  | > mobile originating requests for CSFB and       |
|                  | > increases the availability of the E-UTRAN      |
|                  | > resources for UEs accessing other services by  |
|                  | > broadcasting system information parameters for |
|                  | > AC for CSFB for each UE access class.*         |
|                  |                                                  |
|                  | -   *3GPP Release 11: Extended Access Class      |
|                  |     Barring (EAB)*                               |
|                  |                                                  |
|                  | > *EAB is a mechanism for controlling Mobile     |
|                  | > Originating access attempts from UEs that are  |
|                  | > configured for EAB in order to prevent         |
|                  | > overload of the access network and/or the core |
|                  | > network. In congestion situations, the         |
|                  | > operator can restrict access from UEs          |
|                  | > configured for EAB while permitting access     |
|                  | > from other UEs. UEs configured for EAB are     |
|                  | > considered more tolerant to access             |
|                  | > restrictions than other UEs. When an operator  |
|                  | > determines that it is appropriate to apply     |
|                  | > EAB, the network broadcasts system information |
|                  | > parameters for EAB UEs.*                       |
|                  |                                                  |
|                  | -   *3GPP Release 12: Overriding extended access |
|                  |     barring*                                     |
|                  |                                                  |
|                  | > *Overriding Extended Access Barring is a       |
|                  | > mechanism for the operator to allow UEs that   |
|                  | > are configured for EAB to access the network   |
|                  | > under EAB conditions. The UE configured to     |
|                  | > override extended access class barring         |
|                  | > overrides EAB restrictions as long as it has   |
|                  | > an active PDN connection for which EAB has     |
|                  | > been configured to not apply.*                 |
|                  |                                                  |
|                  | -   *3GPP Release 13: Application Specific       |
|                  |     Congestion Control for Data Communication    |
|                  |     (ACDC)*                                      |
|                  |                                                  |
|                  | > *ACDC is an access control mechanism for the   |
|                  | > operator to allow/prevent new access attempts  |
|                  | > from particular, operator-identified           |
|                  | > applications in the UE in idle mode. ACDC does |
|                  | > not apply to UEs in connected mode. For Access |
|                  | > Control based on ACDC categories, at           |
|                  | > subscription at least four ACDC categories are |
|                  | > allocated to the subscriber and stored in the  |
|                  | > ACDC MO or USIM. The network can               |
|                  | > prevent/mitigate overload of the access        |
|                  | > network and/or the core network. ACDC related  |
|                  | > parameterization is provided with system       |
|                  | > information broadcast.*                        |
|                  |                                                  |
|                  | -   *3GPP Release 15: Coverage Enhancement       |
|                  |     level-based access class barring*            |
|                  |                                                  |
|                  | > *Supports barring of eMTC and NB-IoT devices   |
|                  | > in specific coverage enhancement levels*       |
+------------------+--------------------------------------------------+
| **5.2.3.2.17**   | **Unicast, multicast and broadcast**             |
+------------------+--------------------------------------------------+
| 5.2.3.2.17.1     | Describe how the RIT/SRIT enables:               |
|                  |                                                  |
|                  | -- broadcast capabilities,                       |
|                  |                                                  |
|                  | -- multicast capabilities,                       |
|                  |                                                  |
|                  | -- unicast capabilities,                         |
|                  |                                                  |
|                  | using both dedicated carriers and/or shared      |
|                  | carriers. Please describe how all three          |
|                  | capabilities can exist simultaneously.           |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *The RIT supports mostly unicast transmission of |
|                  | data to/from users.\                             |
|                  | Broadcast capabilities pertain to support and    |
|                  | transmission of cell-wide system                 |
|                  | information/parameters, as well as               |
|                  | broacast/based emergency services (e.g. public   |
|                  | warning messages).*                              |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *The RIT is envisioned to support broadcast,     |
|                  | multicast and unicast services.*                 |
|                  |                                                  |
|                  | *For Broadcast/Multicast, LTE supports MBMS      |
|                  | (multimedia broadcast multicast service),        |
|                  | introduced in Rel-9, and further enhanced in the |
|                  | next releases.*                                  |
|                  |                                                  |
|                  | *Transmission of a MBMS in E-UTRAN uses either   |
|                  | multi-cell Multicast-broadcast single-frequency  |
|                  | network (MBSFN) or single-Cell                   |
|                  | Point-to-Multipoint (SC-PTM) transmission.       |
|                  | Multi-cell transmission of MBMS is characterized |
|                  | by Synchronous transmission of MBMS within its   |
|                  | MBSFN Area; for Single-cell transmission MBMS is |
|                  | transmitted in the coverage of a single cell.*   |
|                  |                                                  |
|                  | *In E-UTRAN, MBMS can be provided either on a    |
|                  | frequency layer shared with non-MBMS services    |
|                  | (set of cells supporting both unicast and MBMS   |
|                  | transmissions i.e. set of \"MBMS/Unicast-mixed   |
|                  | cells\") or on a frequency layer dedicated for   |
|                  | MBMS (set of cells supporting MBMS transmission  |
|                  | only i.e. set of \"MBMS-dedicated cells\").\     |
|                  | Among the latest MBMS enhancements, the          |
|                  | following features have been introduced          |
|                  | (Rel-14), targeting optimized support of TV      |
|                  | services, and other terrestrial broadcast        |
|                  | scenarios:*                                      |
|                  |                                                  |
|                  | -   ***Support of larger Inter-Site Distance     |
|                  |     (ISD)** **at high spectral efficiency,       |
|                  |     e.g..** a larger Cyclic Prefix (CP) to cover |
|                  |     up to 15km ISD;*                             |
|                  |                                                  |
|                  | -   *Mixed unicast and broadcast services over a |
|                  |     single carrier, using up to 100% broadcast   |
|                  |     resource allocation, and a self-contained    |
|                  |     system information and synchronisation       |
|                  |     signals for dedicated carriers;*             |
|                  |                                                  |
|                  | -   *New type of MBSFN subframe, without unicast |
|                  |     control region to reduce overhead;*          |
|                  |                                                  |
|                  | -   ***Shared eMBMS Broadcast:** operators can   |
|                  |     aggregate their eMBMS networks into a shared |
|                  |     eMBMS content distribution platform,         |
|                  |     improving coverage and bandwidth             |
|                  |     efficiency.*                                 |
|                  |                                                  |
|                  | *For NB-IoT/eMTC, recent broadcast/multicast     |
|                  | enhancements (Rel-14) are:*                      |
|                  |                                                  |
|                  | -   #### *Multicast downlink tran                |
|                  | smission based on Single-Cell Point-to-Multipoin |
|                  | t (SC-PTM).* {#multicast-downlink-transmission-b |
|                  | ased-on-single-cell-point-to-multipoint-sc-ptm.} |
+------------------+--------------------------------------------------+
| 5.2.3.2.17.2     | Describe whether the proposal is capable of      |
|                  | providing multiple user services simultaneously  |
|                  | to any user with appropriate channel capacity    |
|                  | assignments?                                     |
|                  |                                                  |
|                  | *[**For NR and LTE component RIT** (common       |
|                  | principles)]{.underline}*                        |
|                  |                                                  |
|                  | *Multiple services per user can be supported by  |
|                  | setting up multiple data radio bearers (DRBs)    |
|                  | per user/device. Each radio bearer is            |
|                  | characterized by an individual QoS               |
|                  | profile/flow.\                                   |
|                  | Multiple services per user/device can also be    |
|                  | supported by mapping multiple services to a      |
|                  | single bearer, if the QoS is the same for these  |
|                  | services.*                                       |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *The new SDAP sublayer (in the Access Stratum)   |
|                  | provides mapping function between (5GC) QoS      |
|                  | flows and DRBs.*                                 |
|                  |                                                  |
|                  | *See more details on QoS in 5.2.3.2.12 and       |
|                  | 5.2.3.2.13.*                                     |
+------------------+--------------------------------------------------+
| 5.2.3.2.17.3     | Provide details of the codec used.               |
|                  |                                                  |
|                  | Does the RIT/SRIT support multiple voice and/or  |
|                  | video codecs? Provide the detail.                |
|                  |                                                  |
|                  | *[**For NR and LTE component RIT** (common       |
|                  | principles)]{.underline}*                        |
|                  |                                                  |
|                  | *The RIT could support various voice and video   |
|                  | codecs, as desired. In fact, the radio interface |
|                  | technology (fully IP-based) is mostly agnostic   |
|                  | to such codecs, and capable of accommodating     |
|                  | diverse range of codec types, rates and          |
|                  | operation (fixed/dynamic/adaptive). This enables |
|                  | support for all main codecs used/defined today   |
|                  | (e.g. AMR-NB/WB, EVS), as well as the capability |
|                  | to support more enhanced codecs that may be      |
|                  | defined in future.*                              |
+------------------+--------------------------------------------------+
| **5.2.3.2.18**   | **Privacy, authorization, encryption,            |
|                  | authentication and legal intercept schemes**     |
+------------------+--------------------------------------------------+
| 5.2.3.2.18.1     | Any privacy, authorization, encryption,          |
|                  | authentication and legal intercept schemes that  |
|                  | are enabled in the radio interface technology    |
|                  | should be described. Describe whether any        |
|                  | synchronisation is needed for privacy and        |
|                  | encryptions mechanisms used in the RIT/SRIT.     |
|                  |                                                  |
|                  | Describe how the RIT/SRIT addresses the radio    |
|                  | access security, with a particular focus on the  |
|                  | following security items:                        |
|                  |                                                  |
|                  | -- system signalling integrity and               |
|                  | confidentiality,                                 |
|                  |                                                  |
|                  | -- user equipment identity authentication and    |
|                  | confidentiality,                                 |
|                  |                                                  |
|                  | -- subscriber identity authentication and        |
|                  | confidentiality,                                 |
|                  |                                                  |
|                  | -- user data integrity and confidentiality       |
|                  |                                                  |
|                  | Describe how the RIT/SRIT may be protected       |
|                  | against attacks, for example:                    |
|                  |                                                  |
|                  | -- passive,                                      |
|                  |                                                  |
|                  | -- man in the middle,                            |
|                  |                                                  |
|                  | -- replay,                                       |
|                  |                                                  |
|                  | -- denial of service.                            |
|                  |                                                  |
|                  | ***For NR component RIT:***                      |
|                  |                                                  |
|                  | *NR has made substantial enhancements to         |
|                  | subscriber's privacy compared to earlier         |
|                  | generations, see 3GPP TS 33.501. The most        |
|                  | important enhancement is the concealment of      |
|                  | subscription permanent identifier over-the-air.  |
|                  | This feature is mainly aimed against the active  |
|                  | attacker. Another enhancement is the guaranteed  |
|                  | regular refreshment of subscription temporary    |
|                  | identifier. This feature is mainly aimed against |
|                  | the passive attacker. Another enhancement is the |
|                  | decoupling of the permanent identifier from the  |
|                  | Paging mechanism, i.e., there is no longer a     |
|                  | Paging message with permanent identifier, the    |
|                  | Paging timings are no longer based on permanent  |
|                  | identifier. This feature mitigates privacy       |
|                  | attacks that use side-channel information in the |
|                  | Paging protocol. Another enhancement comes from  |
|                  | the best effort protection of information in the |
|                  | initial message, i.e., if security is setup,     |
|                  | privacy sensitive information is concealed,      |
|                  | otherwise skipped until the security is setup.   |
|                  | Yet another effort is description of a           |
|                  | device-assisted network-based framework for      |
|                  | false base station detection. This feature can   |
|                  | be used to thwart denial-of-service kind of      |
|                  | attackers. One enhancement is to increase the    |
|                  | authentication between the service network and   |
|                  | the core network, or the function of the home    |
|                  | network control which can be used to prevent     |
|                  | false fraud of the service network.*             |
|                  |                                                  |
|                  | *One enhancement is mitigation of bidding down   |
|                  | attacks, this feature is to avoid the lower      |
|                  | security features of the UE or network           |
|                  | selection.*                                      |
|                  |                                                  |
|                  | *Another enhancement is the authorization and    |
|                  | authentication of the security and network       |
|                  | capabilities of the serviced interface*          |
|                  |                                                  |
|                  | *The new features in NR, e.g., multi             |
|                  | connectivity, and deploying a single base        |
|                  | station as two split units, also help improve    |
|                  | resilience of the radio access network.*         |
|                  |                                                  |
|                  | *Authentication/authorization in NR builds on    |
|                  | strong cryptographic primitives and security     |
|                  | characteristics that already existed in          |
|                  | LTE-Advanced. On top of this, NR has made great  |
|                  | improvement by introduction of the flexible      |
|                  | authentication framework for both the 3GPP and   |
|                  | non-3GPP network. Even further, NR has           |
|                  | significantly reduced the risk of fraud against  |
|                  | the subscribers. An enhancement for NR is that a |
|                  | security anchor (SEAF) is introduced in the      |
|                  | authentication framework. And the secondary      |
|                  | authentication of the external network is        |
|                  | increased.*                                      |
|                  |                                                  |
|                  | *NR includes protection against eavesdropping,   |
|                  | modification, and replay attacks. The strong and |
|                  | well-proven security algorithms from the         |
|                  | LTE-Advanced system are reused and support the   |
|                  | transport of 256 bit key*s*. Signalling traffic  |
|                  | is encrypted and integrity protected. User plane |
|                  | traffic is encrypted and can be integrity        |
|                  | protected. This integrity protection of user     |
|                  | plane traffic is a new enhancement in NR.*       |
|                  |                                                  |
|                  | *It is mandatory to integrity protect radio      |
|                  | resource control messages that redirect devices. |
|                  | This feature makes it infeasible for attackers   |
|                  | to perform rogue redirections.*                  |
|                  |                                                  |
|                  | *Various timers are specified for different      |
|                  | scenarios for devices to wait and retry          |
|                  | connecting with the network. This feature        |
|                  | mitigates the risk of attackers trying to keep   |
|                  | devices locked out from the network.*            |
|                  |                                                  |
|                  | *All the enhancements in NR are made while       |
|                  | simultaneously complying with regulatory duties. |
|                  | Legal intercept is provided by core network      |
|                  | functions.*                                      |
+------------------+--------------------------------------------------+
| **5.2.3.2.19**   | **Frequency planning**                           |
+------------------+--------------------------------------------------+
| 5.2.3.2.19.1     | How does the RIT/SRIT support adding new cells   |
|                  | or new RF carriers? Provide details.             |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *1008 physical cell identities are supported.    |
|                  | Thus, theoretically 1008-cell reuse is realized. |
|                  | In the case of NR operating with a TDD carrier   |
|                  | and an SUL carrier, the cell identity is the     |
|                  | same. In the case of NR operating with carrier   |
|                  | aggregation, the cell identities are allocated   |
|                  | to each of the aggregated carrier.*              |
|                  |                                                  |
|                  | *Actual cell deployment is operation specific.   |
|                  | Self configuration can be also supported.*       |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *504 physical cell identities are supported.     |
|                  | Thus, theoretically 504-cell reuse is realized.  |
|                  | In the case of LTE operating with carrier        |
|                  | aggregation, the cell identities are allocated   |
|                  | to each of the aggregated carrier.*              |
|                  |                                                  |
|                  | *Actual cell deployment is operation specific.   |
|                  | Self configuration is also supported.*           |
+------------------+--------------------------------------------------+
| **5.2.3.2.20**   | **Interference mitigation within radio           |
|                  | interface**                                      |
+------------------+--------------------------------------------------+
| 5.2.3.2.20.1     | Does the proposal support Interference           |
|                  | mitigation? If so, describe the corresponding    |
|                  | mechanism.                                       |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *The RIT has been designed with the aim to       |
|                  | minimize the always-on signals to reduce the     |
|                  | interference in the system. This is achieved     |
|                  | by:*                                             |
|                  |                                                  |
|                  | -   *Support longer periodicities for            |
|                  |     synchronization signals, broadcast channels  |
|                  |     and periodic reference signals*              |
|                  |                                                  |
|                  | -   *Use UE-specific demodulation reference      |
|                  |     signals for control and data that are only   |
|                  |     transmitted when control and/or data is      |
|                  |     being transmitted*                           |
|                  |                                                  |
|                  | -   *Control channel resource allocation in the  |
|                  |     frequency domain is configurable to reduce   |
|                  |     the interference to control channels in      |
|                  |     neighbouring cells*                          |
|                  |                                                  |
|                  | *Coordinated multipoint transmission/reception   |
|                  | (CoMP) is another approach supported by the RIT  |
|                  | to mitigate interference between cells and       |
|                  | improve system performance by dynamic            |
|                  | coordination in the scheduling/transmission      |
|                  | between/from multiple cell sites.*               |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *Static inter-cell interference mitigation is    |
|                  | supported by means of e.g. frequency reuse, soft |
|                  | frequency reuse, and reuse partitioning.*        |
|                  |                                                  |
|                  | *Inter-cell interference mitigation is supported |
|                  | by means of exchanging interference measurements |
|                  | and scheduling decisions between base stations,  |
|                  | see also 5.2.3.2.20.2 below.*                    |
|                  |                                                  |
|                  | *Coordinated multipoint transmission/reception   |
|                  | (CoMP) is another approach supported by the RIT  |
|                  | to mitigate interference between cells and       |
|                  | improve system performance.*                     |
|                  |                                                  |
|                  | *Coordinated multipoint transmission implies     |
|                  | dynamic coordination in the                      |
|                  | scheduling/transmission and/or joint             |
|                  | transmission between/from multiple cell sites.*  |
|                  |                                                  |
|                  | *Coordinated multipoint reception implies        |
|                  | dynamic coordination in the scheduling and/or    |
|                  | joint reception between/at difference cell       |
|                  | sites.*                                          |
|                  |                                                  |
|                  | *The coordinated cell sites could either         |
|                  | correspond to cells of the same eNB (intra-eNB   |
|                  | coordination) or different eNB (inter-eNB        |
|                  | coordination).*                                  |
|                  |                                                  |
|                  | *For eMTC and NB-IoT a repetition based          |
|                  | transmission scheme is supported where coherent  |
|                  | reception of repeated transmission supports      |
|                  | suppression of interference. Cell and user based |
|                  | scrambling is also implemented to support this   |
|                  | mechanism. eMTC supports frequency hopping to    |
|                  | reduce the impact from interference.*            |
+------------------+--------------------------------------------------+
| 5.2.3.2.20.2     | What is the signalling, if any, which can be     |
|                  | used for intercell interference mitigation?      |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *[To support handling of Cross Link Interference |
|                  | (CLI) and for Remote Interference Management     |
|                  | (RIM), NR will support inter-base station        |
|                  | signalling via the Xn interface and the core     |
|                  | network. This is further described in TR         |
|                  | 38.866.]{.underline}*                            |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *To aid inter-cell interference mitigation, the  |
|                  | RIT defines three indicators exchanged between   |
|                  | base stations: The High-interference Indicator   |
|                  | (HI) which provides information to neighbouring  |
|                  | cells about the part of the cell bandwidth upon  |
|                  | which the cell intends to schedule its cell-edge |
|                  | user, the Overload Indicator (OI) which provides |
|                  | information on the uplink interference level     |
|                  | experienced in each part of the cell bandwidth   |
|                  | and Relative Narrowband TX Power (RNTP)          |
|                  | indicator, which provides information on the     |
|                  | downlink transmission power.*                    |
+------------------+--------------------------------------------------+
| 5.2.3.2.20.3     | *Link level interference mitigation*             |
|                  |                                                  |
|                  | Describe the feature or features used to         |
|                  | mitigate intersymbol interference.               |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *Time and frequency synchronization to the DL    |
|                  | and UL frame structures in combination with the  |
|                  | use of a cyclic prefix OFDM transmission in both |
|                  | UL(with or without transform precoding) and DL,  |
|                  | provides robustness against intersymbol          |
|                  | interference.*                                   |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *Time and frequency synchronization to the DL    |
|                  | and UL frame structures in combination with the  |
|                  | use of a cyclic prefix OFDM transmission in both |
|                  | UL (with or without transform precoding) and DL, |
|                  | provides robustness against intersymbol          |
|                  | interference.*                                   |
|                  |                                                  |
|                  | ***See also answer to 5.2.3.2.20.4***            |
+------------------+--------------------------------------------------+
| 5.2.3.2.20.4     | Describe the approach taken to cope with         |
|                  | multipath propagation effects (e.g. via          |
|                  | equalizer, rake receiver, cyclic prefix, etc.).  |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *The use of OFDM transmission in both UL and DL, |
|                  | in combination with a cyclic prefix, provides    |
|                  | inherent robustness to                           |
|                  | time-dispersion/frequency-selectivity on the     |
|                  | radio channel.*                                  |
|                  |                                                  |
|                  | *In case of transform precoding in the UL,       |
|                  | time-dispersion/frequency-selectivity on the     |
|                  | radio channel can be handled by receiver-side    |
|                  | equalization.*                                   |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *On the downlink, the use of OFDM transmission,  |
|                  | in combination with a cyclic prefix, provides    |
|                  | inherent robustness to                           |
|                  | time-dispersion/frequency-selectivity on the     |
|                  | radio channel.*                                  |
|                  |                                                  |
|                  | *On the uplink,                                  |
|                  | time-dispersion/frequency-selectivity on the     |
|                  | radio channel can be handled by receiver-side    |
|                  | equalization. The detailed equalization approach |
|                  | is implementation dependent. Examples of         |
|                  | equalization approaches include frequency-domain |
|                  | linear equalization and Turbo equalization. The  |
|                  | use of cyclic prefix also for the uplink may     |
|                  | simplify the equalizer implementation.*          |
+------------------+--------------------------------------------------+
| 5.2.3.2.20.5     | *Diversity techniques*                           |
|                  |                                                  |
|                  | Describe the diversity techniques supported in   |
|                  | the user equipment and at the base station,      |
|                  | including micro diversity and macro diversity,   |
|                  | characterizing the type of diversity used, for   |
|                  | example:                                         |
|                  |                                                  |
|                  | -- Time diversity: repetition, Rake-receiver,    |
|                  | etc.                                             |
|                  |                                                  |
|                  | -- Space diversity: multiple sectors, etc.       |
|                  |                                                  |
|                  | -- Frequency diversity: frequency hopping (FH),  |
|                  | wideband transmission, etc.                      |
|                  |                                                  |
|                  | -- Code diversity: multiple PN codes, multiple   |
|                  | FH code, etc.                                    |
|                  |                                                  |
|                  | -- Multi-user diversity: proportional fairness   |
|                  | (PF), etc.                                       |
|                  |                                                  |
|                  | -- Other schemes.                                |
|                  |                                                  |
|                  | Characterize the diversity combining algorithm,  |
|                  | for example, switched diversity, maximal ratio   |
|                  | combining, equal gain combining.                 |
|                  |                                                  |
|                  | Provide information on the receiver/transmitter  |
|                  | RF configurations, for example:                  |
|                  |                                                  |
|                  | -- number of RF receivers                        |
|                  |                                                  |
|                  | -- number of RF transmitters.                    |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *The RIT provides the following means for        |
|                  | diversity:*                                      |
|                  |                                                  |
|                  | -   *Space diversity by means of multiple        |
|                  |     transmit and receiver antennas and           |
|                  |     beamforming*                                 |
|                  |                                                  |
|                  |     -   *Number of TX-antenna ports: This is a   |
|                  |         deployment choice, but for the purpose   |
|                  |         of multi-layer transmissions up to 12    |
|                  |         downlink and up to 4 uplink antenna      |
|                  |         ports have been defined where the        |
|                  |         mapping of ports to physical antennas is |
|                  |         an implementation issue*                 |
|                  |                                                  |
|                  |     -   *Number of RX antenna ports:             |
|                  |         Implementation specific*                 |
|                  |                                                  |
|                  | -   *Frequency diversity by means of wide        |
|                  |     overall transmission bandwidth and           |
|                  |     possibility for uplink frequency hopping and |
|                  |     uplink and downlink frequency-distributed    |
|                  |     transmissions*                               |
|                  |                                                  |
|                  | -   *Time diversity by means of fast             |
|                  |     retransmissions with hybrid ARQ protocol     |
|                  |     allowing combining of the retransmissions    |
|                  |     with the original transmission*              |
|                  |                                                  |
|                  | -   *Multi-user diversity by means of            |
|                  |     channel-aware scheduling*                    |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *The RIT provides the following means for        |
|                  | diversity:*                                      |
|                  |                                                  |
|                  | -   *Space diversity by means of multiple        |
|                  |     transmit and receiver antennas*              |
|                  |                                                  |
|                  |     -   *Number of TX antenna ports: Up to 8     |
|                  |         (DL), up to 4 (UL) logical antenna ports |
|                  |         are defined where the mapping of logical |
|                  |         antenna ports to physical antennas is an |
|                  |         implementation specific configuration.*  |
|                  |                                                  |
|                  |     -   *Number of RX antenna ports:             |
|                  |         Implementation specific*                 |
|                  |                                                  |
|                  | -   *Frequency diversity by means of wide        |
|                  |     overall transmission bandwidth. Possibility  |
|                  |     for uplink frequency hopping on a slot basis |
|                  |     and downlink frequency-distributed           |
|                  |     transmission*                                |
|                  |                                                  |
|                  | -   *Time diversity by means of fast             |
|                  |     retransmissions*                             |
|                  |                                                  |
|                  | -   *Multi-user diversity by means of            |
|                  |     channel-aware scheduling*                    |
|                  |                                                  |
|                  | *For NB-IoT transmission 2 DL and 1 UL logical   |
|                  | antenna ports are defined. For eMTC, frequency   |
|                  | and time diversity is supported by frequency     |
|                  | hopping and time based repetitions on all        |
|                  | physical channels.*                              |
+------------------+--------------------------------------------------+
| **5.2.3.2.21**   | **Synchronization requirements**                 |
+------------------+--------------------------------------------------+
| 5.2.3.2.21.1     | Describe RIT's/SRIT's timing requirements, e.g.  |
|                  |                                                  |
|                  | -- Is base station-to-base station               |
|                  | synchronization required? Provide precise        |
|                  | information, the type of synchronization, i.e.,  |
|                  | synchronization of carrier frequency, bit clock, |
|                  | spreading code or frame, and their accuracy.     |
|                  |                                                  |
|                  | -- Is base station-to-network synchronization    |
|                  | required?                                        |
|                  |                                                  |
|                  | State short-term frequency and timing accuracy   |
|                  | of base station transmit signal.                 |
|                  |                                                  |
|                  | *[**For NR and LTE component                     |
|                  | RIT:**]{.underline}*                             |
|                  |                                                  |
|                  | *[Common general aspects]{.underline}*           |
|                  |                                                  |
|                  | *Tight BS-to-BS synchronization is not required. |
|                  | Likewise, tight BS-to-network synchronization is |
|                  | not required.*                                   |
|                  |                                                  |
|                  | *The BS shall support a logical synchronization  |
|                  | port for phase-, time- and/or frequency          |
|                  | synchronization, e.g. to provide.*               |
|                  |                                                  |
|                  | -   *accurate maximum relative phase difference  |
|                  |     for all BSs in synchronized TDD area*        |
|                  |                                                  |
|                  | -   *continuous time without leap seconds        |
|                  |     traceable to common time reference for all   |
|                  |     BSs in synchronized TDD area;*               |
|                  |                                                  |
|                  | -   *FDD time domain inter-cell interference     |
|                  |     coordination.*                               |
|                  |                                                  |
|                  | *Furthermore, common SFN initialization time     |
|                  | shall be provided for all BSs in synchronized    |
|                  | TDD area.*                                       |
|                  |                                                  |
|                  | *A certain RAN-CN Hyper SFN synchronization is   |
|                  | required in case of extended Idle mode DRX.*     |
|                  |                                                  |
|                  | *[Some accuracy requirements]{.underline}*       |
|                  |                                                  |
|                  | *BS transmit signals accuracy:*                  |
|                  |                                                  |
|                  | -   *LTE:*                                       |
|                  |                                                  |
|                  |     -   *Frequency accuracy (wide area BS):      |
|                  |         within ±0.05 ppm, observed over 1ms*     |
|                  |                                                  |
|                  |     -   *Timing accuracy: time alignment error   |
|                  |         (TAE) is within 65 ns for single carrier |
|                  |         (MIMO or TX div), 130 ns for intra-band  |
|                  |         contiguous carrier aggregation, 260 ns   |
|                  |         for intra-band non-contiguous and        |
|                  |         inter-band CA.*                          |
|                  |                                                  |
|                  | -   *NR:.*                                       |
|                  |                                                  |
|                  |     -   *Frequency accuracy (wide area BS):      |
|                  |         within ±0.05 ppm, observed over 1ms*     |
|                  |                                                  |
|                  |     -   *Timing accuracy: time alignment error   |
|                  |         (TAE) is within 65 ns for single carrier |
|                  |         (MIMO or TX div), 260 ns for intra-band  |
|                  |         contiguous carrier aggregation, 3µs for  |
|                  |         intra-band non-contiguous and inter-band |
|                  |         CA.*                                     |
|                  |                                                  |
|                  | *Cell phase synchronization accuracy:*           |
|                  |                                                  |
|                  | -   *NR: The cell phase synchronization accuracy |
|                  |     measured at BS antenna connectors shall be   |
|                  |     better than 3 µs.*                           |
|                  |                                                  |
|                  | -   *LTE: for Wide Area BS (not considering Home |
|                  |     BS), the cell phase synchronization accuracy |
|                  |     measured at BS antenna connectors shall be   |
|                  |     better than 3 µs for small cells (radius up  |
|                  |     to 3km), 10 µs for large cells (radius above |
|                  |     3km).*                                       |
|                  |                                                  |
|                  | *For more information please refer to*           |
|                  |                                                  |
|                  | -   *NR: \[38.401\], \[38.133\], \[38.104\].*    |
|                  |                                                  |
|                  | -   *LTE: \[36.401\], \[36.133\], \[368.104\].*  |
+------------------+--------------------------------------------------+
| 5.2.3.2.21.2     | Describe the synchronization mechanisms used in  |
|                  | the proposal, including synchronization between  |
|                  | a user terminal and a base station.              |
|                  |                                                  |
|                  | *[**For NR and LTE component RIT** (common       |
|                  | principles)]{.underline}*                        |
|                  |                                                  |
|                  | *Cell search is the procedure by which a UE      |
|                  | acquires time and frequency synchronization with |
|                  | a cell and detects the physical layer Cell ID of |
|                  | that cell. A UE receives the following           |
|                  | synchronization signals (SS) in order to perform |
|                  | cell search: the primary synchronization signal  |
|                  | (PSS) and secondary synchronization signal       |
|                  | (SSS). PSS is used (at least) for initial symbol |
|                  | boundary, cyclic prefix, sub frame boundary,     |
|                  | initial frequency synchronization to the cell.   |
|                  | SSS is used for radio frame boundary             |
|                  | identification. PSS and SSS together used for    |
|                  | cell ID detection.*                              |
|                  |                                                  |
|                  | *Other synchronization mechanisms are defined    |
|                  | e.g. for Radio link monitoring, Transmission     |
|                  | timing adjustments, Timing for cell activation / |
|                  | deactivation.*                                   |
|                  |                                                  |
|                  | *[- For NB-IOT]{.underline}*                     |
|                  |                                                  |
|                  | *NB-IoT cell search/synchronization is based on  |
|                  | dedicated narrowband signals transmitted in the  |
|                  | downlink: the primary and secondary narrowband   |
|                  | synchronization signals.*                        |
|                  |                                                  |
|                  | *See more information in:*                       |
|                  |                                                  |
|                  | -   *NR: \[38.213\] sub-clause 4 and \[38.211\]  |
|                  |     sub-clause 7.4.2.*                           |
|                  |                                                  |
|                  | -   *LTE: \[36.213\] and \[36.211\].*            |
|                  |                                                  |
|                  | *[- For eMTC]{.underline}*                       |
|                  |                                                  |
|                  | *In addition to support for the PSS and SSS,     |
|                  | eMTC supports the Resynchronization Signal (RSS) |
|                  | which facilitates an efficient resynchronization |
|                  | to the serving cell.*                            |
+------------------+--------------------------------------------------+
| **5.2.3.2.22**   | **Link budget template**                         |
|                  |                                                  |
|                  | Proponents should complete the link budget       |
|                  | template in § **45.2.3.3** to this description   |
|                  | template for the environments supported in the   |
|                  | RIT.                                             |
|                  |                                                  |
|                  | *The information is provided with link budget    |
|                  | template.*                                       |
+------------------+--------------------------------------------------+
| **5.2.3.2.23**   | **Support for wide range of services**           |
+------------------+--------------------------------------------------+
| **5.2.3.2.23.1** | **Describe what kind of services/applications    |
|                  | can be supported in each usage scenarios in      |
|                  | Recommendation ITU-R M.2083 (eMBB, URLLC, and    |
|                  | mMTC).**                                         |
|                  |                                                  |
|                  | ***This proposal supports a wide range of        |
|                  | services across the diverse usage scenarios      |
|                  | including eMBB, URLLC, and mMTC envisaged in     |
|                  | Recommendation ITU-R M.2083.***                  |
|                  |                                                  |
|                  | ***The example services supported by this        |
|                  | proposal include the services defined in***      |
|                  | ***Recommendation ITU-R M.1822, \[22.261\], and  |
|                  | other services, such as***                       |
|                  |                                                  |
|                  | -   ***eMBB services including conversational    |
|                  |     services (including basic/ rich              |
|                  |     conversational services, low delay           |
|                  |     conversational services), interactive (with  |
|                  |     high and low delay) services, streaming      |
|                  |     (live/non-live) services, and other high     |
|                  |     data rate services; for stationary users,    |
|                  |     pedestrian users, to high speed              |
|                  |     train/vehicle users.***                      |
|                  |                                                  |
|                  | -   ***URLLC services including transportation   |
|                  |     safety, smart grid, mobile health            |
|                  |     application, wireless industry automation,   |
|                  |     etc.***                                      |
|                  |                                                  |
|                  | -   ***mMTC services including smart city, smart |
|                  |     home applications, and other machine-type    |
|                  |     communication (also known as                 |
|                  |     Machine-to-Machine (M2M)) services.***       |
+------------------+--------------------------------------------------+
| **5.2.3.2.23.2** | **Describe any capabilities/features to flexibly |
|                  | deploy a range of services across different      |
|                  | usage scenarios (eMBB, URLLC, and mMTC) in an    |
|                  | efficient manner, (e.g., a proposed RIT/SRIT is  |
|                  | designed to use a single continuous or multiple  |
|                  | block(s) of spectrum).**                         |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *NR is capable of deploying a range of services  |
|                  | across different usage scenarios. While the      |
|                  | specification does not match any physical layer  |
|                  | functionality to any service, different          |
|                  | components can benefit different services in     |
|                  | specific usage scenarios.*                       |
|                  |                                                  |
|                  | *Specifically, the following low latency         |
|                  | structures cater especially to the URLLC         |
|                  | services*                                        |
|                  |                                                  |
|                  | > -     *Front loaded DMRS allows for the        |
|                  | > channel estimate to be ready before the full   |
|                  | > data block is received*                        |
|                  | >                                                |
|                  | > -     *Frequency-first mapping of data bits to |
|                  | > physical resources allows for the channel      |
|                  | > decoder to operate in a pipelined fashion,     |
|                  | > starting to decode the data block immediately  |
|                  | > when the first symbol has been received*       |
|                  | >                                                |
|                  | > -     *Very tight UE processing time budget    |
|                  | > especially targeted for ultra-low latency      |
|                  | > device types*                                  |
|                  | >                                                |
|                  | > -     *Very short scheduling interval achieved |
|                  | > with both high subcarrier spacing (short       |
|                  | > symbol duration) and the possibility to        |
|                  | > schedule short time intervals only*            |
|                  | >                                                |
|                  | > *- At least an UL transmission scheme without  |
|                  | > scheduling grant is supported to reduce UL     |
|                  | > latency.*                                      |
|                  |                                                  |
|                  | *mMTC services can benefit from the following    |
|                  | components*                                      |
|                  |                                                  |
|                  | > -     *DFT-spreading and Pi/2 BPSK modulation  |
|                  | > for reduced PAPR and increased average Tx      |
|                  | > power for better coverage*                     |
|                  | >                                                |
|                  | > -     *Slot aggregation for both control and   |
|                  | > data for better coverage*                      |
|                  | >                                                |
|                  | > -     *High-aggregation level downlink control |
|                  | > for better coverage*                           |
|                  | >                                                |
|                  | > -     *RRC inactive state for optimized        |
|                  | > signalling overhead when moving to active      |
|                  | > state*                                         |
|                  | >                                                |
|                  | > -     *Extended DRX cycle for RRC active state |
|                  | > to improve battery life*                       |
|                  | >                                                |
|                  | > -     *Support for narrow-band (low-cost) UEs  |
|                  | > within a wide-band carrier*                    |
|                  |                                                  |
|                  | *URLLC, eMBB and mMTC services can coexist       |
|                  | within the same spectrum in both time and        |
|                  | frequency domain in multiplexed manner. URLLC    |
|                  | can pre-empt ongoing eMBB/mMTC transmissions, if |
|                  | necessary, and URLLC services can be mapped to   |
|                  | e.g. a shorter allocation duration for lower     |
|                  | latency by small number of scheduled symbols, as |
|                  | well as by using higher sub-carrier spacing and  |
|                  | thus allocation duration for the same number of  |
|                  | scheduled symbols, while eMBB services can be    |
|                  | mapped to do the opposite. Different sub-carrier |
|                  | spacings and scheduling interval durations       |
|                  | **that are appropriate to the desired service    |
|                  | type (e.g., different latency and data rate      |
|                  | requirements)** can coexist in a single carrier  |
|                  | with no need for fixed divisions within the      |
|                  | carrier, by e.g., using **spectral refinement    |
|                  | techniques such as** filtering, windowing, etc.  |
|                  | with the designated waveforms for NR.*           |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *LTE is capable of deploying a range of services |
|                  | across different usage scenarios. While the      |
|                  | specification does not match any physical layer  |
|                  | functionality to any service, different          |
|                  | components can benefit different services in     |
|                  | specific usage scenarios.*                       |
|                  |                                                  |
|                  | *Specifically, the following low latency         |
|                  | components are enabled*                          |
|                  |                                                  |
|                  | -   *Frequency-first mapping of data bits to     |
|                  |     physical resources allows for the channel    |
|                  |     decoder to operate in a pipelined fashion,   |
|                  |     starting to decode the data block            |
|                  |     immediately when the first symbol has been   |
|                  |     received*                                    |
|                  |                                                  |
|                  | -   *Short scheduling interval achieved with     |
|                  |     short TTI length (see item 5.2.3.2.7 and     |
|                  |     reference therein)*                          |
|                  |                                                  |
|                  | -   *Configurable shorter uplink                 |
|                  |     semi-persistent-scheduling (SPS) interval    |
|                  |     (can be less than 10 subframes, e.g. 1ms) is |
|                  |     introduced to reduce uplink latency for      |
|                  |     SPS.*                                        |
|                  |                                                  |
|                  | -   *Uplink skipping mechanism is introduced for |
|                  |     SPS to avoid resource release such that the  |
|                  |     latency of waiting for the next SPS uplink   |
|                  |     grant can be avoided.*                       |
|                  |                                                  |
|                  | *mMTC services are supported by NB-IoT / eMTC*   |
|                  |                                                  |
|                  | -   *DFT-spreading and Pi/2 BPSK (for both       |
|                  |     NB-IoT and eMTC) and Pi/4 QPSK (for NB-IoT)  |
|                  |     modulation for reduced PAPR for better       |
|                  |     coverage*                                    |
|                  |                                                  |
|                  | -   *  Repetition of a transmission for both     |
|                  |     control and data for better coverage*        |
|                  |                                                  |
|                  | -   *RV cycling to improve code rates for better |
|                  |     coverage*                                    |
|                  |                                                  |
|                  | -   *Cyclic repetition to enable symbol-level    |
|                  |     I/Q combining and to improve                 |
|                  |     frequency/timing offset tracking for better  |
|                  |     coverage*                                    |
|                  |                                                  |
|                  | -   *   Frequency hopping in eMTC to improve     |
|                  |     frequency diversity for better coverage*     |
|                  |                                                  |
|                  | -   *    High-aggregation level downlink control |
|                  |     in eMTC for better coverage*                 |
|                  |                                                  |
|                  | -   *    Small data transmission during random   |
|                  |     access without moving to RRC connected mode  |
|                  |     for optimized signalling overhead*           |
|                  |                                                  |
|                  | -   *    PSM mode and extended DRX cycle for RRC |
|                  |     IDLE mode to improve battery life*           |
|                  |                                                  |
|                  | -   *    Support for narrow-band (low-cost) UEs  |
|                  |     within a wide-band carrier system; 1.08 MHz  |
|                  |     for eMTC and 180kHz for NB-IoT.*             |
|                  |                                                  |
|                  | -   *  Support for single sub-carrier and        |
|                  |     sub-PRB (3 and 6 subcarriers) uplink         |
|                  |     transmission in NB-IoT, and sub-PRB (3 and 6 |
|                  |     subcarriers) transmission for eMTC, to       |
|                  |     increase connection density in extended      |
|                  |     coverage*                                    |
|                  |                                                  |
|                  | ***LTE is capable of deploying a range of        |
|                  | services, e.g., mMTC and eMBB services, on a     |
|                  | single continuous block of spectrum, by e.g.,    |
|                  | eMTC in-band operation or NB-IoT with in-band /  |
|                  | guard-band operation (see item** 5.2.3.2.8.1     |
|                  | **for more details).***                          |
+------------------+--------------------------------------------------+
| **5.2.3.2.24**   | **Global circulation of terminals**              |
|                  |                                                  |
|                  | **Describe technical basis for global            |
|                  | circulation of terminals not causing harmful     |
|                  | interference in any country where they           |
|                  | circulate, including a case when terminals have  |
|                  | capability of device-to-device direct            |
|                  | communication mode.**                            |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *3GPP defines a set of NR frequency bands with   |
|                  | band specific requirements in such a way that    |
|                  | each band complies to the regulatory             |
|                  | requirements of a given region or regions within |
|                  | the used deployment. The gNB broadcasts the band |
|                  | information on the deployed carriers and         |
|                  | possible additional transmit requirements for    |
|                  | the UE to comply to. If the UE is not able to    |
|                  | comply with the requirements provided by the     |
|                  | network, it is not allowed to initiate           |
|                  | connection towards the gNB on that band.*        |
|                  |                                                  |
|                  | *In more detail, for a given band, a             |
|                  | transmission the spectrum mask is specified in   |
|                  | terms of a normative (general) spectrum emission |
|                  | mask and an additional spectrum mask \[38.101,   |
|                  | section 6.5\]. The additional spectrum emission  |
|                  | mask which is signaled by the network to the UE  |
|                  | as a normative requirement can be used to        |
|                  | address; a specific regional regulatory          |
|                  | requirement, a frequency band specific           |
|                  | requirement, a roaming requirement and a         |
|                  | specific deployment scenario. This additional    |
|                  | spectrum emission mask can be used to support    |
|                  | the many different sharing requirements in terms |
|                  | of co-existence for a global roaming terminal.*  |
|                  |                                                  |
|                  | *3GPP Release 16 is working to introduce two     |
|                  | side link operation modes, where the harmful     |
|                  | interference is managed by the network:*         |
|                  |                                                  |
|                  | -   *Mode 1: The NR gNB schedules the UE's       |
|                  |     sidelink, and the UE will only transmit on   |
|                  |     its sidelink when scheduled by the gNB it is |
|                  |     connected to.*                               |
|                  |                                                  |
|                  | -   *Mode 2: The UE's sidelink is preconfigured  |
|                  |     and the configuration can be updated         |
|                  |     whenever the UE has IP connectivity. The     |
|                  |     sidelink configuration includes a            |
|                  |     geographical area or areas in which the      |
|                  |     slidenk transmissions are allowed, and if    |
|                  |     the UE moves out of the geographical area(s) |
|                  |     it is not allowed to transmit on the         |
|                  |     sidelink.*                                   |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *3GPP defines a set of LTE frequency bands with  |
|                  | band specific requirements in such a way that    |
|                  | each band complies to the regulatory             |
|                  | requirements of a given region or regions within |
|                  | the used deployment. The eNB broadcasts the band |
|                  | information on the deployed carriers and         |
|                  | possible additional transmit requirements for    |
|                  | the UE to comply to. If the UE is not able to    |
|                  | comply with the requirements provided by the     |
|                  | network, it is not allowed to initiate           |
|                  | connection towards the eNB on that band.*        |
|                  |                                                  |
|                  | *In more detail, for a given band, a             |
|                  | transmission the spectrum mask is specified in   |
|                  | terms of a normative (general) spectrum emission |
|                  | mask and an additional spectrum mask \[36.101,   |
|                  | section 6.6\]. The additional spectrum emission  |
|                  | mask which is signaled by the network to the UE  |
|                  | as a normative requirement can be used to        |
|                  | address; a specific regional regulatory          |
|                  | requirement, a frequency band specific           |
|                  | requirement, a roaming requirement and a         |
|                  | specific deployment scenario. This additional    |
|                  | spectrum emission mask can be used to support    |
|                  | the many different sharing requirements in terms |
|                  | of co-existence for a global roaming terminal.*  |
|                  |                                                  |
|                  | *LTE supports a direct device-to-device          |
|                  | communication mode with a sidelink. This         |
|                  | communication mode is supported when the UE is   |
|                  | served by E-UTRAN as well as when the UE is      |
|                  | outside of E-UTRA coverage. Only those UEs       |
|                  | authorized to be used for public safety and/or   |
|                  | V2X operation can perform sidelink               |
|                  | communication. The authorization is determined   |
|                  | by the user subscription and acquired from the   |
|                  | system information, and includes a possibility   |
|                  | to limit the authorization to operate the        |
|                  | sidelink while out of coverage to a specific     |
|                  | geographical area.*                              |
+------------------+--------------------------------------------------+
| **5.2.3.2.25**   | **Energy efficiency**                            |
|                  |                                                  |
|                  | Describe how the RIT/SRIT supports a high sleep  |
|                  | ratio and long sleep duration.                   |
|                  |                                                  |
|                  | Describe other mechanisms of the RIT/SRIT that   |
|                  | improve the support of energy efficiency         |
|                  | operation for both network and device.           |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | ***[Network energy efficiency]{.underline}***    |
|                  |                                                  |
|                  | *The fundamental always-on transmission that     |
|                  | must take place is the periodic SS/PBCH block.   |
|                  | The SS/PBCK block is used for the UE to detect   |
|                  | the cell, obtain basic information of it on      |
|                  | PBCH, and maintain synchronization to it. The    |
|                  | duration, number and frequency of the SS/PBCH    |
|                  | block transmission depends on the network setup. |
|                  | For the purposes of blind initial access the UE  |
|                  | may assume that there is an SS/PBCH block once   |
|                  | every 20 ms. If the network is configured to     |
|                  | transmit the SS/PBCH block less frequently, that |
|                  | will improve the network energy efficiency at    |
|                  | the cost of increased the initial cell detection |
|                  | time, but after the initial connection has been  |
|                  | established, the UE may be informed of the       |
|                  | configured SS/PBCH block periodicity in the cell |
|                  | from set of {5, 10, 20, 40, 80, 160} ms. If the  |
|                  | cell set up uses analogue beamformer component,  |
|                  | it may provide several SS/PBCH blocks            |
|                  | multiplexed in time-domain fashion within one    |
|                  | SS/PBCH block period.*                           |
|                  |                                                  |
|                  | *Remaining minimum system information carried    |
|                  | over SIB1 needs to be broadcast at least in the  |
|                  | cells in which the UEs are expected to be able   |
|                  | to set up the connection to the network. There   |
|                  | is no specific rate at which the SIB1 needs to   |
|                  | be repeated in the cell, and once the UE         |
|                  | acquires the SIB1, it does not need to read it   |
|                  | again. SIB1 could be time or frequency           |
|                  | multiplexed with the SS/PBCH block. In the       |
|                  | frequency multiplexing case, there would be no   |
|                  | additional on-time for the gNB transmitter. In   |
|                  | the time multiplexing case, having a lower rate  |
|                  | for SIB1 than for SS/PBCH block would suffice at |
|                  | least for higher SS/PBCH repetition              |
|                  | frequencies.*                                    |
|                  |                                                  |
|                  | *The sleep ratio under the above mechanism is    |
|                  | evaluated in TR37.910.*                          |
|                  |                                                  |
|                  | ***[Device energy efficiency]{.underline}***     |
|                  |                                                  |
|                  | *Multiple features facilitating device energy    |
|                  | efficiency have been specified for NR Rel-15.*   |
|                  |                                                  |
|                  | > ***Discontinuous reception (DRX)               |
|                  | > inRRC\_CONNECTED, RRC\_INACTIVE and            |
|                  | > RRC\_IDLE**When DRX is configured, the UE does |
|                  | > not have to continuously monitor PDCCH for     |
|                  | > scheduling or paging messages, but it can      |
|                  | > remain sleeping. DRX is characterized by the   |
|                  | > following:*                                    |
|                  |                                                  |
|                  | -   ***on-duration**: duration that the UE waits |
|                  |     for, after waking up, to receive PDCCHs. If  |
|                  |     the UE successfully decodes a PDCCH, the UE  |
|                  |     stays awake and starts the inactivity        |
|                  |     timer;*                                      |
|                  |                                                  |
|                  | -   ***inactivity-timer**: duration that the UE  |
|                  |     waits to successfully decode a PDCCH, from   |
|                  |     the last successful decoding of a PDCCH,     |
|                  |     failing which it can go back to sleep. The   |
|                  |     UE shall restart the inactivity timer        |
|                  |     following a single successful decoding of a  |
|                  |     PDCCH for a first transmission only (i.e.    |
|                  |     not for retransmissions);*                   |
|                  |                                                  |
|                  | -   ***retransmission-timer**: duration until a  |
|                  |     retransmission can be expected;*             |
|                  |                                                  |
|                  | -   ***DRX cycle**: specifies the periodic       |
|                  |     repetition of the on-duration followed by a  |
|                  |     possible period of inactivity (see figure    |
|                  |     below).*                                     |
|                  |                                                  |
|                  | *Figure: DRX Cycle*                              |
|                  |                                                  |
|                  | > ***Bandwidth part (BWP) adaptation***          |
|                  | >                                                |
|                  | > *With dynamic bandwidth part adaptation, the   |
|                  | > UE can fall-back to monitoring the downlink    |
|                  | > and transmitting the uplink over a narrower    |
|                  | > bandwidth than the nominal carrier bandwidth   |
|                  | > used for high data rate transactions. This     |
|                  | > allows the UEs BB-RF interface to operate with |
|                  | > a much lower clock rate and thus reduce energy |
|                  | > consumption. Lower data rate exchange can      |
|                  | > still take place so that there is no need to   |
|                  | > resume full bandwidth operation just for       |
|                  | > exchanging network signalling messages or      |
|                  | > always-on packets of applications. The UE can  |
|                  | > be moved to the narrow BWP by gNBs             |
|                  | > transmitting a BWP switch bit on the           |
|                  | > scheduling DCI on the PDCCH, or based on an    |
|                  | > inactivity timer. UE can be moved back to the  |
|                  | > full bandwidth operation at any time by the    |
|                  | > gNB with the BWP switch bit.*                  |
|                  | >                                                |
|                  | > ***RRC\_INACTIVE state***                      |
|                  | >                                                |
|                  | > *The introduction of RRC-inactive state to the |
|                  | > RRC state machine allows for the UE to         |
|                  | > maintain RRC connection in an inactive state   |
|                  | > while having the battery saving                |
|                  | > characteristics of the Idle mode. This allows  |
|                  | > for maintaining the RRC connection also when   |
|                  | > the UE is inactive for longer time durations,  |
|                  | > and avoid the signalling overhead and related  |
|                  | > energy consumption needed when the RRC         |
|                  | > connection is re-established from Idle mode.*  |
|                  | >                                                |
|                  | > !                                              |
|                  | [](media/image6.emf){width="2.212538276465442in" |
|                  | > height="2.495206692913386in"}                  |
|                  |                                                  |
|                  | *Figure: NR RRC state machine*                   |
|                  |                                                  |
|                  | > ***Pipelining frame structure enabling         |
|                  | > micro-sleep within slots in which the UE is    |
|                  | > not scheduled***                               |
|                  | >                                                |
|                  | > *The fact that the typical data transmission   |
|                  | > employs a control channel in the beginning of  |
|                  | > the slot, and the absence of the continuous    |
|                  | > reference signal to receive for channel        |
|                  | > estimate maintenance allows for the UE to      |
|                  | > determine early on in the slot whether there   |
|                  | > is a transmission to it, and if there is no    |
|                  | > data for it to decode, it may turn off its     |
|                  | > receiver until the end of the slot.*           |
|                  | >                                                |
|                  | > *Additional power saving mechanisms for NR are |
|                  | > being specified for 3GPP Release 16, including |
|                  | > at least the following techniques:*            |
|                  |                                                  |
|                  | -   *Downlink control channel-based triggering   |
|                  |     of UE adaptation in RRC\_CONNECTED state for |
|                  |     improved energy efficiency.*                 |
|                  |                                                  |
|                  | -   *A procedure of cross-slot scheduling power  |
|                  |     saving allowing the UE to micro-sleep        |
|                  |     between control channel occasions and only   |
|                  |     activating the data channel reception when   |
|                  |     it is scheduled.*                            |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | ***[Network energy efficiency]{.underline}***    |
|                  |                                                  |
|                  | *In LTE system the capacity boosting cells can   |
|                  | be distinguished from cells providing basic      |
|                  | coverage. This can be used to enhance network    |
|                  | energy efficiency by switching off LTE or EN-DC  |
|                  | cells providing additional capacity when its     |
|                  | capacity is not needed, and re-activate the      |
|                  | cells on a need basis.*                          |
|                  |                                                  |
|                  | *The eNB owning a capacity booster cell can      |
|                  | autonomously decide to switch-off such cell to   |
|                  | lower energy consumption (dormant state). The    |
|                  | decision is typically based on cell load         |
|                  | information, consistently with configured        |
|                  | information. The switch-off decision may also be |
|                  | taken by O&M. The eNB may initiate handover      |
|                  | actions in order to off-load the cell being      |
|                  | switched off and may indicate the reason for     |
|                  | handover with an appropriate cause value to      |
|                  | support the target node in taking subsequent     |
|                  | actions, e.g. when selecting the target cell for |
|                  | subsequent handovers. All peer eNBs are informed |
|                  | by the eNB owning the concerned cell about the   |
|                  | switch-off actions over the X2 interface with    |
|                  | the eNB Configuration Update procedure. The eNB  |
|                  | indicates the switch-off action to a GERAN       |
|                  | and/or UTRAN node with the eNB Direct            |
|                  | Information Transfer procedure over S1. All      |
|                  | informed nodes maintain the cell configuration   |
|                  | data, e.g., neighbour relationship               |
|                  | configuration, also when a certain cell is       |
|                  | dormant. If basic coverage is ensured by E-UTRAN |
|                  | cells, eNBs owning non-capacity boosting cells   |
|                  | may request a re-activation over the X2          |
|                  | interface if capacity needs in such cells demand |
|                  | to do so. This is achieved via the Cell          |
|                  | Activation procedure. If basic coverage is       |
|                  | ensured by UTRAN or GERAN cells, the eNB owning  |
|                  | the capacity booster cell may receive a          |
|                  | re-activation request from a GERAN or UTRAN node |
|                  | with the MME Direct Information Transfer         |
|                  | procedure over S1. The eNB owning the capacity   |
|                  | booster cell may also receive from the sending   |
|                  | GERAN or UTRAN node the minimum time before that |
|                  | cell switches off; during this time, the same    |
|                  | eNB may prevent idle mode UEs from camping on    |
|                  | the cell and may prevent incoming handovers to   |
|                  | the same cell.*                                  |
|                  |                                                  |
|                  | ***[Device energy efficiency]{.underline}***     |
|                  |                                                  |
|                  | *Multiple features facilitating device energy    |
|                  | efficiency have been specified for LTE Rel-15.*  |
|                  |                                                  |
|                  | > ***Discontinuous reception (DRX) in RRC        |
|                  | > connected mode***                              |
|                  | >                                                |
|                  | > *When DRX is configured, the UE does not have  |
|                  | > to continuously monitor PDCCH for scheduling   |
|                  | > or paging messages, but it can remain          |
|                  | > sleeping. DRX is characterized by the          |
|                  | > following:*                                    |
|                  |                                                  |
|                  | -   ***on-duration**: duration that the UE waits |
|                  |     for, after waking up, to receive PDCCHs. If  |
|                  |     the UE successfully decodes a PDCCH, the UE  |
|                  |     stays awake and starts the inactivity        |
|                  |     timer;*                                      |
|                  |                                                  |
|                  | -   ***inactivity-timer**: duration that the UE  |
|                  |     waits to successfully decode a PDCCH, from   |
|                  |     the last successful decoding of a PDCCH,     |
|                  |     failing which it can go back to sleep. The   |
|                  |     UE shall restart the inactivity timer        |
|                  |     following a single successful decoding of a  |
|                  |     PDCCH for a first transmission only (i.e.    |
|                  |     not for retransmissions);*                   |
|                  |                                                  |
|                  | -   ***retransmission-timer**: duration until a  |
|                  |     retransmission can be expected;*             |
|                  |                                                  |
|                  | -   ***DRX cycle**: specifies the periodic       |
|                  |     repetition of the on-duration followed by a  |
|                  |     possible period of inactivity (see figure    |
|                  |     11-1 below).*                                |
|                  |                                                  |
|                  | *Figure: DRX Cycle*                              |
|                  |                                                  |
|                  | > ***Discontinuous reception (DRX) in RRC idle   |
|                  | > mode***                                        |
|                  | >                                                |
|                  | > *The UE may use discontinuous reception (DRX)  |
|                  | > to reduce power consumption in idle mode. When |
|                  | > DRX is used, the UE wakes up and listens to    |
|                  | > PDCCH only on specific paging occasion defined |
|                  | > in-terms of paging frame and subframe within   |
|                  | > period of N radio frames defined by the DRX    |
|                  | > cycle of the cell. The UE can remain in sleep  |
|                  | > mode for remaining duration within DRX cycle.* |
|                  | >                                                |
|                  | > *The UE listens to PDCCH on the paging         |
|                  | > occasion and decodes the PDCCH based on P-RNTI |
|                  | > and if the PDCCH decoding is success, UE       |
|                  | > decodes the PDSCH indicated in the PDCCH. The  |
|                  | > UE enters into sleep mode if the PDCCH         |
|                  | > decoding is not successful or if the UE does   |
|                  | > not find any page for its UE-ID in the paging  |
|                  | > message.*                                      |
|                  | >                                                |
|                  | > *The paging occasion of UE within DRX cycle is |
|                  | > determined based on the UE-ID, DRX cycle and   |
|                  | > nB. n is the number of paging occasions per    |
|                  | > DRX cycle. Higher the value of nB indicates    |
|                  | > lesser the paging occasions within DRX cycle   |
|                  | > and vice versa.*                               |
|                  | >                                                |
|                  | > *For higher sleep ratio, higher DRX cycle      |
|                  | > needs to be configured at the cell.*           |
|                  | >                                                |
|                  | > ***Extended Discontinuous reception (DRX) in   |
|                  | > RRC idle mode***                               |
|                  | >                                                |
|                  | > *To support higher sleep duration upto several |
|                  | > hours for low complexity mMTC devices,         |
|                  | > extended DRX functionality can be configured   |
|                  | > in LTE.*                                       |
|                  | >                                                |
|                  | > *When eDRX is configured for UE, the UE wakes  |
|                  | > up periodically in every longer DRX cycle      |
|                  | > defined as eDRX cycle for short duration       |
|                  | > called paging window to monitor the PDCCH for  |
|                  | > reception of paging message. The eDRX cycle    |
|                  | > length is configured in terms of number of     |
|                  | > hyper-frames (1 hyper frame =1024 radio        |
|                  | > frames) by higher layers. Maximum value of     |
|                  | > eDRX cycle is 256 hyper frames for LTE and     |
|                  | > 1024 for NB-IoT devices.*                      |
|                  | >                                                |
|                  | > *During the paging window, the UE monitors the |
|                  | > PDCCH using the DRX cycle configured for the   |
|                  | > cell. The paging window duration will be       |
|                  | > longer than DRX cycle so that UE monitors for  |
|                  | > paging message in more than one paging         |
|                  | > occasion within paging window.(See figure 11-2 |
|                  | > below).*                                       |
|                  | >                                                |
|                  | > *The PTW is UE specific and defined in terms   |
|                  | > of PH (paging hyper frame) and starting and    |
|                  | > end position of the paging window within the   |
|                  | > paging hyper-frame.*                           |
|                  | >                                                |
|                  | > *The paging hyper frame is selected based on   |
|                  | > UE-ID and the extended DRX-cycle value. The    |
|                  | > length of extended DRX-cycle value can be      |
|                  | > configured as multiples of hyper-frame (1024   |
|                  | > radio frames). Maximum eDRX length can be 1024 |
|                  | > hyper frames (approximately) 3hours.*          |
|                  | >                                                |
|                  | > *The paging occasions where UE should monitor  |
|                  | > PDCCH for the UE configured with eDRX is given |
|                  | > in terms of paging window within eDRX cycle.   |
|                  | > The start of paging window is aligned to the   |
|                  | > paging hyper frame calculated based on eDRX    |
|                  | > cycle and UE-ID. Within paging hyper frame,    |
|                  | > the paging window starts at radio frames in    |
|                  | > multiples of 256. The actual starting radio    |
|                  | > frame is determined based on UE-ID. From start |
|                  | > of paging window UE monitors all the paging    |
|                  | > occasions until the end of paging window which |
|                  | > is calculated based paging window length       |
|                  | > configured by upper layers.*                   |
|                  | >                                                |
|                  | > *The UE enters into sleep mode at the end of   |
|                  | > PTW or if it has received a valid page for its |
|                  | > UE ID within PTW whichever happens earlier and |
|                  | > wake up only during next occurrence of PTW in  |
|                  | > next eDRX cycle.*                              |
|                  | >                                                |
|                  | > ***Paging with Wake-Up Signal in idle mode***  |
|                  | >                                                |
|                  | > *When UE supports WUS and the cell is          |
|                  | > configured to support WUS transmission, UE     |
|                  | > shall monitor WUS prior to paging reception on |
|                  | > the PO. If DRX is used and if UE detects WUS   |
|                  | > it reads the PDCCH in the following PO. If     |
|                  | > eDRX is configured and if the UE detects WUS   |
|                  | > within its paging window, it monitors N paging |
|                  | > occasions configured by higher layers. If the  |
|                  | > UE does not detect WUS it need not monitor the |
|                  | > following paging occasions.*                   |
|                  | >                                                |
|                  | > ***Power Saving Mode Operation in idle mode    |
|                  | > (PSM)***                                       |
|                  | >                                                |
|                  | > *The UE may be configured by higher layers to  |
|                  | > enter into indefinite sleep after configurable |
|                  | > timer duration from last successful uplink     |
|                  | > transmission. The UE exit the sleep mode when  |
|                  | > it needs to send next uplink transmission for  |
|                  | > sending tracking area update or for            |
|                  | > application data transmission. The UE is not   |
|                  | > expected to listen to any downlink channels    |
|                  | > including PDCCH for paging when it is in sleep |
|                  | > mode. Any network initiated downlink data      |
|                  | > transmission towards the UE needs to be        |
|                  | > delayed until UE access the network for next   |
|                  | > uplink transmission.*                          |
|                  |                                                  |
|                  | ***For EN-DC operation:***                       |
|                  |                                                  |
|                  | *In EN-DC operation, the en-gNB may autonomously |
|                  | decide to switch-off NR cells to lower energy    |
|                  | consumption. MeNBs are informed by the en-gNB    |
|                  | owning the concerned cell about the switch-off   |
|                  | actions over the X2 interface with the EN-DC     |
|                  | Configuration Update procedure. The en-gNB may   |
|                  | initiate dual connectivity procedures towards    |
|                  | the MeNB in order to off-load the cell being     |
|                  | switched off, and may indicate the reason for    |
|                  | release or modification with an appropriate      |
|                  | cause value to support the master node in taking |
|                  | subsequent actions. The MeNB may request a       |
|                  | re-activation over the X2 interface if capacity  |
|                  | needs demand to do so. This is achieved via the  |
|                  | EN-DC Cell Activation procedure. The switch-on   |
|                  | decision may also be taken by O&M. All peer eNBs |
|                  | are informed by the en-gNB owning the concerned  |
|                  | NR cell about the re-activation by an indication |
|                  | on the X2 interface.*                            |
+------------------+--------------------------------------------------+
| **5.2.3.2.26**   | **Other items**                                  |
+------------------+--------------------------------------------------+
| 5.2.3.2.26.1     | *Coverage extension schemes*                     |
|                  |                                                  |
|                  | Describe the capability to support/ coverage     |
|                  | extension schemes, such as relays or repeaters.  |
|                  |                                                  |
|                  | ***For NR component RIT:***                      |
|                  |                                                  |
|                  | *NR supports the use of the following mechanisms |
|                  | to improve the coverage*                         |
|                  |                                                  |
|                  | -   *NR can use DFT-spreading and Pi/2 BPSK      |
|                  |     > modulation to reduce PAPR and increase     |
|                  |     > average Tx power for better coverage*      |
|                  |                                                  |
|                  | -   *NR can use very low coding rate for better  |
|                  |     > coverage.*                                 |
|                  |                                                  |
|                  | -   *Slot aggregation for both control and data  |
|                  |     > can be used for better coverage*           |
|                  |                                                  |
|                  | -   *High-aggregation level (up to 16) downlink  |
|                  |     > control is possible for better coverage*   |
|                  |                                                  |
|                  | -   *Lower-band supplementary uplink carrier can |
|                  |     > be used with higher band TDD carrier such  |
|                  |     > that coverage limited users can be         |
|                  |     > allocated on SUL carrier to improve the    |
|                  |     > uplink coverage.*                          |
|                  |                                                  |
|                  | -   *Beam management is used to increase the     |
|                  |     > coverage in case of massive MIMO.*         |
|                  |                                                  |
|                  | -   *NR also supports the use of different types |
|                  |     > of repeater (amplify-and-forward)          |
|                  |     > functionality. However, the details of     |
|                  |     > such functionality is outside the scope of |
|                  |     > the specification as the use of repeaters  |
|                  |     > is transparent to both the UE and the      |
|                  |     > network.*                                  |
|                  |                                                  |
|                  | ***For LTE component RIT:***                     |
|                  |                                                  |
|                  | *LTE supports the use of the following           |
|                  | mechanisms to improve the coverage*              |
|                  |                                                  |
|                  | -   *LTE can use DFT-spreading to reduce PAPR    |
|                  |     > and increase average Tx power for better   |
|                  |     > coverage.*                                 |
|                  |                                                  |
|                  | -   *Semi-persistent scheduling can be used for  |
|                  |     > repetition uplink transmission; and        |
|                  |     > HARQ-less repetition can be used for       |
|                  |     > downlink transmission, both are beneficial |
|                  |     > for coverage.*                             |
|                  |                                                  |
|                  | -   *LTE also supports the use of different      |
|                  |     > types of repeater (amplify-and-forward)    |
|                  |     > functionality. However, the details of     |
|                  |     > such functionality is outside the scope of |
|                  |     > the specification as the use of repeaters  |
|                  |     > is transparent to both the UE and the      |
|                  |     > network.*                                  |
|                  |                                                  |
|                  | ***For NB-IoT / eMTC,***                         |
|                  |                                                  |
|                  | -   *DFT-spreading and Pi/2 BPSK and Pi/4 QPSK   |
|                  |     > modulation in NB-IoT for reduced PAPR for  |
|                  |     > better coverage.*                          |
|                  |                                                  |
|                  | -   *Support for single sub-carrier (NB-IoT) and |
|                  |     > sub-PRB (eMTC) uplink transmission to      |
|                  |     > increase connection density in extended    |
|                  |     > coverage*                                  |
|                  |                                                  |
|                  | -   *Repetition of a transmission for both       |
|                  |     > control and data can be used for better    |
|                  |     > coverage.*                                 |
|                  |                                                  |
|                  | *High-aggregation level downlink control is      |
|                  | possible for better coverage.*                   |
+------------------+--------------------------------------------------+
| 5.2.3.2.26.2     | *Self-organisation*                              |
|                  |                                                  |
|                  | Describe any self-organizing aspects that are    |
|                  | enabled by the RIT/SRIT.                         |
|                  |                                                  |
|                  | ***For NR component RIT:***                      |
|                  |                                                  |
|                  | *Support for Self Organizing Networks is an      |
|                  | integrated part of NR. Two use cases that could  |
|                  | benefit from SON have been introduced in the     |
|                  | Release 15 and the work is continuing.*          |
|                  |                                                  |
|                  | *NR currently supports the following             |
|                  | Self-Organizing Network (SON) functions:         |
|                  | (Details are provided in \[38.300\], \[38.413\], |
|                  | \[38.423\], \[38.331\])*                         |
|                  |                                                  |
|                  | *-- Automatic neighbor discovery: the mechanism  |
|                  | allows an gNB to learn information on its        |
|                  | neighbors. The discovery mechanism can utilize   |
|                  | the assistance of the UE (aka ANR funtion        |
|                  | \[38.300, Sec. 15.3.3\]) as well as the exchange |
|                  | of information over the network interfaces       |
|                  | (\[38.423; Sec 8.4.1, 8.4.2, 9.1.3.1, 9.1.3.2,   |
|                  | 9.1.3.4, 9.1.3.5\] as well as the radio resource |
|                  | control information \[38.331; Sec 5.5.2,         |
|                  | 6.3.2\]).*                                       |
|                  |                                                  |
|                  | *-- Xn-C TNL address discovery: the mechanism    |
|                  | allows a gNB to determine the TNL address on its |
|                  | neighbors candidate gNB. The discovery mechanism |
|                  | can utilize of the ANR function (aka ANR funtion |
|                  | \[38.300, Sec. 15.3.4\]) as well as the exchange |
|                  | of information over the network interfaces       |
|                  | (\[38.413; Sec8.8.1, 8.8.2, 9.2.7.1, 9.2.7.2 )*  |
|                  |                                                  |
|                  | ***For LTE component RIT:***                     |
|                  |                                                  |
|                  | *Support for Self Organizing Networks is an      |
|                  | integrated part of LTE. Several use cases that   |
|                  | could benefit from SON have been introduced in   |
|                  | the first release and the work is continuing.*   |
|                  |                                                  |
|                  | *LTE currently supports the following            |
|                  | Self-Organizing Network (SON) functions:*        |
|                  | (*Details are provided in \[36.300\],            |
|                  | \[36.413\], \[36.423\], \[36.314\])*             |
|                  |                                                  |
|                  | *Self-configuration:*                            |
|                  |                                                  |
|                  | *- Dynamic configuration of S1 and X2; the       |
|                  | mechanism allows an eNB to establish an S1       |
|                  | interface towards the MME and/or an X2 interface |
|                  | towards another eNB.(\[36.423, Sec8.3.3, 8.3.5\] |
|                  | \[36.413, Sec8.7.3, 8.7.4, 8.7.5\])*             |
|                  |                                                  |
|                  | *-- PCI selection**;** the mechanism allows an   |
|                  | eNB to select its Physical Cell Identity (PCI).  |
|                  | The selection can be based either on a           |
|                  | centralized or distributed PCI assignment        |
|                  | algorithm \[36.300, Sec 22.3.5\]*                |
|                  |                                                  |
|                  | *-- Automatic neighbor discovery: the mechanism  |
|                  | allows an eNB to learn information on its        |
|                  | neighbors. The discovery mechanism can utilize   |
|                  | the assistance of the UE (aka ANR funtion        |
|                  | \[36.300, Sec. 22.3.3, 22.3.3\]) as well as the  |
|                  | exchange of information over the network         |
|                  | interfaces (\[36.423; Sec 8.3.3, 8.3.5\] as well |
|                  | as the radio resource control                    |
|                  | information\[36.300; Sec 5.5.2, 5.5.3, 5.5.4,    |
|                  | 5.5.5, 6.3.5\]).*                                |
|                  |                                                  |
|                  | *-- TNL address discovery: the mechanism allows  |
|                  | an eNB to determine the TNL address of the       |
|                  | neighbor candidate eNB. The discovery mechanism  |
|                  | can utilize of the ANR function(aka ANR funtion  |
|                  | \[36.300, Sec. 22.3.6\]) as well as the exchange |
|                  | of information over the network interfaces       |
|                  | (\[38.413; Sec8.15, 8.16, 9.1.16, 9.1.17 )*      |
|                  |                                                  |
|                  | *Self-optimisation:*                             |
|                  |                                                  |
|                  | *-- Mobility load balancing: the mechanism       |
|                  | allows an eNB* *to distribute cell load evenly   |
|                  | among cells or to transfer part of the traffic   |
|                  | from congested cells. (\[36.300, Sec 22.4.1\]    |
|                  | \[36.423, 8.3.6, 8.3.7,8.3.8\])*                 |
|                  |                                                  |
|                  | *-- Mobility Robustness optimization: the        |
|                  | mechanism is to detect radio link connection     |
|                  | failure that occurs due to Too Early or Too Late |
|                  | Handovers, or Handover to Wrong cell. (\[36.300, |
|                  | Sec 22.4.2\] \[36.423, Sec 8.3.9, 8.3.10\]       |
|                  | \[36.331, Sec 5.3.11\])*                         |
|                  |                                                  |
|                  | *-- RACH optimization: the mechanism is          |
|                  | supported by UE reported information and by      |
|                  | PRACH parameters exchange between eNBs to        |
|                  | optimize some RACH configurations. (\[36.300,    |
|                  | Sec 22.4.3\] \[36.423, Sec 8.3.3, 8.3.5\]        |
|                  | \[36.331, Sec 5.6.5.3\]).*                       |
|                  |                                                  |
|                  | *-- Energy Saving: the mechanism is to reduce    |
|                  | operational expenses through energy savings      |
|                  | (\[36.300, Sec 22.4.4\]).*                       |
+------------------+--------------------------------------------------+
| 5.2.3.2.26.3     | Describe the frequency reuse schemes (including  |
|                  | reuse factor and pattern) for the assessment of  |
|                  | average spectral efficiency and 5th percentile   |
|                  | user spectral efficiency.                        |
|                  |                                                  |
|                  | *Uncoordinated frequency reuse one is used in    |
|                  | the performance evaluations.*                    |
+------------------+--------------------------------------------------+
| 5.2.3.2.26.4     | Is the RIT/component RIT an evolution of an      |
|                  | existing IMT technology? Provide the detail.     |
|                  |                                                  |
|                  | ***For NR component RIT:***                      |
|                  |                                                  |
|                  | *This RIT is new radio developed by 3GPP, and    |
|                  | will be evolved to be a 3GPP release of NR.*     |
|                  |                                                  |
|                  | ***For LTE component RIT:***                     |
|                  |                                                  |
|                  | *This RIT is part of a 3GPP release of LTE. It   |
|                  | is an evolution and enhancement of previous LTE  |
|                  | releases that are already part of the            |
|                  | IMT-Advanced technologies, see ITU-R             |
|                  | Recommendation M.2012.*                          |
+------------------+--------------------------------------------------+
| 5.2.3.2.26.5     | Does the proposal satisfy a specific spectrum    |
|                  | mask? Provide the detail. (This information is   |
|                  | not intended to be used for sharing studies.)    |
|                  |                                                  |
|                  | ***For NR component RIT:***                      |
|                  |                                                  |
|                  | *Yes.*                                           |
|                  |                                                  |
|                  | *UE:*                                            |
|                  |                                                  |
|                  | *For Frequency Range 1 (FR1) UE:*                |
|                  |                                                  |
|                  | *For single-component-carrier transmission the   |
|                  | spectrum mask is specified in terms of a         |
|                  | normative (general) spectrum emission mask       |
|                  | \[38.101-1, section 6.5.2.2\] and an additional  |
|                  | spectrum mask \[38.101-1, section 6.5.2.3\].     |
|                  | This additional spectrum emission mask which is  |
|                  | signaled by the network to the UE as a normative |
|                  | requirement can be used to address a specific    |
|                  | regional regulatory requirement, a frequency     |
|                  | band specific requirement, a roaming requirement |
|                  | and a specific deployment  scenario.*            |
|                  |                                                  |
|                  | * This additional spectrum emission mask can be  |
|                  | used to support the many different sharing       |
|                  | requirements in terms of co-existence for a      |
|                  | global roaming terminal.*                        |
|                  |                                                  |
|                  | *For transmission of intra-band Carrier          |
|                  | Aggregation appropriate spectrum mask are        |
|                  | expected to be set.*                             |
|                  |                                                  |
|                  | *For Frequency Range 2 (FR2) UE:*                |
|                  |                                                  |
|                  | *For single-component-carrier transmission the   |
|                  | spectrum mask is specified in terms of a         |
|                  | normative (general) spectrum emission mask       |
|                  | \[38.101-2, section 6.5.2.1\]. The additional    |
|                  | spectrum emissions mask is to be set.*           |
|                  |                                                  |
|                  | *For transmission of Carrier Aggregation         |
|                  | appropriate spectrum mask requirements are       |
|                  | defined in \[38.101-2, section 6.5A.2.1\] .*     |
|                  |                                                  |
|                  | *BS:*                                            |
|                  |                                                  |
|                  | *For single-component-carrier transmission and   |
|                  | transmission of aggregated component-carriers    |
|                  | the radiated spectrum mask requirements are      |
|                  | defined in \[38.104\], section 6.6.4. in form of |
|                  | OTA* *out-of-band emissions     limits. The      |
|                  | unwanted emission limits in the part of the      |
|                  | downlink operating band that falls in the        |
|                  | spurious domain are consistent with ITU-R        |
|                  | Recommendation SM.329.*                          |
|                  |                                                  |
|                  | *For single-component-carrier transmission and   |
|                  | transmission of aggregated component-carriers    |
|                  | the conducted spectrum mask requirements are     |
|                  | defined in \[38.104\], section 9.7.4.2 for for   |
|                  | BS type 1-O and section 9.7.4.3 for BS type 2-O. |
|                  | in form of OTA out-of-band emissions.*           |
|                  |                                                  |
|                  | ***For LTE component RIT:***                     |
|                  |                                                  |
|                  | *Yes.*                                           |
|                  |                                                  |
|                  | *UE:*                                            |
|                  |                                                  |
|                  | *For single-component-carrier transmission the   |
|                  | spectrum mask is specified in terms of a         |
|                  | normative (general) spectrum emission mask       |
|                  | \[36.101, section 6.6.2.1\] and an additional    |
|                  | spectrum mask \[36.101, section 6.6.2.2\]. This  |
|                  | additional spectrum emission mask which is       |
|                  | signaled by the network to the UE as a normative |
|                  | requirement can be used to address a specific    |
|                  | regional regulatory requirement, a frequency     |
|                  | band specific requirement, a roaming requirement |
|                  | and a specific deployment scenario.*             |
|                  |                                                  |
|                  | *This additional spectrum emission mask can be   |
|                  | used to support the many different sharing       |
|                  | requirements in terms of co-existence for a      |
|                  | global roaming terminal.*                        |
|                  |                                                  |
|                  | *For transmission of aggregated                  |
|                  | component-carriers appropriate spectrum mask     |
|                  | requirements are defined in \[36.101, section    |
|                  | 6.6.2.1A\].*                                     |
|                  |                                                  |
|                  | *BS:*                                            |
|                  |                                                  |
|                  | *For single-component-carrier transmission and   |
|                  | transmission of aggregated component-carriers,   |
|                  | spectrum mask requirements are defined in        |
|                  | \[36.104\], section 6.6.3. in form of operating  |
|                  | band unwanted emission limits. These Operating   |
|                  | band unwanted emission limits are defined from   |
|                  | 10 MHz below the lowest frequency of the         |
|                  | downlink operating band up to 10 MHz above the   |
|                  | highest frequency of the downlink operating      |
|                  | band. The unwanted emission limits in the part   |
|                  | of the downlink operating band that falls in the |
|                  | spurious domain are consistent with ITU-R        |
|                  | Recommendation SM.329.*                          |
+------------------+--------------------------------------------------+
| 5.2.3.2.26.6     | Describe any UE power saving mechanisms used in  |
|                  | the RIT/SRIT.                                    |
|                  |                                                  |
|                  | ***For NR component RIT:***                      |
|                  |                                                  |
|                  | *Multiple features facilitating device power     |
|                  | saving have been specified for NR Rel-15,        |
|                  | including Discontinuous reception (DRX)          |
|                  | inRRC\_CONNECTED, RRC\_INACTIVE and RRC\_IDLE,   |
|                  | Bandwidth part (BWP) adaptation, RRC\_INACTIVE   |
|                  | state, and Pipelining frame structure enabling   |
|                  | micro-sleep within slots in which the UE is not  |
|                  | scheduled. Details can be found in item          |
|                  | 5.2.3.2.25.*                                     |
|                  |                                                  |
|                  | ***For LTE component RIT:***                     |
|                  |                                                  |
|                  | *Multiple features facilitating device energy    |
|                  | efficiency have been specified for LTE Rel-15,   |
|                  | including Discontinuous reception (DRX) in RRC   |
|                  | connected mode and RRC idle mode, Extended       |
|                  | Discontinuous reception (DRX) in RRC idle mode,  |
|                  | Paging with Wake-Up Signal in idle mode, and     |
|                  | Power Saving Mode (PSM) operation in idle mode.  |
|                  | Details can be found in item 5.2.3.2.25.*        |
+------------------+--------------------------------------------------+
| 5.2.3.2.26.7     | *Simulation process issues*                      |
|                  |                                                  |
|                  | Describe the methodology used in the analytical  |
|                  | approach.                                        |
|                  |                                                  |
|                  | Proponent should provide information on the      |
|                  | width of confidence intervals of user and system |
|                  | performance metrics of corresponding mean        |
|                  | values, and evaluation groups are encouraged to  |
|                  | provide this information as requested in § 7.1   |
|                  | of Report ITU-R M.2412-0.                        |
|                  |                                                  |
|                  | *As described in Section 7.1 of M.2412, system   |
|                  | simulations are iterated over M independent      |
|                  | 'drops' of user locations. Statistics, mean and  |
|                  | 5th percentiles, are calculated over all drops,  |
|                  | and confidence intervals are estimated by        |
|                  | comparing the results of the different drops.    |
|                  | The number of drops is up to each evaluator.*    |
+------------------+--------------------------------------------------+
| 5.2.3.2.26.8     | *Operational life time*                          |
|                  |                                                  |
|                  | Describe the mechanisms to provide long          |
|                  | operational life time for devices without        |
|                  | recharge for at least massive machine type       |
|                  | communications                                   |
|                  |                                                  |
|                  | ***[For NR and LTE component                     |
|                  | RIT:]{.underline}***                             |
|                  |                                                  |
|                  | *NR and LTE, including NB-IoT, support the       |
|                  | following set of common features for providing   |
|                  | long battery life:*                              |
|                  |                                                  |
|                  | > -            *A configurable transmission and  |
|                  | > reception bandwidth for limiting the device    |
|                  | > modem power consumption.*                      |
|                  | >                                                |
|                  | > -            *DFT-spread OFDM modulation for   |
|                  | > limiting the peak to average ratio of the      |
|                  | > uplink waveform and increasing the device      |
|                  | > power amplifier efficiency.*                   |
|                  | >                                                |
|                  | > -            *Uplink power control which       |
|                  | > allows the device to adapt its transmit power  |
|                  | > to the actual radio environment.*              |
|                  | >                                                |
|                  | > -            *Connected mode DRX cycles for    |
|                  | > reducing the device power consumption while in |
|                  | > RRC Active state.*                             |
|                  | >                                                |
|                  | > -            *Measurement rules for reducing   |
|                  | > the RRC idle mode RRM activities.*             |
|                  | >                                                |
|                  | > -            *Resumption of a previous         |
|                  | > connection for minimizing the control          |
|                  | > signalling when initiating a mobile originated |
|                  | > or terminated data transmission.*              |
|                  |                                                  |
|                  | * *                                              |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | > *LTE, including NB-IoT, in addition supports:* |
|                  | >                                                |
|                  | > -            *Power Save Mode which allows a   |
|                  | > UE to power down and suspend idle mode         |
|                  | > activities.*                                   |
|                  | >                                                |
|                  | > -            *Extended DRX which reduces the   |
|                  | > monitoring of the paging channel.*             |
|                  | >                                                |
|                  | > -            *Relaxed idle mode RRM monitoring |
|                  | > of serving and neighbour cells.*               |
|                  | >                                                |
|                  | > -            *Release Assistance Indication    |
|                  | > which allows the UE to indicate to the network |
|                  | > that its data buffer is empty, and is ready to |
|                  | > release its connection.*                       |
|                  | >                                                |
|                  | > -            *Quick RRC release, only          |
|                  | > requiring a HARQ Acknowledgment of the RRC     |
|                  | > Release message.*                              |
|                  | >                                                |
|                  | > -            *Wake-up signal, allows the UE to |
|                  | > monitor paging only if this shorter signal is  |
|                  | > detected before the paging occasion.           |
|                  | > Optionally the UE can use a simplified         |
|                  | > receiver for the detection of of wake-up       |
|                  | > signal which further decreases the energy      |
|                  | > consumption.*                                  |
|                  | >                                                |
|                  | > -            *In addition, all mechanisms      |
|                  | > reducing the latency for small packet data     |
|                  | > transmission (item 5.2.3.2.26.9) will reduce   |
|                  | > the overall transmission and reception time    |
|                  | > and are beneficial for the operational life    |
|                  | > time.*                                         |
+------------------+--------------------------------------------------+
| 5.2.3.2.26.9     | *Latency for infrequent small packet*            |
|                  |                                                  |
|                  | Describe the mechanisms to reduce the latency    |
|                  | for infrequent small packet, which is, in a      |
|                  | transfer of infrequent application layer small   |
|                  | packets/messages, the time it takes to           |
|                  | successfully deliver an application layer        |
|                  | packet/message from the radio protocol layer 2/3 |
|                  | SDU ingress point at the UE to the radio         |
|                  | protocol layer 2/3 SDU egress point in the base  |
|                  | station, when the UE starts from its most        |
|                  | \"battery efficient\" state.                     |
|                  |                                                  |
|                  | ***[For NR and LTE component                     |
|                  | RIT:]{.underline}***                             |
|                  |                                                  |
|                  | *NR and LTE, including NB-IoT, support the       |
|                  | following set of common features for providing   |
|                  | low latency when waking up from its most         |
|                  | "battery efficient" state:*                      |
|                  |                                                  |
|                  | > -     *Resumption of a previous connection for |
|                  | > minimizing the control signalling, and the     |
|                  | > connection setup latency, when initiating a    |
|                  | > mobile originated or mobile terminated data    |
|                  | > transmission.*.                                |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | > *LTE, including NB-IoT, in addition supports:* |
|                  | >                                                |
|                  | > -            *CIoT CP-optimization, i.e. data  |
|                  | > over NAS,  and CIot UP-optimization,           |
|                  | > resumption of a previously suspended RRC       |
|                  | > connection, reducing the signalling exchange   |
|                  | > per data transmission.*                        |
|                  | >                                                |
|                  | > -            *Physical synchronization signals |
|                  | > designed to support efficient time and         |
|                  | > frequency synchronization over a large         |
|                  | > coupling loss interval.*                       |
|                  | >                                                |
|                  | > -            *The Master Information Block     |
|                  | > system information change and access barring   |
|                  | > signalling which allows a UE to verify the     |
|                  | > system information and access barring status   |
|                  | > already upon acquiring the Physical Broadcast  |
|                  | > Channel.*                                      |
|                  | >                                                |
|                  | > -            *The Early Data Transmission      |
|                  | > feature for which Mobile Originated data       |
|                  | > transmission is initiated already in the       |
|                  | > second uplink transmission. Early Data         |
|                  | > Transmission supports data transmission both   |
|                  | > over the User plane and Control plane.*        |
+------------------+--------------------------------------------------+
| 5.2.3.2.26.10    | *Control plane latency*                          |
|                  |                                                  |
|                  | Provide additional information whether the       |
|                  | RIT/SRIT can support a lower control plane       |
|                  | latency (refer to § 4.7.2 in Report ITU-R        |
|                  | M.2410-0).                                       |
|                  |                                                  |
|                  | *As described in the control plane latency       |
|                  | evaluation in TR37.910, if, in control plane     |
|                  | procedure, the latency of step 7 and step 9 can  |
|                  | be further reduced, the 10ms target as           |
|                  | encouraged by ITU-R can be achieved in some      |
|                  | cases.*                                          |
+------------------+--------------------------------------------------+
| 5.2.3.2.26.11    | *Reliability*                                    |
|                  |                                                  |
|                  | **Provide additional information whether the     |
|                  | RIT/RSIT can support reliability for larger      |
|                  | packet sizes (refer to** § **4.10 in Report      |
|                  | ITU-R M.2410-0).**                               |
|                  |                                                  |
|                  | ***[For NR component RIT:]{.underline}***        |
|                  |                                                  |
|                  | *Based on evaluation results \[R1-1907401\], NR  |
|                  | supports 32 Bytes packets transmission with      |
|                  | reliability 99.999% within 1ms one-way latency   |
|                  | in accordance with ITU-R requirements. NR, in    |
|                  | addition, supports:*                             |
|                  |                                                  |
|                  | -   *Reliability higher than 99.999% with packet |
|                  |     duplication over two radio links (PDCP       |
|                  |     duplication).*                               |
|                  |                                                  |
|                  | -   *Reliability of 99.999% within 1 ms one-way  |
|                  |     latency for larger packets (200 bytes) can   |
|                  |     be achieved \[TR 38.824, Rel-15 enabled use  |
|                  |     case\].*                                     |
|                  |                                                  |
|                  | -   *Reliability equal or higher than 99.999%    |
|                  |     for packets larger than 32Bytes within more  |
|                  |     than 1 ms one-way latency \[TR 38.824\].*    |
|                  |                                                  |
|                  | ***[For LTE component RIT:]{.underline}***       |
|                  |                                                  |
|                  | *Based on evaluation results \[R1-1809276\], LTE |
|                  | supports 32 Bytes packets transmission with      |
|                  | reliability 99.999% within 1 ms one-way latency  |
|                  | in accordance with ITU-R requirements.*          |
+------------------+--------------------------------------------------+
| 5.2.3.2.26.12    | *Mobility*                                       |
|                  |                                                  |
|                  | Provide additional information for the downlink  |
|                  | mobility performance of the RIT/SRIT (refer to § |
|                  | 4.11 in Report ITU-R M.2410-0).                  |
|                  |                                                  |
|                  | ***For NR component RIT:***                      |
|                  |                                                  |
|                  | *The downlink mobility performance for NR has    |
|                  | also been evaluated in e.g. \[R1-1809265\] and   |
|                  | it can be concluded that the NR downlink also    |
|                  | fulfils the same KPIs.*                          |
|                  |                                                  |
|                  | * *                                              |
|                  |                                                  |
|                  | ***For LTE component RIT:***                     |
|                  |                                                  |
|                  | *The downlink mobility performance for LTE has   |
|                  | also been evaluated in e.g. \[R1-1809264\] and   |
|                  | it is shown that the LTE downlink also fulfils   |
|                  | the same KPIs.*                                  |
+------------------+--------------------------------------------------+
| **5.2.3.2.27**   | **Other information**                            |
|                  |                                                  |
|                  | Please provide any additional information that   |
|                  | the proponent believes may be useful to the      |
|                  | evaluation process.                              |
|                  |                                                  |
|                  | *None.*                                          |
+------------------+--------------------------------------------------+

**Reference**

\[22.261\] TS22.261v16.7.0 "Service requirements for next generation new
services and markets"

\[36.101\] TS36.101v16.1.0 "Evolved Universal Terrestrial Radio Access
(E-UTRA); User Equipment (UE) radio transmission and reception"

\[36.133\] TS36.133v16.1.0 "Evolved Universal Terrestrial Radio Access
(E-UTRA); Requirements for support of radio resource management"

\[36.201\] TS36.201v15.2.0 "Evolved Universal Terrestrial Radio Access
(E-UTRA); LTE physical layer; General description"

\[36.211\] TS36.211v15.5.0 "Evolved Universal Terrestrial Radio Access
(E-UTRA); Physical channels and modulation"

\[36.212\] TS36.212v15.5.0 "Evolved Universal Terrestrial Radio Access
(E-UTRA); Multiplexing and channel coding"

\[36.213\] TS36.213v15.5.0 "Evolved Universal Terrestrial Radio Access
(E-UTRA); Physical layer procedures"

\[36.300\] TS36.300v15.5.0 "Evolved Universal Terrestrial Radio Access
(E-UTRA) and Evolved Universal Terrestrial Radio Access Network
(E-UTRAN); Overall description; Stage 2"

\[36.304\] TS36.304v15.3.0 "Evolved Universal Terrestrial Radio Access
(E-UTRA); User Equipment (UE) procedures in idle mode"

\[36.321\] TS36.321v15.5.0 "Evolved Universal Terrestrial Radio Access
(E-UTRA); Medium Access Control (MAC) protocol specification"

\[36.322\] TS36.322v15.1.0 "Evolved Universal Terrestrial Radio Access
(E-UTRA); Radio Link Control (RLC) protocol specification"

\[36.401\] TS36.401v15.1.0 "Evolved Universal Terrestrial Radio Access
Network (E-UTRAN); Architecture description"

\[37.340\] TS37.340v15.5.0 "NR; Multi-connectivity; Overall description;
Stage-2"

\[38.101\] TS38.101v15.5.0 "NR; User Equipment (UE) radio transmission
and reception"

\[38.133\] TS38.133v15.5.0 "NR; Requirements for support of radio
resource management"

\[38.201\] TS38.201v15.0.0 "NR; Physical layer; General description"

\[38.211\] TS38.211v15.5.0 "NR; Physical channels and modulation"

\[38.212\] TS38.212v15.5.0 "NR; Multiplexing and channel coding"

\[38.213\] TS38.213v15.5.0 "NR; Physical layer procedures for control"

\[38.214\] TS38.214v15.5.0 "NR; Physical layer procedures for data"

\[38.215\] TS38.215v15.4.0 "NR; Physical layer measurements"

\[38.300\] TS38.300v15.5.0 "NR; Overall description; Stage-2"

\[38.304\] TS38.304v15.3.0 "NR; User Equipment (UE) procedures in idle
mode"

\[38.321\] TS38.321v15.5.0 "NR; Medium Access Control (MAC) protocol
specification"

\[38.322\] TS38.322v15.5.0 "NR; Radio Link Control (RLC) protocol
specification"

\[38.401\] TS38.401v15.5.0 "NG-RAN; Architecture description"

\_\_\_\_\_\_\_\_\_\_\_\_\_\_

[^1]: Developed by 3GPP as 5G, Release 15 and beyond.

[^2]: 'eMTC' is the term used in 3GPP, and refers to LTE MTC
    enhancements introduced from Rel-13 onward. Other terms may be used
    elsewhere, e.g. 'LTE-M'.

[^3]: 'eMTC' is the term used in 3GPP, and refers to LTE MTC
    enhancements introduced from Rel-13 onward. Other terms may be used
    elsewhere, e.g. 'LTE-M'.
