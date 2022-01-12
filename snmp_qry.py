from puresnmp import get
from puresnmp.api.raw import get as raw_get

ip = "127.0.0.1"
community = "public"
oid = '.1.3.6.1.2.1.1'  # only an example

# result = get(ip, community, oid)
raw_result = raw_get(ip, community, oid)
# print(type(result), repr(result))
print(type(raw_result), repr(raw_result))

