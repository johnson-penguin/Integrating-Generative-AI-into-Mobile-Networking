######## Annex A (normative): Cell state handling 

A.1 Relation between the administrative state and the \"Pre-operation state of the gNB-DU Cell\"
================================================================================================

The administrative state indicates the permission to use or prohibition
against using the cell, imposed through the OAM services. The
administrative state has three values: \"LOCKED\", \"SHUTTING DOWN\" or
\"UNLOCKED\"

The meanings of these values are defined in Recommendation ITU‑T X.731
\[18\].

The relation between the administrative state and the \"Pre-operation
state of the gNB-DU Cell\" is defined in subclause 8.5 of 3GPP TS 38.401
\[4\]. See below an extract from subclause 8.5 of TS 38.401 \[4\] on the
F1 startup and cell activation.

If the operationalState is \"ENABLED\" (i.e. the resource is physically
installed and working) and if the administrativeState is \"UNLOCKED\",
the step \"0: Pre-operational state\" will exit and the step \"1: F1
Setup Request\" will be executed.\"

##### 8.5 F1 Startup and cells activation {#f1-startup-and-cells-activation .H6}

This function allows to setup the F1 interface between a gNB-DU and a
gNB-CU and it allows to activate the gNB-DU cells.

Figure 8.5-1: F1 startup and cell activation

A.2 Combined state diagram for gNB cell
=======================================

This is the Combined state diagram for gNB cell.

![](media/image2.png){width="6.695138888888889in" height="4.425in"}

Figure A.2-: Combined gNB cell state diagram

The gNB-DU maintains cell states. The following table is the gNB cell
state transition table.

In 3-split and 2-split deployment scenarios, the interactions between
gNB-CU and gNB-DU are standardized. The interactions specified under the
column \"The state transition events and actions\" of \"The gNB Cell
state transition table\" below shall be present for the state
transition.

In the non-split deployment scenarios, the interactions between gNB-CU
and gNB-DU are not standardized. The interactions between gNB-CU and
gNB-DU specified under the column \"The state transition events and
actions\" of \"The gNB Cell state transition table\" can be replaced by
other means that is not standardized.

Table A.2-1: The gNB Cell state transition table

