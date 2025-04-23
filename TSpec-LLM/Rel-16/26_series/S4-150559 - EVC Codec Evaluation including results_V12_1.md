Source: HEAD acoustics GmbH
===========================

**Title: EVS -- Objective Codec Evaluation - including results of codec
release version 12.1.0**

Document for: Discussion  {#document-for-discussion .list-paragraph}
------------------------

Agenda Item: 6 {#agenda-item-6 .list-paragraph}
--------------

Introduction
============

The new 3GPP voice and audio codec *Enhanced Voice Service* (EVS) \[1\]
will be used in future 4G networks. In consequence, testing close to
typical application scenarios is reasonable to perform already in the
development phase. In this contribution the results of several
experiments conducted based on measurements derived from acoustic
terminal testing (TS 26.132 \[4\]) are shown. Different to terminal
tests only the codec itself is the "device under test". These selected
tests mainly consider transfer function, idle noise, and non-linear
distortions.

The measurement results presented in **clause** **3** are based on the
codec version i.e. the codec used for the EVS codec selection. The
measurement results presented in the following sections are based on the
release version of the codec.

The measurement results presented in **clause** **4** are based on the
release codec version 12.1.0. The measurement results presented include
the fullband version which is available in the release version. It shows
that the error found in the codec selection version in super-wideband
9.6 kbit/s mode is corrected. For all tests except 5.9 kbit/s bitrate
DTX was deactivated.

Evaluation Setup
================

The first step in the evaluation is the scaling with regard to a certain
overload point. In \[2\] the problem of different values (3.0 vs
9.0 dBm0) was discussed. In this contribution, these two overload points
for the conversion from the physical unit Volt to 16-bit scale were
taken into account.

Since the overload point (OVLP) refers to a full-scale sine wave (with
level T~max~ = -3.01 dBov according to \[3\]), for the scaling between
dBov and dBm0 resp. dBV, the following notation can be made:

T~max~ = -3.01 dBov

![](media/image5.png){width="3.5083333333333333in" height="0.175in"}

![](media/image6.png){width="4.217361111111111in" height="0.175in"}

Example: For an OVLP of 3.0 dBm0, the scaling between dBV and dBov is
defined as:

![](media/image7.png){width="3.6416666666666666in" height="0.175in"}

![](media/image8.png){width="2.025in" height="0.4in"}

The scaling back to the physical unit Volt was applied in the
corresponding inverse way.

After scaling, the next step included the encoding and decoding of the
audio data. This was conducted with the provided command line
executable. The source code was not recompiled to a new binary.

For the evaluation of narrowband, wideband, and super-wideband mode, all
bit rates which are available in each bandwidth mode according to
Table 1 of \[1\] were used.

Tests derived from 3GPP TS 26-131/-132 with the codec used for the EVS codec selection
======================================================================================

General
-------

Several tests according to 3GPP TS 26-132 \[4\] were performed in order
to evaluate the performance according to \[5\] of the EVS codec. This
measurement standard is originally intended for acoustic testing of
terminals. Since the EVS codec is regarded as the "device under test",
only electrical insertions are reasonable for testing and thus only
measurements in (acoustic) receiving direction are taken into account.

In narrowband the test signal bandlimitation as defined in 3GPP TS
26-132 \[4\] was used. For superwideband the itu-t P.501 \[6\] test
signals were downsampled to 32 kHz, cut-off frequency 14.4 kHz, \>80
dB/oct. For fullband the original speech signals from ITU-T P.501 \[6\]
were used.

With this approach, the EVS codec can be evaluated with typical test
scenarios, which will occur in real-life applications with mobile
phones.

The following graphs include multiple curves representing the different
bit rates within each bandwidth mode. For the sake of clarity, the
corresponding legends are not repeated in each graph, Table 1 shows the
legends used in the following sections.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image9.png){width="1.5756944444444445in" height="1.5125in"}                ![](media/image10.png){width="1.5756944444444445in" height="2.4791666666666665in"}
  NB mode                                                                              WB mode
  ![](media/image11.png){width="1.5756944444444445in" height="1.8402777777777777in"}   ![](media/image12.png){width="2.0208333333333335in" height="1.7708333333333333in"}
  SWB mode                                                                             FB mode
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

Table 1: Legends for different bit rates

EVS-Mode: Narrowband (NB)
-------------------------

In narrowband mode, a sampling rate of 8 kHz and all bit rates (5.9,
7.2, 8.0, 9.6, 13.2, 16.4 and 24.4 kbit/s) according to Table 1 of \[1\]
were used. The two possible target overload points 3.0 and 9.0 dBm0 were
used by default for all analyses.

It should be noted, that even though Table 1 of \[1\] states that a
narrowband signal can be encoded with 16.4 and 24.4 kbit/s, the provided
command line executable produces a bitstream with 13.2 kbit/s.
Therefore, the magenta, the blue, and the grey curves are identical in
the plots of this section and the last three rows of Table 2 and Table 3
state the same values.

### Transfer Function

#### Frequency Response with real speech

The following results are produced by applying the measurement
instructions according to clause 7.4.2 of \[4\]. To simulate also the
impact of level variations, additional overload points of 21.0 and
39.0 dBm0 were also simulated. These overload points do not represent a
realistic conversion, they are only used for checking the linearity of
the codec and can be regarded as attenuations of 18.0 resp. 36.0 dB
compared to the overload point of 3.0 dBm0.

  ----------------------------------------------------------------------------------- -----------------------------------------------------------------------------------
  ![](media/image13.wmf){width="3.1458333333333335in" height="1.992361111111111in"}   ![](media/image14.wmf){width="3.1458333333333335in" height="1.992361111111111in"}
  ![](media/image15.wmf){width="3.1458333333333335in" height="1.992361111111111in"}   ![](media/image16.wmf){width="3.1458333333333335in" height="1.992361111111111in"}
  Figure 1: Frequency response for different overload points                          
  ----------------------------------------------------------------------------------- -----------------------------------------------------------------------------------

The results of this analysis are shown in Figure 1. For the default and
extra overload points, the codec does not violate the given tolerance
scheme according to \[5\] for all bit rates.

#### Frequency Response with composite source signal (CSS)

The following results are produced by applying the measurement
instructions according to clause 7.3.2 of \[4\] which is intended to be
reported only for informative reasons. The composite source according to
ITU-T P.501 \[6\] signal is used as a reference for the calculation.

  ----------------------------------------------------------------------------------- -----------------------------------------------------------------------------------
  ![](media/image17.wmf){width="3.1458333333333335in" height="1.992361111111111in"}   ![](media/image18.wmf){width="3.1458333333333335in" height="1.992361111111111in"}
  ![](media/image19.wmf){width="3.1458333333333335in" height="1.992361111111111in"}   ![](media/image20.wmf){width="3.1458333333333335in" height="1.992361111111111in"}
  Figure 2: Frequency response for different overload points                          
  ----------------------------------------------------------------------------------- -----------------------------------------------------------------------------------

The results of this analysis are shown in Figure 2. For the default
overload points, the codec does not violate the given tolerance scheme
for all bit rates. In contrast to the results with real speech, the
frequency responses for the extra overload points, i.e., with additional
attenuation of the source signal, violate the given tolerance scheme
several times. Especially for low bit rates (red/green curves) the codec
does not perform well.

### Idle Noise with Activation

#### Idle noise generated with activation and digital zero input

The following results are produced by applying the measurement
instructions and requirements according to clause 7.3.2 of \[4\]. This
includes an activation of the device under test with a CSS burst before
the measured idle segment.

  ----------------------------------------------------------------------------------- -----------------------------------------------------------------------------------
  ![](media/image21.wmf){width="3.1486111111111112in" height="1.976388888888889in"}   ![](media/image22.wmf){width="3.1486111111111112in" height="1.976388888888889in"}
  Figure 3: Idle noise spectrum with activation for different overload points         
  ----------------------------------------------------------------------------------- -----------------------------------------------------------------------------------

Neither in the frequency representation shown in Figure 3 nor in the
absolute level values shown in Table 2, a violation of the requirements
according to \[5\] can be observed for any narrowband bit rate.

  ------------- ------------------------- --------
                overload point \[dBm0\]   
  bit rate      3.0                       9.0
  5.9 kbit/s    -97.2                     -90.2
  7.2 kbit/s    -97.9                     -87.8
  8.0 kbit/s    -98.0                     -86.9
  9.6 kbit/s    -106.7                    -108.2
  13.2 kbit/s   -97.7                     -93.3
  16.4 kbit/s   -97.7                     -93.3
  24.4 kbit/s   -97.7                     -93.3
  ------------- ------------------------- --------

Table 2: Idle noise levels with activation in dB(A) (requirement:
-57.0 dB(A))

#### Idle noise generated with activation and dithering noise

The original measurement described in section 3.2.2.1 was conducted with
an input signal which consists only of digital zeros. In order to
analyze the impact of non-zero samples, two different dithering noises
were used instead as a source signal. This dithering noise was created
by randomly modifying the last N bits of each 16-bit sample. By
increasing N, the dithering noise power increases. In this evaluation,
N = 1 and N = 2 was used.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image23.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}   ![](media/image24.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}
  Figure 4: Idle noise spectrum with activation and 1-bit dithering noise              
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image25.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}   ![](media/image26.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}
  Figure 5: Idle noise spectrum with activation and 2-bit dithering noise              
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  ------------- ------------------------- ----------------- ----------------- ------- ------- -------
                overload point \[dBm0\]                                                       
                3.0                       9.0               3.0               9.0     3.0     9.0
  bit rate      no dithering              1-bit dithering   2-bit dithering                   
  5.9 kbit/s    -97.2                     -90.2             -85.5             -77.2   -76.6   -71.9
  7.2 kbit/s    -97.9                     -87.8             -81.4             -80.2   -81.4   -75.3
  8.0 kbit/s    -98.0                     -86.9             -87.6             -79.9   -81.1   -74.8
  9.6 kbit/s    -106.7                    -108.2            -90.6             -84.6   -89.8   -83.9
  13.2 kbit/s   -97.7                     -93.3             -86.8             -79.0   -80.3   -74.0
  16.4 kbit/s   -97.7                     -93.3             -86.8             -79.0   -80.3   -74.0
  24.4 kbit/s   -97.7                     -93.3             -86.8             -79.0   -80.3   -74.0
  ------------- ------------------------- ----------------- ----------------- ------- ------- -------

