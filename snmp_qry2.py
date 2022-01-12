from pysnmp.hlapi import *

iterator = getCmd(
    SnmpEngine(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget(('127.0.0.1', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
)
#ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
#업타임(단위 sec): ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysUpTime', 0))
#PC이름: ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysName', 0))

errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
print(f"errorIndication: {errorIndication}")
print(f"errorStatus: {errorStatus}")
print(f"errorIndex: {errorIndex}")
print(f"varBinds: {varBinds}")


if errorIndication:
    print(errorIndication)

elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))