+-------------------+-------------------------------------------------+
| Transition number | The state transition event and actions          |
+===================+=================================================+
| 1                 | Event: Receive request to unlock.               |
|                   |                                                 |
|                   | Action: None.                                   |
+-------------------+-------------------------------------------------+
| 2                 | Event: Receive request to lock.                 |
|                   |                                                 |
|                   | Action: None.                                   |
+-------------------+-------------------------------------------------+
| 2a                | Event: Receive request to lock                  |
|                   |                                                 |
|                   | Action: Send to gNB-CU the \"gNB-DU             |
|                   | Configuration Update message\" with served cell |
|                   | to delete.                                      |
+-------------------+-------------------------------------------------+
| 3                 | Event: When the required cell resource is       |
|                   | physically installed and working.               |
|                   |                                                 |
|                   | Action: none.                                   |
+-------------------+-------------------------------------------------+
| 4                 | Event: When the required cell resource is not   |
|                   | physically installed or is not working.         |
|                   |                                                 |
|                   | Action: Send to gNB-CU the \"gNB-DU             |
|                   | Configuration update message\" with cell to     |
|                   | delete.                                         |
+-------------------+-------------------------------------------------+
| 4a                | Event: When the required cell resource is       |
|                   | physically uninstalled or is not working.       |
|                   |                                                 |
|                   | Action: Send to gNB-CU the \"GNB-DU             |
|                   | Configuration Update message\" with served cell |
|                   | to delete.                                      |
+-------------------+-------------------------------------------------+
| 5                 | Event: Receive from gNB-CU the \"F1 Setup       |
|                   | Response message\" (identifying the cell to be  |
|                   | activated).                                     |
|                   |                                                 |
|                   | The cell is activated successfully.             |
|                   |                                                 |
|                   | Actions: Do nothing or send gNB-CU the \"gNB-DU |
|                   | Configuration Update message\" with Cell stated |
|                   | as active\'                                     |
|                   |                                                 |
|                   | \-\-\-\-- or \-\-\-\--                          |
|                   |                                                 |
|                   | Event: Receive from gNB-CU the \"gNB-CU         |
|                   | Configuration Update message\" (identifying     |
|                   | cell to be activated e.g., in case that the     |
|                   | cell was not activated using the \"F1 Setup     |
|                   | Response message\").                            |
|                   |                                                 |
|                   | Actions:                                        |
|                   |                                                 |
|                   | The cell is activated successfully.             |
|                   |                                                 |
|                   | Send to gNB-CU the \"gNB-CU Configuration       |
|                   | Update Response\" to confirm the cell is in     |
|                   | active state.                                   |
|                   |                                                 |
|                   | \-\-\-\-- or \-\-\-\--                          |
|                   |                                                 |
|                   | Event: Receive from gNB-CU the \"gNB-DU         |
|                   | Configuration Update Acknowledge message\"      |
|                   | (identifying cell to be activated e.g., in case |
|                   | that the cell was not activated using the \"F1  |
|                   | Setup Response message\") and                   |
|                   |                                                 |
|                   | the cell is activated successfully              |
|                   |                                                 |
|                   | Actions: Do nothing.                            |
+-------------------+-------------------------------------------------+
| 6                 | Event: Receive from gNB-CU the \"gNB-CU         |
|                   | Configuration Update message\" and responds     |
|                   | with gNB-CU Configuration Update Acknowledge    |
|                   | messages.                                       |
|                   |                                                 |
|                   | Actions: Respond with gNB-CU Configuration      |
|                   | Update Acknowledge messages.                    |
|                   |                                                 |
|                   | \-\-\-\-- or \-\-\-\--                          |
|                   |                                                 |
|                   | Event: Event: DU experiences an internal        |
|                   | failure and decided to place the cell into      |
|                   | inactive state.                                 |
|                   |                                                 |
|                   | Actions: Send to gNB-CU the \"gNB-DU Cell       |
|                   | status Update message\"                         |
+-------------------+-------------------------------------------------+
| 7                 | Event: Send to gNB-CU the \"F1 Setup request\"  |
|                   | (identifying the cell that is configured and    |
|                   | ready to be activated).                         |
|                   |                                                 |
|                   | Actions: none.                                  |
|                   |                                                 |
|                   | \-\-\-\-- or \-\-\-\--                          |
|                   |                                                 |
|                   | Send to gNB-CU the \"gNB-DU Configuration       |
|                   | Update message\" with the served cell to add.   |
|                   |                                                 |
|                   | Actions: none.                                  |
+-------------------+-------------------------------------------------+
| 8                 | Event: Sends to gNB-CU the \"gNB-DU             |
|                   | Configuration Update message\" with served cell |
|                   | to delete. Receive response from gNB-CU the     |
|                   | \"gNB-DU Configuration Update Acknowledge       |
|                   | message\".                                      |
|                   |                                                 |
|                   | Actions: None.                                  |
+-------------------+-------------------------------------------------+
| 9                 | Event: Receive request to shut down.            |
|                   |                                                 |
|                   | Actions: None.                                  |
+-------------------+-------------------------------------------------+
| 10                | Event: Last user quit.                          |
|                   |                                                 |
|                   | Actions: Send to gNB-CU the \"GNB-DU            |
|                   | Configuration Update message\" with served cell |
|                   | to delete.                                      |
+-------------------+-------------------------------------------------+
| 11                | Event: When a cell is created and is            |
|                   | configured.                                     |
|                   |                                                 |
|                   | Actions: None                                   |
+-------------------+-------------------------------------------------+
| 12                | Event: When a cell is deleted.                  |
|                   |                                                 |
|                   | Action: None.                                   |
+-------------------+-------------------------------------------------+

########  Annex B (normative): NSI and NSSI state handling

B.1 NSI state handling
======================

An NetworkSlice Instance (NSI) is a logical object in the management
system that represents a complex grouping of resources that may be in
various states. At any time, the management system needs to know the
state of an NSI.

The Recommendation ITU-T X.731 \[18\], to which \[17\] refers, has
defined the inter-relation between the administrative state, operational
state of systems in general.

Figure B.1-1: Combined NSI state diagram

The interactions specified under the column \"The state transition
events and actions\" of \"NSI state transition table\" below shall be
present for the state transition.

Table B.1-1: The NSI state transition table

+----------------+----------------------------------------------------+
| Trigger number | The state transition events and actions            |
+================+====================================================+
| 0              | Operation allocateNsi results in the creation of   |
|                | NSI. The administrative state is set to LOCKED and |
|                | operationalState is set to DISABLED                |
|                |                                                    |
|                | \-- or --                                          |
|                |                                                    |
|                | CM operation creates NSI. The administrative state |
|                | is set to LOCKED and operationalState is set to    |
|                | DISABLED                                           |
+----------------+----------------------------------------------------+
| 1              | CM operation sets administrative state to          |
|                | UNLOCKED.                                          |
+----------------+----------------------------------------------------+
| 2              | CM operation sets administrative state to LOCKED   |
+----------------+----------------------------------------------------+
| 2a             | CM operation sets administrative state to SHUTTING |
|                | DOWN                                               |
+----------------+----------------------------------------------------+
| 2b             | The last user of the NSInetwork slice stops using  |
|                | the NSInetwork slice                               |
+----------------+----------------------------------------------------+
| 3              | The related NSSI (identified by                    |
|                | NetworkSlice.networkSliceSubnetRef) changes state  |
|                | to UNLOCKED and ENABLED                            |
+----------------+----------------------------------------------------+
| 4              | The related NSSI (identified by                    |
|                | NetworkSlice.networkSliceSubnetRef) changes state  |
|                | to LOCKED                                          |
|                |                                                    |
|                | \-- or --                                          |
|                |                                                    |
|                | The related NSSI (identified by                    |
|                | NetworkSlice.networkSliceSubnetRef) changes state  |
|                | to DISABLED                                        |
+----------------+----------------------------------------------------+
| 5              | Operation deallocateNsi results in the deletion of |
|                | NSI                                                |
|                |                                                    |
|                | \-- or --                                          |
|                |                                                    |
|                | CM operation deletes NSI                           |
+----------------+----------------------------------------------------+

B.2 State handling of NSSI
==========================

A NetworkSliceSubnet Instance (NSSI) is a logical object in the
management system that represents a complex grouping of resources that
may be in various states. At any time the management system needs to
know the state of an NSSI.

The Recommendation ITU-T X.731 \[18\], to which \[17\] refers, has
defined the inter-relation between the administrative state, operational
state of systems in general.

Figure B.2-1: Combined NSSI state diagram

The interactions specified under the column \"The state transition
events and actions\" of \"NSSI state transition table\" below shall be
present for the state transition.

Table B.2-1: The NSSI state transition table

+----------------+----------------------------------------------------+
| Trigger number | The state transition events and actions            |
+================+====================================================+
| 0              | Operation allocateNssi results in the creation of  |
|                | NSSI. The administrative state is set to LOCKED    |
|                | and operationalState is set to DISABLED            |
|                |                                                    |
|                | \-- or --                                          |
|                |                                                    |
|                | CM operation creates NSSI. The administrative      |
|                | state is set to LOCKED and operationalState is set |
|                | to DISABLED                                        |
+----------------+----------------------------------------------------+
| 1              | CM operation sets administrative state to          |
|                | UNLOCKED.                                          |
+----------------+----------------------------------------------------+
| 2              | CM operation sets administrative state to LOCKED   |
+----------------+----------------------------------------------------+
| 2a             | CM operation sets administrative state to SHUTTING |
|                | DOWN                                               |
+----------------+----------------------------------------------------+
| 2b             | The last user of the NSSInetwork slice subnet      |
|                | stops using the NSSInetwork slice subnet           |
+----------------+----------------------------------------------------+
| 3              | All constituent NSSIs (identified by               |
|                | NetworkSliceSubnet.networkSliceSubnetRef) change   |
|                | state to UNLOCKED and ENABLED                      |
+----------------+----------------------------------------------------+
| 4              | At least one constituent NSSI (identified by       |
|                | NetworkSliceSubnet.networkSliceSubnetRef) changes  |
|                | state to LOCKED                                    |
|                |                                                    |
|                | \-- or --                                          |
|                |                                                    |
|                | At least one constituent NSSI (identified by       |
|                | NetworkSliceSubnet.networkSliceSubnetRef) changes  |
|                | state to DISABLED                                  |
+----------------+----------------------------------------------------+
| 5              | Operation deallocateNssi results in the deletion   |
|                | of NSSI                                            |
|                |                                                    |
|                | \-- or --                                          |
|                |                                                    |
|                | CM operation deletes NSSI                          |
+----------------+----------------------------------------------------+

########  Annex C (normative): XML definitions for NR NRM

C.1 General
===========

This annex contains the XML definitions for the NR and NG-RAN NRM, in
accordance with NR and NG-RAN NRM Information Model definitions
specified in clause 4.

C.2 Architectural features
==========================

The overall architectural feature of NR NRM information model is
specified in clause 4, this clause specifies features that are specific
to the Schema definitions.

The XML definitions of the present document specify the schema for a
configuration content, which can be included in a configuration file for
Bulk configuration management operations

C.3 Mapping
===========

C.3.1 General mapping
---------------------

An IOC maps to an XML element of the same name as the IOC\'s name in the
Information Model. An IOC attribute maps to a sub-element of the
corresponding IOC\'s XML element, and the name of this sub-element is
the same as the attribute\'s name in the Information Model.

C.3.2 Information Object Class (IOC) mapping
--------------------------------------------

The mapping is not present in the current version of the present
document.

C.4 Solution Set definitions
============================

C.4.1 XML definition structure
------------------------------

The overall description of the file format of configuration data XML
files is provided by 3GPP TS 32.616 \[33\].

The present document defines the NRM-specific XML schema nrNrm.xsd for
the NR NRM Information Model defined in clause 4.

XML schema nrNrm.xsd explicitly declares NRM-specific XML element types
for the related NRM.

The definition of those NRM-specific XML element types complies with the
generic mapping rules defined in 3GPP TS 32.616 \[33\].

C.4.2 Graphical representation
------------------------------

The graphical representation is not present in the current version of
the present document.

C.4.3 XML schema \"nRNrm.xsd\"
------------------------------

\<?xml version=\"1.0\" encoding=\"UTF-8\"?\>

\<!\--

3GPP TS 28.541 NR Network Resource Model

XML schema definition

nrNrm.xsd

\--\>

\<schema xmlns=\"http://www.w3.org/2001/XMLSchema\"

xmlns:xn=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.623\#genericNrm\"

xmlns:nn=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.541\#nrNrm\"

xmlns:en=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.659\#eutranNrm\"

xmlns:epc=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.709\#epcNrm\"

xmlns:sm=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.626\#stateManagementIRP\"

xmlns:ngc=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.541\#ngcNrm\"

xmlns:sp=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.629\#sonPolicyNrm\"

targetNamespace=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.541\#nrNrm\"
elementFormDefault=\"qualified\"\>

\<import
namespace=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.623\#genericNrm\"/\>

\<import
namespace=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.709\#epcNrm\"/\>

\<import
namespace=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.626\#stateManagementIRP\"/\>

\<import
namespace=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.541\#ngcNrm\"/\>

\<import
namespace=\"http://www.3gpp.org/ftp/specs/archive/28\_series/28.629\#sonPolicyNrm\"/\>

\<simpleType name=\"GnbId\"\>

\<restriction base=\"unsignedLong\"\>

\<maxInclusive value=\"4294967295\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"GnbIdLength\"\>

\<restriction base=\"integer\"\>

\<minLength value=\"22\"/\>

\<maxLength value=\"32\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"Nci\"\>

\<restriction base=\"unsignedLong\"\>

\<maxInclusive value=\"68719476735\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"Pci\"\>

\<restriction base=\"unsignedShort\"\>

\<maxInclusive value=\"503\"/\>

\<!\-- Minimum value is 0, maximum value is 3x167+2=503 \--\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"NrTac\"\>

\<restriction base=\"unsignedLong\"\>

\<maxInclusive value=\"16777215\"/\>

\<!\--5G TAC is 3-octets length \--\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"GnbDuId\"\>

\<restriction base=\"unsignedLong\"\>

\<maxInclusive value=\"68719476735\"/\>

\<!\-- Minimum value is 0, maximum value is 2\^36-1=68719476735 \--\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"GnbCuupId\"\>

\<restriction base=\"unsignedLong\"\>

\<maxInclusive value=\"68719476735\"/\>

\<!\-- Minimum value is 0, maximum value is 2\^36-1=68719476735 \--\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"GnbName\"\>

\<restriction base=\"string\"\>

\<minLength value=\"1\"/\>

\<maxLength value=\"150\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"CyclicPrefix\"\>

\<restriction base=\"integer\"\>

\<enumeration value=\"15\"/\>

\<enumeration value=\"30\"/\>

\<enumeration value=\"60\"/\>

\<enumeration value=\"120\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"QuotaType\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"STRICT\"/\>

\<enumeration value=\"FLOAT\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"CellState\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"IDLE\"/\>

\<enumeration value=\"INACTIVE\"/\>

\<enumeration value=\"ACTIVE\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"BwpContext\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"DL\"/\>

\<enumeration value=\"UL\"/\>

\<enumeration value=\"SUL\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"IsInitialBwp\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"INITIAL\"/\>

\<enumeration value=\"OTHER\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"qOffsetRangeList\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"dB-24\"/\>

\<enumeration value=\"dB-22\"/\>

\<enumeration value=\"dB-20\"/\>

\<enumeration value=\"dB-18\"/\>

\<enumeration value=\"dB-16\"/\>

\<enumeration value=\"dB-14\"/\>

\<enumeration value=\"dB-12\"/\>

\<enumeration value=\"dB-10\"/\>

\<enumeration value=\"dB-8\"/\>

\<enumeration value=\"dB-6\"/\>

\<enumeration value=\"dB-5\"/\>

\<enumeration value=\"dB-4\"/\>

\<enumeration value=\"dB-3\"/\>

\<enumeration value=\"dB-2\"/\>

\<enumeration value=\"dB-1\"/\>

\<enumeration value=\"dB0\"/\>

\<enumeration value=\"dB1\"/\>

\<enumeration value=\"dB2\"/\>

\<enumeration value=\"dB3\"/\>

\<enumeration value=\"dB4\"/\>

\<enumeration value=\"dB5\"/\>

\<enumeration value=\"dB6\"/\>

\<enumeration value=\"dB8\"/\>

\<enumeration value=\"dB10\"/\>

\<enumeration value=\"dB12\"/\>

\<enumeration value=\"dB14\"/\>

\<enumeration value=\"dB16\"/\>

\<enumeration value=\"dB18\"/\>

\<enumeration value=\"dB20\"/\>

\<enumeration value=\"dB22\"/\>

\<enumeration value=\"dB24\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"isESCoveredBy\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"NO\"/\>

\<enumeration value=\"PARTIAL\"/\>

\<enumeration value=\"FULL\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"cellReselectionPriority\"\>

\<restriction base=\"unsignedLong\"\>

\<minInclusive value=\"0\"/\>

\<maxInclusive value=\"16\"/\>

\<!\--Value 0 means lowest priority\--\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"cellReselectionSubPriority\"\>

\<restriction base=\"unsignedLong\"\>

\<minInclusive value=\"0\"/\>

\<maxInclusive value=\"16\"/\>

\<!\--Value 0 means lowest priority\--\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"PMaxRangeType\"\>

\<restriction base=\"short\"\>

\<minInclusive value=\"-30\"/\>

\<maxInclusive value=\"33\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"qOffsetFreq\"\>

\<restriction base=\"short\"\>

\<minInclusive value=\"-24\"/\>

\<maxInclusive value=\"24\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"qQualMin\"\>

\<restriction base=\"integer\"\>

\<minInclusive value=\"-34\"/\>

\<maxInclusive value=\"0\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"qRxLevMin\"\>

\<restriction base=\"integer\"\>

\<minInclusive value=\"-140\"/\>

\<maxInclusive value=\"-44\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"Thresxhighp\"\>

\<restriction base=\"integer\"\>

\<minInclusive value=\"0\"/\>

\<maxInclusive value=\"62\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"Threshxhighq\"\>

\<restriction base=\"integer\"\>

\<minInclusive value=\"0\"/\>

\<maxInclusive value=\"31\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"Threshxlowp\"\>

\<restriction base=\"integer\"\>

\<minInclusive value=\"0\"/\>

\<maxInclusive value=\"62\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"Threshxlowq\"\>

\<restriction base=\"integer\"\>

\<minInclusive value=\"0\"/\>

\<maxInclusive value=\"62\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"Treselectionnr\"\>

\<restriction base=\"integer\"\>

\<minInclusive value=\"0\"/\>

\<maxInclusive value=\"7\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"Treselectionnrsfhigh\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"25\"/\>

\<enumeration value=\"50\"/\>

\<enumeration value=\"75\"/\>

\<enumeration value=\"100\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"Treselectionnrsfmedium\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"25\"/\>

\<enumeration value=\"50\"/\>

\<enumeration value=\"75\"/\>

\<enumeration value=\"100\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"Absolutefrequencyssb\"\>

\<restriction base=\"integer\"\>

\<minInclusive value=\"0\"/\>

\<maxInclusive value=\"3279165\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"Ssbsubcarrierspacing\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"15\"/\>

\<enumeration value=\"30\"/\>

\<enumeration value=\"120\"/\>

\<enumeration value=\"240\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"Multifrequencybandlistnr\"\>

\<restriction base=\"integer\"\>

\<minInclusive value=\"1\"/\>

\<maxInclusive value=\"256\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"beamType\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"SSB-BEAM\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"beamAzimuth\"\>

\<restriction base=\"integer\"\>

\<minInclusive value=\"-1800\"/\>

\<maxInclusive value=\"1800\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"beamTilt\"\>

\<restriction base=\"integer\"\>

\<minInclusive value=\"-900\"/\>

\<maxInclusive value=\"900\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"beamHorizWidth\"\>

\<restriction base=\"integer\"\>

\<minInclusive value=\"0\"/\>

\<maxInclusive value=\"3599\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"beamVertWidth\"\>

\<restriction base=\"integer\"\>

\<minInclusive value=\"0\"/\>

\<maxInclusive value=\"1800\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"coverageShapeType\"\>

\<restriction base=\"integer\"\>

\<minInclusive value=\"0\"/\>

\<maxInclusive value=\"65535\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"resourceType\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"PRB\"/\>

\<enumeration value=\"RRC\"/\>

\<enumeration value=\"DRB\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"LocalEndPoint\"\>

\<sequence\>

\<element name=\"ipv4Address\" type=\"string\"/\>

\<element name=\"ipv6Address\" type=\"string\"/\>

\<element name=\"ipv6Prefix\" type=\"string\"/\>

\<element name=\"vlanId\" type=\"integer\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"RemoteEndPoint\"\>

\<sequence\>

\<element name=\"ipv4Address\" type=\"string\"/\>

\<element name=\"ipv6Address\" type=\"string\"/\>

\<element name=\"ipv6Prefix\" type=\"string\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"blackListEntry\"\>

\<sequence minOccurs=\"0\" maxOccurs=\"1007\"\>

\<element name=\"pci\" type=\"en:Pci\" maxOccurs=\"504\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"blackListEntryIdleMode\"\>

\<sequence minOccurs=\"0\" maxOccurs=\"1007\"\>

\<element name=\"pci\" type=\"en:Pci\" maxOccurs=\"504\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"PLMNIdList\"\>

\<sequence\>

\<element name=\"pLMNId\" type=\"en:PLMNId\" maxOccurs=\"6\"/\>

\<!\-- The first pLMNId of the pLMNIdList is primary PLMN id \--\>

\</sequence\>

\</complexType\>

\<complexType name=\"cellIndividualOffset\"\>

\<sequence\>

\<element name=\"rsrpOffsetSSB\" type=\"qOffsetRangeList\"/\>

\<element name=\"rsrqOffsetSSB\" type=\"qOffsetRangeList\"/\>

\<element name=\"sinrOffsetSSB\" type=\"qOffsetRangeList\"/\>

\<element name=\"rsrpOffsetCSI-RS\" type=\"qOffsetRangeList\"/\>

\<element name=\"rsrqOffsetCSI-RS\" type=\"qOffsetRangeList\"/\>

\<element name=\"sinrOffsetCSI-RS\" type=\"qOffsetRangeList\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"PLMNInfoType\"\>

\<sequence\>

\<element name=\"pLMNId\" type=\"en:PLMNId\"/\>

\<element name=\"sNSSAI\" type=\"ngc:SNssai\" minOccurs=\"0\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"PLMNInfoListType\"\>

\<sequence\>

\<element name=\"pLMNInfo\" type=\"PLMNInfoType\" minOccurs=\"1\"/\>

\</sequence\>

\</complexType\>

\<simpleType name=\"maximumDeviationHoTrigger\"\>

\<restriction base=\"integer\"\>

\<minInclusive value=\"-20\"/\>

\<maxInclusive value=\"20\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"minimumTimeBetweenHoTriggerChange\"\>

\<restriction base=\"integer\"\>

\<minInclusive value=\"0\"/\>

\<maxInclusive value=\"604800\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"tstoreUEcntxt\"\>

\<restriction base=\"integer\"\>

\<minInclusive value=\"0\"/\>

\<maxInclusive value=\"1023\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"loadThreshold\"\>

\<restriction base=\"integer\"\>

\<minInclusive value=\"0\"/\>

\<maxInclusive value=\"100\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"timeDuration\"\>

\<restriction base=\"integer\"\>

\<minInclusive value=\"0\"/\>

\<maxInclusive value=\"900\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"energySavingControl\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"toBeEnergySaving\"/\>

\<enumeration value=\"toBeNotEnergySaving\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"energySavingState\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"isNotEnergySaving\"/\>

\<enumeration value=\"isEnergySaving\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"isProbingCapable\"\>

\<restriction base=\"string\"\>

\<enumeration value=\"yes\"/\>

\<enumeration value=\"no\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"AccessDelayRange\"\>

\<restriction base=\"unsignedShort\"\>

\<minInclusive value=\"10\"/\>

\<maxInclusive value=\"560\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"NumberOfPreambleRange\"\>

\<restriction base=\"unsignedShort\"\>

\<minInclusive value=\"1\"/\>

\<maxInclusive value=\"200\"/\>

\</restriction\>

\</simpleType\>

\<simpleType name=\"RachProbability\"\>

\<restriction base=\"unsignedShort\"\>

\<enumeration value=\"25\"/\>

\<enumeration value=\"50\"/\>

\<enumeration value=\"75\"/\>

\<enumeration value=\"90\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"UeAccDelayProbilityDist\"\>

\<sequence\>

\<element name=\"Probability\" type=\"sp:RachProbability\"/\>

\<element name=\"AccessDelay\" type=\"sp:AccessDelayRange\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"UeAccDelayProbilityDistlist\"\>

\<sequence\>

\<element name=\"ueAccDelayProbilityDist\"
type=\"sp:UeAccDelayProbilityDist\" maxOccurs=\"4\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"UeAccProbilityDist\"\>

\<sequence\>

\<element name=\"Probability\" type=\"sp:RachProbability\"/\>

\<element name=\"NumberOfPreamble\" type=\"sp:NumberOfPreambleRange\"/\>

\</sequence\>

\</complexType\>

\<complexType name=\"UeAccProbilityDistlist\"\>

\<sequence\>

\<element name=\"ueAccProbilityDist\" type=\"sp:UeAccProbilityDist\"
maxOccurs=\"4\"/\>

\</sequence\>

\</complexType\>

\<simpleType name=\"NRPci\"\>

\<restriction base=\"unsignedShort\"\>

\<maxInclusive value=\"1007\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"NRPciList\"\>

\<sequence\>

\<element name=\"nRPci\" type=\"en:NRPci\" maxOccurs=\"1008\"/\>

\</sequence\>

\</complexType\>

\<simpleType name=\"NRPci\"\>

\<restriction base=\"unsignedShort\"\>

\<maxInclusive value=\"1007\"/\>

\</restriction\>

\</simpleType\>

\<complexType name=\"CSonPciList\"\>

\<sequence\>

\<element name=\"nRPci\" type=\"en:NRPci\" maxOccurs=\"1008\"/\>

\</sequence\>

\</complexType\>

\<element name=\"GNBDUFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from ManagedFunction \--\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"peeParametersList\" type=\"xn:peeParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<!\--End of inherited attributes from ManagedFunction\--\>

\<element name=\"gnbId\" type=\"nn:GnbId\"/\>

\<element name=\"gnbIdLength\" type=\"nn:GnbIdLength\"/\>

\<element name=\"gnbDUId\" type=\"nn:GnbDuId\"/\>

\<element name=\"gnbDuName\" type=\"nn:GnbName\" minOccurs=\"0\"/\>

\<element name=\"x2Blacklist\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"x2Whitelist\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"xnBlacklist\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"xnWhitelist\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"xnHOBlackList\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"x2HOBlackList\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"aggressorSetID\" type=\"nn:AggressorSetID\"/\>

\<element name=\"victimSetID\" type=\"nn:VictimSetID\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"nn:NRCellDU\"/\>

\<element ref=\"nn:BWP\"/\>

\<element ref=\"nn:NRSectorCarrier\"/\>

\<element ref=\"nn:EP\_F1C\"/\>

\<element ref=\"nn:EP\_F1U\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"DRACHOptimizationFunction\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"GNBCUCPFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from ManagedFunction \--\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"peeParametersList\" type=\"xn:peeParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<!\--End of inherited attributes from ManagedFunction\--\>

\<element name=\"gnbId\" type=\"nn:GnbId\" /\>

\<element name=\"gnbIdLength\" type=\"nn:GnbIdLength\"/\>

\<element name=\"gnbCuName\" type=\" nn:GnbName\" minOccurs=\"0\"/\>

\<element name=\"pLMNId\" type=\"en:PLMNId\" /\>

\<element name=\"x2Blacklist\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"x2Whitelist\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"xnBlacklist\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"xnWhitelist\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"xnHOBlackList\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"x2HOBlackList\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"mappingSetIDBackhaulAddress\"
type=\"MappingSetIDBackhaulAddress\" minOccurs=\"0\"/\>

\<element name=\"configurable5QISetRef\" type=\"xn:dn\"/\>

\<element name=\"dynamic5QISetRef\" type=\"xn:dn\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"nn:NRCellCU\"/\>

\<element ref=\"nn:EP\_F1C\"/\>

\<element ref=\"nn:EP\_E1\"/\>

\<element ref=\"nn:EP\_XnC\"/\>

\<element ref=\"nn:EP\_X2C\"/\>

\<element ref=\"nn:EP\_NgC\"/\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"DESManagementFunction\"/\>

\<element ref=\"DMROFunction\"/\>

\<element ref=\"DANRManagementFunction\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"GNBCUUPFunction\"
substitutionGroup=\"xn:ManagedElementOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from ManagedFunction \--\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"peeParametersList\" type=\"xn:peeParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<!\--End of inherited attributes from ManagedFunction\--\>

\<element name=\"gNBCUUPId\" type=\"nn:GnbCuupId \"/\>

\<element name=\"pLMNInfoList\" type=\"PLMNInfoListType\"/\>

\<element name=\"gNBId\" type=\"nn:GnbId\"/\>

\<element name=\"gnbIdLength\" type=\"nn:GnbIdLength\"/\>

\<element name=\"configurable5QISetRef\" type=\"xn:dn\"/\>

\<element name=\"dynamic5QISetRef\" type=\"xn:dn\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"nn:EP\_E1\"/\>

\<element ref=\"nn:EP\_F1U\"/\>

\<element ref=\"nn:EP\_XnU\"/\>

\<element ref=\"nn:EP\_NgU\"/\>

\<element ref=\"nn:EP\_X2U\"/\>

\<element ref=\"nn:EP\_S1U\"/\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"NRCellCU\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from ManagedFunction \--\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"peeParametersList\" type=\"xn:peeParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<!\--End of inherited attributes from ManagedFunction\--\>

\<element name=\"nCGI\" type=\"nn:Ncgi\"/\>

\<element name=\"pLMNIdList\" type=\"en:PLMNIdList\"/\>

\<element name=\"sNSSAIList\" type=\"ngc:SnssaiList\" minOccurs=\"0\"/\>

\<element name=\"nRFrequencyRef\" type=\"xn:dn\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\<element ref=\"nRCellRelation\"/\>

\<element ref=\"nRFreqRelation\"/\>

\<element ref=\"eUtranCellRelation\"/\>

\<element ref=\"eUtranFreqRelation\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"1\"\>

\<element ref=\"sp:EnergySavingProperties\"/\>

\<element ref=\"sp:ESPolicies\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref= \"RRMPolicyRatio\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"DESManagementFunction\"/\>

\<element ref=\"DMROFunction\"/\>

\<element ref=\"CESManagementFunction\"/\>

\<element ref=\"DPCIConfigurationFunction\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"NRCellDU\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from ManagedFunction \--\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"peeParametersList\" type=\"xn:peeParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<!\--End of inherited attributes from ManagedFunction\--\>

\<element name=\"nCGI\" type=\"nn:Ncgi\" minOccurs=\"0\"/\>

\<element name=\"operationalState\" type=\"sm:operationalStateType\"
minOccurs=\"0\"/\>

\<element name=\"administrativeState\"
type=\"sm:administrativeStateType\" minOccurs=\"0\"/\>

\<element name=\"cellState\" type=\"nn:CellState\"/\>

\<element name=\"pLMNIdList\" type=\"en:PLMNIdList\"/\>

\<element name=\"sNSSAIList\" type=\"ngc:SnssaiList\" minOccurs=\"0\"/\>

\<element name=\"nRpci\" type=\"nn:Pci\" /\>

\<element name=\"nRTac\" type=\"nn:NrTac\" /\>

\<element name=\"arfcnDL\" type=\"integer\"/\>

\<element name=\"arfcnUL\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"arfcnSUL\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"bSChannelBwDL\" type=\"integer\"/\>

\<element name=\"bSChannelBwUL\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"bSChannelBwSUL\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"nRFrequencyRef\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"nRSectorCarrierRef\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"bWPRef\" type=\"xn:dn\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"1\"\>

\<element ref=\"sp:EnergySavingProperties\"/\>

\<element ref=\"sp:ESPolicies\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"RRMPolicyRatio\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"CPCIConfigurationFunction\"/\>

\<element ref=\"DRACHOptimizationFunction\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"NRSectorCarrier\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from ManagedFunction \--\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"peeParametersList\" type=\"xn:peeParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<!\--End of inherited attributes from ManagedFunction\--\>

\<element name=\"txDirection\" type=\"nn:TxDirection\"/\>

\<element name=\"configuredMaxTxPower\" type=\"integer\"/\>

\<element name=\"arfcnDL\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"arfcnUL\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"bSChannelBwDL\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"bSChannelBwUL\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"sectorEquipmentFunctionRef\" type=\"xn:dn\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"1\"\>

\<element ref=\"sp:EnergySavingProperties\"/\>

\<element ref=\"sp:ESPolicies\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"BWP\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from ManagedFunction \--\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"peeParametersList\" type=\"xn:peeParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<!\--End of inherited attributes from ManagedFunction\--\>

\<element name=\"bwpContext\" type=\"nn:BwpContext\"/\>

\<element name=\"isInitialBwp\" type=\"nn:IsInitialBwp\"/\>

\<element name=\"subCarrierSpacing\" type=\"integer\"/\>

\<element name=\"cyclicPrefix\" type=\"nn:CyclicPrefix\"/\>

\<element name=\"startRB\" type=\"integer\"/\>

\<element name=\"numberOfRBs\" type=\"integer\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"CommonBeamformingFunction\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"coverageShape\" type=\"coverageShapeType\"
minOccurs=\"0\"/\>

\<element name=\"digitalTilt\" type=\"beamTilt\" minOccurs=\"0\"/\>

\<element name=\"digitalAzimuth\" type=\"beamAzimuth\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"1\"\>

\<element ref=\"sp:EnergySavingProperties\"/\>

\<element ref=\"sp:ESPolicies\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"Beam\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"beamIndex\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"beamType\" type=\"beamType\" minOccurs=\"0\"/\>

\<element name=\"beamAzimuth\" type=\"beamAzimuth\" minOccurs=\"0\"/\>

\<element name=\"beamTilt\" type=\"beamTilt\" minOccurs=\"0\"/\>

\<element name=\"beamHorizWidth\" type=\"beamHorizWidth\"
minOccurs=\"0\"/\>

\<element name=\"beamVertWidth\" type=\"beamVertWidth\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"1\"\>

\<element ref=\"sp:EnergySavingProperties\"/\>

\<element ref=\"sp:ESPolicies\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EP\_E1\"\>

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

\<element name=\"localAddress\" type=\"nn:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"nn:RemoteEndPoint\"
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

\<element name=\"EP\_XnC\"\>

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

\<element name=\"localAddress\" type=\"nn:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"nn:RemoteEndPoint\"
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

\<element name=\"EP\_XnU\"\>

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

\<element name=\"localAddress\" type=\"nn:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"nn:RemoteEndPoint\"
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

\<element name=\"EP\_NgC\"\>

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

\<element name=\"localAddress\" type=\"nn:LoacalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"nn:RemoteEndPoint\"
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

\<element name=\"EP\_NgU\"\>

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

\<element name=\"localAddress\" type=\"nn:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"nn:RemoteEndPoint\"
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

\<element name=\"EP\_F1C\"\>

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

\<element name=\"localAddress\" type=\"nn:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"nn:RemoteEndPoint\"
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

\<element name=\"EP\_F1U\"\>

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

\<element name=\"localAddress\" type=\"nn:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"nn:RemoteEndPoint\"
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

\<element name=\"EP\_S1U\"\>

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

\<element name=\"localAddress\" type=\"nn:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"nn:RemoteEndPoint\"
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

\<element name=\"EP\_X2C\"\>

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

\<element name=\"localAddress\" type=\"nn:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"nn:RemoteEndPoint\"
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

\<element name=\"EP\_X2U\"\>

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

\<element name=\"localAddress\" type=\"nn:LocalEndPoint\"
minOccurs=\"0\"/\>

\<element name=\"remoteAddress\" type=\"nn:RemoteEndPoint\"
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

\<element name=\"NRCellRelation\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from Top\_ \--\>

\<element name=\"id\" type=\"string\" /\>

\<!\--End of inherited attributes from Top\_ \--\>

\<element name=\"nRTCI\" type=\"nn:Nrtci\"/\>

\<element name=\"cellIndividualOffset\"
type=\"en:CellIndividualOffset\"/\>

\<element name=\"nRFreqRelationRef\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"adjacentNRCellRef\" type=\"xn:dn\" minOccurs=\"0\"/\>

\<element name=\"isRemoveAllowed\" type=\"boolean\" minOccurs=\"0\"/\>

\<element name=\"isHOAllowed\" type=\"boolean\" minOccurs=\"0\"/\>

\<element name=\"isESCoveredBy\" type=\"nn:isESCoveredBy\"
minOccurs=\"0\"/\>

\<element name=\"isENDCAllowed\" type=\"boolean\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"1\"\>

\<element ref=\"sp:EnergySavingProperties\"/\>

\<element ref=\"sp:ESPolicies\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"NRFreqRelation\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from Top\_ \--\>

\<element name=\"id\" type=\"string\" /\>

\<!\--End of inherited attributes from Top\_ \--\>

\<element name=\"offsetMO\" type=\"en:qOffsetRangeList\"/\>

\<element name=\"blackListEntry\" type=\"en:blackListEntry\"
minOccurs=\"0\"/\>

\<element name=\"blackListEntryIdleMode\"
type=\"en:blackListEntryIdleMode\" minOccurs=\"0\"/\>

\<element name=\"cellReselectionPriority\"
type=\"en:cellReselectionPriority\"/\>

\<element name=\"cellReselectionSubPriority\"
type=\"en:cellReselectionSubPriority\"/\>

\<element name=\"pMax\" type=\"en:PMaxRangeType\" minOccurs=\"0\"/\>

\<element name=\"qOffserFreq\" type=\"nn:qOffserFreq\"
minOccurs=\"0\"/\>

\<element name=\"qQualMin\" type=\"en:qQualMin\" minOccurs=\"0\"/\>

\<element name=\"qRxLevMin\" type=\"en:qRxLevMin\" minOccurs=\"0\"/\>

\<element name=\"threshXHighP\" type=\"en:threshxhighp\"
minOccurs=\"0\"/\>

\<element name=\"threshXHighQ\" type=\"en:threshxhighq\"
minOccurs=\"0\"/\>

\<element name=\"threshXLowP\" type=\"en:threshxlowp\"
minOccurs=\"0\"/\>

\<element name=\"threshXLowQ\" type=\"en:threshxlowp\"
minOccurs=\"0\"/\>

\<element name=\"tReselectionNr\" type=\"nn:Treselectionnr\"
minOccurs=\"0\"/\>

\<element name=\"tReselectionNRSfHigh\" type=\"nn:Treselectionnrsfhigh\"
minOccurs=\"0\"/\>

\<element name=\"tReselectionNRSfMedium\"
type=\"nn:Treselectionnrsfmedium\" minOccurs=\"0\"/\>

\<element name=\"nRFrequencyRef\" type=\"xn:dn\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"1\"\>

\<element ref=\"sp:EnergySavingProperties\"/\>

\<element ref=\"sp:ESPolicies\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"ExternalNRCellCU\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from ManagedFunction \--\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"peeParametersList\" type=\"xn:peeParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<!\--End of inherited attributes from ManagedFunction \--\>

\<element name=\"nCGI\" type=\"nn:Ncgi\"/\>

\<element name=\"pLMNIdList\" type=\"en:PLMNIdList\"/\>

\<element name=\"nRPCI\" type=\"nn:Nrpci\" minOccurs=\"0\"/\>

\<element name=\"nRFrequencyRef\" type=\"xn:dn\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"1\"\>

\<element ref=\"sp:EnergySavingProperties\"/\>

\<element ref=\"sp:ESPolicies\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"ExternalGNBCUCPFunction\"
substitutionGroup=\"xn:SubNetworkOptionallyContainedNrmClass \"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from ManagedFunction \--\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"peeParametersList\" type=\"xn:peeParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<!\--End of inherited attributes from ManagedFunction \--\>

\<element name=\"gnbId\" type=\"nn:GnbId\" /\>

\<element name=\"gnbIdLength\" type=\"nn:GnbIdLength\"/\>

\<element name=\"pLMNId\" type=\"en:PLMNId\" /\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"1\"\>

\<element ref=\"sp:EnergySavingProperties\"/\>

\<element ref=\"sp:ESPolicies\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"RRMPolicy\_\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"resourceType\" type=\"ResourceType\" /\>

\<element name=\"rRMPolicyMemberList\" type=\"PLMNInfoListType\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"RRMPolicyRatio\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"RRMPolicy\_\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"rRMPolicyMaxRatio\" type=\"integer\" minOccurs=\"1\"/\>

\<element name=\"rRMPolicyMinRatio\" type=\"integer\" minOccurs=\"1\"/\>

\<element name=\"rRMPolicyDedicatedRatio\" type=\"integer\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"1\"\>

\<element ref=\"sp:EnergySavingProperties\"/\>

\<element ref=\"sp:ESPolicies\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"NRFrequency\"
substitutionGroup=\"xn:SubNetworkOptionallyContainedNrmClass\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<!\-- Inherited attributes from ManagedFunction \--\>

\<element name=\"userLabel\" type=\"string\" minOccurs=\"0\"/\>

\<element name=\"vnfParametersList\" type=\"xn:vnfParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"peeParametersList\" type=\"xn:peeParametersListType\"
minOccurs=\"0\"/\>

\<element name=\"priority\" type=\"integer\" minOccurs=\"0\"/\>

\<element name=\"measurements\" type=\"xn:MeasurementTypesAndGPsList\"
minOccurs=\"0\"/\>

\<!\--End of inherited attributes from ManagedFunction \--\>

\<element name=\"absoluteFrequencySSB\" type=\"nn:Absolutefrequencyssb\"
minOccurs=\"0\"/\>

\<element name=\"sSBSubCarrierSpacing\" type=\"nn:Ssbsubcarrierspacing\"
minOccurs=\"0\"/\>

\<element name=\"multiFrequencyBandListNR\"
type=\"nn:MultifrequencyBandlistnr\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:VsDataContainer\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"1\"\>

\<element ref=\"sp:EnergySavingProperties\"/\>

\<element ref=\"sp:ESPolicies\"/\>

\</choice\>

\<choice minOccurs=\"0\" maxOccurs=\"unbounded\"\>

\<element ref=\"xn:MeasurementControl\"/\>

\</choice\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"MappingSetIDBackhaulAddress\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"setID\" type=\"nn:SetId\" /\>

\<element name=\"backhaulAdress\" type=\"BackhaulAddress\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"BackhaulAddress\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"gNBID\" type=\"nn:GnbId\" /\>

\<element name=\"tAI\" type=\"TAI\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"TAI\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"nRTac\" type=\"nn:NrTac\" /\>

\<element name=\"pLMNId\" type=\"en:PLMNId\" /\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"DANRManagementFunction\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"intrasystemANRManagementSwitch\" type=\"boolean\"
minOccurs=\"0\"/\>

\<element name=\"intrasystemANRManagementSwitch\" type=\"beamType\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"DESManagementFunction\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"desSwitch\" type=\"boolean\" minOccurs=\"0\"/\>

\<element name=\"intraRatEsActivationOriginalCellLoadParameters\"
type=\"IntraRatEsActivationOriginalCellLoadParameters \"
minOccurs=\"0\"/\>

\<element name=\"intraRatEsActivationCandidateCellsLoadParameters\"
type=\"IntraRatEsActivationCandidateCellsLoadParameters\"
minOccurs=\"0\"/\>

\<element name=\"intraRatEsDeactivationCandidateCellsLoadParameters\"
type=\"IntraRatEsDeactivationCandidateCellsLoadParameters\"
minOccurs=\"0\"/\>

\<element name=\"esNotAllowedTimePeriod\"
type=\"EsNotAllowedTimePeriod\" minOccurs=\"0\"/\>

\<element name=\"interRatEsActivationOriginalCellParameters\"
type=\"InterRatEsActivationOriginalCellParameters\" minOccurs=\"0\"/\>

\<element name=\"interRatEsActivationCandidateCellParameters\"
type=\"InterRatEsActivationCandidateCellParameters\" minOccurs=\"0\"/\>

\<element name=\"interRatEsDeactivationCandidateCellParameters\"
type=\"InterRatEsDeactivationCandidateCellParameters\"
minOccurs=\"0\"/\>

\<element name=\"energySavingState\" type=\"energySavingState\"
minOccurs=\"0\"/\>

\<element name=\"isProbingCapable\" type=\"isProbingCapable\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"IntraRatEsActivationOriginalCellLoadParameters\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"loadThreshold\" type=\"loadThreshold\"
minOccurs=\"0\"/\>

\<element name=\"timeDuration\" type=\"timeDuration\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"IntraRatEsActivationCandidateCellsLoadParameters\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"loadThreshold\" type=\"loadThreshold\"
minOccurs=\"0\"/\>

\<element name=\"timeDuration\" type=\"timeDuration\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"IntraRatEsDeactivationCandidateCellsLoadParameters\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"loadThreshold\" type=\"loadThreshold\"
minOccurs=\"0\"/\>

\<element name=\"timeDuration\" type=\"timeDuration\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EsNotAllowedTimePeriod\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"startTimeandendTime\" type=\"nn:startTimeandendTime\"
/\>

\<element name=\"periodOfDay\" type=\"nn:startTimeandendTime\" /\>

\<element name=\"daysOfWeekList\" type=\"en:daysOfWeekList\" /\>

\<element name=\"listoftimeperiods\" type=\"en:listoftimeperiods\" /\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"InterRatEsActivationOriginalCellParameters\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"loadThreshold\" type=\"loadThreshold\"
minOccurs=\"0\"/\>

\<element name=\"timeDuration\" type=\"timeDuration\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"InterRatEsActivationCandidateCellParameters\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"loadThreshold\" type=\"loadThreshold\"
minOccurs=\"0\"/\>

\<element name=\"timeDuration\" type=\"timeDuration\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"InterRatEsDeactivationCandidateCellParameters\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"loadThreshold\" type=\"loadThreshold\"
minOccurs=\"0\"/\>

\<element name=\"timeDuration\" type=\"timeDuration\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"DRACHOptimizationFunction\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"ueAccProbilityDistlist\"
type=\"UeAccProbilityDistlist\" minOccurs=\"0\"/\>

\<element name=\"ueAccDelayProbilityDistlist\"
type=\"UeAccDelayProbilityDistlist\" minOccurs=\"0\"/\>

\<element name=\"drachOptimizationControl\" type=\"boolean\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"DMROFunction\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"dmroControl\" type=\" boolean\" minOccurs=\"0\"/\>

\<element name=\"maximumDeviationHoTrigger\"
type=\"maximumDeviationHoTrigger\" minOccurs=\"0\"/\>

\<element name=\"minimumTimeBetweenHoTriggerChange\"
type=\"minimumTimeBetweenHoTriggerChange\" minOccurs=\"0\"/\>

\<element name=\"tstoreUEcntxt\" type=\"tstoreUEcntxt\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"DPCIConfigurationFunction\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"nRPciList\" type=\"NRPciList\" minOccurs=\"0\"/\>

\<element name=\"dPciConfigurationControl\" type=\"boolean\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"CPCIConfigurationFunction\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"cSonPciList\" type=\"CSonPciList\" minOccurs=\"0\"/\>

\<element name=\"cPciConfigurationControl\" type=\"boolean\"
minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"CESManagementFunction\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"cesSwitch\" type=\"boolean\" minOccurs=\"0\"/\>

\<element name=\"energySavingState\" type=\"energySavingState\"
minOccurs=\"0\"/\>

\<element name=\"energySavingControl\" type=\"energySavingControl\"
minOccurs=\"0\"/\>

\<element name=\"intraRatEsActivationOriginalCellLoadParameters\"
type=\"IntraRatEsActivationOriginalCellLoadParameters \"
minOccurs=\"0\"/\>

\<element name=\"intraRatEsActivationCandidateCellsLoadParameters\"
type=\"IntraRatEsActivationCandidateCellsLoadParameters\"
minOccurs=\"0\"/\>

\<element name=\"intraRatEsDeactivationCandidateCellsLoadParameters\"
type=\"IntraRatEsDeactivationCandidateCellsLoadParameters\"
minOccurs=\"0\"/\>

\<element name=\"esNotAllowedTimePeriod\"
type=\"EsNotAllowedTimePeriod\" minOccurs=\"0\"/\>

\<element name=\"interRatEsActivationOriginalCellParameters\"
type=\"InterRatEsActivationOriginalCellParameters\" minOccurs=\"0\"/\>

\<element name=\"interRatEsActivationCandidateCellParameters\"
type=\"InterRatEsActivationCandidateCellParameters\" minOccurs=\"0\"/\>

\<element name=\"interRatEsDeactivationCandidateCellParameters\"
type=\"InterRatEsDeactivationCandidateCellParameters\"
minOccurs=\"0\"/\> \</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"IntraRatEsActivationOriginalCellLoadParameters\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"loadThreshold\" type=\"loadThreshold\"
minOccurs=\"0\"/\>

\<element name=\"timeDuration\" type=\"timeDuration\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"IntraRatEsActivationCandidateCellsLoadParameters\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"loadThreshold\" type=\"loadThreshold\"
minOccurs=\"0\"/\>

\<element name=\"timeDuration\" type=\"timeDuration\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"IntraRatEsDeactivationCandidateCellsLoadParameters\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"loadThreshold\" type=\"loadThreshold\"
minOccurs=\"0\"/\>

\<element name=\"timeDuration\" type=\"timeDuration\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"EsNotAllowedTimePeriod\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"startTimeandendTime\" type=\"nn:startTimeandendTime\"
/\>

\<element name=\"periodOfDay\" type=\"nn:startTimeandendTime\" /\>

\<element name=\"daysOfWeekList\" type=\"en:daysOfWeekList\" /\>

\<element name=\"listoftimeperiods\" type=\"en:listoftimeperiods\" /\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"InterRatEsActivationOriginalCellParameters\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"loadThreshold\" type=\"loadThreshold\"
minOccurs=\"0\"/\>

\<element name=\"timeDuration\" type=\"timeDuration\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"InterRatEsActivationCandidateCellParameters\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"loadThreshold\" type=\"loadThreshold\"
minOccurs=\"0\"/\>

\<element name=\"timeDuration\" type=\"timeDuration\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\<element name=\"InterRatEsDeactivationCandidateCellParameters\"\>

\<complexType\>

\<complexContent\>

\<extension base=\"xn:NrmClass\"\>

\<sequence\>

\<element name=\"attributes\"\>

\<complexType\>

\<all\>

\<element name=\"loadThreshold\" type=\"loadThreshold\"
minOccurs=\"0\"/\>

\<element name=\"timeDuration\" type=\"timeDuration\" minOccurs=\"0\"/\>

\</all\>

\</complexType\>

\</element\>

\</sequence\>

\</extension\>

\</complexContent\>

\</complexType\>

\</element\>

\</schema\>

########  Annex D (normative): OpenAPI definition of the NR NRM

D.1 General 
===========

This annex contains the OpenAPI definition of the NR NRM in YAML format.

The Information Service (IS) of the NR NRM is defined in clause 4.

Mapping rules to produce the OpenAPI definition based on the IS are
defined in 3GPP TS 32.160 \[47\].

D.2 Void
========

D.3 Void
========

D.4 Solution Set (SS) definitions
=================================

D.4.1 Void
----------

D.4.2 Void
----------

D.4.3 OpenAPI document \"TS28541\_NrNrm.yaml\"
----------------------------------------------

openapi: 3.0.1

info:

title: NR NRM

version: 16.16.0

description: \>-

OAS 3.0.1 specification of the NR NRM

© 2023, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI,
TTA, TTC).

