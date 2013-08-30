#!/usr/bin/python

# what are the last ten digits of 28433x2**7830457 + 1

from datetime import datetime

begin = datetime.now()
hardbit = long(str(2**1000000)[-11:])
medbit = long(str(2**830457)[-11:])
#b = str(28433* (2**2830457)+1)
softbit = (hardbit**7)*medbit*28433 + 1
answer = str(softbit)[-10:]

end = datetime.now()
print end-begin
print answer
