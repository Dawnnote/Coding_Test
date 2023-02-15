def solution(s):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    # s = s.lower()
    # st = 0
    
    if len(s) == 4 or len(s) ==6:
        if s.isdigit():
            return True
        else:
            return False
        
    return False
#         for i in range(len(s)):
#             if s[i] in abc:
#                 st = 1

#         if st == 1:
#             return False
#         elif st == 0:
#             return True
    
#     return False
        
    
    