All rights reserved.

externalDocs:

description: 3GPP TS 28.541; 5G NRM, NR NRM

url: http://www.3gpp.org/ftp/Specs/archive/28\_series/28.541/

paths: {}

components:

schemas:

\#\-\-\-\-\-\-\-- Definition of
types\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

GnbId:

type: string

GnbIdLength:

type: integer

minimum: 22

maximum: 32

GnbName:

type: string

maxLength: 150

GnbDuId:

type: number

minimum: 0

maximum: 68719476735

GnbCuUpId:

type: number

minimum: 0

maximum: 68719476735

Sst:

type: integer

maximum: 255

Snssai:

type: object

properties:

sst:

\$ref: \'\#/components/schemas/Sst\'

sd:

type: string

PlmnIdList:

type: array

items:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/PlmnId\'

PlmnInfo:

type: object

properties:

plmnId:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/PlmnId\'

snssai:

\$ref: \'\#/components/schemas/Snssai\'

PlmnInfoList:

type: array

items:

\$ref: \'\#/components/schemas/PlmnInfo\'

GGnbId:

type: string

pattern:
\'\^\[0-9\]{3}\[0-9\]{2,3}-(22\|23\|24\|25\|26\|27\|28\|29\|30\|31\|32)-\[0-9\]{1,10}\'

