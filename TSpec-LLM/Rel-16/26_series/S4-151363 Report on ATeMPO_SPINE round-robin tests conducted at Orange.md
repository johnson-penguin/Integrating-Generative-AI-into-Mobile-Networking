**Source: ORANGE**

**Title: Report on ATeMPO\_SPINE round-robin tests conducted at Orange**

**Document for: Information**

Agenda Item: 10.5
-----------------

This document is a re-submission of S4-AHQ101.

1.  Background

The objective of the present document is to document how round robin
tests following the test plan in \[1\] were conducted in the Orange Lab
test facility.

2.  Tests at Orange Lab according to the test plan

Tests were conducted at the Orange Lab premises in Lannion, France. They
were split in two time periods:

-   In a first time period (in Weeks 27-28) testing with the 4.1
    loudspeaker method was performed - the limited time frame was not
    sufficient to perform testing with the new 8-loudspeaker method
    specified in TS 103 224, however binaural noises from TS 103 224
    were used with the 4.1 loudspeaker method.

-   A second time period (in Week 37) was allocated to be able to
    perform tests with the 8-speaker method.

As described in \[2\], the basis was to measure S-MOS, N-MOS and G-MOS
for the ETSI ES 103 106 quality predictor in various conditions.

The complete list of background noise conditions described in \[1\] was
evaluated:

\- 8-speaker method (ETSI TS 103 224)

\- 4.1 loudspeaker method (ETSI ES 202 396-1)

\- 4.1 loudspeaker method using the same noise scenarios as in TS
103 224, for HHHF

Not all DUT positions and bandwidth described in the test plan in \[1\]
could be tested due to time and resource restrictions. More
specifically:

-   For the DUT position only the "hand-held handsfree" case (6 noise
    types plus silence) was considered and the table "desktop handsfree"
    case (one noise type plus silence) was not tested.

-   For bandwidths (UMTS CS call used), only wideband was considered and
    narrowband was not tested.

An acoustically treated room was used. This room is used to conduct all
GSMA HD voice logo certification tests by Orange; the reproducibility of
test results for ES 202 396-1 has been already validated with several
labs worldwide performing self-certification*.*

HEAD acoustics ACQUA with the HAE-BGN and 3PASS background noise systems
were used. Loudspeakers were Genelec 1029 A (loudspeakers 1 to 4),
Foxtex PM0,5sub (subwoofer) and Fostex PM0,5n (loudspeakers 5 to 8). The
test sequences and (smd) script files to execute the tests were provided
by HEAD Acoustics \[3\].

A HEAD Acoustics HATS was used to allow comparison with other labs using
the same HATS model and minimize sources of variation in the round robin
tests.

**Procedure**

The mouth simulator of the HATS was calibrated at MRP (80 to 10000 Hz)
using a ¼-inch pressure-field microphone (B&K 4938).

The HFRP calibration was performed for one measurement distance (50 cm).

The HATS ears were calibrated.

Equalization of the 4.1 speaker system, adhoc delays (optimized
experimentally to keep equalization gains within reasonable limits) were
used:

![](media/image1.png){width="4.38125in" height="3.5381944444444446in"}

Equalization of the 8 speaker system for hand-held handsfree was done
automatically with 3PASS.

3.  Additional tests (beyond the test plan in \[1\])

Some additional tests were conducted;

-   The test plan in \[1\] required to test 6 devices (DUT1 to DUT6)
    that were the same for all labs involved in the round robin
    activity. An extra device (DUT7) was included in all tests.

-   For all test cases (in sending direction), the audio from the DUT
    was recorded to allow informal subjective listening and verify the
    consistency between objective and subjective scores.

-   For the 8-loudspeaker method (HHHF case), tests were conducted twice
    (with and without 22.5 ° rotation of HATS) to check whether the HATS
    rotation with respect to loudspeakers has any impact. Furthermore,
    tests with no HATS rotations were also repeated twice to verify if
    there is any variability - in the following only test results for
    the first trial are reported as the differences in MOS-LQO are in
    the +/-0.1 range.

4.  Physical test setup for the tests in the sending direction

The test room dimensions are 5m (length) x 3,67m (width).

**HATS position**

HRP 143,5 cm above the floor

The HATS was placed 2,59m from the front wall and 1,86m from the right
wall.

HATS rotated by 0° or 22.5° - the latter case was similar to \[2\] to
avoid obstructing the sound from speaker 7.

**Speaker position**

The speaker height and placement are summarized in Table 1.

Table 1. Loudspeaker position in the test room.

  --------------------- --------------- ---------------- ---------------- --------------- ------------
  **Loudspeaker**       **Left wall**   **Front wall**   **right wall**   **back wall**   **Height**
  **1 - Front left**    **0,53 m**      **1,3 m**        ** **            ** **           **1,36 m**
  **2 - Front right**   ** **           **1,25 m**       **0,59 m**       ** **           **1,36 m**
  **3 - Rear right**    ** **           ** **            **0,68 m**       **1,06 m**      **1,36 m**
  **4 - Rear left**     **1,09 m**      **0,68 m**       ** **            ** **           **1,36 m**
  **5-**                ** **           **1,17 m**       ** **            **2,30 m**      **1,23 m**
  **6-**                ** **           ** **            **0,42 m**       **2,30 m**      **1,23 m**
  **7-**                ** **           ** **            **1,86 m**       **0,80 m**      **1,23 m**
  **8-**                **0,42 m**      ** **            ** **            **2,30 m**      **1,21 m**
  --------------------- --------------- ---------------- ---------------- --------------- ------------

