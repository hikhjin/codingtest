bagW, metal = map(int, input().split()) # 배낭 최대 무게, 귀금속 개수
max_price = 0 # 최대 가격
metal_weight = []
metal_price = []
for i in range(1, metal + 1):
    metalW, metalP = map(int, input().split())
    metal_weight.append(metalW) # 귀금속 무게, 가격 따로 리스트로 받음
    metal_price.append(metalP)


while(bagW != 0):
    max_index = metal_price.index(max(metal_price)) # 최댓값 인덱스
    if bagW - max(metal_weight) > 0:

        max_price += max(metal_price) * metal_weight[max_index]
        bagW -= metal_weight[max_index]
        del metal_weight[max_index]
        del metal_price[max_index]
        if len(metal_price) == 0:
            break

    elif bagW - max(metal_weight) <= 0:
        max_price += bagW * metal_price[max_index]
        bagW -= metal_weight[max_index]
        break

print(max_price)