GEnbId:

type: string

pattern: \'\^\[0-9\]{3}\[0-9\]{2,3}-(18\|20\|21\|22)-\[0-9\]{1,7}\'

GGnbIdList:

type: array

items:

\$ref: \'\#/components/schemas/GGnbId\'

GEnbIdList:

type: array

items:

\$ref: \'\#/components/schemas/GEnbId\'

NrPci:

type: integer

maximum: 503

BackhaulAddress:

type: object

properties:

gnbId:

\$ref: \'\#/components/schemas/GnbId\'

tai:

\$ref: \"TS28623\_GenericNrm.yaml\#/components/schemas/Tai\"

MappingSetIDBackhaulAddress:

type: object

properties:

setID:

type: integer

backhaulAddress:

\$ref: \'\#/components/schemas/BackhaulAddress\'

IntraRatEsActivationOriginalCellLoadParameters:

type: object

properties:

loadThreshold:

type: integer

timeDuration:

type: integer

IntraRatEsActivationCandidateCellsLoadParameters:

type: object

properties:

loadThreshold:

type: integer

timeDuration:

type: integer

IntraRatEsDeactivationCandidateCellsLoadParameters:

type: object

properties:

loadThreshold:

type: integer

timeDuration:

type: integer

EsNotAllowedTimePeriod:

