**3GPP TSG SA4\#30 S4-040152**

**Malaga, Spain, 23-27 Feb 2004 Agenda Item: SES**

**Title: Results of error resilience for SES codec candidates**

**Source: France Telecom**

**Contact: Denis Jouvet**

The following figures displays the behaviour of the speech recognition
word error rates under channel error. The results are extracted from
\[1\].

This word file provides the word error rates at 0 and 10% BLER, both for
8 kHz and 16 kHz.

![](media/image1.wmf){width="4.333333333333333in"
height="2.7916666666666665in"}

![](media/image2.wmf){width="4.333333333333333in"
height="2.7916666666666665in"}

At 16 kHz, for AMR-WB 23.85, the intermediate results at 1% and 3% are
also provided. They are reported in the following figure.

![](media/image3.wmf){width="4.333333333333333in"
height="2.7916666666666665in"}

**Conclusion**

DSR is robust to channel errors, whereas AMR based speech recognition
performances degrades significantly with channel errors.

Moreover, the results at 16 kHz show that the performances degradation
significantly gets larger as the channel errors increase.

**Apprendix**

Results from information results (extracted from \[1\]):

**Aurora-3 Italian under channel errors**

  -------- -------- ------------------------- -----------------
  s-rate   vocabs   codec                     Word Error Rate
  8kHz     Digits   w/o coding                3.25
                    AMR-NB 4.75               4.60
                    AMR-NB 4.75 @ 10% BLER    9.73
                    AMR-NB 12.2               3.45
                    AMR-NB 12.2 @ 10% BLER    10.62
                    DSR at 8kHz               2.18
                    DSR 8kHz @ 10% BLER       2.67
                                              
  16kHz    Digits   w/o coding                2.02
                    AMR-WB 12.65              2.43
                    AMR-WB 12.65 @ 10% BLER   5.53
                    AMR-WB 23.85              2.43
                    AMR-WB 23.85 @ 1% BLER    2.43
                    AMR-WB 23.85 @ 3% BLER    3.15
                    AMR-WB 23.85 @ 10% BLER   5.62
                    DSR at 16kHz              1.80
                    DSR 16kHz @ 10% BLER      2.05
  -------- -------- ------------------------- -----------------

  -------- -------- ------------------------- -----------------
  s-rate   vocabs   codec                     Word Error Rate
  8kHz     Digits   w/o coding                *6.4*
                    AMR-NB 4.75               *9.4*
                    AMR-NB 4.75 @ 10% BLER    *NA*
                    AMR-NB 12.2               *6.6*
                    AMR-NB 12.2 @ 10% BLER    *NA*
                    DSR at 8kHz               *6.5*
                    DSR 8kHz @ 10% BLER       *NA*
                                              
  16kHz    Digits   w/o coding                *NA*
                    AMR-WB 12.65              *7.2*
                    AMR-WB 12.65 @ 10% BLER   *NA*
                    AMR-WB 23.85              *NA*
                    AMR-WB 23.85 @ 1% BLER    *NA*
                    AMR-WB 23.85 @ 3% BLER    *NA*
                    AMR-WB 23.85 @ 10% BLER   *NA*
                    DSR at 16kHz              *4.7*
                    DSR 16kHz @ 10% BLER      *NA*
  -------- -------- ------------------------- -----------------

Note: For Aurora-3 under channel errors word error rate is for the
well-matched condition.

**Reference**

\[1\] \"Results for information from ASR vendors\" -- word file in
S4-040100.
