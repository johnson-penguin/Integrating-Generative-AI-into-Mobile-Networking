######## Annex H (normative): YANG definitions for 5GC

H.1 General
===========

This annex contains the YANG definitions for the 5GC NRM, in accordance
with 5GC information model definitions specified in clause 4.

H.2 Void
========

H.3 Void
========

H.4 Void
========

H.5 Modules
===========

H.5.1 module \_3gpp-5g-common-yang-types.yang
---------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5g-common-yang-types {

yang-version 1.1;

namespace \"urn:3gpp:sa5:\_3gpp-5g-common-yang-types\";

prefix \"type5g3gpp\";

import \_3gpp-common-yang-types { prefix types3gpp; }

organization \"3GPP SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"The model defines common types for 5G networks and

network slicing.\";

reference \"3GPP TS 28.541\";

revision 2021-08-04 { reference S5-214052/CR-0517; }

revision 2020-11-05 { reference CR-0411 ; }

revision 2019-10-20 { reference \"Initial version.\"; }

grouping SNssai {

description

\"Single Network Slice Selection Assistance Information(S-NSSAI)\";

reference \"3GPP TS 23.003\";

leaf sd {

description \"Slice Differentiator

If not needed, the value can be set to FFFFFF.\";

type string{

length 6;

pattern \'\[a-fA-F0-9\]\*\';

}

reference \"3GPP TS 23.003\";

}

leaf sst {

type uint8;

description \"Slice/Service Type.

Values 0 to 127 belong to standardized SST range and are defined in

3GPP TS 23.501. Values 128 to 255 belong to operator-specific range.\";

}

}

grouping PLMNInfo {

description \"The PLMNInfo data type define a S-NSSAI member in a
specific

PLMNId, and it have two attributes PLMNId and S-NSSAI (PLMNId, S-NSSAI).

The PLMNId represents a data type that is comprised of mcc

(mobile country code) and mnc (mobile network code), (See TS 23.003

subclause 2.2 and 12.1) and S-NSSAI represents an data type, that is

comprised of an SST (Slice/Service type) and an optional

SD (Slice Differentiator) field\";

uses types3gpp:PLMNId;

uses SNssai;

}

typedef CommModelType {

reference \"3GPP TS 23501\";

type enumeration {

enum DIRECT\_COMMUNICATION\_WO\_NRF {

value 0;

description \"Directly communicate to other pre-configured NF
service.\";

}

enum DIRECT\_COMMUNICATION\_WITH\_NRF {

value 1;

description \"Directly communicate to other NF service discovered

by NRF.\";

}

enum INDIRECT\_COMMUNICATION\_WO\_DEDICATED\_DISCOVERY {

value 2;

description \"Communicate to pre-configured other NF service through

SCP as a proxy.\";

}

enum INDIRECT\_COMMUNICATION\_WITH\_DEDICATED\_DISCOVERY {

value 3;

description \"Communication to NF service discovered by NRF through SCP

as a proxy.\";

}

}

}

grouping CommModel {

leaf groupId {

type uint16;

}

leaf commModelType {

type CommModelType;

}

leaf-list targetNFServiceList {

type types3gpp:DistinguishedName;

}

leaf commModelConfiguration {

type string;

}

}

grouping SupportedFunc {

leaf function {

type string;

}

leaf policy {

type string;

}

}

typedef EnergySavingLoadThresholdT {

type uint32 {

range 0..10000;

}

units 1/10000;

}

typedef EnergySavingTimeDurationT {

type uint32 {

range 0..900;

}

units seconds;

}

typedef PhysCellID {

type uint32 {

range \"0..1007\";

}

reference \"clause 7.4.2 of TS 38.211\";

}

typedef UTC24TimeOfDayT {

description \"Time of day in HH:MM or H:MM 24-hour format per UTC

time zone.\";

type string {

pattern \"((\[01\]?\[0-9\])\|(2\[0-3\])):(\[0-5\]\[0-9\])\";

}

}

typedef DayOfWeekT {

type enumeration {

enum Monday;

enum Tuesday;

enum Wednesday;

enum Thursday;

enum Friday;

enum Saturday;

enum Sunday;

}

}

}

\<CODE ENDS\>

H.5.1a module \_3gpp-5gc-nrm-affunction.yang
--------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-affunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-affunction;

prefix af3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3gpp SA5\";

description \"This IOC is defined only to describe the IOCs representing

its interaction interface with 5GC (i.e. EP\_Rx and EP\_N5).

It has no attributes defined.\";

reference \"3GPP TS 28.541\";

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-05-15 {

description \"initial revision\";

}

grouping AFFunctionGrp {

uses mf3gpp:ManagedFunctionGrp;

}

augment \"/me3gpp:ManagedElement\" {

list AFFunction {

description \"5G Core AF Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses AFFunctionGrp;

}

}

}

}

\<CODE ENDS\>

H.5.2 module \_3gpp-5gc-nrm-amffunction.yang
--------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-amffunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-amffunction;

prefix amf3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

import ietf-inet-types { prefix inet; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"AMFFunction derived from basic ManagedFunction.\";

revision 2020-11-05 { reference CR-0411 ; }

revision 2019-10-25 { reference \"S5-194457 S5-193518\"; }

revision 2019-05-31 { reference \"Ericsson refactoring.\"; }

revision 2018-08-07 { reference \"Initial revision\"; }

grouping AMFFunctionGrp {

description \"Represents the AMFFunction IOC\";

uses mf3gpp:ManagedFunctionGrp;

list pLMNIdList {

min-elements 1;

description \"A list of PLMN identifiers (Mobile Country Code and Mobile

Network Code).\";

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

container aMFIdentifier {

presence true;

description \"An AMF identifier, comprising an AMF Region ID, an

AMF Set ID and an AMF Pointer.\";

uses types3gpp:AmfIdentifier;

}

leaf sBIFQDN {

description \"The FQDN of the registered NF instance in the

service-based interface.\";

type inet:domain-name;

}

list sNSSAIList {

min-elements 1;

description \"List of S-NSSAIs the managed object is capable of
supporting.

(Single Network Slice Selection Assistance Information)

An S-NSSAI has an SST (Slice/Service type) and an optional SD

(Slice Differentiator) field.\";

reference \"3GPP TS 23.003\";

key \"sd sst\";

uses types5g3gpp:SNssai;

}

list managedNFProfile {

key idx;

min-elements 1;

max-elements 1;

uses types3gpp:ManagedNFProfile;

}

list commModelList {

min-elements 1;

key \"groupId\";

description \"Specifies a list of commModel. It can be used by NF and

NF services to interact with each other in 5G Core network \";

reference \"3GPP TS 23.501\";

uses types5g3gpp:CommModel;

}

}

augment \"/me3gpp:ManagedElement\" {

list AMFFunction {

description \"5G Core AMF Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses AMFFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

H.5.3 module \_3gpp-5gc-nrm-amfregion.yang
------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-amfregion {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-amfregion;

prefix amfr3gpp;

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"This IOC represents the AMF Region which consists one or

multiple AMF Sets.\";

revision 2020-11-05 { reference CR-0411 ; }

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-11 { reference \"Ericsson refactoring.\"; }

grouping AMFRegionGrp {

description \"Represents the AMFRegion IOC\";

uses mf3gpp:ManagedFunctionGrp;

list pLMNIdList {

description \"List of at most six entries of PLMN Identifiers, but at

least one (the primary PLMN Id).

The PLMN Identifier is composed of a Mobile Country Code (MCC)

and a Mobile Network Code (MNC).\";

min-elements 1;

max-elements 6;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

leaf-list nRTACList {

description \"List of Tracking Area Codes (legacy TAC or extended TAC)

where the represented management function is serving.\";

reference \"TS 38.413 clause 9.3.3.10\";

min-elements 1;

config false;

type types3gpp:Tac;

}

list sNSSAIList {

description \"List of S-NSSAIs the managed object is capable of
supporting.

(Single Network Slice Selection Assistance Information)

An S-NSSAI has an SST (Slice/Service type) and an optional SD

(Slice Differentiator) field.\";

//conditional support only if the network slicing feature is supported.

reference \"3GPP TS 23.003\";

key \"sd sst\";

uses types5g3gpp:SNssai;

}

leaf aMFRegionId {

description \"Represents the AMF Region ID, which identifies the
region.\";

mandatory true;

type types3gpp:AmfRegionId;

}

leaf-list aMFSet {

description \"The AMFSet that the AFMRegion is associated with.\";

min-elements 1;

type instance-identifier;

}

}

augment \"/subnet3gpp:SubNetwork\" {

list AMFRegion {

description \"5G Core AMFRegion IOC\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses AMFRegionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

H.5.4 module \_3gpp-5gc-nrm-amfset.yang
---------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-amfset {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-amfset;

prefix amfset3gpp;

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"This IOC represents the AMF Set which consists of some
AMFs

that serve a given area and Network Slice.\";

revision 2020-11-05 { reference CR-0411 ; }

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-11 { reference \"Ericsson refactoring.\"; }

grouping AMFSetGrp {

description \"Represents the AMFSet IOC\";

uses mf3gpp:ManagedFunctionGrp;

list pLMNIdList {

description \"List of at most six entries of PLMN Identifiers, but at

least one (the primary PLMN Id). The PLMN Identifier is composed

of a Mobile Country Code (MCC) and a Mobile Network Code (MNC).\";

min-elements 1;

max-elements 6;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

leaf-list nRTACList {

description \"List of Tracking Area Codes (legacy TAC or extended TAC)

where the represented management function is serving.\";

reference \"TS 38.413 clause 9.3.3.10\";

min-elements 1;

config false;

type types3gpp:Tac;

}

list sNSSAIList {

description \"List of S-NSSAIs the managed object is capable of
supporting.

(Single Network Slice Selection Assistance Information)

An S-NSSAI has an SST (Slice/Service type) and an optional SD

(Slice Differentiator) field.\";

//conditional support only if the network slicing feature is supported.

reference \"3GPP TS 23.003\";

key \"sd sst\";

uses types5g3gpp:SNssai;

}

leaf aMFRegion {

description \"The AMFRegion that the AFMSet is associated with.\";

type instance-identifier;

}

leaf-list aMFSetMemberList {

description \"List of DNs of AMFFunction instances of the AMFSet.\";

min-elements 1;

max-elements 1;

type types3gpp:DistinguishedName;

}

}

augment \"/subnet3gpp:SubNetwork\" {

list AMFSet {

description \"5G Core AMFSet IOC\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses AMFSetGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

H.5.5 module \_3gpp-5gc-nrm-ausffunction.yang
---------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-ausffunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-ausffunction;

prefix ausf3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import ietf-inet-types { prefix inet; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"This IOC represents the AUSF function in 5GC. For more

information about the AUSF, see 3GPP TS 23.501.\";

reference \"3GPP TS 28.541\";

revision 2020-11-05 { reference CR-0411 ; }

revision 2019-10-25 { reference \"S5-194457 S5-193518\"; }

revision 2019-05-22 {reference \"initial revision\"; }

grouping AUSFFuntionGrp {

description \"Represents the AUSFFuntion IOC\";

uses mf3gpp:ManagedFunctionGrp;

list pLMNIdList {

description \"List of at most six entries of PLMN Identifiers, but at

least one (the primary PLMN Id).

The PLMN Identifier is composed of a Mobile Country Code (MCC) and

a Mobile Network Code (MNC).\";

min-elements 1;

max-elements 6;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

leaf sBIFQDN {

description \"The FQDN of the registered NF instance in the

service-based interface.\";

type inet:domain-name;

}

list sNSSAIList {

description \"List of S-NSSAIs the managed object is capable of
supporting.

(Single Network Slice Selection Assistance Information)

An S-NSSAI has an SST (Slice/Service type) and an optional SD

(Slice Differentiator) field.\";

//optional support

reference \"3GPP TS 23.003\";

key \"sd sst\";

uses types5g3gpp:SNssai;

}

list managedNFProfile {

key idx;

min-elements 1;

max-elements 1;

uses types3gpp:ManagedNFProfile;

}

list commModelList {

min-elements 1;

key \"groupId\";

description \"Specifies a list of commModel. It can be used by NF and

NF services to interact with each other in 5G Core network \";

reference \"3GPP TS 23.501\";

uses types5g3gpp:CommModel;

}

}

augment \"/me3gpp:ManagedElement\" {

list AUSFFunction {

description \"5G Core AUSF Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses AUSFFuntionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

H.5.6 module \_3gpp-5gc-nrm-dnfunction.yang
-------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-dnfunction {

yang-version 1.1;

namespace urn:3gpp:sa5\_3gpp-5gc-nrm-dnfunction;

prefix dn3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3gpp SA5\";

description \"This IOC is defined only to describe the IOCs representing

Data Network (DN) interaction interface with 5GC (i.e. EP\_N6).

It has no attributes defined.\";

reference \"3GPP TS 28.541\";

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-05-15 {

description \"initial revision\";

}

grouping DNFunctionGrp {

uses mf3gpp:ManagedFunctionGrp;

}

augment \"/me3gpp:ManagedElement\" {

list DNFunction {

description \"5G Core DN Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses DNFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

H.5.7 module \_3gpp-5gc-nrm-ep.yang
-----------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-ep {

yang-version 1.1;

namespace \"urn:3gpp:tsg:sa5:nrm:\_3gpp-5gc-nrm-ep\";

prefix \"cep3gpp\";

import \_3gpp-common-ep-rp { prefix eprp3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-5gc-nrm-affunction { prefix af3gpp; }

import \_3gpp-5gc-nrm-amffunction { prefix amf3gpp; }

import \_3gpp-5gc-nrm-ausffunction { prefix ausf3gpp; }

import \_3gpp-5gc-nrm-dnfunction { prefix dn3gpp; }

import \_3gpp-5gc-nrm-lmffunction { prefix lmf3gpp; }

import \_3gpp-5gc-nrm-n3iwffunction { prefix n3iwf3gpp; }

import \_3gpp-5gc-nrm-ngeirfunction { prefix ngeir3gpp; }

import \_3gpp-5gc-nrm-nrffunction { prefix nrf3gpp; }

import \_3gpp-5gc-nrm-nssffunction { prefix nssf3gpp; }

import \_3gpp-5gc-nrm-pcffunction { prefix pcf3gpp; }

import \_3gpp-5gc-nrm-seppfunction { prefix sepp3gpp; }

import \_3gpp-5gc-nrm-smffunction { prefix smf3gpp; }

import \_3gpp-5gc-nrm-smsffunction { prefix smsf3gpp; }

import \_3gpp-5gc-nrm-udmfunction { prefix udm3gpp; }

import \_3gpp-5gc-nrm-upffunction { prefix upf3gpp; }

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import ietf-inet-types { prefix inet; }

organization \"3GPP SA5\";

description \"Defines the YANG mapping of the 5GC related endpoint

Information Object Classes (IOCs) that are part of the 5G Core

Network Resource Model.\";

reference \"3GPP TS 28.541\";

revision 2019-11-18 {

description \"Ericsson refactoring.\";

}

revision 2018-07-31 {

description \"Initial revision\";

}

grouping EP\_N2Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N3Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N4Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N5Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N6Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N7Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N8Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N9Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N10Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N11Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N12Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N13Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N14Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N15Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N16Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N17Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N20Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N21Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N22Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N26Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N27Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N31Grp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_N32Grp {

uses eprp3gpp:EP\_Common;

container remotePlmnId {

description \"PLMN Identifiers of the remote sepp.

The PLMN Identifier is composed of a Mobile Country Code (MCC) and a
Mobile Network Code (MNC).\";

uses types3gpp:PLMNId;

}

leaf remoteSeppAddress {

description \"The host address of the SEPP.\";

type inet:host;

}

leaf remoteSeppId {

type uint16;

}

leaf n32cParas {

type string;

}

leaf n32fPolicy {

type string;

}

leaf withIPX {

type boolean;

}

}

grouping EP\_S5CGrp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_S5UGrp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_RxGrp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_MAP\_SMSCGrp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_NLSGrp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_NLGGrp {

uses eprp3gpp:EP\_Common;

}

grouping EP\_SBI\_IPXGrp {

uses eprp3gpp:EP\_Common;

leaf-list sBIService {

min-elements 1;

config false;

type string;

}

}

augment \"/me3gpp:ManagedElement/af3gpp:AFFunction\" {

list EP\_N6 {

description \"Represents the EP\_N6 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N6Grp;

}

}

list EP\_Rx {

description \"Represents the EP\_Rx IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_RxGrp;

}

}

}

augment \"/me3gpp:ManagedElement/amf3gpp:AMFFunction\" {

list EP\_N2 {

description \"Represents the EP\_N2 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N2Grp;

}

}

list EP\_N8 {

description \"Represents the EP\_N8 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N8Grp;

}

}

list EP\_N11 {

description \"Represents the EP\_N11 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N11Grp;

}

}

list EP\_N12 {

description \"Represents the EP\_N12 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N12Grp;

}

}

list EP\_N14 {

description \"Represents the EP\_N14 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N14Grp;

}

}

list EP\_N15 {

description \"Represents the EP\_N15 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N15Grp;

}

}

list EP\_N17 {

description \"Represents the EP\_N17 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N17Grp;

}

}

list EP\_N20 {

description \"Represents the EP\_N20 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N20Grp;

}

}

list EP\_N22 {

description \"Represents the EP\_N22 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N22Grp;

}

}

list EP\_N26 {

description \"Represents the EP\_N26 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N26Grp;

}

}

list EP\_NLS {

description \"Represents the EP\_NLS IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_NLSGrp;

}

}

list EP\_NLG {

description \"Represents the EP\_NLG IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_NLGGrp;

}

}

}

augment \"/me3gpp:ManagedElement/ausf3gpp:AUSFFunction\" {

list EP\_N12 {

description \"Represents the EP\_N12 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N12Grp;

}

}

list EP\_N13 {

description \"Represents the EP\_N13 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N13Grp;

}

}

}

augment \"/me3gpp:ManagedElement/dn3gpp:DNFunction\" {

list EP\_N6 {

description \"Represents the EP\_N6 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N6Grp;

}

}

}

augment \"/me3gpp:ManagedElement/lmf3gpp:LMFFunction\" {

list EP\_NLS {

description \"Represents the EP\_NLS IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_NLSGrp;

}

}

}

augment \"/me3gpp:ManagedElement/n3iwf3gpp:N3IWFFunction\" {

list EP\_N2 {

description \"Represents the EP\_N2 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N2Grp;

}

}

list EP\_N3 {

description \"Represents the EP\_N3 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N3Grp;

}

}

}

augment \"/me3gpp:ManagedElement/ngeir3gpp:NGEIRFunction\" {

list EP\_N17 {

description \"Represents the EP\_N17 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N17Grp;

}

}

}

augment \"/me3gpp:ManagedElement/nrf3gpp:NRFFunction\" {

list EP\_N27 {

description \"Represents the EP\_N27 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N26Grp;

}

}

}

augment \"/me3gpp:ManagedElement/nssf3gpp:NSSFFunction\" {

list EP\_N22 {

description \"Represents the EP\_N22 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N22Grp;

}

}

list EP\_N31 {

description \"Represents the EP\_N31 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N31Grp;

}

}

}

augment \"/me3gpp:ManagedElement/pcf3gpp:PCFFunction\" {

list EP\_N5 {

description \"Represents the EP\_N5 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N5Grp;

}

}

list EP\_N7 {

description \"Represents the EP\_N7 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N7Grp;

}

}

list EP\_N15 {

description \"Represents the EP\_N15 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N15Grp;

}

}

list EP\_N16 {

description \"Represents the EP\_N16 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N16Grp;

}

}

list EP\_Rx {

description \"Represents the EP\_Rx IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_RxGrp;

}

}

}

augment \"/me3gpp:ManagedElement/sepp3gpp:SEPPFunction\" {

list EP\_N32 {

description \"Represents the EP\_N32 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N32Grp;

}

}

}

augment \"/me3gpp:ManagedElement/smsf3gpp:SMSFFunction\" {

list EP\_N20 {

description \"Represents the EP\_20 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N20Grp;

}

}

list EP\_N21 {

description \"Represents the EP\_N21 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N21Grp;

}

}

list EP\_MAP\_SMSC {

description \"Represents the EP\_MAP\_SMSC IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_MAP\_SMSCGrp;

}

}

}

augment \"/me3gpp:ManagedElement/smf3gpp:SMFFunction\" {

list EP\_N4 {

description \"Represents the EP\_N4 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N4Grp;

}

}

list EP\_N7 {

description \"Represents the EP\_N7 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N7Grp;

}

}

list EP\_N10 {

description \"Represents the EP\_N10 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N10Grp;

}

}

list EP\_N11 {

description \"Represents the EP\_N11 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N11Grp;

}

}

list EP\_N16 {

description \"Represents the EP\_N16 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N16Grp;

}

}

list EP\_S5C {

description \"Represents the EP\_S5C IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_S5CGrp;

}

}

}

augment \"/me3gpp:ManagedElement/udm3gpp:UDMFunction\" {

list EP\_N8 {

description \"Represents the EP\_N8 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N8Grp;

}

}

list EP\_N10 {

description \"Represents the EP\_N10 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N10Grp;

}

}

list EP\_N13 {

description \"Represents the EP\_N13 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N13Grp;

}

}

}

augment \"/me3gpp:ManagedElement/upf3gpp:UPFFunction\" {

list EP\_N4 {

description \"Represents the EP\_N4 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N4Grp;

}

}

list EP\_N3 {

description \"Represents the EP\_N3 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N3Grp;

}

}

list EP\_N9 {

description \"Represents the EP\_N9 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N9Grp;

}

}

list EP\_S5U {

description \"Represents the EP\_S5U IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_S5UGrp;

}

}

list EP\_EP\_N6 {

description \"Represents the EP\_N6 IOC.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses EP\_N6Grp;

}

}

}

}

\<CODE ENDS\>

H.5.8 module \_3gpp-5gc-nrm-externalnrffunction.yang
----------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-externalnrffunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-externalnrffunction;

prefix extnrf3gpp;

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-common-managed-function { prefix mf3gpp; }

description \"This IOC represents external NRF function controlled by
another management domain.\";

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-11 {

description \"Ericsson refactoring.\";

}

grouping ExternalNRFFunctionGrp {

uses mf3gpp:ManagedFunctionGrp;

list pLMNIdList {

description \"List of at most six entries of PLMN Identifiers, but at
least one (the primary PLMN Id).

The PLMN Identifier is composed of a Mobile Country Code (MCC) and a
Mobile Network Code (MNC).\";

min-elements 1;

max-elements 6;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

}

augment \"/subnet3gpp:SubNetwork\" {

list ExternalNRFFunction {

description \"5G Core External NRF Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses ExternalNRFFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses; }

}

}

\<CODE ENDS\>

H.5.9 module \_3gpp-5gc-nrm-externalnssffunction.yang
-----------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-externalnssffunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-externalnssffunction;

prefix extnssf3gpp;

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-common-managed-function { prefix mf3gpp; }

description \"This IOC represents external NSSF function controlled by
another management domain.\";

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-06-11 {

description \"Ericsson refactoring.\";

}

