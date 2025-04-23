**Title: PSS/MMS High-Rate Audio Selection Test and Processing**

**Plan Version 2.2.0**

**Source: Editor**[^1]

Contents

[4](#status-of-document)

[5](#introduction)

[5](#responsibilities)

[6](#contact-names)

[7](#codecs-anchors-and-references)

[7](#candidate-and-reference-codecs)

[7](#anchors-and-references)

[8](#references-and-conventions)

[8](#reference-documents)

[8](#__RefHeading___Toc50525844)

[9](#test-material)

[9](#material-selection-panel)

[9](#training-material)

[10](#information-relevant-to-all-experiments)

[10](#general-technical-notes)

[10](#testing-methodology)

[10](#error-patterns-and-error-conditions)

[10](#training-phase)

[10](#selection-of-subjects)

[10](#screening-of-subjects)

[12](#description-of-listening-tests)

[12](#test-at-32-kbits-stereo)

[12](#test-at-48-kbits-stereo)

[13](#test-at-32-kbits-stereo-with-frame-loss)

[13](#material)

[13](#experimental-design)

[13](#opinion-scale)

[13](#processing)

[13](#duration-of-the-experiment)

[14](#votes-per-condition)

[14](#randomizations)

[15](#processing-1)

[15](#main-processing)

[15](#concatenation-of-material)

[15](#processing-of-anchor-conditions)

[15](#candidate-and-reference-codec-processing)

[16](#post-processing)

[16](#up-sampling)

[16](#split-up-of-processed-material)

[16](#blinding-of-material)

[17](#annex-a-listeners-instructions)

[17](#training-phase-1)

[17](#blind-grading-phase)

[19](#annex-b-file-formats-naming-conventions-directory-structures-platforms)

[19](#b-1-file-formats)

[19](#b-2-computer-platform)

[19](#b-3-directory-structure)

[19](#b-4-file-naming)0 Status of document 1 Introduction 1.1
Responsibilities 1.2 Contact Names 2 Codecs, Anchors and References 2.1
Candidate and Reference codecs 2.2 Anchors and references 3 References
and Conventions 3.1 Reference Documents 3.2 Key Acronyms 4 Test Material
4.1 Material selection panel 4.2 Training material 5 Information
relevant to all Experiments 5.1 General Technical Notes 5.2 Testing
methodology 5.3 Error Patterns and Error Conditions 5.4 Training phase
5.5 Selection of subjects 5.5.1 Screening of subjects 6 Description of
listening tests 6.1 Test at 32 kbit/s stereo 6.2 Test at 48 Kbit/s
stereo 6.3 Test at 32 Kbit/s stereo with frame loss 6.4 Material 6.5
Experimental Design 6.6 Opinion Scale 6.7 Processing 6.8 Duration of the
Experiment 6.9 Votes Per Condition 6.10 Randomizations 7 Processing 7.1
Main processing 7.1.1 Concatenation of material 7.1.2 Processing of
anchor conditions 7.1.3 Candidate and reference codec processing 7.2
Post-processing 7.2.1 Up-sampling 7.2.2 Split-up of processed material
7.3 Blinding of material Annex A: Listeners Instructions 1 Training
phase 2 Blind grading phase Annex B: File formats, Naming conventions,
Directory structures, Platforms B-1 File formats B-2 Computer platform
B-3 Directory structure B-4 File naming

Status of document
==================

> V 2.2.0:

-   Up-to-date version incorporating changes due to limited candidate
    delivery

-   Includes changes in item selection process according to Oct. 7
    telecon agreement

-   Updated assignment of volunteering organizations for processing
    scripts

Introduction
============

This document contains the complete set of experimental designs for the
selection phase of the PSS/MMS high-rate audio codec selection.

Various types of music material will be used in the testing process.

A summary of the experiments to be conducted can be found in table 1-1.
Please note that experiments at 24 kbit/s in both stereo and mono are
conducted in the course of the low-rate selection test. The selection
process in the high-rate range will re-use the subjective testing
results obtained in those experiments.

Table 1‑1: Experiments for high-rate codec selection

  ---------- -------------------------------------------------- ------------------------------------------------- ------------------------------------------- ----------------------- ------------------ ------------- -----------
  **Exp.**   **Operational mode**                               **\#Codecs in test**                              **\# reference codecs**                     **\#Anchors in test**   **\#References**   **\#items**   **Total**
  **1**      **32 kbps, stereo**                                **2(use case B encoder)**                         **2, incl. RealAudio @ 32 kbit/s stereo**   **2**                   **1**              **12**        **84**
  **2**      **48 kbps, stereo**                                **2(use case B encoder)**                         **2, incl. RealAudio @ 48 kbit/s stereo**   **2**                   **1**              **12**        **84**
  **3**      **32 kbps, stereo, 1% and 3% random frame loss**   **4 (2 candidates at 2 frame loss rates each)**   **2 (AAC-LC at 2 frame loss rates)**        **2**                   **1**              **12**        **108**
  ---------- -------------------------------------------------- ------------------------------------------------- ------------------------------------------- ----------------------- ------------------ ------------- -----------

Section 2 provides a list of candidate and reference codecs used in the
experiments.

Section 3 provides a list of reference documents and contact names for
any question related to the test plan.

Section 5 gives an overview of the audio material required for the
testing.

Sections 6 contains the test plans for each experiment.

The specification of the processing functions of the audio material is
included in section 7

Annex A contains English language examples of instructions for the
listening subjects for the MUSHRA test methodology used in the
experiments.

Annex B presents the filename convention.

Responsibilities
----------------

The processing will be done by the host-lab (T-Systems), reproduced by
the mirror host lab (Audio Research Labs) and verified by the
candidates. The funding for the Selection and the characterization tests
will be equally shared between the proponents.

T-Systems will serve as host laboratory and Audio Research Labs will
serve as the mirror host laboratory. The host laboratory will have the
following responsibilities:

-   Receive candidate testing material after the call for the material.

-   

-   Receive executables of the candidate codecs from the codec
    proponents.

-   Receive executables of the reference codecs.

-   Generate FER pattern file after receipt of the random generator
    seed.

-   Process reference, anchor and codec conditions (including
    re-sampling to sampling frequency of original material) for all
    proposed material.

-   Cross-check the processing between the host laboratories and the
    codec proponents: provide the processed material to the codec
    proponents who cross-check.

-   Prepare final testing and training material based on the indications
    from the material selection entity.

-   Assemble the final distribution of the processed material to the
    listening laboratories, which includes blinding of the material.

The selection experiments for each candidate codec are run by two
listening laboratories in parallel, as shown in Table 1-2.

Table 1‑2: Allocation of sub-experiments to the Listening Laboratories

  --------- ------ ------ ------ ------ ------ ------ ---------- ------
  Exp.      Lab1   Lab2   Lab3   Lab4   Lab5   Lab6   Total      Size
  LL ID     TS     NT     FT     DY     NK     ER     Per Exp.   
  1         X                    X                    2          
  2                x                    x             2          
  3                       x                    x      2          
  Totals:   1      1      1      1      1      1      6          
  --------- ------ ------ ------ ------ ------ ------ ---------- ------

> (Legend: T-Systems (TS), NTT-AT (NT), France Telecom R&D (FT),
> Dynastat (DY), Nokia (NK),\
> Ericsson (ER)

Each listening lab will be asked to provide a full report of the
experiments performed. The test results will be included in spreadsheets
prepared for that purpose. Any deviations from the specifications
contained in this document will be documented along with the results.

The test results will then be combined by the Global Analysis Laboratory
(Audio Research Labs) and presented to SA4.

Contact Names
-------------

\<list contact names\>

Codecs, Anchors and References
==============================

Candidate and Reference codecs
------------------------------

The following table provides an overview of the candidate codec
participating in the PSS/MMS high-rate audio selection tests.

+--------+----------------+------------------+------------------+
| **\#** | **Codec name** | **Providing      | **Contact**      |
|        |                | O                |                  |
|        |                | rganization(s)** |                  |
+--------+----------------+------------------+------------------+
| 1      | aacPlus        | Coding           | [k               |
|        |                | Technologies/\   | unz\@codingtechn |
|        |                | NEC              | ologies.com](mai |
|        |                |                  | lto:kunz@CODINGT |
|        |                |                  | ECHNOLOGIES.COM) |
|        |                |                  |                  |
|        |                |                  | [frederic.gabi   |
|        |                |                  | n\@nectech.fr](m |
|        |                |                  | ailto:Frederic.G |
|        |                |                  | abin@nectech.FR) |
+--------+----------------+------------------+------------------+
| 2      | CT             | Coding           | [k               |
|        |                | Technologies     | unz\@codingtechn |
|        |                |                  | ologies.com](mai |
|        |                |                  | lto:kunz@CODINGT |
|        |                |                  | ECHNOLOGIES.COM) |
+--------+----------------+------------------+------------------+

The reference codecs are listed in the following table.

+--------+----------------+------------------+------------------+
| **\#** | **Codec name** | **Providing      | **Contact**      |
|        |                | O                |                  |
|        |                | rganization(s)** |                  |
+--------+----------------+------------------+------------------+
| 3      | AAC            | Fraunhofer       | <B               |
|        |                |                  | ernhard.grill@ii |
|        |                |                  | s.fraunhofer.de> |
|        |                |                  |                  |
|        |                |                  | <Joh             |
|        |                |                  | annes.hilpert@ii |
|        |                |                  | s.fraunhofer.de> |
+--------+----------------+------------------+------------------+
| 4      | RealAudio      | RealNetworks     | Greg Conklin     |
|        |                |                  | <                |
|        |                |                  | gregc@real.com>\ |
|        |                |                  | Jeremy Worley    |
|        |                |                  | <j               |
|        |                |                  | worley@real.com> |
+--------+----------------+------------------+------------------+

Anchors and references
----------------------

Besides the items encoded with the candidate and reference codecs,
anchor and reference items will be included in the tests. Their purpose
is to normalize the tests and to make them more comparable across
different realizations.

In the experiments, two anchors will be used with lowpass filtered
original signal. Also included is the uncoded original signal, once as
open and once as hidden reference.

  -------- ------------------ ------------------- ---------------------------
  **\#**   **Type**           **Specification**   **Channel type**
  1        Anchor             3.5 kHz Lowpass     Mono, stereo at 48 kbit/s
  2        Anchor             7.0 kHz Lowpass     Mono, stereo at 48 kbit/s
  6        Hidden Reference   Original signal     Mono/Stereo
  7        Open Reference     Original signal     Mono/Stereo
  -------- ------------------ ------------------- ---------------------------

References and Conventions
==========================

Reference Documents
-------------------

  ------- ------------------------------ --------------------------------------------------------------------------------------
  \[I\]   RECOMMENDATION ITU-R BS.1534   Method for the subjective assessment of intermediate quality level of coding systems
  ------- ------------------------------ --------------------------------------------------------------------------------------

Test Material
=============

The test material will be composed following a similar approach as in
MPEG audio codec standardization. First, a call will be sent out for
stereo test material according to a number of generic audio signal
categories. Then, an independent selection entity (FTR&D) will identify
12 critical items, which are representative for assumed typical
application scenarios such as music streaming, video soundtracks, sports
commentary, commercials, news, out of the categories to be used in the
experiments.

Original material shall always be in stereo and sampled at 48kHz.

The selection panel will identify, based on material coded by the
candidate and reference codecs, a set of critical test items covering
all the following generic audio signal categories with a focus on the
music categories:

-   Pop, with and/or without vocals

-   Classic, with and/or without vocals

-   Single instruments

-   a capella vocals, solo and/or choir

-   Mixed speech and music

-   Speech with and/or without background noise

The approximate lengths in time of the items will be 10s at a maximum.

Material selection panel
------------------------

The selection entity is formed by the following organizations:

-   Organizations TBA

All 3GPP members are invited to submit test material to the host lab.
The submitting organization shall assign the items to the
above-mentioned audio signal categories. The host lab will blind the
material and provide it to the material selection entity after
encoding/decoding it.

This ensures the selection is based on items whose origin is not
revealed to the selection entity.

The host lab will further maintain and report to SA4 a list indicating
the number of proposed items per submitting organization.

In case the submitted material is insufficient/inadequate to conduct the
tests, the selection entity will add the missing test items.

The selection entity will provide SA4 with a report about the selection
process.

Training material
-----------------

Limited material will be used in the training phase in which the
subjects familiarize with the testing methodology and environment.

The training will be conducted with four sound items. These items will
be identified by the selection entity and shall not be re-used in the
blind grading phase. The training phase shall be executed as a separate
short MUSHRA session.

Information relevant to all Experiments
=======================================

General Technical Notes
-----------------------

Any and all deviations from the specifications contained in this
document must be documented and submitted to TSG-SA-WG4 along with the
experimental results.

For all experiments, subjects should be seated in a quiet environment;
30dBA Hoth Spectrum (as defined by ITU-T, Recommendation P.800, Annex A,
section A.1.1.2.2.1 Room Noise, with table A.1 and Figure A.1) measured
at the head position of the subject. This will help ensure consistency
between the different subjects in the same laboratory as well as across
the different laboratories in which these experiments will be performed.

The test stimuli will be presented to the subjects over headphones
meeting one of the following requirements:

1\) Binaural listening using closed-back, supra-aural headphones;

2\) Binaural listening using open-back, circum-aural headphones.

Testing methodology
-------------------

The testing is carried out according to MUSHRA methodology \[1\], which
is suitable for evaluation of intermediate audio quality and gives
accurate and reliable results.

The labs carrying out the testing should have experience with the MUSHRA
method from earlier exercises.

The MUSHRA test method applied here uses the original unprocessed
material with full bandwidth as the reference signal (which is also used
as a hidden reference), a number of hidden anchors, the conditions of
the codec under test as well as the reference conditions with which the
codec under test is to be compared.

Error Patterns and Error Conditions
-----------------------------------

Error conditions will be applied in experiment 5 according to document
S4-030433.

Training phase
--------------

Prior to the actual testing a training phase is carried out in which the
test subjects are familiarized with testing methodology and environment.
The training is done following the same MUSHRA methodology as the actual
test, though limited to four trials.

The training is based on the same codec, anchor and reference conditions
as the blind grading phase.

Selection of subjects
---------------------

The selection of subjects follows the guidelines given in \[1\].

In particular, it is recommended that experienced listeners should be
used. These listeners should have some experience in listening to sound
in a critical way. Such listeners will give a more reliable result more
quickly than non-experienced listeners.

### Screening of subjects

There is sometimes a reason for introducing a rejection technique either
before (pre-screening) or after (post-screening) the real test. In some
cases both types of rejections might be used. Here, rejection is a
process where all judgements from a particular subject are omitted.

Any type of rejection technique, not carefully analysed and applied, may
lead to a biased result. It is thus extremely important that, whenever
elimination of data has been made, the test report clearly describes the
criterion applied.

#### Pre-screening of subjects

The listening panel should be composed of experienced listeners, in
other words, people who understand and have been properly trained in the
described method of subjective quality evaluation. These listeners
should:

-   have experience in listening to sound in a critical way;

-   have normal hearing (ISO Standard 389 should be used as a
    guideline).

The training procedure might be used as a tool for pre-screening.

#### Post-screening of subjects

Post-screening methods can be roughly separated into at least two
classes:

-   one is based on the ability of the subject to make consistent
    repeated gradings;

-   the other relies on inconsistencies of an individual grading
    compared with the mean result of all subjects for a given item.

It is recommended to look to the individual spread and to the deviation
from the mean grading of all subjects.

The aim of this is to get a fair assessment of the quality of the test
items.

If few subjects use either extreme end of the scale (excellent, bad) and
the majority are concentrated at another point on the scale, these
subjects could be recognized as outliers and might be rejected.

Due to the fact that "intermediate quality" is tested, a subject should
be able to identify the coded version very easily and therefore find a
grade which is in the range of the majority of the subjects. Subjects
with grades at the upper end of the scale are likely to be less critical
and subjects who have grades only at the lowest end of the scale are
likely to be too critical. By rejecting these extreme subjects a more
realistic quality assessment is expected.

The methods are primarily used to eliminate subjects who cannot make the
appropriate discriminations. The application of a post-screening method
may clarify the tendencies in a test result. However, bearing in mind
the variability of subjects' sensitivities to different artefacts,
caution should be exercised.

Taking into account the size of the listening panel used throughout the
experiments, the effects of any individual subject's grades is low and
so the need to reject a subject's data is greatly diminished.

Description of listening tests
==============================

Test at 32 kbit/s stereo
------------------------

  ----------------------------- ---- --------------------------------------------------------------------------------------------------------------------------------------------------------
  Main Codec Conditions              
  Candidates                    2    2 candidates, use case B encoder each
  Error Conditions                   No errors
  Applications                       32 kbit/s stereo
                                     
  References:                        
  Codec references              1    AAC-LC
  Other references              1    RealAudio, for information purposes only
  Open Reference                1    Original signal
  Hidden Reference              1    Original signal
  Anchors                       2    3.5 kHz and 7 kHz band-limited original signal
                                     
  Common Conditions                  
  Number of test items          12   
  Listening Level                    To be chosen by subject
  Listeners                     15   Experienced listeners
  Presentation randomizations   15   One per listener
  Rating Scale                       Continuous quality scale
  Replications                  2    The experiment covers all candidate codecs, 2 independent test sites
  Listening System                   Binaural high-quality headphones
  Listening Environment              Room Noise: Hoth Spectrum at 30dBA (as defined by ITU-T, Recommendation P.800, Annex A, section A.1.1.2.2.1 Room Noise, with table A.1 and Figure A.1)
  ----------------------------- ---- --------------------------------------------------------------------------------------------------------------------------------------------------------

Test at 48 Kbit/s stereo 
------------------------

  ----------------------------- ---- --------------------------------------------------------------------------------------------------------------------------------------------------------
  Main Codec Conditions              
  Candidates                    2    2 candidates, use case B encoder each
  Error Conditions                   No errors
  Applications                       48 kbit/s stereo
                                     
  References:                        
  Codec references              1    AAC-LC
  Other references              1    RealAudio, for information purposes only
  Open Reference                1    Original signal
  Hidden Reference              1    Original signal
  Anchors                       2    3.5 kHz and 7 kHz band-limited original signal
                                     
  Common Conditions                  
  Number of test items          12   
  Listening Level                    To be chosen by subject
  Listeners                     15   Experienced listeners
  Presentation randomizations   15   One per listener
  Rating Scale                       Continuous quality scale
  Replications                  2    The experiment covers all candidate codecs, 2 independent test sites
  Listening System                   Binaural high-quality headphones
  Listening Environment              Room Noise: Hoth Spectrum at 30dBA (as defined by ITU-T, Recommendation P.800, Annex A, section A.1.1.2.2.1 Room Noise, with table A.1 and Figure A.1)
  ----------------------------- ---- --------------------------------------------------------------------------------------------------------------------------------------------------------

Test at 32 Kbit/s stereo with frame loss
----------------------------------------

  ----------------------------- ---- --------------------------------------------------------------------------------------------------------------------------------------------------------
  Main Codec Conditions              
  Candidates                    2    Use case A encoder
  Error Conditions              2    1% and 3% frame loss, random
  Applications                       32 kbit/s stereo
                                     
  References:                        
  Codec references              2    AAC-LC at 1% and 3% frame loss, random
  Other references                   None
  Open Reference                1    Original signal
  Hidden Reference              1    Original signal
  Anchors                       3    3.5 kHz and 7 kHz band-limited original signal
                                     
  Common Conditions                  
  Number of test items          12   
  Listening Level                    To be chosen by subject
  Listeners                     15   Experienced listeners
  Presentation randomizations   15   One per listener
  Rating Scale                       Continuous quality scale
  Replications                  2    The experiment covers all candidate codecs, 2 independent test sites
  Listening System                   Binaural high-quality headphones
  Listening Environment              Room Noise: Hoth Spectrum at 30dBA (as defined by ITU-T, Recommendation P.800, Annex A, section A.1.1.2.2.1 Room Noise, with table A.1 and Figure A.1)
  ----------------------------- ---- --------------------------------------------------------------------------------------------------------------------------------------------------------

Material
--------

See section 4.

Experimental Design
-------------------

See section 5.2

Opinion Scale
-------------

The question asked of the subject will be a continuous Listening Quality
Scale ranging from 0 to 100.

The intervals 0 to 20 correspond to BAD, 20 to 40 to POOR, 40-60 to
FAIR, 60 to 80 to GOOD, and 80 to 100 to EXCELLENT.

Processing
----------

Processing is specified in section 7.

Duration of the Experiment
--------------------------

The duration of the experiment per subject depends on the number of
trials and on the number of items per trial. However, it can be assumed
that each vote requires listening to the respective item, the open
reference and two (quality-wise) neighboring items 2 times. With an
assumed average length per item of 7.5 s, the test will consume a
listening time per subject of:

\#trial \* \#hidden items/trial \* (1+1+2) \* \#re-listenings \*
length/item.

For the blind grading phase in each of the sub-experiments this accounts
to

12 \* 9 \* 4 \* 2 \* 7.5s = \~1.8 hours per subject.

For the training phase the number of re-listenings is assumed to be 1.
For each of the sub-experiments this accounts to

4 \* 9 \* 4 \* 1 \* 7.5s = \~20 min per subject,

In order to avoid listener fatigue, sufficient breaks are required
between the trials.

The experiments can be carried out with several subjects in parallel
provided that a corresponding number of proper listening facilities are
available.

Votes Per Condition
-------------------

The number of votes per conditions is identical to the number of
subjects per sub-experiment.

Randomizations
--------------

Each listener will be presented with the sound items in an individual
random presentation order. Also the order of the trials will be random
per individual.

The statistical significance of the results obtained in the
sub-experiments with frame erasures may suffer from the effect that --
due to different frame sizes of the candidate codecs -- the frame
erasures become effective at different points in time. The subjective
relevancy of the frame erasure will thus not only depend on the frame
error mitigation procedure of the codec candidates but also on the
signal characteristic of the sound item at the erased frames.

In order to statistically mitigate this latter effect as much as
possible there will be a randomization of the error patterns across the
various listeners and the various listening labs. I.e. for each
individual listening different error patterns will be used.

Processing
==========

Main processing
---------------

Common for the processing of all conditions is that it will be done with
concatenated material. To that purpose, the complete material including
training material will be concatenated into one single file. This file
will then be processed through the respective candidate or reference
codecs, or the specific anchor signal processing will be applied. After
processing and proper compensation of the processing delay, the material
will be split up again into separate items.

### Concatenation of material 

The concatenation will be done using an executable script. The script
will take as input all items of the training material and the test
material. The order in the concatenation is such that the training
material will precede the test material. Output of the concatenation
script will be a single file containing the concatenated material and a
time-file comprising name identifiers and time markers of the individual
items. The time-file will be used after processing for split-up of the
material to the individual items.

The concatenation script will be provided by: Ericsson

### Processing of anchor conditions

The creation of anchor conditions should be performed using the
"resamp-audio" tool of the AFSP library.

The program is freely available on the Internet, a copy (including usage
assistance, if necessary) will be provided to the host lab by Coding
Technologies.

Usage examples: Assuming a stereo .wav file sampled at 48kHz as the
input signal, the anchor signals are created by the following
commandlines:

-   3.5kHz anchor signal: ResampAudio --i 1 --f cutoff=0.0729167
    \<input-file\> \<output-file.wav\>

-   7kHz anchor signal: ResampAudio --i 1 --f cutoff=0.145833
    \<input-file\> \<output-file.wav\>

### Candidate and reference codec processing

The concatenated material file will be created by the hostlab. After
processing, the encoded material as well as the concatenated original
files will be delivered to candidates for cross-checking. The candidates
make sure that possible codec delay is properly compensated. The
procedure of how the delay was compensated need to be reported as part
of the respective candidate codec descriptions.

The analogue processing procedure will be applied to the reference
codecs.

#### Impaired channel processing

The host lab does the impaired channel processing with a FER pattern
file identifying correct and erroneous frames. The host lab will produce
that file using a script provided by:

Volunteering organization : Ericsson and Coding Technologies .

The input to the script is a seed to the random generator included in
the script. It will be provided by the ETSI Secretary, Paolo Usai after
candidate submission.

The format of the FER pattern file is ASCII text with one line per
frame. A '0' (zero) in a line indicates a correct frame, a '1' (one)
indicates a frame erasure.

The length of the file will be sufficient to cover the complete
concatenated training and test material, assuming a minimum frame length
of 10 ms. Note, that depending on the actual frame size of the
individual candidate codecs, the FER patter file will not be applied in
its entire length.

In order to realize the randomization of the error patterns across each
individual listening (see paragraph 7.9), before application the error
pattern file will be circularly shifted with individual time offsets.
The time offset (in frames) for listener *s*, lab *p* is calculated as
follows:

$\text{offs} = \text{mod}(s \cdot \text{12345} + p \cdot \text{31415},\text{totlen})$,
where *totlen* is the total length of the FER pattern file (in frames).

The circular shift will be done using an executable script with the
command line syntax:

shiftcirc --\<offs\> \<inpat\> \<outpat\>

The script will be provided by volunteering organization Coding
Technologies.

Post-processing
---------------

The post-processing comprises the steps of up-sampling to the original
sampling frequency of 48 kHz and split-up of the concatenated material.

### Up-sampling

Resampling to the original sampling frequency of 48 kHz will be done
using "resamp-audio" tool from the AFSP library.

The program is freely available on the Internet, a copy (including usage
assistance, if necessary) will be provided to the host lab by Coding
Technologies.

In order to avoid possible signal clipping distortions introduced after
re-sampling during the conversion of the internal floating-point to the
16-bit integer representation of the wav-file, before this conversion
the re-sampled signal is attenuated by applying a constant factor of
0.93 (≈ -0.3 dB).

Note, in order to ensure that this factor is consistently applied to all
codec, anchor and reference conditions, the program must always be
applied, even if actually no re-sampling is necessary since the sampling
rate of the respective signal is already 48 kHz.

Usage example: To attenuate and resample a .wav file of an arbitrary
sampling rate to 48 kHz sampling rate, the following commandline should
be used:

-   ResampAudio --s 48000 -g 0.93 \<input-file.wav\> \<output-file.wav\>

### Split-up of processed material

The split-up of the processed material to partial sound files will be
done using a program which is functionally inverse to the concatenation
procedure described in section 8.2.1. The program will take the
concatenated and processed (and delay-compensated) file along with the
time-file as input. On time intervals of length 2*N* around the time
markers *n~i~* indicated by the time-file it will first apply a
roll-off/roll-on window with Hanning characteristic:

and then split-up the file at the time markers *n~i~*. *N* corresponds
to a roll-off/roll-on time of 10 ms. I.e. *N*=0.01 \* *f~s~* where
*f~s~* is the sampling frequency of the file. Partial sound files will
be generated with names according to the name identifiers comprised in
the time-file and a processing tag, identifying the kind of processing.

The split-up program will have the following command-line syntax:

splitup \<infile\> \<processing\_tag\> \<timefile\>

The input file format is wav if the name has the extension .wav. If it
has the extension .raw, then a headerless 1-channel (mono) 16 bit PCM
file sampled at 48kHz is assumed.

The processing tag is an arbitrary string which is added to the name
identifiers given in the time-file.

The generated output files are of .wav format.

The program will be provided by Ericsson.

Blinding of material
--------------------

The purpose of blinding is to unveil the identity of the different
codec, reference and anchor conditions. The blinding is done using a
script that maps the de-concatenated items onto files with names
unveiling the actual condition. The mapping shall vary across the
different items.

The blinding of the material is made by the host lab, based on a script
created by the host lab. The host lab is responsible to keep the mapping
confidential.

Annex A: Listeners Instructions {#annex-a-listeners-instructions .MyHeading-1}
===============================

The following is an example of the type of instructions that should be
given to or read to the subjects in order to instruct them on how to
perform the test.

**Instructions to be given to subjects**

1 Training phase {#training-phase-1 .list-paragraph}
================

The first step in the listening tests is to become familiar with the
testing process. This phase is called a training phase and it precedes
the formal evaluation or blind grading phase.

The purpose of the training phase is to allow you, as an evaluator, to
learn how to use the test equipment and the grading scale.

In the training phase you will make a short test similar to the one you
will make in the blind grading phase of the test.

No grades given during the training phase will be taken into account in
the actual tests.

2 Blind grading phase {#blind-grading-phase .list-paragraph}
=====================

The purpose of the blind grading phase is to invite you to assign your
grades using the quality scale. Your grades should reflect your
subjective judgement of the quality level for each of the sound excerpts
presented to you. Each trial will contain \<x\> signals to be graded.
Each of the items is approximately 5 to 10 s long. You should listen to
the reference and all the test conditions by clicking on the respective
buttons. In a first step it is recommended to browse through all signals
within each trial in order to get a coarse impression of the offered
quality range. Then you may listen more carefully and start to rank the
signals. You may listen to the signals in any order, any number of
times. Use the slider for each signal to indicate your opinion of its
quality. When you are satisfied with your grading of all signals you
should click on the "register scores" button at the bottom of the
screen.

You will use the quality scale as given in Fig. 1 when assigning your
grades.

The grading scale is continuous from "excellent" to "bad". A grade of 0
corresponds to the bottom of the "bad" category, while a grade of 100
corresponds to the top of the "excellent" category.

In evaluating the sound excerpts, please note that you should not
necessarily give a grade in the "bad" category to the sound excerpt with
the lowest quality in the test. However one or more excerpts must be
given a grade of 100 because the unprocessed reference signal is
included as one of the excerpts to be graded.

You should not discuss your personal interpretation or your gradings
with the other subjects at any time during the test.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Annex B: File formats, Naming conventions, Directory structures, Platforms {#annex-b-file-formats-naming-conventions-directory-structures-platforms .MyHeading-1}
==========================================================================

 B-1 File formats {#b-1-file-formats .list-paragraph}
================

Unless specified differently all signal files are of wav format using a
linear 16-bit PCM sample representation. The sampling rate prior to
pre-processing and after post-processing is 48 kHz.

B-2 Computer platform {#b-2-computer-platform .list-paragraph}
=====================

The processing will be done in a Cygwin environment under Windows.

B-3 Directory structure {#b-3-directory-structure .list-paragraph}
=======================

Root

\|

-.- org Original (unprocessed) material

.- preproc Pre-processed material

.- ep Error pattern and program to generate it

.- bin Programs and scripts required for pre-processing\
and error pattern generation

\|

.- cand\_1 Directory for candidate codec 1

\| \|

\| .- processed processed material

\| .- bin programs and scripts required for processing

\| .- tmp intermediate processing results

\|

.- cand\_2 Directory for candidate codec 2

\| \|

\| .- processed processed material

\| .- bin programs and scripts required for processing

\| .- tmp intermediate processing results

\|

.- ref Reference codecs, anchors and hidden references

\| \|

\| .- processed processed material

\| .- bin programs and scripts required for processing

\| .- tmp intermediate processing results

\|

.- output Processed and blinded material per sub-experiment

\|

.- exp\_1

.- exp\_2

.- exp\_3

.

B-4 File naming {#b-4-file-naming .list-paragraph}
===============

1\. Unprocessed original signals:

\<signal\_category\>\_\<item\_no\>\_org.wav

where

-   \<signal\_category\> is one out of {p, c, si, v, sm, sp} (for Pop,
    Classic, Single instruments, a capella vocals, Mixed speech and
    music, Speech)

-   \<item\_no\> is a number identifying the item out of the respective
    signal category.

2\. Pre-processed original signals after concatenation:

all\_cat.wav

The corresponding time-file comprising the segmentation information is:

all\_cat.tim

3\. Material after main processing:

all\_cat\_\<codec\_id\>\_\<exp\_id\>.wav

where

-   \<codec\_id\> is one out of

    -   {cand\_1, cand\_2, AAC, RN, lp3500, lp7000, hidref, opref} for
        the stereo experiments below 48kbit/s,

    -   {cand\_1, cand\_2, AAC, RN, lp3500, lp7000, hidref, opref} for
        the stereo experiments at 48kbit/s.

-   \<exp\_id\> is one out of {1, 2, 3}

4\. Processed material after de-concatenation:

\<signal\_category\>\_\<item\_no\>\_\<codec\_id\>\_\<exp\_id\>.wav

5\. Processed material after blinding:

\<signal\_category\>\_\<item\_no\>\_\<exp\_id\>\_\<sub\_exp\>\_\<cond\_id\>.wav

where \<cond\_id\> is one out of

-   {1-7} for the stereo experiments below 48kbit/s,

-   {1-8} for the stereo experiments at 48kbit/s.

[^1]: Contact:

    Oliver Kunz

    Coding TechnologiesTel: +49 911 928 9112

    Fax: +49 911 928 9199

    E-mail: kunz\@codingtechnologies.com
