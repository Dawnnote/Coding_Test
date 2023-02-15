def convert_day(date):
    y, m, d = date.split('.')
    return 28*12*int(y) + int(m)*28+int(d) # 문제에서 한달은 28일

def solution(today, terms, privacies):
    
    today = convert_day(today)
    
    terms_dic = {}
    for term in terms:
        typ, month = term.split(' ')
        terms_dic[typ] = int(month) * 28 
    
    result = []
    for idx, privacy in enumerate(privacies, start = 1):
        date, typ = privacy.split(' ')
        date = convert_day(date) + terms_dic[typ]
        
        if date <= today:
            result.append(idx)
    
    return result