**Equalization of the 4.1 speaker method (ES 202 396-1)**

![](media/image2.png){width="5.8875in" height="5.280555555555556in"}

**Equalization of the 8-speaker method (TS 103 224) for the hand-held
handsfree mode**

The same positions were used in the 8-loudspeaker case, except that 4
loudspeakers were added in the room and the HATS was rotated by either
0° or 22.5°. The loudspeaker numbering was the same as in \[2\] except
that loudspeakers 3 and 4 (rear) were swapped.

5.  Equalization results

    1.  Hand-held handsfree equalization results (8 speaker method)

Only equalization results for no HATS rotation are shown here, however
equalization results for the 22.5° rotation case are also available if
needed.

Diagrams of validation results

  ----------------------------------------------------------------------------------- -----------------------------------------------------------------------------------
  Calibration Position                                                                Fine tuning position
  Frequency Response I                                                                50 Hz to 10000 Hz
  ![](media/image3.wmf){width="3.229861111111111in" height="2.5388888888888888in"}    ![](media/image4.wmf){width="3.229861111111111in" height="2.5388888888888888in"}
  Frequency Response II                                                               10000 Hz to 16000 Hz
  ![](media/image5.wmf){width="3.229861111111111in" height="2.5388888888888888in"}    ![](media/image6.wmf){width="3.229861111111111in" height="2.5388888888888888in"}
  Average Frequency Response                                                          50 Hz to 20000 Hz
  ![](media/image7.wmf){width="3.229861111111111in" height="2.5388888888888888in"}    ![](media/image8.wmf){width="3.229861111111111in" height="2.5388888888888888in"}
  Mag. of Complex Coherence                                                           100 Hz to 1000 Hz
  ![](media/image9.wmf){width="3.229861111111111in" height="2.5388888888888888in"}    ![](media/image10.wmf){width="3.229861111111111in" height="2.5388888888888888in"}
  Phase of Complex Coherence I                                                        100 Hz to 1000 Hz
  ![](media/image11.wmf){width="3.229861111111111in" height="2.5388888888888888in"}   ![](media/image12.wmf){width="3.229861111111111in" height="2.5388888888888888in"}
  Phase of Complex Coherence II                                                       1000 Hz to 1500 Hz
  ![](media/image13.wmf){width="3.229861111111111in" height="2.5388888888888888in"}   ![](media/image14.wmf){width="3.229861111111111in" height="2.5388888888888888in"}
  ----------------------------------------------------------------------------------- -----------------------------------------------------------------------------------

2.  Equalization results for the 4.1 speaker method (ES 202 396-1)

![](media/image15.png){width="6.2375in" height="4.064583333333333in"}

3.  Mouth equalization results

![](media/image16.png){width="6.299305555555556in"
height="4.471527777777778in"}

6.  Additional positioning information for the ES 103 224 method

The positioning was made according to the testing procedure documented
in \[3\].

7.  Test results

As noted in \[2\], the detailed results will be available all labs have
completed their measurements and the differences between the background
noise methods can be analyzed using the same noise scenarios for the
HHHF mode.

Results from the two noise generation methods were very close when using
the same noise scenarios (from TS 103 224) as shown in Table 2.

Table 2. MOS-LQO values for TS 103 224 (no HATS rotation) minus MOS-LQO
values for ES 202 396-1 with noise scenarios from TS 102 224.

  ------- --------- --------------- ------------------ ---------------- --------------- ------------
          **Pub**   **Crossroad**   **Trainstation**   **Inside Car**   **Cafeteria**   **Office**
  S-MOS   ** **     ** **           ** **              ** **            ** **           ** **
  DUT1    0,1       0               0                  0                0,1             0
  DUT2    -0,1      -0,1            0                  -0,1             -0,1            0
  DUT3    0         -0,1            0                  -0,1             -0,1            0
  DUT4    -0,3      -0,1            -0,1               0                -0,1            0
  DUT5    0,2       0,1             0                  0                0,2             0,1
  DUT6    -0,3      -0,1            -0,1               0                -0,2            -0,1
  DUT7    -0,4      0               0                  0                -0,1            -0,2
  N-MOS                                                                                  
  DUT1    0         -0,1            -0,1               -0,1             0               0
  DUT2    -0,1      -0,1            -0,2               -0,1             -0,2            -0,2
  DUT3    0         -0,3            0                  -0,2             -0,2            -0,3
  DUT4    0         -0,1            -0,1               -0,1             0               -0,3
  DUT5    0         -0,1            0                  -0,1             -0,2            -0,3
  DUT6    -0,1      0               0                  -0,2             -0,1            -0,1
  DUT7    -0,1      -0,1            -0,2               -0,1             -0,1            -0,1
  G-MOS                                                                                  
  DUT1    0         0               0                  -0,1             0               0
  DUT2    -0,1      -0,1            -0,1               -0,1             -0,1            -0,1
  DUT3    -0,1      -0,1            -0,1               -0,2             -0,1            -0,1
  DUT4    -0,2      -0,1            0                  0                -0,1            -0,2
  DUT5    0,1       0               0                  -0,1             0               0
  DUT6    -0,2      -0,1            0                  0                -0,2            -0,2
  DUT7    -0,3      -0,1            -0,1               0                -0,1            -0,2
  ------- --------- --------------- ------------------ ---------------- --------------- ------------

