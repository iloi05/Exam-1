def list_of_names(scores):
    if scores == 0:
        print("The student dictionary is empty")
        return None
    else:
        name_list=[]
        for p in scores.values():
            name_list.append([p["lastname"], p["firstname"]])
        name_list.sort(key=lambda x: x[0])
        return name_list

def student_hw_avg(scores, /, *, id):
    if id not in scores:
        print("This student is not in the student dictionary")
        return None
    else:
        avg = sum(scores[id]["HW_scores"])/len(scores[id]["HW_scores"])
        return avg

def class_hw_avg(scores, /, *, hw_index):
    total = 0
    count = 0
    if hw_index < 0 and hw_index >= 3:
        print("Out of range")
        return None
    else:
        for s in scores.values():
            hw_scores = s["HW_scores"]
            if hw_index < len(hw_scores):
                total += hw_scores[hw_index]
                count += 1
        return total/count