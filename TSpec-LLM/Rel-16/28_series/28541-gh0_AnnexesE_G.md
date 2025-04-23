######## Annex E (normative): YANG definitions for NR NRM

E.1 General
===========

This annex contains the YANG definitions for the NR and NG-RAN NRM, in
accordance with NR and NG-RAN NRM information model definitions
specified in clause 4.

E.2 Void
========

E.3 Void
========

E.4 Void
========

E.5 Modules 
===========

E.5.1 module \_3gpp-nr-nrm-beam.yang
------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-beam {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-nrnetwork-beam\";

prefix \"beam3gpp\";

import \_3gpp-nr-nrm-commonbeamformingfunction { prefix cbeamff3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-nr-nrm-gnbdufunction { prefix gnbdu3gpp; }

import \_3gpp-nr-nrm-nrsectorcarrier { prefix nrsectcarr3gpp; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the Beam Information

Object Class (IOC) that is part of the NR Network Resource Model
(NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2019-11-22 {

description \"Initial revision\";

reference \"S5-197643\";

}

typedef BeamType {

type enumeration {

enum SSB-BEAM;

}

}

grouping BeamGrp {

description \"Represents the Beam IOC.\";

reference \"3GPP TS 28.541\";

uses mf3gpp:ManagedFunctionGrp;

leaf beamIndex {

description \"Index of the beam. \";

mandatory true;

type int32;

}

leaf beamType {

description \"The type of the beam. \";

mandatory false;

type BeamType;

}

leaf beamAzimuth {

description \"The azimuth of a beam transmission, which means the
horizontal beamforming pointing angle (beam peak direction) in the (Phi)
φ-axis in 1/10^th^ degree resolution. The pointing angle is the
direction equal to the geometric centre of the half-power contour of the
beam relative to the reference plane. Zero degree implies explicit
antenna bearing (boresight). Positive angle implies clockwise from the
antenna bearing.\";

reference \"3GPP TS 38.104, TS 38.901, TS 28.662\";

mandatory false;

type int32 { range \"-1800..1800\"; }

units \"0.1\";

}

leaf beamTilt {

description \"The tilt of a beam transmission, which means the vertical
beamforming pointing angle (beam peak direction) in the (Theta) θ-axis
in 1/10th degree resolution.

The pointing angle is the direction equal to the geometric centre of the
half-power contour of the beam relative to the reference plane. Positive
value implies downtilt.\";

reference \"3GPP TS 38.104, TS 38.901, TS 28.662\";

mandatory false;

type int32 { range \"-900..900\"; }

units \"0.1\";

}

leaf beamHorizWidth {

description \" The Horizontal beamWidth of a beam transmission, which
means the horizontal beamforming half-power (3dB down) beamwidth in the
(Phi) φ-axis in 1/10th degree resolution.\";

reference \"3GPP TS 38.104, TS 38.901\";

mandatory false;

type int32 { range \"0..3599\"; }

units \"0.1\";

}

leaf beamVertWidth {

description \" The Vertical beamWidth of a beam transmission, which
means the vertical beamforming half-power (3dB down) beamwidth in the
(Theta) θ-axis in 1/10th degree resolution.\";

reference \"3GPP TS 38.104, TS 38.901\";

mandatory false;

type int32 { range \"0..1800\"; }

units \"0.1\";

}

}

augment
\"/me3gpp:ManagedElement/gnbdu3gpp:GNBDUFunction/nrsectcarr3gpp:NRSectorCarrier/cbeamff3gpp:CommonBeamformingFunction\"
{

list Beam {

description \"Represents the per-Beam information required for, e.g.
beam performance management utilizing measurements generated in the RAN.
Can have spatial attributes of horizontal/azimuth (ie: Phi φ-axis) and
vertical/tilt (ie: Theta θ-axis) beam pointing direction and beam width
attributes.\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses BeamGrp;

}

}

}

}

\<CODE ENDS\>

E.5.1a module \_3gpp-nr-nrm-bwp.yang 
------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-bwp {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-bwp\";

prefix \"bwp3gpp\";

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-nr-nrm-gnbdufunction { prefix gnbdu3gpp; }

organization \"3GPP SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"Defines the YANG mapping of the BWP Information Object
Class

(IOC) that is part of the NR Network Resource Model (NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2021-01-25 { reference CR-0453; }

revision 2020-11-02 { reference CR-0409 ; }

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-17 { reference \"Initial revision\"; }

typedef CyclicPrefix {

type enumeration {

enum NORMAL;

enum EXTENDED;

}

}

typedef BwpContext {

type enumeration {

enum DL;

enum UL;

enum SUL;

}

}

typedef IsInitialBwp {

type enumeration {

enum INITIAL;

enum OTHER;

}

}

grouping BWPGrp {

description \"Represents the BWP IOC.\";

reference \"3GPP TS 28.541\";

uses mf3gpp:ManagedFunctionGrp;

leaf bwpContext {

description \"Identifies whether the object is used for downlink, uplink

or supplementary uplink.\";

mandatory true;

type BwpContext;

}

leaf isInitialBwp {

description \"Identifies whether the object is used for initial or other

BWP.\";

mandatory true;

type IsInitialBwp;

}

leaf subCarrierSpacing {

description \"Subcarrier spacing configuration for a BWP.\";

reference \"3GPP TS 38.104\";

mandatory true;

type uint32 { range \"15 \| 30 \| 60 \| 120\"; }

units kHz;

}

leaf cyclicPrefix {

description \"Cyclic prefix, which may be normal or extended.\";

reference \"3GPP TS 38.211\";

mandatory true;

type CyclicPrefix;

}

leaf startRB {

description \"Offset in common resource blocks to common resource block
0

for the applicable subcarrier spacing for a BWP.\";

reference \"N\_BWP\_start in 3GPP TS 38.211\";

mandatory true;

type uint32;

}

leaf numberOfRBs {

description \"Number of physical resource blocks for a BWP.\";

reference \"N\_BWP\_size in 3GPP TS 38.211\";

mandatory true;

type uint32;

}

}

augment \"/me3gpp:ManagedElement/gnbdu3gpp:GNBDUFunction\" {

list BWP {

description \"Represents a bandwidth part (BWP).\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses BWPGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

E.5.1b module \_3gpp-nr-nrm-commonbeamformingfunction.yang 
----------------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-commonbeamformingfunction {

yang-version 1.1;

namespace
\"urn:3gpp:sa5:\_3gpp-nr-nrm-nrnetwork-commonbeamformingfunction\";

prefix \"combeamformfunc3gpp\";

import \_3gpp-nr-nrm-nrsectorcarrier { prefix nrsectcarr3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-nr-nrm-gnbdufunction { prefix gnbdu3gpp; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the CommonBeamformingFuntion
Information

Object Class (IOC) that is part of the NR Network Resource Model
(NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2019-11-22 {

description \"Initial revision\";

reference \"S5-197643\";

}

grouping CommonBeamformingFunctionGrp {

description \"Represents the CommonBeamformingFunction IOC.\";

reference \"3GPP TS 28.541\";

uses mf3gpp:ManagedFunctionGrp;

leaf coverageShape {

description \"Identifies the sector carrier coverage shape described by
the envelope of the contained SSB beams. The coverage shape is
implementation dependent.\";

mandatory true;

type int32 { range \"0..65535\"; }

}

leaf digitalAzimuth {

description \"Digitally-controlled azimuth through beamforming. It
represents the horizontal pointing direction of the antenna relative to
the antenna bore sight, representing the total non-mechanical horizontal
pan of the selected coverageShape. Positive value gives azimuth to the
right and negative value gives an azimuth to the left.\";

reference \"3GPP TS 38.104, TS 38.901, TS 28.662\";

type int32 { range \"-1800..1800\"; }

units \"0.1\";

}

leaf digitalTilt {

description \"Digitally-controlled tilt through beamforming. It
represents the vertical pointing direction of the antenna relative to
the antenna bore sight, representing the total non-mechanical vertical
tilt of the selected coverageShape. Positive value gives downwards tilt
and negative value gives upwards tilt.\";

reference \"3GPP TS 38.104, TS 38.901, TS 28.662\";

type int32 { range \"-900..900\"; }

units \"0.1\";

}

}

augment
\"/me3gpp:ManagedElement/gnbdu3gpp:GNBDUFunction/nrsectcarr3gpp:NRSectorCarrier\"
{

list CommonBeamformingFunction {

description \"Represents common beamforming functionality (eg: SSB
beams) for the NRSectorCarrier.\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses CommonBeamformingFunctionGrp;

}

}

}

}

\<CODE ENDS\>

E.5.2 module\_3gpp-nr-nrm-ep.yang
---------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-ep {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-ep\";

prefix \"ep3gpp\";

import \_3gpp-common-ep-rp { prefix eprp3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-nr-nrm-gnbcucpfunction { prefix gnbcucp3gpp; }

import \_3gpp-nr-nrm-gnbcuupfunction { prefix gnbcuup3gpp; }

import \_3gpp-nr-nrm-gnbdufunction { prefix gnbdu3gpp; }

organization \"3GPP SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"Defines the YANG mapping of the NR related endpoint

Information Object Classes (IOCs) that are part of the NR Network

Resource Model (NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2021-04-30 { reference CR-0489; }

revision 2021-03-02 { reference CR-0434; }

revision 2021-01-16 { reference CR-0447; }

revision 2020-11-02 { reference CR-0409 ; }

revision 2020-03-02 { reference S5-201191; }

revision 2019-06-17 { reference \"Initial revision\"; }

feature EPClassesUnderGNBCUCPFunction {

description \"Endpoint classes shall be contained under
GNBCUCPFunction\";

}

feature EPClassesUnderGNBCUUPFunction {

description \"Endpoint classes shall be contained under
GNBCUUPFunction\";

}

feature EPClassesUnderGNBDUFunction {

description \"Endpoint classes shall be contained under GNBDUFunction\";

}

grouping EP\_E1Grp {

description \"Represents the EP\_E1 IOC.\";

reference \"3GPP TS 28.541, 3GPP TS 38.401\";

uses eprp3gpp:EP\_Common;

}

grouping EP\_F1CGrp {

description \"Represents the EP\_F1C IOC.\";

reference \"3GPP TS 28.541, 3GPP TS 38.470\";

uses eprp3gpp:EP\_Common;

}

grouping EP\_F1UGrp {

description \"Represents the EP\_F1U IOC.\";

reference \"3GPP TS 28.541, 3GPP TS 38.470\";

uses eprp3gpp:EP\_Common;

}

grouping EP\_XnCGrp {

description \"Represents the EP\_XnC IOC.\";

reference \"3GPP TS 28.541, 3GPP TS 38.420\";

uses eprp3gpp:EP\_Common;

}

grouping EP\_XnUGrp {

description \"Represents the EP\_XnU IOC.\";

reference \"3GPP TS 28.541, 3GPP TS 38.420\";

uses eprp3gpp:EP\_Common;

}

grouping EP\_NgCGrp {

description \"Represents the EP\_NgC IOC.\";

reference \"3GPP TS 28.541, 3GPP TS 38.470\";

uses eprp3gpp:EP\_Common;

}

grouping EP\_NgUGrp {

description \"Represents the EP\_NgU IOC.\";

reference \"3GPP TS 28.541, 3GPP TS 38.470\";

uses eprp3gpp:EP\_Common;

}

grouping EP\_X2CGrp {

description \"Represents the EP\_X2C IOC.\";

reference \"3GPP TS 28.541, 3GPP TS 36.423\";

uses eprp3gpp:EP\_Common;

}

grouping EP\_X2UGrp {

description \"Represents the EP\_X2U IOC.\";

reference \"3GPP TS 28.541, 3GPP TS 36.425\";

uses eprp3gpp:EP\_Common;

}

grouping EP\_S1UGrp {

description \"Represents the EP\_S1U IOC.\";

reference \"3GPP TS 28.541, 3GPP TS 36.410\";

uses eprp3gpp:EP\_Common;

}

augment \"/me3gpp:ManagedElement/gnbcucp3gpp:GNBCUCPFunction\" {

if-feature EPClassesUnderGNBCUCPFunction;

list EP\_E1 {

description \"Represents the local end point of the logical link,

supporting E1 interface between gNB-CU-CP and gNB-CU-UP.\";

reference \"3GPP TS 28.541, 3GPP TS 38.401\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_E1Grp;

}

}

list EP\_F1C {

description \"Represents the local end point of the control plane

interface (F1-C) between the gNB-DU and gNB-CU or gNB-CU-CP.\";

reference \"3GPP TS 28.541, 3GPP TS 38.470\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_F1CGrp;

}

}

list EP\_NgC {

description \"Represents the local end point of the control plane

interface (NG-C) between the gNB and AMF.\";

reference \"3GPP TS 28.541, 3GPP TS 38.470\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_NgCGrp;

}

}

list EP\_XnC {

description \"Represents the local gNB node end point of the logical

link, supporting Xn application protocols, to a neighbour NG-RAN node

(including gNB and ng-eNB). The Xn Application PDUs are carried over

SCTP/IP/Data link layer/Physical layer stack.\";

reference \"3GPP TS 28.541, 3GPP TS 38.420 subclause 7\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_XnCGrp;

}

}

list EP\_X2C {

description \"Represents the local end point of the logical link,

supporting X2-C application protocols used in EN-DC, to a neighbour

eNB or en-gNB node.\";

reference \"3GPP TS 28.541, 3GPP TS 36.423\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_X2CGrp;

}

}

}

augment \"/me3gpp:ManagedElement/gnbcuup3gpp:GNBCUUPFunction\" {

if-feature EPClassesUnderGNBCUUPFunction;

list EP\_E1 {

description \"Represents the local end point of the logical link,

supporting E1 interface between gNB-CU-CP and gNB-CU-UP.\";

reference \"3GPP TS 28.541, 3GPP TS 38.401\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_E1Grp;

}

}

list EP\_F1U {

description \"Represents the local end point of the user plane

interface (F1-U) between the gNB-DU and gNB-CU or gNB-CU-UP.\";

reference \"3GPP TS 28.541, 3GPP TS 38.470\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_F1UGrp;

}

}

list EP\_NgU {

description \"Represents the local end point of the NG user plane

(NG-U) interface between the gNB and UPF.\";

reference \"3GPP TS 28.541, 3GPP TS 38.470\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_NgUGrp;

}

}

list EP\_XnU {

description \"Represents the one end-point of a logical link supporting

the Xn user plane (Xn-U) interface. The Xn-U interface provides

non-guaranteed delivery of user plane PDUs between two NG-RAN nodes.\";

reference \"3GPP TS 28.541, 3GPP TS 38.420\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_XnUGrp;

}

}

list EP\_X2U {

description \"Represents the local end-point of a logical link
supporting

the X2 user plane (X2-U) interface used in EN-DC.\";

reference \"3GPP TS 28.541, 3GPP TS 36.425\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_X2UGrp;

}

}

list EP\_S1U {

description \"Represents the local end point of the logical link,

supporting S1-U interface towards a S-GW node.\";

reference \"3GPP TS 28.541, 3GPP TS 36.410\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_S1UGrp;

}

}

}

augment \"/me3gpp:ManagedElement/gnbdu3gpp:GNBDUFunction\" {

if-feature EPClassesUnderGNBDUFunction;

list EP\_F1C {

description \"Represents the local end point of the control plane

interface (F1-C) between the DU and CU or CU-CP.\";

reference \"3GPP TS 28.541, 3GPP TS 38.470\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_F1CGrp;

}

}

list EP\_F1U {

description \"Represents the local end point of the user plane

interface (F1-U) between the DU and CU or CU-UP.\";

reference \"3GPP TS 28.541, 3GPP TS 38.470\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_F1UGrp;

}

}

}

}

\<CODE ENDS\>

E.5.3 module \_3gpp-nr-nrm-eutrancellrelation.yang
--------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-eutrancellrelation {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-eutrancellrelation\";

prefix \"eutrancellrel3gpp\";

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-nr-nrm-gnbcucpfunction { prefix gnbcucp3gpp; }

import \_3gpp-nr-nrm-nrcellcu { prefix nrcellcu3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the EUtranCellRelation
Information

Object Class (IOC) that is part of the NR Network Resource Model
(NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-17 {

description \"Initial revision\";

}

typedef ActionAllowed {

type enumeration {

enum YES;

enum NO;

}

}

typedef EnergySavingCoverage {

type enumeration {

enum YES;

enum NO;

enum PARTIAL;

}

}

grouping EUtranCellRelationGrp {

description \"Represents the EUtranCellRelation IOC.\";

reference \"3GPP TS 28.541, EUtranRelation in 3GPP TS 28.658\";

uses mf3gpp:ManagedFunctionGrp;

leaf tCI {

description \"Target Cell Identifier. Consists of E-UTRAN Cell Global

Identifier (ECGI) and Physical Cell Identifier (PCI) of the target

cell. Identifies the target cell from the perspective of the parent

cell instance.\";

mandatory true;

type uint64;

}

leaf isRemoveAllowed {

description \"Indicates if the subject EUtranCellRelation can be removed

(deleted) or not. If YES, the subject EUtranCellRelation instance can

be removed (deleted). If NO, the subject EUtranCellRelation instance

shall not be removed (deleted) by any entity but an IRPManager.\";

mandatory true;

type ActionAllowed;

}

leaf isHOAllowed {

description \"Indicates if handover is allowed or prohibited. If YES,

handover is allowed from source cell to target cell. Source cell is

represented by the parent cell instance. Target cell is the adjacent

cell referenced by this EUtranCellRelation instance. If NO, handover

shall not be allowed.\";

mandatory true;

type ActionAllowed;

}

leaf isENDCAllowed {

description \"Indicates if EN-DC is allowed or prohibited. If TRUE,

the target cell is allowed to be used for EN-DC. The target cell is

referenced by the NRCellRelation that contains this isENDCAllowed.

If FALSE, EN-DC shall not be allowed.\";

mandatory true;

type ActionAllowed;

}

leaf isICICInformationSendAllowed {

description \"Indicates if ICIC (Inter Cell Interference Coordination)

load information message sending is allowed or prohibited. If YES,

ICIC load information message sending is allowed from source cell to

target cell. Source cell is represented by the parent cell instance.

Target cell is the adjacent cell referenced by this EUtranCellRelation

instance. If NO, ICIC load information message sending shall not be

allowed.\";

reference \"3GPP TS 36.423\";

mandatory true;

type ActionAllowed;

}

leaf isLBAllowed {

description \"Indicates if load balancing is allowed or prohibited from

source cell to target cell. If YES, load balancing is allowed from

source cell to target cell. Source cell is represented by the parent

cell instance. Target cell is the adjacent cell referenced by this

EUtranCellRelation instance. If NO, load balancing shall be prohibited

from source cell to target cell.\";

mandatory true;

type ActionAllowed;

}

leaf isESCoveredBy {

description \"Indicates whether the adjacent cell according to this

planning provides no, partial or full coverage for the parent cell

instance. Adjacent cells with this attribute equal to YES are

recommended to be considered as candidate cells to take over the

coverage when the original cell is about to be transferred to energy

saving state. The entirety of adjacent cells with this property equal

to PARTIAL are recommended to be considered as entirety of candidate

cells to take over the coverage when the original cell is about to be

transferred to energy saving state.\";

mandatory true;

type EnergySavingCoverage;

}

leaf qOffset {

description \"Offset applicable to a specific neighbouring cell used for

evaluating the cell as a candidate for cell re-selection. Corresponds

to parameter q-OffsetCell broadcast in SIB4 for intra-frequency cells

and in SIB5 for inter-frequency cells. Used for Mobility Robustness

Optimization.\";

reference \"3GPP TS 36.331\";

mandatory true;

type types3gpp:QOffsetRange;

}

leaf cellIndividualOffset {

description \"Offset applicable to a neighbouring cell. It is used for

evaluating the neighbouring cell for handover in connected mode. Used

by the HandOver parameter Optimization (HOO) function or Load

Balancing Optimization (LBO) function.\";

reference \"3GPP TS 36.331\";

config false;

type types3gpp:QOffsetRange;

}

leaf adjacentCell {

description \"Reference to an EUtranCellFDD/TDD or

ExternalEUtranCellFDD/TDD instance.\";

mandatory true;

type types3gpp:DistinguishedName;

}

}

augment
/me3gpp:ManagedElement/gnbcucp3gpp:GNBCUCPFunction/nrcellcu3gpp:NRCellCU
{

list EUtranCellRelation {

description \"Represents a relation between an NR cell and an E-UTRAN
cell.\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EUtranCellRelationGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

E.5.4 module \_3gpp-nr-nrm-eutranetwork.yang
--------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-eutranetwork {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-eutranetwork\";

prefix \"eutranet3gpp\";

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the EUtraNetwork Information
Object

Class (IOC) that is part of the NR Network Resource Model (NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2019-06-17 {

description \"Initial revision\";

}

feature ExternalsUnderEUtraNetwork {

description \"Classes representing external entities like
EUtranFrequency,

ExternalENBFunction are contained under a EUtraNetwork list/class.\";

}

grouping EUtraNetworkGrp {

description \"Represents the EUtraNetwork IOC.\";

reference \"3GPP TS 28.541\";

uses subnet3gpp:SubNetworkGrp;

}

list EUtraNetwork {

description \"A subnetwork containing gNB external E-UTRAN entities.\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EUtraNetworkGrp;

leaf-list parents {

description \"Reference to all containg EUtraNetwork instances

in strict order from the root EUtraNetwork down to the immediate

parent EUtraNetwork.

If EUtraNetworks form a containment hierarchy this is

modeled using references between the child EUtraNetwork and the parent

EUtraNetworks.

This reference MUST NOT be present for the top level EUtraNetwork and

MUST be present for other EUtraNetworks.\";

type leafref {

path \"../../../EUtraNetwork/id\";

}

}

leaf-list containedChildren{

description \"Reference to all directly contained EUtraNetwork
instances.

If EUtraNetworks form a containment hierarchy this is

modeled using references between the child EUtraNetwork and the parent

EUtraNetwork.\";

type leafref {

path \"../../../EUtraNetwork/id\";

}

}

}

}

}

\<CODE ENDS\>

E.5.5 module \_3gpp-nr-nrm-eutranfreqrelation.yang
--------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-eutranfreqrelation {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-eutranfreqrelation\";

prefix \"eutranfreqrel3gpp\";

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-nr-nrm-gnbcucpfunction { prefix gnbcucp3gpp; }

import \_3gpp-nr-nrm-nrcellcu { prefix nrcellcu3gpp; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the EUtranFreqRelation
Information

Object Class (IOC) that is part of the NR Network Resource Model
(NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-17 {

description \"Initial revision\";

}

grouping EUtranFreqRelationGrp {

description \"Represents the EUtranFreqRelation IOC.\";

reference \"3GPP TS 28.541\";

uses mf3gpp:ManagedFunctionGrp;

leaf cellIndividualOffset {

description \"Offset applicable to a neighbouring cell. Used for

evaluating the neighbouring cell for handover in connected mode.

Used by the HandOver parameter Optimization (HOO) function or

Load Balancing Optimization (LBO) function.\";

reference \"cellIndividualOffset in MeasObjectEUTRA in 3GPP TS 38.331\";

default 0;

type types3gpp:QOffsetRange;

}

leaf-list blackListEntry {

description \"A list of Physical Cell Identities (PCIs) that are

blacklisted in E-UTRAN measurements.\";

reference \"3GPP TS 38.331\";

min-elements 0;

type uint16 { range \"0..1007\"; }

}

leaf-list blackListEntryIdleMode {

description \"A list of Physical Cell Identities (PCIs) that are

blacklisted in SIB4 and SIB5.\";

min-elements 0;

type uint16 { range \"0..1007\"; }

}

leaf cellReselectionPriority {

description \"The absolute priority of the carrier frequency used by the

cell reselection procedure. Value 0 means lowest priority. The value

must not already used by other RAT, i.e. equal priorities between RATs

are not supported. The UE behaviour when no value is entered is

specified in subclause 5.2.4.1 of 3GPP TS 38.304.\";

reference \"CellReselectionPriority in 3GPP TS 38.331, priority in

3GPP TS 38.304\";

mandatory true;

type int32 { range \"0..7\"; }

}

leaf cellReselectionSubPriority {

description \"Indicates a fractional value to be added to the value of

cellReselectionPriority to obtain the absolute priority of the

concerned carrier frequency for E-UTRA and NR.\";

reference \"3GPP TS 38.331\";

type uint8 { range \"2 \| 4 \| 6 \| 8\"; }

units \"0.1\";

}

leaf pMax {

description \"Used for calculation of the parameter Pcompensation

(defined in 3GPP TS 38.304), at cell reselection to a cell.\";

reference \"PEMAX in 3GPP TS 38.101-1\";

mandatory true;

type int32 { range \"-30..33\"; }

units dBm;

}

leaf qOffsetFreq {

description \"The frequency specific offset applied when evaluating

candidates for cell reselection.\";

type int32;

default 0;

}

leaf qQualMin {

description \"Indicates the minimum required quality level in the cell.

Value 0 means that it is not sent and UE applies in such case the

(default) value of negative infinity for Qqualmin. Sent in SIB3 or

SIB5.\";

reference \"qQualMin in TS 38.304\";

mandatory true;

type int32 { range \"-34..-3 \| 0\"; }

units dB;

}

leaf qRxLevMin {

description \"Indicates the required minimum received Reference Symbol

Received Power (RSRP) level in the (E-UTRA) frequency for cell

reselection. Broadcast in SIB3 or SIB5, depending on whether the

related frequency is intra- or inter-frequency. Resolution is 2.\";

reference \"Qrxlevmin in 3GPP TS 38.304\";

mandatory true;

type int32 { range \"-140..-44\"; }

units dBm;

}

leaf threshXHighP {

description \"Specifies the Srxlev threshold used by the UE when

reselecting towards a higher priority RAT/frequency than the current

serving frequency. Each frequency of NR and E-UTRAN might have a

specific threshold. Resolution is 2.\";

reference \"ThreshX, HighP in 3GPP TS 38.304\";

mandatory true;

type int32 { range \"0..62\"; }

units dB;

}

leaf threshXHighQ {

description \"Specifies the Squal threshold used by the UE when

reselecting towards a higher priority RAT/frequency than the current

serving frequency. Each frequency of NR and E-UTRAN might have a

specific threshold.\";

reference \"ThreshX, HighQ in 3GPP TS 38.304\";

mandatory true;

type int32 { range 0..31; }

units dB;

}

leaf threshXLowP {

description \"Specifies the Srxlev threshold used by the UE when

reselecting towards a lower priority RAT/frequency than the current

serving frequency. Each frequency of NR and E-UTRAN might have a

specific threshold. Resolution is 2.\";

reference \"ThreshX, LowP in 3GPP TS 38.304\";

mandatory true;

type int32 { range \"0..62\"; }

units dB;

}

leaf threshXLowQ {

description \"Specifies the Squal threshold used by the UE when

reselecting towards a lower priority RAT/frequency than the current

serving frequency. Each frequency of NR and E-UTRAN might have a

specific threshold.\";

reference \"ThreshX, LowQ in 3GPP TS 38.304\";

mandatory false;

type int32 { range \"0..31\"; }

units dB;

}

leaf tReselectionEutra {

description \"Cell reselection timer for intra frequency E-UTRA cell

reselection. May be used for Mobility Robustness Optimization.\";

reference \"t-ReselectionEUTRA in 3GPP TS 36.331 and in 3GPP TS
23.207\";

mandatory true;

type uint8 { range \"0..7\"; }

units s;

}

leaf tReselectionEutraSfHigh {

description \"The attribute tReselectionEutra (parameter
TreselectionEUTRA

in 3GPP TS 38.304) multiplied with this scaling factor if the UE is in

high mobility state.\";

reference \"Speed dependent ScalingFactor for TreselectionEUTRA for high

mobility state in 3GPP TS 38.304\";

mandatory true;

type uint8 { range \"25 \| 50 \| 75 \| 100\"; }

units %;

}

leaf tReselectionEutraSfMedium {

description \"The attribute tReselectionEutra (parameter
TreselectionEUTRA

in 3GPP TS 38.304) multiplied with this scaling factor if the UE is in

medium mobility state.\";

reference \"Speed dependent ScalingFactor for TreselectionEUTRA for
medium

mobility state in 3GPP TS 38.304\";

mandatory true;

type uint8 { range \"25 \| 50 \| 75 \| 100\"; }

units %;

}

leaf eUtranFrequencyRef {

description \"Reference to a corresponding EUtranFrequency instance.\";

mandatory true;

type types3gpp:DistinguishedName;

}

}

augment
/me3gpp:ManagedElement/gnbcucp3gpp:GNBCUCPFunction/nrcellcu3gpp:NRCellCU
{

list EUtranFreqRelation {

description \"Represents a frequency relation between an NR cell and an

E-UTRAN cell.\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EUtranFreqRelationGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

E.5.6 module \_3gpp-nr-nrm-eutranfrequency.yang
-----------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-eutranfrequency {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-eutranfrequency\";

prefix \"eutraneteutranfreq3gpp\";

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-nr-nrm-eutranetwork { prefix eutranet3gpp; }

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the EUtranFrequency
Information

Object Class (IOC), that is part of the NR Network Resource Model
(NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM),

3GPP TS 28.658 (E-UTRAN) Network Resource Model (NRM)\";

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-17 {

description \"Initial revision\";

}

grouping EUtranFrequencyGrp {

description \"Represents the EUtranFrequency IOC.\";

reference \"3GPP TS 28.541\";

uses mf3gpp:ManagedFunctionGrp;

leaf earfcnDL {

description \"Specifies the channel number for the central DL
frequency.\";

reference \"3GPP TS 36.101\";

mandatory true;

type uint32 { range \"0..262143\"; }

}

leaf-list multiBandInfoListEutra {

description \"List of additional frequency bands the frequency belongs
to.\";

config false;

min-elements 0;

type uint16 { range \"1..256\"; }

}

}

grouping EUtranFrequencyWrapper {

list EUtranFrequency {

description \"Represents certain E-UTRAN frequency properties.\";

reference \"3GPP TS 28.658\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EUtranFrequencyGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

augment \"/subnet3gpp:SubNetwork\" {

if-feature subnet3gpp:ExternalsUnderSubNetwork ;

uses EUtranFrequencyWrapper ;

}

augment \"/eutranet3gpp:EUtraNetwork\" {

if-feature eutranet3gpp:ExternalsUnderEUtraNetwork;

uses EUtranFrequencyWrapper ;

}

}

\<CODE ENDS\>

E.5.7 module \_3gpp-nr-nrm-externalamffunction.yang
---------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-externalamffunction {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-externalamffunction\";

prefix \"extamf3gpp\";

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-nr-nrm-nrnetwork { prefix nrnet3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-common-yang-types { prefix types3gpp; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the ExternalAMFFunction
Information

Object Class (IOC) that is part of the NR Network Resource Model
(NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-17 {

description \"Initial revision\";

}

grouping ExternalAMFFunctionGrp {

description \"Represents the ExternalAMFFunction IOC.\";

reference \"3GPP TS 28.541\";

uses mf3gpp:ManagedFunctionGrp;

list pLMNIdList {

description \"List of at most six entries of PLMN Identifiers, but at
least

one (the primary PLMN Id).

The PLMN Identifier is composed of a Mobile Country Code (MCC) and a

Mobile Network Code (MNC).\";

min-elements 1;

max-elements 6;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

container aMFIdentifier {

presence true;

description \"An AMF identifier, comprising an AMF Region ID, an AMF Set
ID and an AMF Pointer.\";

uses types3gpp:AmfIdentifier;

}

}

grouping ExternalAMFFunctionWrapper {

list ExternalAMFFunction {

description \"Represents the properties, known by the management

function, of a AMFFunction managed by another management

function.\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses ExternalAMFFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

augment \"/subnet3gpp:SubNetwork\" {

if-feature subnet3gpp:ExternalsUnderSubNetwork ;

uses ExternalAMFFunctionWrapper;

}

augment \"/nrnet3gpp:NRNetwork\" {

if-feature nrnet3gpp:ExternalsUnderNRNetwork;

uses ExternalAMFFunctionWrapper;

}

}

\<CODE ENDS\>

E.5.8 module \_3gpp-nr-nrm-externalenbfunction.yang
---------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-externalenbfunction {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-externalenbfunction\";

prefix \"extenb3gpp\";

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-nr-nrm-eutranetwork { prefix eutranet3gpp; }

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the ExternalENBFunction

Information Object Class (IOC) that is part of the NR Network Resource

Model (NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM),

3GPP TS 28.658 (E-UTRAN) Network Resource Model (NRM)\";

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-17 {

description \"Initial revision\";

}

grouping ExternalENBFunctionGrp {

description \"Represets the ExternalENBFunction IOC.\";

reference \"3GPP TS 28.658\";

uses mf3gpp:ManagedFunctionGrp;

leaf eNBId {

description \"Unambiguously identifies an eNodeB within a PLMN.\";

reference \"3GPP TS 36.413, 3GPP TS 36.300\";

mandatory true;

type int32 { range \"0..268435455\"; } // Representing 28 bit eNB ID.

// 18, 20 and 21 bit eNB IDs also

// allowed.

}

}

grouping ExternalENBFunctionWrapper {

list ExternalENBFunction {

description \"Represents an external eNB functionality.\";

reference \"3GPP TS 28.658\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses ExternalENBFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

augment \"/subnet3gpp:SubNetwork\" {

if-feature subnet3gpp:ExternalsUnderSubNetwork ;

uses ExternalENBFunctionWrapper;

}

augment \"/eutranet3gpp:EUtraNetwork\" {

if-feature eutranet3gpp:ExternalsUnderEUtraNetwork;

uses ExternalENBFunctionWrapper;

}

}

\<CODE ENDS\>

E.5.9 module\_3gpp-nr-nrm-externaleutrancell.yang
-------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-externaleutrancell {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-externaleutrancell\";

prefix \"exteutrancell3gpp\";

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-nr-nrm-eutranetwork { prefix eutranet3gpp; }

import \_3gpp-nr-nrm-externalenbfunction { prefix extenb3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the ExternalEUtranCellFDD and

ExternalEUtranCellTDD Information Object Classes (IOCs) that are part

of the NR Network Resource Model (NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM),

3GPP TS 28.658 (E-UTRAN) Network Resource Model (NRM)\";

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-17 {

description \"Initial revision\";

}

grouping ExternalEUtranGenericCellGrp {

description \"Represents the ExternalEUtranGenericCell IOC.\";

reference \"3GPP TS 28.658\";

uses mf3gpp:ManagedFunctionGrp;

leaf pci {

description \"The Physical Cell Identity (PCI) of the cell (for

NM-Centralized, EM-Centralized and Distributed PCI assignment cases).

In the case of NM-Centralized PCI assignment, see 3GPP TS 36.300.\";

reference \"3GPP TS 36.211\";

mandatory true;

type int32 { range \"0..503\"; }

}

list plmnIdList {

description \"List of unique identities for PLMNs. A cell can broadcast

up to 6 PLMN IDs. This is to support the case that one cell can be

used by up to 6 operator\'s core networks. The PLMN(s) included in this

list will use the same single tracking area code (TAC) and the same

Cell Identity (cellLocalId) for sharing the radio access network

resources. One member of plmnIdList is the primary PLMN ID. A PLMN ID

included in this list cannot be included in the cellAccessInfoList.

The PLMN ID is composed of a Mobile Country Code (MCC) and a Mobile

Network Code (MNC).\";

reference \"3GPP TS 36.300, 3GPP TS 36.331, 3GPP TS 23.003\";

key \"mcc mnc\";

min-elements 1;

max-elements 6;

uses types3gpp:PLMNId;

}

leaf cellLocalId {

description \"Unambiguously identifies a cell within an eNodeB.\";

reference \"NCI defined in 3GPP TS 38.300\";

type int32 {range \"0..255\"; }

}

leaf eNBId {

description \"Unambiguously identifies an eNodeB within a PLMN.\";

reference \"3GPP TS 36.413, 3GPP TS 36.300\";

mandatory true;

type int32 { range \"0..268435455\"; } // Representing 28 bit eNB ID.

// 18, 20 and 21 bit eNB IDs also

// allowed.

}

}

grouping ExternalEUtranCellFDDGrp {

description \"Represents the ExternalEUtranCellFDD IOC.\";

reference \"3GPP TS 28.658\";

uses ExternalEUtranGenericCellGrp;

leaf earfcnDL {

description \"The channel number for the central DL frequency.\";

reference \"3GPP TS 36.101\";

mandatory true;

type int32 { range \"0..17999 \| 46590..262143\"; }

}

leaf earfcnUL {

description \"The channel number for the central UL frequency. Value 0

means that the UL channel number is N/A for the DL-only bands.\";

reference \"3GPP TS 36.101\";

mandatory true;

type int32 { range \"0 \| 18000..35999 \| 46590..262143\"; }

}

}

grouping ExternalEUtranCellTDDGrp {

description \"Represents the ExternalEUtranCellTDD IOC.\";

reference \"3GPP TS 28.658\";

uses ExternalEUtranGenericCellGrp;

leaf earfcn {

description \"The frequency number for the central frequency.\";

reference \"3GPP TS 36.104\";

mandatory true;

type int32 { range \"36000..262143\"; }

}

}

grouping ExternalEUtranCellFDDWrapper {

list ExternalEUtranCellFDD {

description \"Represents the common properties of external E-UTRAN FDD

cell provided by eNB or NG-RAN FDD cell provided by ng-eNB.\";

reference \"3GPP TS 28.658\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses ExternalEUtranCellFDDGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

grouping ExternalEUtranCellTDDWrapper {

list ExternalEUtranCellTDD {

description \"Represents the common properties of external E-UTRAN cell

TDD provided by eNB or NG-RAN TDD cell provided by ng-eNB.\";

reference \"3GPP TS 28.658\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses ExternalEUtranCellTDDGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

augment \"/subnet3gpp:SubNetwork/extenb3gpp:ExternalENBFunction\" {

if-feature subnet3gpp:ExternalsUnderSubNetwork;

uses ExternalEUtranCellFDDWrapper;

}

augment \"/eutranet3gpp:EUtraNetwork/extenb3gpp:ExternalENBFunction\" {

if-feature eutranet3gpp:ExternalsUnderEUtraNetwork;

uses ExternalEUtranCellFDDWrapper;

}

augment \"/subnet3gpp:SubNetwork/extenb3gpp:ExternalENBFunction\" {

if-feature subnet3gpp:ExternalsUnderSubNetwork;

uses ExternalEUtranCellTDDWrapper;

}

augment \"/eutranet3gpp:EUtraNetwork/extenb3gpp:ExternalENBFunction\" {

if-feature eutranet3gpp:ExternalsUnderEUtraNetwork;

uses ExternalEUtranCellTDDWrapper;

}

}

\<CODE ENDS\>

E.5.10 module \_3gpp-nr-nrm-externalgnbcucpfunction.yang
--------------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-externalgnbcucpfunction {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-externalgnbcucpfunction\";

prefix \"extgnbcucp3gpp\";

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-nr-nrm-nrnetwork { prefix nrnet3gpp; }

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the ExternalGNBCUCPFunction

Information Object Class (IOC), that is part of the NR Network Resource

Model (NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-17 {

description \"Initial revision\";

}

grouping ExternalGNBCUCPFunctionGrp {

description \"Represets the ExternalGNBCUCPFunction IOC.\";

reference \"3GPP TS 28.541\";

uses mf3gpp:ManagedFunctionGrp;

leaf gNBId {

description \"Identifies a gNB within a PLMN.\";

reference \"gNB Identifier (gNB ID) in 3GPP TS 38.300, Global gNB ID

in 3GPP TS 38.413\";

mandatory true;

type int64 { range \"0..4294967295\"; }

}

leaf gNBIdLength {

description \"Indicates the number of bits for encoding the gNB ID.\";

reference \"gNB ID in 3GPP TS 38.300, Global gNB ID in 3GPP TS 38.413\";

mandatory true;

type int32 { range \"22..32\"; }

}

list pLMNId {

description \"Specifies the PLMN identifier to be used as part of the

global RAN node identity.\";

key \"mcc mnc\";

min-elements 1;

max-elements 1;

uses types3gpp:PLMNId;

}

}

grouping ExternalGNBCUCPFunctionWrapper {

list ExternalGNBCUCPFunction {

description \"Represents the properties, known by the management
function,

of a GNBCUCPFunction managed by another management function.\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses ExternalGNBCUCPFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

augment \"/subnet3gpp:SubNetwork\" {

if-feature subnet3gpp:ExternalsUnderSubNetwork ;

uses ExternalGNBCUCPFunctionWrapper;

}

augment \"/nrnet3gpp:NRNetwork\" {

if-feature nrnet3gpp:ExternalsUnderNRNetwork;

uses ExternalGNBCUCPFunctionWrapper;

}

}

\<CODE ENDS\>

E.5.11 module \_3gpp-nr-nrm-externalgnbcuupfunction.yang
--------------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-externalgnbcuupfunction {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-externalgnbcuupfunction\";

prefix \"extgnbcuup3gpp\";

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-nr-nrm-nrnetwork { prefix nrnet3gpp; }

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the ExternalGNBCUUPFunction

Information Object Class (IOC), that is part of the NR Network

Resource Model (NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-17 {

description \"Initial revision\";

}

grouping ExternalGNBCUUPFunctionGrp {

description \"Represets the ExternalGNBCUUPFunction IOC.\";

reference \"3GPP TS 28.541\";

uses mf3gpp:ManagedFunctionGrp;

leaf gNBId {

description \"Identifies a gNB within a PLMN.\";

reference \"gNB Identifier (gNB ID) in 3GPP TS 38.300, Global gNB ID

in 3GPP TS 38.413\";

mandatory true;

type int64 { range \"0..4294967295\"; }

}

leaf gNBIdLength {

description \"Indicates the number of bits for encoding the gNB ID.\";

reference \"gNB ID in 3GPP TS 38.300, Global gNB ID in 3GPP TS 38.413\";

mandatory true;

type int32 { range \"22..32\"; }

}

}

grouping ExternalGNBCUUPFunctionWrapper {

list ExternalGNBCUUPFunction {

description \"Represents the properties, known by the management
function,

of a GNBCUUPFunction managed by another management function.\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses ExternalGNBCUUPFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

augment \"/subnet3gpp:SubNetwork\" {

if-feature subnet3gpp:ExternalsUnderSubNetwork ;

uses ExternalGNBCUUPFunctionWrapper;

}

augment \"/nrnet3gpp:NRNetwork\" {

if-feature nrnet3gpp:ExternalsUnderNRNetwork;

uses ExternalGNBCUUPFunctionWrapper;

}

}

\<CODE ENDS\>

E.5.12 module \_3gpp-nr-nrm-externalgnbdufunction.yang
------------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-externalgnbdufunction {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-externalgnbdufunction\";

prefix \"extgnbdu3gpp\";

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-nr-nrm-nrnetwork { prefix nrnet3gpp; }

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the ExternalGNBDUFunction

Information Object Class (IOC) that is part of the NR Network Resource

Model (NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-17 {

description \"Initial revision\";

}

grouping ExternalGNBDUFunctionGrp {

description \"Represets the ExternalGNBDUFunction IOC.\";

reference \"3GPP TS 28.541\";

uses mf3gpp:ManagedFunctionGrp;

leaf gNBId {

description \"Identifies a gNB within a PLMN.\";

reference \"gNB Identifier (gNB ID) in 3GPP TS 38.300, Global gNB ID

in 3GPP TS 38.413\";

mandatory true;

type int64 { range \"0..4294967295\"; }

}

leaf gNBIdLength {

description \"Indicates the number of bits for encoding the gNB ID.\";

reference \"gNB ID in 3GPP TS 38.300, Global gNB ID in 3GPP TS 38.413\";

mandatory true;

type int32 { range \"22..32\"; }

}

list pLMNId {

description \"Specifies the PLMN identifier to be used as part of the

global RAN node identity.\";

key \"mcc mnc\";

min-elements 1;

max-elements 1;

uses types3gpp:PLMNId;

}

}

grouping ExternalGNBDUFunctionWrapper {

list ExternalGNBDUFunction {

description \"Represents the properties, known by the management
function,

of a GNBDUFunction managed by another management function.\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses ExternalGNBDUFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

augment \"/subnet3gpp:SubNetwork\" {

if-feature subnet3gpp:ExternalsUnderSubNetwork ;

uses ExternalGNBDUFunctionWrapper;

}

augment \"/nrnet3gpp:NRNetwork\" {

if-feature nrnet3gpp:ExternalsUnderNRNetwork;

uses ExternalGNBDUFunctionWrapper;

}

}

\<CODE ENDS\>

E.5.13 module \_3gpp-nr-nrm-externalnrcellcu.yang
-------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-externalnrcellcu {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-externalnrcellcu\";

prefix \"extnrcellcu3gpp\";

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-nr-nrm-nrnetwork { prefix nrnet3gpp; }

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-nr-nrm-externalgnbcucpfunction { prefix extgnbcucp3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the ExternalNRCellCU
Information

Object Class (IOC), that is part of the NR Network Resource Model
(NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-17 {

description \"Initial revision\";

}

grouping ExternalNRCellCUGrp {

description \"Represents the ExternalNRCellCU IOC.\";

reference \"3GPP TS 28.541\";

uses mf3gpp:ManagedFunctionGrp;

leaf cellLocalId {

description \"Identifies an NR cell of a gNB. Together with
corresponding

gNB ID it forms the NR Cell Identifier (NCI).\";

reference \"NCI in 3GPP TS 38.300\";

mandatory true;

type int32 {range \"0..16383\"; }

}

leaf nRPCI {

description \"The Physical Cell Identity (PCI) of the NR cell.\";

reference \"3GPP TS 36.211\";

mandatory true;

type int32 { range \"0..1007\"; }

}

list pLMNIdList {

description \"Defines which PLMNs that are assumed to be served by the

NR cell in another gNB CU-CP. This list is either updated by the

managed element itself (e.g. due to ANR, signalling over Xn, etc.) or

by consumer over the standard interface.\";

key \"mcc mnc\";

min-elements 1;

max-elements 12;

uses types3gpp:PLMNId;

}

leaf nRFrequencyRef {

description \"Reference to corresponding NRFrequency instance.\";

mandatory true;

type types3gpp:DistinguishedName;

}

}

grouping ExternalNRCellCUWrapper {

list ExternalNRCellCU {

description \"Represents the properties of an NRCellCU controlled by

another Management Service Provider.\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses ExternalNRCellCUGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

augment
\"/subnet3gpp:SubNetwork/extgnbcucp3gpp:ExternalGNBCUCPFunction\" {

if-feature subnet3gpp:ExternalsUnderSubNetwork ;

uses ExternalNRCellCUWrapper;

}

augment \"/nrnet3gpp:NRNetwork/extgnbcucp3gpp:ExternalGNBCUCPFunction\"
{

if-feature nrnet3gpp:ExternalsUnderNRNetwork;

uses ExternalNRCellCUWrapper;

}

}

\<CODE ENDS\>

E.5.14 module \_3gpp-nr-nrm-externalservinggwfunction.yang
----------------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-externalservinggwfunction {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-externalservinggwfunction\";

prefix \"extservgw3gpp\";

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-nr-nrm-eutranetwork { prefix eutranet3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the ExternalServingGWFunction

Information Object Class (IOC) that is part of the NR Network Resource

Model (NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-17 {

description \"Initial revision\";

}

grouping ExternalServingGWFunctionGrp {

description \"Represents the ExternalServingGWFunction IOC.\";

reference \"3GPP TS 28.541\";

uses mf3gpp:ManagedFunctionGrp;

}

grouping ExternalServingGWFunctionWrapper {

list ExternalServingGWFunction {

description \"Represents the properties, known by the management

function, of a ServingGWFunction managed by another management

function.\";

reference \"3GPP TS 28.658\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses ExternalServingGWFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

augment \"/subnet3gpp:SubNetwork\" {

if-feature subnet3gpp:ExternalsUnderSubNetwork ;

uses ExternalServingGWFunctionWrapper;

}

augment \"/eutranet3gpp:EUtraNetwork\" {

if-feature eutranet3gpp:ExternalsUnderEUtraNetwork;

uses ExternalServingGWFunctionWrapper;

}

}

\<CODE ENDS\>

E.5.15 module \_3gpp-nr-nrm-externalupffunction.yang
----------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-externalupffunction {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-externalupffunction\";

prefix \"extupf3gpp\";

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-nr-nrm-nrnetwork { prefix nrnet3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the ExternalUPFFunction
Information

Object Class (IOC) that is part of the NR Network Resource Model
(NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-17 {

description \"Initial revision\";

}

grouping ExternalUPFFunctionGrp {

description \"Represents the ExternalUPFFunction IOC.\";

reference \"3GPP TS 28.541\";

uses mf3gpp:ManagedFunctionGrp;

}

grouping ExternalUPFFunctionWrapper {

list ExternalUPFFunction {

description \"Represents the properties, known by the management

function, of a UPFFunction managed by another management

function.\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses ExternalUPFFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

augment \"/subnet3gpp:SubNetwork\" {

if-feature subnet3gpp:ExternalsUnderSubNetwork ;

uses ExternalUPFFunctionWrapper;

}

augment \"/nrnet3gpp:NRNetwork\" {

if-feature nrnet3gpp:ExternalsUnderNRNetwork;

uses ExternalUPFFunctionWrapper;

}

}

\<CODE ENDS\>

E.5.16 module \_3gpp-nr-nrm-gnbcucpfunction.yang
------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-gnbcucpfunction {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-gnbcucpfunction\";

prefix \"gnbcucp3gpp\";

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-nr-nrm-rrmpolicy { prefix nrrrmpolicy3gpp; }

organization \"3GPP SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"Defines the YANG mapping of the GNBCUCPFunction
Information

Object Class (IOC) that is part of the NR Network Resource Model
(NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2020-10-02 { reference CR-0383 ; }

revision 2020-08-06 { reference \"CR-0333\"; }

revision 2020-08-03 { reference \"CR-0321\"; }

revision 2020-06-03 { reference \"CR-0286\"; }

revision 2020-05-08 { reference S5-203316 ; }

revision 2020-04-28 { reference \"0260\"; }

revision 2020-02-14 { reference S5-20XXXX ; }

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-17 {

description \"Initial revision\";

}

feature DESManagementFunction {

description \"Classs representing Distributed SON Energy Saving
feature\";

}

feature DANRManagementFunction {

description \"Classs representing D-SON function of ANR Management
feature\";

}

feature DMROFunction {

description \"Classs representing D-SON function of MRO feature\";

}

grouping GNBCUCPFunctionGrp {

description \"Represents the GNBCUCPFunction IOC.\";

reference \"3GPP TS 28.541\";

uses mf3gpp:ManagedFunctionGrp;

uses nrrrmpolicy3gpp:RRMPolicy\_Grp;

leaf gNBId {

description \"Identifies a gNB within a PLMN. The gNB Identifier (gNB
ID)

is part of the NR Cell Identifier (NCI) of the gNB cells.\";

reference \"gNB ID in 3GPP TS 38.300, Global gNB ID in 3GPP TS 38.413\";

mandatory true;

type int64 { range \"0..4294967295\"; }

}

leaf gNBIdLength {

description \"Indicates the number of bits for encoding the gNB ID.\";

reference \"gNB ID in 3GPP TS 38.300, Global gNB ID in 3GPP TS 38.413\";

mandatory true;

type int32 { range \"22..32\"; }

}

leaf gNBCUName {

description \"Identifies the Central Unit of an gNB.\";

reference \"3GPP TS 38.473\";

mandatory true;

type string { length \"1..150\"; }

}

list pLMNId {

description \"The PLMN identifier to be used as part of the global RAN

node identity.\";

key \"mcc mnc\";

min-elements 1;

max-elements 1;

uses types3gpp:PLMNId;

}

leaf-list x2BlackList {

type string;

description \"List of nodes to which X2 connections are prohibited.\";

}

leaf-list x2WhiteList {

type string;

description \"List of nodes to which X2 connections are enforced.\";

}

leaf-list xnBlackList {

type string;

description \"List of nodes to which Xn connections are prohibited.\";

}

leaf-list xnWhiteList {

type string;

description \"List of nodes to which X2 connections are enforced.\";

}

leaf-list xnHOBlackList {

type string;

description \"List of nodes to which handovers over Xn are
prohibited.\";

}

leaf configurable5QISetRef {

type types3gpp:DistinguishedName;

description \"DN of the Configurable5QISet that the GNBCUCPFunction
supports (is associated to).\";

}

leaf-list x2HOBlackList {

type string;

description \"List of nodes to which handovers over X2 are
prohibited.\";

}

leaf dynamic5QISetRef {

type types3gpp:DistinguishedName;

description \"DN of the Dynamic5QISet that the GNBCUCPFunction supports
(is associated to).\";

}

}

augment \"/me3gpp:ManagedElement\" {

list GNBCUCPFunction {

description \"Represents the logical function CU-CP of gNB and
en-gNB.\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses GNBCUCPFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

E.5.17 module \_3gpp-nr-nrm-gnbcuupfunction.yang
------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-gnbcuupfunction {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-gnbcuupfunction\";

prefix \"gnbcuup3gpp\";

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-nr-nrm-rrmpolicy { prefix nrrrmpolicy3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

organization \"3GPP SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"Defines the YANG mapping of the GNBCUUPFunction
Information

Object Class (IOC) that is part of the NR Network Resource Model
(NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2020-11-05 { reference CR-0411 ; }

revision 2020-08-06 { reference \"CR-0333\"; }

revision 2020-08-03 { reference \"CR-0321\"; }

revision 2020-06-03 { reference \"CR-0286\"; }

revision 2020-05-28 { reference \"CR-0318\"; }

revision 2020-03-12 { reference \"SP-200233 S5-201547\"; }

revision 2020-02-14 { reference S5-20XXXX ; }

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-08-21 { reference \"Initial revision\"; }

grouping TAIGrp {

description \"Tracking Area Identity\";

list pLMNId {

key \"mcc mnc\";

description \"PLMN IDs for the Tracking area\";

uses types3gpp:PLMNId;

}

leaf nRTAC {

type int64;

description \"Identity of the common Tracking Area Code for the PLMNs

allowedValues:

a\) It is the TAC or Extended-TAC.

b\) A cell can only broadcast one TAC or Extended-TAC.

See TS 36.300, subclause 10.1.7 (PLMNID and TAC relation).

c\) TAC is defined in subclause 19.4.2.3 of 3GPP TS 23.003 and

Extended-TAC is defined in subclause 9.3.1.29 of 3GPP TS 38.473.

d\) For a 5G SA (Stand Alone), it has a non-null value.\";

}

}

grouping BackhaulAddressGrp {

description \"Indicates the backhauladdress of gNB.\";

leaf gNBId {

type uint32 {

range \"0..4294967295\";

}

description \"It identifies a gNB within a PLMN. The gNB ID is part of

the NR Cell Identifier (NCI) of the gNB cells.\";

reference \"gNB Identifier (gNB ID) of subclause 8.2 of TS 38.300.

Global gNB ID in subclause 9.3.1.6 of TS 38.413\";

}

list tAI {

key nRTAC;

min-elements 1;

max-elements 1;

description \"Tracking Area Identity\";

reference \"subclause 9.3.3.11 in TS 38.413\";

uses TAIGrp;

}

}

grouping MappingSetIDBackhaulAddressGrp {

description \"Mapping relationship between setID and backhaulAddress of
gNB\";

leaf idx {

type uint32 ;

description \"ID value\";

}

leaf setID {

type uint32;

mandatory true;

description \"Indicates the setID of gNB.\";

reference \"Subclause 7.4.1.6 in TS 38.211\";

}

list backhaulAddress {

key gNBId;

min-elements 1;

max-elements 1;

description \"Indicates the backhauladdress of gNB.\";

uses BackhaulAddressGrp;

}

}

grouping GNBCUUPFunctionGrp {

description \"Represents the GNBCUUPFunction IOC.\";

reference \"3GPP TS 28.541\";

uses mf3gpp:ManagedFunctionGrp;

uses nrrrmpolicy3gpp:RRMPolicy\_Grp;

leaf gNBCUUPId {

type uint64 {

range \"0..68719476735\" ;

}

config false;

mandatory true;

description \"Identifies the gNB-CU-UP at least within a gNB-CU-CP\";

reference \"\'gNB-CU-UP ID\' in subclause 9.3.1.15 of 3GPP TS 38.463\";

}

leaf gNBId {

type uint32;

mandatory true;

description \"Identifies a gNB within a PLMN. The gNB ID is part of the

NR Cell Identifier (NCI) of the gNB cells. \";

reference \"gNB Identifier (gNB ID) of subclause 8.2 of TS 38.300.

Global gNB ID in subclause 9.3.1.6 of TS 38.413\";

}

leaf gNBIdLength {

mandatory true;

type int32 { range \"22..32\"; }

description \"Indicates the number of bits for encoding the gNB Id.\";

reference \"gNB Id in 3GPP TS 38.300, Global gNB ID in 3GPP TS 38.413\";

}

list pLMNInfoList {

description \"The PLMNInfoList is a list of PLMNInfo data type. It

defines which PLMNs that can be served by the GNBCUUPFunction and

which S-NSSAIs can be supported by the GNBCUUPFunction for

corresponding PLMN in case of network slicing feature is supported\";

key \"mcc mnc sd sst\";

uses types5g3gpp:PLMNInfo;

}

list mappingSetIDBackhaulAddressList {

key idx;

description \"Specifies a list of mappingSetIDBackhaulAddress used to

retrieve the backhaul address of the victim set.

Must be present if Remote Interference Management function is

supported.\";

uses MappingSetIDBackhaulAddressGrp;

}

leaf configurable5QISetRef {

type types3gpp:DistinguishedName;

description \"DN of the Configurable5QISet that the GNBCUUPFunction

supports (is associated to).\";

}

leaf dynamic5QISetRef {

type types3gpp:DistinguishedName;

description \"DN of the Dynamic5QISet that the GNBCUUPFunction

supports (is associated to).\";

}

}

augment \"/me3gpp:ManagedElement\" {

list GNBCUUPFunction {

key id;

description \"Represents the logical function CU-UP of gNB or en-gNB.\";

reference \"3GPP TS 28.541\";

uses top3gpp:Top\_Grp;

container attributes {

uses GNBCUUPFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

E.5.18 module\_3gpp-nr-nrm-gnbdufunction.yang
---------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-gnbdufunction {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-gnbdufunction\";

prefix \"gnbdu3gpp\";

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-nr-nrm-rrmpolicy { prefix nrrrmpolicy3gpp; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the GNBDUFunction Information

Object Class (IOC) that is part of the NR Network Resource Model
(NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2021-04-30 { reference CR-0489; }

revision 2020-10-02 { reference CR-0383 ; }

revision 2020-03-12 { reference \"SP-200233 S5-201547\" ; }

revision 2020-02-14 { reference S5-20XXXX ; }

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-08-21 {

description \"Initial revision.\";

}

feature DRACHOptimizationFunction {

description \"Classs representing D-SON function of RACH optimization

feature\";

}

grouping GNBDUFunctionGrp {

description \"Represents the GNBDUFunction IOC.\";

reference \"3GPP TS 28.541\";

uses mf3gpp:ManagedFunctionGrp;

uses nrrrmpolicy3gpp:RRMPolicy\_Grp;

leaf gNBId {

type int64 { range \"0..4294967295\"; }

mandatory true;

description \"Identifies a gNB within a PLMN. The gNB Identifier (gNB
ID)

is part of the NR Cell Identifier (NCI) of the gNB cells.\";

reference \"gNB ID in 3GPP TS 38.300, Global gNB ID in 3GPP TS 38.413\";

}

leaf gNBIdLength {

type int32 { range \"22..32\"; }

mandatory true;

description \"Indicates the number of bits for encoding the gNB ID.\";

reference \"gNB ID in 3GPP TS 38.300, Global gNB ID in 3GPP TS 38.413\";

}

leaf gNBDUId {

type int64 { range \"0..68719476735\"; }

mandatory true;

description \"Uniquely identifies the DU at least within a gNB.\";

reference \"3GPP TS 38.473\";

}

leaf gNBDUName {

type string { length \"1..150\"; }

description \"Identifies the Distributed Unit of an NR node\";

reference \"3GPP TS 38.473\";

}

leaf aggressorSetID {

type uint32 { range \"0..4194304\"; }

config false;

description \"Indicates the associated aggressor gNB Set ID of the cell

Valid when Remote Interference Management function is supported.\";

reference \"3GPP TS 38.211 subclause 7.4.1.6\";

}

leaf victimSetID {

type uint32 { range \"0..4194304\"; }

config false;

description \"Indicates the associated victim gNB Set ID of the cell

Valid when Remote Interference Management function is supported.\";

reference \"3GPP TS 38.211 subclause 7.4.1.6\";

}

}

augment \"/me3gpp:ManagedElement\" {

list GNBDUFunction {

key id;

description \"Represents the logical function DU of gNB or en-gNB.\";

reference \"3GPP TS 28.541\";

uses top3gpp:Top\_Grp;

container attributes {

uses GNBDUFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

E.5.19 module \_3gpp-nr-nrm-nrcellcu.yang
-----------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-nrcellcu {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-nrcellcu\";

prefix \"nrcellcu3gpp\";

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-nr-nrm-gnbcucpfunction { prefix gnbcucp3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

organization \"3GPP SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"Defines the YANG mapping of the NRCellCU Information
Object

Class (IOC) that is part of the NR Network Resource Model (NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2020-11-25 { reference CR-0385 ; }

revision 2020-11-05 { reference CR-0411 ; }

revision 2020-10-02 { reference CR-0383 ; }

revision 2020-05-08 { reference S5-203316 ; }

revision 2020-02-14 { reference S5-20XXXX ; }

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-17 { reference \"Initial revision\"; }

feature DPCIConfigurationFunction {

description \"Class representing Distributed SON

function of PCI configuration feature\";

}

feature DESManagementFunction {

description \"Class representing Distributed SON

Energy Saving feature\";

}

feature DMROFunction {

description \"Class representing D-SON function of MRO feature\";

}

feature CESManagementFunction {

description \"Class representing Centralized SON Energy Saving

feature\";

}

grouping NRCellCUGrp {

description \"Represents the NRCellCU IOC.\";

reference \"3GPP TS 28.541\";

uses mf3gpp:ManagedFunctionGrp;

leaf cellLocalId {

description \"Identifies an NR cell of a gNB. Together with
corresponding

gNB ID it forms the NR Cell Identifier (NCI).\";

mandatory true;

type int32 { range \"0..16383\"; }

}

list pLMNInfoList {

description \"The PLMNInfoList is a list of PLMNInfo data type. It
defines

which PLMNs that can be served by the NR cell, and which S-NSSAIs that

can be supported by the NR cell for corresponding PLMN in case of

network slicing feature is supported.\";

// Note: Whether the attribute pLMNId in the pLMNInfo can be writable

// depends on the implementation.

key \"mcc mnc sd sst\";

min-elements 1;

uses types5g3gpp:PLMNInfo;

}

leaf nRFrequencyRef {

description \"Reference to corresponding NRFrequency instance.\";

config false;

type types3gpp:DistinguishedName;

}

}

augment \"/me3gpp:ManagedElement/gnbcucp3gpp:GNBCUCPFunction\" {

list NRCellCU {

description \"Represents the information required by CU that is

responsible for the management of inter-cell mobility and neighbour

relations via ANR.\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses NRCellCUGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

E.5.20 module \_3gpp-nr-nrm-nrcelldu.yang
-----------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-nrcelldu {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-nrcelldu\";

prefix \"nrcelldu3gpp\";

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-nr-nrm-gnbdufunction { prefix gnbdu3gpp; }

import \_3gpp-nr-nrm-rrmpolicy { prefix nrrrmpolicy3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

organization \"3GPP SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"Defines the YANG mapping of the NRCellDU Information
Object

Class (IOC) that is part of the NR Network Resource Model (NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2020-11-25 { reference CR-0385 ; }

revision 2020-11-05 { reference CR-0411 ; }

revision 2020-10-02 { reference CR-0383; }

revision 2020-05-08 { reference S5-203316 ; }

revision 2020-02-14 { reference S5-20XXXX ; }

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-09-03 { reference \"Initial revision\"; }

feature DRACHOptimizationFunction {

description \"Class representing D-SON function of RACH optimization

feature\";

}

feature CPCIConfigurationFunction {

description \"Class representing Centralized SON function of

PCI configuration feature\";

}

grouping NRCellDUGrp {

description \"Represents the NRCellDU IOC.\";

reference \"3GPP TS 28.541\";

uses mf3gpp:ManagedFunctionGrp;

uses nrrrmpolicy3gpp:RRMPolicy\_Grp;

leaf cellLocalId {

description \"Identifies an NR cell of a gNB. Together with the

corresponding gNB identifier in forms the NR Cell Identity (NCI).\";

reference \"NCI in 3GPP TS 38.300\";

mandatory true;

type int32 { range \"0..16383\"; }

}

leaf operationalState {

description \"Operational state of the NRCellDU instance. Indicates

whether the resource is installed and partially or fully operable

(ENABLED) or the resource is not installed or not operable

(DISABLED).\";

config false;

type types3gpp:OperationalState;

}

leaf administrativeState {

description \"Administrative state of the NRCellDU. Indicates the

permission to use or prohibition against using the cell, imposed

through the OAM services.\";

type types3gpp:AdministrativeState;

default LOCKED;

}

leaf cellState {

description \"Cell state of the NRCellDU instance. Indicates whether the

cell is not currently in use (IDLE), or currently in use but not

configured to carry traffic (INACTIVE), or currently in use and is

configured to carry traffic (ACTIVE).\";

config false;

type types3gpp:CellState;

}

list pLMNInfoList {

description \"The PLMNInfoList is a list of PLMNInfo data type. It

defines which PLMNs that can be served by the NR cell, and which

S-NSSAIs that can be supported by the NR cell for corresponding PLMN

in case of network slicing feature is supported. The plMNId of the

first entry of the list is the PLMNId used to construct the nCGI for

the NR cell.\";

key \"mcc mnc sd sst\";

min-elements 1;

ordered-by user;

uses types5g3gpp:PLMNInfo;

}

leaf nRPCI {

description \"The Physical Cell Identity (PCI) of the NR cell.\";

reference \"3GPP TS 36.211\";

mandatory true;

type int32 { range \"0..1007\"; }

}

leaf nRTAC {

description \"The common 5GS Tracking Area Code for the PLMNs.\";

reference \"3GPP TS 23.003, 3GPP TS 38.473\";

type types3gpp:Tac;

}

leaf arfcnDL {

description \"NR Absolute Radio Frequency Channel Number (NR-ARFCN) for

downlink.\";

reference \"3GPP TS 38.104\";

mandatory true;

type int32;

}

leaf arfcnUL {

description \"NR Absolute Radio Frequency Channel Number (NR-ARFCN) for

uplink.\";

reference \"3GPP TS 38.104\";

type int32;

}

leaf arfcnSUL {

description \"NR Absolute Radio Frequency Channel Number (NR-ARFCN) for

supplementary uplink.\";

reference \"3GPP TS 38.104\";

type int32;

}

leaf bSChannelBwDL {

description \"Base station channel bandwidth for downlink.\";

reference \"3GPP TS 38.104\";

type int32;

units MHz;

}

leaf bSChannelBwUL {

description \"Base station channel bandwidth for uplink.\";

reference \"3GPP TS 38.104\";

type int32;

units MHz;

}

leaf bSChannelBwSUL {

description \"Base station channel bandwidth for supplementary
uplink.\";

reference \"3GPP TS 38.104\";

type int32;

units MHz;

}

leaf ssbFrequency {

description \"Indicates cell defining SSB frequency domain position.

Frequency (in terms of NR-ARFCN) of the cell defining SSB transmission.

The frequency identifies the position of resource element RE=\#0

(subcarrier \#0) of resource block RB\#10 of the SS block. The frequency

must be positioned on the NR global frequency raster, as defined in

3GPP TS 38.101-1, and within bSChannelBwDL.\";

mandatory true;

type int32 { range \"0..3279165\"; }

}

leaf ssbPeriodicity {

description \"Indicates cell defined SSB periodicity. The SSB
periodicity

is used for the rate matching purpose.\";

mandatory true;

type int32 { range \"5 \| 10 \| 20 \| 40 \| 80 \| 160\"; }

units \"subframes (ms)\";

}

leaf ssbSubCarrierSpacing {

description \"Subcarrier spacing of SSB. Only the values 15 kHz or 30
kHz

(\< 6 GHz), 120 kHz or 240 kHz (\> 6 GHz) are applicable.\";

reference \"3GPP TS 38.211\";

mandatory true;

type int32 { range \"15 \| 30 \| 120 \| 240\"; }

units kHz;

}

leaf ssbOffset {

description \"Indicates cell defining SSB time domain position. Defined

as the offset of the measurement window, in which to receive SS/PBCH

blocks, where allowed values depend on the ssbPeriodicity

(ssbOffset \< ssbPeriodicity).\";

mandatory true;

type int32 { range \"0..159\"; }

units \"subframes (ms)\";

}

leaf ssbDuration {

description \"Duration of the measurement window in which to receive

SS/PBCH blocks.\";

reference \"3GPP TS 38.213\";

mandatory true;

type int32 { range \"1..5\"; }

units \"subframes (ms)\";

}

leaf-list nRSectorCarrierRef {

description \"Reference to corresponding NRSectorCarrier instance.\";

min-elements 1;

type types3gpp:DistinguishedName;

}

leaf-list bWPRef {

description \"Reference to corresponding BWP instance.\";

type types3gpp:DistinguishedName;

}

leaf-list nRFrequencyRef {

description \"Reference to corresponding NRFrequency instance.\";

type types3gpp:DistinguishedName;

> }

}

augment \"/me3gpp:ManagedElement/gnbdu3gpp:GNBDUFunction\" {

list NRCellDU {

description \"Represents the information of a cell known by DU.\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses NRCellDUGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

E.5.21 module \_3gpp-nr-nrm-nrcellrelation.yang
-----------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-nrcellrelation {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-nrcellrelation\";

prefix \"nrcellrel3gpp\";

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-nr-nrm-gnbcucpfunction { prefix gnbcucp3gpp; }

import \_3gpp-nr-nrm-nrcellcu { prefix nrcellcu3gpp; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the NRCellRelation Information

Object Class (IOC) that is part of the NR Network Resource Model
(NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2021-01-25 { reference CR-0454 ; }

revision 2020-06-03 { reference S5-202333 ; }

revision 2020-04-23 { reference CR0281 ; }

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-08-30 {

description \"Initial revision\";

}

typedef EnergySavingCoverage {

type enumeration {

enum FULL;

enum NO;

enum PARTIAL;

}

}

grouping NRCellRelationGrp {

description \"Represents the NRCellRelation IOC.\";

reference \"3GPP TS 28.541\";

leaf nRTCI {

description \"Target NR Cell Identifier. It consists of NR Cell

Identifier (NCI) and Physical Cell Identifier of the target NR cell

(nRPCI).\";

type uint64;

}

container cellIndividualOffset {

description \"A set of offset values for the neighbour cell. Used when

UE is in connected mode. Defined for rsrpOffsetSSB, rsrqOffsetSSB,

sinrOffsetSSB, rsrpOffsetCSI-RS, rsrqOffsetCSI-RS and

sinrOffsetCSI-RS.\";

reference \"cellIndividualOffset in MeasObjectNR in 3GPP TS 38.331\";

leaf rsrpOffsetSsb {

description \"Offset value of rsrpOffsetSSB.\";

default 0;

type types3gpp:QOffsetRange;

}

leaf rsrqOffsetSsb{

description \"Offset value of rsrqOffsetSSB.\";

default 0;

type types3gpp:QOffsetRange;

}

leaf sinrOffsetSsb {

description \"Offset value of sinrOffsetSSB.\";

default 0;

type types3gpp:QOffsetRange;

}

leaf rsrpOffsetCsiRs{

description \"Offset value of rsrpOffsetCSI-RS.\";

default 0;

type types3gpp:QOffsetRange;

}

leaf rsrqOffsetCsiRs {

description \"Offset value of rsrqOffsetCSI-RS.\";

default 0;

type types3gpp:QOffsetRange;

}

leaf sinrOffsetCsiRs {

description \"Offset value of sinrOffsetCSI-RS.\";

default 0;

type types3gpp:QOffsetRange;

}

}

leaf nRFreqRelationRef {

description \"Reference to a corresponding NRFreqRelation instance.\";

mandatory true;

type types3gpp:DistinguishedName;

}

leaf adjacentNRCellRef {

description \"Reference to an adjacent NR cell (NRCellCU or

ExternalNRCellCU).\";

mandatory true;

type types3gpp:DistinguishedName;

}

leaf isRemoveAllowed {

type boolean;

default true;

description \"True if the ANR function in the node is allowed to remove
this relation.\";

}

leaf isHOAllowed {

type boolean;

default true;

description \"True if handovers are allowed over this relation.\";

}

leaf isESCoveredBy {

description \"Indicates whether the adjacent cell

provides no, partial or full coverage for the parent cell

instance. Adjacent cells with this attribute equal to FULL are

recommended to be considered as candidate cells to take over the

coverage when the original cell is about to be changed to energy

saving state. All adjacent cells with this property equal

to PARTIAL are recommended to be considered as entirety of candidate

cells to take over the coverage when the original cell is about to be

changed to energy saving state.\";

type EnergySavingCoverage;

}

}

augment
/me3gpp:ManagedElement/gnbcucp3gpp:GNBCUCPFunction/nrcellcu3gpp:NRCellCU
{

list NRCellRelation {

description \"Represents a neighbour cell relation from a source cell

to a target cell, where the target cell is an NRCellCU or

ExternalNRCellCU instance.\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses NRCellRelationGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

E.5.22 module \_3gpp-nr-nrm-nrfreqrelation.yang
-----------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-nrfreqrelation {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-nrfreqrelation\";

prefix \"nrfreqrel3gpp\";

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-nr-nrm-gnbcucpfunction { prefix gnbcucp3gpp; }

import \_3gpp-nr-nrm-nrcellcu { prefix nrcellcu3gpp; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the NRFreqRelation Information

Object Class (IOC) that is part of the NR Network Resource Model
(NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2020-04-23 { reference CR0281 ; }

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-17 {

description \"Initial revision\";

}

grouping NRFreqRelationGrp {

description \"Represents the NRFreqRelation IOC.\";

reference \"3GPP TS 28.541\";

container offsetMO {

description \"A set of offset values applicable to all measured cells

with reference signal(s) indicated in corresponding MeasObjectNR. It

is used to indicate a cell, beam or measurement object specific offset

to be applied when evaluating candidates for cell re-selection or when

evaluating triggering conditions for measurement reporting. It is

defined for rsrpOffsetSSB, rsrqOffsetSSB, sinrOffsetSSB,

rsrpOffsetCSI-RS, rsrqOffsetCSI-RS and sinrOffsetCSI-RS.\";

reference \"offsetMO in MeasObjectNR in 3GPP TS 38.331\";

leaf rsrpOffsetSsb {

description \"Offset value of rsrpOffsetSSB.\";

default 0;

type types3gpp:QOffsetRange;

}

leaf rsrqOffsetSsb {

description \"Offset value of rsrqOffsetSSB.\";

default 0;

type types3gpp:QOffsetRange;

}

leaf sinrOffsetSsb {

description \"Offset value of sinrOffsetSSB.\";

default 0;

type types3gpp:QOffsetRange;

}

leaf rsrpOffsetCsiRs {

description \"Offset value of rsrpOffsetCSI-RS.\";

default 0;

type types3gpp:QOffsetRange;

}

leaf rsrqOffsetCsiRs {

description \"Offset value of rsrqOffsetCSI-RS.\";

default 0;

type types3gpp:QOffsetRange;

}

leaf sinrOffsetCsiRs {

description \"Offset value of sinrOffsetCSI-RS.\";

default 0;

type types3gpp:QOffsetRange;

}

}

leaf-list blackListEntry {

description \"A list of Physical Cell Identities (PCIs) that are

blacklisted in NR measurements.\";

reference \"3GPP TS 38.331\";

min-elements 0;

type uint16 { range \"0..1007\"; }

}

leaf-list blackListEntryIdleMode {

description \"A list of Physical Cell Identities (PCIs) that are

blacklisted in SIB4 and SIB5.\";

min-elements 0;

type uint16 { range \"0..1007\"; }

}

leaf cellReselectionPriority {

description \"The absolute priority of the carrier frequency used by the

cell reselection procedure. Value 0 means lowest priority. The value

must not already used by other RAT, i.e. equal priorities between RATs

are not supported. The UE behaviour when no value is entered is

specified in subclause 5.2.4.1 of 3GPP TS 38.304.\";

reference \"CellReselectionPriority in 3GPP TS 38.331, priority in

3GPP TS 38.304\";

type uint32;

default 0;

}

leaf cellReselectionSubPriority {

description \"Indicates a fractional value to be added to the value of

cellReselectionPriority to obtain the absolute priority of the

concerned carrier frequency for E-UTRA and NR.\";

reference \"3GPP TS 38.331\";

type uint8 { range \"2 \| 4 \| 6 \| 8\"; }

units \"0.1\";

}

leaf pMax {

description \"Used for calculation of the parameter Pcompensation

(defined in 3GPP TS 38.304), at cell reselection to a cell.\";

reference \"PEMAX in 3GPP TS 38.101-1\";

mandatory false;

type int32 { range \"-30..33\"; }

units dBm;

}

leaf qOffsetFreq {

description \"The frequency specific offset applied when evaluating

candidates for cell reselection.\";

mandatory false;

type types3gpp:QOffsetRange;

default 0;

}

leaf qQualMin {

description \"Indicates the minimum required quality level in the cell.

Value 0 means that it is not sent and UE applies in such case the

(default) value of negative infinity for Qqualmin. Sent in SIB3 or

SIB5.\";

reference \"3GPP TS 38.304\";

type int32 { range \"-34..-3 \| 0\"; }

units dB;

default 0;

}

leaf qRxLevMin {

description \"Indicates the required minimum received Reference Symbol

Received Power (RSRP) level in the NR frequency for cell reselection.

Broadcast in SIB3 or SIB5, depending on whether the related frequency

is intra- or inter-frequency. Resolution is 2.\";

reference \"3GPP TS 38.304\";

mandatory true;

type int32 { range \"-140..-44\"; }

units dBm;

}

leaf threshXHighP {

description \"Specifies the Srxlev threshold used by the UE when

reselecting towards a higher priority RAT/frequency than the current

serving frequency. Each frequency of NR and E-UTRAN might have a

specific threshold. Resolution is 2.\";

reference \"ThreshX, HighP in 3GPP TS 38.304\";

mandatory true;

type int32 { range \"0..62\"; }

units dB;

}

leaf threshXHighQ {

description \"Specifies the Squal threshold used by the UE when

reselecting towards a higher priority RAT/frequency than the current

serving frequency. Each frequency of NR and E-UTRAN might have a

specific threshold.\";

reference \"ThreshX, HighQ in 3GPP TS 38.304\";

mandatory true;

type int32 { range \"0..31\"; }

units dB;

}

leaf threshXLowP {

description \"Specifies the Srxlev threshold used by the UE when

reselecting towards a lower priority RAT/frequency than the current

serving frequency. Each frequency of NR and E-UTRAN might have a

specific threshold. Resolution is 2.\";

reference \"ThreshX, LowP in 3GPP TS 38.304\";

mandatory true;

type int32 { range \"0..62\"; }

units dB;

}

leaf threshXLowQ {

description \"Specifies the Squal threshold used by the UE when

reselecting towards a lower priority RAT/frequency than the current

serving frequency. Each frequency of NR and E-UTRAN might have a

specific threshold.\";

reference \"ThreshX, LowQ in 3GPP TS 38.304\";

mandatory true;

type int32 { range \"0..31\"; }

units dB;

}

leaf tReselectionNR {

description \"Cell reselection timer for NR.\";

reference \"TreselectionRAT for NR in 3GPP TS 38.331\";

mandatory true;

type int32 { range \"0..7\"; }

units s;

}

leaf tReselectionNRSfHigh {

description \"The attribute tReselectionNr (parameter TreselectionNR in

3GPP TS 38.304) is multiplied with this scaling factor if the UE is

in high mobility state.\";

reference \"Speed dependent ScalingFactor for TreselectionNR for high

mobility state in 3GPP TS 38.304\";

mandatory true;

type uint8 { range \"25 \| 50 \| 75 \| 100\"; }

units %;

}

leaf tReselectionNRSfMedium {

description \"The attribute tReselectionNr (parameter TreselectionNR in

3GPP TS 38.304) multiplied with this scaling factor if the UE is in

medium mobility state.\";

reference \"Speed dependent ScalingFactor for TreselectionNR for medium

mobility state in 3GPP TS 38.304\";

mandatory true;

type uint8 { range \"25 \| 50 \| 75 \| 100\"; }

units %;

}

leaf nRFrequencyRef {

description \"Reference to a corresponding NRFrequency instance.\";

mandatory true;

type types3gpp:DistinguishedName;

}

}

augment
/me3gpp:ManagedElement/gnbcucp3gpp:GNBCUCPFunction/nrcellcu3gpp:NRCellCU
{

list NRFreqRelation {

description \"Together with the target NRFrequency, it represents the

frequency properties applicable to the referencing NRFreqRelation.\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses NRFreqRelationGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

E.5.23 module \_3gpp-nr-nrm-nrfrequency.yang
--------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-nrfrequency {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-nrnetwork-nrfrequency\";

prefix \"nrfreq3gpp\";

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-nr-nrm-nrnetwork { prefix nrnet3gpp; }

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the NRFrequency Information
Object

Class (IOC) that is part of the NR Network Resource Model (NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-17 {

description \"Initial revision\";

}

grouping NRFrequencyGrp {

description \"Represents the NRFrequency IOC.\";

reference \"3GPP TS 28.541\";

uses mf3gpp:ManagedFunctionGrp;

leaf absoluteFrequencySSB {

description \"The absolute frequency applicable for a downlink NR
carrier

frequency associated with the SSB, in terms of NR-ARFCN.\";

mandatory true;

type uint32 { range \"0.. 3279165\"; }

}

leaf sSBSubCarrierSpacing {

description \"Sub-carrier spacing of the SSB.\";

mandatory true;

type uint8 { range \"15 \| 30 \| 60 \| 120\"; }

units \"kHz\";

}

leaf-list multiFrequencyBandListNR {

description \"List of additional frequency bands the frequency belongs
to.

The list is automatically set by the gNB.\";

config false;

min-elements 0;

type uint16 { range \"1..256\"; }

}

}

grouping NRFrequencyWrapper {

list NRFrequency {

description \"Represents certain NR frequency properties.\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses NRFrequencyGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

augment \"/subnet3gpp:SubNetwork\" {

if-feature subnet3gpp:ExternalsUnderSubNetwork ;

uses NRFrequencyWrapper;

}

augment \"/nrnet3gpp:NRNetwork\" {

if-feature nrnet3gpp:ExternalsUnderNRNetwork;

uses NRFrequencyWrapper;

}

}

\<CODE ENDS\>

E.5.24 module \_3gpp-nr-nrm-nrnetwork.yang
------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-nrnetwork {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-nrnetwork\";

prefix \"nrnet3gpp\";

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the NRNetwork Information
Object

Class (IOC) that is part of the NR Network Resource Model (NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2019-06-17 {

description \"Initial revision\";

}

feature ExternalsUnderNRNetwork {

description \"Classes representing external entities like NRFrequency,

ExternalGNBCUCPFunction, ExternalGNBDUFunction

are contained under a NRNetwork list/class.\";

}

grouping NRNetworkGrp {

description \"Represents the NRNetwork IOC.\";

reference \"3GPP TS 28.541\";

uses subnet3gpp:SubNetworkGrp;

}

list NRNetwork {

description \"A subnetwork containing gNB external NR entities.\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses NRNetworkGrp;

}

}

}

\<CODE ENDS\>

E.5.25 module \_3gpp-nr-nrm-nrsectorcarrier.yang
------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-nrsectorcarrier {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-nrnetwork-nrsectorcarrier\";

prefix \"nrsectcarr3gpp\";

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-nr-nrm-gnbdufunction { prefix gnbdu3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3GPP SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"Defines the YANG mapping of the NRSectorCarrier
Information

Object Class (IOC) that is part of the NR Network Resource Model
(NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2020-05-28 { reference CR-0316 ; }

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-17 {

description \"Initial revision\";

}

grouping NRSectorCarrierGrp {

description \"Represents the NRSectorCarrier IOC.\";

reference \"3GPP TS 28.541\";

uses mf3gpp:ManagedFunctionGrp;

leaf txDirection {

description \"Indicates if the transmission direction is downlink,

uplink, or both downlink and uplink.\";

mandatory true;

type types3gpp:TxDirection;

}

leaf configuredMaxTxPower {

description \"Maximum transmisssion power at the antenna port for all

downlink channels, used simultaneously in a cell, added together.

Condition: The sector-carrier has a downlink and the

configuration of Tx power at antenna port reference point is
supported.\";

mandatory true;

type int32;

units mW;

}

leaf configuredMaxTxEIRP {

type int64;

units dBm;

mandatory true;

description \"The maximum emitted isotroptic radiated power (EIRP) in
dBm

for all downlink channels, used simultaneously in a cell, added
together.

Condition: the sector-carrier has a downlink and the

configuration of emitted isotropic radiated power is supported\";

}

leaf arfcnDL {

description \"NR Absolute Radio Frequency Channel Number (NR-ARFCN)

for downlink.

Condition: The sector-carrier has a downlink AND the value

differs from the referring cell\'s value of arfcnDL.\";

reference \"3GPP TS 38.104\";

mandatory true;

type int32 { range \"0..3279165\"; }

}

leaf arfcnUL {

description \"NR Absolute Radio Frequency Channel Number (NR-ARFCN)

for uplink.

Condition: The sector-carrier has an uplink AND the value

differs from the referring cell\'s value of arfcnUL.\";

reference \"3GPP TS 38.104\";

mandatory true;

type int32 { range \"0..3279165\"; }

}

leaf bSChannelBwDL {

description \"Base station channel bandwitdth for downlink.

Condition: The sector-carrier has a downlink AND the value

differs from the referring cell\'s value of bSChannelBwDL.\";

reference \"3GPP TS 38.104\";

mandatory true;

type int32 { range \"5 \| 10 \| 15 \| 20 \| 30 \| 40 \| 50 \| 60 \| 70
\| 80 \|

90 \| 100\"; }

units MHz;

}

leaf bSChannelBwUL {

description \"Base station channel bandwitdth for uplink.\";

reference \"3GPP TS 38.104\";

mandatory true;

type int32 { range \"5 \| 10 \| 15 \| 20 \| 30 \| 40 \| 50 \| 60 \| 70
\| 80 \|

90 \| 100\"; }

units MHz;

}

leaf sectorEquipmentFunctionRef {

description \"Reference to corresponding SectorEquipmentFunction

instance.\";

reference \"3GPP TS 23.622\";

mandatory true;

type types3gpp:DistinguishedName;

}

}

augment \"/me3gpp:ManagedElement/gnbdu3gpp:GNBDUFunction\" {

list NRSectorCarrier {

description \"Represents the resources of each transmission point

included in the cell.\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses NRSectorCarrierGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

E.5.26 module \_3gpp-nr-nrm-rrmpolicy.yang
------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-rrmpolicy {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-rrmpolicy\";

prefix nrrrmpolicy3gpp;

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3GPP SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"Defines the YANG mapping of the RRMPolicy abstract class
that

is part of the NR Network Resource Model (NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2020-11-05 { reference CR-0411 ; }

revision 2020-04-28 { reference \"CR0285\"; }

revision 2020-02-14 { reference \"Initial revision\"; }

grouping rRMPolicyMemberGrp {

description \"This data type represents an RRM Policy member that will
be

part of a rRMPolicyMemberList. A RRMPolicyMember is defined by its

pLMNId and sNSSAI (S-NSSAI).

The members in a rRMPolicyMemberList are assigned a specific amount of

RRM resources based on settings in RRMPolicy.\";

uses types5g3gpp:PLMNInfo;

}

typedef CyclicPrefix {

type enumeration {

enum NORMAL;

enum EXTENDED;

}

}

grouping RRMPolicy\_Grp {

description \"This IOC represents the properties of an abstract
RRMPolicy.

The RRMPolicy\_ IOC needs to be subclassed to be instantiated.

It defines two attributes apart from those inherited from Top IOC, the

resourceType attribute defines type of resource (PRB, RRC

connected users, DRB usage etc.) and the rRMPolicyMemberList attribute

defines the RRMPolicyMember(s)that are subject to this policy.

An RRM resource (defined in resourceType

attribute) is located in NRCellDU, NRCellCU, GNBDUFunction,

GNBCUCPFunction or in GNBCUUPFunction. The RRMPolicyRatio IOC is one

realization of a RRMPolicy\_ IOC. This RRM framework allows adding new

policies, both standardized (like RRMPolicyRatio) or as vendor specific,

by inheriting from the abstract RRMPolicy\_ IOC.\";

leaf resourceType {

description \"The resourceType attribute defines type of resource (PRB,

RRC connected users, DRB usage etc.) that is subject to policy.

Valid values are \'PRB\', \'RRC\' or \'DRB\'\";

mandatory true;

type string;

}

list rRMPolicyMemberList{

description \"It represents the list of RRMPolicyMember (s) that the

managed object is supporting. A RRMPolicyMember \<\<dataType\>\> include

the PLMNId \<\<dataType\>\> and S-NSSAI \<\<dataType\>\>.\" ;

min-elements 1;

   key \"mcc mnc sd sst\";

uses rRMPolicyMemberGrp;

}

} // grouping

grouping RRMPolicyRatioGrp {

description \"Represents the RRMPolicyRatio concrete IOC.\";

uses RRMPolicy\_Grp; // Inherits RRMPolicy\_

leaf rRMPolicyMaxRatio {

description \" This attribute specifies the maximum percentage of radio

resource that can be used by the associated rRMPolicyMemberList.

The maximum percentage of radio resource include at least one of

the shared resources, prioritized resources and dedicated resources.

The sum of the rRMPolicyMaxRatio values assigned to all
RRMPolicyRatio(s)

name-contained by same ManagedEntity can be greater that 100.\";

default 100;

type uint8 { range \"0..100\"; }

units percent;

}

leaf rRMPolicyMinRatio {

description \" This attribute specifies the minimum percentage of radio

resources that can be used by the associated rRMPolicyMemberList.

The minimum percentage of radio resources including at least one of

prioritized resources and dedicated resources. The sum of the

rRMPolicyMinRatio values assigned to all RRM PolicyRatio(s)

name-contained by same ManagedEntity shall be less or equal 100.\";

default 0;

type uint8 { range \"0..100\"; }

units percent;

}

leaf rRMPolicyDedicatedRatio {

description \" This attribute specifies the percentage of radio resource

that dedicatedly used by the associated rRMPolicyMemberList. The sum of

the rRMPolicyDeidctaedRatio values assigned to all RRMPolicyRatio(s)

name-contained by same ManagedEntity shall be less or equal 100. \";

default 0;

type uint8 { range \"0..100\"; }

units percent;

}

}

list RRMPolicyRatio {

description \" The RRMPolicyRatio IOC is one realization of a
RRMPolicy\_ IOC,

see the inheritance in Figure 4.2.1.2-1. This RRM framework allows

adding new policies, both standardized (like RRMPolicyRatio) or as

vendor specific, by inheriting from the

abstract RRMPolicy\_ IOC. For details see subclause 4.3.36.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses RRMPolicyRatioGrp;

}

}

}

\<CODE ENDS\>

E.5.27 Void
-----------

E.5.28 module \_3gpp-nr-nrm-danrmanagementfunction.yang
-------------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-danrmanagementfunction {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-danrmanagementfunction\";

prefix \"danrmanagementfunction3gpp\";

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-nr-nrm-gnbcucpfunction { prefix gnbcucp3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

organization \"3GPP SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"Defines the YANG mapping of the DANRManagementFunction
Information Object Class

(IOC) that is part of the NR Network Resource Model (NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2020-05-08 { reference S5-203316; }

grouping DANRManagementFunctionGrp {

description \"Represents the DANRManagementFunction IOC.\";

reference \"3GPP TS 28.541\";

uses top3gpp:Top\_Grp;

leaf intrasystemANRManagementSwitch {

description \"This attribute determines whether the intra-system ANR
function is activated or deactivated.\";

type boolean;

}

leaf intersystemANRManagementSwitch {

description \"This attribute determines whether the inter-system ANR
function is activated or deactivated.\";

type boolean;

}

}

augment \"/me3gpp:ManagedElement/gnbcucp3gpp:GNBCUCPFunction\" {

if-feature gnbcucp3gpp:DANRManagementFunction;

uses DANRManagementFunctionGrp;

}

}

\<CODE ENDS\>

E.5.29 module \_3gpp-nr-nrm-desmanagementfunction.yang
------------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-desmanagementfunction {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-desmanagementfunction\";

prefix \"desmf3gpp\";

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-nr-nrm-gnbcucpfunction { prefix gnbcucp3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-nr-nrm-nrcellcu { prefix nrcellcu3gpp; }

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-5g-common-yang-types { prefix type5g3gpp; }

organization \"3GPP SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"Defines the YANG mapping of the DESManagementFunction

Information Object Class (IOC) that is part of the NR Network Resource

Model (NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2021-08-04 { reference S5-214052/CR-0517; }

revision 2020-05-08 { reference S5-203316; }

grouping loadTimeThresholdGrp {

description \"Represents the the traffic load threshold and the time

duration.\";

leaf loadThreshold {

description \"This attribute is used by distributed ES algorithms to
allow

a cell to enter the energySaving state.\";

type type5g3gpp:EnergySavingLoadThresholdT;

}

leaf timeDuration {

description \"The time duration indicates how long the traffic load

(either for UL or DL) in the cell needs to have been above the

threshold to wake up one or more original cells which have been

provided backup coverage by the candidate cell.\";

type type5g3gpp:EnergySavingTimeDurationT;

}

}

grouping DESManagementFunctionGrp {

description \"Represents the DESManagementFunction IOC.\";

leaf desSwitch {

description \"This attribute determines whether the Distributed SON

energy saving function is enabled or disabled.\";

type boolean;

}

list intraRatEsActivationOriginalCellLoadParameters {

description \"This attributes is relevant, if the cell acts as an
original

cell. This attribute indicates the traffic load threshold and the time

duration, which are used by distributed ES algorithms to allow a cell

to enter the energySaving state.\";

key loadThreshold;

min-elements 1;

max-elements 1;

uses loadTimeThresholdGrp;

}

list intraRatEsActivationCandidateCellsLoadParameters {

description \"This attribute indicates the traffic load threshold and
the

time duration, which are used by distributed ES algorithms level to

allow an \'original\' cell to enter the energySaving state.\";

key loadThreshold;

min-elements 1;

max-elements 1;

uses loadTimeThresholdGrp;

}

list intraRatEsDeactivationCandidateCellsLoadParameters {

description \"This attributes is relevant, if the cell acts as a
candidate

cell.This attribute indicates the traffic load threshold and the time

duration which is used by distributed ES algorithms to allow a cell to

leave the energySaving state.\";

key loadThreshold;

min-elements 1;

max-elements 1;

uses loadTimeThresholdGrp;

}

list esNotAllowedTimePeriod {

description \"This is a list of time periods during which

inter-RAT energy saving is not allowed\";

key idx;

leaf idx {

type uint32;

}

uses EsNotAllowedTimePeriodGrp;

}

list interRatEsActivationOriginalCellParameters {

description \"This attribute indicates the traffic load threshold and
the

time duration, which are used by distributed inter-RAT ES algorithms to

allow an original cell to enter the energySaving state.\";

key loadThreshold;

min-elements 1;

max-elements 1;

uses loadTimeThresholdGrp;

}

list interRatEsActivationCandidateCellParameters {

description \"This attribute indicates the traffic load threshold and
the

time duration, which are used by distributed inter-RAT ES algorithms to

allow an original cell to enter the energySaving state.\";

key loadThreshold;

min-elements 1;

max-elements 1;

uses loadTimeThresholdGrp;

}

list interRatEsDeactivationCandidateCellParameters {

description \"This attribute indicates the traffic load threshold and
the

time duration which is used by distributed inter-RAT ES algorithms to

allow an original cell to leave the energySaving state.\";

key loadThreshold;

min-elements 1;

max-elements 1;

uses loadTimeThresholdGrp;

}

leaf energySavingState {

description \"Specifies the status regarding the energy saving in the

cell.\";

type enumeration {

enum isNotEnergySaving;

enum isEnergySaving;

}

}

leaf isProbingCapable {

description \"This attribute indicates whether this cell is capable of

performing the ES probing procedure.\";

type enumeration{

enum yes;

enum no;

}

}

}

grouping EsNotAllowedTimePeriodGrp {

leaf startTime {

description \"Start of not allowed time period in UTC time zone.

If set, the endTime must also be set. If not set, this is

interpreted as around the clock.\";

must ../endTime;

type type5g3gpp:UTC24TimeOfDayT;

}

leaf endTime {

description \"If endTime has a lower value than startTime, it will

be interpreted as referring to the following day.\";

type type5g3gpp:UTC24TimeOfDayT;

must ../startTime;

}

leaf-list daysOfWeek {

description \"Specifies that the not allowed periods are only

applicable to the specified days in UTC timezone. Every day if

not set.\";

type type5g3gpp:DayOfWeekT;

}

}

grouping DESManagementFunctionSubtree {

list DESManagementFunction {

description \"This IOC represents the management capabilities of

Distributed SON Energy Saving (ES) functions. This is provided for

Energy Saving purposes.

In the case where multiple DESManagement MOIs exist at different

levels of the containment tree, the DESManagement MOI at the lower

level overrides the DESManagement MOIs at higher level(s) of the same

containment tree.\";

reference \"clause 6.2.3.0 in TS 28.310\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses DESManagementFunctionGrp;

}

}

}

augment \"/me3gpp:ManagedElement/gnbcucp3gpp:GNBCUCPFunction/\"+

\"nrcellcu3gpp:NRCellCU\" {

if-feature nrcellcu3gpp:DESManagementFunction;

uses DESManagementFunctionSubtree;

}

augment /me3gpp:ManagedElement/gnbcucp3gpp:GNBCUCPFunction {

if-feature gnbcucp3gpp:DESManagementFunction;

uses DESManagementFunctionSubtree;

}

augment /me3gpp:ManagedElement {

if-feature me3gpp:DESManagementFunction;

uses DESManagementFunctionSubtree;

}

augment /subnet3gpp:SubNetwork {

if-feature subnet3gpp:DESManagementFunction;

uses DESManagementFunctionSubtree;

}

}

\<CODE ENDS\>

E.5.30 module \_3gpp-nr-nrm-drachoptimizationfunction.yang
----------------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-drachoptimizationfunction {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-drachoptimizationfunction\";

prefix \"dracho3gpp\";

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-nr-nrm-nrcelldu { prefix nrcelldu3gpp; }

import \_3gpp-nr-nrm-gnbdufunction { prefix gnbdu3gpp; }

organization \"3GPP SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"Defines the YANG mapping of the DRACHOptimizationFunction

Information Object Class (IOC) that is part of the NR Network Resource

Model (NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2021-08-04 { reference S5-214052/CR-0517; }

revision 2021-01-25 { reference CR-0454 ; }

revision 2020-10-02 { reference \"CR-0384, CR-0382\" ; }

revision 2020-05-08 { reference S5-203316; }

typedef TargetProbabilityT {

type enumeration {

enum 25;

enum 50;

enum 75;

enum 90;

}

}

typedef NumberofpreamblessentT {

type uint32 {

range \"1..200\";

}

}

typedef AccessdelayT {

type uint32 {

range \"10..560\";

}

}

grouping NumPreableAccessDelayGrp {

description \"Represents the target Access Probability (APn) for the
RACH

optimization function.\";

leaf targetProbability {

description \"This attribute determines the target Probability.\";

mandatory true;

type TargetProbabilityT;

}

leaf numberofpreamblessent {

description \"This attribute determines the number of preambles sent.\";

mandatory true;

type NumberofpreamblessentT;

}

}

grouping DRACHOptimizationFunctionGrp {

description \"Represents the DRACHOptimizationFunction IOC.\";

list ueAccProbilityDist {

description \"This is a list of target Access Probability (APn) for the

RACH optimization function.\";

key \"targetProbability numberofpreamblessent\";

uses NumPreableAccessDelayGrp;

}

list ueAccDelayProbilityDist {

description \"This is a list of target Access Delay probability (ADP)

for the RACH optimization function.\";

key \"targetProbability numberofpreamblessent\";

uses NumPreableAccessDelayGrp;

}

leaf drachOptimizationControl {

description \"This attribute determines whether the RACH Optimization

function is enabled or disabled.\";

type boolean;

}

}

grouping DRACHOptimizationFunctionSubtree {

list DRACHOptimizationFunction {

description \"This IOC represents the management capabilities of

Centralized SON Energy Saving (ES) functions. This is provided for

Energy Saving purposes.

In the case where multiple CESManagement MOIs exist at different

levels of the containment tree, the CESManagement MOI at the lower

level overrides the CESManagement MOIs at higher level(s) of the

same containment tree.\";

reference \"clause 6.2.2 in TS 28.310\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses DRACHOptimizationFunctionGrp;

}

}

}

augment \"/me3gpp:ManagedElement/gnbdu3gpp:GNBDUFunction/\"+

\"nrcelldu3gpp:NRCellDU\" {

if-feature nrcelldu3gpp:DRACHOptimizationFunction;

uses DRACHOptimizationFunctionSubtree;

}

augment \"/me3gpp:ManagedElement/gnbdu3gpp:GNBDUFunction\" {

if-feature gnbdu3gpp:DRACHOptimizationFunction;

uses DRACHOptimizationFunctionSubtree;

}

augment \"/me3gpp:ManagedElement\" {

if-feature me3gpp:DRACHOptimizationFunction;

uses DRACHOptimizationFunctionSubtree;

}

augment \"/subnet3gpp:SubNetwork\" {

if-feature nrcelldu3gpp:DRACHOptimizationFunction;

uses DRACHOptimizationFunctionSubtree;

}

}

\<CODE ENDS\>

E.5.31 module \_3gpp-nr-nrm-dmrofunction.yang
---------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-dmrofunction {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-dmrofunction\";

prefix \"dmrof3gpp\";

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-nr-nrm-gnbcucpfunction { prefix gnbcucp3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-nr-nrm-nrcellcu { prefix nrcellcu3gpp; }

organization \"3GPP SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"Defines the YANG mapping of the DMROFunction

Information Object Class (IOC) that is part of the NR Network Resource

Model (NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2021-08-04 { reference S5-214052/CR-0517; }

revision 2020-05-08 { reference S5-203316; }

grouping DMROFunctionGrp {

description \"Represents the DMROFunction IOC.\";

leaf maximumDeviationHoTrigger {

description \"This parameter defines the maximum allowed absolute

deviation of the Handover Trigger, from the default point of

operation. Range -20 to 20 in .5 dB steps. \";

type string {

pattern \'-?((20)\|(1?\[0-9\]))\\.\[05\]\';

// -20.0, -19.5, -19.0, \..., -0.5, 0.0, 0.5, 1.0, \... 19.5, 20.0

}

units dB;

}

leaf minimumTimeBetweenHoTriggerChange {

description \"This parameter defines the minimum allowed time interval

between two Handover Trigger change performed by MRO. This is used to

control the stability and convergence of the algorithm.\";

type uint32 {

range 0..604800; // \<= 1 week

}

units seconds;

}

leaf tstoreUEcntxt {

description \"The timer used for detection of too early HO, too late HO

and HO to wrong cell.\";

type uint32 {

range 0..1023;

}

units \"100 milliseconds\";

}

leaf dmroControl {

description \"This attribute determines whether the MRO function is

enabled or disabled.\";

type boolean;

}

}

grouping DMROFunctionSubtree {

list DMROFunction {

description \"This IOC contains attributes to support the D-SON function

of MRO.

In the case where multiple DMRO MOIs exist at different levels of the

containment tree, the DMRO MOI at the lower level overrides the DMRO

MOIs at higher level(s) of the same containment tree.\";

reference \"clause 7.1.2 in TS 28.313\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses DMROFunctionGrp;

}

}

}

augment \"/me3gpp:ManagedElement/gnbcucp3gpp:GNBCUCPFunction/\"+

\"nrcellcu3gpp:NRCellCU\" {

if-feature nrcellcu3gpp:DMROFunction;

uses DMROFunctionSubtree;

}

augment /me3gpp:ManagedElement/gnbcucp3gpp:GNBCUCPFunction {

if-feature gnbcucp3gpp:DMROFunction;

uses DMROFunctionSubtree;

}

augment /me3gpp:ManagedElement {

if-feature me3gpp:DMROFunction;

uses DMROFunctionSubtree;

}

augment /subnet3gpp:SubNetwork {

if-feature subnet3gpp:DMROFunction;

uses DMROFunctionSubtree;

}

}

\<CODE ENDS\>

E.5.32 module \_3gpp-nr-nrm-dpciconfigurationfunction.yang
----------------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-dpciconfigurationfunction {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-dpciconfigurationfunction\";

prefix \"dpcicf3gpp\";

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-nr-nrm-nrcellcu { prefix nrcellcu3gpp; }

import \_3gpp-nr-nrm-gnbcucpfunction { prefix gnbcucp3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-5g-common-yang-types { prefix type5g3gpp; }

organization \"3GPP SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"Defines the YANG mapping of the DPCIConfigurationFunction

Information Object Class (IOC) that is part of the NR Network Resource

Model (NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2021-08-04 { reference S5-214052/CR-0517; }

revision 2020-11-25 { reference CR-0385 ; }

revision 2020-05-08 { reference S5-203316; }

grouping DPCIConfigurationFunctionGrp {

description \"Represents the DPCICONFIGURATIONFunction IOC.\";

list nRPciList {

description \"This holds a list of physical cell identities that can be

assigned to the NR cells. This attribute shall be supported if D-SON

PCI configuration function is supported.\";

key NRPci;

leaf NRPci {

type type5g3gpp:PhysCellID;

}

}

leaf dPciConfigurationControl {

description \"This attribute determines whether the Distributed SON PCI

configuration Function is enabled or disabled.\";

type boolean;

}

}

grouping DPCIConfigurationFunctionSubtree {

list DPCIConfigurationFunction {

description \"This IOC contains attributes to support the Distributed
SON

function of PCI configuration.

In the case where multiple DPCIConfiguration MOIs exist at different

levels of the containment tree, the DPCIConfiguration MOI at the lower

level overrides the DPCIConfiguration MOIs at higher level(s) of the

same containment tree.\";

reference \"clause 7.1.3 in TS 28.313\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses DPCIConfigurationFunctionGrp;

}

}

}

augment \"/me3gpp:ManagedElement/gnbcucp3gpp:GNBCUCPFunction/\"+

\"nrcellcu3gpp:NRCellCU\" {

if-feature nrcellcu3gpp:DPCIConfigurationFunction;

uses DPCIConfigurationFunctionSubtree;

}

augment /me3gpp:ManagedElement {

if-feature me3gpp:DPCIConfigurationFunction;

uses DPCIConfigurationFunctionSubtree;

}

augment /subnet3gpp:SubNetwork {

if-feature subnet3gpp:DPCIConfigurationFunction;

uses DPCIConfigurationFunctionSubtree;

}

}

\<CODE ENDS\>

E.5.33 module \_3gpp-nr-nrm-cpciconfigurationfunction.yang
----------------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-cpciconfigurationfunction {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-cpciconfigurationfunction\";

prefix \"cpcicf3gpp\";

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-nr-nrm-nrcelldu { prefix nrcelldu3gpp; }

import \_3gpp-nr-nrm-gnbdufunction { prefix gnbdu3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

organization \"3GPP SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"Represents the CPCIConfigurationFunction Information
Object

Class(IOC) that is part of the NR Network Resource Model.\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2021-08-04 { reference S5-214052/CR-0517; }

revision 2020-05-08 { reference S5-203316; }

grouping CPCIConfigurationFunctionGrp {

description \"Represents the CPCIConfigurationFunction IOC.\";

leaf cPciConfigurationControl {

description \"This attribute determines whether the Centralized SON

PCI configuration function is enabled or disabled.\";

type boolean;

mandatory true;

}

leaf-list cSonPciList {

type int32 { range \"0..1007\"; }

min-elements 1;

description \"Holds a list of physical cell identities that can be

assigned to the pci attribute by gNB. The assignment algorithm is not

specified.

See TS 38.211 clause 7.4.2.1 for legal values of pci.

This attribute shall be supported if and only if the C-SON PCI

configuration is supported.\";

reference \"See TS 38.211 clause 7.4.2.1\";

}

}

grouping CPCIConfigurationFunctionSubtree {

list CPCIConfigurationFunction {

description \"This IOC contains attributes to support the Cross

Domain-Centralized SON function of PCI configuration

In the case where multiple CPCIConfiguration MOIs exist at different

levels of the containment tree, the CPCIConfiguration MOI at the lower

level overrides the CPCIConfiguration MOIs at higher level(s) of the

same containment tree.\";

reference \"clause 7.2.1 in TS 28.313\";

key id;

uses top3gpp:Top\_Grp ;

container attributes {

uses CPCIConfigurationFunctionGrp ;

}

}

}

augment
/me3gpp:ManagedElement/gnbdu3gpp:GNBDUFunction/nrcelldu3gpp:NRCellDU {

if-feature nrcelldu3gpp:CPCIConfigurationFunction;

uses CPCIConfigurationFunctionSubtree;

}

augment /me3gpp:ManagedElement {

if-feature me3gpp:CPCIConfigurationFunction;

uses CPCIConfigurationFunctionSubtree;

}

augment /subnet3gpp:SubNetwork {

if-feature subnet3gpp:CPCIConfigurationFunction;

uses CPCIConfigurationFunctionSubtree;

}

}

\<CODE ENDS\>

E.5.34 module \_3gpp-nr-nrm-cesmanagementfunction.yang
------------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-nr-nrm-cesmanagementfunction {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-nr-nrm-cesmanagementfunction\";

prefix \"cesmf3gpp\";

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-nr-nrm-nrcellcu { prefix nrcellcu3gpp; }

import \_3gpp-nr-nrm-gnbcucpfunction { prefix gnbcucp3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-5g-common-yang-types { prefix type5g3gpp; }

organization \"3GPP SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"Defines the YANG mapping of the CESManagementFunction

Information Object Class (IOC) that is part of the NR Network Resource
Model

(NRM).\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2021-08-04 { reference S5-214052/CR-0517; }

revision 2020-05-08 { reference S5-203316; }

grouping loadTimeThresholdGrp {

description \"Represents the the traffic load threshold and the time

duration.\";

leaf loadThreshold {

description \"This attribute is used by distributed ES algorithms to
allow

a cell to enter the energySaving state.\";

type type5g3gpp:EnergySavingLoadThresholdT;

}

leaf timeDuration {

description \"The time duration indicates how long the traffic load

(either for UL or DL) in the cell needs to have been above the

threshold to wake up one or more original cells which have been

provided backup coverage by the candidate cell.\";

type type5g3gpp:EnergySavingLoadThresholdT;

}

}

grouping CESManagementFunctionGrp {

description \"Represents the CESManagementFunction IOC.\";

leaf cesSwitch {

description \"This attribute determines whether the Centralized SON
energy

saving function is enabled or disabled.\";

type boolean;

default true;

}

list intraRatEsActivationOriginalCellLoadParameters {

description \"This attributes is relevant, if the cell acts as an
original

cell.This attribute indicates the traffic load threshold and the time

duration, which are used by distributed ES algorithms to allow a cell

to enter the energySaving state. The time duration indicates how long

the load needs to have been below the threshold.\";

key loadThreshold;

min-elements 1;

max-elements 1;

uses loadTimeThresholdGrp;

}

list intraRatEsActivationCandidateCellsLoadParameters {

description \"This attributes is relevant, if the cell acts as a
candidate

cell. This attribute indicates the traffic load threshold and the time

duration, which are used by distributed ES algorithms level to allow an

\'original\' cell to enter the energySaving state. Threshold and
duration

are applied to the candidate cell(s) which will provides coverage

backup of an original cell when it is in the energySaving state. The

threshold applies in the same way for a candidate cell, no matter for

which original cell it will provide backup coverage.

The time duration indicates how long the traffic in the candidate cell

needs to have been below the threshold before any original cells which

will be provided backup coverage by the candidate cell enters energy

saving state.\";

key loadThreshold;

min-elements 1;

max-elements 1;

uses loadTimeThresholdGrp;

}

list intraRatEsDeactivationCandidateCellsLoadParameters {

description \"This attributes is relevant, if the cell acts as a
candidate

cell. This attribute indicates the traffic load threshold and the time

duration which is used by distributed ES algorithms to allow a cell to

leave the energySaving state. Threshold and time duration are applied

to the candidate cell when it which provides coverage backup for the

cell in energySaving state. The threshold applies in the same way for a

candidate cell, no matter for which original cell it provides backup

coverage.

The time duration indicates how long the traffic in the candidate cell

needs to have been above the threshold to wake up one or more original

cells which have been provided backup coverage by the candidate cell.\";

key loadThreshold;

min-elements 1;

max-elements 1;

uses loadTimeThresholdGrp;

}

list esNotAllowedTimePeriod {

description \"This is a list of time periods during which

inter-RAT energy saving is not allowed\";

key idx;

leaf idx {

type uint32;

}

uses EsNotAllowedTimePeriodGrp;

}

list interRatEsActivationOriginalCellParameters {

description \"This attribute is relevant, if the cell acts as an
original

cell. This attribute indicates the traffic load threshold and the time

duration, which are used by distributed inter-RAT ES algorithms to

allow an original cell to enter the energySaving state. The time

duration indicates how long the traffic load (both for UL and DL) needs

to have been below the threshold.

In case the original cell is an EUTRAN cell, the load information

refers to Composite Available Capacity Group IE (see 3GPP TS 36.413

\[12\] Annex B.1.5) and the following applies:

Load = (100 - \'Capacity Value\' ) \* \'Cell Capacity Class Value\',

where \'Capacity Value\' and \'Cell Capacity Class Value\' are defined
in

3GPP TS 36.423 \[7\].

In case the original cell is a UTRAN cell, the load information refers

to Cell Load Information Group IE (see 3GPP TS 36.413 \[12\] Annex
B.1.5)

and the following applies:

Load= \'Load Value\' \* \'Cell Capacity Class Value\', where \'Load
Value\'

and \'Cell Capacity Class Value\' are defined in 3GPP TS 25.413 \[19\].

If the \'Cell Capacity Class Value\' is not known, then \'Cell Capacity

Class Value\' should be set to 1 when calculating the load, and the load

threshold should be set in range of 0..100.\";

key loadThreshold;

min-elements 1;

max-elements 1;

uses loadTimeThresholdGrp;

}

list interRatEsActivationCandidateCellParameters {

description \"This attribute is relevant, if the cell acts as a
candidate

cell. This attribute indicates the traffic load threshold and the time

duration, which are used by distributed inter-RAT ES algorithms to

allow an original cell to enter the energySaving state. Threshold and

time duration are applied to the candidate cell(s) which will provides

coverage backup of an original cell when it is in the energySaving

state. The time duration indicates how long the traffic load (both for

UL and DL) in the candidate cell needs to have been below the threshold

before any original cells which will be provided backup coverage by the

candidate cell enters energySaving state.

In case the candidate cell is a UTRAN or GERAN cell, the load

information refers to Cell Load Information Group IE (see 3GPP TS

36.413 \[12\] Annex B.1.5) and the following applies:

Load= \'Load Value\' \* \'Cell Capacity Class Value\', where \'Load
Value\'

and \'Cell Capacity Class Value\' are defined in 3GPP TS 25.413 \[19\]

(for UTRAN) / TS 48.008 \[20\] (for GERAN).

If the \'Cell Capacity Class Value\' is not known, then \'Cell Capacity

Class Value\' should be set to 1 when calculating the load, and the load

threshold should be set in range of 0..100.\";

min-elements 1;

max-elements 1;

key loadThreshold;

uses loadTimeThresholdGrp;

}

list interRatEsDeactivationCandidateCellParameters {

description \"This attribute is relevant, if the cell acts as a
candidate

cell. This attribute indicates the traffic load threshold and the time

duration which is used by distributed inter-RAT ES algorithms to allow

an original cell to leave the energySaving state. Threshold and time

duration are applied to the candidate cell which provides coverage

backup for the cell in energySaving state.

The time duration indicates how long the traffic load (either for UL or

DL\) in the candidate cell needs to have been above the threshold to

wake up one or more original cells which have been provided backup

coverage by the candidate cell.

For the load see the definition of

interRatEsActivationCandidateCellParameters.

This attribute indicates the traffic load threshold and the time

duration which is used by distributed inter-RAT ES algorithms to allow

an original cell to leave the energySaving state.\";

key loadThreshold;

min-elements 1;

max-elements 1;

uses loadTimeThresholdGrp;

}

leaf energySavingState {

description \"Specifies the status regarding the energy saving in the

cell. If the value of energySavingControl is toBeEnergySaving, then it

shall be tried to achieve the value isEnergySaving for the

energySavingState. If the value of energySavingControl is

toBeNotEnergySaving, then it shall be tried to achieve the value

isNotEnergySaving for the energySavingState. \";

type enumeration{

enum isNotEnergySaving;

enum isEnergySaving;

}

}

leaf energySavingControl {

description \"This attribute allows the Cross Domain-Centralized SON

energy saving function to initiate energy saving activation or

deactivation.\";

type enumeration{

enum toBeEnergySaving;

enum toBeNotEnergySaving;

}

}

}

grouping EsNotAllowedTimePeriodGrp {

leaf startTime {

description \"Start of not allowed time period in UTC time zone.

If set, the endTime must also be set. If not set, this is

interpreted as around the clock.\";

must ../endTime;

type type5g3gpp:UTC24TimeOfDayT;

}

leaf endTime {

description \"If endTime has a lower value than startTime, it will

be interpreted as referring to the following day.\";

must ../startTime;

type type5g3gpp:UTC24TimeOfDayT;

}

leaf-list daysOfWeek {

description \"Specifies that the not allowed periods are only

applicable to the specified days in UTC timezone. Every day if

not set.\";

type type5g3gpp:DayOfWeekT;

}

}

grouping CESManagementFunctionSubtree {

list CESManagementFunction {

description \"This IOC represents the management capabilities of

Centralized SON Energy Saving (ES) functions. This is provided for

Energy Saving purposes.

In the case where multiple CESManagement MOIs exist at different

levels of the containment tree, the CESManagement MOI at the lower

level overrides the CESManagement MOIs at higher level(s) of the

same containment tree.\";

reference \"clause 6.2.2 in TS 28.310\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses CESManagementFunctionGrp;

}

}

}

augment \"/me3gpp:ManagedElement/gnbcucp3gpp:GNBCUCPFunction/\"+

\"nrcellcu3gpp:NRCellCU\" {

if-feature nrcellcu3gpp:CESManagementFunction;

uses CESManagementFunctionSubtree;

}

augment /me3gpp:ManagedElement {

if-feature me3gpp:CESManagementFunction;

uses CESManagementFunctionSubtree;

}

augment /subnet3gpp:SubNetwork {

if-feature subnet3gpp:CESManagementFunction;

uses CESManagementFunctionSubtree;

}

}

\<CODE ENDS\>

E.6 Void
========

E.7 Mount information
=====================

If the class ManagedElement and the underlying hierarchy is contained
under a SubNetwork all YANG modules containing IOCs that can be
contained under the ManagedElement directly or under other IOCs
contained by the ManagedElement and the YANG module for ManagedElement
itself shall be mounted at the mountpoint \"children-of-SubNetwork\" in
the YANG module \_3gpp-common-subnetwork. 

See IETF RFC 8528 \[45\] that describes the mechanism that adds the
schema trees defined by a set of YANG modules onto a mount point defined
in the schema tree in another YANG module.

########  Annex F (normative): XML definitions for 5GC NRM

F.1 General
===========

This annex contains the XML definitions for the 5GC NRM specified in
clause 5, in accordance with 5G NRM Information Model definitions
specified in clause 4.

F.2 Architectural features
==========================

The overall architectural feature of 5GC NRM information model is
specified in clause 4, this clause specifies features that are specific
to the Schema definitions.

The XML definitions of the present document specify the schema for a
configuration content, which can be included in a configuration file for
Bulk configuration management operations.

F.3 Mapping
===========

F.3.1 General mapping
---------------------

An IOC maps to an XML element of the same name as the IOC\'s name in the
Information Model. An IOC attribute maps to a sub-element of the
corresponding IOC\'s XML element, and the name of this sub-element is
the same as the attribute\'s name in the Information Model.

F.3.2 Information Object Class (IOC) mapping
--------------------------------------------

The mapping is not present in the current version of the present
document.

F.4 Solution Set definitions
============================

F.4.1 XML definition structure
------------------------------

The overall description of the file format of configuration data XML
files is provided by 3GPP TS 32.616 \[33\].

The present document defines the NRM-specific XML schema ngcNrm.xsd for
the 5GC NRM Information Model defined in clause 4.

XML schema ngcNrm.xsd explicitly declares NRM-specific XML element types
for the related NRM.

The definition of those NRM-specific XML element types complies with the
generic mapping rules defined in 3GPP TS 32.616 \[33\].

F.4.2 Graphical representation
------------------------------

The graphical representation is not present in the current version of
the present document.

F.4.3 XML schema \"ngcNrm.xsd\"
-------------------------------

\<?xml version=\"1.0\" encoding=\"UTF-8\"?\>

\<!\--

3GPP TS 28.541 5GC Network Resource Model

XML schema definition

ngcNrm.xsd

\--\>

\<schema

targetNamespace=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.541\#ngcNrm\"

elementFormDefault=\"qualified\"

attributeFormDefault=\"unqualified\"

xmlns=\"http://www.w3.org/2001/XMLSchema\"

xmlns:xn=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.623\#genericNrm\"
xmlns:nn=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.541\#nrNrm\"
xmlns:en=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.659\#eutranNrm\"

xmlns:ngc=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.541\#ngcNrm\"

\>

\<import
namespace=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.623\#genericNrm\"/\>

\<import
namespace=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.659\#eutranNrm\"/\>

\<import
namespace=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.541\#nrNrm\"/\>

\<!\--NGC NRM IM class associated XML elements \--\>

\<complexType name=\"aMFIdentifier\"\>

\<sequence\>

\<element name=\"amfRegionId\" type=\"ngc:AmfRegionId\"/\>

\<element name=\"amfSetId\" type=\"ngc:AmfSetId\"/\>

\<element name=\"amfPointer\" type=\"ngc:AmfPointer\"/\>

\</sequence\>

\</complexType\>

\<simpleType name=\"AmfRegionId\"\>

\<restriction base=\"integer\"\>

\<maxInclusive value=\"255\"/\>

\<!\-- The AMF Region ID is 8-bitslength, defined in 23.003 \--\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"AmfSetId\"\>

\<restriction base=\"integer\"\>

\<maxInclusive value=\"1023\"/\>

\<!\-- The AMF Region ID is 10-bits length, defined in 23.003 \--\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"AmfPointer\"\>

\<restriction base=\"integer\"\>

\<maxInclusive value=\"63\"/\>

\<!\-- The AMF Pointer is 6-bits length, defined in 23.003 \--\>

\</restriction\>

\</simpleType\> \<complexType name=\"NrTACList\"\>

\<sequence\>

\<element name=\"tac\" type=\"nn:NrTac\" minOccurs=\"0\"
maxOccurs=\"unbounded\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"managedNFProfile\"\>

\<sequence\>

\<element name=\"nfInstanceID\" type=\"string\"/\>

\<element name=\"nfType\" type=\"ngc:NfType\"/\>

\<element name=\"hostAddr\" type=\"ngc:hostAddr\"/\>

\<element name=\"authzInfo\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"location\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"capacity\" type=\"ngc:capacity\" minOccurs=\"0\"/\>

\<element name=\"nfInfo\" type=\"ngc:Nfinfo\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"hostAddr\"\>

\<!\-- Refer to definitions in TS 28.541\--\>

\<sequence\>

\<choice minOccurs=\"0\" maxOccurs=\"1\"\>

\<element name=\"ipAddress\" type=\"string\"/\>

\<element name=\"fqdn\" type=\"string\"/\>

\</choice\>

\</sequence\>

\</complexType\>

\<simpleType name=\"capacity\"\>

\<!\-- Refer to definitions in TS 28.541\--\>

\<restriction base=\"integer\"\>

\<minInclusive value=\"0\"/\>

\<maxInclusive value=\"65535\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"Nfinfo\"\>

\<!\-- Refer to definitions in TS 28.541\--\>

\<sequence\>

\<choice minOccurs=\"0\" maxOccurs=\"1\"\>

\<element name=\"amfInfo\" type=\"ngc:AmfInfo\"/\>

\<element name=\"udrInfo\" type=\"ngc:UdrInfo\"/\>

\<element name=\"udmInfo\" type=\"ngc:UdmInfo\"/\>

\<element name=\"ausfInfo\" type=\"ngc:AusfInfo\"/\>

\<element name=\"upfInfo\" type=\"ngc:UpfInfo\"/\>

\</choice\>

\</sequence\>

\</complexType\>

\<complexType name=\"NFProfileList\"\>

\<sequence\>

\<element name=\"nfProfile\" type=\"ngc:NfProfile\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"NfProfile\"\>

\<sequence\>

\<element name=\"nfInstanceID\" type=\"string\"/\>

\<!\-- nfInstanceID is uuid of NF instance \--\>

\<element name=\"nfType\" type=\"ngc:NfType\"/\>

\<element name=\"sNssais\" type=\"ngc: SnssaiList\"/\>

\<element name=\"fqdn\" type=\"string\"/\>

\<element name=\"interPlmnFqdn\" type=\"string\"/\>

\<element name=\"ipv4Addresses\" type=\"string\"/\>

\<element name=\"ipv6Addresses\" type=\"string\"/\>

\<element name=\"ipv6Prefixes\" type=\"string\"/\>

\<element name=\"capacity\" type=\"string\"/\>

\<element name=\"udrInfo\" type=\"ngc:UdrInfo\"/\>

\<element name=\"amfInfo\" type=\"ngc:AmfInfo\"/\>

\<element name=\"smfInfo\" type=\"ngc:SmfInfo\"/\>

\<element name=\"upfInfo\" type=\"ngc:UpfInfo\"/\>

\<element name=\"nfServices\" type=\"ngc:NfServices\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"nFSrvGroupId\" type=\"string\"/\>

\<element name=\"smfServingAreas\" type=\"string\"/\>

\<element name=\"locality\" type=\"string\"/\>

\<element name=\"authzInfo\" type=\"string\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"NfServices\"\>

\<sequence\>

\<element name=\"serviceInstanceId\" type=\"string\"/\>

\<element name=\"serviceName\" type=\"string\"/\>

\<element name=\"version\" type=\"string\"/\>

\<element name=\"schema\" type=\"string\"/\>

\<element name=\"fqdn\" type=\"string\"/\>

\<element name=\"interPlmnFqdn\" type=\"string\"/\>

\<element name=\"ipEndPoints\" type=\"ngc:IpEndpoints\"/\>

\<element name=\"apiPrefix\" type=\"string\"/\>

\<element name=\"defaultNotificationSubscriptions\"
type=\"ngc:DefaultNotificationSubscriptions\"/\>

\<element name=\"allowedPlmns\" type=\"nn:PLMNIdList\"/\>

\<element name=\"allowedNfTypes\" type=\"ngc:NFTypeList\"/\>

\<element name=\"allowedNssais\" type=\"ngc:Nssai\"/\>

\<element name=\"capacity\" type=\"string\"/\>

\<element name=\"supportedFeatures\" type=\"string\"/\>

\</sequence\>

\</complexType\>

\<simpleType name=\"NfType\"\>

\<restriction base=\"string\"\>

\<!\-- NF name is defined in TS 23.501 \--\>

\<enumeration value=\"NRF\"/\>

\<enumeration value=\"UDM\"/\>

\<enumeration value=\"AMF\"/\>

\<enumeration value=\"SMF\"/\>

\<enumeration value=\"AUSF\"/\>

\<enumeration value=\"NEF\"/\>

\<enumeration value=\"PCF\"/\>

\<enumeration value=\"SMSF\"/\>

\<enumeration value=\"NSSF\"/\>

\<enumeration value=\"UDR\"/\>

\<enumeration value=\"LMF\"/\>

\<enumeration value=\"GMLC\"/\>

\<enumeration value=\"5GEIR\"/\>

\<enumeration value=\"SEPP\"/\>

\<enumeration value=\"UPF\"/\>

\<enumeration value=\"N3IWF\"/\>

\<enumeration value=\"AF\"/\>

\<enumeration value=\"UDSF\"/\>

\<enumeration value=\"DN\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"NFTypeList\"\>

\<sequence\>

\<element name=\"NFType\" type=\"ngc:NfType\"/\>

\</sequence\>

\</complexType\>

> \<complexType name=\"LocalEndPoint\"\>
>
> \<sequence\>

\<element name=\"ipv4Address\" type=\"string\"/\>

\<element name=\"ipv6Address\" type=\"string\"/\>

\<element name=\"ipv6Prefix\" type=\"string\"/\>

\<element name=\"vlanId\" type=\"integer\"/\>

> \</sequence\>
>
> \</complexType\>
>
> \<complexType name=\"RemoteEndPoint\"\>
>
> \<sequence\>
>
> \<element name=\"ipv4Address\" type=\"string\"/\>
>
> \<element name=\"ipv6Address\" type=\"string\"/\>
>
> \<element name=\"ipv6Prefix\" type=\"string\"/\>
>
> \</sequence\>
>
> \</complexType\>

\<complexType name=\"UdrInfo\"\>

\<sequence\>

\<element name=\"supiRange\" type=\"ngc:SupiRange\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"SupiRange\"\>

\<sequence\>

\<element name=\"start\" type=\"string\"/\>

\<element name=\"end\" type=\"string\"/\>

\<element name=\"pattern\" type=\"string\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"AmfInfo\"\>

\<sequence\>

\<element name=\"amfSetId\" type=\"ngc:AmfSetId\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"SmfInfo\"\>

\<sequence\>

\<element name=\"dnn\" type=\"string\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"UpfInfo\"\>

\<sequence\>

\<element name=\"snssaiUpfInfo\" type=\"ngc:SnssaiUpfInfo\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"UdmInfo\"\>

\<sequence\>

\<element name=\"nFSrvGroupId\" type=\"string\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"AusfInfo\"\>

\<sequence\>

\<element name=\"nFSrvGroupId\" type=\"string\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"SnssaiUpfInfo\"\>

\<sequence\>

\<element name=\"sNssai\" type=\"ngc:SNssai\"/\>

\<element name=\"dnnUpfInfoList\" type=\"ngc:DnnUpfInfoList\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"DnnUpfInfoList\"\>

\<sequence\>

\<element name=\"dnn\" type=\"string\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"DefaultNotificationSubscription\"\>

\<sequence\>

\<element name=\"notificationType\" type=\"ngc:NotificationType\"/\>

\<element name=\"callbackUri\" type=\"string\"/\>

\<element name=\"n1MessageClass\" type=\"string\"/\>

\<element name=\"n2InformationClass\" type=\"string\"/\>

\</sequence\>

\</complexType\>

\<simpleType name=\"NotificationType\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"N1\_MESSAGES\"/\>

\<enumeration value=\"N2\_INFORMATION\"/\>

\<enumeration value=\"LOCATION\_NOTIFICATION\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"TransportProtocol\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"TCP\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"NfStatus\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"REGISTERED\"/\>

\<enumeration value=\"SUSPENDED\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"NfRegistrationData\"\>

\<sequence\>

\<element name=\"heartBeatTimer\" type=\"integer\"/\>

\<element name=\"nfProfile\" type=\"ngc:NfProfile\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"CNSIIdList\"\>

\<sequence\>

\<element name=\"cNSIId\" type=\"string\"/\>

\<!\-- CNSI Id is defined in TS 29.531 \--\>

\</sequence\>

\</complexType\>

\<complexType name=\"SnssaiList\"\>

\<sequence\>

\<element name=\"sNssai\" type=\"ngc:SNssai\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"SNssai\"\>

\<sequence\>

\<element name=\"sst\" type=\"ngc:Sst\" minOccurs=\"0\"/\>

\<element name=\"sd\" type=\"ngc:Sd\"/\>

\</sequence\>

\</complexType\>

\<simpleType name=\"Sst\"\>

\<restriction base=\"integer\"\>

\<maxInclusive value=\"255\"/\>

\<!\-- SST is 1-octets length and defined in TS 23.003 \--\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"Sd\"\>

\<restriction base=\"string\"\>

\<pattern value=\"\^\[A-Fa-f0-9\]{6}\$\"/\>

\<!\-- SST is 3-octets length and defined in TS 23.003 \--\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"WeightFactor\"\>

\<restriction base=\"integer\"\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"SEPPType\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"CSEPP\"/\>

\<enumeration value=\"PSEPP\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"SupportedFunc\"\>

\<sequence\>

\<element name=\"function\" type=\"string\"/\>

\<element name=\"policy\" type=\"string\" minOccurs=\"0\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"SupportedFuncList\"\>

\<sequence\>

\<element name=\"supportedFunc\" type=\"ngc:SupportedFunc\"/\>

\</sequence\>

\</complexType\>

\<simpleType name=\"CommModelType\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"DIRECT\_COMMUNICATION\_WO\_NRF\"/\>

\<enumeration value=\"DIRECT\_COMMUNICATION\_WITH\_NRF\"/\>

\<enumeration
value=\"INDIRECT\_COMMUNICATION\_WO\_DEDICATED\_DISCOVERY\"/\>

\<enumeration
value=\"INDIRECT\_COMMUNICATION\_WITH\_DEDICATED\_DISCOVERY\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"CommModel\"\>

\<sequence\>

\<element name=\"groupId\" type=\"integer\"/\>

\<element name=\"commModelType\" type=\"ngc:CommModelType\"/\>

\<element name=\"targetNFServiceList\" type=\"xn:dnlist\"/\>

\<element name=\"commModelConfiguration\" type=\"string\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"CommModelList\"\>

\<sequence\>

\<element name=\"commModel\" type=\"ngc:CommModel\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"CapabilityList\"\>

\<sequence\>

\<element name=\"capability\" type=\"string\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"FiveQIList\"\>

\<sequence\>

\<element name=\"FiveQI\" type=\"integer\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"FiveQiDscpMapping\"\>

\<sequence\>

\<element name=\"fiveQIValues\" type=\"ngc:FiveQIList\"/\>

\<element name=\"dscp\" type=\"integer\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"FiveQiDscpMappingList\"\>

\<sequence\>

\<element name=\"fiveQiDscpMapping\" type=\"ngc:FiveDscpMapping\"/\>

\</sequence\>

\</complexType\>

\<simpleType name=\"FiveQIResourceType\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"GBR\"/\>

\<enumeration value=\"NonGBR\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"PacketErrorRate\"\>

\<sequence\>

\<element name=\"scalar\" type=\"integer\"/\>

\<element name=\"exponent\" type=\"integer\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"FiveQICharacteristics\"\>

\<sequence\>

\<element name=\"fiveQIValue\" type=\"integer\"/\>

\<element name=\"resourceType\" type=\"ngc:FiveQIResourceType\"/\>

\<element name=\"priorityLevel\" type=\"integer\"/\>

\<element name=\"packetDelayBudget\" type=\"integer\"/\>

\<element name=\"packetErrorRate\" type=\"ngc:PacketErrorRate \"/\>

\<element name=\"averagingWindow\" type=\"integer\"/\>

\<element name=\"maximumDataBurstVolume\" type=\"integer\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"FiveQIList\"\>

\<sequence\>

\<element name=\"fiveQI\" type=\"ngc:FiveQICharacteristics\"/\>

\</sequence\>

\</complexType\>

\<simpleType name=\"GtpUPathQoSMonitoringStateType\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"ENABLED\"/\>

\<enumeration value=\"DISABLED\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"DscpList\"\>

\<sequence\>

\<element name=\"dscp\" type=\"integer\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"GtpUPathDelayThresholdsType\"\>

\<sequence\>

\<element name=\"n3AveragePacketDelayThreshold \" type=\"integer\"/\>

\<element name=\"n3MinPacketDelayThreshold\" type=\"integer\"/\>

\<element name=\"n3MaxPacketDelayThreshold\" type=\"integer\"/\>

\<element name=\"n9AveragePacketDelayThreshold \" type=\"integer\"/\>

\<element name=\"n9MinPacketDelayThreshold\" type=\"integer\"/\>

\<element name=\"n9MaxPacketDelayThreshold\" type=\"integer\"/\>

\</sequence\>

\</complexType\>

\<simpleType name=\"QFQoSMonitoringStateType\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"ENABLED\"/\>

\<enumeration value=\"DISABLED\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"FiveqiList\"\>

\<sequence\>

\<element name=\"FiveQI\" type=\"integer\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"QFPacketDelayThresholdsType\"\>

\<sequence\>

\<element name=\"thresholdDl\" type=\"integer\"/\>

\<element name=\"thresholUl\" type=\"integer\"/\>

\<element name=\"thresholdRtt\" type=\"integer\"/\>

\</sequence\>

\</complexType\>

\<simpleType name=\"AfSigProtocol\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"NO\_INFORMATION\"/\>

\<enumeration value=\"SIP\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"PccRule\"\>

\<sequence\>

\<element name=\"pccRuleId\" type=\"string\"/\>

\<element name=\"flowInfoList\" type=\"ngc:FlowInformationList\"/\>

\<element name=\"applicationId\" type=\"string\"/\>

\<element name=\"appDescriptor\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"contentVersion\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"precedence\" type=\"integer\"/\>

\<element name=\"afSigProtocol\" type=\"ngc:AfSigProtocol\"
minOccurs=\"0\"/\>

\<element name=\"isAppRelocatable\" type=\"boolean\" minOccurs=\"0\"/\>

\<element name=\"isUeAddrPreserved\" type=\"boolean\" minOccurs=\"0\"/\>

\<element name=\"qosData\" type=\"ngc:QoSDataList\"/\>

\<element name=\"altQosParams\" type=\"ngc:QoSDataList\"
minOccurs=\"0\"/\>

\<element name=\"trafficControlData\"
type=\"ngc:TrafficControlDataList\"/\>

\<element name=\"conditionData\" type=\"ngc:ConditionData\"
minOccurs=\"0\"/\>

\<element name=\"tscaiInputUl\" type=\"ngc:TscaiInputContainer\"
minOccurs=\"0\"/\>

\<element name=\"tscaiInputDl\" type=\"ngc:TscaiInputContainer\"
minOccurs=\"0\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"PccRuleList\"\>

\<sequence\>

\<element name=\"pccRule\" type=\"ngc:PccRule\"/\>

\</sequence\>

\</complexType\>

\<simpleType name=\"FlowDirection\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"DOWNLINK\"/\>

\<enumeration value=\"UPLINK\"/\>

\<enumeration value=\"BIDIRECTIONAL\"/\>

\<enumeration value=\"UNSPECIFIED\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"FlowInformation\"\>

\<sequence\>

\<element name=\"flowDescription\" type=\"string\"/\>

\<element name=\"ethFlowDescription\" type=\"ngc:EthFlowDescription\"/\>

\<element name=\"packFiltId\" type=\"string\"/\>

\<element name=\"packetFilterUsage\" type=\"boolean\"/\>

\<element name=\"tosTrafficClass\" type=\"string\"/\>

\<element name=\"spi\" type=\"string\"/\>

\<element name=\"flowLabel\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"flowDirection\" type=\"ngc:FlowDirection\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"FlowInformationList\"\>

\<sequence\>

\<element name=\"flowInfo\" type=\"ngc:FlowInformation\"/\>

\</sequence\>

\</complexType\>

\<simpleType name=\"FDir\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"DOWNLINK\"/\>

\<enumeration value=\"UPLINK\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"VlanTagList\"\>

\<sequence\>

\<element name=\"vlanTag\" type=\"string\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"EthFlowDescription\"\>

\<sequence\>

\<element name=\"destMacAddr\" type=\"string\"/\>

\<element name=\"ethType\" type=\"string\"/\>

\<element name=\"fDesc\" type=\"string\"/\>

\<element name=\"fDir\" type=\"ngc:FDir\"/\>

\<element name=\"sourceMacAddr\" type=\"string\"/\>

\<element name=\"vlanTags\" type=\"ngc:VlanTagList\"/\>

\<element name=\"srcMacAddrEnd\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"destMacAddrEnd\" type=\"string\" minOccurs=\"0\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"QoSData\"\>

\<sequence\>

\<element name=\"qosId\" type=\"string\"/\>

\<element name=\"fiveQIValue\" type=\"integer\"/\>

\<element name=\"maxbrUl\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"maxbrDl\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"gbrUl\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"gbrDl\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"arp\" type=\"ngc:ARP\"/\>

\<element name=\"qosNotificationControl\" type=\"boolean\"
minOccurs=\"0\"/\>

\<element name=\"reflectiveQos\" type=\"boolean\" minOccurs=\"0\"/\>

\<element name=\"sharingKeyDl\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"sharingKeyUl\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"maxPacketLossRateDl\" type=\"integer\"
minOccurs=\"0\"/\>

\<element name=\"maxPacketLossRateUl\" type=\"integer\"
minOccurs=\"0\"/\>

\<element name=\"extMaxDataBurstVol\" type=\"integer\"
minOccurs=\"0\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"QoSDataList\"\>

\<sequence\>

\<element name=\"qoSData\" type=\"ngc:QoSData\"/\>

\</sequence\>

\</complexType\>

\<simpleType name=\"PreemptCap\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"NOT\_PREEMPT\"/\>

\<enumeration value=\"MAY\_PREEMPT\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"PreemptVuln\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"NOT\_PREEMPTABLE\"/\>

\<enumeration value=\"PREEMPTABLE\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"ARP\"\>

\<sequence\>

\<element name=\"priorityLevel\" type=\"integer\"/\>

\<element name=\"preemptCap\" type=\"ngc:PreemptCap\"/\>

\<element name=\"preemptVuln\" type=\"ngc:PreemptVuln\"/\>

\</sequence\>

\</complexType\>

\<simpleType name=\"FlowStatus\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"ENABLED-UPLINK\"/\>

\<enumeration value=\"ENABLED-DOWNLINK\"/\>

\<enumeration value=\"ENABLED\"/\>

\<enumeration value=\"DISABLED\"/\>

\<enumeration value=\"REMOVED\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"SteerFun\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"MPTCP\"/\>

\<enumeration value=\"ATSSS\_LL\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"TrafficControlData\"\>

\<sequence\>

\<element name=\"tcId\" type=\"string\"/\>

\<element name=\"flowStatus\" type=\"ngc:FlowStatus\"/\>

\<element name=\"redirectInfo\" type=\"ngc:RedirectInformation\"
minOccurs=\"0\"/\>

\<element name=\"addRedirectInfo\" type=\"ngc:RedirectInformationList\"
minOccurs=\"0\"/\>

\<element name=\"muteNotif\" type=\"boolean\" minOccurs=\"0\"/\>

\<element name=\"trafficSteeringPolIdDl\" type=\"string\"
minOccurs=\"0\"/\>

\<element name=\"trafficSteeringPolIdUl\" type=\"string\"
minOccurs=\"0\"/\>

\<element name=\"routeToLocs\" type=\"ngc:RouteToLocationList\"/\>

\<element name=\"upPathChgEvent\" type=\"ngc:UpPathChgEvent\"
minOccurs=\"0\"/\>

\<element name=\"steerFun\" type=\"ngc:SteerFun\" minOccurs=\"0\"/\>

\<element name=\"steerModeDl\" type=\"ngc:SteeringMode\"
minOccurs=\"0\"/\>

\<element name=\"steerModeUl\" type=\"ngc:SteeringMode\"
minOccurs=\"0\"/\>

\<element name=\"mulAccCtrl\" type=\"ngc:MulAccCtrl\" minOccurs=\"0\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"TrafficControlDataList\"\>

\<sequence\>

\<element name=\"trafficControlData\" type=\"ngc:TrafficControlData\"/\>

\</sequence\>

\</complexType\>

\<simpleType name=\"RedirectAddressType\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"IPV4\_ADDR\"/\>

\<enumeration value=\"IPV6\_ADDR\"/\>

\<enumeration value=\"URL\"/\>

\<enumeration value=\"SIP\_URI\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"RedirectInformation\"\>

\<sequence\>

\<element name=\"redirectEnabled\" type=\"boolean\"/\>

\<element name=\"redirectAddressType\"
type=\"ngc:RedirectAddressType\"/\>

\<element name=\"redirectServerAddress\" type=\"string\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"RedirectInformationList\"\>

\<sequence\>

\<element name=\"redirectInformation\"
type=\"ngc:RedirectInformation\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"RouteToLocation\"\>

\<sequence\>

\<element name=\"dnai\" type=\"string\"/\>

\<element name=\"routeInfo\" type=\"ngc:RouteInformation\"/\>

\<element name=\"routeProfId\" type=\"string\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"RouteToLocationList\"\>

\<sequence\>

\<element name=\"routeToLocation\" type=\"ngc:RouteToLocation\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"RouteInformation\"\>

\<sequence\>

\<element name=\"ipv4Addr\" type=\"string\"/\>

\<element name=\"ipv6Addr\" type=\"string\"/\>

\<element name=\"portNumber\" type=\"integer\"/\>

\</sequence\>

\</complexType\>

\<simpleType name=\"DnaiChgType\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"EARLY\"/\>

\<enumeration value=\"EARLY\_LATE\"/\>

\<enumeration value=\"LATE\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"UpPathChgEvent\"\>

\<sequence\>

\<element name=\"notificationUri\" type=\"string\"/\>

\<element name=\"notifCorreId\" type=\"string\"/\>

\<element name=\"dnaiChgType\" type=\"ngc:DnaiChgType\"/\>

\<element name=\"afAckInd\" type=\"boolean\" minOccurs=\"0\"/\>

\</sequence\>

\</complexType\>

\<simpleType name=\"SteerModeValue\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"ACTIVE\_STANDBY\"/\>

\<enumeration value=\"LOAD\_BALANCING\"/\>

\<enumeration value=\"SMALLEST\_DELAY\"/\>

\<enumeration value=\"PRIORITY\_BASED\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"SteeringMode\"\>

\<sequence\>

\<element name=\"steerModeValue\" type=\"ngc:SteerModeValue\"/\>

\<element name=\"active\" type=\"ngc:AccessType\"/\>

\<element name=\"standby\" type=\"ngc:AccessType\" minOccurs=\"0\"/\>

\<element name=\"threeGLoad\" type=\"integer\"/\>

\<element name=\"prioAcc\" type=\"ngc:AccessType\"/\>

\</sequence\>

\</complexType\>

\<simpleType name=\"MulAccCtrl\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"ALLOWED\"/\>

\<enumeration value=\"NOT\_ALLOWED\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"RatType\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"NR\"/\>

\<enumeration value=\"EUTRA\"/\>

\<enumeration value=\"WLAN\"/\>

\<enumeration value=\"VIRTUAL\"/\>

\<enumeration value=\"NBIOT\"/\>

\<enumeration value=\"WIRELINE\"/\>

\<enumeration value=\"WIRELINE\_CABLE\"/\>

\<enumeration value=\"WIRELINE\_BBF\"/\>

\<enumeration value=\"LTE-M\"/\>

\<enumeration value=\"NR\_U\"/\>

\<enumeration value=\"EUTRA\_U\"/\>

\<enumeration value=\"TRUSTED\_N3GA\"/\>

\<enumeration value=\"TRUSTED\_WLAN\"/\>

\<enumeration value=\"UTRA\"/\>

\<enumeration value=\"GERA\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"AccessType\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"3GPP\_ACCESS\"/\>

\<enumeration value=\"NON\_3GPP\_ACCESS\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"ConditionData\"\>

\<sequence\>

\<element name=\"condId\" type=\"string\"/\>

\<element name=\"activationTime\" type=\"dateTime\" minOccurs=\"0\"/\>

\<element name=\"deactivationTime\" type=\"dateTime\" minOccurs=\"0\"/\>

\<element name=\"accessType\" type=\"ngc:AccessType\" minOccurs=\"0\"/\>

\<element name=\"ratType\" type=\"ngc:RatType\" minOccurs=\"0\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"TscaiInputContainer\"\>

\<sequence\>

\<element name=\"periodicity\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"burstArrivalTime\" type=\"dateTime\" minOccurs=\"0\"/\>

\</sequence\>

\</complexType\>

\<element name=\"AMFFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"pLMNIdList\" type=\"nn:PLMNIdList\"/\>

\<element name=\"aMFIdentifier\" type=\"ngc:aMFIdentifier\"/\>

\<element name=\"sBIFqdn\" type=\"string\"/\>

\<element name=\"snssaiList\" type=\"ngc:SnssaiList\" minOccurs=\"0\"/\>

\<element name=\"aMFSet\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<element name=\"managedNFProfile\" type=\"ngc:managedNFProfile\"
minOccurs=\"0\"/\>

\<element name=\"commModelList\" type=\"ngc:CommModelList\"
minOccurs=\"1\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"ngc:EP\_N2\"/\>

\<element ref=\"ngc:EP\_N8\"/\>

\<element ref=\"ngc:EP\_N11\"/\>

\<element ref=\"ngc:EP\_N12\"/\>

\<element ref=\"ngc:EP\_N14\"/\>

\<element ref=\"ngc:EP\_N15\"/\>

\<element ref=\"ngc:EP\_N17\"/\>

\<element ref=\"ngc:EP\_N22\"/\>

\<element ref=\"ngc:EP\_N26\"/\>

\<element ref=\"ngc:EP\_N20\"/\>

\<element ref=\"ngc:EP\_NLS\"/\>

\<element ref=\"ngc:EP\_NLG\"/\>

\<element ref=\"xn:VsDataContainer\"/\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"SMFFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"pLMNIdList\" type=\"en:PLMNIdList\"/\>

\<element name=\"nRTACList\" type=\"ngc:NrTACList\"/\>

\<element name=\"sBIFqdn\" type=\"string\"/\>

\<element name=\"snssaiList\" type=\"ngc:SnssaiList\" minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<element name=\"managedNFProfile\" type=\"ngc:managedNFProfile\"
minOccurs=\"0\"/\>

\<element name=\"commModelList\" type=\"ngc:CommModelList\"
minOccurs=\"1\"/\>

\<element name=\"configurable5QISetRef\" type=\"xn:dn\"
minOccurs=\"0\"/\>

\<element name=\"dynamic5QISetRef\" type=\"xn:dn\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"ngc:EP\_N4\"/\>

\<element ref=\"ngc:EP\_N10\"/\>

\<element ref=\"ngc:EP\_N11\"/\>

\<element ref=\"ngc:EP\_N7\"/\>

\<element ref=\"ngc:EP\_N16\"/\>

\<element ref=\"ngc:EP\_S5C\"/\>

\<element ref=\"ngc:FiveQiDscpMappingSet\"/\>

\<element ref=\"ngc:GtpUPathQoSMonitoringControl\"/\>

\<element ref=\"ngc:QFQoSMonitoringControl\"/\>

\<element ref=\"ngc:PredefinedPccRuleSet\"/\> \<element
ref=\"xn:VsDataContainer\"/\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"UPFFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"pLMNIdList\" type=\"en:PLMNIdList\"/\>

\<element name=\"nRTACList\" type=\"ngc:NrTACList\"/\>

\<element name=\"snssaiList\" type=\"ngc:SnssaiList\" minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<element name=\"managedNFProfile\" type=\"ngc:managedNFProfile\"
minOccurs=\"0\"/\>

\<element name=\"commModelList\" type=\"ngc:CommModelList\"
minOccurs=\"1\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"ngc:EP\_N4\"/\>

\<element ref=\"ngc:EP\_N3\"/\>

\<element ref=\"ngc:EP\_N9\"/\>

\<element ref=\"ngc:EP\_S5U\"/\>

\<element ref=\"ngc:EP\_N6\"/\>

\<element ref=\"xn:VsDataContainer\"/\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"N3IWFFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"pLMNIdList\" type=\"en:PLMNIdList\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<element name=\"commModelList\" type=\"ngc:CommModelList\"
minOccurs=\"1\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"ngc:EP\_N2\"/\>

\<element ref=\"ngc:EP\_N3\"/\>

\<element ref=\"xn:VsDataContainer\"/\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"PCFFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"pLMNIdList\" type=\"en:PLMNIdList\" /\>

\<element name=\"sBIFqdn\" type=\"string\" /\>

\<element name=\"snssaiList\" type=\"ngc:SnssaiList\" minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<element name=\"managedNFProfile\" type=\"ngc:managedNFProfile\"
minOccurs=\"0\"/\>

\<element name=\"commModelList\" type=\"ngc:CommModelList\"
minOccurs=\"1\"/\>

\<element name=\"configurable5QISetRef\" type=\"xn:dn\"
minOccurs=\"0\"/\>

\<element name=\"dynamic5QISetRef\" type=\"xn:dn\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"ngc:EP\_N7\"/\>

\<element ref=\"ngc:EP\_N15\"/\>

\<element ref=\"ngc:EP\_N16\"/\>

\<element ref=\"ngc:EP\_N5\"/\>

\<element ref=\"ngc:EP\_Rx\"/\>

\<element ref=\"ngc:PredefinedPccRuleSet\"/\>

\<element ref=\"xn:VsDataContainer\"/\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"AUSFFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"pLMNIdList\" type=\"en:PLMNIdList\"/\>

\<element name=\"sBIFqdn\" type=\"string\"/\>

\<element name=\"snssaiList\" type=\"ngc:SnssaiList\" minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<element name=\"managedNFProfile\" type=\"ngc:managedNFProfile\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"ngc:EP\_N12\"/\>

\<element ref=\"ngc:EP\_N13\"/\>

\<element ref=\"xn:VsDataContainer\"/\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"UDMFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"pLMNIdList\" type=\"en:PLMNIdList\"/\>

\<element name=\"sBIFqdn\" type=\"string\"/\>

\<element name=\"snssaiList\" type=\"ngc:SnssaiList\" minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<element name=\"managedNFProfile\" type=\"ngc:managedNFProfile\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"ngc:EP\_N8\"/\>

\<element ref=\"ngc:EP\_N10\"/\>

\<element ref=\"ngc:EP\_N13\"/\>

\<element ref=\"xn:VsDataContainer\"/\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"UDRFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"pLMNIdList\" type=\"en:PLMNIdList\"/\>

\<element name=\"sBIFqdn\" type=\"string\"/\>

\<element name=\"snssaiList\" type=\"ngc:SnssaiList\" minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<element name=\"managedNFProfile\" type=\"ngc:managedNFProfile\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"UDSFFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"pLMNIdList\" type=\"en:PLMNIdList\"/\>

\<element name=\"sBIFqdn\" type=\"string\"/\>

\<element name=\"snssaiList\" type=\"ngc:SnssaiList\" minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<element name=\"managedNFProfile\" type=\"ngc:managedNFProfile\"
minOccurs=\"0\"/\>

\<element name=\"commModelList\" type=\"ngc:CommModelList\"
minOccurs=\"1\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"NRFFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"pLMNIdList\" type=\"en:PLMNIdList\"/\>

\<element name=\"sBIFqdn\" type=\"string\"/\>

\<element name=\"cNSIIdList\" type=\"ngc:CNSIIdList\" minOccurs=\"0\"/\>

\<element name=\"nFProfileList\" type=\"ngc:NFProfileList\"
minOccurs=\"0\"/\>

\<element name=\"snssaiList\" type=\"ngc:SnssaiList\" minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<element name=\"commModelList\" type=\"ngc:CommModelList\"
minOccurs=\"1\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"ngc:EP\_N27\"/\>

\<element ref=\"xn:VsDataContainer\"/\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"NSSFFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"pLMNIdList\" type=\"en:PLMNIdList\"/\>

\<element name=\"sBIFqdn\" type=\"string\"/\>

\<element name=\"cNSIIdList\" type=\"ngc:CNSIIdList\"/\>

\<element name=\"snssaiList\" type=\"ngc: SnssaiList\"
minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>
\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<element name=\"managedNFProfile\" type=\"ngc:managedNFProfile\"
minOccurs=\"0\"/\>

\<element name=\"commModelList\" type=\"ngc:CommModelList\"
minOccurs=\"1\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"ngc:EP\_N27\"/\>

\<element ref=\"ngc:EP\_N31\"/\>

\<element ref=\"xn:VsDataContainer\"/\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"SMSFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"pLMNIdList\" type=\"en:PLMNIdList\"/\>

\<element name=\"sBIFqdn\" type=\"string\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<element name=\"managedNFProfile\" type=\"ngc:managedNFProfile\"
minOccurs=\"0\"/\>

\<element name=\"commModelList\" type=\"ngc:CommModelList\"
minOccurs=\"1\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"ngc:EP\_N20\"/\>

\<element ref=\"ngc:EP\_N21\"/\>

\<element ref=\"ngc:EP\_MAP\_SMSC\"/\>

\<element ref=\"xn:VsDataContainer\"/\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"LMFFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"pLMNIdList\" type=\"en:PLMNIdList\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<element name=\"managedNFProfile\" type=\"ngc:managedNFProfile\"
minOccurs=\"0\"/\>

\<element name=\"commModelList\" type=\"ngc:CommModelList\"
minOccurs=\"1\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"ngc:EP\_NLS\"/\>

\<element ref=\"xn:VsDataContainer\"/\>

\<element ref=\"xn:MeasurementControl\"/\> \</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"NGEIRFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"pLMNIdList\" type=\"en:PLMNIdList\"/\>

\<element name=\"sBIFqdn\" type=\"string\"/\>

\<element name=\"snssaiList\" type=\"ngc:SnssaiList\" minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<element name=\"managedNFProfile\" type=\"ngc:managedNFProfile\"
minOccurs=\"0\"/\> \<element name=\"commModelList\"
type=\"ngc:CommModelList\" minOccurs=\"1\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"ngc:EP\_N17\"/\>

\<element ref=\"xn:VsDataContainer\"/\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"SEPPFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"pLMNId\" type=\"en:PLMNId\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"sEPPType\" type=\"nn:SEPPType\"/\>

\<element name=\"sEPPId\" type=\"integer\"/\>

\<element name=\"fqdn\" type=\"string\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"ngc:EP\_N32\"/\>

\<element ref=\"xn:VsDataContainer\"/\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"ExternalSEPPFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"pLMNId\" type=\"en:PLMNId\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"sEPPId\" type=\"integer\"/\>

\<element name=\"fqdn\" type=\"string\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"ngc:EP\_N32\"/\>

\<element ref=\"xn:VsDataContainer\"/\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"NWDAFFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"pLMNIdList\" type=\"en:PLMNIdList\"/\>

\<element name=\"sBIFqdn\" type=\"string\"/\>

\<element name=\"snssaiList\" type=\"ngc:SnssaiList\" minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<element name=\"managedNFProfile\" type=\"ngc:managedNFProfile\"
minOccurs=\"0\"/\>

\<element name=\"commModelList\" type=\"ngc:CommModelList\"
minOccurs=\"1\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"SCPFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<element name=\"supportedFuncList\" type=\"ngc:SupportedFuncList\"/\>

\<element name=\"address\" type=\"string\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"NEFFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<element name=\"sBIFqdn\" type=\"string\"/\>

\<element name=\"snssaiList\" type=\"ngc:SnssaiList\" minOccurs=\"0\"/\>

\<element name=\"managedNFProfile\" type=\"ngc:ManagedNFProfile\"/\>

\<element name=\"capabilitylist\" type=\"ngc:CapabilityList\"/\>

\<element name=\"isINEF\" type=\"boolean\"/\>

\<element name=\"isCAPIFSup\" type=\"boolean\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N2\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemoteEndPoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N3\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemoteEndPoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N4\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemoteEndPoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N5\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemotePoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N6\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemotePoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N7\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemotePoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N8\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemotePoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N9\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemoteEndPoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N10\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:Remote\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N11\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:Remote\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N12\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemoteEndPoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N13\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemoteEndPoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N14\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemoteEndPoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N15\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemoteEndPoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N16\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:Local\" minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemotePoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N17\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemotePoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N20\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:Local\" minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemotePoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N21\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:Local\" minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemotePoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N22\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemoteEndPoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N26\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemoteEndPoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

> \</element\>

\<element name=\"EP\_N27\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemoteEndPoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

> \</element\>

\<element name=\"EP\_N31\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemoteEndPoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_N32\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemoteEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remotePlmnId\" type=\"en:PLMNId\"/\>

\<element name=\"remoteSeppAddress\" type=\"string\"/\>

\<element name=\"remoteSeppId\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"n32cParas\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"n32fPolicy\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"withIPX\" type=\"boolean\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_S5C\"\> \<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemoteEndPoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_S5U\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemoteEndPoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_Rx\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemoteEndPoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_MAP\_SMSC\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemoteEndPoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_NLS\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemoteEndPoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_NLG\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\" minOccurs=\"0\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from EP\_RP \--\>

\<element name=\"farEndEntity\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from EP\_RP \--\>

\<element name=\"localAddress\" type=\"ngc:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"ngc:RemoteEndPoint\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"FiveQiDscpMappingSet\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"fiveQiDscpMappingList\"
type=\"ngc:FiveQiDscpMappingList\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"Configurable5QISet\"
substitutionGroup=\"xn:SubNetworkOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"configurable5QIs\" type=\"ngc:FiveQIList\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"Dynamic5QISet\"
substitutionGroup=\"xn:SubNetworkOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"dynamic5QIs\" type=\"ngc:FiveQIList\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"GtpUPathQoSMonitoringControl\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"gtpUPathQoSMonitoringState\" type=\"ngc:
GtpUPathQoSMonitoringStateType\"/\>

\<element name=\"gtpUPathMonitoredSNSSAIs\" type=\"ngc:SnssaiList\"/\>

\<element name=\"monitoredDSCPs\" type=\"ngc:DscpList\"/\>

\<element name=\"isEventTriggeredGtpUPathMonitoringSupported\"
type=\"boolean\"/\>

\<element name=\"isPeriodicGtpUMonitoringSupported\" type=\"boolean\"/\>

\<element name=\"isImmediateGtpUMonitoringSupported\"
type=\"boolean\"/\>

\<element name=\"gtpUPathDelayThresholds\"
type=\"ngc:GtpUPathDelayThresholdsType\" minOccurs=\"0\"/\>

\<element name=\"gtpUPathMinimumWaitTime\" type=\"integer\"
minOccurs=\"0\"/\>

\<element name=\"gtpUPathMeasurementPeriod\" type=\"integer\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"QFQoSMonitoringControl\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"qFQoSMonitoringState\"
type=\"ngc:QFQoSMonitoringStateType\"/\>

\<element name=\"qFMonitoredSNSSAIs\" type=\"ngc:SnssaiList\"/\>

\<element name=\"qFMonitored5QIs\" type=\"ngc:FiveqiList\"/\>

\<element name=\"isEventTriggeredQFMonitoringSupported\"
type=\"boolean\"/\>

\<element name=\"isPeriodicQFMonitoringSupported\" type=\"boolean\"/\>

\<element name=\"isSessionReleasedQFMonitoringSupported\"
type=\"boolean\"/\>

\<element name=\"qFPacketDelayThresholds\"
type=\"ngc:QFPacketDelayThresholdsType\" minOccurs=\"0\"/\>

\<element name=\"qFMinimumWaitTime\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"qFMeasurementPeriod \" type=\"integer\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"PredefinedPccRuleSet\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"predefinedPccRules\" type=\"ngc:PccRuleList\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\</schema\>

########  Annex G (normative): OpenAPI definition of the 5GC NRM

G.1 General 
===========

This annex contains the OpenAPI definition of the NR NRM in YAML format.

The Information Service (IS) of the NR NRM is defined in clause 4.

Mapping rules to produce the OpenAPI definition based on the IS are
defined in 3GPP TS 32.160 \[47\].

G.2 Void
========

G.3 Void
========

G.4 Solution Set (SS) definitions
=================================

G.4.1 Void
----------

G.4.2 Void
----------

G.4.3 OpenAPI document \"TS28541\_5GcNrm.yaml\"
-----------------------------------------------

openapi: 3.0.1

info:

title: 3GPP 5GC NRM

version: 16.16.0

description: \>-

OAS 3.0.1 specification of the 5GC NRM

© 2023, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI,
TTA, TTC).

All rights reserved.

externalDocs:

description: 3GPP TS 28.541; 5G NRM, 5GC NRM

url: http://www.3gpp.org/ftp/Specs/archive/28\_series/28.541/

paths: {}

components:

schemas:

\#\-\-\-\-\-\-\-- Definition of
types\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

AmfIdentifier:

type: object

description: \'AmfIdentifier comprise of amfRegionId, amfSetId and
amfPointer\'

properties:

amfRegionId:

\$ref: \'\#/components/schemas/AmfRegionId\'

amfSetId:

\$ref: \'\#/components/schemas/AmfSetId\'

amfPointer:

\$ref: \'\#/components/schemas/AmfPointer\'

AmfRegionId:

type: integer

description: AmfRegionId is defined in TS 23.003

maximum: 255

AmfSetId:

type: string

description: AmfSetId is defined in TS 23.003

maximum: 1023

AmfPointer:

type: integer

description: AmfPointer is defined in TS 23.003

maximum: 63

IpEndPoint:

type: object

properties:

ipv4Address:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Ipv4Addr\'

ipv6Address:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Ipv6Addr\'

ipv6Prefix:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Ipv6Prefix\'

transport:

\$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/TransportProtocol\'

port:

type: integer

NFProfileList:

type: array

description: List of NF profile

items:

\$ref: \'\#/components/schemas/NFProfile\'

NFProfile:

type: object

description: \'NF profile stored in NRF, defined in TS 29.510\'

properties:

nFInstanceId:

type: string

description: uuid of NF instance

nFType:

\$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/NFType\'

nFStatus:

\$ref: \'\#/components/schemas/NFStatus\'

plmn:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/PlmnId\'

sNssais:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/Snssai\'

fqdn:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Fqdn\'

interPlmnFqdn:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Fqdn\'

nfServices:

type: array

items:

\$ref: \'\#/components/schemas/NFService\'

NFService:

type: object

description: NF Service is defined in TS 29.510

properties:

serviceInstanceId:

type: string

serviceName:

type: string

version:

type: string

schema:

type: string

fqdn:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Fqdn\'

interPlmnFqdn:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Fqdn\'

ipEndPoints:

type: array

items:

\$ref: \'\#/components/schemas/IpEndPoint\'

apiPrfix:

type: string

allowedPlmns:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/PlmnId\'

allowedNfTypes:

type: array

items:

\$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/NFType\'

allowedNssais:

type: array

items:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/Snssai\'

NFStatus:

type: string

description: any of enumerated value

enum:

\- REGISTERED

\- SUSPENDED

CNSIIdList:

type: array

items:

\$ref: \'\#/components/schemas/CNSIId\'

CNSIId:

type: string

description: CNSI Id is defined in TS 29.531, only for Core Network

TACList:

type: array

items:

\$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Tac\'

WeightFactor:

type: integer

UdmInfo:

type: object

properties:

nFSrvGroupId:

type: string

AusfInfo:

type: object

properties:

nFSrvGroupId:

type: string

UpfInfo:

type: object

properties:

smfServingAreas:

type: string

AmfInfo:

type: object

properties:

priority:

type: integer

SupportedDataSetId:

type: string

description: any of enumerated value

enum:

\- SUBSCRIPTION

\- POLICY

\- EXPOSURE

\- APPLICATION

Udrinfo:

type: object

properties:

supportedDataSetIds:

type: array

items:

\$ref: \'\#/components/schemas/SupportedDataSetId\'

nFSrvGroupId:

type: string

NFInfo:

oneOf:

\- \$ref: \'\#/components/schemas/UdmInfo\'

\- \$ref: \'\#/components/schemas/AusfInfo\'

\- \$ref: \'\#/components/schemas/UpfInfo\'

\- \$ref: \'\#/components/schemas/AmfInfo\'

\- \$ref: \'\#/components/schemas/Udrinfo\'

ManagedNFProfile:

type: object

properties:

nfInstanceID:

type: string

nfType:

\$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/NFType\'

authzInfo:

type: string

hostAddr:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/HostAddr\'

locality:

type: string

nFInfo:

\$ref: \'\#/components/schemas/NFInfo\'

capacity:

type: integer

SEPPType:

type: string

description: any of enumerated value

enum:

\- CSEPP

\- PSEPP

SupportedFunc:

type: object

properties:

function:

type: string

policy:

type: string

SupportedFuncList:

type: array

items:

\$ref: \'\#/components/schemas/SupportedFunc\'

CommModelType:

type: string

description: any of enumerated value

enum:

\- DIRECT\_COMMUNICATION\_WO\_NRF

\- DIRECT\_COMMUNICATION\_WITH\_NRF

\- INDIRECT\_COMMUNICATION\_WO\_DEDICATED\_DISCOVERY

\- INDIRECT\_COMMUNICATION\_WITH\_DEDICATED\_DISCOVERY

CommModel:

type: object

properties:

groupId:

type: integer

commModelType:

\$ref: \'\#/components/schemas/CommModelType\'

targetNFServiceList:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/DnList\'

commModelConfiguration:

type: string

CommModelList:

type: array

items:

\$ref: \'\#/components/schemas/CommModel\'

CapabilityList:

type: array

items:

type: string

FiveQiDscpMapping:

type: object

properties:

fiveQIValues:

type: array

items:

type: integer

dscp:

type: integer

SnssaiList:

type: array

items:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/Snssai\'

PacketErrorRate:

type: object

properties:

scalar:

type: integer

exponent:

type: integer

FiveQICharacteristics:

type: object

properties:

fiveQIValue:

type: integer

resourceType:

type: string

enum:

\- GBR

\- NonGBR

priorityLevel:

type: integer

packetDelayBudget:

type: integer

packetErrorRate:

\$ref: \'\#/components/schemas/PacketErrorRate\'

averagingWindow:

type: integer

maximumDataBurstVolume:

type: integer

GtpUPathDelayThresholdsType:

type: object

properties:

n3AveragePacketDelayThreshold:

type: integer

n3MinPacketDelayThreshold:

type: integer

n3MaxPacketDelayThreshold:

type: integer

n9AveragePacketDelayThreshold:

type: integer

n9MinPacketDelayThreshold:

type: integer

n9MaxPacketDelayThreshold:

type: integer

QFPacketDelayThresholdsType:

type: object

properties:

thresholdDl:

type: integer

thresholdUl:

type: integer

thresholdRtt:

type: integer

QosData:

type: object

properties:

qosId:

type: string

fiveQIValue:

type: integer

maxbrUl:

\$ref: \'TS29571\_CommonData.yaml\#/components/schemas/BitRateRm\'

maxbrDl:

\$ref: \'TS29571\_CommonData.yaml\#/components/schemas/BitRateRm\'

gbrUl:

\$ref: \'TS29571\_CommonData.yaml\#/components/schemas/BitRateRm\'

gbrDl:

\$ref: \'TS29571\_CommonData.yaml\#/components/schemas/BitRateRm\'

arp:

\$ref: \'TS29571\_CommonData.yaml\#/components/schemas/Arp\'

qosNotificationControl:

type: boolean

reflectiveQos:

type: boolean

sharingKeyDl:

type: string

sharingKeyUl:

type: string

maxPacketLossRateDl:

\$ref:
\'TS29571\_CommonData.yaml\#/components/schemas/PacketLossRateRm\'

maxPacketLossRateUl:

\$ref:
\'TS29571\_CommonData.yaml\#/components/schemas/PacketLossRateRm\'

extMaxDataBurstVol:

\$ref:
\'TS29571\_CommonData.yaml\#/components/schemas/ExtMaxDataBurstVolRm\'

QosDataList:

type: array

items:

\$ref: \'\#/components/schemas/QosData\'

SteeringMode:

type: object

properties:

steerModeValue:

\$ref:
\'TS29512\_Npcf\_SMPolicyControl.yaml\#/components/schemas/SteerModeValue\'

active:

\$ref: \'TS29571\_CommonData.yaml\#/components/schemas/AccessType\'

standby:

\$ref: \'TS29571\_CommonData.yaml\#/components/schemas/AccessTypeRm\'

threeGLoad:

\$ref: \'TS29571\_CommonData.yaml\#/components/schemas/Uinteger\'

prioAcc:

\$ref: \'TS29571\_CommonData.yaml\#/components/schemas/AccessType\'

TrafficControlData:

type: object

properties:

tcId:

type: string

flowStatus:

\$ref:
\'TS29514\_Npcf\_PolicyAuthorization.yaml\#/components/schemas/FlowStatus\'

redirectInfo:

\$ref:
\'TS29512\_Npcf\_SMPolicyControl.yaml\#/components/schemas/RedirectInformation\'

addRedirectInfo:

type: array

items:

\$ref:
\'TS29512\_Npcf\_SMPolicyControl.yaml\#/components/schemas/RedirectInformation\'

minItems: 1

muteNotif:

type: boolean

trafficSteeringPolIdDl:

type: string

nullable: true

trafficSteeringPolIdUl:

type: string

nullable: true

routeToLocs:

type: array

items:

\$ref: \'TS29571\_CommonData.yaml\#/components/schemas/RouteToLocation\'

traffCorreInd:

type: boolean

upPathChgEvent:

\$ref:
\'TS29512\_Npcf\_SMPolicyControl.yaml\#/components/schemas/UpPathChgEvent\'

steerFun:

\$ref:
\'TS29512\_Npcf\_SMPolicyControl.yaml\#/components/schemas/SteeringFunctionality\'

steerModeDl:

\$ref: \'\#/components/schemas/SteeringMode\'

steerModeUl:

\$ref: \'\#/components/schemas/SteeringMode\'

mulAccCtrl:

\$ref:
\'TS29512\_Npcf\_SMPolicyControl.yaml\#/components/schemas/MulticastAccessControl\'

TrafficControlDataList:

type: array

items:

\$ref: \'\#/components/schemas/TrafficControlData\'

PccRule:

type: object

properties:

pccRuleId:

type: string

description: Univocally identifies the PCC rule within a PDU session.

flowInfoList:

type: array

items:

\$ref:
\'TS29512\_Npcf\_SMPolicyControl.yaml\#/components/schemas/FlowInformation\'

applicationId:

type: string

appDescriptor:

\$ref:
\'TS29512\_Npcf\_SMPolicyControl.yaml\#/components/schemas/ApplicationDescriptor\'

contentVersion:

\$ref:
\'TS29514\_Npcf\_PolicyAuthorization.yaml\#/components/schemas/ContentVersion\'

precedence:

\$ref: \'TS29571\_CommonData.yaml\#/components/schemas/Uinteger\'

afSigProtocol:

\$ref:
\'TS29512\_Npcf\_SMPolicyControl.yaml\#/components/schemas/AfSigProtocol\'

isAppRelocatable:

type: boolean

isUeAddrPreserved:

type: boolean

qosData:

type: array

items:

\$ref: \'\#/components/schemas/QosDataList\'

altQosParams:

type: array

items:

\$ref: \'\#/components/schemas/QosDataList\'

trafficControlData:

type: array

items:

\$ref: \'\#/components/schemas/TrafficControlDataList\'

conditionData:

\$ref:
\'TS29512\_Npcf\_SMPolicyControl.yaml\#/components/schemas/ConditionData\'

tscaiInputDl:

\$ref:
\'TS29514\_Npcf\_PolicyAuthorization.yaml\#/components/schemas/TscaiInputContainer\'

tscaiInputUl:

\$ref:
\'TS29514\_Npcf\_PolicyAuthorization.yaml\#/components/schemas/TscaiInputContainer\'

\#\-\-\-\-\-\-\-- Definition of concrete IOCs
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

MnS:

oneOf:

\- type: object

properties:

SubNetwork:

\$ref: \'\#/components/schemas/SubNetwork-Multiple\'

\- type: object

properties:

ManagedElement:

\$ref: \'\#/components/schemas/ManagedElement-Multiple\'

SubNetwork-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/SubNetwork-Attr\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/SubNetwork-ncO\'

\- type: object

properties:

SubNetwork:

\$ref: \'\#/components/schemas/SubNetwork-Multiple\'

ManagedElement:

\$ref: \'\#/components/schemas/ManagedElement-Multiple\'

ExternalAmfFunction:

\$ref: \'\#/components/schemas/ExternalAmfFunction-Multiple\'

ExternalNrfFunction:

\$ref: \'\#/components/schemas/ExternalNrfFunction-Multiple\'

ExternalNssfFunction:

\$ref: \'\#/components/schemas/ExternalNssfFunction-Multiple\'

AmfSet:

\$ref: \'\#/components/schemas/AmfSet-Multiple\'

AmfRegion:

\$ref: \'\#/components/schemas/AmfRegion-Multiple\'

Configurable5QISet:

\$ref: \'\#/components/schemas/Configurable5QISet-Multiple\'

Dynamic5QISet:

\$ref: \'\#/components/schemas/Dynamic5QISet-Multiple\'

ManagedElement-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedElement-Attr\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedElement-ncO\'

\- type: object

properties:

AmfFunction:

\$ref: \'\#/components/schemas/AmfFunction-Multiple\'

SmfFunction:

\$ref: \'\#/components/schemas/SmfFunction-Multiple\'

UpfFunction:

\$ref: \'\#/components/schemas/UpfFunction-Multiple\'

N3iwfFunction:

\$ref: \'\#/components/schemas/N3iwfFunction-Multiple\'

PcfFunction:

\$ref: \'\#/components/schemas/PcfFunction-Multiple\'

AusfFunction:

\$ref: \'\#/components/schemas/AusfFunction-Multiple\'

UdmFunction:

\$ref: \'\#/components/schemas/UdmFunction-Multiple\'

UdrFunction:

\$ref: \'\#/components/schemas/UdrFunction-Multiple\'

UdsfFunction:

\$ref: \'\#/components/schemas/UdsfFunction-Multiple\'

NrfFunction:

\$ref: \'\#/components/schemas/NrfFunction-Multiple\'

NssfFunction:

\$ref: \'\#/components/schemas/NssfFunction-Multiple\'

SmsfFunction:

\$ref: \'\#/components/schemas/SmsfFunction-Multiple\'

LmfFunction:

\$ref: \'\#/components/schemas/LmfFunction-Multiple\'

NgeirFunction:

\$ref: \'\#/components/schemas/NgeirFunction-Multiple\'

SeppFunction:

\$ref: \'\#/components/schemas/SeppFunction-Multiple\'

NwdafFunction:

\$ref: \'\#/components/schemas/NwdafFunction-Multiple\'

ScpFunction:

\$ref: \'\#/components/schemas/ScpFunction-Multiple\'

NefFunction:

\$ref: \'\#/components/schemas/NefFunction-Multiple\'

Configurable5QISet:

\$ref: \'\#/components/schemas/Configurable5QISet-Multiple\'

Dynamic5QISet:

\$ref: \'\#/components/schemas/Dynamic5QISet-Multiple\'

AmfFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnIdList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnIdList\'

amfIdentifier:

\$ref: \'\#/components/schemas/AmfIdentifier\'

sBIFqdn:

type: string

weightFactor:

\$ref: \'\#/components/schemas/WeightFactor\'

snssaiList:

\$ref: \'\#/components/schemas/SnssaiList\'

amfSetRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

managedNFProfile:

\$ref: \'\#/components/schemas/ManagedNFProfile\'

commModelList:

\$ref: \'\#/components/schemas/CommModelList\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

EP\_N2:

\$ref: \'\#/components/schemas/EP\_N2-Multiple\'

EP\_N8:

\$ref: \'\#/components/schemas/EP\_N8-Multiple\'

EP\_N11:

\$ref: \'\#/components/schemas/EP\_N11-Multiple\'

EP\_N12:

\$ref: \'\#/components/schemas/EP\_N12-Multiple\'

EP\_N14:

\$ref: \'\#/components/schemas/EP\_N14-Multiple\'

EP\_N15:

\$ref: \'\#/components/schemas/EP\_N15-Multiple\'

EP\_N17:

\$ref: \'\#/components/schemas/EP\_N17-Multiple\'

EP\_N20:

\$ref: \'\#/components/schemas/EP\_N20-Multiple\'

EP\_N22:

\$ref: \'\#/components/schemas/EP\_N22-Multiple\'

EP\_N26:

\$ref: \'\#/components/schemas/EP\_N26-Multiple\'

EP\_NLS:

\$ref: \'\#/components/schemas/EP\_NLS-Multiple\'

EP\_NLG:

\$ref: \'\#/components/schemas/EP\_NLG-Multiple\'

AmfSet-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnIdList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnIdList\'

nRTACList:

\$ref: \'\#/components/schemas/TACList\'

amfSetId:

\$ref: \'\#/components/schemas/AmfSetId\'

snssaiList:

\$ref: \'\#/components/schemas/SnssaiList\'

aMFRegionRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

aMFSetMemberList:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/DnList\'

AmfRegion-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnIdList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnIdList\'

nRTACList:

\$ref: \'\#/components/schemas/TACList\'

amfRegionId:

\$ref: \'\#/components/schemas/AmfRegionId\'

snssaiList:

\$ref: \'\#/components/schemas/SnssaiList\'

aMFSetListRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/DnList\'

SmfFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnIdList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnIdList\'

nRTACList:

\$ref: \'\#/components/schemas/TACList\'

sBIFqdn:

type: string

snssaiList:

\$ref: \'\#/components/schemas/SnssaiList\'

managedNFProfile:

\$ref: \'\#/components/schemas/ManagedNFProfile\'

commModelList:

\$ref: \'\#/components/schemas/CommModelList\'

configurable5QISetRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

dynamic5QISetRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

EP\_N4:

\$ref: \'\#/components/schemas/EP\_N4-Multiple\'

EP\_N7:

\$ref: \'\#/components/schemas/EP\_N7-Multiple\'

EP\_N10:

\$ref: \'\#/components/schemas/EP\_N10-Multiple\'

EP\_N11:

\$ref: \'\#/components/schemas/EP\_N11-Multiple\'

EP\_N16:

\$ref: \'\#/components/schemas/EP\_N16-Multiple\'

EP\_S5C:

\$ref: \'\#/components/schemas/EP\_S5C-Multiple\'

FiveQiDscpMappingSet:

\$ref: \'\#/components/schemas/FiveQiDscpMappingSet-Single\'

GtpUPathQoSMonitoringControl:

\$ref: \'\#/components/schemas/GtpUPathQoSMonitoringControl-Single\'

QFQoSMonitoringControl:

\$ref: \'\#/components/schemas/QFQoSMonitoringControl-Single\'

PredefinedPccRuleSet:

\$ref: \'\#/components/schemas/PredefinedPccRuleSet-Single\'

UpfFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnIdList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnIdList\'

nRTACList:

\$ref: \'\#/components/schemas/TACList\'

snssaiList:

\$ref: \'\#/components/schemas/SnssaiList\'

managedNFProfile:

\$ref: \'\#/components/schemas/ManagedNFProfile\'

commModelList:

\$ref: \'\#/components/schemas/CommModelList\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

EP\_N3:

\$ref: \'\#/components/schemas/EP\_N3-Multiple\'

EP\_N4:

\$ref: \'\#/components/schemas/EP\_N4-Multiple\'

EP\_N6:

\$ref: \'\#/components/schemas/EP\_N6-Multiple\'

EP\_N9:

\$ref: \'\#/components/schemas/EP\_N9-Multiple\'

EP\_S5U:

\$ref: \'\#/components/schemas/EP\_S5U-Multiple\'

N3iwfFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnIdList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnIdList\'

commModelList:

\$ref: \'\#/components/schemas/CommModelList\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

EP\_N3:

\$ref: \'\#/components/schemas/EP\_N3-Multiple\'

EP\_N4:

\$ref: \'\#/components/schemas/EP\_N4-Multiple\'

PcfFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnIdList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnIdList\'

sBIFqdn:

type: string

snssaiList:

\$ref: \'\#/components/schemas/SnssaiList\'

managedNFProfile:

\$ref: \'\#/components/schemas/ManagedNFProfile\'

commModelList:

\$ref: \'\#/components/schemas/CommModelList\'

configurable5QISetRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

dynamic5QISetRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

EP\_N5:

\$ref: \'\#/components/schemas/EP\_N5-Multiple\'

EP\_N7:

\$ref: \'\#/components/schemas/EP\_N7-Multiple\'

EP\_N15:

\$ref: \'\#/components/schemas/EP\_N15-Multiple\'

EP\_N16:

\$ref: \'\#/components/schemas/EP\_N16-Multiple\'

EP\_Rx:

\$ref: \'\#/components/schemas/EP\_Rx-Multiple\'

PredefinedPccRuleSet:

\$ref: \'\#/components/schemas/PredefinedPccRuleSet-Single\'

AusfFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnIdList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnIdList\'

sBIFqdn:

type: string

snssaiList:

\$ref: \'\#/components/schemas/SnssaiList\'

managedNFProfile:

\$ref: \'\#/components/schemas/ManagedNFProfile\'

commModelList:

\$ref: \'\#/components/schemas/CommModelList\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

EP\_N12:

\$ref: \'\#/components/schemas/EP\_N12-Multiple\'

EP\_N13:

\$ref: \'\#/components/schemas/EP\_N13-Multiple\'

UdmFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnIdList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnIdList\'

sBIFqdn:

type: string

snssaiList:

\$ref: \'\#/components/schemas/SnssaiList\'

managedNFProfile:

\$ref: \'\#/components/schemas/ManagedNFProfile\'

commModelList:

\$ref: \'\#/components/schemas/CommModelList\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

EP\_N8:

\$ref: \'\#/components/schemas/EP\_N8-Multiple\'

EP\_N10:

\$ref: \'\#/components/schemas/EP\_N10-Multiple\'

EP\_N13:

\$ref: \'\#/components/schemas/EP\_N13-Multiple\'

UdrFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnIdList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnIdList\'

sBIFqdn:

type: string

snssaiList:

\$ref: \'\#/components/schemas/SnssaiList\'

managedNFProfile:

\$ref: \'\#/components/schemas/ManagedNFProfile\'

UdsfFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnIdList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnIdList\'

sBIFqdn:

type: string

snssaiList:

\$ref: \'\#/components/schemas/SnssaiList\'

managedNFProfile:

\$ref: \'\#/components/schemas/ManagedNFProfile\'

NrfFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnIdList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnIdList\'

sBIFqdn:

type: string

cNSIIdList:

\$ref: \'\#/components/schemas/CNSIIdList\'

nFProfileList:

\$ref: \'\#/components/schemas/NFProfileList\'

snssaiList:

\$ref: \'\#/components/schemas/SnssaiList\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

EP\_N27:

\$ref: \'\#/components/schemas/EP\_N27-Multiple\'

NssfFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnIdList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnIdList\'

sBIFqdn:

type: string

cNSIIdList:

\$ref: \'\#/components/schemas/CNSIIdList\'

nFProfileList:

\$ref: \'\#/components/schemas/NFProfileList\'

snssaiList:

\$ref: \'\#/components/schemas/SnssaiList\'

commModelList:

\$ref: \'\#/components/schemas/CommModelList\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

EP\_N22:

\$ref: \'\#/components/schemas/EP\_N22-Multiple\'

EP\_N31:

\$ref: \'\#/components/schemas/EP\_N31-Multiple\'

SmsfFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnIdList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnIdList\'

sBIFqdn:

type: string

managedNFProfile:

\$ref: \'\#/components/schemas/ManagedNFProfile\'

commModelList:

\$ref: \'\#/components/schemas/CommModelList\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

EP\_N20:

\$ref: \'\#/components/schemas/EP\_N20-Multiple\'

EP\_N21:

\$ref: \'\#/components/schemas/EP\_N21-Multiple\'

EP\_MAP\_SMSC:

\$ref: \'\#/components/schemas/EP\_MAP\_SMSC-Multiple\'

LmfFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnIdList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnIdList\'

managedNFProfile:

\$ref: \'\#/components/schemas/ManagedNFProfile\'

commModelList:

\$ref: \'\#/components/schemas/CommModelList\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

EP\_NLS:

\$ref: \'\#/components/schemas/EP\_NLS-Multiple\'

NgeirFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnIdList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnIdList\'

sBIFqdn:

type: string

snssaiList:

\$ref: \'\#/components/schemas/SnssaiList\'

managedNFProfile:

\$ref: \'\#/components/schemas/ManagedNFProfile\'

commModelList:

\$ref: \'\#/components/schemas/CommModelList\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

EP\_N17:

\$ref: \'\#/components/schemas/EP\_N17-Multiple\'

SeppFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnId:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/PlmnId\'

sEPPType:

\$ref: \'\#/components/schemas/SEPPType\'

sEPPId:

type: integer

fqdn:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Fqdn\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

EP\_N32:

\$ref: \'\#/components/schemas/EP\_N32-Multiple\'

NwdafFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnIdList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnIdList\'

sBIFqdn:

type: string

snssaiList:

\$ref: \'\#/components/schemas/SnssaiList\'

managedNFProfile:

\$ref: \'\#/components/schemas/ManagedNFProfile\'

commModelList:

\$ref: \'\#/components/schemas/CommModelList\'

ScpFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

supportedFuncList:

\$ref: \'\#/components/schemas/SupportedFuncList\'

address:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/HostAddr\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

NefFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

sBIFqdn:

type: string

snssaiList:

\$ref: \'\#/components/schemas/SnssaiList\'

managedNFProfile:

\$ref: \'\#/components/schemas/ManagedNFProfile\'

capabilityList:

\$ref: \'\#/components/schemas/CapabilityList\'

isCAPIFSup:

type: boolean

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

ExternalAmfFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnIdList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnIdList\'

amfIdentifier:

\$ref: \'\#/components/schemas/AmfIdentifier\'

ExternalNrfFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnIdList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnIdList\'

ExternalNssfFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnIdList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnIdList\'

ExternalSeppFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr\'

\- type: object

properties:

plmnId:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/PlmnId\'

sEPPId:

type: integer

fqdn:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Fqdn\'

EP\_N2-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N3-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

epTransportRefs:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/DnList\'

EP\_N4-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N5-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N6-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N7-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N8-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N9-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N10-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N11-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N12-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N13-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N14-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N15-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N16-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N17-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N20-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N21-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N22-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N26-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N27-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N31-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_N32-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

remotePlmnId:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/PlmnId\'

remoteSeppAddress:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/HostAddr\'

remoteSeppId:

type: integer

n32cParas:

type: string

n32fPolicy:

type: string

withIPX:

type: boolean

EP\_S5C-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_S5U-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_Rx-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_MAP\_SMSC-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_NLS-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

EP\_NLG-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/EP\_RP-Attr\'

\- type: object

properties:

localAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/RemoteAddress\'

FiveQiDscpMappingSet-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- type: object

properties:

FiveQiDscpMappingList:

type: array

items:

\$ref: \'\#/components/schemas/FiveQiDscpMapping\'

Configurable5QISet-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- type: object

properties:

configurable5QIs:

type: array

items:

\$ref: \'\#/components/schemas/FiveQICharacteristics\'

Dynamic5QISet-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- type: object

properties:

dynamic5QIs:

type: array

items:

\$ref: \'\#/components/schemas/FiveQICharacteristics\'

GtpUPathQoSMonitoringControl-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- type: object

properties:

gtpUPathQoSMonitoringState:

type: string

enum:

\- ENABLED

\- DISABLED

gtpUPathMonitoredSNSSAIs:

type: array

items:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/Snssai\'

monitoredDSCPs:

type: array

items:

type: integer

minimum: 0

maximum: 255

isEventTriggeredGtpUPathMonitoringSupported:

type: boolean

isPeriodicGtpUMonitoringSupported:

type: boolean

isImmediateGtpUMonitoringSupported:

type: boolean

gtpUPathDelayThresholds:

\$ref: \'\#/components/schemas/GtpUPathDelayThresholdsType\'

gtpUPathMinimumWaitTime:

type: integer

gtpUPathMeasurementPeriod:

type: integer

QFQoSMonitoringControl-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- type: object

properties:

qFQoSMonitoringState:

type: string

enum:

\- ENABLED

\- DISABLED

qFMonitoredSNSSAIs:

type: array

items:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/Snssai\'

qFMonitored5QIs:

type: array

items:

type: integer

minimum: 0

maximum: 255

isEventTriggeredQFMonitoringSupported:

type: boolean

isPeriodicQFMonitoringSupported:

type: boolean

isSessionReleasedQFMonitoringSupported:

type: boolean

qFPacketDelayThresholds:

\$ref: \'\#/components/schemas/QFPacketDelayThresholdsType\'

qFMinimumWaitTime:

type: integer

qFMeasurementPeriod:

type: integer

PredefinedPccRuleSet-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- type: object

properties:

predefinedPccRules:

type: array

items:

\$ref: \'\#/components/schemas/PccRule\'

\#\-\-\-\-\-\-\-- Definition of JSON arrays for name-contained IOCs
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

SubNetwork-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/SubNetwork-Single\'

ManagedElement-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/ManagedElement-Single\'

AmfFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/AmfFunction-Single\'

SmfFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/SmfFunction-Single\'

UpfFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/UpfFunction-Single\'

N3iwfFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/N3iwfFunction-Single\'

PcfFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/PcfFunction-Single\'

AusfFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/AusfFunction-Single\'

UdmFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/UdmFunction-Single\'

UdrFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/UdrFunction-Single\'

UdsfFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/UdsfFunction-Single\'

NrfFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/NrfFunction-Single\'

NssfFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/NssfFunction-Single\'

SmsfFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/SmsfFunction-Single\'

LmfFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/LmfFunction-Single\'

NgeirFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/NgeirFunction-Single\'

SeppFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/SeppFunction-Single\'

NwdafFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/NwdafFunction-Single\'

ScpFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/ScpFunction-Single\'

NefFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/NefFunction-Single\'

ExternalAmfFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/ExternalAmfFunction-Single\'

ExternalNrfFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/ExternalNrfFunction-Single\'

ExternalNssfFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/ExternalNssfFunction-Single\'

ExternalSeppFunction-Nultiple:

type: array

items:

\$ref: \'\#/components/schemas/ExternalSeppFunction-Single\'

AmfSet-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/AmfSet-Single\'

AmfRegion-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/AmfRegion-Single\'

EP\_N2-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N2-Single\'

EP\_N3-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N3-Single\'

EP\_N4-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N4-Single\'

EP\_N5-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N5-Single\'

EP\_N6-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N6-Single\'

EP\_N7-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N7-Single\'

EP\_N8-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N8-Single\'

EP\_N9-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N9-Single\'

EP\_N10-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N10-Single\'

EP\_N11-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N11-Single\'

EP\_N12-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N12-Single\'

EP\_N13-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N13-Single\'

EP\_N14-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N14-Single\'

EP\_N15-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N15-Single\'

EP\_N16-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N16-Single\'

EP\_N17-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N17-Single\'

EP\_N20-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N20-Single\'

EP\_N21-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N21-Single\'

EP\_N22-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N22-Single\'

EP\_N26-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N26-Single\'

EP\_N27-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N27-Single\'

EP\_N31-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N31-Single\'

EP\_N32-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_N32-Single\'

EP\_S5C-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_S5C-Single\'

EP\_S5U-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_S5U-Single\'

EP\_Rx-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_Rx-Single\'

EP\_MAP\_SMSC-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_MAP\_SMSC-Single\'

EP\_NLS-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_NLS-Single\'

EP\_NLG-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_NLG-Single\'

Configurable5QISet-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/Configurable5QISet-Single\'

Dynamic5QISet-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/Dynamic5QISet-Single\'

\#\-\-\-\-\-\-\-\-\-\-\-- Definitions in TS 28.541 for TS 28.532
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

resources-5gcNrm:

oneOf:

\- \$ref: \'\#/components/schemas/MnS\'

\- \$ref: \'\#/components/schemas/SubNetwork-Single\'

\- \$ref: \'\#/components/schemas/ManagedElement-Single\'

\- \$ref: \'\#/components/schemas/AmfFunction-Single\'

\- \$ref: \'\#/components/schemas/SmfFunction-Single\'

\- \$ref: \'\#/components/schemas/UpfFunction-Single\'

\- \$ref: \'\#/components/schemas/N3iwfFunction-Single\'

\- \$ref: \'\#/components/schemas/PcfFunction-Single\'

\- \$ref: \'\#/components/schemas/AusfFunction-Single\'

\- \$ref: \'\#/components/schemas/UdmFunction-Single\'

\- \$ref: \'\#/components/schemas/UdrFunction-Single\'

\- \$ref: \'\#/components/schemas/UdsfFunction-Single\'

\- \$ref: \'\#/components/schemas/NrfFunction-Single\'

\- \$ref: \'\#/components/schemas/NssfFunction-Single\'

\- \$ref: \'\#/components/schemas/SmsfFunction-Single\'

\- \$ref: \'\#/components/schemas/LmfFunction-Single\'

\- \$ref: \'\#/components/schemas/NgeirFunction-Single\'

\- \$ref: \'\#/components/schemas/SeppFunction-Single\'

\- \$ref: \'\#/components/schemas/NwdafFunction-Single\'

\- \$ref: \'\#/components/schemas/ScpFunction-Single\'

\- \$ref: \'\#/components/schemas/NefFunction-Single\'

\- \$ref: \'\#/components/schemas/ExternalAmfFunction-Single\'

\- \$ref: \'\#/components/schemas/ExternalNrfFunction-Single\'

\- \$ref: \'\#/components/schemas/ExternalNssfFunction-Single\'

\- \$ref: \'\#/components/schemas/ExternalSeppFunction-Single\'

\- \$ref: \'\#/components/schemas/AmfSet-Single\'

\- \$ref: \'\#/components/schemas/AmfRegion-Single\'

\- \$ref: \'\#/components/schemas/QFQoSMonitoringControl-Single\'

\- \$ref: \'\#/components/schemas/GtpUPathQoSMonitoringControl-Single\'

\- \$ref: \'\#/components/schemas/EP\_N2-Single\'

\- \$ref: \'\#/components/schemas/EP\_N3-Single\'

\- \$ref: \'\#/components/schemas/EP\_N4-Single\'

\- \$ref: \'\#/components/schemas/EP\_N5-Single\'

\- \$ref: \'\#/components/schemas/EP\_N6-Single\'

\- \$ref: \'\#/components/schemas/EP\_N7-Single\'

\- \$ref: \'\#/components/schemas/EP\_N8-Single\'

\- \$ref: \'\#/components/schemas/EP\_N9-Single\'

\- \$ref: \'\#/components/schemas/EP\_N10-Single\'

\- \$ref: \'\#/components/schemas/EP\_N11-Single\'

\- \$ref: \'\#/components/schemas/EP\_N12-Single\'

\- \$ref: \'\#/components/schemas/EP\_N13-Single\'

\- \$ref: \'\#/components/schemas/EP\_N14-Single\'

\- \$ref: \'\#/components/schemas/EP\_N15-Single\'

\- \$ref: \'\#/components/schemas/EP\_N16-Single\'

\- \$ref: \'\#/components/schemas/EP\_N17-Single\'

\- \$ref: \'\#/components/schemas/EP\_N20-Single\'

\- \$ref: \'\#/components/schemas/EP\_N21-Single\'

\- \$ref: \'\#/components/schemas/EP\_N22-Single\'

\- \$ref: \'\#/components/schemas/EP\_N26-Single\'

\- \$ref: \'\#/components/schemas/EP\_N27-Single\'

\- \$ref: \'\#/components/schemas/EP\_N31-Single\'

\- \$ref: \'\#/components/schemas/EP\_N31-Single\'

\- \$ref: \'\#/components/schemas/EP\_S5C-Single\'

\- \$ref: \'\#/components/schemas/EP\_S5U-Single\'

\- \$ref: \'\#/components/schemas/EP\_Rx-Single\'

\- \$ref: \'\#/components/schemas/EP\_MAP\_SMSC-Single\'

\- \$ref: \'\#/components/schemas/EP\_NLS-Single\'

\- \$ref: \'\#/components/schemas/EP\_NLG-Single\'

\- \$ref: \'\#/components/schemas/Configurable5QISet-Single\'

\- \$ref: \'\#/components/schemas/FiveQiDscpMappingSet-Single\'

\- \$ref: \'\#/components/schemas/PredefinedPccRuleSet-Single\'

\- \$ref: \'\#/components/schemas/Dynamic5QISet-Single\'
