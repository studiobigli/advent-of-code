def distance() -> dict:
    left_list: list[int] = [] 
    right_list: list[int] = []
    distance_list: list[int] = []

    with open('day1.txt', 'r') as f:
        for line in f:
            left_list.append(int(line.split()[0]))
            right_list.append(int(line.split()[1]))
    left_list.sort()
    right_list.sort()

    for i in range(len(left_list)):
        distance_list.append(max(left_list[i], right_list[i]) - min(left_list[i], right_list[i]))
    sum_distance: int = sum(distance_list)
    return {"distance": sum_distance, "left list": left_list, "right list": right_list}

def similarity(left_list: list[int], right_list: list[int]) -> int:
    similarity_list: list[int] = []

    for i in left_list:
        i_score = 0
        for j in right_list:
            if j == i:
                i_score += 1
        similarity_list.append(i*i_score)
    
    return sum(similarity_list)

if __name__ == "__main__":
    distance_result = distance()
    similarity_result = similarity(distance_result["left list"], distance_result["right list"])

    print(f"TOTAL DISTANCE: {distance_result["distance"]}")
    print(f"SIMILARITY SCORE: {similarity_result}")