Table 3: Idle noise levels with activation and dithering noise in dB(A)

Neither in the frequency representations shown in Figure 4 and Figure 5
nor in the absolute level values shown in Table 3, a violation of the
requirements can be observed for any narrowband bit rate or overload
point.

The results for the two overload points, however, show a different
behavior with respect to the same dithering noise power. This is
attributed to the different states of the codec depending on the
overload point specific scalings of the activation sequence. Therefore,
the next section describes the same measurement without activation.

### Idle Noise without Activation

The following results are produced by applying measurement instructions
and requirements of section 3.2.2 but without the preceding activation
sequence.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image27.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}   ![](media/image28.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}
  Figure 6: Idle noise spectrum without activation for different overload points       
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image29.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}   ![](media/image30.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}
  Figure 7: Idle noise spectrum without activation with 1-bit dithering noise          
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image31.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}   ![](media/image32.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}
  Figure 8: Idle noise spectrum without activation with 2-bit dithering noise          
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  ------------- ------------------------- ----------------- ----------------- ------- ------- -------
                overload point \[dBm0\]                                                       
                3.0                       9.0               3                 9       3       9
  bit rate      no dithering              1-bit dithering   2-bit dithering                   
  5.9 kbit/s    -107.5                    -101.5            -86.8             -80.8   -81.8   -75.8
  7.2 kbit/s    -108.2                    -102.7            -87               -80.9   -81.8   -75.7
  8.0 kbit/s    -108.4                    -107.9            -85.9             -80     -81.4   -75.1
  9.6 kbit/s    \< -200.0                 \< -200.0         -92.1             -86.1   -87.8   -81.8
  13.2 kbit/s   -101.9                    -96.3             -85.3             -79.2   -79.9   -73.9
  16.4 kbit/s   -101.9                    -96.3             -85.3             -79.2   -79.9   -73.9
  24.4 kbit/s   -101.9                    -96.3             -85.3             -79.2   -79.9   -73.9
  ------------- ------------------------- ----------------- ----------------- ------- ------- -------

Table 4: Idle noise levels without activation with dithering noise in
dB(A)

Again, neither in the frequency representations shown in Figure 6,
Figure 7, and Figure 8 nor in the absolute level values shown in Table
4, a violation of the requirements can be observed for any wideband bit
rate or overload point.

For the bit rates 9.6 kbit/s, the digital zero input is encoded to a
digital zero output leading to idle noise levels lower than -200 dB(A),
which are outside the plotting range in Figure 6. The other bit rates,
however, generate a non-zero output even for digital zero input.

With dithering noise, the results for the two overload points are
shifted by 6 dB but otherwise show the same behavior. Changing the
overload point from 3 dB to 9 dB as well as enlarging the dithering
noise power from 1-bit to 2-bit, both increase the idle noise spectrum
by about 6 dB. This is consistent and to be expected as in both cases 1
bit of coding precision is lost.

### Distortion vs. input level

The following results are produced by applying the measurement
instructions and requirements according to clause 7.8.2 of \[4\]. It
measures the signal-to-distortion ratio for a 1020 Hz sine with
different source levels. For levels -40 and -45 dBm0, the limits of
22.5 dB and 17.5 dB, respectively, are recommendations and not be
regarded as a failing result.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image33.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}   ![](media/image34.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}
  Figure 9: Signal-to-distortion ratio for different input levels                      
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

The results of this analysis are shown in Figure 9. For all mandatory
levels of -30 dBm0 and above, the codec does not violate the given
tolerance scheme according to \[5\] for all bit rates.

### Distortion vs. frequency

The following results are produced by applying the measurement
instructions and requirements according to clause 7.8.2 of \[4\] which
are extended with source frequencies above 1 kHz. It measures the
signal-to-distortion ratio for different frequencies and constant input
level.

  ----------------------------------------------------------------------- -----------------------------------------------------------------------
  ![](media/image35.wmf){width="3.1243055555555554in" height="1.975in"}   ![](media/image36.wmf){width="3.1243055555555554in" height="1.975in"}
  Figure 10: Signal-to-distortion ratio for different frequencies         
  ----------------------------------------------------------------------- -----------------------------------------------------------------------

The results of this analysis are shown in Figure 10. For all tested
frequencies, the codec does not violate the given tolerance scheme
according to \[5\] for all bit rates.

EVS-Mode: Wideband (WB)
-----------------------

In wideband mode, a sampling rate of 16 kHz and all bit rates (5.9, 7.2,
8.0, 9.6, 13.2, 16.4, 24.4, 32.0, 48.0, 64.0, 96.0 and 128.0 kbit/s)
according to Table 1 of \[1\] were used. The two possible target
overload points 3.0 and 9.0 dBm0 were used by default for all analyses.

### Transfer Function

#### Frequency Response with real speech

The following results are produced by applying the measurement
instructions according to clause 8.4.2 of \[4\]. To simulate also the
impact of level variations, additional overload points of 21.0 and
39.0 dBm0 were also simulated. These overload points do not represent a
realistic conversion, they are only used for checking the linearity of
the codec and can be regarded as attenuations of 18.0 resp. 36.0 dB
compared to the overload point 3.0 dBm0.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image37.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}   ![](media/image38.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}
  ![](media/image39.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}   ![](media/image40.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}
  Figure 11: Frequency response for different overload points                          
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

The results of this analysis are shown in Figure 11. For the default and
extra overload points, the codec does not violate the given tolerance
scheme according to \[5\] for all bit rates.

#### Frequency Response with composite source signal (CSS)

The following results are produced by applying the measurement
instructions similar to clause 8.3.2 of \[4\] which is intended to be
reported only for informative reasons. The composite source according to
ITU-T P.501 \[6\] signal is used as a reference for the calculation.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image41.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}   ![](media/image42.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}
  ![](media/image43.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}   ![](media/image44.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}
  Figure 12: Frequency response for different overload points                          
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

The results of this analysis are shown in Figure 12. For the default
overload points, the codec does not violate the given tolerance scheme
for all bit rates. As for the narrowband mode, the frequency responses
for the extra overload points, i.e., with additional attenuation of the
source signal, violate the given tolerance scheme again several times.
Especially for low bit rates (red/green/cyan curves) the codec does not
perform well when using the CSS.

### Idle Noise with Activation

#### Idle noise generated with activation and digital zero input

The following results are produced by applying the measurement
instructions and requirements according to clause 8.3.2 of \[4\]. This
includes an activation of the device under test with a CSS burst before
the measured idle segment.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image45.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}   ![](media/image46.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}
  Figure 13: Idle noise spectrum with activation for different overload points         
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  -------------- ------------------------- --------
                 overload point \[dBm0\]   
  bit rate       3.0                       9.0
  5.9 kbit/s     -92.1                     -86.4
  7.2 kbit/s     -88.7                     -89.3
  8.0 kbit/s     -88.9                     -89.8
  9.6 kbit/s     -107.9                    -107.1
  13.2 kbit/s    -94.7                     -92.1
  16.4 kbit/s    -105.0                    -106.3
  24.4 kbit/s    -108.7                    -108.4
  32.0 kbit/s    -103.5                    -103.5
  48.0 kbit/s    -112.3                    -111.1
  64.0 kbit/s    -102.3                    -105.5
  96.0 kbit/s    -111.4                    -112.9
  128.0 kbit/s   -111.5                    -113.9
  -------------- ------------------------- --------

Table 5: Idle noise levels with activation in dB(A) (requirement:
-57.0 dB(A))

Neither in the frequency representation shown in Figure 13 nor in the
absolute level values shown in Table 5, a violation of the requirements
according to \[5\] can be observed for any wideband bit rate.

#### Idle noise generated with activation and dithering noise

The original measurement described in section 3.3.2.1 was conducted with
an input signal which consists only of digital zeros. In order to
analyze the impact of non-zero samples, two different dithering noises
were used instead as a source signal. This dithering noise was created
by randomly modifying the last N bits of each 16-bit sample. By
increasing N, the dithering noise power increases. In this evaluation,
N = 1 and N = 2 was used.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image47.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}   ![](media/image48.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}
  Figure 14: Idle noise spectrum with activation and 1-bit dithering noise             
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image49.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}   ![](media/image50.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}
  Figure 15: Idle noise spectrum with activation and 2-bit dithering noise             
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  -------------- ------------------------- ----------------- ----------------- ------- ------- -------
                 overload point \[dBm0\]                                                       
                 3.0                       9.0               3.0               9.0     3.0     9.0
  bit rate       no dithering              1-bit dithering   2-bit dithering                   
  5.9 kbit/s     -92.1                     -86.4             -85.5             -80.0   -80.1   -74.4
  7.2 kbit/s     -88.7                     -89.3             -86.1             -80.7   -81.0   -75.7
  8.0 kbit/s     -88.9                     -89.8             -86.2             -78.7   -79.4   -74.1
  9.6 kbit/s     -107.9                    -107.1            -90.5             -84.7   -84.5   -78.6
  13.2 kbit/s    -94.7                     -92.1             -88.6             -83.0   -81.5   -75.5
  16.4 kbit/s    -105.0                    -106.3            -89.8             -83.9   -82.7   -76.7
  24.4 kbit/s    -108.7                    -108.4            -84.4             -83.8   -82.0   -75.8
  32.0 kbit/s    -103.5                    -103.5            -89.1             -82.7   -81.4   -75.4
  48.0 kbit/s    -112.3                    -111.1            -87.9             -81.9   -80.6   -74.7
  64.0 kbit/s    -102.3                    -105.5            -88.0             -81.6   -80.8   -74.9
  96.0 kbit/s    -111.4                    -112.9            -88.2             -82.3   -80.9   -74.9
  128.0 kbit/s   -111.5                    -113.9            -88.3             -82.3   -80.9   -74.9
  -------------- ------------------------- ----------------- ----------------- ------- ------- -------

Table 6: Idle noise levels with activation and dithering noise in dB(A)

Neither in the frequency representations shown in Figure 14 and Figure
15 nor in the absolute level values shown in Table 6, a violation of the
requirements can be observed for any wideband bit rate or overload
point.

The results for the two overload points, however, show a different
behavior with respect to the same dithering noise power, especially at
bit rate 24.4 kbit/s. The codec produces a higher amount of low
frequency noise after the activation signal compared to other bitrates.
Probably this can be attributed to the different states of the codec
depending on the overload point specific scaling of the activation
sequence. The low frequency noise disappears shortly after the
activation. Therefore, the next section describes the same measurement
without activation.

