import calc_type as ct
import complex_oper as co
import rational_oper as ro

type = ct.type()
print(type)
if type == 'complex':
    x = co.x()
    y = co.y()
    operation = co.selectoperation()
    res = co.res(x, y)
    co.record(x, y, res)

if type == 'rational':
    x = ro.x()
    y = ro.y()
    operation = ro.selectoperation()
    res = ro.res(x, y)
    ro.record(x, y, res)

