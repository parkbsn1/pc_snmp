from pysnmp.hlapi import *

iterator = getCmd(
    SnmpEngine(),
    CommunityData('public'),
    UdpTransportTarget(('127.0.0.1', 161)),
    ContextData(),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.4.20.1.5.127.0.0.1')),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.1.3.0')),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.6.3'))
)

#uptime: 1.3.6.1.2.1.1.3.0
#mac: 1.3.6.1.2.1.2.2.1.6.N

errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
print(f"1) errorIndication: {errorIndication}")
print(f"2) errorStatus: {errorStatus}")
print(f"3) errorIndex: {errorIndex}")
print(f"4) varBinds(type:{type(varBinds)}/len:{len(varBinds)}): {varBinds}")
print('-'*30)


if errorIndication:
    print(errorIndication)

elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

else:
    for varBind in varBinds:
        print(f"{varBind}")
        print(' = '.join([x.prettyPrint() for x in varBind]))