### Idle Noise without Activation

The following results are produced by applying measurement instructions
and requirements of section 3.3.2 but without the preceding activation
sequence.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image51.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}   ![](media/image52.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}
  Figure 16: Idle noise spectrum without activation for different overload points      
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image53.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}   ![](media/image54.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}
  Figure 17: Idle noise spectrum without activation with 1-bit dithering noise         
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image55.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}   ![](media/image56.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}
  Figure 18: Idle noise spectrum without activation with 2-bit dithering noise         
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  -------------- ------------------------- ----------------- ----------------- ------- ------- -------
                 overload point \[dBm0\]                                                       
                 3.0                       9.0               3.0               9.0     3       9
  bit rate       no dithering              1-bit dithering   2-bit dithering                   
  5.9 kbit/s     -101.6                    -95.6             -87.7             -81.7   -76.5   -70.5
  7.2 kbit/s     -102.6                    -96.6             -82.6             -76.6   -78.3   -72.3
  8.0 kbit/s     -100.9                    -94.9             -82.2             -76.2   -77.9   -71.9
  9.6 kbit/s     \< -200.0                 \< -200.0         -90.2             -84.2   -83.9   -77.9
  13.2 kbit/s    -96.4                     -90.4             -86.0             -80.0   -79.2   -73.2
  16.4 kbit/s    \< -200.0                 \< -200.0         -90.2             -84.2   -82.8   -76.8
  24.4 kbit/s    \< -200.0                 \< -200.0         -89.6             -83.6   -82.1   -76.1
  32.0 kbit/s    -122.4                    -116.4            -88.6             -82.6   -82.5   -76.5
  48.0 kbit/s    \< -200.0                 \< -200.0         -88.0             -82.0   -80.5   -74.5
  64.0 kbit/s    \< -200.0                 \< -200.0         -87.8             -81.8   -82.3   -76.3
  96.0 kbit/s    \< -200.0                 \< -200.0         -88.3             -82.3   -80.6   -74.6
  128.0 kbit/s   \< -200.0                 \< -200.0         -88.3             -82.3   -80.6   -74.6
  -------------- ------------------------- ----------------- ----------------- ------- ------- -------

Table 7: Idle noise levels without activation with dithering noise in
dB(A)

Again, neither in the spectral analysis of the noise floor shown in
Figure 16, Figure 17, and Figure 18 nor in the absolute level values
shown in Table 7, a violation of the requirements can be observed for
any wideband bit rate or overload point.

For the bit rates 9.6, 16.4, 24.4, 48.0, 64.0, 96.0, and 128.0 kbit/s,
the digital zero input is encoded to a digital zero output leading to
idle noise levels lower than -200 dB(A), which are outside the plotting
range in Figure 16. The other bit rates 5.9, 7.2, 8.0, 13.2, and
32.0 kbit/s, however, generate a non-zero output even for digital zero
input.

With dithering noise, the results for the two overload points are
shifted by 6 dB but otherwise show the same behavior.

### Distortion vs. input level

The following results are produced by applying the measurement
instructions and requirements according to clause 8.8.2 of \[4\]. The
signal-to-distortion ratio is measured for a 1020 Hz sine with different
source levels. For levels -40 and -45 dBm0, the limits of 22.5 dB and
17.5 dB, respectively, are recommendations and not be regarded as a
failing result.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image57.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}   ![](media/image58.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}
  Figure 19: Signal-to-distortion ratio for different input levels                     
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

The results of this analysis are shown in Figure 19. It can be observed
that for lower bit rates (red/green/cyan/yellow curves) the
signal-to-distortion ratio violates the tolerance scheme according to
\[5\] at some gain points. All other bit rates pass the test. Note, that
the apparently strong variances of distortion curves are mainly caused
by the sinusoidal source signal which is used here. For these bit rates,
sine signals are not well encoded/decoded. Distortion measurements with
real speech or at least speech-like signals might lead to more uniform
results.

### Distortion vs. frequency

The following results are produced by applying the measurement
instructions and requirements according to clause 8.8.2 of \[4\] which
are extended with source frequencies above 1 kHz. The
signal-to-distortion ratio for different frequencies and constant input
level is measured.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image59.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}   ![](media/image60.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}
  Figure 20: Signal-to-distortion ratio for different frequencies                      
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

The results of this analysis are shown in Figure 20. Again, the
signal-to-distortion ratio violates the tolerance scheme according to
\[5\] at lower bit rates (red/green/cyan curves) for the same reason as
above. All other bit rates pass the test.

EVS-Mode: Super-Wideband (SWB)
------------------------------

In super-wideband mode, a sampling rate of 32 kHz and all bit rates
(9.6, 13.2, 16.4, 24.4, 32.0, 48.0, 64.0, 96.0 and 128.0 kbit/s)
according to Table 1 of \[1\] were used. The two possible target
overload points 3.0 and 9.0 dBm0 were used by default for all analyses.

It should be noted, that even though Table 1 of \[1\] states that a
signal can be encoded in super-wideband mode with 9.6 kbit/s, the
provided command line executable encodes effectively only the wideband
bandwidth up to 8 kHz. Therefore, the green curve violates the tolerance
schema in Figure 21, Figure 22, and Figure 30.

### Transfer Function

#### Frequency Response with real speech

The following results are produced by applying measurement instructions
similar to clause 8.4.2 of \[4\] which are adapted to super-wideband by
replacing the source signal with a fullband version of the same file and
extending the tolerance schema to 14 kHz. To simulate also the impact of
level variations, additional overload points of 21.0 and 39.0 dBm0 were
also simulated. These overload points do not represent a realistic
conversion; they are only used for checking the linearity of the codec
and can be regarded as attenuations of 18.0 resp. 36.0 dB compared to
the overload point 3.0 dBm0.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image61.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}   ![](media/image62.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}
  ![](media/image63.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}   ![](media/image64.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}
  Figure 21: Frequency response for different overload points                          
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

The results of this analysis are shown in Figure 21. For the default and
extra overload points, the codec does not violate the given tolerance
scheme according to \[5\] for all bit rates but 9.6 kbit/s as explained
above.

#### Frequency Response with composite source signal (CSS)

The following results are produced by applying the measurement
instructions similar to clause 8.3.2 of \[4\] which is intended to be
reported only for informative reasons. The composite source according to
ITU-T P.501 \[6\] signal is used as a reference for the calculation.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image65.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}   ![](media/image66.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}
  ![](media/image67.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}   ![](media/image68.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}
  Figure 22: Frequency response for different overload points                          
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

The results of this analysis are shown in Figure 22. For the default
overload points, the codec does not violate the given tolerance scheme
for all bit rates but 9.6 kbit/s as explained above. As for the
narrowband mode, the frequency responses for the extra overload points,
i.e., with additional attenuation of the source signal, violate the
given tolerance scheme again several times. Especially for low bit rates
(red/green curves) the codec does not perform well.

### Idle Noise with Activation

#### Idle noise generated with activation and digital zero input

The following results are produced by applying measurement instructions
and requirements similar to clause 8.3.2 of \[4\] which are adapted to
super-wideband by replacing the source signal with a fullband version of
the same file. This includes an activation of the device under test with
a CSS burst before the measured idle segment.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image69.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}   ![](media/image70.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}
  Figure 23: Idle noise spectrum with activation for different overload points         
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  -------------- ------------------------- --------
                 overload point \[dBm0\]   
  bit rate       3.0                       9.0
  9.6 kbit/s     -106.1                    -108.2
  13.2 kbit/s    -92.1                     -91.6
  16.4 kbit/s    -106.0                    -105.6
  24.4 kbit/s    -109.5                    -108.1
  32.0 kbit/s    -94.6                     -91.3
  48.0 kbit/s    -111.6                    -109.8
  64.0 kbit/s    -107.8                    -106.6
  96.0 kbit/s    -110.3                    -111.8
  128.0 kbit/s   -110.8                    -114.7
  -------------- ------------------------- --------

Table 8: Idle noise levels with activation in dB(A) (requirement:
-57.0 dB(A))

Neither in the frequency representation shown in Figure 23 nor in the
absolute level values shown in Table 8, a violation of the requirements
according to \[5\] can be observed for any super-wideband bit rate.

#### Idle noise generated with activation and dithering noise

The original measurement described in section 3.4.2.1 was conducted with
an input signal which consists only of digital zeros. In order to
analyze the impact of non-zero samples, two different dithering noises
were used instead as a source signal. This dithering noise was created
by randomly modifying the last N bits of each 16-bit sample. By
increasing N, the dithering noise power increases. In this evaluation,
N = 1 and N = 2 was used.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image71.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}   ![](media/image72.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}
  Figure 24: Idle noise spectrum with activation and 1-bit dithering noise             
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image73.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}   ![](media/image74.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}
  Figure 25: Idle noise spectrum with activation and 2-bit dithering noise             
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  -------------- ------------------------- ----------------- ----------------- ------- ------- -------
                 overload point \[dBm0\]                                                       
                 3.0                       9.0               3.0               9.0     3.0     9.0
  bit rate       no dithering              1-bit dithering   2-bit dithering                   
  9.6 kbit/s     -106.1                    -108.2            -93.2             -87.4   -87.5   -81.4
  13.2 kbit/s    -92.1                     -91.6             -89.9             -84.3   -83.6   -77.8
  16.4 kbit/s    -106.0                    -105.6            -90.2             -84.6   -83.2   -77.3
  24.4 kbit/s    -109.5                    -108.1            -78.8             -84.4   -82.7   -76.8
  32.0 kbit/s    -94.6                     -91.3             -89.7             -84.9   -82.9   -76.9
  48.0 kbit/s    -111.6                    -109.8            -80.4             -83.8   -82.3   -76.3
  64.0 kbit/s    -107.8                    -106.6            -90.0             -84.1   -82.8   -76.4
  96.0 kbit/s    -110.3                    -111.8            -90.3             -84.3   -82.5   -76.5
  128.0 kbit/s   -110.8                    -114.7            -90.3             -84.3   -82.5   -76.5
  -------------- ------------------------- ----------------- ----------------- ------- ------- -------

Table 9: Idle noise levels with activation and dithering noise in dB(A)

