######### Source: Coding Technologies

**Title: Characterization test phase 2, settings used for Enhanced
aacPlus**

**Agenda Item: 13.2**

**Document for: Information**

####### Introduction

This document outlines the simulation setup that has been used for the
processing of the test vectors for the Enhanced aacPlus codec in the
course of the characaterization test phase 2 \[1\].

**Simulation setup**

To be able to embed the encoding and decoding into the simulation chain
as discussed according during SA-4\#35 and the succeeding telecons and
agreements via email, an RFC 3640 compliant bistream format conversion
tools has been provided by Fraunhofer IIS. The following figure shows
the simulation chain setup:

The building blocks can be described as follows:

1.  The 3GPP floating point encoder according to \[2\] has been used to
    produce 3GP file format bitstreams.

2.  A 3GPP file format to RTP RFC3640 conversion tool converts the 3GPP
    file to a RFC3640 formatted - RTP stream.

3.  A modified (bugfixed) version of the error insertion device based on
    \[4\] has been provided by Siemens to simulate the channel errors.

4.  A RFC3640 RTP stream to error pattern file conversion tool analyses
    the distorted RTP stream and writes out a respective error pattern
    file on audio frame level.

5.  The 3GPP fixed-point decoder \[3\] reads in the non-distorted 3GPP
    file as well as the audio frame error pattern file which finally
    results in the decoded error prone audio output.

####### Packetization configuration

For the RFC 3640 packetization configuration the following parameters
have been chosen:

-   1 access unit per RTP packet

-   the following interleaving pattern (interleaving 46 access unites):
    1 27 8 34 15 41 22 3 29 10 36 17 43 24 5 31 12 38 19 45 26 7 33 14
    40 21 2 28 9 35 16 42 23 4 30 11 37 18 44 25 6 32 13 39 20 0

The interleaving leads to a delay of 46 audio frames. Given the
framelength of 2048 samples and a sampling rate of 48 kHz this
corresponds to a delay of 1,96 sec.

For the bitrate overhead calculation, it was agreed to assume ROHC to
require 8 bytes for the IP overhead for one SDU. The RFC 3640 protocol
furthermore requires 2 bytes header length per SDU and another 2 bytes
per AU in one SDU. This results in an overall bitrate overhead of 48000
/ 2048 \* 12 bytes = 2250 bit/sec. This bitrate overhead has been
substracted from the gross bitrate which results in the net bitrate that
has been used to configure the encoder for all test cases.

The 40 kbit/s test case has been a special case since it was realized
that the bitrate border for usage of the Parametric Stereo encoding tool
has been chosen too low. Hence it was found beneficial to run the
encoder at a net bitrate of 35,99 kbit/s, which means that the encoder
has effectively been run at a gross bitrate of 38,249 kbit/s.

####### Conclusions

All above executables and configurations have been provided as Win32
executables and accormpanying Bash-Shell Scripts. The processing over
the selected material and testcases according to \[1\] has been
independantly performed and cross-checked with the mirror processing
lab. Since all resulting test vectors could be verifed with exact
matching MD5-sums it can be concluded that the processing was done
correctly.

####### References

> \[1\] S4-050440 "PSS/MMS/MBMS Audio Codec Characterization Test Plan
> Version 0.7"
>
> \[2\] TS 26.410, 6.3.0 "General audio codec audio processing
> functions; Enhanced aacPlus general audio codec; Floating-point ANSI-C
> code"
>
> \[3\] TS 26.411, 6.1.0 "General audio codec audio processing
> functions; Enhanced aacPlus general audio\
> codec; Fixed-point ANSI-C code"

\[4\] S4-AHVIC036 "Offline Simulator for RTP/IP over UTRAN"

> []{.underline}
>
> []{.underline}

[]{.underline}
