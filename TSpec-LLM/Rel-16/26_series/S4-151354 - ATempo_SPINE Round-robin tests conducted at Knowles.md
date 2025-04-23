**Source: Knowles Inc.**

**Title: ATeMPO\_SPINE round-robin tests conducted at Knowles**

**Document for: Information**

Agenda Item: 10.5
-----------------

1.  Background

Within the ongoing work item "Acoustic Test methods and Performance
Objectives for Speakerphone Performance in Noisy Environments"
(ATeMPO\_SPINE), a round-robin test is conducted. A number of commercial
mobile phones are circulated between labs to study the suitability of
different test setups. The round-robin test plan can be found in \[1\],
from where we quote the objectives of the round-robin test:

> "
>
> Questions to answer:
>
> How good is the reproducibility of the ETSI ES 202 396-1 and ETSI TS
> 103 224 background noise (BGN) simulation methods?
>
> Find out whether the different BGN simulation methods lead to
> different S-MOS-LQO and N-MOS-LQO results when measuring the same UE.
>
> "

The purpose of the present document is to document how the tests were
conducted in the Knowles lab and to report on some observations made.

2.  Tests at Knowles according to the test plan

Tests were conducted at the Knowles premises in Mountain View,
California, USA, during week 30, according to plan, with the following
observations:

The basis was to measure S-MOS, N-MOS and G-MOS for the ETSI ES 103 106
quality predictor in various conditions.

Background noise:

\- 8-speaker method (ETSI TS 103 224)

\- 4.1 loudspeaker method (ETSI ES 202 396-1)

\- 4.1 loudspeaker method using the same noise scenarios as in TS
103 224, for HHHF

DUT position:

\- DUT in front of HATS "hand-held handsfree" (6 noise types plus
silence)[^1]

\- DUT laying on a table "desktop handsfree" (one noise type plus
silence)

Bandwidths (UMTS CS call used):

\- Narrowband

\- Wideband

An "office-type" room (see ETSI ES 202 396-1) in the audio lab was used.
It has the specified ceiling absorbers. The walls have absorbing
objects, resulting in a RT60 reverberation time of 117.4 ms and clarity
C80 of 29.2 dB.

HEAD acoustics ACQUA with the HAE-BGN and 3PASS background noise systems
were used. Loudspeakers were JBL LSR6328P. The test sequences were
provided by HEAD acoustics.

A HEAD acoustics HMS II.3 HATS was used.

**Procedure**

The mouth simulator of the HATS was calibrated at MRP (90 to 11000 Hz)
using a ¼-inch pressure-field microphone.

The HFRP calibration was performed for the two different measurement
distances, 30 and 50 cm.

The HATS ears were calibrated.

Equalization of the 4.1 speaker system, standard delays were used:

![](media/image1.png){width="1.9791666666666667in"
height="0.7395833333333334in"}

Equalization of the 8 speaker system for hand-held handsfree.

Measurements of DUT:s in HHHF mode

Equalization of the 8 speaker system for desktop handsfree.

Measurements of DUT:s in DTHF mode

3.  Additional tests (beyond the test plan in \[1\])

As programmed by HEAD acoustics, the noise spectrum was captured from
the reference microphone and from the output of the system simulator.
This makes it possible to assess what the actual input to and output
from the DUT, for diagnostic purposes.

For wideband speech:

-   RLR for the hand-held handsfree mode was measured using the
    procedures of 26.132

-   Recording of the receiving direction with applied background noise

For the latter test, the Dynastat speech file used the sending MOS-LQO
tests was fed in the receiving direction at active speech level -16
dBm0. The receiving direction was recorded in hand-held handsfree mode
using both ears of the HATS with free-field correction. The background
noise was calibrated using TS 103 224 procedures, with the microphone
array mounted on HATS.

The recordings are binaural recordings where the background noise and
the mobile phone micro-speaker can be presented to subjects, providing
realistic spatial cues.

The purpose was to give additional insight to which of the noise types
that are relevant use cases for the hand-held handsfree mode, and which
are too noisy to be used in practice.

For a sub-set of the devices, intelligibility, speech quality, and
listening effort were measured and reported in S4-151033 \[4\].

