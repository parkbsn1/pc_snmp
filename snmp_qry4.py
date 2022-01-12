from pysnmp.hlapi import *
g = bulkCmd(
    SnmpEngine(),
    CommunityData('public'),
    UdpTransportTarget(('127.0.0.1', 161)),
    ContextData(),
    0, 25,
    ObjectType(ObjectIdentity('SNMPv2-MIB', 'hrSWRunName'))
)

#ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr'))

print(type(g))
print(next(g))