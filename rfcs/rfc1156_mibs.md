# RFC 1156 - Management Information Base for Network Management of TCP/IP-based internets

# 1. Status of this Memo


# 2. IAB Policy Statement

first edition of an evolving document on MIBs

_IAB_ - Internet Activities Board - recommends all TCP/IP-based internets be network manageable.  

# 3. Introduction

Two Parts to Internet Management

_MIB_ - Management Information Base for use with network mgmt protocols in TCP/IP-based internets.  That's what this doc covers.

_Network Management Protocol_ - Either SNMP or CMOT


IAB designated both as full "Standard Protocols" with "Recommended" status. "Keep SNMP Simple!"


Current Network Management framework to TCP/IP-based internets consists of:
* Structure and Identification of Management Information for TCP/IP-based Internets, which describes how managed objects contained in the MIB are defined as set forth (RFC 1155)
* MIBs - Management Information Base for use with network mgmt  which describes the managed objects contained in the MIB (RFC 1156)
* the Simple Network Management Protocol, which defines the protocol used to manage these objects (RFC 1157)

Rest of doc describes objects considered essential.  Doc lays out a criteria for essential (ie. evidence of current use, exclude impl-specific like BSD UNIX)


# 4. Objects

_MIB_ defined again but this time as a virtual information store which managed objectsare accessed

Describing these objects by three parts
* name or unique OID which can often be a textual str
* syntax defines the ADS corresponding to obj type using ASN.1 language
* encoding is how an object type is repr from syntax

## 4.1 Object Groups

Grouping provides a means of assigning object identifiers, and a method for implementations of managed agents.

* System
* Interfaces
* Address Translation
* IP
* ICMP
* TCP
* UDP
* EGP (Ext. Gateway Protocol)

## 4.2 Format of Definitions

Described by the following fields
* Name and syntax as defined above
* Definition - a textual human readable format for implementations to follow
* Access - read/write/nonaccessible
* Status - mandatory/optional/obsolete




# 5. Object Definitions
This is the bulk of the document
```
   RFC1156-MIB

   DEFINITIONS ::= BEGIN

   IMPORTS
		   mgmt, OBJECT-TYPE, NetworkAddress, IpAddress,
		   Counter, Gauge, TimeTicks
			   FROM RFC1155-SMI;

   mib        OBJECT IDENTIFIER ::= { mgmt 1 }

   system     OBJECT IDENTIFIER ::= { mib 1 }
   interfaces OBJECT IDENTIFIER ::= { mib 2 }
   at         OBJECT IDENTIFIER ::= { mib 3 }
   ip         OBJECT IDENTIFIER ::= { mib 4 }
   icmp       OBJECT IDENTIFIER ::= { mib 5 }
   tcp        OBJECT IDENTIFIER ::= { mib 6 }
   udp        OBJECT IDENTIFIER ::= { mib 7 }
   egp        OBJECT IDENTIFIER ::= { mib 8 }

   END
```
  5.1 The System Group .....................................   9
   5.2 The Interfaces Group .................................  11
   5.2.1 The Interfaces Table ...............................  11
   5.3 The Address Translation Group ........................  23
   5.4 The IP Group .........................................  26
   5.4.1 The IP Address Table ...............................  34
   5.4.2 The IP Routing Table ...............................  36
   5.5 The ICMP Group .......................................  43
   5.6 The TCP Group ........................................  53
   5.7 The UDP Group ........................................  62
   5.8 The EGP Group ........................................  64
   5.8.1 The EGP Neighbor Table .............................  65
