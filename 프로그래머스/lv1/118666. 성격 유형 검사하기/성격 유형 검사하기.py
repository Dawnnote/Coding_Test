def solution(survey, choices):
    test = [-3, -2, -1, 0, 1, 2, 3]

    for idx, choice in enumerate(choices):
        choices[idx] = test[choice-1]

    survey_dic = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for idx, num in enumerate(choices):
        if num <= 0:
            survey_dic[survey[idx][0]] += abs(num)
        elif num >= 0:
            survey_dic[survey[idx][1]] += num


    survey_ty = list(survey_dic.keys())
    survey_num = list(survey_dic.values())

    result = ''
    for i in range(2,len(survey_ty)+1,2):
        if survey_num[i-2] >= survey_num[i-1]:
            result += survey_ty[i-2]
        elif survey_num[i-2] < survey_num[i-1]:
            result += survey_ty[i-1]

    return result

###############################
# def solution(survey, choices):

#     my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
#     for A,B in zip(survey,choices):
#         if A not in my_dict.keys():
#             A = A[::-1]
#             my_dict[A] -= B-4
#         else:
#             my_dict[A] += B-4

#     result = ""
#     for name in my_dict.keys():
#         if my_dict[name] > 0:
#             result += name[1]
#         elif my_dict[name] < 0:
#             result += name[0]
#         else:
#             result += sorted(name)[0]

#     return result

###########################################
# def solution(survey, choices):
#     answer = ''

#     scores = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0 }
#     add_score = {1:3, 2:2, 3:1, 4:0, 5:-1, 6:-2, 7:-3}

#     for i in range(len(survey)):
#         scores[survey[i][0]] += add_score[choices[i]]

#     answer += "R" if scores["R"] >= scores["T"] else "T"
#     answer += "C" if scores["C"] >= scores["F"] else "F"
#     answer += "J" if scores["J"] >= scores["M"] else "M"
#     answer += "A" if scores["A"] >= scores["N"] else "N"

#     return answer