Neither in the frequency representations shown in Figure 24 and Figure
25 nor in the absolute level values shown in Table 9, a violation of the
requirements can be observed for any super-wideband bit rate or overload
point.

The results for the two overload points, however, show a different
behavior with respect to the same dithering noise power, especially at
bit rates 24.4 and 48.0 kbit/s. This is attributed to the different
states of the codec depending on the overload point specific scalings of
the activation sequence. Therefore, the next section describes the same
measurement without activation.

### Idle Noise without Activation

The following results are produced by applying measurement instructions
and requirements of section 3.4.2 but without the preceding activation
sequence.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image75.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}   ![](media/image76.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}
  Figure 26: Idle noise spectrum without activation for different overload points      
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image77.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}   ![](media/image78.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}
  Figure 27: Idle noise spectrum without activation with 1-bit dithering noise         
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image79.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}   ![](media/image80.wmf){width="3.1486111111111112in" height="1.9715277777777778in"}
  Figure 28: Idle noise spectrum without activation with 2-bit dithering noise         
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  -------------- ------------------------- ----------------- ----------------- ------- ------- -------
                 overload point \[dBm0\]                                                       
                 3.0                       9.0               3.0               9.0     3.0     9.0
  bit rate       no dithering              1-bit dithering   2-bit dithering                   
  9.6 kbit/s     \< -200.0                 \< -200.0         -92.9             -86.9   -88.2   -82.2
  13.2 kbit/s    -92.9                     -86.9             -89.6             -83.6   -82.5   -76.5
  16.4 kbit/s    \< -200.0                 \< -200.0         -90.6             -84.6   -83.6   -77.6
  24.4 kbit/s    \< -200.0                 \< -200.0         -90.4             -84.4   -82.9   -76.9
  32.0 kbit/s    -95.0                     -89.0             -91.3             -85.3   -83.5   -77.5
  48.0 kbit/s    \< -200.0                 \< -200.0         -89.9             -83.9   -82.4   -76.4
  64.0 kbit/s    \< -200.0                 \< -200.0         -90.1             -84.1   -83.1   -77.1
  96.0 kbit/s    \< -200.0                 \< -200.0         -90.2             -84.2   -82.3   -76.3
  128.0 kbit/s   \< -200.0                 \< -200.0         -90.2             -84.2   -82.6   -76.6
  -------------- ------------------------- ----------------- ----------------- ------- ------- -------

Table 10: Idle noise levels without activation with dithering noise in
dB(A)

Again, neither in the frequency representations shown in Figure 26,
Figure 27, and Figure 28 nor in the absolute level values shown in Table
10, a violation of the requirements can be observed for any
super-wideband bit rate or overload point.

For all bit rates but 13.2 and 32.0 kbit/s, the digital zero input is
encoded to a digital zero output leading to idle noise levels lower than
-200 dB(A), which are outside the plotting range in Figure 26. These two
bit rates, however, generate a non-zero output even for digital zero
input.

With dithering noise, the results for the two overload points are
shifted by 6 dB but otherwise show the same behavior.

### Distortion vs. input level

The following results are produced by applying the measurement
instructions and requirements according to clause 8.8.2 of \[4\], which
are adapted to super-wideband by evaluating the distortion up to 14 kHz.
It measures the signal-to-distortion ratio for a 1020 Hz sine with
different source levels. For levels -40 and -45 dBm0, the limits of
22.5 dB and 17.5 dB, respectively, are recommendations and not be
regarded as a failing result.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image81.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}   ![](media/image82.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}
  Figure 29: Signal-to-distortion ratio for different input levels                     
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

The results of this analysis are shown in Figure 29. At low bit rates
(red/green curves), the signal-to-distortion ratio violates the
tolerance according to \[5\] scheme at gain as low as -30dB. All other
bit rates pass the test.

### Distortion vs. frequency

The following results are produced by applying the measurement
instructions and requirements according to clause 8.8.2 of \[4\] which
are extended with source frequencies above 1 kHz and adapted to
super-wideband by evaluating the distortion up to 14 kHz. It measures
the signal-to-distortion ratio for different frequencies and constant
input level.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image83.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}   ![](media/image84.wmf){width="3.1458333333333335in" height="1.9868055555555555in"}
  Figure 30: Signal-to-distortion ratio for different frequencies                      
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

The results of this analysis are shown in Figure 30. For all tested
frequencies, the codec does not violate the given tolerance scheme
according to \[5\] for all bit rates but 9.6 kbit/s. At 9.6 kbit/s, the
codec fails for the test frequency of about 13 kHz, which is not encoded
at this bit rate as explained above

Tests derived from 3GPP TS 26.131 and TS 26.132 with EVS v12.1.0 \[7\]
======================================================================

 EVS-Mode: Narrowband (NB)
-------------------------

###  General

In narrowband mode, a sampling rate of 8 kHz and all bit rates (5.9,
7.2, 8.0, 9.6, 13.2, 16.4 and 24.4 kbit/s) according to Table 1 of \[1\]
were used. The two possible target overload points 3.0 and 9.0 dBm0 were
used by default for all analyses.

###  Frequency response with real speech

The following results are produced by applying the measurement
instructions according to clause 7.4.2 of \[4\]. To simulate also the
impact of level variations, additional overload points of 21.0 and
39.0 dBm0 were also simulated. These overload points do not represent a
realistic conversion, they are only used for checking the linearity of
the codec and can be regarded as attenuations of 18.0 resp. 36.0 dB
compared to the overload point of 3.0 dBm0.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image85.wmf){width="3.1444444444444444in" height="1.9909722222222221in"}   ![](media/image86.wmf){width="3.1444444444444444in" height="1.9909722222222221in"}
  ![](media/image87.wmf){width="3.1444444444444444in" height="1.9909722222222221in"}   ![](media/image88.wmf){width="3.1444444444444444in" height="1.9909722222222221in"}
  Figure 31: Frequency response for different overload points                          
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

The results of this analysis are shown in Figure 1. For the default and
extra overload points, the codec does not violate the given tolerance
scheme according to \[5\] for all bit rates.

The results when using 1/3^rd^ octave instead of 1/12^th^ octave
analysis are in Figure 32.

  -------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------
  ![](media/image89.wmf){width="3.138888888888889in" height="1.9875in"}                                          ![](media/image90.wmf){width="3.138888888888889in" height="1.9875in"}
                                                                                                                 
  Figure 32: Frequency response EVS NB in 1/3^rd^ Oct. for different overload points with P.501 speech signals   
  -------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------

###  Frequency response with composite source signal (CSS)

The following results are produced by applying the measurement
instructions according to clause 7.3.2 of \[4\] which is intended to be
reported only for informative reasons. The composite source according to
ITU-T P.501 \[6\] signal is used as a reference for the calculation.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image91.wmf){width="3.1444444444444444in" height="1.9909722222222221in"}   ![](media/image92.wmf){width="3.1444444444444444in" height="1.9909722222222221in"}
  ![](media/image93.wmf){width="3.1444444444444444in" height="1.9909722222222221in"}   ![](media/image94.wmf){width="3.1444444444444444in" height="1.9909722222222221in"}
  Figure 33: Frequency response for different overload points                          
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

The results of this analysis are shown in Figure 33. For none of the
overload points, the codec violates the given tolerance scheme. This
applies for all bit rates Idle noise generated with activation and
digital zero input

The following results are produced by applying the measurement
instructions and requirements according to clause 7.3.2 of \[4\]. This
includes an activation of the device under test with a CSS burst before
the measured idle segment.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image95.wmf){width="3.1465277777777776in" height="1.9784722222222222in"}   ![](media/image96.wmf){width="3.1465277777777776in" height="1.9784722222222222in"}
  Figure 34: Idle noise spectrum with activation for different overload points         
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

Neither in the frequency representation shown in Figure 34 nor in the
absolute level values shown in Table 11, a violation of the requirements
according to \[5\] can be observed for any narrowband bit rate.

  ------------- ------------------------- --------
                overload point \[dBm0\]   
  bit rate      3.0                       9.0
  5.9 kbit/s    -93.3                     -89.9
  7.2 kbit/s    -100.9                    -97.3
  8.0 kbit/s    -100.1                    -94.7
  9.6 kbit/s    -92.0                     -108.5
  13.2 kbit/s   -99.2                     -94.0
  16.4 kbit/s   -91.7                     -107.2
  24.4 kbit/s   -91.6                     -109.8
  ------------- ------------------------- --------

Table 11: Idle noise levels with activation in dB(A) (requirement:
-57.0 dB(A))

###  Idle noise generated with activation and dithering noise

The original measurement described in section 3.2.2.1 was conducted with
an input signal which consists only of digital zeros. In order to
analyze the impact of non-zero samples, two different dithering noises
were used instead as a source signal. This dithering noise was created
by randomly modifying the last N bits of each 16-bit sample. By
increasing N, the dithering noise power increases. In this evaluation,
N = 1 and N = 2 was used.

  ----------------------------------------------------------------------------------- -----------------------------------------------------------------------------------
  ![](media/image97.wmf){width="3.136111111111111in" height="1.9722222222222223in"}   ![](media/image98.wmf){width="3.136111111111111in" height="1.9722222222222223in"}
  Figure 35: Idle noise spectrum with activation and 1-bit dithering noise            
  ----------------------------------------------------------------------------------- -----------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------- ------------------------------------------------------------------------------------
  ![](media/image99.wmf){width="3.136111111111111in" height="1.9722222222222223in"}   ![](media/image100.wmf){width="3.136111111111111in" height="1.9722222222222223in"}
  Figure 36: Idle noise spectrum with activation and 2-bit dithering noise            
  ----------------------------------------------------------------------------------- ------------------------------------------------------------------------------------

  ------------- ------------------------- ----------------- ----------------- ------- ------- -------
                overload point \[dBm0\]                                                       
                3.0                       9.0               3.0               9.0     3.0     9.0
  bit rate      no dithering              1-bit dithering   2-bit dithering                   
  5.9 kbit/s    -93.3                     -89.9             -85.0             -79.1   -79.6   -73.3
  7.2 kbit/s    -100.9                    -97.3             -79.5             -80.6   -81.4   -75.6
  8.0 kbit/s    -100.1                    -94.7             -86.7             -79.9   -81.1   -75.1
  9.6 kbit/s    -92.0                     -108.5            -90.3             -85.9   -88.9   -82.9
  13.2 kbit/s   -99.2                     -94.0             -85.9             -79.0   -80.1   -74.2
  16.4 kbit/s   -91.7                     -107.2            -89.3             -83.3   -82.2   -76.1
  24.4 kbit/s   -91.6                     -109.8            -88.7             -82.6   -81.2   -75.2
  ------------- ------------------------- ----------------- ----------------- ------- ------- -------

