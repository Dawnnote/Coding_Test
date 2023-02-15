def solution(id_pw, db):

    for i in range(len(db)):
        if db[i] == id_pw:
            return "login"
        elif db[i][0] == id_pw[0] and db[i][1] != id_pw[1]:
            return "wrong pw"
    
    return "fail"