grouping ExternalNSSFFunctionGrp {

uses mf3gpp:ManagedFunctionGrp;

list pLMNIdList {

description \"List of at most six entries of PLMN Identifiers, but at
least one (the primary PLMN Id).

The PLMN Identifier is composed of a Mobile Country Code (MCC) and a
Mobile Network Code (MNC).\";

min-elements 1;

max-elements 6;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

}

augment \"/subnet3gpp:SubNetwork\" {

list ExternalNSSFFunction {

description \"5G Core External NSSF Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses ExternalNSSFFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

H.5.10 module \_3gpp-5gc-nrm-lmffunction.yang
---------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-lmffunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-lmffunction;

prefix lmf3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3gpp SA5\";

description \"This IOC represents the LMF function defined in 3GPP TS
23.501.\";

reference \"3GPP TS 28.541\";

revision 2019-10-25 { reference \"S5-194457 S5193518\"; }

revision 2019-05-15 {

description \"initial revision\";

reference \"Based on

3GPP TS 28.541\";

}

grouping LMFFunctionGrp {

uses mf3gpp:ManagedFunctionGrp;

list pLMNIdList {

description \"List of at most six entries of PLMN Identifiers, but at
least one (the primary PLMN Id).

The PLMN Identifier is composed of a Mobile Country Code (MCC) and a
Mobile Network Code (MNC).\";

min-elements 1;

max-elements 6;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

list managedNFProfile {

key idx;

min-elements 1;

uses types3gpp:ManagedNFProfile;

}

list commModelList {

min-elements 1;

key \"groupId\";

uses types5g3gpp:CommModel;

}

}

augment \"/me3gpp:ManagedElement\" {

list LMFFunction {

description \"5G Core LMF Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses LMFFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

H.5.11 module \_3gpp-5gc-nrm-n3iwffunction.yang
-----------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-n3iwffunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-n3iwffunction;

prefix n3iwf3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3gpp SA5\";

description \"This IOC represents the N3IWF function which is used to
enable non-3GPP

access networks connected to the 5GC. For more information about the
N3IWF, see 3GPP TS 23.501.\";

reference \"3GPP TS 28.541\";

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-05-22 {

description \"initial revision\";

}

grouping N3IWFFunctionGrp {

uses mf3gpp:ManagedFunctionGrp;

list pLMNIdList {

description \"List of at most six entries of PLMN Identifiers, but at
least one (the primary PLMN Id).

The PLMN Identifier is composed of a Mobile Country Code (MCC) and a
Mobile Network Code (MNC).\";

min-elements 1;

max-elements 6;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

list commModelList {

min-elements 1;

key \"groupId\";

uses types5g3gpp:CommModel;

}

}

augment \"/me3gpp:ManagedElement\" {

list N3IWFFunction {

description \"5G Core N3IWF Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses N3IWFFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

H.5.12 module \_3gpp-5gc-nrm-nfprofile.yang
-------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-nfprofile {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-nfprofile;

prefix nfp3gpp;

import \_3gpp-common-yang-types { prefix types3gpp; }

import ietf-inet-types { prefix inet; }

import ietf-yang-types { prefix yang; }

import \_3gpp-5gc-nrm-nfservice { prefix nfs3gpp; }

organization \"3gpp SA5\";

description \"NF profile class.\";

reference \"3GPP TS 29.510\";

revision 2019-06-17 {

description \"initial revision\";

}

grouping NFProfileGrp {

leaf nfInstanceID {

description \"String uniquely identifying a NF instance.\";

mandatory true;

type string;

}

leaf nfType {

description \"Type of Network Function.\";

mandatory true;

type types3gpp:NfType;

}

leaf nfStatus {

description \"Status of the NF Instance.\";

mandatory true;

type NFStatus;

}

leaf heartBeatTimer {

description \"Time in seconds expected between 2 consecutive heart-beat
messages from

an NF Instance to the NRF. It may be included in the registration
request.

When present in the request it shall contain the heartbeat time proposed
by the NF service consumer.\";

//conditional support

type uint16;

}

list plmnList {

description \"PLMN(s) of the Network Function.

This IE shall be present if this information is available for the NF.

If not provided, PLMN ID(s) of the PLMN of the NRF are assumed for the
NF.\";

//conditional support

min-elements 1;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

list sNssais { //is the key unique

description \"S-NSSAIs of the Network Function. If not provided, the NF
can serve any S-NSSAI.

When present this IE represents the list of S-NSSAIs supported in all
the PLMNs listed in the plmnList IE.\";

min-elements 1;

//optional support

key \"sst sd\";

uses Snssai;

}

list perPlmnSnssaiList {

description \"This IE may be included when the list of S-NSSAIs
supported by the NF for each PLMN it is supporting is different.

When present, this IE shall include the S-NSSAIs supported by the
Network Function

for each PLMN supported by the Network Function. When present, this IE
shall override sNssais IE.\";

min-elements 1;

//optional support

key idx; //no obvious leaf to use as a key

leaf idx { type uint32; }

uses PlmnSnssai;

}

leaf-list nsiList {

description \"NSI identities of the Network Function.

If not provided, the NF can serve any NSI.\";

//optional support

min-elements 1;

type string;

}

leaf fqdn {

description \"FQDN of the Network Function. For AMF, the FQDN registered
with the NRF

shall be that of the AMF Name.\";

//conditional support

type inet:domain-name;

}

leaf interPlmnFqdn {

description \"If the NF needs to be discoverable by other NFs in a
different PLMN,

then an FQDN that is used for inter-PLMN routing is specified.\";

//conditional support

type inet:domain-name;

}

leaf-list ipv4Addresses {

description \"IPv4 address(es) of the Network Function.\";

min-elements 1;

//conditional support

type inet:ipv4-address;

}

leaf-list ipv6Addresses {

description \"IPv6 address(es) of the Network Function.\";

min-elements 1;

//conditional support

type inet:ipv6-address;

}

list allowedPlmns {

description \"PLMNs allowed to access the NF instance.

If not provided, any PLMN is allowed to access the NF.\";

min-elements 1;

//optional support

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

leaf-list allowedNfTypes {

description \"Type of the NFs allowed to access the NF instance.

If not provided, any NF type is allowed to access the NF.\";

min-elements 1;

//optional support

type types3gpp:NfType;

}

leaf-list allowedNfDomains {

description \"Pattern representing the NF domain names allowed to access
the NF instance.

If not provided, any NF domain is allowed to access the NF.\";

min-elements 1;

//optional support

type string;

}

list allowedNssais { //is the key unique

description \"S-NSSAI of the allowed slices to access the NF instance.

If not provided, any slice is allowed to access the NF.\";

min-elements 1;

//optional support

key \"sst sd\";

uses Snssai;

}

leaf priority {

description \"Priority (relative to other NFs of the same type) in the
range of 0-65535, to be used for NF selection;

lower values indicate a higher priority. If priority is also present in
the nfServiceList parameters,

those will have precedence over this value. The NRF may overwrite the
received priority value when exposing

an NFProfile with the Nnrf\_NFDiscovery service.\";

//optional support

type uint16;

}

leaf capacity {

description \"Static capacity information in the range of 0-65535,
expressed as a weight

relative to other NF instances of the same type; if capacity is also
present

in the nfServiceList parameters, those will have precedence over this
value.\";

//optional support

type uint16;

}

leaf load {

description \"Dynamic load information, ranged from 0 to 100, indicates
the current load percentage of the NF.\";

//optional support

type types3gpp:Load;

}

leaf locality {

description \"Operator defined information about the location of the NF
instance (e.g. geographic location, data center).\";

//optional support

type string;

}

grouping udrInfo {

//optional support

leaf groupId {

description \"Identity of the UDR group that is served by the UDR
instance.

If not provided, the UDR instance does not pertain to any UDR group.\";

//optional support

type string;

}

list supiRanges {

description \"List of ranges of SUPI\'s whose profile data is available
in the UDR instance.\";

key \"start end pattern\";

min-elements 1;

//optional support

uses SupiRange;

}

list gpsiRanges {

description \"List of ranges of GPSIs whose profile data is available in
the UDR instance.\";

key \"start end pattern\";

min-elements 1;

//optional support

uses IdentityRange;

}

list externalGroupIdentifiersRanges {

description \"List of ranges of external groups whose profile data is
available in the UDR instance.\";

key \"start end pattern\";

min-elements 1;

//optional support

uses IdentityRange;

}

leaf-list supportedDataSets {

description \"List of supported data sets in the UDR instance.

If not provided, the UDR supports all data sets.\";

min-elements 1;

//optional support

type DataSetId;

}

}

grouping udmInfo {

//optional support

leaf groupId {

description \"Identity of the UDM group that is served by the UDM
instance.

If not provided, the UDM instance does not pertain to any UDM group.\";

//optional support

type string;

}

list supiRanges {

description \"List of ranges of SUPI\'s whose profile data is available
in the UDM instance.\";

key \"start end pattern\";

min-elements 1;

//optional support

uses SupiRange;

}

list gpsiRanges {

description \"List of ranges of GPSIs whose profile data is available in
the UDM instance.\";

key \"start end pattern\";

min-elements 1;

//optional support

uses IdentityRange;

}

list externalGroupIdentifiersRanges {

description \"List of ranges of external groups whose profile data is
available in the UDM instance.\";

key \"start end pattern\";

min-elements 1;

//optional support

uses IdentityRange;

}

leaf-list routingIndicators {

description \"List of Routing Indicator information that allows to route
network signalling with SUCI

to the UDM instance. If not provided, the UDM can serve any Routing
Indicator.

Pattern: \'\^\[0-9\]{1,4}\$\'.\";

//optional support

min-elements 1;

type string;

}

}

grouping ausfInfo {

//optional support

leaf groupId {

description \"Identity of the AUSF group. If not provided, the AUSF
instance does not pertain to any AUSF group.\";

//optional support

type string;

}

list supiRanges {

description \"List of ranges of SUPIs that can be served by the AUSF
instance. If not provided, the AUSF can serve any SUPI.\";

key \"start end pattern\";

min-elements 1;

//optional support

uses SupiRange;

}

leaf-list routingIndicators {

description \"List of Routing Indicator information that allows to route
network signalling with SUCI

to the AUSF instance. If not provided, the AUSF can serve any Routing
Indicator.

Pattern: \'\^\[0-9\]{1,4}\$\'.\";

//optional support

min-elements 1;

type string;

}

}

grouping amfInfo {

//optional support

leaf amfRegionId {

description \"AMF region identifier\";

type string;

}

leaf amfSetId {

description \"AMF set identifier\";

type string;

}

list guamiList {

description \"List of supported GUAMIs.\";

key idx; //no obvious leaf to use as a key

leaf idx { type uint32; }

min-elements 1;

uses Guami;

}

list taiList {

description \"The list of TAIs the AMF can serve. It may contain the
non-3GPP access TAI.

The absence of this attribute and the taiRangeList attribute indicate
that

the AMF can be selected for any TAI in the serving network.\";

key idx; //no obvious leaf to use as a key

leaf idx { type uint32; }

//optional support

min-elements 1;

uses Tai;

}

list taiRangeList {

description \"The range of TAIs the AMF can serve. The absence of this
attribute and the taiList

attribute indicate that the AMF can be selected for any TAI in the
serving network.\";

//optional support

min-elements 1;

key idx; //no obvious leaf to use as a key

leaf idx { type uint32; }

uses TaiRange;

}

list backupInfoAmfFailure {

description \"List of GUAMIs for which the AMF acts as a backup for AMF
failure.\";

key idx; //no obvious leaf to use as a key

leaf idx { type uint32; }

//optional support

min-elements 1;

uses Guami;

}

list backupInfoAmfRemoval {

description \"List of GUAMIs for which the AMF acts as a backup for
planned AMF removal.\";

key idx; //no obvious leaf to use as a key

leaf idx { type uint32; }

//optional support

min-elements 1;

uses Guami;

}

list n2InterfaceAmfInfo {

description \"N2 interface information of the AMF. This information
needs not be sent in NF Discovery responses.

It may be used by the NRF to update the DNS for AMF discovery by the 5G
Access Network.\";

//optional support

max-elements 1;

key idx; //no obvious leaf to use as a key

leaf idx { type uint32; }

uses N2InterfaceAmfInfo;

}

}

grouping smfInfo {

//optional support

list sNssaiSmfInfoList {

description \"List of parameters supported by the SMF per S-NSSAI.\";

min-elements 1;

key idx; //no obvious leaf to use as a key

leaf idx { type uint32; }

uses sNssaiSmfInfoItem;

}

list taiList {

description \"The list of TAIs the SMF can serve. It may contain the
non-3GPP access TAI.

The absence of this attribute and the taiRangeList attribute indicate
that

the SMF can be selected for any TAI in the serving network.\";

key idx; //no obvious leaf to use as a key

leaf idx { type uint32; }

//optional support

min-elements 1;

uses Tai;

}

list taiRangeList {

description \"The range of TAIs the SMF can serve. The absence of this
attribute and the taiList

attribute indicate that the SMF can be selected for any TAI in the
serving network.\";

//optional support

min-elements 1;

key idx; //no obvious leaf to use as a key

leaf idx { type uint32; }

uses TaiRange;

}

leaf pgwFqdn {

description \"The FQDN of the PGW if the SMF is a combined SMF/PGW-C.\";

//optional support

type inet:domain-name;

}

leaf-list accessType {

description \"If included, this IE shall contain the access type
(3GPP\_ACCESS and/or NON\_3GPP\_ACCESS) supported by the SMF.

If not included, it shall be assumed the both access types are
supported.\";

//conditional support

min-elements 1;

max-elements 2;

type AccessType;

}

}

grouping upfInfo {

//optional support

list sNssaiUpfInfoList {

description \"List of parameters supported by the UPF per S-NSSAI.\";

min-elements 1;

key idx; //no obvious leaf to use as a key

leaf idx { type uint32; }

uses SnssaiUpfInfoItem;

}

leaf-list smfServingArea {

description \"The SMF service area(s) the UPF can serve.

If not provided, the UPF can serve any SMF service area.\";

//optional support

min-elements 1;

type string;

}

list interfaceUpfInfo {

description \"List of User Plane interfaces configured on the UPF. When
this IE is provided in the NF Discovery response,

the NF Service Consumer (e.g. SMF) may use this information for UPF
selection.\";

key idx; //no obvious leaf to use as a key

leaf idx { type uint32; }

//optional support

min-elements 1;

uses InterfaceUpfInfoItem;

}

leaf iwkEpsInd {

description \"Indicates whether interworking with EPS is supported by
the UPF.

true: Supported

false (default): Not Supported\";

//optional support

type boolean;

}

leaf-list pduSessionTypes {

description \"List of PDU session type(s) supported by the UPF. The
absence of this attribute indicates that the UPF can be selected

for any PDU session type.\";

//optional support

min-elements 1;

type PduSessionType;

}

}

grouping pcfInfo {

//optional support

leaf-list dnnList {

description \"DNNs supported by the PCF.

If not provided, the PCF can serve any DNN.\";

//optional support

min-elements 1;

type string;

}

list supiRanges {

description \"List of ranges of SUPIs that can be served by the PCF
instance. If not provided, the PCF can serve any SUPI.\";

key \"start end pattern\";

min-elements 1;

//optional support

uses SupiRange;

}

leaf rxDiamHost {

description \"This IE shall be present if the PCF supports Rx interface.

When present, this IE shall indicate the Diameter host of the Rx
interface for the PCF.

Pattern: \'\^(\[A-Za-z0-9\]+(-\[A-Za-z0-9\]+).)+\[a-z\]{2,}\$\'.\";

//conditional support

type string;

}

leaf rxDiamRealm {

description \"This IE shall be present if the PCF supports Rx interface.

When present, this IE shall indicate the Diameter realm of the Rx
interface for the PCF.

Pattern: \'\^(\[A-Za-z0-9\]+(-\[A-Za-z0-9\]+).)+\[a-z\]{2,}\$\'.\";

//conditional support

type string;

}

}

grouping bsfInfo {

//optional support

list ipv4AddressRanges {

description \"List of ranges of IPv4 addresses handled by BSF.

If not provided, the BSF can serve any IPv4 address.\";

//optional support

key \"start end\";

uses types3gpp:Ipv4AddressRange;

}

leaf-list dnnList {

description \"List of DNNs handled by the BSF

If not provided, the BSF can serve any DNN.\";

//optional support

min-elements 1;

type string;

}

leaf-list ipDomainList {

description \"List of IPv4 address domains, as described in subclause
6.2 of 3GPP TS 29.513, handled by the BSF.

If not provided, the BSF can serve any IP domain.\";

//optional support

min-elements 1;

type string;

}

list ipv6PrefixRanges {

description \"List of ranges of IPv6 prefixes handled by the BSF.

If not provided, the BSF can serve any IPv6 prefix.\";

//optional support

key \"start end\";

uses types3gpp:Ipv6PrefixRange;

}

}

grouping chfInfo {

//optional support

list supiRangeList {

description \"List of ranges of SUPIs that can be served by the CHF
instance. If not provided, the CHF can serve any SUPI.\";

key \"start end pattern\";

min-elements 1;

//optional support

uses SupiRange;

}

list gpsiRangeList {

description \"List of ranges of GPSI that can be served by the CHF
instance. If not provided, the CHF can serve any GPSI.\";

key \"start end pattern\";

min-elements 1;

//optional support

uses IdentityRange;

}

list plmnRangeList {

description \"List of ranges of PLMNs (including the PLMN IDs of the CHF
instance) that can be served by the CHF instance.

If not provided, the CHF can serve any PLMN.\";

min-elements 1;

//optional support

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

}

grouping nrfInfoGrp {

//optional support

list servedUdrInfo {

description \"This attribute contains all the udrInfo attributes locally
configured in the NRF or the NRF received during NF registration.\";

//optional support

key nfInstanceID;

leaf nfInstanceID {

description \"String uniquely identifying a NF instance.\";

type string;

}

min-elements 1;

uses udrInfo;

}

list servedUdmInfo {

description \"This attribute contains all the udmInfo attributes locally
configured in the NRF or the NRF received during NF registration.\";

//optional support

key nfInstanceID;

leaf nfInstanceID {

description \"String uniquely identifying a NF instance.\";

type string;

}

min-elements 1;

uses udmInfo;

}

list servedAusfInfo {

description \"This attribute contains all the ausfInfo attributes
locally configured in the NRF or the NRF received during NF
registration.\";

//optional support

key nfInstanceID;

leaf nfInstanceID {

description \"String uniquely identifying a NF instance.\";

type string;

}

min-elements 1;

uses ausfInfo;

}

list servedAmfInfo {

description \"This attribute contains all the amfInfo attributes locally
configured in the NRF or the NRF received during NF registration.\";

//optional support

key nfInstanceID;

leaf nfInstanceID {

description \"String uniquely identifying a NF instance.\";

type string;

}

min-elements 1;

uses amfInfo;

}

list servedSmfInfo {

description \"This attribute contains all the smfInfo attributes locally
configured in the NRF or the NRF received during NF registration.\";

//optional support

key nfInstanceID;

leaf nfInstanceID {

description \"String uniquely identifying a NF instance.\";

type string;

}

min-elements 1;

uses smfInfo;

}

list servedUpfInfo {

description \"This attribute contains all the upfInfo attributes locally
configured in the NRF or the NRF received during NF registration.\";

//optional support

key nfInstanceID;

leaf nfInstanceID {

description \"String uniquely identifying a NF instance.\";

type string;

}

min-elements 1;

uses upfInfo;

}

list servedPcfInfo {

description \"This attribute contains all the pcfInfo attributes locally
configured in the NRF or the NRF received during NF registration.\";

//optional support

key nfInstanceID;

leaf nfInstanceID {

description \"String uniquely identifying a NF instance.\";

type string;

}

min-elements 1;

uses pcfInfo;

}

list servedBsfInfo {

description \"This attribute contains all the bsfInfo attributes locally
configured in the NRF or the NRF received during NF registration.\";

//optional support

key nfInstanceID;

leaf nfInstanceID {

description \"String uniquely identifying a NF instance.\";

type string;

}

min-elements 1;

uses bsfInfo;

}

list servedChfInfo {

description \"This attribute contains all the bsfInfo attributes locally
configured in the NRF or the NRF received during NF registration.\";

//optional support

key nfInstanceID;

leaf nfInstanceID {

description \"String uniquely identifying a NF instance.\";

type string;

}

min-elements 1;

uses chfInfo;

}

}

list nrfInfo {

key idx; //no obvious leaf to use as a key

leaf idx { type uint32; }

max-elements 1;

uses nrfInfoGrp;

}

leaf customInfo {

description \"Specific data for custom Network Functions.\";

type string;

}

leaf recoveryTime {

description \"Timestamp when the NF was (re)started.\";

//optional support

type yang:date-and-time;

}

leaf nfServicePersistence {

description \"If present, and set to true, it indicates that the
different service instances of a same NF Service in this NF instance,

supporting a same API version, are capable to persist their resource
state in shared storage and therefore these resources

are available after a new NF service instance supporting the same API
version is selected by a NF Service Consumer (see 3GPP TS 23.527).

Otherwise, it indicates that the NF Service Instances of a same NF
Service are not capable to share resource state inside the NF
Instance.\";

//optional support

type boolean;

}

list nfServices {

description \"List of NF Service Instances. It shall include the
services produced by the NF that can be discovered by other NFs.\";

key serviceInstanceID;

//optional support

min-elements 1;

uses nfs3gpp:NFServiceGrp;

}

leaf nfProfileChangesSupportInd {

description \"NF Profile Changes Support Indicator. This IE may be
present in the NFRegister or NFUpdate (NF Profile Complete Replacement)
request and shall be absent in the response.

true: the NF Service Consumer supports receiving NF Profile Changes in
the response.

false (default): the NF Service Consumer does not support receiving NF
Profile Changes in the response.\";

//optional support

type boolean;

}

leaf nfProfileChangesInd {

description \"NF Profile Changes Indicator. This IE shall be absent in
the request to the NRF and may be included by the NRF in NFRegister or
NFUpdate (NF Profile Complete Replacement) response.

true: the NF Profile contains NF Profile changes.

false (default): complete NF Profile.\";

//optional support

type boolean;

}

list defaultNotificationSubscriptions {

description \"Notification endpoints for different notification
types.\";

key notificationType;

//optional support

min-elements 1;

uses types3gpp:DefaultNotificationSubscription;

}

}

typedef NFStatus {

type enumeration {

enum REGISTERED;

enum SUSPENDED;

}

}

typedef DataSetId {

type enumeration {

enum SUBSCRIPTION;

enum POLICY;

enum EXPOSURE;

enum APPLICATION;

}

}

grouping SupiRange {

leaf start {

description \"First value identifying the start of a SUPI range. To be
used when the range of SUPI\'s can be represented as a numeric range
(e.g., IMSI ranges).\";

type string {

pattern \'\^\[0-9\]+\$\';

}

}

leaf end {

description \"Last value identifying the end of a SUPI range. To be used
when the range of SUPI\'s can be represented as a numeric range (e.g.
IMSI ranges).\";

type string {

pattern \'\^\[0-9\]+\$\';

}

}

leaf pattern {

description \"Pattern representing the set of SUPI\'s belonging to this
range.

A SUPI value is considered part of the range if and only if the SUPI
string fully matches the regular expression.\";

type string;

}

}

grouping IdentityRange {

leaf start {

description \"First value identifying the start of an identity range. To
be used when the range of identities can be represented as a numeric
range (e.g., MSISDN ranges).\";

type string {

pattern \'\^\[0-9\]+\$\';

}

}

leaf end {

description \"Last value identifying the end of an identity range. To be
used when the range of identities can be represented as a numeric range
(e.g. MSISDN ranges).\";

type string {

pattern \'\^\[0-9\]+\$\';

}

}

leaf pattern {

description \"Pattern representing the set of identities belonging to
this range.

An identity value is considered part of the range if and only if the
identity string fully matches the regular expression.\";

type string;

}

}

grouping TacRange {

leaf start {

description \"First value identifying the start of a TAC range, to be
used when the range of TAC\'s can be represented as a hexadecimal range
(e.g., TAC ranges).\";

type string {

pattern \'\^(\[A-Fa-f0-9\]{4}\|\[A-Fa-f0-9\]{6}\$)\';

}

}

leaf end {

description \"Last value identifying the end of a TAC range, to be used
when the range of TAC\'s can be represented as a hexadecimal range (e.g.
TAC ranges).\";

type string {

pattern \'\^(\[A-Fa-f0-9\]{4}\|\[A-Fa-f0-9\]{6})\$\';

}

}

leaf pattern {

description \"Pattern representing the set of TAC\'s belonging to this
range.\";

type string;

}

}

grouping SnssaiUpfInfoItem {

list sNssai { //is the key unique

description \"Supported S-NSSAI.\";

min-elements 1;

max-elements 1;

key \"sst sd\";

uses Snssai;

}

list dnnUpfInfoList {

description \"List of parameters supported by the UPF per DNN.\";

min-elements 1;

key dnn;

uses DnnUpfInfoItem;

}

}

grouping DnnUpfInfoItem {

leaf dnn {

description \"String representing a Data Network.\";

mandatory true;

type string;

}

leaf-list dnaiList {

description \"List of Data network access identifiers supported by the
UPF for this DNN.

The absence of this attribute indicates that the UPF can be selected for
this DNN for any DNAI.\";

min-elements 1;

type string; //dnai is the type but its only a string with desc: DNAI
(Data network access identifier), is this needed as its own typedef or
string is ok

}

leaf-list pduSessionTypes {

description \"List of PDU session type(s) supported by the UPF for a
specific DNN.\";

min-elements 1;

type PduSessionType;

}

}

grouping Snssai {

leaf sst {

description \"Unsigned integer, within the range 0 to 255, representing
the Slice/Service Type.

It indicates the expected Network Slice behaviour in terms of features
and services.\";

mandatory true;

type uint32;

}

leaf sd {

description \"3-octet string, representing the Slice Differentiator, in
hexadecimal representation.\";

//optional

type string {

pattern \'\^\[A-Fa-f0-9\]{6}\$\';

}

}

reference \"3GPP TS 29.571\";

}

typedef PduSessionType {

type enumeration {

enum IPV4;

enum IPV6;

enum IPV4V6;

enum UNSTRUCTURED;

enum ETHERNET;

}

}

grouping Guami {

list plmnId {

description \"PLMN Identity.\";

min-elements 1;

max-elements 1;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

list amfId {

description \"AMF Identity.\";

min-elements 1;

max-elements 1;

key \"amfRegionId amfSetId amfPointer\";

uses types3gpp:AmfIdentifier;

}

}

grouping Tai {

list plmnId {

description \"PLMN Identity.\";

min-elements 1;

max-elements 1;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

leaf tac { type types3gpp:Tac; }

}

grouping InterfaceUpfInfoItem {

leaf interfaceType {

description \"User Plane interface type.\";

mandatory true;

type UPInterfaceType;

}

////At least one of the addressing parameters (ipv4address, ipv6adress
or endpointFqdn) shall be included in the InterfaceUpfInfoItem.

choice address {

case ipv4EndpointAddresses {

leaf-list ipv4EndpointAddresses {

description \"Available endpoint IPv4 address(es) of the User Plane
interface.\";

//conditional support

min-elements 1;

type inet:ipv4-address;

}

}

case ipv6EndpointAddresses {

leaf-list ipv6EndpointAddresses {

description \"Available endpoint IPv6 address(es) of the User Plane
interface.\";

//conditional support

min-elements 1;

type inet:ipv6-address;

}

}

case endpointFqdn {

leaf endpointFqdn {

description \"FQDN of available endpoint of the User Plane interface.\";

//conditional support

type inet:domain-name;

}

}

}

leaf networkInstance {

description \"Network Instance associated to the User Plane
interface.\";

//optional support

type string;

}

}

typedef UPInterfaceType {

type enumeration {

enum N3;

enum N6;

enum N9;

}

}

grouping TaiRange {

list plmnId {

description \"PLMN ID related to the TacRange.\";

min-elements 1;

max-elements 1;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

list tacRangeList { //is this key unique

description \"The range of the TACs.\";

min-elements 1;

key \"start end\";

uses TacRange;

}

}

typedef AccessType {

type enumeration {

enum 3GPP\_ACCESS;

enum NON\_3GPP\_ACCESS;

}

}

grouping N2InterfaceAmfInfo {

//At least one of the addressing parameters (ipv4address or ipv6adress)
shall be included.

choice address {

case ipv4EndpointAddress {

leaf-list ipv4EndpointAddress {

description \"Available AMF endpoint IPv4 address(es) for N2.\";

//conditional support

min-elements 1;

type inet:ipv4-address;

}

}

case ipv6EndpointAddress {

leaf-list ipv6EndpointAddress {

description \"Available AMF endpoint IPv6 address(es) for N2.\";

//conditional support

min-elements 1;

type inet:ipv6-address;

}

}

}

leaf amfName {

description \"AMF name.\";

type string;

}

}

grouping sNssaiSmfInfoItem {

list sNssai { //is the key unique

description \"Supported S-NSSAI.\";

min-elements 1;

max-elements 1;

key \"sst sd\";

uses Snssai;

}

list dnnSmfInfoList { //is the key unique

description \"List of parameters supported by the SMF per DNN.\";

min-elements 1;

key dnn;

uses DnnSmfInfoItem;

}

}

grouping DnnSmfInfoItem {

leaf dnn {

description \"Supported DNN.\";

mandatory true;

type string;

}

}

grouping PlmnSnssai {

list plmnId {

description \"PLMN ID for which list of supported S-NSSAI(s) is
provided.\";

min-elements 1;

max-elements 1;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

list sNssaiList { //is the key unique

description \"The specific list of S-NSSAIs supported by the given
PLMN.\";

min-elements 1;

key \"sst sd\";

uses Snssai;

}

}

}

\<CODE ENDS\>

H.5.13 module \_3gpp-5gc-nrm-nfservice.yang
-------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-nfservice {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-nfservice;

prefix nfs3gpp;

import \_3gpp-common-yang-types { prefix types3gpp; }

import ietf-yang-types { prefix yang; }

import ietf-inet-types { prefix inet; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"NF service class.\";

reference \"3GPP TS 29.510\";

revision 2020-11-05 { reference CR-0411 ; }

revision 2019-06-17 { reference \"initial revision\"; }

grouping NFServiceGrp {

description \"Represents the NFService IOC\";

leaf serviceInstanceID {

description

\"Unique ID of the service instance within a given NF Instance.\";

mandatory true;

type string;

}

leaf serviceName {

description \"Name of the service instance (e.g. \'nudm-sdm\').\";

mandatory true;

type ServiceName;

}

list versions { //check in review if key is ok (unique)

description \"API versions supported by the NF Service and if available,

the corresponding retirement date of the NF Service.\";

min-elements 1;

key \"apiVersionInUri apiFullVersion\";

uses NFServiceVersion;

}

leaf scheme {

description \"URI scheme (e.g. \'http\', \'https\').\";

mandatory true;

type UriScheme;

}

leaf nfServiceStatus {

description \"Status of the NF Service Instance.\";

mandatory true;

type NFServiceStatus;

}

leaf fqdn {

description \"FQDN of the NF Service Instance.\";

//optional support

type inet:domain-name;

}

leaf interPlmnFqdn {

description \"If the NF service needs to be discoverable by other NFs in
a

different PLMN, then an FQDN that is used for inter PLMN routing.\";

//optional support

type inet:domain-name;

}

list ipEndPoints {

description \"IP address(es) and port information of the Network
Function

(including IPv4 and/or IPv6 address) where the service is listening

for incoming service requests.\";

//optional support

key idx;

leaf idx {

type string;

}

min-elements 1;

uses ipEndPoint;

}

leaf apiPrefix {

description \"Optional path segment(s) used to construct the {apiRoot}

variable of the different API URIs.\";

//optional support

type string;

}

list defaultNotificationSubscriptions {

description \"Notification endpoints for different notification
types.\";

key notificationType;

//optional support

min-elements 1;

uses types3gpp:DefaultNotificationSubscription;

}

list allowedPlmns {

description \"PLMNs allowed to access the service instance.

The absence of this attribute indicates that any PLMN is allowed to

access the service instance.\";

min-elements 1;

//optional support

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

leaf-list allowedNfTypes {

description \"Type of the NFs allowed to access the service instance.

The absence of this attribute indicates that any NF type is allowed

to access the service instance.\";

min-elements 1;

//optional support

type types3gpp:NfType;

}

leaf-list allowedNfDomains {

description \"Pattern representing the NF domain names allowed to

access the service instance.\";

//optional support

min-elements 1;

type string;

}

list allowedNssais {

description \"S-NSSAI of the allowed slices to access the service
instance.

The absence of this attribute indicates that any slice is allowed to

access the service instance.\";

min-elements 1;

//optional support

key \"sd sst\";

uses types5g3gpp:SNssai; }

leaf priority {

description \"Priority (relative to other services of the same type)

in the range of 0-65535, to be used for NF Service selection; lower

values indicate a higher priority.\";

//optional support

type uint16;

}

leaf capacity {

description \"Static capacity information in the range of 0-65535,

expressed as a weight relative to other services of the same type.\";

//optional support

type uint16;

}

leaf load {

description \"Dynamic load information, ranged from 0 to 100,

indicates the current load percentage of the NF Service.\";

//optional support

type types3gpp:Load;

}

leaf recoveryTime {

description \"Timestamp when the NF was (re)started.\";

//optional support

type yang:date-and-time;

}

list chfServiceInfo { //is the key unique

description \"Specific data for a CHF service instance.\";

//optional support

max-elements 1;

key \"primaryChfServiceInstance secondaryChfServiceInstance\";

uses ChfServiceInfo;

}

leaf supportedFeatures {

description \"Supported Features of the NF Service instance.\";

//optional support

type SupportedFeatures;

}

}

typedef SupportedFeatures {

type string {

pattern \'\[A-Fa-f0-9\]\*\';

}

}

grouping ipEndPoint {

choice address {

leaf ipv4Address {

type inet:ipv4-address;

}

leaf ipv6Address {

type inet:ipv6-address;

}

leaf ipv6Prefix {

type inet:ipv6-prefix;

}

}

leaf transport {

type TransportProtocol;

}

leaf port {

type uint16;

}

}

typedef TransportProtocol {

type enumeration {

enum TCP;

enum STCP;

enum UDP;

}

}

grouping NFServiceVersion {

leaf apiVersionInUri {

mandatory true;

type string;

}

leaf apiFullVersion {

mandatory true;

type string;

}

leaf expiry {

//optional to support

type yang:date-and-time;

}

}

typedef ServiceName {

type enumeration {

enum NNRF\_NFM;

enum NNRF\_DISC;

enum NUDM\_SDM;

enum NUDM\_UECM;

enum NUDM\_UEAU;

enum NUDM\_EE;

enum NUDM\_PP;

enum NAMF\_COMM;

enum NAMF\_EVTS;

enum NAMF\_MT;

enum NAMF\_LOC;

enum NSMF\_PDUSESSION;

enum NSMF\_EVENT-EXPOSURE;

enum NAUSF\_AUTH;

enum NAUSF\_SORPROTECTION;

enum NNEF\_PFDMANAGEMENT;

enum NPCF\_AM-POLICY-CONTROL;

enum NPCF\_SMPOLICYCONTROL;

enum NPCF\_POLICYAUTHORIZATION;

enum NPCF\_BDTPOLICYCONTROL;

enum NPCF\_EVENTEXPOSURE;

enum NPCF\_UE\_POLICY\_CONTROL;

enum NSMSF\_SMS;

enum NNSSF\_NSSELECTION;

enum NNSSF\_NSSAIAVAILABILITY;

enum NUDR\_DR;

enum NLMF\_LOC;

enum N5G\_EIR\_EIC;

enum NBSF\_MANAGEMENT;

enum NCHF\_SPENDINGLIMITCONTROL;

enum NCHF\_CONVERGEDCHARGING;

enum NNWDAF\_EVENTSSUBSCRIPTION;

enum NNWDAF\_ANALYTICSINFO;

}

}

typedef UriScheme {

type enumeration {

enum HTTP;

enum HTTPS;

}

}

typedef NFServiceStatus {

type enumeration {

enum REGISTERED;

enum SUSPENDED;

enum UNDISCOVERABLE;

}

}

grouping ChfServiceInfo {

leaf primaryChfServiceInstance {

description \"Shall be present if the CHF service instance serves as a

secondary CHF instance of another primary CHF service instance.\";

//conditional to support

type string;

}

leaf secondaryChfServiceInstance {

description \"Shall be present if the CHF service instance serves as a

primary CHF instance of another secondary CHF service instance.\";

//conditional to support

type string;

}

}

}

\<CODE ENDS\>

H.5.14 module \_3gpp-5gc-nrm-ngeirfunction.yang
-----------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-ngeirfunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-ngeirfunction;

prefix ngeir3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"This IOC represents the 5G-EIR function in 5GC. For more

information about the 5G-EIR, see 3GPP TS 23.501.\";

reference \"3GPP TS 28.541\";

revision 2020-11-05 { reference CR-0411 ; }

revision 2019-10-25 { reference \"S5-194457 S5-195427 S5-193518\"; }

revision 2019-05-15 {reference \"initial revision\"; }

grouping NGEIRFunctionGrp {

description \"Represents the NGEIRFunction IOC\";

uses mf3gpp:ManagedFunctionGrp;

list pLMNIdList {

description \"List of at most six entries of PLMN Identifiers, but at

least one (the primary PLMN Id).

The PLMN Identifier is composed of a Mobile Country Code (MCC) and

a Mobile Network Code (MNC).\";

min-elements 1;

max-elements 6;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

list sNSSAIList {

description \"List of S-NSSAIs the managed object is capable of
supporting.

(Single Network Slice Selection Assistance Information)

An S-NSSAI has an SST (Slice/Service type) and an optional SD

(Slice Differentiator) field.\";

//optional support

reference \"3GPP TS 23.003\";

key \"sd sst\";

uses types5g3gpp:SNssai;

}

list managedNFProfile {

key idx;

min-elements 1;

max-elements 1;

uses types3gpp:ManagedNFProfile;

}

list commModelList {

min-elements 1;

key \"groupId\";

description \"Specifies a list of commModel. It can be used by NF and

NF services to interact with each other in 5G Core network \";

reference \"3GPP TS 23.501\";

uses types5g3gpp:CommModel;

}

}

augment \"/me3gpp:ManagedElement\" {

list NGEIRFunction {

description \"5G Core NGEIR Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses NGEIRFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

H.5.15 module \_3gpp-5gc-nrm-nrffunction.yang
---------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-nrffunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-nrffunction;

prefix nrf3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import ietf-inet-types { prefix inet; }

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-5gc-nrm-nfprofile { prefix nfp3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"This IOC represents the NRF function in 5GC.

For more information about the NRF, see 3GPP TS 23.501 \[2\].\";

reference \"3GPP TS 28.541\";

revision 2020-11-05 { reference CR-0411 ; }

revision 2020-08-03 { reference \"CR-0321\"; }

revision 2019-10-28 { reference S5-193518 ; }

revision 2019-05-15 { reference \"initial revision\"; }

grouping NRFFunctionGrp {

description \"Represents the NRFFunction IOC\";

uses mf3gpp:ManagedFunctionGrp;

list pLMNIdList {

description \"List of at most six entries of PLMN Identifiers, but at

least one (the primary PLMN Id).

The PLMN Identifier is composed of a Mobile Country Code (MCC) and a

Mobile Network Code (MNC).\";

min-elements 1;

max-elements 6;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

leaf sBIFQDN {

description \"The FQDN of the registered NF instance in the
service-based

interface.\";

type inet:domain-name;

}

leaf-list cNSIIdList {

description \"NSI ID. NSI ID is an identifier for identifying the Core

Network part of a Network Slice instance when multiple Network Slice

instances of the same Network Slice are deployed, and there is a need

to differentiate between them in the 5GC, see clause 3.1 of TS 23.501

and subclause 6.1.6.2.7 of 3GPP TS 29.531\";

type string;

}

list sNSSAIList {

description \"List of S-NSSAIs the managed object is capable of
supporting.

(Single Network Slice Selection Assistance Information)

An S-NSSAI has an SST (Slice/Service type) and an optional SD

(Slice Differentiator) field.\";

//optional support

reference \"3GPP TS 23.003\";

key \"sd sst\";

uses types5g3gpp:SNssai;

}

list nFProfileList {

description \"Set of NFProfile(s) to be registered in the NRF
instance.\";

//optional support

key nfInstanceID;

uses nfp3gpp:NFProfileGrp;

}

}

augment \"/me3gpp:ManagedElement\" {

list NRFFunction {

description \"5G Core NRF Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses NRFFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

H.5.16 module \_3gpp-5gc-nrm-nssffunction.yang
----------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-nssffunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-nssffunction;

prefix nssf3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import ietf-inet-types { prefix inet; }

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"This IOC represents the NSSF function in 5GC. For more

information about the NSSF, see 3GPP TS 23.501.\";

reference \"3GPP TS 28.541\";

revision 2020-11-05 { reference CR-0411 ; }

revision 2020-08-03 { reference \"CR-0321\"; }

revision 2019-10-25 { reference \"S5-194457 S5-195427 S5-193518\"; }

revision 2019-05-15 { reference \"initial revision\"; }

grouping NSSFFunctionGrp {

description \"Represents the NSSFFunction IOC\";

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

leaf sBIFQDN {

description \"The FQDN of the registered NF instance in the
service-based

interface.\";

type inet:domain-name;

}

list sNSSAIList {

description \"List of S-NSSAIs the managed object is capable of
supporting.

(Single Network Slice Selection Assistance Information)

An S-NSSAI has an SST (Slice/Service type) and an optional SD

(Slice Differentiator) field.\";

reference \"3GPP TS 23.003\";

key \"sd sst\";

uses types5g3gpp:SNssai;

}

leaf-list cNSIIdList {

description \"NSI ID. NSI ID is an identifier for identifying the Core

Network part of a Network Slice instance when multiple Network Slice

instances of the same Network Slice are deployed, and there is a need

to differentiate between them in the 5GC, see clause 3.1 of TS 23.501

and subclause 6.1.6.2.7 of 3GPP TS 29.531\";

type string;

}

list managedNFProfile {

key idx;

min-elements 1;

max-elements 1;

uses types3gpp:ManagedNFProfile;

}

}

augment \"/me3gpp:ManagedElement\" {

list NSSFFunction {

description \"5G Core NSSF Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses NSSFFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

H.5.17 module \_3gpp-5gc-nrm-nwdaffunction.yang
-----------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-nwdaffunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-nwdaffunction;

prefix nwdaf3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import ietf-inet-types { prefix inet; }

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"This IOC represents the NWDAF function in 5GC. For more

information about the NWDAF, see 3GPP TS 23.501.\";

reference \"3GPP TS 28.541\";

revision 2020-11-05 { reference CR-0411 ; }

revision 2019-10-25 { reference \"S5-194457 S5-195427 S5-193518\"; }

revision 2019-05-15 {reference \"initial revision\"; }

grouping NWDAFFunctionGrp {

description \"Represents the NWDAFFunction IOC\";

uses mf3gpp:ManagedFunctionGrp;

list pLMNIdList {

description \"List of at most six entries of PLMN Identifiers, but at

least one (the primary PLMN Id).

The PLMN Identifier is composed of a Mobile Country Code (MCC) and a

Mobile Network Code (MNC).\";

min-elements 1;

max-elements 6;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

leaf sBIFQDN {

description \"The FQDN of the registered NF instance in the
service-based

interface.\";

type inet:domain-name;

}

list sNSSAIList {

description \"List of S-NSSAIs the managed object is capable of
supporting.

(Single Network Slice Selection Assistance Information)

An S-NSSAI has an SST (Slice/Service type) and an optional SD

(Slice Differentiator) field.\";

//optional support

reference \"3GPP TS 23.003\";

key \"sd sst\";

uses types5g3gpp:SNssai;

}

list managedNFProfile {

key idx;

min-elements 1;

max-elements 1;

uses types3gpp:ManagedNFProfile;

}

list commModelList {

min-elements 1;

key \"groupId\";

description \"Specifies a list of commModel. It can be used by NF and

NF services to interact with each other in 5G Core network \";

reference \"3GPP TS 23.501\";

uses types5g3gpp:CommModel;

}

}

augment \"/me3gpp:ManagedElement\" {

list NWDAFFunction {

description \"5G Core NWDAF Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses NWDAFFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

H.5.18 module \_3gpp-5gc-nrm-pcffunction.yang
---------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-pcffunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-pcffunction;

prefix pcf3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import ietf-inet-types { prefix inet; }

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"This IOC represents the PCF function in 5GC. For more

information about the PCF, see 3GPP TS 23.501.\";

reference \"3GPP TS 28.541\";

revision 2020-11-05 { reference CR-0411 ; }

revision 2020-08-06 { reference \"CR-0333\"; }

revision 2020-08-06 { reference \"CR-0331\"; }

revision 2019-10-25 { reference \"S5-194457 S5-193518\"; }

revision 2019-05-22 { reference \"initial revision\"; }

grouping PCFFuntionGrp {

description \"Represents the PCFFuntion IOC\";

uses mf3gpp:ManagedFunctionGrp;

list pLMNIdList {

description \"List of at most six entries of PLMN Identifiers, but at

least one (the primary PLMN Id).

The PLMN Identifier is composed of a Mobile Country Code (MCC) and a

Mobile Network Code (MNC).\";

min-elements 1;

max-elements 6;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

leaf sBIFQDN {

description \"The FQDN of the registered NF instance in the
service-based

interface.\";

type inet:domain-name;

}

list sNSSAIList {

description \"List of S-NSSAIs the managed object is capable of
supporting.

(Single Network Slice Selection Assistance Information)

An S-NSSAI has an SST (Slice/Service type) and an optional SD

(Slice Differentiator) field.\";

//optional support

reference \"3GPP TS 23.003\";

key \"sd sst\";

uses types5g3gpp:SNssai;

}

list managedNFProfile {

key idx;

min-elements 1;

max-elements 1;

uses types3gpp:ManagedNFProfile;

}

list commModelList {

min-elements 1;

key \"groupId\";

description \"Specifies a list of commModel. It can be used by NF and

NF services to interact with each other in 5G Core network \";

reference \"3GPP TS 23.501\";

uses types5g3gpp:CommModel;

}

leaf dynamic5QISetRef {

type types3gpp:DistinguishedName;

description \"DN of the Dynamic5QISet that the PCFFunction supports

(is associated to).\";

}

leaf configurable5QISetRef {

type types3gpp:DistinguishedName;

description \"DN of the Configurable5QISet that the PCFFunction supports

(is associated to).\";

}

}

augment \"/me3gpp:ManagedElement\" {

list PCFFunction {

description \"5G Core PCF Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses PCFFuntionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

H.5.19 module \_3gpp-5gc-nrm-seppfunction.yang
----------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-seppfunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-seppfunction;

prefix sepp3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import ietf-inet-types { prefix inet; }

organization \"3gpp SA5\";

description \"This IOC represents the SEPP function which support
message filtering

and policing on inter-PLMN control plane interface. For more information
about the SEPP, see 3GPP TS 23.501.\";

reference \"3GPP TS 28.541\";

revision 2020-08-03 { reference \"CR-0321\"; }

revision 2019-10-28 { reference S5-193518 ; }

typedef SEPPType {

reference \"3GPP TS 23501\";

type enumeration {

enum CSEPP {

value 0;

description \"consumer SEPP\";

}

enum PSEPP {

value 1;

description \"producer SEPP\";

}

}

}

grouping SEPPFunctionGrp {

uses mf3gpp:ManagedFunctionGrp;

container pLMNId {

description \"PLMN Identifiers of the sepp.

The PLMN Identifier is composed of a Mobile Country Code (MCC) and a
Mobile Network Code (MNC).\";

uses types3gpp:PLMNId;

}

leaf sEPPType {

type sepp3gpp:SEPPType;

}

leaf sEPPId {

type uint16;

}

leaf fqdn {

description \"The domain name of the SEPP.\";

type inet:domain-name;

}

}

augment \"/me3gpp:ManagedElement\" {

list SEPPFunction {

description \"5G Core SEPP Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses SEPPFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses; }

}

}

\<CODE ENDS\>

H.5.19a module \_3gpp-5gc-nrm- externalseppfunction.yang
--------------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-externalseppfunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-extternalseppfunction;

prefix extsepp3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import ietf-inet-types { prefix inet; }

organization \"3gpp SA5\";

description \"This IOC represents the external SEPP function which
support message filtering

and policing on inter-PLMN control plane interface. For more information
about the SEPP, see 3GPP TS 23.501.\";

reference \"3GPP TS 28.541\";

revision 2019-11-17 {

description \"initial revision\";

reference \"Based on

3GPP TS 28.541\";

}

grouping ExternalSEPPFunctionGrp {

uses mf3gpp:ManagedFunctionGrp;

container pLMNId {

description \"PLMN Identifiers of the sepp.

The PLMN Identifier is composed of a Mobile Country Code (MCC) and a
Mobile Network Code (MNC).\";

uses types3gpp:PLMNId;

}

leaf sEPPId {

type uint16;

}

leaf fqdn {

description \"The domain name of the SEPP.\";

type inet:domain-name;

}

}

augment \"/me3gpp:ManagedElement\" {

list ExternalSEPPFunction {

description \"5G Core SEPP Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses ExternalSEPPFunctionGrp;

}

}

}

}

\<CODE ENDS\>

H.5.20 module \_3gpp-5gc-nrm-smffunction
----------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-smffunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-smffunction;

prefix smf3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

import ietf-inet-types { prefix inet; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"SMFFunction derived from basic ManagedFunction.\";

revision 2020-11-05 { reference CR-0411 ; }

revision 2020-08-06 { reference \"CR-0333\"; }

revision 2020-06-03 { reference \"CR-0286\"; }

revision 2019-10-25 { reference \"S5-194457 S5-193518\"; }

revision 2019-05-31 {reference \"Ericsson refactoring.\"; }

revision 2018-08-07 { reference \"Initial revision\";}

grouping SMFFunctionGrp {

description \"Represents the SMFFuntion IOC\";

uses mf3gpp:ManagedFunctionGrp;

list pLMNIdList {

min-elements 1;

description \"A list of PLMN identifiers (Mobile Country Code and Mobile

Network Code).\";

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

leaf-list nRTACList {

description \"List of Tracking Area Codes (legacy TAC or extended TAC)

where the represented management function is serving.\";

reference \"TS 38.413 clause 9.3.3.10\";

min-elements 1;

config false;

type types3gpp:Tac;

}

leaf sBIFQDN {

description \"The FQDN of the registered NF instance in the
service-based

interface.\";

type inet:domain-name;

}

list sNSSAIList {

description \"List of S-NSSAIs the managed object is capable of
supporting.

(Single Network Slice Selection Assistance Information)

An S-NSSAI has an SST (Slice/Service type) and an optional SD

(Slice Differentiator) field.\";

reference \"3GPP TS 23.003\";

key \"sd sst\";

uses types5g3gpp:SNssai;

}

list managedNFProfile {

key idx;

min-elements 1;

max-elements 1;

uses types3gpp:ManagedNFProfile;

}

list commModelList {

min-elements 1;

key \"groupId\";

description \"Specifies a list of commModel. It can be used by NF and

NF services to interact with each other in 5G Core network \";

reference \"3GPP TS 23.501\";

uses types5g3gpp:CommModel;

}

leaf configurable5QISetRef {

type types3gpp:DistinguishedName;

description \"DN of the Configurable5QISet that the SMFFunction supports

(is associated to).\";

}

leaf dynamic5QISetRef {

type types3gpp:DistinguishedName;

description \"DN of the Dynamic5QISet that the SMFFunction supports

(is associated to).\";

}

}

augment \"/me3gpp:ManagedElement\" {

list SMFFunction {

description \"5G Core SMF Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses SMFFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

H.5.21 module \_3gpp-5gc-nrm-smsffunction.yang
----------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-smsffunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-smsffunction;

prefix smsf3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3gpp SA5\";

description \"This IOC represents the SMSF function defined in 3GPP TS
23.501.\";

reference \"3GPP TS 28.541\";

revision 2019-10-25 { reference \"S5-194457 S5-195427 S5-193518\"; }

revision 2019-05-15 {

description \"initial revision\";

}

grouping SMSFFunctionGrp {

uses mf3gpp:ManagedFunctionGrp;

list pLMNIdList {

description \"List of at most six entries of PLMN Identifiers, but at
least one (the primary PLMN Id).

The PLMN Identifier is composed of a Mobile Country Code (MCC) and a
Mobile Network Code (MNC).\";

min-elements 1;

max-elements 6;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

list managedNFProfile {

key idx;

min-elements 1;

uses types3gpp:ManagedNFProfile;

}

list commModelList {

min-elements 1;

key \"groupId\";

uses types5g3gpp:CommModel;

}

}

augment \"/me3gpp:ManagedElement\" {

list SMSFFunction {

description \"5G Core SMSF Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses SMSFFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

H.5.22 module \_3gpp-5gc-nrm-udmfunction.yang
---------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-udmfunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-udmfunction;

prefix udm3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import ietf-inet-types { prefix inet; }

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"This IOC represents the UDM function in 5GC. For more

information about the UDM, see 3GPP TS 23.501.\";

reference \"3GPP TS 28.541\";

revision 2020-11-05 { reference CR-0411 ; }

revision 2019-10-25 { reference \"S5-194457 S5-195427 S5-193518\"; }

revision 2019-05-22 { reference \"initial revision\";}

grouping UDMFuntionGrp {

description \"Represents the UDMFuntion IOC\";

uses mf3gpp:ManagedFunctionGrp;

list pLMNIdList {

description \"List of at most six entries of PLMN Identifiers, but at

least one (the primary PLMN Id).

The PLMN Identifier is composed of a Mobile Country Code (MCC) and a

Mobile Network Code (MNC).\";

min-elements 1;

max-elements 6;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

leaf sBIFQDN {

description \"The FQDN of the registered NF instance in the
service-based

interface.\";

type inet:domain-name;

}

list sNSSAIList {

description \"List of S-NSSAIs the managed object is capable of
supporting.

(Single Network Slice Selection Assistance Information)

An S-NSSAI has an SST (Slice/Service type) and an optional SD

(Slice Differentiator) field.\";

//optional support

reference \"3GPP TS 23.003\";

key \"sd sst\";

uses types5g3gpp:SNssai;

}

list managedNFProfile {

key idx;

min-elements 1;

max-elements 1;

uses types3gpp:ManagedNFProfile;

}

list commModelList {

min-elements 1;

key \"groupId\";

description \"Specifies a list of commModel. It can be used by NF and

NF services to interact with each other in 5G Core network \";

reference \"3GPP TS 23.501\";

uses types5g3gpp:CommModel;

}

}

augment \"/me3gpp:ManagedElement\" {

list UDMFunction {

description \"5G Core UDM Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses UDMFuntionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

H.5.23 module \_3gpp-5gc-nrm-udrfunction.yang
---------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-udrfunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-udrfunction;

prefix udr3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import ietf-inet-types { prefix inet; }

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"This IOC represents the UDR function in 5GC. For more
information

about the UDR, see 3GPP TS 23.501.\";

reference \"3GPP TS 28.541\";

revision 2020-11-05 { reference CR-0411 ; }

revision 2019-10-25 { reference \"S5-194457 S5-195427 S5-193518\"; }

revision 2019-05-22 { reference \"initial revision\"; }

grouping UDRFuntionGrp {

description \"Represents the UDRFuntion IOC\";

uses mf3gpp:ManagedFunctionGrp;

list pLMNIdList {

description \"List of at most six entries of PLMN Identifiers, but at

least one (the primary PLMN Id).

The PLMN Identifier is composed of a Mobile Country Code (MCC) and a

Mobile Network Code (MNC).\";

min-elements 1;

max-elements 6;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

leaf sBIFQDN {

description \"The FQDN of the registered NF instance in the
service-based

interface.\";

type inet:domain-name;

}

list sNSSAIList {

description \"List of S-NSSAIs the managed object is capable of
supporting.

(Single Network Slice Selection Assistance Information)

An S-NSSAI has an SST (Slice/Service type) and an optional SD

(Slice Differentiator) field.\";

//optional support

reference \"3GPP TS 23.003\";

key \"sd sst\";

uses types5g3gpp:SNssai;

}

list managedNFProfile {

key idx;

min-elements 1;

max-elements 1;

uses types3gpp:ManagedNFProfile;

}

}

augment \"/me3gpp:ManagedElement\" {

list UDRFunction {

description \"5G Core UDR Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses UDRFuntionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

H.5.24 module \_3gpp-5gc-nrm-udsffunction.yang
----------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-udsffunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-udsffunction;

prefix udsf3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import ietf-inet-types { prefix inet; }

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"This IOC represents the UDSF function which can be
interacted

with any other 5GC NF defined in 3GPP TS 23.501.\";

reference \"3GPP TS 28.541\";

revision 2020-11-05 { reference CR-0411 ; }

revision 2019-10-25 { reference \"S5-194457 S5-195427 S5-193518\"; }

revision 2019-05-22 { reference \"initial revision\"; }

grouping UDSFFuntionGrp {

description \"Represents the UDSFFuntion IOC\";

uses mf3gpp:ManagedFunctionGrp;

list pLMNIdList {

description \"List of at most six entries of PLMN Identifiers, but at

least one (the primary PLMN Id).

The PLMN Identifier is composed of a Mobile Country Code (MCC) and a

Mobile Network Code (MNC).\";

min-elements 1;

max-elements 6;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

leaf sBIFQDN {

description \"The FQDN of the registered NF instance in the

service-based interface.\";

type inet:domain-name;

}

list sNSSAIList {

description \"List of S-NSSAIs the managed object is capable of
supporting.

(Single Network Slice Selection Assistance Information)

An S-NSSAI has an SST (Slice/Service type) and an optional SD

(Slice Differentiator) field.\";

//optional support

reference \"3GPP TS 23.003\";

key \"sd sst\";

uses types5g3gpp:SNssai;

}

list managedNFProfile {

key idx;

min-elements 1;

max-elements 1;

description \"Managed Network Function profile\";

reference \"3GPP TS 23.501\";

uses types3gpp:ManagedNFProfile;

}

}

augment \"/me3gpp:ManagedElement\" {

list UDSFFunction {

description \"5G Core UDSF Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses UDSFFuntionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses; }

}

}

\<CODE ENDS\>

H.5.25 module \_3gpp-5gc-nrm-upffunction.yang
---------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-upffunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-upffunction;

prefix upf3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-yang-types { prefix types3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3GPP SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"UPFFunction derived from basic ManagedFunction.\";

reference \"3GPP TS 28.541 5G Network Resource Model (NRM)\";

revision 2020-11-05 { reference CR-0411 ; }

revision 2019-10-25 { reference \"S5-194457 S5-193518\"; }

revision 2019-05-31 { reference \"Ericsson refactoring.\"; }

revision 2018-08-07 { reference \"Initial revision\"; }

grouping UPFFunctionGrp {

description \"Represents the UPFFunction IOC\";

uses mf3gpp:ManagedFunctionGrp;

list pLMNIdList {

description \"A list of PLMN identifiers (Mobile Country Code and Mobile

Network Code).\";

min-elements 1;

key \"mcc mnc\";

uses types3gpp:PLMNId;

}

leaf-list nRTACList {

description \"List of Tracking Area Codes (legacy TAC or extended TAC)

where the represented management function is serving.\";

reference \"TS 38.413 clause 9.3.3.10\";

min-elements 1;

config false;

type types3gpp:Tac;

}

list sNSSAIList {

description \"List of S-NSSAIs the managed object is capable of
supporting.

(Single Network Slice Selection Assistance Information)

An S-NSSAI has an SST (Slice/Service type) and an optional SD

(Slice Differentiator) field.\";

reference \"3GPP TS 23.003\";

key \"sd sst\";

uses types5g3gpp:SNssai;

}

list managedNFProfile {

key idx;

min-elements 1;

max-elements 1;

reference \"3GPP TS 23.003\";

uses types3gpp:ManagedNFProfile;

}

leaf-list supportedBMOList {

type string;

description \"List of supported BMOs (Bridge Managed Objects) required

for integration with TSN system.\";

}

}

augment /me3gpp:ManagedElement {

list UPFFunction {

description \"5G Core UPF Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses UPFFunctionGrp;

}

uses mf3gpp:ManagedFunctionContainedClasses;

}

}

}

\<CODE ENDS\>

H.5.26 module \_3gpp-5gc-nrm-scpfunction.yang
---------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-scpfunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-scpfunction;

prefix scp3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import ietf-inet-types { prefix inet; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3gpp SA5\";

description \"This IOC represents the SCP function in 5GC. For more
information about the SCP, see 3GPP TS 23.501.\";

reference \"3GPP TS 28.541\";

revision 2019-10-20 {

description \"initial revision\";

reference \"Based on

3GPP TS 28.541\";

}

grouping SCPFunctionGrp {

uses mf3gpp:ManagedFunctionGrp;

leaf address {

description \"The host address of the SCP.\";

type inet:host;

}

list supportedFuncList {

min-elements 1;

key \"function\";

uses types5g3gpp:SupportedFunc;

}

}

augment \"/me3gpp:ManagedElement\" {

list SCPFunction {

description \"5G Core SCP Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses SCPFunctionGrp;

}

}

}

}

\<CODE ENDS\>

H.5.27 module \_3gpp-5gc-nrm-neffunction.yang
---------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-neffunction {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-neffunction;

prefix nef3gpp;

import \_3gpp-common-managed-function { prefix mf3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import ietf-inet-types { prefix inet; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"This IOC represents the NEF function in 5GC. For more

information about the NEF, see 3GPP TS 23.501.\";

reference \"3GPP TS 28.541\";

revision 2020-11-05 { reference CR-0411 ; }

revision 2019-10-20 { reference \"initial revision\"; }

grouping NEFFunctionGrp {

description \"Represents the NEFFunction IOC\";

uses mf3gpp:ManagedFunctionGrp;

leaf sBIFQDN {

description \"The FQDN of the registered NF instance in the

service-based interface.\";

type inet:domain-name;

}

list sNSSAIList {

description \"List of S-NSSAIs the managed object is capable of
supporting.

(Single Network Slice Selection Assistance Information)

An S-NSSAI has an SST (Slice/Service type) and an optional SD

(Slice Differentiator) field.\";

key \"sd sst\";

uses types5g3gpp:SNssai;

}

leaf-list capabilityList {

description \"List of supported capabilities of the NEF.\";

reference \"3GPP TS 23.003\";

type string;

}

leaf isCAPIFSup {

type boolean;

}

}

augment \"/me3gpp:ManagedElement\" {

list NEFFunction {

description \"5G Core NEF Function\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses NEFFunctionGrp;

}

}

}

}

\<CODE ENDS\>

H.5.28 module \_3gpp-5gc-nrm-QFQoSMonitoringControl.yang
--------------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-QFQoSMonitoringControl {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-QFQoSMonitoringControl;

prefix qFQMCtrl3gpp;

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-5gc-nrm-smffunction { prefix smf3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"This IOC represents the capabilities and properties for
control

of QoS monitoring per QoS flow per UE for URLLC service defined

> in 3GPP TS 23.501.\";

reference \"3GPP TS 28.541\";

revision 2020-11-05 { reference CR-0411 ; }

revision 2020-08-03 { reference \"CR-0321\"; }

revision 2020-04-10 { reference \"S5-202101\"; }

grouping QFPacketDelayThresholdsTypeGrp {

description \"Represents the QFPacketDelayThresholdsType\";

leaf thresholdDl {

type uint32;

units milliseconds;

description \"Downlink threshold\";

}

leaf thresholdUl {

type uint32;

units milliseconds;

description \"Uplink threshold\";

}

leaf thresholdRtt {

type uint32;

units milliseconds;

description \"Round trip threshold\";

}

}

grouping QFQoSMonitoringControlGrp {

description \"Represents the QFQoSMonitoringControl IOC.\";

reference \"3GPP TS 28.541\";

leaf qFQoSMonitoringState {

description \"The state of QoS monitoring per QoS flow per UE.\";

mandatory true;

type enumeration {

enum ENABLED;

enum DISABLED;

}

}

list qFMonitoredSNSSAIs {

description \"The S-NSSAIs for which the QoS monitoring per QoS flow

per UE is to be performed.\";

reference \"3GPP TS 23.003\";

key \"sd sst\";

uses types5g3gpp:SNssai;

}

leaf-list qFMonitored5QIs {

description \"The 5QIs for which the QoS monitoring per QoS flow

per UE is to be performed.\";

reference \"3GPP TS 23.501\";

type uint32 {

range \"0..255\";

}

}

leaf isEventTriggeredQFMonitoringSupported {

description \"It indicates whether the event based QoS monitoring

reporting per QoS flow per UE is supported.\";

mandatory true;

reference \"3GPP TS 29.244\";

type boolean;

}

leaf isPeriodicQFMonitoringSupported {

description \"It indicates whether the periodic QoS monitoring reporting

per QoS flow per UE is supported.\";

mandatory true;

reference \"3GPP TS 29.244\";

type boolean;

}

leaf isSessionReleasedQFMonitoringSupported {

description \"It indicates whether the session release based QoS
monitoring

reporting per QoS flow per UE is supported.\";

mandatory true;

reference \"3GPP TS 29.244\";

type boolean;

}

list qFPacketDelayThresholds {

key \"idx\";

min-elements 1;

max-elements 1;

description \"It specifies the thresholds for reporting the packet delay

between PSA and UE for QoS monitoring per QoS flow per UE.\";

leaf idx { type uint32 ; }

uses QFPacketDelayThresholdsTypeGrp;

}

leaf qFMinimumWaitTime {

description \"It specifies the minimum waiting time (in seconds) between

two consecutive reports for event triggered QoS monitoring reporting

per QoS flow per UE.\";

type uint32;

}

leaf qFMeasurementPeriod {

description \"It specifies the period (in seconds) for reporting the

packet delay for QoS monitoring per QoS flow per UE.\";

type uint32;

}

}

augment \"/me3gpp:ManagedElement/smf3gpp:SMFFunction\" {

list QFQoSMonitoringControl {

description \"Represents the QFQoSMonitoringControl IOC.\";

reference \"3GPP TS 28.541\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses QFQoSMonitoringControlGrp;

}

}

}

}

\<CODE ENDS\>

H.5.29 module \_3gpp-5gc-nrm-GtpUPathQoSMonitoringControl.yang
--------------------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-GtpUPathQoSMonitoringControl {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-GtpUPathQoSMonitoringControl;

prefix gupqmc3gpp;

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-5g-common-yang-types { prefix types5g3gpp; }

import \_3gpp-5gc-nrm-smffunction { prefix smf3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"This IOC represents the capabilities and properties for
control

of GTP-U path QoS monitoring defined in 3GPP TS 23.501.\";

reference \"3GPP TS 28.541\";

revision 2021-01-25 { reference CR-0453; }

revision 2020-11-05 { reference CR-0411 ; }

revision 2020-09-30 { reference \"CR-0377\"; }

revision 2020-08-03 { reference \"CR-0321\"; }

revision 2020-04-10 { reference \"S5-202103\"; }

grouping GtpUPathDelayThresholdsType {

description \"Thresholds for reporting the packet delay for GTP-U path
QoS

monitoring \";

reference \"3GPP TS 29.244\";

leaf n3AveragePacketDelayThreshold {

mandatory true;

type uint32;

}

leaf n3MinPacketDelayThreshold {

mandatory true;

type uint32;

}

leaf n3MaxPacketDelayThreshold {

mandatory true;

type uint32;

}

leaf n9AveragePacketDelayThreshold {

mandatory true;

type uint32;

}

leaf n9MinPacketDelayThreshold {

mandatory true;

type uint32;

}

leaf n9MaxPacketDelayThreshold {

mandatory true;

type uint32;

}

}

grouping GtpUPathQoSMonitoringControlGrp {

description \"Represents the GtpUPathQoSMonitoringControl IOC.\";

leaf gtpUPathQoSMonitoringState {

description \"The state of GTP-U path QoS monitoring.\";

mandatory true;

type enumeration {

enum ENABLED;

enum DISABLED;

}

}

list gtpUPathMonitoredSNSSAIs {

key \"sd sst\";

description \"The S-NSSAIs for which the the GTP-U path QoS monitoring
is

to be performed.\";

reference \"3GPP TS 23.003\";

uses types5g3gpp:SNssai;

}

leaf-list monitoredDSCPs {

description \"The DSCPs for which the GTP-U path QoS monitoring is to be

performed.\";

reference \"3GPP TS 29.244\";

type uint32;

}

leaf isEventTriggeredGtpUPathMonitoringSupported {

description \"It indicates whether the event triggered GTP-U path QoS

monitoring reporting based on thresholds is supported.\";

mandatory true;

reference \"3GPP TS 29.244\";

type boolean;

}

leaf isPeriodicGtpUMonitoringSupported {

description \"It indicates whether the periodic GTP-U path QoS
monitoring

reporting is supported.\";

mandatory true;

reference \"3GPP TS 29.244\";

type boolean;

}

leaf isImmediateGtpUMonitoringSupported {

description \"It indicates whether the immediate GTP-U path QoS
monitoring

reporting is supported.\";

mandatory true;

reference \"3GPP TS 29.244\";

type boolean;

}

list gtpUPathDelayThresholds {

key n3AveragePacketDelayThreshold;

// if max-elements is increased later, the key may need to be modified

min-elements 1;

max-elements 1;

description \"It specifies the thresholds for reporting the packet delay

for the GTO-U path QoS monitoring.\";

uses GtpUPathDelayThresholdsType;

}

leaf gtpUPathMinimumWaitTime {

description \"It specifies the minimum waiting time (in seconds) between

two consecutive reports for event triggered GTP-U path QoS monitoring

reporting.\";

type uint32;

}

leaf gtpUPathMeasurementPeriod {

description \"It specifies the period (in seconds) for reporting the
packet

delay for GTP-U path QoS monitoring.\";

type uint32;

}

}

augment \"/me3gpp:ManagedElement/smf3gpp:SMFFunction\" {

list GtpUPathQoSMonitoringControl {

description \"Specifies the capabilities and properties for control of

GTP-U path QoS monitoring. For more information about the GTP-U path

QoS monitoring.\";

reference \"3GPP TS 23.501\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses GtpUPathQoSMonitoringControlGrp;

}

}

}

}

\<CODE ENDS\>

H.5.30 module \_3gpp-5gc-nrm-Configurable5QISet.yang
----------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-configurable5qiset {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-configurable5qiset;

prefix Conf5QIs3gpp;

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"This IOC represents the configurable 5QIs, including

their QoS characteristics, that need to be pre-configured

(and configurable) to the 5G NFs.\";

reference \"3GPP TS 28.541\";

revision 2022-04-29 { reference \"CR-0730\"; }

revision 2020-08-03 { reference \"CR-0321\"; }

revision 2020-06-03 { reference \"CR-0286\"; }

grouping PacketErrorRate {

leaf scalar {

type uint32 {

range 0..9 ;

}

mandatory true;

description \"The Packet Error Rate of a 5QI expressed as Scalar x 10-k

where k is the Exponent.\";

}

leaf exponent {

type uint32 {

range 0..9 ;

}

mandatory true;

description \"The Packet Error Rate of a 5QI expressed as Scalar x 10-k,

where k is the Exponent.\";

}

}

grouping FiveQICharacteristics {

leaf fiveQIValue {

type uint32 {

range 0..255 ;

}

mandatory true;

description \"Identifies the 5QI value.\";

}

leaf resourceType {

type enumeration {

enum GBR;

enum NON\_GBR;

}

mandatory true;

description \"It indicates the Resource Type of a 5QI, as specified

in TS 23.501 \";

}

leaf priorityLevel {

type uint32 {

range 0..127 ;

}

}

leaf packetDelayBudget {

type uint32 {

range 0..1023 ;

}

description \"Indicates the Packet Delay Budget (in unit of 0.5ms)of a
5QI,

as specified in TS 23.501 \";

}

list packetErrorRate {

key \"scalar exponent\";

min-elements 0;

max-elements 1;

uses PacketErrorRate;

reference \"TS 23.501\";

}

leaf averagingWindow {

type uint32 {

range 0..4095 ;

}

units ms;

reference \"TS 23.501\";

}

leaf maximumDataBurstVolume {

type uint32{

range 0..4095 ;

}

units byte;

}

}

grouping Configurable5QISetGrp {

description \"Represents the Configurable5QISet IOC.\";

list configurable5QIs {

key \"fiveQIValue\";

uses FiveQICharacteristics;

}

}

grouping Configurable5QISetSubtree {

list Configurable5QISet {

description \"Specifies the non-standardized 5QIs, including their QoS

characteristics, that need to be pre-configured (and configurable) to

the 5G NFs, see 3GPP TS 23.501.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses Configurable5QISetGrp;

}

}

}

augment \"/subnet3gpp:SubNetwork\" {

uses Configurable5QISetSubtree;

}

augment \"/me3gpp:ManagedElement\" {

uses Configurable5QISetSubtree;

}

}

\<CODE ENDS\>

H.5.31 module \_3gpp-5gc-nrm-FiveQiDscpMappingSet.yang
------------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-FiveQiDscpMappingSet {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-FiveQiDscpMappingSet;

prefix FiveQiDscpMapping3gpp;

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-5gc-nrm-smffunction { prefix smf3gpp; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \" This IOC represents the set of mapping between 5QIs and
DSCP.\";

reference \"3GPP TS 28.541\";

revision 2020-08-03 { reference \"CR-0321\"; }

revision 2020-05-27 { reference \"CR-0287\"; }

grouping FiveQiDscpMapping {

leaf-list fiveQIValues {

type uint32 {

range 0..255 ;

}

min-elements 1;

description \" Identifies the 5QI values that are mapped to a same DSCP,
as specified in TS 28.541.\";

}

leaf dscp {

type uint32 {

range 0..255 ;

}

mandatory true;

}

}

grouping FiveQiDscpMappingSetGrp {

description \"Represents the FiveQiDscpMappingSet IOC.\";

list FiveQiDscpMappingList {

key \"dscp\";

uses FiveQiDscpMapping;

}

}

grouping FiveQiDscpMappingSetSubtree {

list FiveQiDscpMappingSet {

description \"Specifies the mapping between 5QIs and DSCPs.\";

key id;

uses top3gpp:Top\_Grp;

container attributes {

uses FiveQiDscpMappingSetGrp;

}

}

}

augment \"/me3gpp:ManagedElement/smf3gpp:SMFFunction\" {

uses FiveQiDscpMappingSetSubtree;

}

}

\<CODE ENDS\>

H.5.32 module \_3gpp-5gc-nrm-PredefinedPccRuleSet.yang
------------------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-predefinedpccruleset {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-predefinedpccruleset;

prefix PrePcRul3gpp;

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-5gc-nrm-smffunction { prefix smf3gpp; }

import \_3gpp-5gc-nrm-pcffunction { prefix pcf3gpp; }

import ietf-yang-types { prefix yang; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"This IOC represents the predefined PCC rules, which are

configured to SMF and referenced by PCF.\";

reference \"3GPP TS 28.541\";

revision 2021-01-25 { reference \"CR-0453\"; }

revision 2020-09-30 { reference \"CR-0377\"; }

revision 2020-08-21 { reference \"CR-0330\"; }

grouping TscaiInputContainer {

description \"It specifies the transports TSCAI input parameters for TSC

traffic at the ingress interface of the DS-TT/UE for a PCC rule.\";

reference \"3GPP TS 29.512\";

leaf periodicity {

type uint32;

description \"It identifies the time period between the start of two
bursts

in reference to the TSN GM.\";

reference \"3GPPTS 29.571.\";

}

leaf burstArrivalTime {

type yang:date-and-time;

description \"It Indicates the arrival time (in date-time format) of the

data burst in reference to the TSN GM.\";

reference \"3GPPTS 29.571.\";

}

}

grouping ConditionData {

description \"It specifies the specifies the condition data for a PCC
rule.\";

leaf condId {

type string;

mandatory true;

description \"It uniquely identifies the condition data.\";

}

leaf activationTime {

type yang:date-and-time;

description \" It indicates the time (in date-time format) when the

decision data shall be activated.\";

reference \"3GPPTS 29.512 and TS 29.571.\";

}

leaf deactivationTime {

type yang:date-and-time;

description \"It indicates the time (in date-time format) when the
decision

data shall be deactivatedTS 29.512 and TS 29.571.\";

}

leaf accessType {

type enumeration {

enum 3GPP\_ACCESS;

enum NON\_3GPP\_ACCESS;

}

description \"It provides the condition of access type of the UE when
the

session AMBR shall be enforced.\";

reference \"3GPPTS 29.512.\";

}

leaf ratType {

type enumeration {

enum NR;

enum EUTRA;

enum WLAN;

enum VIRTUAL;

enum NBIOT;

enum WIRELINE;

enum WIRELINE\_CABLE;

enum WIRELINE\_BBF;

enum LTE-M;

enum NR\_U;

enum EUTRA\_U;

enum TRUSTED\_N3GA;

enum TRUSTED\_WLAN;

enum UTRA;

enum GERA;

}

description \"It provides the condition of RAT type of the UE when the

session AMBR shall be enforced.\";

reference \"3GPPTS 29.512 and TS 29.571.\";

}

}

grouping SteeringMode {

description \"It specifies the traffic distribution rule, see TS
29.512.\";

leaf steerModeValue {

type enumeration {

enum ACTIVE\_STANDBY;

enum LOAD\_BALANCING;

enum SMALLEST\_DELAY;

enum PRIORITY\_BASED;

}

mandatory true;

description \"It indicates the value of the steering mode, see TS
29.512.\";

}

leaf active {

type enumeration {

enum 3GPP\_ACCESS;

enum NON\_3GPP\_ACCESS;

}

description \"It indicates the active access, see TS 29.571.\";

}

leaf standby {

type enumeration {

enum 3GPP\_ACCESS;

enum NON\_3GPP\_ACCESS;

}

description \"It indicates the Standby access, see TS 29.571.\";

}

leaf threeGLoad {

type uint8 {

range 0..100;

}

description \"It indicates the traffic load to steer to the 3GPP Access

expressed in one percent.\";

}

leaf prioAcc {

type enumeration {

enum 3GPP\_ACCESS;

enum NON\_3GPP\_ACCESS;

}

description \"It indicates the high priority access.\";

reference \"3GPPTS 29.571.\";

}

}

grouping UpPathChgEvent {

description \"It specifies the information about the AF subscriptions of
the

UP path change.\";

reference \"TS 29.512\";

leaf notificationUri {

type string;

mandatory true;

description \"It provides notification address (Uri) of AF receiving the

event notification.\";

}

leaf notifCorreId {

type string;

mandatory true;

description \"It is used to set the value of Notification Correlation ID
in

the notification sent by the SMF, see TS 29.512.\";

}

leaf dnaiChgType {

type enumeration {

enum EARLY;

enum EARLY\_LATE;

enum LATE;

}

mandatory true;

description \"It indicates the type of DNAI change, see TS 29.512.\";

}

leaf afAckInd {

type boolean;

default false;

description \"It identifies whether the AF acknowledgement of UP path

event notification is expected.\";

}

}

grouping RouteInformation {

description \"It specifies the traffic routing information.\";

leaf ipv4Addr {

type string;

description \"It defines the Ipv4 address of the tunnel end point in the

data network, formatted in the dotted decimal notation.\";

}

leaf ipv6Addr {

type string;

description \"It defines the Ipv6 address of the tunnel end point in

the data network.\";

}

leaf portNumber {

type uint32;

mandatory true;

description \" It defines the UDP port number of the tunnel end point in

the data network, see TS 29.571.\";

}

}

grouping RouteToLocation {

description \"It specifies a list of location which the traffic shall be

routed to for the AF request.\";

leaf dnai {

type string;

mandatory true;

description \"It represents the DNAI (Data network access identifier.\";

reference \"3GPPTS 23.501.\";

}

container routeInfo{

description \"It provides the traffic routing information.\";

uses RouteInformation;

}

leaf routeProfId {

type string;

description \"It identifies the routing profile.\";

}

}

grouping RedirectInformaton {

description \"It specifies the redirect information for traffic control
in

the PCC rule.\";

leaf redirectEnabled {

type boolean;

mandatory true;

description \"It indicates whether the redirect instruction is
enabled.\";

}

leaf redirectAddressType {

type enumeration {

enum IPV4\_ADDR;

enum IPV6\_ADDR;

enum URL;

enum SIP\_URI;

}

mandatory true;

description \"It indicates the type of redirect address.\";

reference \"3GPPTS 29.512.\";

}

leaf redirectServerAddress {

type string;

mandatory true;

description \"It indicates the address of the redirect server.\";

}

}

grouping TrafficControlDataInformation {

description \"It specifies the traffic control data for a service

flow of a PCC rule.\";

leaf tcId {

type string;

mandatory true;

description \"It univocally identifies the traffic control policy data

within a PDU session.\";

}

leaf flowStatus {

type enumeration {

enum ENABLED-UPLINK;

enum ENABLED-DOWNLINK;

enum ENABLED;

enum DISABLED;

enum REMOVED;

}

mandatory true;

description \"It represents whether the service data flow(s) are enabled

or disabled.\";

}

container redirectInfo {

description \"It contains the redirect information indicating

whether the detected application traffic should be redirected to another

controlled address.\";

uses RedirectInformaton;

}

container addRedirectInfo {

description \"It contains the additional redirect information indicating

whether the detected application traffic should be redirected to another

controlled address.\";

list redirectInfo {

description \"The list of redirect information indicating whether the

detected application traffic should be redirected to another

controlled address.\";

key \"redirectServerAddress\";

uses RedirectInformaton;

}

}

leaf muteNotif {

type boolean;

default false;

description \"It indicates whether applicat\'on\'s start or stop
notification

is to be muted.\";

}

leaf trafficSteeringPolIdDl {

type string;

description \"It references to a pre-configured traffic steering policy
for

downlink traffic at the SMF, see TS 29.512.\";

}

leaf trafficSteeringPolIdUl {

type string;

description \"It references to a pre-configured traffic steering policy
for

uplink traffic at the SMF, see TS 29.512.\";

}

container routeToLocs {

description \"It provides a list of location which the traffic shall be

routed to for the AF request.\";

list routeToLoc {

description \"The list of location which the traffic shall be routed to

for the AF request.\";

key \"dnai\";

uses RouteToLocation;

}

}

uses UpPathChgEvent;

leaf steerFun {

type enumeration {

enum MPTCP;

enum ATSSS\_LL;

}

description \"It indicates the applicable traffic steering
functionality.\";

reference \"3GPPTS 29.512.\";

}

container steerModeDl {

description \"It provides the traffic distribution rule across 3GPP and

Non-3GPP accesses to apply for downlink traffic.\";

uses SteeringMode;

}

container steerModeUl {

description \"It provides the traffic distribution rule across 3GPP and

Non-3GPP accesses to apply for uplink traffic.\";

uses SteeringMode;

}

leaf mulAccCtrl {

type enumeration {

enum ALLOWED;

enum NOT\_ALLOWED;

}

description \"It indicates whether the service data flow, corresponding
to

the service data flow template, is allowed or not allowed.\";

}

}

grouping ARP {

description \"It specifies the allocation and retention priority of a
QoS

control policy.\";

leaf priorityLevel {

type uint8 {

range 1..15;

}

mandatory true;

description \"It defines the relative importance of a resource
request.\";

}

leaf preemptCap {

type enumeration {

enum NOT\_PREEMPT;

enum MAY\_PREEMPT;

}

mandatory true;

description \"It defines whether a service data flow may get resources
that

were already assigned to another service data flow with a lower priority

level.\";

}

leaf preemptVuln {

type enumeration {

enum NOT\_PREEMPTABLE;

enum PREEMPTABLE;

}

mandatory true;

description \"It defines whether a service data flow may lose the
resources

assigned to it in order to admit a service data flow with higher

priority level.\";

}

}

grouping QosDataInformation {

description \"It specifies the QoS control policy data for a service
flow

of a PCC rule.\";

leaf qosId {

type string;

mandatory true;

description \"It identifies the QoS control policy data for a PCC
rule.\";

}

leaf fiveQIValue {

type uint8 {

range 0..255;

}

description \"It indicates the 5QI value.\";

}

leaf maxbrUl {

type string;

description \"It represents the maximum uplink bandwidth.\";

}

leaf maxbrDl {

type string;

description \"It represents the maximum downlink bandwidth.\";

}

leaf gbrUl {

type string;

description \"It represents the guaranteed uplink bandwidth.\";

}

leaf gbrDl {

type string;

description \"It represents the guaranteed downlink bandwidth.\";

}

uses ARP;

leaf qosNotificationControl {

type boolean;

default false;

description \"It indicates whether notifications are requested from 3GPP

NG-RAN when the GFBR can no longer (or again) be guaranteed for a

QoS Flow during the lifetime of the QoS Flow.\";

}

leaf reflectiveQos {

type boolean;

default false;

description \"Indicates whether the QoS information is reflective for
the

corresponding non-GBR service data flow\";

}

leaf sharingKeyDl {

type string;

description \"It indicates, by containing the same value, what PCC rules

may share resource in downlink direction.\";

}

leaf sharingKeyUl {

type string;

description \"It indicates, by containing the same value, what PCC rules

may share resource in uplink direction.\";

}

leaf maxPacketLossRateDl {

type uint16 {

range 0..1000;

}

description \"It indicates the downlink maximum rate for lost packets
that

can be tolerated for the service data flow.\";

}

leaf maxPacketLossRateUl {

type uint16 {

range 0..1000;

}

description \"It indicates the uplink maximum rate for lost packets that

can be tolerated for the service data flow.\";

}

leaf extMaxDataBurstVol {

type uint32 {

range 4096..2000000;

}

description \"It denotes the largest amount of data that is required to

be transferred within a period of 5G-AN PDB, see TS 29.512.\";

}

}

grouping EthFlowDescription {

description \"It describes an Ethernet flow.\";

leaf destMacAddr {

type string;

mandatory true;

description \"It specifies the destination MAC address formatted in the

hexadecimal. .\";

reference \"clause 1.1 and clause 2.1 of IETF RFC 7042.\";

}

leaf ethType {

type string;

mandatory true;

description \"A two-octet string that represents the Ethertype.\";

reference \" IEEE 802.3 and IETF RFC 7042in hexadecimal
representation.\";

}

leaf fDesc {

type string;

description \"It contains the flow description for the Uplink or
Downlink

IP flow. It shall be present when the ethtype is IP.\";

}

leaf fDir {

type enumeration {

enum DOWNLINK;

enum UPLINK;

}

mandatory true;

description \"It indicates the packet filter direction.\";

}

leaf sourceMacAddr {

type string;

mandatory true;

description \"It specifies the source MAC address formatted in the

hexadecimal notation.\";

reference \"clause 1.1 and clause 2.1 of IETF RFC 7042\";

}

leaf-list vlanTags {

type string;

description \"It specifies the Customer-VLAN and/or Service-VLAN tags

containing the VID, PCP/DEI fields as defined in IEEE 802.1Qand

IETF RFC 7042. The first/lower instance in the array stands for the

Customer-VLAN tag and the second/higher instance in the array stands

for the Service-VLAN tag.\";

}

leaf srcMacAddrEnd {

type string;

description \"It specifies the source MAC address end. If this attribute

is present, the sourceMacAddr attribute specifies the source MAC address

start. E.g. srcMacAddrEnd with value 00-10-A4-23-3E-FE and sourceMacAddr

with value 00-10-A4-23-3E-02 means all MAC addresses

from 00-10-A4-23-3E-02 up to and including 00-10-A4-23-3E-FE.\";

}

leaf destMacAddrEnd {

type string;

description \"It specifies the destination MAC address end. If this

attribute is present, the destMacAddr attribute specifies the

destination MAC address start.\";

}

}

grouping FlowInformation {

description \"It specifies the flow information of a PCC rule.\";

leaf flowDescription {

type string;

mandatory true;

description \"It defines a packet filter for an IP flow.\";

}

uses EthFlowDescription;

leaf packFiltId {

type string;

mandatory true;

description \"It is the identifier of the packet filter.\";

}

leaf packetFilterUsage {

type boolean;

default false;

description \"It indicates if the packet shall be sent to the UE.\";

}

leaf tosTrafficClass {

type string;

mandatory true;

description \"It contains the Ipv4 Type-of-Service and mask field or the

Ipv6 Traffic-Class field and mask field.\";

}

leaf spi {

type string;

mandatory true;

description \"It is the security parameter index of the IPSec packet.\";

reference \"IETF RFC 4301\";

}

leaf flowLabel {

type string;

description \"It specifies the Ipv6 flow label header field.\";

}

leaf flowDirection {

type enumeration {

enum DOWNLINK;

enum UPLINK;

enum BIDIRECTIONAL;

enum UNSPECIFIED;

}

mandatory true;

description \"It indicates the direction/directions that a filter is

applicable.\";

}

}

grouping PccRule {

description \"It specifies the PCC rule, see TS 29.512.\";

leaf pccRuleId {

type string;

mandatory true;

description \"It identifies the PCC rule.\";

}

container flowInfoList {

description \"It is a list of IP flow packet filter information.\";

list flowInfo {

description \"The list of IP flow packet filter information.\";

key \"packFiltId\";

uses FlowInformation;

}

}

leaf applicationId {

type string;

default false;

description \"A reference to the application detection filter configured

at the UPF.\";

}

leaf appDescriptor {

type string;

description \"It is the ATSSS rule application descriptor.\";

}

leaf contentVersion {

type uint8;

description \"Indicates the content version of the PCC rule.\";

}

leaf precedence {

type uint8 {

range 0..255;

}

description \"It indicates the order in which this PCC rule is applied

relative to other PCC rules within the same PDU session.\";

}

leaf afSigProtocol {

type enumeration {

enum NO\_INFORMATION;

enum SIP;

}

description \"Indicates the protocol used for signalling between the UE

and the AF, the default value is NO\_INFORMATION.\";

}

leaf isAppRelocatable {

type boolean;

default false;

description \"It indicates the application relocation possibility, the

default value is NO\_INFORMATION.\";

}

leaf isUeAddrPreserved {

type boolean;

default false;

description \"It Indicates whether UE IP address should be preserved.\";

}

container qosData {

description \"It contains the QoS control policy data for a PCC rule.\";

list qosDataInfo {

description \"The list of QoS control policy data.\";

key \"qosId\";

uses QosDataInformation;

}

}

container altQosParams {

description \"It contains the QoS control policy data for the

Alternative QoS parameter sets of the service data flow.\";

list qosDataInfo {

description \"The list of QoS control policy data.\";

key \"qosId\";

uses QosDataInformation;

}

}

container trafficControlData {

description \"It contains the traffic control policy data for a PCC
rule.\";

list trafficControlDataInfo {

description \"The list of traffic control policy data.\";

key \"tcId\";

uses TrafficControlDataInformation;

}

}

uses ConditionData;

container tscaiInputUl {

description \"It contains transports TSCAI input parameters for

TSC traffic at the ingress interface of the DS-TT/UE

(uplink flow direction).\";

uses TscaiInputContainer;

}

container tscaiInputDl {

description \"It contains transports TSCAI input parameters for TSC
traffic

at the ingress of the NW-TT (downlink flow direction).\";

uses TscaiInputContainer;

}

}

grouping PredefinedPccRuleSetGrp {

description \"Represents the PredefinedPccRuleSet IOC.\";

list PredefinedPccRules {

description \"The list of predefined PCC rules.\";

key \"pccRuleId\";

uses PccRule;

}

}

grouping PredefinedPccRuleSetSubtree {

description \"It specifies the PredefinedPccRuleSet IOC with inherited

attributes.\";

list PredefinedPccRuleSet {

description \"Specifies the predefined PCC rules.\";

key \"id\";

uses top3gpp:Top\_Grp;

container attributes {

description \"It contains the attributes defined specifically in the

PredefinedPccRuleSet IOC.\";

uses PredefinedPccRuleSetGrp;

}

}

}

augment \"/me3gpp:ManagedElement/smf3gpp:SMFFunction\" {

description \"It specifies the containment relation of
PredefinedPccRuleSet

MOI with SMFFunction MOI.\";

uses PredefinedPccRuleSetSubtree;

}

augment \"/me3gpp:ManagedElement/pcf3gpp:PCFFunction\" {

description \"It specifies the containment relation of
PredefinedPccRuleSet

MOI with PCFFunction MOI.\";

uses PredefinedPccRuleSetSubtree;

}

}

\<CODE ENDS\>

H.5.33 module \_3gpp-5gc-nrm-dynamic5QISet.yang
-----------------------------------------------

\<CODE BEGINS\>

module \_3gpp-5gc-nrm-dynamic5qiset {

yang-version 1.1;

namespace urn:3gpp:sa5:\_3gpp-5gc-nrm-dynamic5qiset;

prefix dyn5QIs3gpp;

import \_3gpp-common-top { prefix top3gpp; }

import \_3gpp-common-subnetwork { prefix subnet3gpp; }

import \_3gpp-common-managed-element { prefix me3gpp; }

import \_3gpp-5gc-nrm-configurable5qiset { prefix Conf5QIs3gpp; }

organization \"3gpp SA5\";

contact
\"https://www.3gpp.org/DynaReport/TSG-WG\--S5\--officials.htm?Itemid=464\";

description \"This IOC represents the dynamic 5QIs including their QoS

characteristics.\";

reference \"3GPP TS 28.541\";

revision 2020-09-30 { reference \"CR-0377\"; }

revision 2020-08-06 { reference \"CR-0333\"; }

grouping Dynamic5QISetGrp {

description \"Represents the Dynamic5QISet IOC.\";

list dynamic5QIs {

key \"fiveQIValue\";

description \"Represents the Dynamic5QISet IOC.\";

uses Conf5QIs3gpp:FiveQICharacteristics;

}

}

grouping Dynamic5QISetSubtree {

description \"Helps augmenting Dynamic5QISet into multiple places.\";

list Dynamic5QISet {

description \"Specifies the dynamic 5QIs including their QoS

characteristics, see 3GPP TS 23.501.\";

key \"id\";

uses top3gpp:Top\_Grp;

container attributes {

uses Dynamic5QISetGrp;

}

}

}

augment \"/subnet3gpp:SubNetwork\" {

uses Dynamic5QISetSubtree;

}

augment \"/me3gpp:ManagedElement\" {

uses Dynamic5QISetSubtree;

}

}

\<CODE ENDS\>

H.6 Void
========

H.7 Mount information
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

########  Annex I (normative): XML definitions for network slice

I.1 General
===========

This annex contains the XML definitions for the network slice NRM, in
accordance with network slice NRM Information Model definitions
specified in clause 6.

I.2 Architectural features
==========================

The overall architectural feature of network slice information model is
specified in clause 6, this clause specifies features that are specific
to the Schema definitions.

The XML definitions of the present document specify the schema for a
configuration content, which can be included in a configuration file for
Bulk configuration management operations.

I.3 Mapping
===========

I.3.1 General mapping
---------------------

An IOC maps to an XML element of the same name as the IOC\'s name in the
Information Model. An IOC attribute maps to a sub-element of the
corresponding IOC\'s XML element, and the name of this sub-element is
the same as the attribute\'s name in the Information Model.

I.3.2 Information Object Class (IOC) mapping
--------------------------------------------

The mapping is not present in the current version of the present
document.

I.4 Solution Set (SS) definitions
=================================

I.4.1 XML definition structure
------------------------------

The overall description of the file format of configuration data XML
files is provided by 3GPP TS 32.616 \[33\].

This annex defines the NRM-specific XML schema sliceNrm.xsd for the
network slice Information Model defined in clause 6.

XML schema sliceNrm.xsd explicitly declares NRM-specific XML element
types for the related NRM.

The definition of those NRM-specific XML element types complies with the
generic mapping rules defined in 3GPP TS 32.616 \[33\].

I.4.2 Graphical representation
------------------------------

The graphical representation is not present in the current version of
the present document.

I.4.3 XML schema \"sliceNrm.xsd\"
---------------------------------

\<?xml version=\"1.0\" encoding=\"UTF-8\"?\>

\<!\--

3GPP TS 28.541 network slice Network Resource Model

XML schema definition

sliceNrm.xsd

\--\>

\<schema xmlns=\"http://www.w3.org/2001/XMLSchema\"

xmlns:xn=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.623\#genericNrm\"

xmlns:sl=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.541\#sliceNrm\"

xmlns:nn=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.541\#nrNrm\"

xmlns:ngc=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.541\#ngcNrm\"

xmlns:en=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.659\#eutranNrm\"

xmlns:sm=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.626\#stateManagementIRP\"

targetNamespace=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.541\#sliceNrm\"
elementFormDefault=\"qualified\"\>

\<import
namespace=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.623\#genericNrm\"/\>

\<import
namespace=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.541\#nrNrm\"/\>

\<import
namespace=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.541\#ngcNrm\"/\>

\<import
namespace=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.659\#eutranNrm\"/\>

\<import
namespace=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.626\#stateManagementIRP\"/\>

\<simpleType name=\"MobilityLevel\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"STATIONARY\"/\>

\<enumeration value=\"NOMADIC\"/\>

\<enumeration value=\"RESTRICTED MOBILITY\"/\>

\<enumeration value=\"FULLY MOBILITY\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"SharingLevel\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"SHARED\"/\>

\<enumeration value=\"NON-SHARED\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"Category\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"character\"/\>

\<enumeration value=\"scalability\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"Tagging\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"performance\"/\>

\<enumeration value=\"function\"/\>

\<enumeration value=\"operation\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"Exposure\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"API\"/\>

\<enumeration value=\"KPI\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"ServAttrCom\"\>

\<sequence\>

\<element name=\"category\" type=\"sl:Category\"/\>

\<element name=\"tagging\" type=\"sl:Tagging\" minOccurs=\"0\"
maxOccurs=\"3\"/\>

\<element name=\"exposure\" type=\"sl:Exposure\" minOccurs=\"0\"/\>

\</sequence\>

\</complexType \>

\<simpleType name=\"DelayToleranceSupport\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"NOT SUPPORTED\"/\>

\<enumeration value=\"SUPPORTED\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"DeterministicCommAvailability\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"NOT SUPPORTED\"/\>

\<enumeration value=\"SUPPORTED\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"UserMgmtOpenSupport\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"NOT SUPPORTED\"/\>

\<enumeration value=\"SUPPORTED\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"V2XCommModelsV2XMode\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"NOT SUPPORTED\"/\>

\<enumeration value=\"SUPPORTED BY NR\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"DelayTolerance\"\>

\<sequence\>

\<element name=\"servAttrCom\" type=\"sl:ServAttrCom\"/\>

\<element name=\"support\" type=\"sl:DelayToleranceSupport\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"DeterministicComm\"\>

\<sequence\>

\<element name=\"servAttrCom\" type=\"sl:ServAttrCom\"/\>

\<element name=\"availability\"
type=\"sl:DeterministicCommAvailability\"/\>

\<element name=\"periodicityList\" type=\"string\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"DLThpt\"\>

\<sequence\>

\<element name=\"servAttrCom\" type=\"sl:ServAttrCom\"/\>

\<element name=\"guaThpt\" type=\"float\"/\>

\<element name=\"maxThpt\" type=\"float\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"ULThpt\"\>

\<sequence\>

\<element name=\"servAttrCom\" type=\"sl:ServAttrCom\"/\>

\<element name=\"guaThpt\" type=\"float\" minOccurs=\"0\"/\>

\<element name=\"maxThpt\" type=\"float\" minOccurs=\"0\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"MaxPktSize\"\>

\<sequence\>

\<element name=\"servAttrCom\" type=\"sl:ServAttrCom\"/\>

\<element name=\"maxsize\" type=\"integer\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"KPIMonitoring\"\>

\<sequence\>

\<element name=\"servAttrCom\" type=\"sl:ServAttrCom\"/\>

\<element name=\"kPIList\" type=\"string\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"UserMgmtOpen\"\>

\<sequence\>

\<element name=\"servAttrCom\" type=\"sl:ServAttrCom\"/\>

\<element name=\"support\" type=\"sl:UserMgmtOpenSupport\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"V2XCommMode\"\>

\<sequence\>

\<element name=\"servAttrCom\" type=\"sl:ServAttrCom\"/\>

\<element name=\"v2XMode\" type=\"sl:V2XCommModelsV2XMode\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"TermDensity\"\>

\<sequence\>

\<choice minOccurs=\"1\" maxOccurs=\"1\"\>

\<element name=\"servAttrCom\" type=\"sl:ServAttrCom\"/\>

\<element name=\"density\" type=\"integer\"/\>

\</choice\>

\</sequence\>

\</complexType\>

\<complexType name=\"ServiceProfile\"\>

\<sequence\>

\<element name=\"serviceProfileId\" type=\"string\"/\>

\<element name=\"sNSSAIList\" type=\"ngc:SnssaiList\"/\>

\<element name=\"pLMNIdList\" type=\"en:PLMNIdList\"/\>

\<element name=\"maxNumberofUEs\" type=\"long\" minOccurs=\"0\"/\>

\<element name=\"latency\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"uEMobilityLevel\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"resourceSharingLevel\" type=\"integer\"
minOccurs=\"0\"/\>

\<element name=\"sst\" type=\"ngc:Sst\"/\>

\<element name=\"availability\" type=\"float\" minOccurs=\"0\"/\>

\<element name=\"delayTolerance\" type=\"sl:DelayTolerance\"
minOccurs=\"0\"/\>

\<element name=\"deterministicComm\" type=\"sl:DeterministicComm\"
minOccurs=\"0\"/\>

\<element name=\"dLThptPerSlice\" type=\"sl:DLThpt\" minOccurs=\"0\"/\>

\<element name=\"dLThptPerUE\" type=\"sl:DLThpt\" minOccurs=\"0\"/\>

\<element name=\"uLThptPerSlice\" type=\"sl:ULThpt\" minOccurs=\"0\"/\>

\<element name=\"uLThptPerUE\" type=\"sl:ULThpt\" minOccurs=\"0\"/\>

\<element name=\"maxPktSize\" type=\"sl:MaxPktSize\" minOccurs=\"0\"/\>

\<element name=\"maxNumberofConns\" type=\"sl:MaxNumberofConns\"
minOccurs=\"0\"/\>

\<element name=\"kPIMonitoring\" type=\"sl:KPIMonitoring\"
minOccurs=\"0\"/\>

\<element name=\"userMgmtOpen\" type=\"sl:UserMgmtOpen\"
minOccurs=\"0\"/\>

\<element name=\"v2XCommModels\" type=\"sl:V2XCommMode\"
minOccurs=\"0\"/\>

\<element name=\"coverageArea\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"termDensity\" type=\"sl:TermDensity\"
minOccurs=\"0\"/\>

\<element name=\"activityFactor\" type=\"float\" minOccurs=\"0\"/\>

\<element name=\"uESpeed\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"jitter\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"survivalTime\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"reliability\" type=\"string\" minOccurs=\"0\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"ServiceProfileList\"\>

\<sequence\>

\<element name=\"serviceProfile\" type=\"sl:ServiceProfile\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"SliceProfile\"\>

\<sequence\>

\<element name=\"sliceProfileId\" type=\"string\"/\>

\<element name=\"sNSSAIList\" type=\" ngc:SnssaiList\"/\>

\<element name=\"pLMNIdList\" type=\"en:PLMNIdList\"/\>

\<element name=\"perfReq\" type=\"sl:PerfReq\"/\>

\<element name=\"maxNumberofUEs\" type=\"long\" minOccurs=\"0\"/\>

\<element name=\"coverageAreaTAList\" type=\"ngc:NrTACList\"
minOccurs=\"0\"/\>

\<element name=\"latency\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"uEMobilityLevel\" type=\"sl:MobilityLevel\"
minOccurs=\"0\"/\>

\<element name=\"resourceSharingLevel\" type=\"integer\"
minOccurs=\"0\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"SliceProfileList\"\>

\<sequence\>

\<element name=\"sliceProfile\" type=\"sl:SliceProfile\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"NsInfo\"\>

\<!\-- Refer to definitions in subclause 8.3.3.2.2 of ETSI NFV IFA013
\--\>

\<sequence\>

\<element name=\"nsInstanceId\" type=\"string\"/\>

\<element name=\"nsName\" type=\"string\"/\>

\<element name=\"description\" type=\"string\"/\>

\</sequence\>

\</complexType\>

\<element name=\"NetworkSlice\"
substitutionGroup=\"xn:SubNetworkOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from SubNetwork \--\>

\<element name=\"dnPrefix\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"userDefinedNetworkType\" type=\"string\"/\>

\<element name=\"setOfMcc\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from SubNetwork \--\>

\<element name=\"operationalState\" type=\"sm:operationalStateType\"/\>

\<element name=\"administrativeState\"
type=\"sm:administrativeStateType\"/\>

\<element name=\"serviceProfileList\" type=\"sl:ServiceProfileList\"/\>
\<element *name*=\"networkSliceSubnetRef\" *type*=\"xn:dn\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"NetworkSliceSubnet\"
substitutionGroup=\"xn:SubNetworkOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from SubNetwork \--\>

\<element name=\"dnPrefix\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"userLabel\" type=\"string\"/\>

\<element name=\"userDefinedNetworkType\" type=\"string\"/\>

\<element name=\"setOfMcc\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<!\-- End of inherited attributes from SubNetwork \--\>

\<element name=\"operationalState\" type=\"sm:operationalStateType\"/\>

\<element name=\"administrativeState\"
type=\"sm:administrativeStateType\"/\>

\<element name=\"nsInfo\" type=\"sl:NsInfo\" minOccurs=\"0\"/\>

\<element name=\"sliceProfileList\" type=\"sl:SliceProfileList\"/\>

\<element *name*=\"managedFunctionRef\" *type*=\"xn:dnlist\"/\>

\<element *name*=\"networkSliceSubnetRef\" *type*=\"xn:dnlist\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\</schema\>

########  Annex J (normative): OpenAPI definition of the Slice NRM

J.1 General 
===========

This annex contains the OpenAPI definition of the Slice NRM in YAML
format.

The Information Service (IS) of the NR NRM is defined in clause 6.

Mapping rules to produce the OpenAPI definition based on the IS are
defined in 3GPP TS 32.160 \[47\].

J.2 Void
========

J.3 Void
========

J.4 Solution Set (SS) definitions
=================================

J.4.1 Void
----------

J.4.2 Void
----------

J.4.3 OpenAPI document \"TS28541\_SliceNrm.yaml\"
-------------------------------------------------

openapi: 3.0.1

info:

title: Slice NRM

version: 16.16.0

description: \>-

OAS 3.0.1 specification of the Slice NRM

@ 2023, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI,
TTA, TTC).

All rights reserved.

externalDocs:

description: 3GPP TS 28.541; 5G NRM, Slice NRM

url: http://www.3gpp.org/ftp/Specs/archive/28\_series/28.541/

paths: {}

components:

schemas:

\#\-\-\-\-\-\-\-\-\-\-\-- Type definitions
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Float:

type: number

format: float

MobilityLevel:

type: string

enum:

\- STATIONARY

\- NOMADIC

\- RESTRICTED\_MOBILITY

\- FULL\_MOBILITY

SharingLevel:

type: string

enum:

\- SHARED

\- NON\_SHARED

NetworkSliceSharingIndicator:

type: string

enum:

\- SHARED

\- NON\_SHARED

PerfReqEmbb:

type: object

properties:

expDataRateDL:

type: number

expDataRateUL:

type: number

areaTrafficCapDL:

type: number

areaTrafficCapUL:

type: number

userDensity:

type: number

activityFactor:

type: number

PerfReqEmbbList:

type: array

items:

\$ref: \'\#/components/schemas/PerfReqEmbb\'

PerfReqUrllc:

type: object

properties:

cSAvailabilityTarget:

type: number

cSReliabilityMeanTime:

type: string

expDataRate:

type: number

msgSizeByte:

type: string

transferIntervalTarget:

type: string

survivalTime:

type: string

PerfReqUrllcList:

type: array

items:

\$ref: \'\#/components/schemas/PerfReqUrllc\'

PerfReq:

oneOf:

\- \$ref: \'\#/components/schemas/PerfReqEmbbList\'

\- \$ref: \'\#/components/schemas/PerfReqUrllcList\'

Category:

type: string

enum:

\- CHARACTER

\- SCALABILITY

Tagging:

type: array

items:

type: string

enum:

\- PERFORMANCE

\- FUNCTION

\- OPERATION

Exposure:

type: string

enum:

\- API

\- KPI

ServAttrCom:

type: object

properties:

category:

\$ref: \'\#/components/schemas/Category\'

tagging:

\$ref: \'\#/components/schemas/Tagging\'

exposure:

\$ref: \'\#/components/schemas/Exposure\'

Support:

type: string

enum:

\- NOT\_SUPPORTED

\- SUPPORTED

DelayTolerance:

type: object

properties:

servAttrCom:

\$ref: \'\#/components/schemas/ServAttrCom\'

support:

\$ref: \'\#/components/schemas/Support\'

DeterministicComm:

type: object

properties:

servAttrCom:

\$ref: \'\#/components/schemas/ServAttrCom\'

availability:

\$ref: \'\#/components/schemas/Support\'

periodicityList:

type: array

items:

type: integer

DLThptPerSlice:

type: object

properties:

servAttrCom:

\$ref: \'\#/components/schemas/ServAttrCom\'

guaThpt:

\$ref: \'\#/components/schemas/Float\'

maxThpt:

\$ref: \'\#/components/schemas/Float\'

DLThptPerUE:

type: object

properties:

servAttrCom:

\$ref: \'\#/components/schemas/ServAttrCom\'

guaThpt:

\$ref: \'\#/components/schemas/Float\'

maxThpt:

\$ref: \'\#/components/schemas/Float\'

ULThptPerSlice:

type: object

properties:

servAttrCom:

\$ref: \'\#/components/schemas/ServAttrCom\'

guaThpt:

\$ref: \'\#/components/schemas/Float\'

maxThpt:

\$ref: \'\#/components/schemas/Float\'

ULThptPerUE:

type: object

properties:

servAttrCom:

\$ref: \'\#/components/schemas/ServAttrCom\'

guaThpt:

\$ref: \'\#/components/schemas/Float\'

maxThpt:

\$ref: \'\#/components/schemas/Float\'

MaxPktSize:

type: object

properties:

servAttrCom:

\$ref: \'\#/components/schemas/ServAttrCom\'

maxsize:

type: integer

MaxNumberofConns:

type: object

properties:

servAttrCom:

\$ref: \'\#/components/schemas/ServAttrCom\'

nOofConn:

type: integer

KPIMonitoring:

type: object

properties:

servAttrCom:

\$ref: \'\#/components/schemas/ServAttrCom\'

kPIList:

type: array

items:

type: string

UserMgmtOpen:

type: object

properties:

servAttrCom:

\$ref: \'\#/components/schemas/ServAttrCom\'

support:

\$ref: \'\#/components/schemas/Support\'

V2XCommMode:

type: object

properties:

servAttrCom:

\$ref: \'\#/components/schemas/ServAttrCom\'

v2XMode:

\$ref: \'\#/components/schemas/Support\'

TermDensity:

type: object

properties:

servAttrCom:

\$ref: \'\#/components/schemas/ServAttrCom\'

density:

type: integer

NsInfo:

type: object

properties:

nsInstanceId:

type: string

nsName:

type: string

ServiceProfile:

type: object

properties:

serviceProfileId:

type: string

plmnInfoList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnInfoList\'

maxNumberofUEs:

type: number

latency:

type: number

uEMobilityLevel:

\$ref: \'\#/components/schemas/MobilityLevel\'

sst:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/Sst\'

networkSliceSharingIndicator:

\$ref: \'\#/components/schemas/NetworkSliceSharingIndicator\'

availability:

type: number

delayTolerance:

\$ref: \'\#/components/schemas/DelayTolerance\'

deterministicComm:

\$ref: \'\#/components/schemas/DeterministicComm\'

dLThptPerSlice:

\$ref: \'\#/components/schemas/DLThptPerSlice\'

dLThptPerUE:

\$ref: \'\#/components/schemas/DLThptPerUE\'

uLThptPerSlice:

\$ref: \'\#/components/schemas/ULThptPerSlice\'

uLThptPerUE:

\$ref: \'\#/components/schemas/ULThptPerUE\'

maxPktSize:

\$ref: \'\#/components/schemas/MaxPktSize\'

maxNumberofConns:

\$ref: \'\#/components/schemas/MaxNumberofConns\'

kPIMonitoring:

\$ref: \'\#/components/schemas/KPIMonitoring\'

userMgmtOpen:

\$ref: \'\#/components/schemas/UserMgmtOpen\'

v2XCommMode:

\$ref: \'\#/components/schemas/V2XCommMode\'

coverageArea:

type: array

items:

type: string

termDensity:

\$ref: \'\#/components/schemas/TermDensity\'

activityFactor:

\$ref: \'\#/components/schemas/Float\'

uESpeed:

type: integer

jitter:

type: integer

survivalTime:

type: string

reliability:

type: string

SliceProfile:

type: object

properties:

sliceProfileId:

type: string

plmnInfoList:

\$ref: \'TS28541\_NrNrm.yaml\#/components/schemas/PlmnInfoList\'

perfReq:

\$ref: \'\#/components/schemas/PerfReq\'

maxNumberofUEs:

type: number

coverageAreaTAList:

type: array

items:

\$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Tai\'

latency:

type: number

uEMobilityLevel:

\$ref: \'\#/components/schemas/MobilityLevel\'

resourceSharingLevel:

\$ref: \'\#/components/schemas/SharingLevel\'

IpAddress:

oneOf:

\- \$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Ipv4Addr\'

\- \$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Ipv6Addr\'

ServiceProfileList:

type: array

items:

\$ref: \'\#/components/schemas/ServiceProfile\'

SliceProfileList:

type: array

items:

\$ref: \'\#/components/schemas/SliceProfile\'

\#\-\-\-\-\-\-\-\-\-\-\-- Definition of concrete IOCs
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

MnS:

oneOf:

\- type: object

properties:

SubNetwork:

\$ref: \'\#/components/schemas/SubNetwork-Multiple\'

\# - type: object

\# properties:

\# ManagedElement:

\# \$ref: \'\#/components/schemas/ManagedElement-Multiple\'

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

NetworkSlice:

\$ref: \'\#/components/schemas/NetworkSlice-Multiple\'

NetworkSliceSubnet:

\$ref: \'\#/components/schemas/NetworkSliceSubnet-Multiple\'

EP\_Transport:

\$ref: \'\#/components/schemas/EP\_Transport-Multiple\'

NetworkSlice-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- type: object

properties:

networkSliceSubnetRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

operationalState:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/OperationalState\'

administrativeState:

\$ref:
\'TS28623\_ComDefs.yaml\#/components/schemas/AdministrativeState\'

serviceProfileList:

\$ref: \'\#/components/schemas/ServiceProfileList\'

NetworkSliceSubnet-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- type: object

properties:

managedFunctionRefList:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/DnList\'

networkSliceSubnetRefList:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/DnList\'

operationalState:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/OperationalState\'

administrativeState:

\$ref:
\'TS28623\_ComDefs.yaml\#/components/schemas/AdministrativeState\'

nsInfo:

\$ref: \'\#/components/schemas/NsInfo\'

sliceProfileList:

\$ref: \'\#/components/schemas/SliceProfileList\'

epTransportRefList:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/DnList\'

priorityLabel:

type: integer

EP\_Transport-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

type: object

properties:

ipAddress:

\$ref: \'\#/components/schemas/IpAddress\'

logicInterfaceId:

type: string

nextHopInfo:

type: string

qosProfile:

type: string

epApplicationRefs:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/DnList\'

\#\-\-\-\-\-\-\-- Definition of JSON arrays for name-contained IOCs
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

SubNetwork-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/SubNetwork-Single\'

NetworkSlice-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/NetworkSlice-Single\'

NetworkSliceSubnet-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/NetworkSliceSubnet-Single\'

EP\_Transport-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_Transport-Single\'

\#\-\-\-\-\-\-\-\-\-\-\-- Definitions in TS 28.541 for TS 28.532
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

resources-sliceNrm:

oneOf:

\- \$ref: \'\#/components/schemas/MnS\'

\- \$ref: \'\#/components/schemas/SubNetwork-Single\'

\- \$ref: \'\#/components/schemas/NetworkSlice-Single\'

\- \$ref: \'\#/components/schemas/NetworkSliceSubnet-Single\'

########  - \$ref: \'\#/components/schemas/EP\_Transport-Single\' Annex K (normative): Void

########  Annex L (normative): Relation of GSMA GST, ServiceProfile and SliceProfile

L.1 General
===========

This annex describes the relation between GSMA GST\[50\] and information
model ServiceProfile and SliceProfile.

L.2 GSMA GST, ServiceProfile and sliceProfile
=============================================

The GSMA GST is used as the SLA information for the communication
between the NSC (e.g. vertical industry) and the NSP. The SLA
requirements can be fulfilled from management aspect and control aspect
in a coordinated way. The SLS includes ServiceProfile information model.

As shown in figure L.2.1, the GST \[50\] is translated and used as input
to NRM ServiceProfile, the ServiceProfile can be translated to
corresponding requirements for dedicated domains. For example, 5GC
SliceProfile is used to carry 5GC domain requirements, NG-RAN
SliceProfile is used to carry NG-RAN domain requirements, and TN
requirements are translated and provide to TN domain. Some of the
information in 5GC SliceProfile and NG-RAN SliceProfile translated to
configurable parameters of network function for the control plane SLA
support purpose.

NOTE: how to do the translation is out of the scope of the present
document.

![](media/image1.png){width="6.510416666666667in" height="2.78125in"}

Figure L.2-1 Relation between GSMA GST, ServiceProfile and SliceProfile

########  Annex M (normative): Managed NF Service state handling

M.1 Combined state diagram for a Managed NF Service
===================================================

Figure M.1-: Combined Managed NF Service state diagram

Table M.1-1: The Managed NF Service state transition table

+----------------+----------------------------------------------------+
| Trigger number | The state transition events and actions            |
+================+====================================================+
| 1              | Event: Received information of deployment of a     |
|                | Network Function (NF) service.                     |
|                |                                                    |
|                | Action: Create a ManagedNFService instance (MSI)   |
|                | whose(Administrative/Operational/Registration) are |
|                | set to Locked/Disabled/Deregistered.               |
+----------------+----------------------------------------------------+
| 2              | Event: Received information of positive state      |
|                | change of the NF service.                          |
|                |                                                    |
|                | Action: Set the Operational state of the MSI to    |
|                | Enabled.                                           |
+----------------+----------------------------------------------------+
| 3              | Event: Received CM operation to unlock the NF      |
|                | Service or the NF.                                 |
|                |                                                    |
|                | Action: Set the Administrative state of the MSI to |
|                | Unlocked.                                          |
|                |                                                    |
|                | Note: Changing Administrative state on NF service  |
|                | level is optional                                  |
+----------------+----------------------------------------------------+
| 4              | Event: Received information that the NF Service is |
|                | registered to an NRF either by the NF itself or by |
|                | an OAM system on behalf of the NF.                 |
|                |                                                    |
|                | Action: Set the registration state of the MSI to   |
|                | Registered.                                        |
+----------------+----------------------------------------------------+
| 5              | Event: Received information that the NF Service is |
|                | deregistered from the NRF either by the NF itself  |
|                | or by an OAM system on behalf of the NF.           |
|                |                                                    |
|                | Action: Set registration state of the MSI to       |
|                | Deregistered.                                      |
+----------------+----------------------------------------------------+
| 6              | Event: Received information that the NF Service is |
|                | unavailable because of, for example, limitation of |
|                | resource or other exceptions.                      |
|                |                                                    |
|                | Action: Set the Operational state of the MSI to    |
|                | Disabled.                                          |
+----------------+----------------------------------------------------+
| 7              | Event: Received information that the NF Service is |
|                | unavilable.                                        |
|                |                                                    |
|                | Action: Deregister the NF Service on behalf of the |
|                | NF, and set the registration state of the MSI to   |
|                | Deregistered.                                      |
+----------------+----------------------------------------------------+
| 8              | Event: Received CM operation to lock the NF        |
|                | Service or the NF.                                 |
|                |                                                    |
|                | Action: Set the Administrative state of the MSI to |
|                | Locked.                                            |
|                |                                                    |
|                | Note: Changing Administrative state on NF service  |
|                | level is optional                                  |
+----------------+----------------------------------------------------+
| 9              | Event: Received information that the NF Service is |
|                | terminated or deleted,                             |
|                |                                                    |
|                | Action: Delete the MSI and set its state to NULL.  |
+----------------+----------------------------------------------------+

######## Annex N (informative): Mapping between GSMA GST and ServiceProfile 

Table N-1 shows the mapping from the GSMA GST, see reference \[50\] to
the ServiceProfile which can be found in clause 6.3.3 of the present
document.

Table N-1: Mapping between GSMA GST and ServiceProfile

  GSMA GST attribute name \[50\]                                                                                                                                                      GST reference location \[50\]   ServiceProfile attribute   Clause number (see NOTE)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------- -------------------------- --------------------------
  Availability                                                                                                                                                                        3.4.1                           availability               6.4.1
  Area of service                                                                                                                                                                     3.4.2                           coverageArea               6.4.1
  Delay tolerance                                                                                                                                                                     3.4.3                           delayTolerance             6.4.1 and 6.3.7
  Deterministic communication                                                                                                                                                         3.4.4                           deterministicComm          6.4.1
  Maximum supported packet size                                                                                                                                                       3.4.11                          MaxPktSize                 6.4.1 and 6.3.11
  Downlink throughput per network slice                                                                                                                                               3.4.5                           dLThptPerSlice             6.4.1 and 6.3.9
  Uplink throughput per network slice                                                                                                                                                 3.4.31                          uLThptPerSlice             6.4.1 and 6.3.9
  Downlink maximum throughput per UE                                                                                                                                                  3.4.6                           dLThptPerUE                6.4.1 and 6.3.9
  Uplink maximum throughput per UE                                                                                                                                                    3.4.32                          uLThptPerUE                6.4.1 and 6.3.9
  Energy efficiency                                                                                                                                                                   3.4.7                           NA                         NA
  Performance monitoring                                                                                                                                                              3.4.18                          kPIMonitoring              6.4.1 and 6.3.14
  Number of connections                                                                                                                                                               3.4.16                          maxNumberofConns           6.4.1 and 6.3.12
  Number of terminals                                                                                                                                                                 3.4.17                          maxNumberofUEs             6.4.1 and 6.3.38
  NB-IoT support                                                                                                                                                                      3.4.14                          NA                         NA
  Positioning support                                                                                                                                                                 3.4.20                          NA                         NA
  Radiospectrum                                                                                                                                                                       3.4.21                          NA                         NA
  Simultaneous use of the network slice                                                                                                                                               3.4.25                          NA                         NA
  Synchronicity                                                                                                                                                                       3.4.29                          NA                         NA
  Terminal density                                                                                                                                                                    3.4.30                          termDensity                6.4.1 and 6.3.17
  Supported device velocity                                                                                                                                                           3.4.28                          uESpeed                    6.4.1
  User management openness                                                                                                                                                            3.4.33                          userMgmtOpen               6.4.1 and 6.3.14
  V2X communication mode                                                                                                                                                              3.4.35                          v2XCommModels              6.4.1 and 6.3.16
  Latency from (last) UPF to Application Server                                                                                                                                       3.4.36                          NA                         NA
  Network Slice Specific Authentication and Authorization (NSSAA) Required                                                                                                            3.4.37                          NA                         NA
  Slice quality of service parameters                                                                                                                                                 3.4.26                          NA                         NA
  Performance prediction                                                                                                                                                              3.4.19                          NA                         NA
  User data access                                                                                                                                                                    3.4.34                          NA                         NA
  Isolation level                                                                                                                                                                     3.4.9                           NA                         NA
  Group communication support                                                                                                                                                         3.4.8                           NA                         NA
  Mission critical support                                                                                                                                                            3.4.12                          NA                         NA
  MMTel support                                                                                                                                                                       3.4.13                          NA                         NA
  Network Slice Customer network functions                                                                                                                                            3.4.15                          NA                         NA
  Monitoring and analytics                                                                                                                                                            3.4.23                          NA                         NA
  Session and Service Continuity support                                                                                                                                              3.4.24                          NA                         NA
  Support for non-IP traffic                                                                                                                                                          3.4.27                          NA                         NA
  NOTE: The attribute definitions can be found in clause 6.4, there where the attribute is defined by a custom data type the clause for the data type definition is also mentioned.                                                              

########  Annex O (informative): Change history

  -------------------- ---------- ----------- ------ ----- ----- ----------------------------------------------------------------------------------------------------------------- -------------
  **Change history**                                                                                                                                                               
  Date                 Meeting    TDoc        CR     Rev   Cat   Subject/Comment                                                                                                   New version
  2018-09              SA\#81                                    Upgrade to change control version                                                                                 15.0.0
  2018-09              SA\#81                                    EdiHelp review                                                                                                    15.0.1
  2018-12              SA\#82     SP-181046   0001   1     F     Fix issues raised by EditHelp                                                                                     15.1.0
  2018-12              SA\#82     SP-181046   0002   2     F     Update NR Stage 2 definition to align with TS 37.340 for MR-DC                                                    15.1.0
  2018-12              SA\#82     SP-181046   0003   1     F     Update NRM Stage 2 defintion to align with TS 23.501 for 5G architecture                                          15.1.0
  2018-12              SA\#82     SP-181046   0005   1     F     Update Stage 3 XML definition of NR to align with Stage 2 content                                                 15.1.0
  2018-12              SA\#82     SP-181046   0006   1     F     Update Stage 3 JSON definition of NR to align with Stage 2 content                                                15.1.0
  2018-12              SA\#82     SP-181046   0007   1     F     Update Stage 3 YANG definition of NR to align with Stage 2 content                                                15.1.0
  2018-12              SA\#82     SP-181046   0008   1     F     Update Stage 3 XML definition of 5GC to align with Stage 2 content                                                15.1.0
  2018-12              SA\#82     SP-181046   0009   1     F     Update Stage 3 JSON definition of 5GC to align with Stage 2 content                                               15.1.0
  2018-12              SA\#82     SP-181046   0011   1     F     Update stage 3 XML definition of NS to align with Stage 2 content                                                 15.1.0
  2018-12              SA\#82     SP-181046   0012   1     F     Update Stage 3 JSON definition of NS to align with Stage 2 content                                                15.1.0
  2018-12              SA\#82     SP-181046   0013   1     F     Update stage 3 YANG definition of NS to align with Stage 2 content                                                15.1.0
  2018-12              SA\#82     SP-181046   0014   1     F     Correct the term sNSSAIList and nRTAClist                                                                         15.1.0
  2018-12              SA\#82     SP-181046   0015   1     F     Update the inheritance hierarchy figure for NR NRM to include BWP IOC and NRSectorCarrier IOC                     15.1.0
  2018-12              SA\#82     SP-181046   0016   1     F     Change the term nCGI to nCI                                                                                       15.1.0
  2018-12              SA\#82     SP-181046   0019   1     F     Align properties of cell state                                                                                    15.1.0
  2018-12              SA\#82     SP-181046   0021   1     F     Add missing attribute definition and condition                                                                    15.1.0
  2018-12              SA\#82     SP-181047   0022   1     F     Add missing detail definition for attribute                                                                       15.1.0
  2018-12              SA\#82     SP-181047   0023   1     F     Adding missing attribute, and correction of reference                                                             15.1.0
  2018-12              SA\#82     SP-181043   0025   \-    F     Remove NSSF from the abbrevations                                                                                 15.1.0
  2018-12              SA\#82     SP-181046   0027   \-    F     Replace symbol for network slice state management                                                                 15.1.0
  2018-12              SA\#82     SP-181046   0031   1     F     Remove the ExternalENBFunction definition                                                                         15.1.0
  2018-12              SA\#82     SP-181046   0033   1     F     Align the management of external function and cell with TS 28.658                                                 15.1.0
  2018-12              SA\#82     SP-181156   0034   1     F     Update NR NRM with Cell Relation                                                                                  15.1.0
  2018-12              SA\#82     SP-181156   0038   3     F     RRM Policy enhancements                                                                                           15.1.0
  2018-12              SA\#82     SP-181156   0039   1     F     Fix containment issue in YANG definition                                                                          15.1.0
  2018-12              SA\#82     SP-181156   0040   \-    F     Implement minor corrections                                                                                       15.1.0
  2018-12              SA\#82     SP-181042   0041   \-    F     Update Stage 3 NRM for RRM Policy enhancements                                                                    15.1.0
  2019-03              SA\#83     SP-190121   0043   1     F     Align NR attributes definition related to SSB with corresponding NG-RAN IE definition                             15.2.0
  2019-03              SA\#83     SP-190121   0044   1     F     Correct the use of nCI and PLMN                                                                                   15.2.0
  2019-03              SA\#83     SP-190121   0045   \-    F     Remove duplicate definition for ExternalNRCellCU                                                                  15.2.0
  2019-03              SA\#83     SP-190121   0046   2     F     Correct class diagram for view on external entities                                                               15.2.0
  2019-03              SA\#83     SP-190121   0047   1     F     Correct the definition for resourceSharingLevel                                                                   15.2.0
  2019-03              SA\#83     SP-190121   0048   1     F     Correction of references                                                                                          15.2.0
  2019-03              SA\#83     SP-190121   0052   1     F     Align the term mFIdList and constituentNSSIIdList                                                                 15.2.0
  2019-03              SA\#83     SP-190121   0053   1     F     Correct the definition of nSSIId                                                                                  15.2.0
  2019-03              SA\#83     SP-190121   0054   1     F     Add missing attribute constraint for class definition of NSSFFunction                                             15.2.0
  2019-03              SA\#83     SP-190121   0055   1     F     Correct attribute constraints for RRMpolicy related attributes in NRCellCU                                        15.2.0
  2019-03              SA\#83     SP-190121   0057   \-    F     Correct cardinality of End Point (EP) to target                                                                   15.2.0
  2019-03              SA\#83     SP-190121   0058   0     F     Correct Import table                                                                                              15.2.0
  2019-03              SA\#83     SP-190121   0059   \-    F     Remove ExternalNRCellCU.pLMNIdList                                                                                15.2.0
  2019-03              SA\#83     SP-190121   0060   \-    F     Use \'bS\' (not \'bs\') to prefix all BS (base station) attributes                                                15.2.0
  2019-03              SA\#83     SP-190121   0061   1     F     Correction of State attributes descriptions                                                                       15.2.0
  2019-03              SA\#83     SP-190121   0062   \-    F     Update 5G JSON Solution Set to align with generic NRM                                                             15.2.0
  2019-03              SA\#83     SP-190121   0063   1     F     Update YANG Solution Set to align with Stage 2 definition                                                         15.2.0
  2019-03              SA\#83     SP-190121   0064   1     F     Update Information Service to fix Network Slice modeling issue                                                    15.2.0
  2019-03              SA\#83     SP-190121   0065   1     F     Update Solution Set to fix Network Slice modeling issue                                                           15.2.0
  2019-03              SA\#83     SP-190121   0066   1     F     Add availability in service profile of network slice resource model                                               15.2.0
  2019-03              SA\#83     SP-190121   0068   1     F     Add sST attribute to ServiceProfile                                                                               15.2.0
  2019-03              SA\#83     SP-190121   0069   1     F     Update to sST attribute stage 3                                                                                   15.2.0
  2019-03              SA\#83     SP-190149   0073   2     F     Replace CoverageAreaTAList type definition                                                                        16.0.0
  2019-03              SA\#83     SP-190149   0074   1     F     Name datatypes SliceProfile and ServiceProfile                                                                    16.0.0
  2019-03              SA\#83     SP-190149   0075   1     F     Add datatype definition for S-NSSAI                                                                               16.0.0
  2019-03              SA\#83     SP-190149   0076   1     F     Remove incomplete description for TAC                                                                             16.0.0
  2019-03              SA\#83     SP-190149   0079   1     F     Name datatype RRMPolicyRatio2                                                                                     16.0.0
  2019-06              SA\#84     SP-190374   0083   \-    A     Remove attribute availabilityStatus in NRCellDU IOC                                                               16.1.0
  2019-06              SA\#84     SP-190373   0085   1     F     Correct the definition for nsInfo                                                                                 16.1.0
  2019-06              SA\#84     SP-190374   0088   1     A     Update Information Service of NR to fix unclear Note issue                                                        16.1.0
  2019-06              SA\#84     SP-190373   0096   2     A     Correct the use of plmnIdList                                                                                     16.1.0
  2019-06              SA\#84     SP-190373   0098   1     F     Add missing clauses to RRMPolicyRatio2 data type                                                                  16.1.0
  2019-06              SA\#84     SP-190373   0099   1     F     Update RRMPolicyRatio2 data type name in stage 3                                                                  16.1.0
  2019-06              SA\#84     SP-190373   0102   \-    F     Fix the implementation errors                                                                                     16.1.0
  2019-09              SA\#85     SP-190745   0089   2     B     Update 5GC Information Service to align with Managed Service Definition                                           16.2.0
  2019-09              SA\#85     SP-190743   0107   1     A     Correct description for NR deployment scenario                                                                    16.2.0
  2019-09              SA\#85     SP-190743   0109   1     A     Correct NR NRM model to be applicable for all NG-RAN architecture                                                 16.2.0
  2019-09              SA\#85     SP-190745   0114   1     C     Support NF Profile management                                                                                     16.2.0
  2019-09              SA\#85     SP-190743   0121   1     A     Clarification of sNSSAIList attribute                                                                             16.2.0
  2019-09              SA\#85     SP-190744   0123   \-    A     Remove pLMNId from GNBDUFunction                                                                                  16.2.0
  2019-09              SA\#85     SP-190743   0126   2     A     Update class definition with inheritance information                                                              16.2.0
  2019-09              SA\#85     SP-190743   0128   1     A     Correct description of NRCellCU and NRCellDU to be applicable for all deployment scenarios                        16.2.0
  2019-09              SA\#85     SP-190743   0130   \-    A     Correct XML solution set for NR                                                                                   16.2.0
  2019-09              SA\#85     SP-190743   0132   \-    A     Correct XML solution set for Network slice                                                                        16.2.0
  2019-09              SA\#85     SP-190750   0133   1     F     Clarification on slice model                                                                                      16.2.0
  2019-09              SA\#85     SP-190743   0142   1     A     Add YANG mount info                                                                                               16.2.0
  2019-09              SA\#85     SP-190743   0143   \-    A     Add YANG solution                                                                                                 16.2.0
  2019-09              SA\#85     SP-190745   0149   1     F     generate JSON definition for 5GC NRM based on new style guideline                                                 16.2.0
  2019-09              SA\#85     SP-190744   0150   1     A     Fix NR NRM to add missed ID info                                                                                  16.2.0
  2019-09              SA\#85     SP-190744   0152   \-    F     XML Solution Set for 5GC                                                                                          16.2.0
  2019-09              SA\#85     SP-190744   0154   \-    A     Correct ETSI NFV reference                                                                                        16.2.0
  2019-09              SA\#85     SP-190744   0157   1     A     generate JSON definition for Slice NRM based on new style guideline                                               16.2.0
  2019-09              SA\#85     SP-190744   0158   1     A     generate JSON definition for NR NRM based on new style guideline                                                  16.2.0
  2019-12              SA\#86     SP-191159   0146   3     F     To syn up with v1540 stage 2                                                                                      16.3.0
  2019-12              SA\#86     SP-191173   0156   2     A     Correct Import table                                                                                              16.3.0
  2019-12              SA\#86     SP-191166   0161   1     C     Extensions to PCF and UPF IOCs for support of TSC (Time Sensitive Communication)                                  16.3.0
  2019-12              SA\#86     SP-191166   0166   1     F     Correct XML solution set for NR                                                                                   16.3.0
  2019-12              SA\#86     SP-191166   0167   1     F     Correct Network slice NRM                                                                                         16.3.0
  2019-12              SA\#86     SP-191173   0168   2     A     Correct NR TAC attribute property                                                                                 16.3.0
  2019-12              SA\#86     SP-191173   0170   \-    A     Correction of the duplicated IOC NSSFFunction in daigram                                                          16.3.0
  2019-12              SA\#86     SP-191173   0172   \-    A     Correction of the wrong IOC names in transport view diagram\-\--Not implemented, wrong baseline (MCC)             16.3.0
  2019-12              SA\#86     SP-191166   0175   2     F     XML Solution Set for 5GC                                                                                          16.3.0
  2019-12              SA\#86     SP-191170   0177   3     C     Update on slice NRM                                                                                               16.3.0
  2019-12              SA\#86     SP-191170   0178   2     B     Add relation of GST and profiles                                                                                  16.3.0
  2019-12              SA\#86     SP-191166   0180   3     F     Update SEPP Stage 2 definition in 5GC NRM                                                                         16.3.0
  2019-12              SA\#86     SP-191166   0182   1     C     Add NEF Stage 2 definition in 5GC NRM                                                                             16.3.0
  2019-12              SA\#86     SP-191166   0184   1     C     Add SCP Stage 2 definition in 5GC NRM                                                                             16.3.0
  2019-12              SA\#86     SP-191166   0185   \-    C     Add Stage 3 definitions of 5GC NRM to align with stage 2                                                          16.3.0
  2019-12              SA\#86     SP-191166   0186   1     C     Support communication model in 5GC NF - Stage 2                                                                   16.3.0
  2019-12              SA\#86     SP-191166   0192   1     F     Fix merging errors of the specification                                                                           16.3.0
  2019-12              SA\#86     SP-191166   0195   \-    C     Add State Handling diagram for NF service                                                                         16.3.0
  2019-12              SA\#86     SP-191166   0197   \-    B     Updates to YANG SS                                                                                                16.3.0
  2019-12              SA\#86     SP-191170   0198   1     C     Update XML definitions of ServiceProfile NRM                                                                      16.3.0
  2019-12              SA\#86     SP-191170   0199   2     C     Update JSON definitions of ServiceProfile NRM                                                                     16.3.0
  2019-12              SA\#86     SP-191166   0200   1     C     Add managedNFProfile definition for ngc NRM - stage3                                                              16.3.0
  2019-12              SA\#86     SP-191166   0202   2     B     Add the RIM monitoring parameters for remote interference management                                              16.3.0
  2019-12              SA\#86     SP-191166   0212   2     F     Correct Network slice NRM                                                                                         16.3.0
  2019-12              SA\#86     SP-191166   0213   \-    F     Update SEPP Stage 3 definition in 5GC NRM                                                                         16.3.0
  2019-12              SA\#86     SP-191180   0222   2     B     Management of NR ANR, Stage 2                                                                                     16.3.0
  2019-12              SA\#86     SP-191180   0223   \-    B     Management of NR ANR, Stage 3                                                                                     16.3.0
  2019-12              SA\#86     SP-191173   0226   1     A     Add Stages 2 NRM Info Model definitions for beam managed object classes                                           16.3.0
  2019-12              SA\#86     SP-191173   0227   \-    A     Add Stages 2 NRM Info Model definitions for beam managed object classes                                           16.3.0
  2020-03              SA\#87E    SP-200169   0163   4     F     Correct the parameter sNSSAIList                                                                                  16.4.0
  2020-03              SA\#87E    SP-200169   0179   3     C     Update of RRM Policy                                                                                              16.4.0
  2020-03              SA\#87E    SP-200169   0235   \-    F     Correction of reference                                                                                           16.4.0
  2020-03              SA\#87E    SP-200169   0239   1     F     Update the NR NRM to align with NG-RAN overview architecture                                                      16.4.0
  2020-03              SA\#87E    SP-200169   0241   \-    F     Some correction on the NR NRM                                                                                     16.4.0
  2020-03              SA\#87E    SP-200169   0242   \-    F     Fix merging errors of the specification                                                                           16.4.0
  2020-03              SA\#87E    SP-200169   0243   1     F     Update NRM attribute definitions                                                                                  16.4.0
  2020-03              SA\#87E    SP-200233   0245   2     B     Add the RIM parameters for remote interference management                                                         16.4.0
  2020-03              SA\#87E    SP-200234   0248   1     F     Update on slice NRM and solution sets                                                                             16.4.0
  2020-03              SA\#87E    SP-200234   0250   1     F     Update of GNBCUUPFunction NRM                                                                                     16.4.0
  2020-03              SA\#87E    SP-200232   0253   2     B     Add Stage 3 NRM Info Model definitions for RRMPolicy and PLMNInfo related CRs                                     16.4.0
  2020-03              SA\#87E    SP-200178   0254   1     F     Correct CR implementation errors                                                                                  16.4.0
  2020-03              SA\#87E    SP-200235   0255   1     F     Add OpenAPI definitions required by the ProvMnS                                                                   16.4.0
  2020-03              SA\#87E    SP-200169   0258         F     Correct errors in yang solution set                                                                               16.4.0
  2020-03              SA\#87E                                   Correction of implementation errrors                                                                              16.4.1
  2020-06              SA\#88-e   SP-200489   0259   1     F     Update on the RRMpolicyRatio                                                                                      16.5.0
  2020-06              SA\#88-e   SP-200493   0260   \-    F     Replace DN with better identifier for whitelists and blacklists management                                        16.5.0
  2020-06              SA\#88-e   SP-200603   0261   1     B     Add IOC for control of QoS monitoring per QoS flow per UE                                                         16.5.0
  2020-06              SA\#88-e   SP-200604   0262   1     B     Add IOC for control of GTP-U path QoS monitoring                                                                  16.5.0
  2020-06              SA\#88-e   SP-200489   0263   1     F     Correction of reference                                                                                           16.5.0
  2020-06              SA\#88-e   SP-200493   0268   \-    B     ANR management for EN-DC architecture                                                                             16.5.0
  2020-06              SA\#88-e   SP-200484   0269   1     F     Clarification on network slice related identifiers                                                                16.5.0
  2020-06              SA\#88-e   SP-200484   0270   \-    F     Stage 3 update for clarification on network slice related identifiers                                             16.5.0
  2020-06              SA\#88-e   SP-200484   0274   1     F     Correct sNSSAI definition in XML solution set                                                                     16.5.0
  2020-06              SA\#88-e   SP-200484   0275   1     F     Clarify the NR NRM used for different deployment scenarios                                                        16.5.0
  2020-06              SA\#88-e   SP-200484   0278   \-    F     Add missing notification types to the definition of common notifications                                          16.5.0
  2020-06              SA\#88-e   SP-200491   0279   1     A     Update on NRCellDU                                                                                                16.5.0
  2020-06              SA\#88-e   SP-200491   0281   1     A     Update Clause 4.2.1.2 Inheritance UML diagram                                                                     16.5.0
  2020-06              SA\#88-e   SP-200490   0283   2     B     new NRM fragment to support RIM stage 2                                                                           16.5.0
  2020-06              SA\#88-e   SP-200490   0284   1     B     new NRM fragment to support RIM stage 3                                                                           16.5.0
  2020-06              SA\#88-e   SP-200489   0285   \-    F     Update stage 3 on the RRMpolicyRatio                                                                              16.5.0
  2020-06              SA\#88-e   SP-200605   0286   2     B     Add IOC for configurable 5QIs                                                                                     16.5.0
  2020-06              SA\#88-e   SP-200490   0287   1     B     Add IOC for 5QI to DSCP mapping                                                                                   16.5.0
  2020-06              SA\#88-e   SP-200493   0289   \-    B     Stage3 add the NRM fragment for SON management                                                                    16.5.0
  2020-06              SA\#88-e   SP-200493   0290   \-    B     ANR management for EN-DC architecture                                                                             16.5.0
  2020-06              SA\#88-e   SP-200493   0291   1     B     Add the NRM fragment for SON management                                                                           16.5.0
  2020-06              SA\#88-e   SP-200490   0293   \-    F     Add CommModelList NRM definition                                                                                  16.5.0
  2020-06              SA\#88-e   SP-200490   0294   1     F     Update NRM attribute definitions                                                                                  16.5.0
  2020-06              SA\#88-e   SP-200490   0295   1     F     Correct NRM definition in XML solution                                                                            16.5.0
  2020-06              SA\#88-e   SP-200485   0300   1     F     Clarification on the relation of GST, ServiceProfile and SliceProfile                                             16.5.0
  2020-06              SA\#88-e   SP-200496   0301   1     B     Add ES coverage relation in NRCellRelation                                                                        16.5.0
  2020-06              SA\#88-e   SP-200490   0302   \-    F     Update the decription for RRMPolicy\_ and resouceType                                                             16.5.0
  2020-06              SA\#88-e   SP-200490   0303   \-    F     Update definition for attribute localAddress in EP\_RP IOC                                                        16.5.0
  2020-06              SA\#88-e   SP-200486   0305   1     A     Correction of references                                                                                          16.5.0
  2020-06              SA\#88-e   SP-200485   0306   1     F     add transport information and slice mapping on backhaul endpoints                                                 16.5.0
  2020-06              SA\#88-e   SP-200485   0307   \-    F     add transport information and slice mapping on backhaul endpoints stage 3                                         16.5.0
  2020-06              SA\#88-e   SP-200490   0312   1     F     Update SliceProfile attributes solution 1                                                                         16.5.0
  2020-06              SA\#88-e   SP-200490   0315   1     B     Add configuredMaxTxEIRP on NRSectorCarrier                                                                        16.5.0
  2020-06              SA\#88-e   SP-200490   0316   \-    B     Stage 3 Add configuredMaxTxEIRP on NRSectorCarrier                                                                16.5.0
  2020-06              SA\#88-e   SP-200490   0318   \-    F     Update NRM YANG for 28.541                                                                                        16.5.0
  2020-06              SA\#88-e   SP-200496   0319   \-    B     Add ES coverage relation in NRCellRelation Stage 3                                                                16.5.0
  2020-06              SA\#88-e   SP-200612   0320   1     F     Update openAPI for NRCellRelation and NRFreqRelation                                                              16.5.0
  2020-09              SA\#89-e   SP-200729   0321   \-    F     Correction of NRM YANG errors                                                                                     16.6.0
  2020-09              SA\#89-e   SP-200729   0322   1     F     Correct on NR NRM                                                                                                 16.6.0
  2020-09              SA\#89-e   SP-200729   0323   \-    F     Correct the openAPI definition for NR NRM                                                                         16.6.0
  2020-09              SA\#89-e   SP-200730   0325   \-    A     Correct on frequency related IOC                                                                                  16.6.0
  2020-09              SA\#89-e   SP-200729   0329   1     B     Add IOC for predefined PCC rules                                                                                  16.6.0
  2020-09              SA\#89-e   SP-200729   0330   2     B     Add IOC for predefined PCC rules                                                                                  16.6.0
  2020-09              SA\#89-e   SP-200729   0331   \-    B     Enable PCF to support configurable 5QIs                                                                           16.6.0
  2020-09              SA\#89-e   SP-200729   0332   \-    B     Add IOC for dynamic 5QIs - stage 2                                                                                16.6.0
  2020-09              SA\#89-e   SP-200729   0333   \-    B     Add IOC for dynamic 5QIs - stage 3                                                                                16.6.0
  2020-09              SA\#89-e   SP-200729   0334   \-    B     Add TCE mapping info in GNBCUCPFunction                                                                           16.6.0
  2020-09              SA\#89-e   SP-200729   0335   \-    B     Add TCE mapping info in openAPI solution                                                                          16.6.0
  2020-09              SA\#89-e   SP-200729   0336   \-    F     Add missing definitions for perfReq                                                                               16.6.0
  2020-09              SA\#89-e   SP-200754   0338   1     F     Delete supportedAccessTech to align with GST                                                                      16.6.0
  2020-09              SA\#89-e   SP-200724   0339   \-    F     Correction on duplicated annex numbering                                                                          16.6.0
  2020-09              SA\#89-e   SP-200729   0345   \-    F     Update NRM attribute definitions                                                                                  16.6.0
  2020-09              SA\#89-e   SP-200749   0362   \-    F     Deleting SupportedAccessTech - Stage 3 - XML                                                                      16.6.0
  2020-09              SA\#89-e   SP-200724   0368   1     F     Add relation between transport and application level endpoints                                                    16.6.0
  2020-09              SA\#89-e   SP-200724   0369   \-    F     Add relation between transport and application level endpoints stage 3                                            16.6.0
  2020-09              SA\#89-e   SP-200729   0370   1     F     Cleanup stage 2 editorial issue and stage 3 yaml error                                                            16.6.0
  2020-09              SA\#89-e   SP-200749   0371   \-    F     Add clarifying note to ServiceProfile                                                                             16.6.0
  2020-11                                                        No technical changes, cleanup of watermarks, hidden text and custom XMl, etc                                      16.6.1
  2020-11                                                        Some code was changed by mistake in the previous version. These changes have been reverted.                       16.6.2
  2020-12              SA\#90e    SP-201057   0377   \-    F     Correction of NRM YANG errors                                                                                     16.7.0
  2020-12              SA\#90e    SP-201045   0378   \-    F     Add subclause reference of MRO related attribute                                                                  16.7.0
  2020-12              SA\#90e    SP-201057   0379   \-    F     Correct the definition for configurable5QI and dynamic5QI                                                         16.7.0
  2020-12              SA\#90e    SP-201045   0381   1     F     Change RACH control attributes from beam to cell                                                                  16.7.0
  2020-12              SA\#90e    SP-201045   0383   1     F     Move Distributed RACH control IOC from CU to DU                                                                   16.7.0
  2020-12              SA\#90e    SP-201045   0385   2     F     Move Distributed PCI control IOC from DU to CU                                                                    16.7.0
  2020-12              SA\#90e    SP-201057   0389   \-    F     Correction of cell neighbour relations related attributes in openAPI solution                                     16.7.0
  2020-12              SA\#90e    SP-201057   0394   1     F     Correct Network slice NRM                                                                                         16.7.0
  2020-12              SA\#90e    SP-201050   0398   \-    F     Add containment relationship for network slice IOCs                                                               16.7.0
  2020-12              SA\#90e    SP-201050   0400   \-    F     Add containment relationship for network slice IOCs stage 3                                                       16.7.0
  2020-12              SA\#90e    SP-201053   0408   \-    F     Fix description related to service profile                                                                        16.7.0
  2020-12              SA\#90e    SP-201089   0409   1     F     Correction of NRM YANG errors                                                                                     16.7.0
  2020-12              SA\#90e    SP-201089   0411   \-    F     YANG improvements                                                                                                 16.7.0
  2020-12              SA\#90e    SP-201056   0413   \-    F     Add serviceProfileId and sliceProfileId to stage 3 yaml                                                           16.7.0
  2020-12              SA\#90e    SP-201089   0418   \-    F     Update notifyThresholdCrossing to be a common notification.                                                       16.7.0
  2020-12              SA\#90e    SP-201089   0420   \-    F     pLMNInfoList faulty attribute definition                                                                          16.7.0
  2020-12              SA\#90e    SP-201089   0422   \-    F     Fix containment relationship for EP\_Transport IOC                                                                16.7.0
  2021-03              SA\#91e    SP-210153   0429   4     F     Correction of ServiceProfile attributes                                                                           16.8.0
  2021-03              SA\#91e    SP-210153   0431   1     F     Correction on Dynamic5QISet IOC based on LS reply from SA2                                                        16.8.0
  2021-03              SA\#91e    SP-210154   0434   3     F     Correct the NF name in definition of EP\_NgU                                                                      16.8.0
  2021-03              SA\#91e    SP-210153   0439   \-    F     Add missing inheritance description information in the attribute definition for several IOCs                      16.8.0
  2021-03              SA\#91e    SP-210153   0441   2     F     Correct multiplicity issue for several attributes of NR NRM                                                       16.8.0
  2021-03              SA\#91e    SP-210146   0444   2     F     Fix containment relationship for EP\_Transport IOC                                                                16.8.0
  2021-03              SA\#91e    SP-210143   0460   1     F     Update of the PCI and DESManagementFunction                                                                       16.8.0
  2021-03              SA\#91e    SP-210154   0466   1     A     Correction to NSI and NSSI state management                                                                       16.8.0
  2021-03              SA\#91e    SP-210143   0471   \-    F     YANG compilation error and missing stage 2 corrections                                                            16.8.0
  2021-03              SA\#91e    SP-210146   0473   \-    F     Fix compilation and other errors                                                                                  16.8.0
  2021-06              SA\#92e    SP-210411   0477   \-    F     Yang Corrections of implementation errors                                                                         16.9.0
  2021-06              SA\#92e    SP-210411   0489   \-    F     Correct the description for GNBDUFunction and EP\_NgC                                                             16.9.0
  2021-06              SA\#92e    SP-210406   0500   1     F     Fix editorial issue of network slice NRM                                                                          16.9.0
  2021-06              SA\#92e    SP-210406   0502   1     F     fix inheritance relation of network slice NRM                                                                     16.9.0
  2021-06              SA\#92e    SP-210411   0509   \-    F     Correct inconsistencies in definitions around network slice management                                            16.9.0
  2021-06              SA\#92e    SP-210406   0513   1     F     Correction to definition for domain centralized SON                                                               16.9.0
  2021-06              SA\#92e    SP-210590   0516   \-    F     Fix conflict of stage 3 OpenAPI code                                                                              16.9.0
  2021-09              SA\#93e    SP-210871   0517               YANG NR-NRM model structure repair and cleanup                                                                    16.10.0
  2021-09              SA\#93e    SP-210885   0521   \-    F     Deprecate Top-Attr and use Top instead                                                                            16.10.0
  2021-09              SA\#93e    SP-210885   0523   \-    F     Fix incorrect attributes inheritance description                                                                  16.10.0
  2021-09              SA\#93e    SP-210871   0529   \-    F     Remove the attribute definition which is not used                                                                 16.10.0
  2021-09              SA\#93e    SP-210871   0533   1     F     Fix the issue caused by the updated NetworkSliceSubnet inheritence relationship                                   16.10.0
  2021-09              SA\#93e    SP-210871   0544   \-    F     Correction for attribute description of servAttrCom                                                               16.10.0
  2021-09              SA\#93e    SP-210871   0546   \-    F     Correction of YAML references                                                                                     16.10.0
  2021-09              SA\#93e    SP-210885   0552   \-    F     Remove isINEF attribute from NEFFunction IOC                                                                      16.10.0
  2021-09              SA\#93e    SP-210871   0553   \-    F     YANG updates to correct YANG merging problems                                                                     16.10.0
  2021-09              SA\#93e    SP-210871   0561   \-    F     Moving RIM monitoring related attributes to NRCellDU                                                              16.10.0
  2021-09              SA\#93e    SP-210885   0565   1     F     Fix inconsistent clauses and attributes used in TS 38.211 and TS 28.541                                           16.10.0
  2021-12              SA\#94e    SP-211472   0570   \-    F     Align different (abbreviated) names for support qualifier to S                                                    16.11.0
  2021-12              SA\#94e    SP-211454   0572   1     F     Correct Class diagram of AMF Region/AMF Set and stage 3 implementation                                            16.11.0
  2021-12              SA\#94e    SP-211454   0574   1     F     Clarify the usage of pLMNId in first entry in pLMNInfoList                                                        16.11.0
  2021-12              SA\#94e    SP-211454   0588   1     F     cNSIId description clarification                                                                                  16.11.0
  2021-12              SA\#94e    SP-211462   0594   1     F     DMRO correction                                                                                                   16.11.0
  2021-12              SA\#94e    SP-211454   0603   \-    F     Correct PLMNInfo support qualifier                                                                                16.11.0
  2021-12              SA\#94e    SP-211464   0605   1     F     Clarify tenant relationship with ServiceProfileId                                                                 16.11.0
  2021-12              SA\#94e    SP-211475   0620   \-    F     Correct the wrong reference for TS 32.160                                                                         16.11.0
  2021-12              SA\#94e    SP-211472   0623   \-    F     Rel-16 Fix stage3 definition for plmnId                                                                           16.11.0
  2021-12              SA\#94e    SP-211472   0640   \-    F     Correct spelling of Attribute properties                                                                          16.11.0
  2022-03              SA\#95e    SP-220179   0654   \-    F     Remove incorrect reference to TS 22.104                                                                           16.12.0
  2022-03              SA\#95e    SP-220179   0677   \-    F     Correct YANG mapping in TS document                                                                               16.12.0
  2022-03              SA\#95e                                   Correct document header and History table                                                                         16.12.1
  2022-03              SA\#95e                                   Removal of comments in the document                                                                               16.12.2
  2022-06              SA\#96     SP-220497   0684   \-    F     Diagram fix for NRM fragment for RRM policies                                                                     16.13.0
  2022-06              SA\#96     SP-220497   0686   \-    F     Fixing OpenAPI Discoverability issue in stage 3-5gcNrm.yaml                                                       16.13.0
  2022-06              SA\#96     SP-220497   0687   \-    F     Fixing OpenAPI Discoverability issue in stage 3- nrNrm.yaml                                                       16.13.0
  2022-06              SA\#96     SP-220497   0688   \-    F     Fixing OpenAPI Discoverability issue in Stage3-sliceNrm.yaml                                                      16.13.0
  2022-06              SA\#96     SP-220498   0692   \-    F     CT OpenAPI file relative-path URI references and dependence change for 5gcNrm.yaml                                16.13.0
  2022-06              SA\#96     SP-220498   0695   1     F     OpenAPI file name and dependence change for 5gcNrm.yaml                                                           16.13.0
  2022-06              SA\#96     SP-220498   0696   1     F     OpenAPI file name and dependence change for nrNrm.yaml                                                            16.13.0
  2022-06              SA\#96     SP-220498   0697   1     F     OpenAPI file name and dependence change for sliceNrm.yaml                                                         16.13.0
  2022-06              SA\#96     SP-220498   0701   \-    F     Correction to RRMPolicy\_ IOC reference in RRMPolicyRatio IOC                                                     16.13.0
  2022-06              SA\#96     SP-220498   0703   \-    F     Add attribute properties for NetworkSliceSubnet attribute priorityLabel                                           16.13.0
  2022-06              SA\#96     SP-220498   0709   1     F     Correct isOrdered-isUnique for multivalue attributes                                                              16.13.0
  2022-06              SA\#96     SP-220510   0718   \-    F     Correction on minor errors in nrNRM.yaml                                                                          16.13.0
  2022-06              SA\#96     SP-220510   0720   \-    F     Correction on the attribution definition in the wrong yaml file                                                   16.13.0
  2022-06              SA\#96     SP-220510   0726         F     Fix BWP association in NRCellDU                                                                                   16.13.0
  2022-06              SA\#96     SP-220510   0728   \-    F     Update 5QI set reference attribute definition                                                                     16.13.0
  2022-06              SA\#96     SP-220510   0730   \-    F     Update 5QI set description - YANG module                                                                          16.13.0
  2023-01              SA\#98e    SP-221169   0794   1     F     Correcting name of nSInstanceId                                                                                   16.14.0
  2023-01              SA\#98e    SP-221169   0801   2     F     Correction to multiplicity of relation between NetworkSlice IOC and NetworkSliceSubnet IOC                        16.14.0
  2023-01              SA\#98e    SP-221169   0804   \-    F     Correction to GSMA NG 116 reference for KPIMonitoring                                                             16.14.0
  2023-01              SA\#98e    SP-221169   0807   \-    F     Correction to ServiceProfile attribute v2XCommModels name in YAML defintion                                       16.14.0
  2023-01              SA\#98e    SP-221169   0810   \-    F     Correction to inconsistencies in GNBCUCPFunction definition                                                       16.14.0
  2023-01              SA\#98e    SP-221173   0814   1     A     Adding YANG begin and End markers                                                                                 16.14.0
  2023-01              SA\#98e    SP-221182   0836   \-    F     Consistency in use of servAttrCom \--\> non implemented, CR incorrect                                             16.14.0
  2023-01              SA\#98e    SP-221182   0839   1     F     Correct kPIList                                                                                                   16.14.0
  2023-01              SA\#98e    SP-221182   0842   2     F     Correct periodicityList                                                                                           16.14.0
  2023-01              SA\#98e                                   Adding a return in annex E.5.7 (implementation mistake)                                                           16.14.1
  2023-03              SA\#99     SP-230199   0865   \-    F     Remove redundant stage 3 definition for Mnc and PlmnId                                                            16.15.0
  2023-03              SA\#99     SP-230200   0879   1     A     Clarify Monut information clauses                                                                                 16.15.0
  2023-04              SA\#99                                    Adding missing YAML files in the zip                                                                              16.15.1
  2023-05              SA\#99                                    Fixing Foreword clause title                                                                                      16.15.2
  2023-06              SA\#100    SP-230648   0901   1     F     Correction to multiplicity definition to nRPciList and stage 3 implementation of both NRPciList and CSonPciList   16.16.0
  2023-06              SA\#100    SP-230648   0906   1     F     Clean up of incorrect use of multiplicity isOrdered isUnique and isNullable in attribute properties table         16.16.0
  2023-09              SA\#101    SP-230964   0940   1     F     Correct attribute name for indication of v2XCommMode                                                              16.17.0
  2023-09              SA\#101    SP-230964   0948   1     F     Update Annex L with mapping table                                                                                 16.17.0
  2023-09              SA\#101    SP-230941   0953   1     F     Correction to type defintion of coverageAreaTAList                                                                16.17.0
  2023-09              SA\#101    SP-230941   0967   1     F     Removing redundant Tai definition in NR NRM                                                                       16.17.0
  2023-09              SA\#101    SP-230941   0971   1     F     Fix small inconsistent issues in stage2, typo in stage 2 and 3                                                    16.17.0
  2023-09              SA\#101    SP-230941   0974   2     F     Fix a few inheritance diagram issues in NR NRM                                                                    16.17.0
  2023-09              SA\#101    SP-230941   0977   1     F     Update RRMPolicyRatio                                                                                             16.17.0
  2023-09              SA\#101    SP-230941   0982   \-    F     Remove duplicated notifications                                                                                   16.17.0
  2023-09              SA\#101    SP-230958   0987   1     F     Correct the issues for the attribute with the ENUM type for network slicing NRM fragment                          16.17.0
  2023-09              SA\#101    SP-230941   0995   1     F     Correction on DeterministicComm data type                                                                         16.17.0
  -------------------- ---------- ----------- ------ ----- ----- ----------------------------------------------------------------------------------------------------------------- -------------