Table 12: Idle noise levels with activation and dithering noise in dB(A)

Neither in the frequency representations shown in Figure 35 and Figure
36 nor in the absolute level values shown in Table 12, a violation of
the requirements can be observed for any narrowband bit rate or overload
point.

The results for the two overload points, however, show a slightly
different behavior with respect to the same dithering noise power. This
is attributed to the different states of the codec depending on the
overload point specific scalings of the activation sequence.

###  Idle Noise without Activation

The following results are produced by applying measurement without the
preceding activation sequence.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image101.wmf){width="3.136111111111111in" height="1.9722222222222223in"}   ![](media/image102.wmf){width="3.136111111111111in" height="1.9722222222222223in"}
  Figure 37: Idle noise spectrum without activation for different overload points      
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image103.wmf){width="3.136111111111111in" height="1.9722222222222223in"}   ![](media/image104.wmf){width="3.136111111111111in" height="1.9722222222222223in"}
  Figure 38: Idle noise spectrum without activation with 1-bit dithering noise         
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image105.wmf){width="3.136111111111111in" height="1.9722222222222223in"}   ![](media/image106.wmf){width="3.136111111111111in" height="1.9722222222222223in"}
  Figure 39: Idle noise spectrum without activation with 2-bit dithering noise         
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  ------------- ------------------------- ----------------- ----------------- ------- ------- -------
                overload point \[dBm0\]                                                       
                3.0                       9.0               3                 9       3       9
  bit rate      no dithering              1-bit dithering   2-bit dithering                   
  5.9 kbit/s    -94.8                     -88.8             -84.1             -78.1   -78.5   -72.6
  7.2 kbit/s    -110.2                    -102.7            -86.9             -80.9   -81.6   -75.7
  8.0 kbit/s    -108.9                    -107.9            -86.0             -80.0   -81.3   -75.3
  9.6 kbit/s    -205.8                    -205.8            -92.5             -86.5   -88.1   -82.1
  13.2 kbit/s   -102.4                    -95.7             -85.2             -79.4   -80.2   -74.1
  16.4 kbit/s   -205.8                    -205.8            -89.2             -83.2   -82.0   -76.0
  24.4 kbit/s   -205.8                    -205.8            -88.2             -82.2   -81.2   -75.2
  ------------- ------------------------- ----------------- ----------------- ------- ------- -------

Table 13: Idle noise levels without activation with dithering noise in
dB(A)

Again, neither in the frequency representations shown in Figure 37,
Figure 38, and Figure 39 nor in the absolute level values shown in Table
13, a violation of the requirements can be observed for any wideband bit
rate or overload point.

For the bit rates 9.6 kbit/s, the digital zero input is encoded to a
digital zero output leading to idle noise levels lower than -200 dB(A),
which are outside the plotting range in Figure 37. The other bit rates,
however, generate a non-zero output even for digital zero input.

With dithering noise, the results for the two overload points are
shifted by 6 dB but otherwise show the same behavior. Changing the
overload point from 3 dB to 9 dB as well as enlarging the dithering
noise power from 1-bit to 2-bit, both increase the idle noise spectrum
by about 6 dB. This is consistent and to be expected as in both cases 1
bit of coding precision is lost.

###  Distortion vs. input level

The following results are produced by applying the measurement
instructions and requirements according to clause 7.8.2 of \[4\]. It
measures the signal-to-distortion ratio for a 1020 Hz sine with
different source levels. For levels -40 and -45 dBm0, the limits of
22.5 dB and 17.5 dB, respectively, are recommendations and not be
regarded as a failing result.

  ------------------------------------------------------------------------ ------------------------------------------------------------------------
  ![](media/image107.wmf){width="3.138888888888889in" height="1.9875in"}   ![](media/image108.wmf){width="3.138888888888889in" height="1.9875in"}
  Figure 40: Signal-to-distortion ratio for different input levels         
  ------------------------------------------------------------------------ ------------------------------------------------------------------------

The results of this analysis are shown in Figure 40. For all mandatory
levels of -30 dBm0 and above, the codec does not violate the given
tolerance scheme according to \[5\] for all bit rates.

###  Distortion vs. frequency

The following results are produced by applying the measurement
instructions and requirements according to clause 7.8.2 of \[4\] which
are extended with source frequencies above 1 kHz. It measures the
signal-to-distortion ratio for different frequencies and constant input
level.

  ------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------
  ![](media/image109.wmf){width="3.1194444444444445in" height="1.9784722222222222in"}   ![](media/image110.wmf){width="3.1194444444444445in" height="1.9784722222222222in"}
  Figure 41: Signal-to-distortion ratio for different frequencies                       
  ------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------

The results of this analysis are shown in Figure 41. For all tested
frequencies, the codec does not violate the given tolerance scheme
according to \[5\] for all bit rates.

EVS-Mode: Wideband (WB)
-----------------------

###  General

In wideband mode, a sampling rate of 16 kHz and all bit rates (5.9, 7.2,
8.0, 9.6, 13.2, 16.4, 24.4, 32.0, 48.0, 64.0, 96.0 and 128.0 kbit/s)
according to Table 1 of \[1\] were used. The two possible target
overload points 3.0 and 9.0 dBm0 were used by default for all analyses.

###  Frequency response with real speech

The following results are produced by applying the measurement
instructions according to clause 8.4.2 of \[4\]. To simulate also the
impact of level variations, additional overload points of 21.0 and
39.0 dBm0 were also simulated. These overload points do not represent a
realistic conversion, they are only used for checking the linearity of
the codec and can be regarded as attenuations of 18.0 resp. 36.0 dB
compared to the overload point 3.0 dBm0.

  ------------------------------------------------------------------------ ------------------------------------------------------------------------
  ![](media/image111.wmf){width="3.138888888888889in" height="1.9875in"}   ![](media/image112.wmf){width="3.138888888888889in" height="1.9875in"}
  ![](media/image113.wmf){width="3.138888888888889in" height="1.9875in"}   ![](media/image114.wmf){width="3.138888888888889in" height="1.9875in"}
  Figure 42: Frequency response for different overload points              
  ------------------------------------------------------------------------ ------------------------------------------------------------------------

The results of this analysis are shown in Figure 42. For the default and
extra overload points, the codec does not violate the given tolerance
scheme according to \[5\] for all bit rates.

Instead of 1/12^th^ octave analysis was used. The results using 1/3^rd^
octave analysis are shown in Figure 43.

  -------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------
  ![](media/image115.wmf){width="3.138888888888889in" height="1.9875in"}                                         ![](media/image116.wmf){width="3.138888888888889in" height="1.9875in"}
                                                                                                                 
  Figure 43: Frequency response EVS WB in 1/3^rd^ Oct. for different overload points with P.501 speech signals   
  -------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------

###  Frequency response with composite source signal (CSS)

The following results are produced by applying the measurement
instructions similar to clause 8.3.2 of \[4\] which is intended to be
reported only for informative reasons. The composite source according to
ITU-T P.501 \[6\] signal is used as a reference for the calculation.

  ------------------------------------------------------------------------ ------------------------------------------------------------------------
  ![](media/image117.wmf){width="3.138888888888889in" height="1.9875in"}   ![](media/image118.wmf){width="3.138888888888889in" height="1.9875in"}
  ![](media/image119.wmf){width="3.138888888888889in" height="1.9875in"}   ![](media/image120.wmf){width="3.138888888888889in" height="1.9875in"}
  Figure 44: Frequency response for different overload points              
  ------------------------------------------------------------------------ ------------------------------------------------------------------------

The results of this analysis are shown in Figure 44. For none of the
overload points, the codec violates the given tolerance scheme. This is
valid for all bit rates..

###  Idle noise generated with activation and digital zero input

The following results are produced by applying the measurement
instructions and requirements according to clause 8.3.2 of \[4\]. This
includes an activation of the device under test with a CSS burst before
the measured idle segment.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image121.wmf){width="3.136111111111111in" height="1.9722222222222223in"}   ![](media/image122.wmf){width="3.136111111111111in" height="1.9722222222222223in"}
  Figure 45: Idle noise spectrum with activation for different overload points         
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  -------------- ------------------------- --------
                 overload point \[dBm0\]   
  bit rate       3.0                       9.0
  5.9 kbit/s     -205.8                    -205.8
  7.2 kbit/s     -91.6                     -88.4
  8.0 kbit/s     -92.4                     -87.5
  9.6 kbit/s     -108.1                    -107.2
  13.2 kbit/s    -95.2                     -91.7
  16.4 kbit/s    -105.5                    -106.9
  24.4 kbit/s    -109.2                    -109.1
  32.0 kbit/s    -107.3                    -105.3
  48.0 kbit/s    -113.2                    -111.4
  64.0 kbit/s    -101.8                    -107.8
  96.0 kbit/s    -111.9                    -113.0
  128.0 kbit/s   -111.9                    -114.5
  -------------- ------------------------- --------

Table 14: Idle noise levels with activation in dB(A) (requirement:
-57.0 dB(A))

Neither in the frequency representation shown in Figure 44 nor in the
absolute level values shown in Table 14, a violation of the requirements
according to \[5\] can be observed for any wideband bit rate.

###  Idle noise generated with activation and dithering noise

