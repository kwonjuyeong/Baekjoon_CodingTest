for test_case in range(1,11):
    result = 0
    building = int(input())
    building_height = list(map(int , input().split()))
    for i in range(2, building-2):
        def_2 = building_height[i] - building_height[i-2]
        def_1 = building_height[i] - building_height[i-1]
        def1 = building_height[i] - building_height[i+1]
        def2 = building_height[i] - building_height[i+2]
        if def_2 > 0 and def_1 > 0 and def1 > 0 and def2 > 0 :
            result += min(def_2, def_1, def1, def2)

    print("#{} {}".format(test_case,result))