4.  Physical test setup for the tests in the sending direction

**HATS height**

HRP 130 cm above the floor

**Speaker height**

Speakers 1-4: 126 cm to acoustical center

Speakers 5-8: 142 cm to acoustical center

The speaker stands used provided a locator pin to fix heights at
pre-determined levels. Friction locks were also available, but the
locator pin was deemed more reliable, and so the height selection was
limited to those available.

**Placement**

Speakers 1-4 (corners) were placed on a square with distance of 146 cm
from the center point of the array to each corner.

Speakers 5-8 (sides) were placed on a square with distance of 126 cm
from the centerpoint of the array to each side.

HATS was in most cases rotated \~22.5 deg, to avoid obstructing the
sound from speaker 7, as was also done by Sony in S4-151040 \[5\].

**Measurements in hand-held handsfree mode**

As noted above, the HATS location was rotated within the speaker array.
The corresponding figure from \[5\] is reproduced here for convenience.

![](media/image2.png){width="4.801388888888889in"
height="4.172916666666667in"}

Figure 1 Measurements in HHHF mode using both background noise methods.
The UE is shown in blue. From \[5\]

**Measurements in desktop handsfree mode**

Continuing the approach of using a rotation to avoid obstruction of
speakers, the desktop set up also followed \[5\]. Figure 2 reproduces
the relevant figure from \[5\]. As the HEAD acoustics HATS was used, it
was mounted with the torso-box reversed, as reported by HEAD acoustics.

![](media/image3.png){width="5.34375in" height="4.220833333333333in"}

Figure 2 Measurements in DTHF mode using both background noise methods.
The UE is shown in blue. From \[5\]

5.  Equalization results

    1.  Hand-held handsfree equalization results (8 speaker method)

  ----------------------------------------------------------------------------------- -----------------------------------------------------------------------------------
  Calibration Position                                                                Fine tuning position
  Frequency Response I                                                                50 Hz to 10000 Hz
  ![](media/image4.wmf){width="3.234027777777778in" height="2.5388888888888888in"}    ![](media/image5.wmf){width="3.234027777777778in" height="2.5388888888888888in"}
  Frequency Response II                                                               10000 Hz to 16000 Hz
  ![](media/image6.wmf){width="3.234027777777778in" height="2.5388888888888888in"}    ![](media/image7.wmf){width="3.234027777777778in" height="2.5388888888888888in"}
  Average Frequency Response                                                          50 Hz to 20000 Hz
  ![](media/image8.wmf){width="3.234027777777778in" height="2.5388888888888888in"}    ![](media/image9.wmf){width="3.234027777777778in" height="2.5388888888888888in"}
  Mag. of Complex Coherence                                                           100 Hz to 1000 Hz
  ![](media/image10.wmf){width="3.234027777777778in" height="2.5388888888888888in"}   ![](media/image11.wmf){width="3.234027777777778in" height="2.5388888888888888in"}
  Phase of Complex Coherence I                                                        100 Hz to 1000 Hz
  ![](media/image12.wmf){width="3.234027777777778in" height="2.5388888888888888in"}   ![](media/image13.wmf){width="3.234027777777778in" height="2.5388888888888888in"}
  Phase of Complex Coherence II                                                       1000 Hz to 1500 Hz
  ![](media/image14.wmf){width="3.234027777777778in" height="2.5388888888888888in"}   ![](media/image15.wmf){width="3.234027777777778in" height="2.5388888888888888in"}
  ----------------------------------------------------------------------------------- -----------------------------------------------------------------------------------

2.  Desktop handsfree equalization results (8 speaker method)