The original measurement was conducted with an input signal which
consists only of digital zeros. In order to analyze the impact of
non-zero samples, two different dithering noises were used instead as a
source signal. This dithering noise was created by randomly modifying
the last N bits of each 16-bit sample. By increasing N, the dithering
noise power increases. In this evaluation, N = 1 and N = 2 was used.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image123.wmf){width="3.136111111111111in" height="1.9722222222222223in"}   ![](media/image124.wmf){width="3.136111111111111in" height="1.9722222222222223in"}
  Figure 46: Idle noise spectrum with activation and 1-bit dithering noise             
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image125.wmf){width="3.136111111111111in" height="1.9722222222222223in"}   ![](media/image126.wmf){width="3.136111111111111in" height="1.9722222222222223in"}
  Figure 47: Idle noise spectrum with activation and 2-bit dithering noise             
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  -------------- ------------------------- ----------------- ----------------- -------- -------- --------
                 overload point \[dBm0\]                                                         
                 3.0                       9.0               3.0               9.0      3.0      9.0
  bit rate       no dithering              1-bit dithering   2-bit dithering                     
  5.9 kbit/s     -205.8                    -205.8            -205.8            -205.8   -205.8   -205.8
  7.2 kbit/s     -91.6                     -88.4             -84.5             -79.2    -80.1    -74.4
  8.0 kbit/s     -92.4                     -87.5             -84.4             -79.0    -78.6    -72.9
  9.6 kbit/s     -108.1                    -107.2            -90.5             -84.5    -84.3    -78.3
  13.2 kbit/s    -95.2                     -91.7             -87.3             -81.4    -80.6    -74.8
  16.4 kbit/s    -105.5                    -106.9            -89.9             -84.0    -82.9    -76.8
  24.4 kbit/s    -109.2                    -109.1            -84.4             -83.7    -82.1    -76.0
  32.0 kbit/s    -107.3                    -105.3            -88.2             -82.3    -81.2    -75.2
  48.0 kbit/s    -113.2                    -111.4            -87.9             -81.9    -80.7    -74.7
  64.0 kbit/s    -101.8                    -107.8            -87.2             -81.1    -80.5    -74.5
  96.0 kbit/s    -111.9                    -113.0            -88.2             -82.2    -80.9    -74.9
  128.0 kbit/s   -111.9                    -114.5            -88.2             -82.2    -80.9    -74.9
  -------------- ------------------------- ----------------- ----------------- -------- -------- --------

Table 15: Idle noise levels with activation and dithering noise in dB(A)

Neither in the frequency representations shown in Figure 46 and Figure
47 nor in the absolute level values shown in Table 15, a violation of
the requirements can be observed for any wideband bit rate or overload
point.

The results for the two overload points, however, show a different
behavior with respect to the same dithering noise power, especially at
the bit rate 24.4 kbit/s. The codec produces a higher amount of low
frequency noise after the activation signal compared to other bitrates.
Probably this can be attributed to the different states of the codec
depending on the overload point specific scaling of the activation
sequence. The low frequency noise disappears shortly after the
activation. Therefore, the next section describes the same measurement
without activation.

###  Idle Noise without Activation

The following results are produced by applying measurement instructions
and requirements without the preceding activation sequence.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image127.wmf){width="3.136111111111111in" height="1.9722222222222223in"}   ![](media/image128.wmf){width="3.136111111111111in" height="1.9722222222222223in"}
  Figure 48: Idle noise spectrum without activation for different overload points      
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image129.wmf){width="3.136111111111111in" height="1.9722222222222223in"}   ![](media/image130.wmf){width="3.136111111111111in" height="1.9722222222222223in"}
  Figure 49: Idle noise spectrum without activation with 1-bit dithering noise         
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image131.wmf){width="3.136111111111111in" height="1.9722222222222223in"}   ![](media/image132.wmf){width="3.136111111111111in" height="1.9722222222222223in"}
  Figure 50: Idle noise spectrum without activation with 2-bit dithering noise         
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  -------------- ------------------------- ----------------- ----------------- -------- -------- --------
                 overload point \[dBm0\]                                                         
                 3.0                       9.0               3.0               9.0      3        9
  bit rate       no dithering              1-bit dithering   2-bit dithering                     
  5.9 kbit/s     -205.8                    -205.8            -205.8            -205.8   -205.8   -205.8
  7.2 kbit/s     -100.1                    -94.1             -82.2             -76.2    -79.0    -73.0
  8.0 kbit/s     -98.4                     -92.4             -82.2             -76.2    -78.2    -72.2
  9.6 kbit/s     -205.8                    -205.8            -90.0             -84.0    -84.1    -78.1
  13.2 kbit/s    -96.4                     -90.4             -85.9             -79.9    -79.5    -73.5
  16.4 kbit/s    -205.8                    -205.8            -90.2             -84.2    -82.8    -76.8
  24.4 kbit/s    -205.8                    -205.8            -89.6             -83.6    -82.1    -76.1
  32.0 kbit/s    -205.8                    -205.8            -87.3             -81.3    -81.1    -75.1
  48.0 kbit/s    -205.8                    -205.8            -88.0             -82.0    -80.5    -74.5
  64.0 kbit/s    -205.8                    -205.8            -86.9             -80.9    -80.2    -74.2
  96.0 kbit/s    -205.8                    -205.8            -88.3             -82.3    -80.6    -74.6
  128.0 kbit/s   -205.8                    -205.8            -88.3             -82.3    -80.6    -74.6
  -------------- ------------------------- ----------------- ----------------- -------- -------- --------

Table 16: Idle noise levels without activation with dithering noise in
dB(A)

Again, neither in the spectral analysis of the noise floor shown in
Figure 48, Figure 49, and Figure 50 nor in the absolute level values
shown in Table 16, a violation of the requirements can be observed for
any wideband bit rate or overload point.

For the bit rates 9.6, 16.4, 24.4, 48.0, 64.0, 96.0, and 128.0 kbit/s,
the digital zero input is encoded to a digital zero output leading to
idle noise levels lower than -200 dB(A), which are outside the plotting
range in Figure 48. The other bit rates 5.9, 7.2, 8.0, 13.2, and
32.0 kbit/s, however, generate a non-zero output even for digital zero
input.

With dithering noise, the results for the two overload points are
shifted by 6 dB but otherwise show the same behavior.

###  Distortion vs. input level

The following results are produced by applying the measurement
instructions and requirements according to clause 8.8.2 of \[4\]. The
signal-to-distortion ratio is measured for a 1020 Hz sine with different
source levels. For levels -40 and -45 dBm0, the limits of 22.5 dB and
17.5 dB, respectively, are recommendations and not be regarded as a
failing result.

  ------------------------------------------------------------------------ ------------------------------------------------------------------------
  ![](media/image133.wmf){width="3.138888888888889in" height="1.9875in"}   ![](media/image134.wmf){width="3.138888888888889in" height="1.9875in"}
  Figure 51: Signal-to-distortion ratio for different input levels         
  ------------------------------------------------------------------------ ------------------------------------------------------------------------

The results of this analysis are shown in Figure 51. It can be observed
that for lower bit rates (red/gree curves) the signal-to-distortion
ratio slightly violates the tolerance scheme according to \[5\] at some
gain points when choosing the overload point to 3.0 dBm0. All other bit
rates pass the test..

###  Distortion vs. frequency

The following results are produced by applying the measurement
instructions and requirements according to clause 8.8.2 of \[4\] which
are extended with source frequencies above 1 kHz. The
signal-to-distortion ratio for different frequencies and constant input
level is measured.

  ------------------------------------------------------------------------ ------------------------------------------------------------------------
  ![](media/image135.wmf){width="3.138888888888889in" height="1.9875in"}   ![](media/image136.wmf){width="3.138888888888889in" height="1.9875in"}
  Figure 52: Signal-to-distortion ratio for different frequencies          
  ------------------------------------------------------------------------ ------------------------------------------------------------------------

The results of this analysis are shown in Figure 52. Again, the
signal-to-distortion ratio violates the tolerance scheme according to
\[5\] at lower bit rates (red/green/cyan curves) for the same reason as
above. All other bit rates pass the test.

EVS-Mode: Super-Wideband (SWB)
------------------------------

###  General

In super-wideband mode, a sampling rate of 32 kHz and all bit rates
(9.6, 13.2, 16.4, 24.4, 32.0, 48.0, 64.0, 96.0 and 128.0 kbit/s)
according to Table 1 of \[1\] were used. The two possible target
overload points 3.0 and 9.0 dBm0 were used by default for all analyses.

###  Frequency response with real speech

The following results are produced by applying measurement instructions
similar to clause 8.4.2 of \[4\] which are adapted to super-wideband by
replacing the source signal with a fullband version of the same file. To
simulate also the impact of level variations, additional overload points
of 21.0 and 39.0 dBm0 were also simulated. These overload points do not
represent a realistic conversion; they are only used for checking the
linearity of the codec and can be regarded as attenuations of 18.0 resp.
36.0 dB compared to the overload point 3.0 dBm0.

  ------------------------------------------------------------------------ ------------------------------------------------------------------------
  ![](media/image137.wmf){width="3.138888888888889in" height="1.9875in"}   ![](media/image138.wmf){width="3.138888888888889in" height="1.9875in"}
  ![](media/image139.wmf){width="3.138888888888889in" height="1.9875in"}   ![](media/image140.wmf){width="3.138888888888889in" height="1.9875in"}
  Figure 53: Frequency response for different overload points              
  ------------------------------------------------------------------------ ------------------------------------------------------------------------

The results of this analysis are shown in Figure 53. For the default and
extra overload points, the codec provides an accurate transmission
behavior for all bit rates.

The results for the 1/3^rd^ octave analysis are shown in Figure 54.

  --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------
  ![](media/image141.wmf){width="3.138888888888889in" height="1.9875in"}                                          ![](media/image142.wmf){width="3.138888888888889in" height="1.9875in"}
                                                                                                                  
  Figure 54: Frequency response EVS SWB in 1/3^rd^ Oct. for different overload points with P.501 speech signals   
  --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------

###  Frequency response with composite source signal (CSS)

The following results are produced by applying the measurement
instructions similar to clause 8.3.2 of \[4\] which is intended to be
reported only for informative reasons. The composite source according to
ITU-T P.501 \[6\] signal is used as a reference for the calculation.

  ------------------------------------------------------------------------ ------------------------------------------------------------------------
  ![](media/image143.wmf){width="3.138888888888889in" height="1.9875in"}   ![](media/image144.wmf){width="3.138888888888889in" height="1.9875in"}
  ![](media/image145.wmf){width="3.138888888888889in" height="1.9875in"}   ![](media/image146.wmf){width="3.138888888888889in" height="1.9875in"}
  Figure 55: Frequency response for different overload points              
  ------------------------------------------------------------------------ ------------------------------------------------------------------------

The results of this analysis are shown in Figure 55. For the default
overload points, the codec provides an accurate transmission behavior
for all bit rates.

###  Idle noise generated with activation and digital zero input