These results are illustrated in the figures below.

![](media/image17.png){width="6.395138888888889in"
height="2.5729166666666665in"}

![](media/image18.png){width="6.395138888888889in" height="2.5625in"}

![](media/image19.png){width="6.395138888888889in"
height="2.5729166666666665in"}

Comparison of test methods for HHHF for wideband (MOS values for TS
103 224 minus MOS values for ES 202 396-1 with noise scenarios from TS
102 224). For each noise scenario, the DUTS are plotted in sequence
DUT1, DUT2...DUT7. Absolute values ranged from 2.3 to 4.2 (S-MOS), 1.7
to 3.5 (N-MOS) and 1.7 to 3.4 (G-MOS) for the TS 103 224 method.

Similarly, a comparison of test results between 0° and 22.5° HATS
rotation is provided in Table 3.

Table 3. MOS-LQO values for TS 103 224 (no HATS rotation) minus MOS-LQO
for TS 103 224 (22.5° HATS rotation) with noise scenarios from TS
102 224.

  ------- --------- --------------- ------------------ ---------------- --------------- ------------
          **Pub**   **Crossroad**   **Trainstation**   **Inside Car**   **Cafeteria**   **Office**
  S-MOS   ** **     ** **           ** **              ** **            ** **           ** **
  DUT1    0,1       0               0                  0                0,1             0
  DUT2    0         -0,2            -0,1               -0,1             0               0,1
  DUT3    0         -0,1            0                  -0,1             -0,1            0
  DUT4    -0,3      -0,1            -0,1               0                -0,1            0
  DUT5    0,4       0               0,2                0                0,1             0,1
  DUT6    -0,1      0               0                  0,1              0               0
  DUT7    -0,4      0               0                  -0,1             0               -0,1
  N-MOS                                                                                  
  DUT1    -0,1      -0,1            -0,1               -0,1             0               0
  DUT2    -0,3      -0,2            -0,3               -0,3             -0,3            -0,3
  DUT3    -0,1      -0,3            0                  -0,2             -0,2            -0,3
  DUT4    0         0               -0,1               -0,1             0               -0,1
  DUT5    -0,1      -0,1            0                  0                -0,1            -0,1
  DUT6    -0,1      0               0                  -0,1             0               0
  DUT7    -0,2      -0,2            -0,2               -0,2             0               0
  G-MOS                                                                                  
  DUT1    0         0               0                  -0,1             0               0
  DUT2    -0,1      -0,3            -0,2               -0,2             -0,1            0
  DUT3    -0,1      0               0                  -0,2             0               0
  DUT4    -0,2      0               0                  0,1              -0,1            -0,1
  DUT5    0,2       0               0,1                -0,1             0               0,1
  DUT6    0         0               0                  0,1              0               -0,1
  DUT7    -0,4      -0,1            -0,1               -0,1             -0,1            -0,1
  ------- --------- --------------- ------------------ ---------------- --------------- ------------

8.  Conclusions from the tests

The detailed conclusions about lab-to-lab variability will be drawn when
results from all labs will be made available and analyzed.

The following preliminary observations can be made for the tests
conducted in Orange:

-   Similar to \[2\], both background noise methods produced almost
    identical hand-held handsfree results (averaged over noise types)
    and both methods use multiple speakers with highly correlated
    signals.

-   MOS results averaged over noise scenarios were very similar between
    the two methods. The same observation can be made when checking the
    influence of 0° vs. 22.5° HATS rotation for the 8-loudpeaker case.

-   Testing with the 3PASS system (TS 103 224) proved to be sometimes
    unstable and some test cases had to be repeated several times.

-   Results from informal listening indicated that the MOS-LQO scores do
    not always represent perceived quality.

9.  References

\[1\] Tdoc SQ-AHQ099, Proposed test plan for a Round Robin Test for
comparison of background noise simulations -- Rev. 1, Source: Editor
(Qualcomm)

\[2\] S4-151040, ATeMPO\_SPINE round-robin tests conducted at Sony,
Source: Sony Mobile Communications

\[3\] Head Acoustics documentation provided for round robin

\[4\] ETSI ES 202 396-1, Speech quality performance in the presence of
background noise; Part 1: Background noise simulation technique and
background noise database

\[5\] ETSI TS 103 224, A sound field reproduction method for terminal
testing including a background noise database
