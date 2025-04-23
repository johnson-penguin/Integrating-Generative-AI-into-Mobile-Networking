\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#

Readme.txt file for AMR VAD Option 2 test vector generation - 6 Sept
2000

Contact: Jim Ashley

Motorola, Inc.

ashley\@labs.mot.com

\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#

Update: 6 March 2001: Adjustments for 06.73 v. 7.5.0

26.073 v. 3.2.0 v. 4.0.0, v. 5.0.0, 6.0.0, 7.0.0, 8.0.0, 9.0.0, 10.0.0,
11.0.0, 12.0.0, 13.0.0, 14.0.0 and 15.0.0

Stefan.Bruhn\@ericsson.com

Summary of changes:

\- Applied uppercase file naming convention from TS 06.74/26.074

\- All files now LSB first according to TS 06.74/26.074

\- Supplied blocklength 1 to g711demo

\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#

This file describes the necessary steps for generating master test
vectors

for the AMR VAD Option 2 algorithm. The process was originally developed

on a Sun Sparc Ultra-2 platform running SunOS 5.6.

Step 1) Unpack the processing script and input vectors:

Unzipping the file \"TVGen\_VAD2.zip\" should yield the following files
in the

working directory. The \*.inp files are headerless 16 bit binary 2\'s
complement

speech files in little-endian format (LSB first).

300160 Sep 17 1999 InputMasterTVs/Dt21.inp

197280 Sep 17 1999 InputMasterTVs/Dt22.inp

300320 Sep 17 1999 InputMasterTVs/Dt23.inp

380160 Sep 13 1999 InputMasterTVs/Dt24.inp

7201 Sep 6 12:56 Readme.txt

3229 Sep 6 11:20 TVGen\_VAD2.csh

Step 2) Edit the C-Shell script (TVGen\_VAD2.csh) for your environment:

The first few lines of this script define the local environment. Only
the items

between the SET USER DEFINES and END USER DEFINES comments should need

modification. These items include:

path to AMR executables

path to ITU-T G.711 A/u Law companding routines

path to input test vectors (default should be OK)

path to output directory

path to scratch disc space

flags for linear and/or A/u Law test vector generation

Step 3) Run script:

Enter the command \"TVGen\_VAD2.csh\". This should produce a directory

structure similar to the following (which was specific to AMR v7.4.0):

\% ls -lR VAD2\_TV\_740

VAD2\_TV\_740:

total 24

drwxr-xr-x 2 ashley ae598 4096 Sep 6 11:36 alaw

drwxr-xr-x 2 ashley ae598 4096 Sep 6 11:29 linear

drwxr-xr-x 2 ashley ae598 4096 Sep 6 11:42 mulaw

VAD2\_TV\_740/alaw:

total 15456

-rw-r\--r\-- 1 ashley ae598 300032 Sep 6 11:29 Dt21a.inp

-rw-r\--r\-- 1 ashley ae598 468500 Sep 6 11:29 Dt21a122.cod

-rw-r\--r\-- 1 ashley ae598 299520 Sep 6 11:29 Dt21a122.out

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:29 Dt22a.inp

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:32 Dt22a102.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:33 Dt22a102.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:30 Dt22a122.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:30 Dt22a122.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:36 Dt22a475.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:36 Dt22a475.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:35 Dt22a515.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:35 Dt22a515.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:35 Dt22a59.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:35 Dt22a59.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:34 Dt22a67.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:34 Dt22a67.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:34 Dt22a74.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:34 Dt22a74.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:33 Dt22a795.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:33 Dt22a795.out

-rw-r\--r\-- 1 ashley ae598 300032 Sep 6 11:30 Dt23a.inp

-rw-r\--r\-- 1 ashley ae598 468500 Sep 6 11:31 Dt23a122.cod

-rw-r\--r\-- 1 ashley ae598 299520 Sep 6 11:31 Dt23a122.out

-rw-r\--r\-- 1 ashley ae598 379904 Sep 6 11:31 Dt24a.inp

-rw-r\--r\-- 1 ashley ae598 593500 Sep 6 11:32 Dt24a122.cod

-rw-r\--r\-- 1 ashley ae598 379392 Sep 6 11:32 Dt24a122.out

VAD2\_TV\_740/linear:

total 15464

-rwxr-x\-\-- 1 ashley ae598 300160 Sep 17 1999 Dt21.inp

-rw-r\--r\-- 1 ashley ae598 469000 Sep 6 11:22 Dt21\_122.cod

-rw-r\--r\-- 1 ashley ae598 300160 Sep 6 11:22 Dt21\_122.out

-rwxr-x\-\-- 1 ashley ae598 197280 Sep 17 1999 Dt22.inp

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:25 Dt22\_102.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:25 Dt22\_102.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:23 Dt22\_122.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:23 Dt22\_122.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:29 Dt22\_475.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:29 Dt22\_475.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:28 Dt22\_515.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:28 Dt22\_515.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:28 Dt22\_59.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:28 Dt22\_59.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:27 Dt22\_67.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:27 Dt22\_67.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:26 Dt22\_74.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:27 Dt22\_74.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:26 Dt22\_795.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:26 Dt22\_795.out

-rwxr-x\-\-- 1 ashley ae598 300320 Sep 17 1999 Dt23.inp

-rw-r\--r\-- 1 ashley ae598 469000 Sep 6 11:24 Dt23\_122.cod

-rw-r\--r\-- 1 ashley ae598 300160 Sep 6 11:24 Dt23\_122.out

-rwxr-x\-\-- 1 ashley ae598 380160 Sep 13 1999 Dt24.inp

-rw-r\--r\-- 1 ashley ae598 594000 Sep 6 11:25 Dt24\_122.cod

-rw-r\--r\-- 1 ashley ae598 380160 Sep 6 11:25 Dt24\_122.out

VAD2\_TV\_740/mulaw:

total 15456

-rw-r\--r\-- 1 ashley ae598 300032 Sep 6 11:36 Dt21u.inp

-rw-r\--r\-- 1 ashley ae598 468500 Sep 6 11:36 Dt21u122.cod

-rw-r\--r\-- 1 ashley ae598 299520 Sep 6 11:36 Dt21u122.out

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:36 Dt22u.inp

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:39 Dt22u102.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:39 Dt22u102.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:37 Dt22u122.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:37 Dt22u122.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:42 Dt22u475.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:42 Dt22u475.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:42 Dt22u515.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:42 Dt22u515.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:41 Dt22u59.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:41 Dt22u59.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:41 Dt22u67.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:41 Dt22u67.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:40 Dt22u74.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:40 Dt22u74.out

-rw-r\--r\-- 1 ashley ae598 308000 Sep 6 11:40 Dt22u795.cod

-rw-r\--r\-- 1 ashley ae598 197120 Sep 6 11:40 Dt22u795.out

-rw-r\--r\-- 1 ashley ae598 300032 Sep 6 11:37 Dt23u.inp

-rw-r\--r\-- 1 ashley ae598 468500 Sep 6 11:38 Dt23u122.cod

-rw-r\--r\-- 1 ashley ae598 299520 Sep 6 11:38 Dt23u122.out

-rw-r\--r\-- 1 ashley ae598 379904 Sep 6 11:38 Dt24u.inp

-rw-r\--r\-- 1 ashley ae598 593500 Sep 6 11:39 Dt24u122.cod

-rw-r\--r\-- 1 ashley ae598 379392 Sep 6 11:39 Dt24u122.out