The following results are produced by applying measurement instructions
and requirements similar to clause 8.3.2 of \[4\] which are adapted to
super-wideband by replacing the source signal with a fullband version of
the same file. This includes an activation of the device under test with
a CSS burst before the measured idle segment.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image147.wmf){width="3.136111111111111in" height="1.9722222222222223in"}   ![](media/image148.wmf){width="3.136111111111111in" height="1.9722222222222223in"}
  Figure 56: Idle noise spectrum with activation for different overload points         
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  -------------- ------------------------- --------
                 overload point \[dBm0\]   
  bit rate       3.0                       9.0
  9.6 kbit/s     -97.8                     -107.7
  13.2 kbit/s    -92.2                     -91.3
  16.4 kbit/s    -106.1                    -106.1
  24.4 kbit/s    -111.7                    -108.9
  32.0 kbit/s    -82.3                     -90.9
  48.0 kbit/s    -112.4                    -110.1
  64.0 kbit/s    -108.0                    -111.7
  96.0 kbit/s    -110.6                    -112.2
  128.0 kbit/s   -111.2                    -115.7
  -------------- ------------------------- --------

Table 17: Idle noise levels with activation in dB(A) (requirement:
-57.0 dB(A))

Neither in the frequency representation shown in Figure 56 nor in the
absolute level values shown in Table 17, a violation of the requirements
according to \[5\] can be observed for any super-wideband bit rate.

###  Idle noise generated with activation and dithering noise

The original measurement was conducted with an input signal which
consists only of digital zeros. In order to analyze the impact of
non-zero samples, two different dithering noises were used instead as a
source signal. This dithering noise was created by randomly modifying
the last N bits of each 16-bit sample. By increasing N, the dithering
noise power increases. In this evaluation, N = 1 and N = 2 was used.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image149.wmf){width="3.136111111111111in" height="1.9722222222222223in"}   ![](media/image150.wmf){width="3.136111111111111in" height="1.9722222222222223in"}
  Figure 57: Idle noise spectrum with activation and 1-bit dithering noise             
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image151.wmf){width="3.136111111111111in" height="1.9722222222222223in"}   ![](media/image152.wmf){width="3.136111111111111in" height="1.9722222222222223in"}
  Figure 58: Idle noise spectrum with activation and 2-bit dithering noise             
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  -------------- ------------------------- ----------------- ----------------- ------- ------- -------
                 overload point \[dBm0\]                                                       
                 3.0                       9.0               3.0               9.0     3.0     9.0
  bit rate       no dithering              1-bit dithering   2-bit dithering                   
  9.6 kbit/s     -97.8                     -107.7            -90.4             -85.2   -84.5   -78.7
  13.2 kbit/s    -92.2                     -91.3             -89.5             -84.0   -83.1   -77.4
  16.4 kbit/s    -106.1                    -106.1            -90.1             -84.3   -83.3   -77.4
  24.4 kbit/s    -111.7                    -108.9            -90.0             -84.3   -82.7   -76.8
  32.0 kbit/s    -82.3                     -90.9             -90.9             -84.9   -82.7   -77.0
  48.0 kbit/s    -112.4                    -110.1            -89.6             -83.7   -82.3   -76.3
  64.0 kbit/s    -108.0                    -111.7            -89.7             -83.8   -82.3   -76.4
  96.0 kbit/s    -110.6                    -112.2            -90.2             -84.2   -82.4   -76.4
  128.0 kbit/s   -111.2                    -115.7            -90.2             -84.2   -82.5   -76.5
  -------------- ------------------------- ----------------- ----------------- ------- ------- -------

Table 18: Idle noise levels with activation and dithering noise in dB(A)

Neither in the frequency representations shown in Figure 57 and Figure
58, nor in the absolute level values shown in Table 18, a violation of
the requirements can be observed for any super-wideband bit rate or
overload point.

###  Idle Noise without Activation

The following results are produced by applying the tests without the
preceding activation sequence.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image153.wmf){width="3.136111111111111in" height="1.9722222222222223in"}   ![](media/image154.wmf){width="3.136111111111111in" height="1.9722222222222223in"}
  Figure 59: Idle noise spectrum without activation for different overload points      
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image155.wmf){width="3.136111111111111in" height="1.9722222222222223in"}   ![](media/image156.wmf){width="3.136111111111111in" height="1.9722222222222223in"}
  Figure 60: Idle noise spectrum without activation with 1-bit dithering noise         
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image157.wmf){width="3.136111111111111in" height="1.9722222222222223in"}   ![](media/image158.wmf){width="3.136111111111111in" height="1.9722222222222223in"}
  Figure 61: Idle noise spectrum without activation with 2-bit dithering noise         
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

  -------------- ------------------------- ----------------- ----------------- ------- ------- -------
                 overload point \[dBm0\]                                                       
                 3.0                       9.0               3.0               9.0     3.0     9.0
  bit rate       no dithering              1-bit dithering   2-bit dithering                   
  9.6 kbit/s     -205.8                    -205.8            -91.3             -85.3   -85.3   -79.3
  13.2 kbit/s    -92.9                     -86.9             -89.7             -83.7   -82.7   -76.7
  16.4 kbit/s    -205.8                    -205.8            -90.4             -84.4   -83.5   -77.5
  24.4 kbit/s    -205.8                    -205.8            -90.4             -84.4   -82.9   -76.9
  32.0 kbit/s    -95.2                     -89.2             -91.1             -85.1   -83.1   -77.1
  48.0 kbit/s    -205.8                    -205.8            -89.7             -83.7   -82.4   -76.4
  64.0 kbit/s    -205.8                    -205.8            -89.7             -83.7   -82.0   -76.0
  96.0 kbit/s    -205.8                    -205.8            -90.2             -84.2   -82.3   -76.3
  128.0 kbit/s   -205.8                    -205.8            -90.2             -84.2   -82.6   -76.6
  -------------- ------------------------- ----------------- ----------------- ------- ------- -------

Table 19: Idle noise levels without activation with dithering noise in
dB(A)

Again, neither in the frequency representations shown in Figure 59,
Figure 60, and Figure 61 nor in the absolute level values shown in Table
19, a violation of the requirements can be observed for any
super-wideband bit rate or overload point.

For all bit rates but 13.2 and 32.0 kbit/s, the digital zero input is
encoded to a digital zero output leading to idle noise levels lower than
-200 dB(A), which are outside the plotting range in Figure 59. These two
bit rates, however, generate a non-zero output even for digital zero
input.

With dithering noise, the results for the two overload points are
shifted by 6 dB but otherwise show the same behavior.

### Distortion vs. input level

The following results are produced by applying the measurement
instructions and requirements according to clause 8.8.2 of \[4\], which
are adapted to super-wideband by evaluating the distortion up to 14 kHz.
It measures the signal-to-distortion ratio for a 1020 Hz sine with
different source levels.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image159.wmf){width="3.134027777777778in" height="1.9819444444444445in"}   ![](media/image160.wmf){width="3.134027777777778in" height="1.9819444444444445in"}
  Figure 62: Signal-to-distortion ratio for different input levels                     
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

The results of this analysis are shown in Figure 62. At all bit rates
and gains, the signal-to-distortion ratio extends at least 40dB.

###  Distortion vs. frequency

The following results are produced by applying the measurement
instructions and requirements according to clause 8.8.2 of \[4\] which
are extended with source frequencies above 1 kHz and adapted to
super-wideband by evaluating the distortion up to 14 kHz. It measures
the signal-to-distortion ratio for different frequencies and constant
input level.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image161.wmf){width="3.134027777777778in" height="1.9819444444444445in"}   ![](media/image162.wmf){width="3.134027777777778in" height="1.9819444444444445in"}
  Figure 63: Signal-to-distortion ratio for different frequencies                      
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

The results of this analysis are shown in Figure 63. For all bit rates
and gains, the signal-to-distortion ratio extends at least 40dB, except
one frequency (about 8 kHz) for rate 16.4kbit/s (light blue curve).

EVS-Mode: Fullband (FB)
-----------------------

In fullband mode, a sampling rate of 48 kHz and all possible bit rates
(16.4, 24.4, 32.0, 48.0, 64.0, 96.0 and 128.0 kbit/s) according to
Table 1 of \[1\] were used. The two possible target overload points 3.0
and 9.0 dBm0 were used by default for all analyses.

### Frequency Response with real speech

The following results are produced by applying measurement instructions
similar to clause 8.4.2 of \[4\] which are adapted to fullband by
replacing the source signal with a fullband version of the same. To
simulate also the impact of level variations, additional overload points
of 21.0 and 39.0 dBm0 were also simulated. These overload points do not
represent a realistic conversion; they are only used for checking the
linearity of the codec and can be regarded as attenuations of 18.0 resp.
36.0 dB compared to the overload point 3.0 dBm0. The results of this
analysis are shown in Figure 64.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image163.wmf){width="3.134027777777778in" height="1.9847222222222223in"}   ![](media/image164.wmf){width="3.134027777777778in" height="1.9847222222222223in"}
  ![](media/image165.wmf){width="3.134027777777778in" height="1.9847222222222223in"}   ![](media/image166.wmf){width="3.134027777777778in" height="1.9847222222222223in"}
  Figure 64: Frequency response for different overload points                          
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

For lower codec rates (16.4 and 24.4 kbit/s, red/green curves), the
transmission characteristics show some slight degradations for
frequencies between 15 and 20 kHz.

### Frequency Response with composite source signal (CSS)

The following results are produced by applying the measurement
instructions similar to clause 8.3.2 of \[4\] which is intended to be
reported only for informative reasons. The composite source according to
ITU-T P.501 \[6\] signal is used as a reference for the calculation. The
results of this analysis are shown in Figure 65.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image167.wmf){width="3.134027777777778in" height="1.9847222222222223in"}   ![](media/image168.wmf){width="3.134027777777778in" height="1.9847222222222223in"}
  ![](media/image169.wmf){width="3.134027777777778in" height="1.9847222222222223in"}   ![](media/image170.wmf){width="3.134027777777778in" height="1.9847222222222223in"}
  Figure 65: Frequency response for different overload points                          
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

### Idle Noise with Activation

#### Idle noise generated with activation and digital zero input

