def solution(lines):
    st = []
    for i in lines:
        st.append(set(range(min(i), max(i))))
        
    result = len(st[0] & st[1] | st[1] & st[2] | st[0] & st[2])
    
    return result
