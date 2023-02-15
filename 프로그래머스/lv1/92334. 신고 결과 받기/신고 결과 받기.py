def solution(id_list, report, k):
    
    user_dic = {i : 0 for i in id_list}

    report_dic = {}
    for i in set(report):
        user, reports = i.split(' ')
        if reports in report_dic:
            report_dic[reports] += [user]
        else:
            report_dic[reports] = [user]

    reports = []
    for v in report_dic.values():
        if len(v) >= k:
            reports += v
    
    # reports = sum([v for v in report_dic.values() if len(v) >= k], [])

    for name in reports:
        if name in user_dic:
            user_dic[name] += 1

    return list(user_dic.values())