type: object

properties:

startTimeandendTime:

type: string

periodOfDay:

type: string

daysOfWeekList:

type: string

listoftimeperiods:

type: string

InterRatEsActivationOriginalCellParameters:

type: object

properties:

loadThreshold:

type: integer

timeDuration:

type: integer

InterRatEsActivationCandidateCellParameters:

type: object

properties:

loadThreshold:

type: integer

timeDuration:

type: integer

InterRatEsDeactivationCandidateCellParameters:

type: object

properties:

loadThreshold:

type: integer

timeDuration:

type: integer

UeAccProbabilityDist:

type: object

properties:

targetProbability:

type: integer

numberofpreamblessent:

type: integer

UeAccDelayProbabilityDist:

type: object

properties:

targetProbability:

type: integer

accessdelay:

type: integer

NRPciList:

type: array

items:

\$ref: \'\#/components/schemas/NrPci\'

minItems: 0

maxItems: 1007

CSonPciList:

type: array

items:

\$ref: \'\#/components/schemas/NrPci\'

minItems: 1

maxItems: 100

MaximumDeviationHoTrigger:

type: integer

minimum: -20

maximum: 20

MinimumTimeBetweenHoTriggerChange:

type: integer

minimum: 0

maximum: 604800

TstoreUEcntxt:

type: integer

minimum: 0

maximum: 1023

CellState:

type: string

enum:

\- IDLE

\- INACTIVE

\- ACTIVE

CyclicPrefix:

type: string

enum:

\- \'15\'

\- \'30\'

\- \'60\'

\- \'120\'

TxDirection:

type: string

enum:

\- DL

\- UL

\- DL and UL

BwpContext:

type: string

enum:

\- DL

\- UL

\- SUL

IsInitialBwp:

type: string

enum:

\- INITIAL

\- OTHER

\- SUL

IsESCoveredBy:

type: string

enum:

\- NO

\- PARTIAL

\- FULL

RrmPolicyMember:

type: object

properties:

plmnId:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/PlmnId\'

snssai:

\$ref: \'\#/components/schemas/Snssai\'

RrmPolicyMemberList:

type: array

items:

\$ref: \'\#/components/schemas/RrmPolicyMember\'

AddressWithVlan:

type: object

properties:

ipv4Address:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Ipv4Addr\'

ipv6Address:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Ipv6Addr\'

vlanId:

type: integer

minimum: 0

maximum: 4096

LocalAddress:

