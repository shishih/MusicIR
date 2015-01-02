import math

def calc_cos(v1,v2):
    if len(v1) != len(v2):
        print('the length of the two vector dosn\'t match')
        raise SystemExit
    length = len(v1)
    sxy = 0.0
    sx2 = 0.0
    sy2 = 0.0
    for i in range(1,length):
        sxy += float(v1[i]) * float(v2[i])
        sx2 += float(v1[i]) * float(v1[i])
        sy2 += float(v2[i]) * float(v2[i])
    if sx2 * sy2 == 0:
        return 0
    else:
        result = sxy / math.sqrt(sx2 * sy2)
        return result

def calc_dis(v1,v2):
    if len(v1) != len(v2):
        print('the length of the two vector dosn\'t match')
        raise SystemExit
    length = len(v1)
    result2 = 0.0
    for i in range(1,length):
        result2 += (float(v1[i]) - float(v2[i])) ** 2
    return result2

def compare(kw_only1, kw_only2):
    return kw_only1[1] - kw_only2[1]