Characteristics template for 3GPP 5G NR RIT (Release 15 and beyond)
-------------------------------------------------------------------

The description templates provided by 3GPP are for the description of
the characteristics of 5G[^1] developed by 3GPP. It includes one
characteristics template for SRIT (encompassing NR and LTE), and one
characteristics template for NR RIT.

This document provides the characteristics template for the description
of the characteristics of the NR RIT based on 3GPP Rel-15 and Rel-16
work.

For this characteristics template, 3GPP has addressed all of the
characteristics, and it is expected that these descriptions are helpful
to assist in evaluation activities for independent evaluation groups, as
well as to facilitate the understanding of the state-of-art of 3GPP
development on the RIT.

+------------------+--------------------------------------------------+
| Item             | Item to be described                             |
+==================+==================================================+
| **5.2.3.2.1**    | **Test environment(s)**                          |
+------------------+--------------------------------------------------+
| 5.2.3.2.1.1      | What test environments (described in Report      |
|                  | ITU-R M.2412-0) does this technology description |
|                  | template address?                                |
|                  |                                                  |
|                  | *This proposal targets to addresses all the five |
|                  | test environments across the three usage         |
|                  | scenarios (eMBB, mMTC, and URLLC) as described   |
|                  | in Report ITU-R M.2412-0.*                       |
+------------------+--------------------------------------------------+
| **5.2.3.2.2**    | **Radio interface functional aspects**           |
+------------------+--------------------------------------------------+
| 5.2.3.2.2.1      | *Multiple access schemes*                        |
|                  |                                                  |
|                  | Which access scheme(s) does the proposal use?    |
|                  | Describe in detail the multiple access schemes   |
|                  | employed with their main parameters.             |
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
|                  | π/2 BPSK DFT-S-OFDM for above 24 GHz. Any        |
|                  | PAPR-reduction algorithm is                      |
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
|                  | *Decoding mechanism is receiver-implementation   |
|                  | specific. Example of information on the decoding |
|                  | mechanism will be provided together with self    |
|                  | evaluation.*                                     |
+------------------+--------------------------------------------------+
| 5.2.3.2.2.3.2    | Describe the bit interleaving scheme for both    |
|                  | uplink and downlink.                             |
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
+------------------+--------------------------------------------------+
| **5.2.3.2.3**    | **Describe channel tracking capabilities         |
|                  | (e.g. channel tracking algorithm, pilot symbol   |
|                  | configuration, etc.) to accommodate rapidly      |
|                  | changing delay spread profile.**                 |
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
|                  |     transmitted periodically aperiodically, and  |
|                  |     semi-persistently by the UE on a gNB         |
|                  |     configurable rate.*                          |
|                  |                                                  |
|                  | *Details of channel-tracking/estimation          |
|                  | algorithms are receiver-implementation specific, |
|                  | and not part of the specification.*              |
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
+------------------+--------------------------------------------------+
| 5.2.3.2.4.2      | *Layer 1 and Layer 2 overhead estimation.*       |
|                  |                                                  |
|                  | Describe how the RIT/SRIT accounts for all layer |
|                  | 1 (PHY) and layer 2 (MAC) overhead and provide   |
|                  | an accurate estimate that includes static and    |
|                  | dynamic overheads.                               |
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
+------------------+--------------------------------------------------+
| 5.2.3.2.4.3      | *Variable bit rate capabilities:*                |
|                  |                                                  |
|                  | Describe how the proposal supports different     |
|                  | applications and services with various bit rate  |
|                  | requirements.                                    |
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
|                  | *The transport-block size can vary between X     |
|                  | bits and Y bits. The number of bits per          |
|                  | transport block can be set with a fine           |
|                  | granularity.*                                    |
|                  |                                                  |
|                  | *See \[38.214\] sub-clause 5.1.3.2 for details.* |
+------------------+--------------------------------------------------+
| 5.2.3.2.4.5      | *Signalling transmission scheme:*                |
|                  |                                                  |
|                  | Describe how transmission schemes are different  |
|                  | for signalling/control from that of user data.   |
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
|                  | -   *NG-RAN: NG Radio Access Network ( connected |
|                  |     to 5GC)*                                     |
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
|                  | sub-clauses 9.2.3 & 9.3.*                        |
+------------------+--------------------------------------------------+
| 5.2.3.2.5.2      | Describe the handover mechanisms and procedures  |
|                  | to meet the simultaneous handover requirements   |
|                  | of a large number of users in high speed         |
|                  | scenarios (up to 500km/h moving speed) with high |
|                  | handover success rate.                           |
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
|                  | *[General\                                       |
|                  | ]{.underline}NR performs radio resource          |
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
|                  | *NR supports dynamic and flexible radio resource |
|                  | management by packet scheduling that allocates   |
|                  | and de-allocates resources to user and control   |
|                  | plane packets.*                                  |
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
|                  | *For more details, refer to \[38.300\].*         |
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
|                  | *The frame structure related information is as   |
|                  | follows:*                                        |
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
|                  | the partial slot transmissions that occur        |
|                  | several times within one slot. The supported     |
|                  | partial slot allocations and scheduling          |
|                  | intervals are 2, 4 and 7 symbols for DL and 1-14 |
|                  | symbols for UL for normal cyclic prefix, and 2,  |
|                  | 4 and 6 symbols for DL and 1-12 symbols for UL   |
|                  | for extended cyclic prefix.*                     |
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
+------------------+--------------------------------------------------+
| 5.2.3.2.8.3      | What are the frequency bands supported by the    |
|                  | RIT/SRIT? Please list.                           |
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
+------------------+--------------------------------------------------+
| 5.2.3.2.8.4      | What is the minimum amount of spectrum required  |
|                  | to deploy a contiguous network, including        |
|                  | guardbands (MHz)?                                |
|                  |                                                  |
|                  | *The minimum amount of paired spectrum is 2 x 5  |
|                  | MHz. The minimum amount of unpaired spectrum is  |
|                  | 5 MHz.*                                          |
+------------------+--------------------------------------------------+
| 5.2.3.2.8.5      | What are the minimum and maximum transmission    |
|                  | bandwidth (MHz) measured at the 3 dB down        |
|                  | points?                                          |
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
|                  |     and analog beamforming is supported. Beam    |
|                  |     management with periodic and aperiodic beam  |
|                  |     refinement is also supported at the UE and   |
|                  |     at the base station.*                        |
+------------------+--------------------------------------------------+
| 5.2.3.2.9.2      | How many antenna elements are supported by the   |
|                  | base station and UE for transmission and         |
|                  | reception? What is the antenna spacing (in       |
|                  | wavelengths)?                                    |
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
|                  | antennas is supported by NR.*                    |
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
+------------------+--------------------------------------------------+
| **5.2.3.2.11**   | **Power classes**                                |
+------------------+--------------------------------------------------+
| 5.2.3.2.11.1     | *UE emitted power*                               |
+------------------+--------------------------------------------------+
| 5.2.3.2.11.1.1   | What is the radiated antenna power measured at   |
|                  | the antenna (dBm)?                               |
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
+------------------+--------------------------------------------------+
| 5.2.3.2.11.2     | *Base station emitted power*                     |
+------------------+--------------------------------------------------+
| 5.2.3.2.11.2.1   | What is the base station transmit power per RF   |
|                  | carrier?                                         |
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
|                  | ***[RAN/Radio Architectures:]{.underline}***     |
|                  |                                                  |
|                  | *This RIT contains NR standalone architecture.*  |
|                  |                                                  |
|                  | *The following paragraphs provide a high level   |
|                  | summary of radio interface protocols and         |
|                  | channels.*                                       |
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
+------------------+--------------------------------------------------+
| 5.2.3.2.13.2     | What is the bit rate required for transmitting   |
|                  | feedback information?                            |
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
|                  | *For more details, refer to:\[38.300\],          |
|                  | \[38.321\] and \[38.213\]*                       |
+------------------+--------------------------------------------------+
| **5.2.3.2.14**   | **Cell selection**                               |
+------------------+--------------------------------------------------+
| 5.2.3.2.14.1     | Describe in detail how the RIT/SRIT accomplishes |
|                  | cell selection to determine the serving cell for |
|                  | the users.                                       |
|                  |                                                  |
|                  | *Cell selection is based on the following        |
|                  | principles:*                                     |
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
|                  | *For more details, refer to:\[38.300\]           |
|                  | sub-clause 9.2.1.1 and \[38.304\] sub-clause     |
|                  | 5.2*                                             |
+------------------+--------------------------------------------------+
| **5.2.3.2.15**   | **Location determination mechanisms**            |
+------------------+--------------------------------------------------+
| 5.2.3.2.15.1     | Describe any location determination mechanisms   |
|                  | that may be used, e.g., to support location      |
|                  | based services.                                  |
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
+------------------+--------------------------------------------------+
| **5.2.3.2.16**   | **Priority access mechanisms**                   |
+------------------+--------------------------------------------------+
| 5.2.3.2.16.1     | Describe techniques employed to support          |
|                  | prioritization of access to radio or network     |
|                  | resources for specific services or specific      |
|                  | users (e.g., to allow access by emergency        |
|                  | services).                                       |
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
|                  | *The RIT supports mostly unicast transmission of |
|                  | data to/from users.\                             |
|                  | Broadcast capabilities pertain to support and    |
|                  | transmission of cell-wide system                 |
|                  | information/parameters, as well as               |
|                  | broacast/based emergency services (e.g. public   |
|                  | warning messages).*                              |
+------------------+--------------------------------------------------+
| 5.2.3.2.17.2     | Describe whether the proposal is capable of      |
|                  | providing multiple user services simultaneously  |
|                  | to any user with appropriate channel capacity    |
|                  | assignments?                                     |
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
|                  | capabilities of the serviced interface.*         |
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
+------------------+--------------------------------------------------+
| **5.2.3.2.20**   | **Interference mitigation within radio           |
|                  | interface**                                      |
+------------------+--------------------------------------------------+
| 5.2.3.2.20.1     | Does the proposal support Interference           |
|                  | mitigation? If so, describe the corresponding    |
|                  | mechanism.                                       |
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
+------------------+--------------------------------------------------+
| 5.2.3.2.20.2     | What is the signalling, if any, which can be     |
|                  | used for intercell interference mitigation?      |
|                  |                                                  |
|                  | *[To support handling of Cross Link Interference |
|                  | (CLI) and for Remote Interference Management     |
|                  | (RIM), NR will support inter-base station        |
|                  | signalling via the Xn interface and the core     |
|                  | network. This is further described in TR         |
|                  | 38.866.]{.underline}*                            |
+------------------+--------------------------------------------------+
| 5.2.3.2.20.3     | *Link level interference mitigation*             |
|                  |                                                  |
|                  | Describe the feature or features used to         |
|                  | mitigate intersymbol interference.               |
|                  |                                                  |
|                  | *Time and frequency synchronization to the DL    |
|                  | and UL frame structures in combination with the  |
|                  | use of a cyclic prefix OFDM transmission in both |
|                  | UL(with or without transform precoding) and DL,  |
|                  | provides robustness against intersymbol          |
|                  | interference.*                                   |
|                  |                                                  |
|                  | ***See also answer to 5.2.3.2.20.4***            |
+------------------+--------------------------------------------------+
| 5.2.3.2.20.4     | Describe the approach taken to cope with         |
|                  | multipath propagation effects (e.g. via          |
|                  | equalizer, rake receiver, cyclic prefix, etc.).  |
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
|                  | -   *Frequency accuracy (wide area BS): within   |
|                  |     ±0.05 ppm, observed over 1ms*                |
|                  |                                                  |
|                  | -   *Timing accuracy: time alignment error (TAE) |
|                  |     is within 65 ns for single carrier (MIMO or  |
|                  |     TX div), 260 ns for intra-band contiguous    |
|                  |     carrier aggregation, 3µs for intra-band      |
|                  |     non-contiguous and inter-band CA.*           |
|                  |                                                  |
|                  | *Cell phase synchronization accuracy:*           |
|                  |                                                  |
|                  | -   *The cell phase synchronization accuracy     |
|                  |     measured at BS antenna connectors shall be   |
|                  |     better than 3 µs.*                           |
|                  |                                                  |
|                  | *For more information please refer to            |
|                  | \[38.401\], \[38.133\], \[38.104\].*             |
+------------------+--------------------------------------------------+
| 5.2.3.2.21.2     | Describe the synchronization mechanisms used in  |
|                  | the proposal, including synchronization between  |
|                  | a user terminal and a base station.              |
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
|                  | *See more information in \[38.213\] sub-clause 4 |
|                  | and \[38.211\] sub-clause 7.4.2.*                |
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
|                  | ***This proposal targets to support a wide range |
|                  | of services across the diverse usage scenarios   |
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
|                  | [](media/image3.emf){width="2.212538276465442in" |
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
+------------------+--------------------------------------------------+
| **5.2.3.2.26**   | **Other items**                                  |
+------------------+--------------------------------------------------+
| 5.2.3.2.26.1     | *Coverage extension schemes*                     |
|                  |                                                  |
|                  | Describe the capability to support/ coverage     |
|                  | extension schemes, such as relays or repeaters.  |
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
+------------------+--------------------------------------------------+
| 5.2.3.2.26.2     | *Self-organisation*                              |
|                  |                                                  |
|                  | Describe any self-organizing aspects that are    |
|                  | enabled by the RIT/SRIT.                         |
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
|                  | *This RIT is new radio developed by 3GPP, and    |
|                  | will be evolved to be a 3GPP release of NR.*     |
+------------------+--------------------------------------------------+
| 5.2.3.2.26.5     | Does the proposal satisfy a specific spectrum    |
|                  | mask? Provide the detail. (This information is   |
|                  | not intended to be used for sharing studies.)    |
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
+------------------+--------------------------------------------------+
| 5.2.3.2.26.6     | Describe any UE power saving mechanisms used in  |
|                  | the RIT/SRIT.                                    |
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
|                  | *NR supports the following set of features for   |
|                  | providing long battery life:*                    |
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
|                  | *NR supports the following set of features for   |
|                  | providing low latency when waking up from its    |
|                  | most "battery efficient" state:*                 |
|                  |                                                  |
|                  | > -     *Resumption of a previous connection for |
|                  | > minimizing the control signalling, and the     |
|                  | > connection setup latency, when initiating a    |
|                  | > mobile originated or mobile terminated data    |
|                  | > transmission.*                                 |
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
+------------------+--------------------------------------------------+
| 5.2.3.2.26.12    | *Mobility*                                       |
|                  |                                                  |
|                  | Provide additional information for the downlink  |
|                  | mobility performance of the RIT/SRIT (refer to § |
|                  | 4.11 in Report ITU-R M.2410-0).                  |
|                  |                                                  |
|                  | *The downlink mobility performance for NR has    |
|                  | also been evaluated in e.g. \[R1-1809265\] and   |
|                  | it can be concluded that the NR downlink also    |
|                  | fulfils the same KPIs.*                          |
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