type: object

properties:

addressWithVlan:

\$ref: \'\#/components/schemas/AddressWithVlan\'

port:

type: integer

minimum: 0

maximum: 65535

RemoteAddress:

type: object

properties:

ipv4Address:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Ipv4Addr\'

ipv6Address:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Ipv6Addr\'

CellIndividualOffset:

type: object

properties:

rsrpOffsetSSB:

type: integer

rsrqOffsetSSB:

type: integer

sinrOffsetSSB:

type: integer

rsrpOffsetCSI-RS:

type: integer

rsrqOffsetCSI-RS:

type: integer

sinrOffsetCSI-RS:

type: integer

QOffsetRange:

type: integer

enum:

\- -24

\- -22

\- -20

\- -18

\- -16

\- -14

\- -12

\- -10

\- -8

\- -6

\- -5

\- -4

\- -3

\- -2

\- -1

\- 0

\- 24

\- 22

\- 20

\- 18

\- 16

\- 14

\- 12

\- 10

\- 8

\- 6

\- 5

\- 4

\- 3

\- 2

\- 1

QOffsetRangeList:

type: object

properties:

rsrpOffsetSSB:

\$ref: \'\#/components/schemas/QOffsetRange\'

rsrqOffsetSSB:

\$ref: \'\#/components/schemas/QOffsetRange\'

sinrOffsetSSB:

\$ref: \'\#/components/schemas/QOffsetRange\'

rsrpOffsetCSI-RS:

\$ref: \'\#/components/schemas/QOffsetRange\'

rsrqOffsetCSI-RS:

\$ref: \'\#/components/schemas/QOffsetRange\'

sinrOffsetCSI-RS:

\$ref: \'\#/components/schemas/QOffsetRange\'

QOffsetFreq:

type: number

TReselectionNRSf:

type: integer

enum:

\- 25

\- 50

\- 75

\- 100

SsbPeriodicity:

type: integer

enum:

\- 5

\- 10

\- 20

\- 40

\- 80

\- 160

SsbDuration:

type: integer

enum:

\- 1

\- 2

\- 3

\- 4

\- 5

SsbSubCarrierSpacing:

type: integer

enum:

\- 15

\- 30

\- 120

\- 240

CoverageShape:

type: integer

maximum: 65535

DigitalTilt:

type: integer

minimum: -900

maximum: 900

DigitalAzimuth:

type: integer

minimum: -1800

maximum: 1800

RSSetId:

type: integer

maximum: 4194303

RSSetType:

type: string

enum:

\- RS1

\- RS2

FrequencyDomainPara:

type: object

properties:

rimRSSubcarrierSpacing:

type: integer

rIMRSBandwidth:

type: integer

nrofGlobalRIMRSFrequencyCandidates:

type: integer

rimRSCommonCarrierReferencePoint:

type: integer

rimRSStartingFrequencyOffsetIdList:

type: array

items:

type: integer

SequenceDomainPara:

type: object

properties:

nrofRIMRSSequenceCandidatesofRS1:

type: integer

rimRSScrambleIdListofRS1:

type: array

items:

type: integer

nrofRIMRSSequenceCandidatesofRS2:

type: integer

rimRSScrambleIdListofRS2:

type: array

items:

type: integer

enableEnoughNotEnoughIndication:

type: string

enum:

\- ENABLE

\- DISABLE

RIMRSScrambleTimerMultiplier:

type: integer

RIMRSScrambleTimerOffset:

type: integer

TimeDomainPara:

type: object

properties:

dlULSwitchingPeriod1:

type: string

enum:

\- MS0P5

\- MS0P625

\- MS1

\- MS1P25

\- MS2

\- MS2P5

\- MS3

\- MS4

\- MS5

\- MS10

\- MS20

symbolOffsetOfReferencePoint1:

type: integer

dlULSwitchingPeriod2:

type: string

enum:

\- MS0P5

\- MS0P625

\- MS1

\- MS1P25

\- MS2

\- MS2P5

\- MS3

\- MS4

\- MS5

\- MS10

\- MS20

symbolOffsetOfReferencePoint2:

type: integer

totalnrofSetIdofRS1:

type: integer

totalnrofSetIdofRS2:

type: integer

nrofConsecutiveRIMRS1:

type: integer

nrofConsecutiveRIMRS2:

type: integer

consecutiveRIMRS1List:

type: array

items:

type: integer

consecutiveRIMRS2List:

type: array

items:

type: integer

enablenearfarIndicationRS1:

type: string

enum:

\- ENABLE

\- DISABLE

enablenearfarIndicationRS2:

type: string

enum:

\- ENABLE

\- DISABLE

RimRSReportInfo:

type: object

properties:

detectedSetID:

type: integer

propagationDelay:

type: integer

functionalityOfRIMRS:

type: string

enum:

\- RS1

\- RS2

\- RS1forEnoughMitigation

\- RS1forNotEnoughMitigation

RimRSReportConf:

type: object

properties:

reportIndicator:

type: string

enum:

\- ENABLE

\- DISABLE

reportInterval:

type: integer

nrofRIMRSReportInfo:

type: integer

maxPropagationDelay:

type: integer

rimRSReportInfoList:

type: array

items:

\$ref: \'\#/components/schemas/RimRSReportInfo\'

TceMappingInfo:

type: object

properties:

TceIPAddress:

oneOf:

\- \$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Ipv4Addr\'

\- \$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Ipv6Addr\'

TceID:

type: integer

PlmnTarget:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/PlmnId\'

TceMappingInfoList:

type: array

items:

\$ref: \'\#/components/schemas/TceMappingInfo\'

\#\-\-\-\-\-\-\-- Definition of abstract IOCs
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

RrmPolicy\_-Attr:

type: object

properties:

resourceType:

type: string

rRMPolicyMemberList:

\$ref: \'\#/components/schemas/RrmPolicyMemberList\'

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

\$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/SubNetwork-Attr\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/SubNetwork-ncO\'

\- type: object

properties:

SubNetwork:

\$ref: \'\#/components/schemas/SubNetwork-Multiple\'

ManagedElement:

\$ref: \'\#/components/schemas/ManagedElement-Multiple\'

NRFrequency:

\$ref: \'\#/components/schemas/NRFrequency-Multiple\'

ExternalGnbCuCpFunction:

\$ref: \'\#/components/schemas/ExternalGnbCuCpFunction-Multiple\'

ExternalENBFunction:

\$ref: \'\#/components/schemas/ExternalENBFunction-Multiple\'

EUtranFrequency:

\$ref: \'\#/components/schemas/EUtranFrequency-Multiple\'

DESManagementFunction:

\$ref: \'\#/components/schemas/DESManagementFunction-Single\'

DRACHOptimizationFunction:

\$ref: \'\#/components/schemas/DRACHOptimizationFunction-Single\'

DMROFunction:

\$ref: \'\#/components/schemas/DMROFunction-Single\'

DPCIConfigurationFunction:

\$ref: \'\#/components/schemas/DPCIConfigurationFunction-Single\'

CPCIConfigurationFunction:

\$ref: \'\#/components/schemas/CPCIConfigurationFunction-Single\'

CESManagementFunction:

\$ref: \'\#/components/schemas/CESManagementFunction-Single\'

Configurable5QISet:

\$ref:
\'TS28541\_5GcNrm.yaml\#/components/schemas/Configurable5QISet-Multiple\'

RimRSGlobal:

\$ref: \'\#/components/schemas/RimRSGlobal-Single\'

Dynamic5QISet:

\$ref:
\'TS28541\_5GcNrm.yaml\#/components/schemas/Dynamic5QISet-Multiple\'

ManagedElement-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

\$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedElement-Attr\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedElement-ncO\'

\- type: object

properties:

GnbDuFunction:

\$ref: \'\#/components/schemas/GnbDuFunction-Multiple\'

GnbCuUpFunction:

\$ref: \'\#/components/schemas/GnbCuUpFunction-Multiple\'

GnbCuCpFunction:

\$ref: \'\#/components/schemas/GnbCuCpFunction-Multiple\'

DESManagementFunction:

\$ref: \'\#/components/schemas/DESManagementFunction-Single\'

DRACHOptimizationFunction:

\$ref: \'\#/components/schemas/DRACHOptimizationFunction-Single\'

DMROFunction:

\$ref: \'\#/components/schemas/DMROFunction-Single\'

DPCIConfigurationFunction:

\$ref: \'\#/components/schemas/DPCIConfigurationFunction-Single\'

CPCIConfigurationFunction:

\$ref: \'\#/components/schemas/CPCIConfigurationFunction-Single\'

CESManagementFunction:

\$ref: \'\#/components/schemas/CESManagementFunction-Single\'

Configurable5QISet:

\$ref:
\'TS28541\_5GcNrm.yaml\#/components/schemas/Configurable5QISet-Multiple\'

Dynamic5QISet:

\$ref:
\'TS28541\_5GcNrm.yaml\#/components/schemas/Dynamic5QISet-Multiple\'

GnbDuFunction-Single:

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

gnbDuId:

\$ref: \'\#/components/schemas/GnbDuId\'

gnbDuName:

\$ref: \'\#/components/schemas/GnbName\'

gnbId:

\$ref: \'\#/components/schemas/GnbId\'

gnbIdLength:

\$ref: \'\#/components/schemas/GnbIdLength\'

rimRSReportConf:

\$ref: \'\#/components/schemas/RimRSReportConf\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

RRMPolicyRatio:

\$ref: \'\#/components/schemas/RRMPolicyRatio-Multiple\'

NrCellDu:

\$ref: \'\#/components/schemas/NrCellDu-Multiple\'

Bwp-Multiple:

\$ref: \'\#/components/schemas/Bwp-Multiple\'

NrSectorCarrier-Multiple:

\$ref: \'\#/components/schemas/NrSectorCarrier-Multiple\'

EP\_F1C:

\$ref: \'\#/components/schemas/EP\_F1C-Single\'

EP\_F1U:

\$ref: \'\#/components/schemas/EP\_F1U-Multiple\'

DRACHOptimizationFunction:

\$ref: \'\#/components/schemas/DRACHOptimizationFunction-Single\'

GnbCuUpFunction-Single:

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

gnbId:

\$ref: \'\#/components/schemas/GnbId\'

gnbIdLength:

\$ref: \'\#/components/schemas/GnbIdLength\'

gnbCuUpId:

\$ref: \'\#/components/schemas/GnbCuUpId\'

plmnInfoList:

\$ref: \'\#/components/schemas/PlmnInfoList\'

configurable5QISetRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

dynamic5QISetRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

RRMPolicyRatio:

\$ref: \'\#/components/schemas/RRMPolicyRatio-Multiple\'

EP\_E1:

\$ref: \'\#/components/schemas/EP\_E1-Single\'

EP\_XnU:

\$ref: \'\#/components/schemas/EP\_XnU-Multiple\'

EP\_F1U:

\$ref: \'\#/components/schemas/EP\_F1U-Multiple\'

EP\_NgU:

\$ref: \'\#/components/schemas/EP\_NgU-Multiple\'

EP\_X2U:

\$ref: \'\#/components/schemas/EP\_X2U-Multiple\'

EP\_S1U:

\$ref: \'\#/components/schemas/EP\_S1U-Multiple\'

GnbCuCpFunction-Single:

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

gnbId:

\$ref: \'\#/components/schemas/GnbId\'

gnbIdLength:

\$ref: \'\#/components/schemas/GnbIdLength\'

gnbCuName:

\$ref: \'\#/components/schemas/GnbName\'

plmnId:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/PlmnId\'

x2BlackList:

\$ref: \'\#/components/schemas/GGnbIdList\'

xnBlackList:

\$ref: \'\#/components/schemas/GGnbIdList\'

x2WhiteList:

\$ref: \'\#/components/schemas/GGnbIdList\'

xnWhiteList:

\$ref: \'\#/components/schemas/GGnbIdList\'

x2XnHOBlackList:

\$ref: \'\#/components/schemas/GEnbIdList\'