Diagrams of validation results

  ----------------------------------------------------------------------------------- -----------------------------------------------------------------------------------
  Calibration Position                                                                Fine tuning position
  Frequency Response I                                                                50 Hz to 10000 Hz
  ![](media/image16.wmf){width="3.234027777777778in" height="2.5388888888888888in"}   ![](media/image17.wmf){width="3.234027777777778in" height="2.5388888888888888in"}
  Frequency Response II                                                               10000 Hz to 16000 Hz
  ![](media/image18.wmf){width="3.234027777777778in" height="2.5388888888888888in"}   ![](media/image19.wmf){width="3.234027777777778in" height="2.5388888888888888in"}
  Average Frequency Response                                                          50 Hz to 20000 Hz
  ![](media/image20.wmf){width="3.234027777777778in" height="2.5388888888888888in"}   ![](media/image21.wmf){width="3.234027777777778in" height="2.5388888888888888in"}
  Mag. of Complex Coherence                                                           100 Hz to 1000 Hz
  ![](media/image22.wmf){width="3.234027777777778in" height="2.5388888888888888in"}   ![](media/image23.wmf){width="3.234027777777778in" height="2.5388888888888888in"}
  Phase of Complex Coherence I                                                        100 Hz to 1000 Hz
  ![](media/image24.wmf){width="3.234027777777778in" height="2.5388888888888888in"}   ![](media/image25.wmf){width="3.234027777777778in" height="2.5388888888888888in"}
  Phase of Complex Coherence II                                                       1000 Hz to 1500 Hz
  ![](media/image26.wmf){width="3.234027777777778in" height="2.5388888888888888in"}   ![](media/image27.wmf){width="3.234027777777778in" height="2.5388888888888888in"}
  ----------------------------------------------------------------------------------- -----------------------------------------------------------------------------------

3.  Equalization results for the 4.1 speaker method (ES 202 396-1)

![](media/image28.jpeg){width="6.3597222222222225in" height="3.99375in"}

4.  Mouth equalization results

![](media/image29.png){width="5.839583333333334in"
height="4.043055555555555in"}

6.  Additional positioning info for the ES 103 224 method

As in Sony's report \[5\], the positioning of devices was intended to
replicate what was done at the HEAD acoustics lab.

1.  Hand-held handsfree

![](media/image30.png){width="6.497222222222222in"
height="2.9791666666666665in"}

Distance from Pos.5 to HATS lips: 27.5 cm horizontal, 5 cm vertical

2.  Desk-top handsfree

![](media/image31.png){width="6.495138888888889in"
height="3.8958333333333335in"}

Distance from Pos.5 to HATS lips: 37.5 cm horizontal, 30 cm vertical
(from table top)

7.  Test results

As a detailed analysis of all results is available in a joint
contribution for this meeting, no additional analysis will be presented
here.

It was noted in the course of reviewing that analysis that there was an
outlier for one device when tested using the ES 202 396-1 method. It is
believed that there was an issue with reproduction, possibly the
subwoofer was not properly engaged, or some other intermittent failure
occurred. There was no evidence of any recurring or systematic issue.

8.  Conclusions from the tests

As noted in \[5\], more fully-formed conclusions will be drawn from the
detailed analysis of the joint contribution

We also note along with Sony \[5\]:

-   For desktop handsfree, the equalization was not successful at high
    frequencies (frequency response at the fine-tuning position),
    despite several attempts. Initial efforts used a 1x1 m surface that
    was very smooth (hard plastic). Using a surface with slight texture
    variation produced somewhat better results, but still did not pass
    the current frequency response requirements for the fine-tuning
    position.

-   A lot of preparations and efforts were required to conduct the
    tests, it is quite resource intensive, especially if accuracy is a
    priority.

9.  References

\[1\] Tdoc SQ-AHQ099 Proposed test plan for a Round Robin Test for
comparison of background noise simulations -- Rev. 1

\[2\] ETSI ES 202 396-1 Speech quality performance in the presence of
background noise; Part 1: Background noise simulation technique and
background noise database

\[3\] ETSI TS 103 224 A sound field reproduction method for terminal
testing including a background noise database

\[4\] S4-151033 On receiving listening to handheld speakerphone in
noise. Audience, Inc. TSG SA4\#85, 24-28 August 2015, Kobe, Japan.

\[5\] S4-151040 ATeMPO-SPINE round-robin tests conducted at Sony. Sony
Mobile Communications, TSG SA4\#85, 24-28 August 2015, Kobe, Japan.

[^1]: The test plan \[1\] prescribes 8 noise types but it was decided
    offline to reduce to 6 noise types to increase chances of completing
    the round-robin on time
