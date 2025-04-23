**Source:** Nokia, Ericsson

**Title: Additional information on AMR-WB+ performance**

Agenda item: 8 {#agenda-item-8 .list-paragraph}
==============

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Summary {#summary .list-paragraph}
=======

This document gives additional information on the AMR-WB+ audio codec
performance in various operation conditions. AMR-WB+ with flexible codec
control is compared against Enhanced aacPlus (EAAC+) codec available
from Coding Technologies in low rate applications using MUSHRA
methodology.

Results indicate that the flexible codec control with increased audio
bandwidth improves the subjective quality of the AMR-WB+ codec
especially in music content.

Introduction
============

A subjective listening tests have been conducted to characterize the
performance of the AMR-WB+. Tests have been conducted using the same
high quality procedures that have been used to perform the official
selection tests. Two listening laboratories conducted tests
independently. The results from Nokia listening test laboratory in
Finland and Ericsson listening test laboratory in Sweden were combined.
Both laboratories performed testing with the same material.

Source material
===============

Tests have been performed using the material Nokia and Ericsson provided
for the 3GPP PSS/MMS audio codec selection phase testing. Two different
sets of material were utilised. Both sets consisted of 12 test and 4
practice items. Same material was used in both test laboratories.

Processing
==========

Processing of the source material has been done according to the low
rate audio selection test and processing plan \[1\]. Only the tested
codecs were different. Main processing has been done using concatenated
material. All the processing has been done using the very same tools
(up/down sampling, file concatenation etc.) that were used in the
processing phase of the official low rate test A4.

Test conditions
===============

  ----------------------------- ---- --------------------------------------------------------------------------------------------------------------------------------------------------------
  **Main Codec Conditions**          

  Candidates                    3    AMR-WB+\@14kbps, 18kbps & 24kbps\
                                     E-AAC+ \@16 kbps, 18 kbps & 24 kbps

  Use case                      1    A (PSS)

  Error Conditions              1    No errors

  Mono/Stereo                   1    Stereo

                                     

  **Codec references**               

  Codec references              1    AMR-WB+ \@24 kbps use case A

  Input sampling rate           1    24 kHz

  Input characteristics              

  Number of input channels      2    Stereo

  Number of output channels     2    Stereo

                                     

  **Other references**               

  Open Reference                1    Original signal

  Hidden Reference              1    Original signal

  Anchors                       2    3.5 kHz and 7 kHz low-pass filtered original signal

                                     

  **Common Conditions**              

  Stimulus type                      Sound item

  Radio Channels                0    Clean

  Number of audio items         12   

  Input sampling rate                48 kHz

  Number of input channels      2    Stereo

  Output sampling rate               Unspecified

  Number of output channels     2    Stereo

  Listening Level               1    To be chosen by subject

  Listening laboratories        2    Nokia and Ericsson listening test laboratories

  Listeners                     46   Experienced listeners (Nokia 26, Ericsson 20)

  Presentation randomizations   46   One for each listener

  Rating Scale                  1    Continuous quality scale

  Listening System              1    Binaural high-quality headphones

  Listening Environment              Room Noise: Hoth Spectrum at 30dBA (as defined by ITU-T, Recommendation P.800, Annex A, section A.1.1.2.2.1 Room Noise, with table A.1 and Figure A.1)
  ----------------------------- ---- --------------------------------------------------------------------------------------------------------------------------------------------------------

Table 1: Overview of the test conditions for low rate tests (A4)

Listening sessions
==================

Nokia listening test laboratory
-------------------------------

### Presentation sequences

All listeners listened their sound items and each trial of the item in
unique order.

### Listeners

All the listeners were native finish speakers with prior experience in
MUSHRA test methodology. They were all tested before listening with
audiometer to have normal hearing (to fulfil ISO Standard 389
requirements).

### Listening environment

Listeners were placed in high quality, acoustically isolated booths. Six
identical booths with internal dimensions of 1.4 x 1.1 x 2.1m were used.
The background noise-rating curve of each booth fulfils the ISO NR15
requirement. The reverberation times within the booths are \<300ms above
315Hz one-third octave bands. No discernible flutters are audible within
the booths \[2\].

### Environmental noise

Environmental noise was fed into the booths with the required Hoth
spectrum to represent typical room noise at the required 30dBA level (as
defined by ITU-T, Recommendation P.800 \[4\]). Two loudspeaker units
(type: Genelec 1029A) per booth were used. Speakers were positioned so
that the sound pressure level was 30 dBA above the centre of the seat of
subject\'s chair.

### Testing facility

The listening test was controlled by remote PCs with a keyboard, mouse
and an LCD screen in the booths. Six machines were used to play the
samples to the listeners and to collect their answers. Each one is
furnished with a high quality digital sound card (type: RME DIGI 96/8
PRO), providing 44.1kHz or 48kHz output at a resolution of 24 bits. The
digital audio output signals were subsequently fed to a Studer D19 24bit
multi-channel digital to analogue converter employing an AES/EBU bus. A
Symmetrix 304 headphone amplifier was used. Samples were presented
binaurally to the listeners over high quality Sennheiser HD580
headphones.

Ericsson listening test laboratory
----------------------------------

### Presentation sequences

All listeners listened their sound items and each trial of the item in
unique order.

### Listeners

The listening panel was selected from experienced listeners inside
Ericsson. A pre-screening procedure was used were previous performance
in intermediate quality audio listening tests served as an indication of
the listeners' ability to judge anchors and references in a correct way,
as well as the ability to repeatedly grade in a consistent manner. The
listeners, both male and female, were between 25 to 45 years of age and
had all had previous experience of audio listening tests using the
MUSHRA methodology.

### Listening environment

The listening environments were two listening labs, which both conformed
to the standard requirements.

### Environmental noise

Environmental noise was fed into the booths with the required Hoth
spectrum to represent typical room noise at the required 30dBA level (as
defined by ITU-T, Recommendation P.800 \[3\]).

### Testing facility

Open-back circum-aural headphones were used (Sennheiser HD600) and the
listeners could individually adjust the listening level to their
preference. The audio was fed from the computer to the listener using
M-audio USB Duo sound cards.

The MUSHRA software has been developed in-house. It has a similar GUI as
the CRC-SEAQ software shown in the test plan although there is a
possibility to show the waveform of the current test item. The waveform
is rendered from the open reference clip, thus showing no information
about the encoded clips. The software performs both inter-item and
intra-item randomization of the test sequence, and provides a raw output
of the test results into individual listener output files.

AMR-WB+ codec
=============

The flexible control of AMR-WB+ is utilised in the experiment. The core
and stereo rates and internal sampling frequency (ISF) are set according
to Table 2. To compare the performance of the flexible codec control the
configuration utilised in PSS/MMS codec selection is included.

  ------- ----------------------- --------------------------------------------------- ------------ ---------
          **Codec**               **Core**                                            **Stereo**   **ISF**
  **1**   AMR-WB+ 14kbps          10.4                                                3.6          25.6
  **2**   AMR-WB+ 18kbps          13.6                                                4.4          25.6
  **3**   AMR-WB+ 24kbps          16.8                                                4.4          28.8
  **4**   AMR-WB+ 24 kbps (PSS)   Configuration utilised in PSS/MMS selection tests                
  ------- ----------------------- --------------------------------------------------- ------------ ---------

Table 2: AMR-WB+ codec configuration

Test results
============

Results in numerical format are given in Table 3, and in graphical
format in Figure 1.

  -------- ---------------------- ----------- --------- ------- --------- -----------
           **Condition**          **Music**   **SoM**   **S**   **SbM**   **Total**
  **1**    Direct                 98.93       98.77     99.28   98.68     98.98
  **2**    Low-pass (BW=7.0kHz)   50.54       53.39     55.36   56.17     53.56
  **3**    Low-pass (BW=3.5kHz)   27.03       28.91     29.91   31.85     29.11
  **4**    EAAC+ 16kbps           57.65       55.23     48.62   51.25     53.17
  **5**    EAAC+ 18kbps           63.26       63.09     53.72   55.72     58.79
  **6**    EAAC+ 24kbps           82.37       77.27     67.95   68.57     74.41
  **7**    AMR-WB+ 14kbps         53.27       54.63     56.66   65.38     56.64
  **8**    AMR-WB+ 18kbps         64.35       66.60     68.65   74.10     67.78
  **9**    AMR-WB+ 24kbps         73.62       77.75     79.13   78.67     76.99
  **10**   AMR-WB+ 24kbps (PSS)   64.63       70.98     74.52   77.78     71.18
  -------- ---------------------- ----------- --------- ------- --------- -----------

Table 3: A4 test results in numerical format (46 listeners)

![](media/image1.wmf){width="7.136111111111111in"
height="4.579861111111111in"}Figure 1: Overall A4 test results in
graphical format (46 listeners)

Conclusion
==========

Test results indicate that the AMR-WB+ with flexible codec control
provides significant performance improvement. Compared to the AMR-WB+ 24
kbps stereo mode utilised in the PSS/MMS audio codec selection tests,
the 24 kbps mode with higher internal sampling frequency, and thus, with
higher audio bandwidth, provides significantly better audio quality. The
results also indicate that the performance of AMR-WB+ e.g. in music does
not saturate at low rates. This applies for both mono and stereo
application. Hence, flexible codec control proves to be useful.

References
==========

\[1\] S4-030824 "Low-Rate Audio Selection Test and Processing Plan"

\[2\] M. Kylliäinen et al.; "Compact high performance listening spaces."
Euronoise, Naples, 2003.

\[3\] ITU-T, Recommendation P.800