mappingSetIDBackhaulAddress:

\$ref: \'\#/components/schemas/MappingSetIDBackhaulAddress\'

tceMappingInfoList:

\$ref: \'\#/components/schemas/TceMappingInfoList\'

configurable5QISetRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

dynamic5QISetRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

RRMPolicyRatio:

\$ref: \'\#/components/schemas/RRMPolicyRatio-Multiple\'

NrCellCu:

\$ref: \'\#/components/schemas/NrCellCu-Multiple\'

EP\_XnC:

\$ref: \'\#/components/schemas/EP\_XnC-Multiple\'

EP\_E1:

\$ref: \'\#/components/schemas/EP\_E1-Multiple\'

EP\_F1C:

\$ref: \'\#/components/schemas/EP\_F1C-Multiple\'

EP\_NgC:

\$ref: \'\#/components/schemas/EP\_NgC-Multiple\'

EP\_X2C:

\$ref: \'\#/components/schemas/EP\_X2C-Multiple\'

DANRManagementFunction:

\$ref: \'\#/components/schemas/DANRManagementFunction-Single\'

DESManagementFunction:

\$ref: \'\#/components/schemas/DESManagementFunction-Single\'

DMROFunction:

\$ref: \'\#/components/schemas/DMROFunction-Single\'

NrCellCu-Single:

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

cellLocalId:

type: integer

plmnInfoList:

\$ref: \'\#/components/schemas/PlmnInfoList\'

nRFrequencyRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

RRMPolicyRatio:

\$ref: \'\#/components/schemas/RRMPolicyRatio-Multiple\'

NRCellRelation:

\$ref: \'\#/components/schemas/NRCellRelation-Multiple\'

EUtranCellRelation:

\$ref: \'\#/components/schemas/EUtranCellRelation-Multiple\'

NRFreqRelation:

\$ref: \'\#/components/schemas/NRFreqRelation-Multiple\'

EUtranFreqRelation:

\$ref: \'\#/components/schemas/EUtranFreqRelation-Multiple\'

DESManagementFunction:

\$ref: \'\#/components/schemas/DESManagementFunction-Single\'

DMROFunction:

\$ref: \'\#/components/schemas/DMROFunction-Single\'

CESManagementFunction:

\$ref: \'\#/components/schemas/CESManagementFunction-Single\'

DPCIConfigurationFunction:

\$ref: \'\#/components/schemas/DPCIConfigurationFunction-Single\'

NrCellDu-Single:

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

administrativeState:

\$ref:
\'TS28623\_ComDefs.yaml\#/components/schemas/AdministrativeState\'

operationalState:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/OperationalState\'

cellLocalId:

type: integer

cellState:

\$ref: \'\#/components/schemas/CellState\'

plmnInfoList:

\$ref: \'\#/components/schemas/PlmnInfoList\'

nrPci:

\$ref: \'\#/components/schemas/NrPci\'

nrTac:

\$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Tac\'

arfcnDL:

type: integer

arfcnUL:

type: integer

arfcnSUL:

type: integer

bSChannelBwDL:

type: integer

bSChannelBwUL:

type: integer

bSChannelBwSUL:

type: integer

ssbFrequency:

type: integer

minimum: 0

maximum: 3279165

ssbPeriodicity:

\$ref: \'\#/components/schemas/SsbPeriodicity\'

ssbSubCarrierSpacing:

\$ref: \'\#/components/schemas/SsbSubCarrierSpacing\'

ssbOffset:

type: integer

minimum: 0

maximum: 159

ssbDuration:

\$ref: \'\#/components/schemas/SsbDuration\'

nrSectorCarrierRef:

type: array

items:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

bwpRef:

type: array

items:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

rimRSMonitoringStartTime:

type: string

rimRSMonitoringStopTime:

type: string

rimRSMonitoringWindowDuration:

type: integer

rimRSMonitoringWindowStartingOffset:

type: integer

rimRSMonitoringWindowPeriodicity:

type: integer

rimRSMonitoringOccasionInterval:

type: integer

rimRSMonitoringOccasionStartingOffset:

type: integer

nRFrequencyRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

victimSetRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

aggressorSetRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

RRMPolicyRatio:

\$ref: \'\#/components/schemas/RRMPolicyRatio-Multiple\'

CPCIConfigurationFunction:

\$ref: \'\#/components/schemas/CPCIConfigurationFunction-Single\'

DRACHOptimizationFunction:

\$ref: \'\#/components/schemas/DRACHOptimizationFunction-Single\'

NRFrequency-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

type: object

properties:

absoluteFrequencySSB:

type: integer

minimum: 0

maximum: 3279165

ssbSubCarrierSpacing:

\$ref: \'\#/components/schemas/SsbSubCarrierSpacing\'

multiFrequencyBandListNR:

type: integer

minimum: 1

maximum: 256

EUtranFrequency-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

type: object

properties:

earfcnDL:

type: integer

minimum: 0

maximum: 262143

multiBandInfoListEutra:

type: integer

minimum: 1

maximum: 256

NrSectorCarrier-Single:

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

txDirection:

\$ref: \'\#/components/schemas/TxDirection\'

configuredMaxTxPower:

type: integer

arfcnDL:

type: integer

arfcnUL:

type: integer

bSChannelBwDL:

type: integer

bSChannelBwUL:

type: integer

sectorEquipmentFunctionRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

CommonBeamformingFunction:

\$ref: \'\#/components/schemas/CommonBeamformingFunction-Single\'

Bwp-Single:

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

bwpContext:

\$ref: \'\#/components/schemas/BwpContext\'

isInitialBwp:

\$ref: \'\#/components/schemas/IsInitialBwp\'

subCarrierSpacing:

type: integer

cyclicPrefix:

\$ref: \'\#/components/schemas/CyclicPrefix\'

startRB:

type: integer

numberOfRBs:

type: integer

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

CommonBeamformingFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- type: object

properties:

coverageShape:

\$ref: \'\#/components/schemas/CoverageShape\'

digitalAzimuth:

\$ref: \'\#/components/schemas/DigitalAzimuth\'

digitalTilt:

\$ref: \'\#/components/schemas/DigitalTilt\'

\- type: object

properties:

Beam:

\$ref: \'\#/components/schemas/Beam-Multiple\'

Beam-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- type: object

properties:

beamIndex:

type: integer

beamType:

type: string

enum:

\- SSB-BEAM

beamAzimuth:

type: integer

minimum: -1800

maximum: 1800

beamTilt:

type: integer

minimum: -900

maximum: 900

beamHorizWidth:

type: integer

minimum: 0

maximum: 3599

beamVertWidth:

type: integer

minimum: 0

maximum: 1800

RRMPolicyRatio-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \'\#/components/schemas/RrmPolicy\_-Attr\'

\- type: object

properties:

rRMPolicyMaxRatio:

type: integer

default: 100

minimum: 0

maximum: 100

rRMPolicyMinRatio:

type: integer

default: 0

minimum: 0

maximum: 100

rRMPolicyDedicatedRatio:

type: integer

default: 0

minimum: 0

maximum: 100

NRCellRelation-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

type: object

properties:

nRTCI:

type: integer

cellIndividualOffset:

\$ref: \'\#/components/schemas/CellIndividualOffset\'

adjacentNRCellRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

nRFrequencyRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

isRemoveAllowed:

type: boolean

isHOAllowed:

type: boolean

isESCoveredBy:

\$ref: \'\#/components/schemas/IsESCoveredBy\'

isENDCAllowed:

type: boolean

EUtranCellRelation-Single:

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

adjacentEUtranCellRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

NRFreqRelation-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

type: object

properties:

offsetMO:

\$ref: \'\#/components/schemas/QOffsetRangeList\'

blackListEntry:

type: array

items:

type: integer

minimum: 0

maximum: 1007

blackListEntryIdleMode:

type: integer

cellReselectionPriority:

type: integer

cellReselectionSubPriority:

type: number

minimum: 0.2

maximum: 0.8

multipleOf: 0.2

pMax:

type: integer

minimum: -30

maximum: 33

qOffsetFreq:

\$ref: \'\#/components/schemas/QOffsetFreq\'

qQualMin:

type: number

qRxLevMin:

type: integer

minimum: -140

maximum: -44

threshXHighP:

type: integer

minimum: 0

maximum: 62

threshXHighQ:

type: integer

minimum: 0

maximum: 31

threshXLowP:

type: integer

minimum: 0

maximum: 62

threshXLowQ:

type: integer

minimum: 0

maximum: 31

tReselectionNr:

type: integer

minimum: 0

maximum: 7

tReselectionNRSfHigh:

\$ref: \'\#/components/schemas/TReselectionNRSf\'

tReselectionNRSfMedium:

\$ref: \'\#/components/schemas/TReselectionNRSf\'

nRFrequencyRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

EUtranFreqRelation-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

type: object

properties:

cellIndividualOffset:

\$ref: \'\#/components/schemas/CellIndividualOffset\'

blackListEntry:

type: array

items:

type: integer

minimum: 0

maximum: 1007

blackListEntryIdleMode:

type: integer

cellReselectionPriority:

type: integer

cellReselectionSubPriority:

type: number

minimum: 0.2

maximum: 0.8

multipleOf: 0.2

pMax:

type: integer

minimum: -30

maximum: 33

qOffsetFreq:

\$ref: \'\#/components/schemas/QOffsetFreq\'

qQualMin:

type: number

qRxLevMin:

type: integer

minimum: -140

maximum: -44

threshXHighP:

type: integer

minimum: 0

maximum: 62

threshXHighQ:

type: integer

minimum: 0

maximum: 31

threshXLowP:

type: integer

minimum: 0

maximum: 62

threshXLowQ:

type: integer

minimum: 0

maximum: 31

tReselectionEutran:

type: integer

minimum: 0

maximum: 7

tReselectionNRSfHigh:

\$ref: \'\#/components/schemas/TReselectionNRSf\'

tReselectionNRSfMedium:

\$ref: \'\#/components/schemas/TReselectionNRSf\'

eUTranFrequencyRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

DANRManagementFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

type: object

properties:

intrasystemANRManagementSwitch:

type: boolean

intersystemANRManagementSwitch:

type: boolean

DESManagementFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

type: object

properties:

desSwitch:

type: boolean

intraRatEsActivationOriginalCellLoadParameters:

\$ref:
\"\#/components/schemas/IntraRatEsActivationOriginalCellLoadParameters\"

intraRatEsActivationCandidateCellsLoadParameters:

\$ref:
\"\#/components/schemas/IntraRatEsActivationCandidateCellsLoadParameters\"

intraRatEsDeactivationCandidateCellsLoadParameters:

\$ref:
\"\#/components/schemas/IntraRatEsDeactivationCandidateCellsLoadParameters\"

esNotAllowedTimePeriod:

\$ref: \"\#/components/schemas/EsNotAllowedTimePeriod\"

interRatEsActivationOriginalCellParameters:

\$ref:
\"\#/components/schemas/InterRatEsActivationOriginalCellParameters\"

interRatEsActivationCandidateCellParameters:

\$ref:
\"\#/components/schemas/InterRatEsActivationCandidateCellParameters\"

interRatEsDeactivationCandidateCellParameters:

\$ref:
\"\#/components/schemas/InterRatEsDeactivationCandidateCellParameters\"

isProbingCapable:

type: string

enum:

\- yes

\- no

energySavingState:

type: string

enum:

\- isNotEnergySaving

\- isEnergySaving

DRACHOptimizationFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

type: object

properties:

drachOptimizationControl:

type: boolean

ueAccProbabilityDist:

\$ref: \"\#/components/schemas/UeAccProbabilityDist\"

ueAccDelayProbabilityDist:

\$ref: \"\#/components/schemas/UeAccDelayProbabilityDist\"

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

DMROFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

type: object

properties:

dmroControl:

type: boolean

maximumDeviationHoTrigger:

\$ref: \'\#/components/schemas/MaximumDeviationHoTrigger\'