The following results are produced by applying measurement instructions
and requirements similar to clause 8.3.2 of \[4\] which are adapted to
fullband by replacing the source signal with a fullband version of the
same file. This includes an activation of the device under test with a
CSS burst before the measured idle segment.

  ------------------------------------------------------------------------------ ---------------------------------------------------------------
  ![](media/image171.wmf){width="3.13125in" height="1.96875in"}                  ![](media/image172.wmf){width="3.13125in" height="1.96875in"}
  Figure 66: Idle noise spectrum with activation for different overload points   
  ------------------------------------------------------------------------------ ---------------------------------------------------------------

  -------------- ------------------------- --------
                 overload point \[dBm0\]   
  bit rate       3.0                       9.0
  16.4 kbit/s    -105.1                    -105.3
  24.4 kbit/s    -108.1                    -109.8
  32.0 kbit/s    -86.4                     -85.9
  48.0 kbit/s    -111.5                    -105.5
  64.0 kbit/s    -103.7                    -102.7
  96.0 kbit/s    -111.1                    -110.6
  128.0 kbit/s   -110.9                    -110.9
  -------------- ------------------------- --------

Table 20: Idle noise levels with activation in dB(A) (requirement:
-57.0 dB(A))

Neither in the frequency representation shown in Figure 66, nor in the
absolute level values shown in Table 20, a violation of the requirements
according to \[5\] can be observed for any fullband bit rate.

#### Idle noise generated with activation and dithering noise

The original measurement described in the previous section was conducted
with an input signal which consists only of digital zeros. In order to
analyze the impact of non-zero samples, two different dithering noises
were used instead as a source signal. This dithering noise was created
by randomly modifying the last N bits of each 16-bit sample. By
increasing N, the dithering noise power increases. In this evaluation,
N = 1 and N = 2 was used.

  -------------------------------------------------------------------------- ---------------------------------------------------------------
  ![](media/image173.wmf){width="3.13125in" height="1.96875in"}              ![](media/image174.wmf){width="3.13125in" height="1.96875in"}
  Figure 67: Idle noise spectrum with activation and 1-bit dithering noise   
  -------------------------------------------------------------------------- ---------------------------------------------------------------

  -------------------------------------------------------------------------- ---------------------------------------------------------------
  ![](media/image175.wmf){width="3.13125in" height="1.96875in"}              ![](media/image176.wmf){width="3.13125in" height="1.96875in"}
  Figure 68: Idle noise spectrum with activation and 2-bit dithering noise   
  -------------------------------------------------------------------------- ---------------------------------------------------------------

  -------------- ------------------------- ----------------- ----------------- ------- ------- -------
                 overload point \[dBm0\]                                                       
                 3.0                       9.0               3.0               9.0     3.0     9.0
  bit rate       no dithering              1-bit dithering   2-bit dithering                   
  16.4 kbit/s    -105.1                    -105.3            -89.1             -83.3   -82.6   -76.7
  24.4 kbit/s    -108.1                    -109.8            -89.2             -83.5   -82.3   -76.3
  32.0 kbit/s    -86.4                     -85.9             -88.4             -82.6   -82.0   -76.0
  48.0 kbit/s    -111.5                    -105.5            -88.8             -82.8   -81.6   -75.6
  64.0 kbit/s    -103.7                    -102.7            -87.9             -81.9   -81.5   -75.5
  96.0 kbit/s    -111.1                    -110.6            -89.6             -83.6   -81.9   -75.9
  128.0 kbit/s   -110.9                    -110.9            -89.6             -83.6   -81.9   -75.9
  -------------- ------------------------- ----------------- ----------------- ------- ------- -------

Table 21: Idle noise levels with activation and dithering noise in dB(A)

Neither in the frequency representations shown in Figure 67 and Figure
68, nor in the absolute level values shown in Table 21, a violation of
the requirements can be observed for any fullband bit rate or overload
point.

The results for the two overload points, however, show a different
behavior with respect to the same dithering noise power. This is
attributed to the different states of the codec depending on the
overload point specific scaling of the activation sequence. Therefore,
the next section describes the same measurement without activation.

### Idle Noise without Activation

The following results are produced by applying measurement instructions
and requirements of the previous section,3.4.2 but without the preceding
activation sequence.

  --------------------------------------------------------------------------------- ---------------------------------------------------------------
  ![](media/image177.wmf){width="3.13125in" height="1.96875in"}                     ![](media/image178.wmf){width="3.13125in" height="1.96875in"}
  Figure 69: Idle noise spectrum without activation for different overload points   
  --------------------------------------------------------------------------------- ---------------------------------------------------------------

  ------------------------------------------------------------------------------ ---------------------------------------------------------------
  ![](media/image179.wmf){width="3.13125in" height="1.96875in"}                  ![](media/image180.wmf){width="3.13125in" height="1.96875in"}
  Figure 70: Idle noise spectrum without activation with 1-bit dithering noise   
  ------------------------------------------------------------------------------ ---------------------------------------------------------------

  ------------------------------------------------------------------------------ ---------------------------------------------------------------
  ![](media/image181.wmf){width="3.13125in" height="1.96875in"}                  ![](media/image182.wmf){width="3.13125in" height="1.96875in"}
  Figure 71: Idle noise spectrum without activation with 2-bit dithering noise   
  ------------------------------------------------------------------------------ ---------------------------------------------------------------

  -------------- ------------------------- ----------------- ----------------- ------- ------- -------
                 overload point \[dBm0\]                                                       
                 3.0                       9.0               3.0               9.0     3.0     9.0
  bit rate       no dithering              1-bit dithering   2-bit dithering                   
  16.4 kbit/s    -205.8                    -205.8            -91.3             -85.3   -84.5   -78.5
  24.4 kbit/s    -205.8                    -205.8            -91.3             -85.3   -84.2   -78.2
  32.0 kbit/s    -94.5                     -88.5             -89.0             -83.0   -83.1   -77.1
  48.0 kbit/s    -205.8                    -205.8            -90.7             -84.7   -83.4   -77.4
  64.0 kbit/s    -205.8                    -205.8            -87.8             -81.8   -81.9   -75.9
  96.0 kbit/s    -205.8                    -205.8            -91.1             -85.1   -83.6   -77.6
  128.0 kbit/s   -205.8                    -205.8            -91.1             -85.1   -83.7   -77.7
  -------------- ------------------------- ----------------- ----------------- ------- ------- -------

Table 22: Idle noise levels without activation with dithering noise in
dB(A)

Again, neither in the frequency representations shown in Figure 69,
Figure 70 or Figure 71, nor in the absolute level values shown in Table
22, a violation of the requirements can be observed for any fullband bit
rate or overload point.

For all bit rates but 32.0 kbit/s, the digital zero input is encoded to
a digital zero output leading to idle noise levels lower than
-200 dB(A), which are outside the plotting range of Figure 69. These two
bit rates, however, generate a non-zero output even for digital zero
input.

With dithering noise, the results for the two overload points are
shifted by 6 dB but otherwise show the same behavior.

### Distortion vs. input level

The following results are produced by applying the measurement
instructions and requirements according to clause 8.8.2 of \[4\], which
are adapted to fullband by evaluating the distortion up to 14 kHz. It
measures the signal-to-distortion ratio for a 1020 Hz sine with
different source levels.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image183.wmf){width="3.134027777777778in" height="1.9847222222222223in"}   ![](media/image184.wmf){width="3.134027777777778in" height="1.9847222222222223in"}
  Figure 72: Signal-to-distortion ratio for different input levels                     
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

The results of this analysis are shown in Figure 72. At all bit rates
and gains, the signal-to-distortion ratio extends at least 40dB.

### Distortion vs. frequency

The following results are produced by applying the measurement
instructions and requirements according to clause 8.8.2 of \[4\] which
are extended with source frequencies above 1 kHz and adapted to fullband
by evaluating the distortion up to 14 kHz. It measures the
signal-to-distortion ratio for different frequencies and constant input
level. The results of this analysis are shown in Figure 73.

  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------
  ![](media/image185.wmf){width="3.134027777777778in" height="1.9847222222222223in"}   ![](media/image186.wmf){width="3.134027777777778in" height="1.9847222222222223in"}
  Figure 73: Signal-to-distortion ratio for different frequencies                      
  ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------

Conclusions
===========

This contribution introduces the results of several measurements of the
EVS codec using adapted tests originally intended for acoustic terminal
testing. Two versions of the codec were evaluated: the codec version
which was used in the selection phase; version 12.1 provides the current
release.

In narrowband mode, all bit rates pass all requirements of \[5\]. No
noticeable differences between both versionscould be observed.

EVS WB at 5.9, 7.2, and 8.0 kbit/s demonstrates lower than 40 dB
signal-to-distortion ratio (SDR) at certain frequencies with pure tones
(Figures 19,20, 51,52) in both, the codec version used in selection as
well as in version12.1.0. In version 12.1.0 this behavior is improved,
for rates above 8 kbps, the SDR extends to at least 40 dB with pure
tones (Figure 51, 52).

While the codec version used in the selection phase shows some
degradation in distortion at 9.6 kbit/s and 13.2 kbit/s, EVS SWB version
12.1.0 at all bit rates produces at least 40 dB signal-to-distortion
ratio (Figure 62, 63), except at 16.4 kbit/s and at one frequency (about
8 kHz \@16.4 kbit/s in Fig. 63).

Across all bitrates and for various operating bandwidths NB/WB/SWB, the
EVS codec version 12.1 exceeds the frequency response tolerance
requirements over an extended range of overload points when tested using
both real speech and composite source signal.

The fullband mode was introduced with the release version 12.1. Since no
requirements are available for this mode, results can only be reported.
However, besides some slight degradation in the frequency response
evaluations, the codec accurately performs on all tests.

References
==========

1.  3GPP TS 26.441: "EVS Codec General Overview".

2.  3GPP Tdoc S4-141011, "EVS overload point definition", Sony Mobile
    Communications, TSG SA4\#80 meeting, 4-8 August 2014, San Francisco,
    USA

3.  ITU-T Rec. G.100.1: "The use of the decibel and of relative levels
    in speechband telecommunications", 11/2001.

4.  3GPP TS 26.132: "Speech and video telephony terminal acoustic test
    specification (Release 12)".

5.  3GPP TS 26.131: "Terminal acoustic characteristics for telephony --
    Requirements"

6.  Recommendation ITU-T P.501: "Test signals for use in telephonometry"

7.  3GPP TS 26.442: "Codec for Enhanced Voice Services (EVS); ANSI C
    code (fixed-point) (Release 12)"