minimumTimeBetweenHoTriggerChange:

\$ref: \'\#/components/schemas/MinimumTimeBetweenHoTriggerChange\'

tstoreUEcntxt:

\$ref: \'\#/components/schemas/TstoreUEcntxt\'

DPCIConfigurationFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

type: object

properties:

dPciConfigurationControl:

type: boolean

nRPciList:

\$ref: \"\#/components/schemas/NRPciList\"

CPCIConfigurationFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

type: object

properties:

cPciConfigurationControl:

type: boolean

cSonPciList:

\$ref: \"\#/components/schemas/CSonPciList\"

CESManagementFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

type: object

properties:

cesSwitch:

type: boolean

intraRatEsActivationOriginalCellLoadParameters:

\$ref:
\"\#/components/schemas/IntraRatEsActivationOriginalCellLoadParameters\"

intraRatEsActivationCandidateCellsLoadParameters:

\$ref:
\"\#/components/schemas/IntraRatEsActivationCandidateCellsLoadParameters\"

intraRatEsDeactivationCandidateCellsLoadParameters:

\$ref:
\"\#/components/schemas/IntraRatEsDeactivationCandidateCellsLoadParameters\"

esNotAllowedTimePeriod:

\$ref: \"\#/components/schemas/EsNotAllowedTimePeriod\"

interRatEsActivationOriginalCellParameters:

\$ref:
\"\#/components/schemas/IntraRatEsActivationOriginalCellLoadParameters\"

interRatEsActivationCandidateCellParameters:

\$ref:
\"\#/components/schemas/IntraRatEsActivationOriginalCellLoadParameters\"

interRatEsDeactivationCandidateCellParameters:

\$ref:
\"\#/components/schemas/IntraRatEsActivationOriginalCellLoadParameters\"

energySavingControl:

type: string

enum:

\- toBeEnergySaving

\- toBeNotEnergySaving

energySavingState:

type: string

enum:

\- isNotEnergySaving

\- isEnergySaving

RimRSGlobal-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

type: object

properties:

frequencyDomainPara:

\$ref: \'\#/components/schemas/FrequencyDomainPara\'

sequenceDomainPara:

\$ref: \'\#/components/schemas/SequenceDomainPara\'

timeDomainPara:

\$ref: \'\#/components/schemas/TimeDomainPara\'

RimRSSet:

\$ref: \'\#/components/schemas/RimRSSet-Multiple\'

RimRSSet-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

type: object

properties:

setId:

\$ref: \'\#/components/schemas/RSSetId\'

setType:

\$ref: \'\#/components/schemas/RSSetType\'

nRCellDURefs:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/DnList\'

ExternalGnbDuFunction-Single:

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

gnbId:

\$ref: \'\#/components/schemas/GnbId\'

gnbIdLength:

\$ref: \'\#/components/schemas/GnbIdLength\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

EP\_F1C:

\$ref: \'\#/components/schemas/EP\_F1C-Multiple\'

EP\_F1U:

\$ref: \'\#/components/schemas/EP\_F1U-Multiple\'

ExternalGnbCuUpFunction-Single:

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

gnbId:

\$ref: \'\#/components/schemas/GnbId\'

gnbIdLength:

\$ref: \'\#/components/schemas/GnbIdLength\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

EP\_E1:

\$ref: \'\#/components/schemas/EP\_E1-Multiple\'

EP\_F1U:

\$ref: \'\#/components/schemas/EP\_F1U-Multiple\'

EP\_XnU:

\$ref: \'\#/components/schemas/EP\_XnU-Multiple\'

ExternalGnbCuCpFunction-Single:

allOf:

\- \$ref: \'TS28623\_GenericNrm.yaml\#/components/schemas/Top\'

\- type: object

properties:

attributes:

allOf:

\- \$ref: \>-

TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-Attr

\- type: object

properties:

gnbId:

\$ref: \'\#/components/schemas/GnbId\'

gnbIdLength:

\$ref: \'\#/components/schemas/GnbIdLength\'

plmnId:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/PlmnId\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

ExternalNrCellCu:

\$ref: \'\#/components/schemas/ExternalNrCellCu-Multiple\'

EP\_XnC:

\$ref: \'\#/components/schemas/EP\_XnC-Multiple\'

EP\_E1:

\$ref: \'\#/components/schemas/EP\_E1-Multiple\'

EP\_F1C:

\$ref: \'\#/components/schemas/EP\_F1C-Multiple\'

ExternalNrCellCu-Single:

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

cellLocalId:

type: integer

nrPci:

\$ref: \'\#/components/schemas/NrPci\'

plmnIdList:

\$ref: \'\#/components/schemas/PlmnIdList\'

nRFrequencyRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

ExternalENBFunction-Single:

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

eNBId:

type: integer

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

\- type: object

properties:

ExternalEUTranCell:

\$ref: \'\#/components/schemas/ExternalEUTranCell-Multiple\'

ExternalEUTranCell-Single:

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

EUtranFrequencyRef:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/Dn\'

\- \$ref:
\'TS28623\_GenericNrm.yaml\#/components/schemas/ManagedFunction-ncO\'

EP\_XnC-Single:

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

\$ref: \'\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'\#/components/schemas/RemoteAddress\'

EP\_E1-Single:

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

\$ref: \'\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'\#/components/schemas/RemoteAddress\'

EP\_F1C-Single:

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

\$ref: \'\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'\#/components/schemas/RemoteAddress\'

EP\_NgC-Single:

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

\$ref: \'\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'\#/components/schemas/RemoteAddress\'

EP\_X2C-Single:

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

\$ref: \'\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'\#/components/schemas/RemoteAddress\'

EP\_XnU-Single:

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

\$ref: \'\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'\#/components/schemas/RemoteAddress\'

EP\_F1U-Single:

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

\$ref: \'\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'\#/components/schemas/RemoteAddress\'

EP\_NgU-Single:

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

\$ref: \'\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'\#/components/schemas/RemoteAddress\'

epTransportRefs:

\$ref: \'TS28623\_ComDefs.yaml\#/components/schemas/DnList\'

EP\_X2U-Single:

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

\$ref: \'\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'\#/components/schemas/RemoteAddress\'

EP\_S1U-Single:

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

\$ref: \'\#/components/schemas/LocalAddress\'

remoteAddress:

\$ref: \'\#/components/schemas/RemoteAddress\'

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

GnbDuFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/GnbDuFunction-Single\'

GnbCuUpFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/GnbCuUpFunction-Single\'

GnbCuCpFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/GnbCuCpFunction-Single\'

NrCellDu-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/NrCellDu-Single\'

NrCellCu-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/NrCellCu-Single\'

NRFrequency-Multiple:

type: array

minItems: 1

items:

\$ref: \'\#/components/schemas/NRFrequency-Single\'

EUtranFrequency-Multiple:

type: array

minItems: 1

items:

\$ref: \'\#/components/schemas/EUtranFrequency-Single\'

NrSectorCarrier-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/NrSectorCarrier-Single\'

Bwp-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/Bwp-Single\'

Beam-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/Beam-Single\'

RRMPolicyRatio-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/RRMPolicyRatio-Single\'

NRCellRelation-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/NRCellRelation-Single\'

EUtranCellRelation-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EUtranCellRelation-Single\'

NRFreqRelation-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/NRFreqRelation-Single\'

EUtranFreqRelation-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EUtranFreqRelation-Single\'

RimRSSet-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/RimRSSet-Single\'

ExternalGnbDuFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/ExternalGnbDuFunction-Single\'

ExternalGnbCuUpFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/ExternalGnbCuUpFunction-Single\'

ExternalGnbCuCpFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/ExternalGnbCuCpFunction-Single\'

ExternalNrCellCu-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/ExternalNrCellCu-Single\'

ExternalENBFunction-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/ExternalENBFunction-Single\'

ExternalEUTranCell-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/ExternalEUTranCell-Single\'

EP\_E1-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_E1-Single\'

EP\_XnC-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_XnC-Single\'

EP\_F1C-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_F1C-Single\'

EP\_NgC-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_NgC-Single\'

EP\_X2C-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_X2C-Single\'

EP\_XnU-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_XnU-Single\'

EP\_F1U-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_F1U-Single\'

EP\_NgU-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_NgU-Single\'

EP\_X2U-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_X2U-Single\'

EP\_S1U-Multiple:

type: array

items:

\$ref: \'\#/components/schemas/EP\_S1U-Single\'

\#\-\-\-\-\-\-\-- Definitions in TS 28.541 for TS 28.532
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

resources-nrNrm:

oneOf:

\- \$ref: \'\#/components/schemas/MnS\'

\- \$ref: \'\#/components/schemas/SubNetwork-Single\'

\- \$ref: \'\#/components/schemas/ManagedElement-Single\'

\- \$ref: \'\#/components/schemas/GnbDuFunction-Single\'

\- \$ref: \'\#/components/schemas/GnbCuUpFunction-Single\'

\- \$ref: \'\#/components/schemas/GnbCuCpFunction-Single\'

\- \$ref: \'\#/components/schemas/NrCellCu-Single\'

\- \$ref: \'\#/components/schemas/NrCellDu-Single\'

\- \$ref: \'\#/components/schemas/NRFrequency-Single\'

\- \$ref: \'\#/components/schemas/EUtranFrequency-Single\'

\- \$ref: \'\#/components/schemas/NrSectorCarrier-Single\'

\- \$ref: \'\#/components/schemas/Bwp-Single\'

\- \$ref: \'\#/components/schemas/CommonBeamformingFunction-Single\'

\- \$ref: \'\#/components/schemas/Beam-Single\'

\- \$ref: \'\#/components/schemas/RRMPolicyRatio-Single\'

\- \$ref: \'\#/components/schemas/NRCellRelation-Single\'

\- \$ref: \'\#/components/schemas/EUtranCellRelation-Single\'

\- \$ref: \'\#/components/schemas/NRFreqRelation-Single\'

\- \$ref: \'\#/components/schemas/EUtranFreqRelation-Single\'

\- \$ref: \'\#/components/schemas/DANRManagementFunction-Single\'

\- \$ref: \'\#/components/schemas/DESManagementFunction-Single\'

\- \$ref: \'\#/components/schemas/DRACHOptimizationFunction-Single\'

\- \$ref: \'\#/components/schemas/DMROFunction-Single\'

\- \$ref: \'\#/components/schemas/DPCIConfigurationFunction-Single\'

\- \$ref: \'\#/components/schemas/CPCIConfigurationFunction-Single\'

\- \$ref: \'\#/components/schemas/CESManagementFunction-Single\'

\- \$ref: \'\#/components/schemas/RimRSGlobal-Single\'

\- \$ref: \'\#/components/schemas/RimRSSet-Single\'

\- \$ref: \'\#/components/schemas/ExternalGnbDuFunction-Single\'

\- \$ref: \'\#/components/schemas/ExternalGnbCuUpFunction-Single\'

\- \$ref: \'\#/components/schemas/ExternalGnbCuCpFunction-Single\'

\- \$ref: \'\#/components/schemas/ExternalNrCellCu-Single\'

\- \$ref: \'\#/components/schemas/ExternalENBFunction-Single\'

\- \$ref: \'\#/components/schemas/ExternalEUTranCell-Single\'

\- \$ref: \'\#/components/schemas/EP\_XnC-Single\'

\- \$ref: \'\#/components/schemas/EP\_E1-Single\'

\- \$ref: \'\#/components/schemas/EP\_F1C-Single\'

\- \$ref: \'\#/components/schemas/EP\_NgC-Single\'

\- \$ref: \'\#/components/schemas/EP\_X2C-Single\'

\- \$ref: \'\#/components/schemas/EP\_XnU-Single\'

\- \$ref: \'\#/components/schemas/EP\_F1U-Single\'

\- \$ref: \'\#/components/schemas/EP\_NgU-Single\'

\- \$ref: \'\#/components/schemas/EP\_X2U-Single\'

\- \$ref: \'\#/components/schemas/EP\_S1U-Single\'
