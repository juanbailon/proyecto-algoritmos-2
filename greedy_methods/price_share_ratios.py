from typing import List, Union
from data_structures.heaps import MaxHeapForOffersRatios, MaxHeap


def price_shares_ratio_criteria(total_shares: int, share_min_price: float, total_offers:int, buying_offers: List[List], ratio_type= 1):
    """  """
    max_heap = MaxHeap()

    for id, offer in enumerate(buying_offers):
        if(id<len(buying_offers)-1):
            ratio=0
            if(ratio_type==1):
                ratio = offer[0]/offer[1] if offer[1]!=0 else 0
            elif(ratio_type==2):
                ratio = offer[1]/offer[0] if offer[0]!=0 else 0
            elif(ratio_type==3):
                ratio = offer[0]/offer[2] if offer[2]!=0 else 0
            elif(ratio_type==4):
                ratio = offer[2]/offer[0] if offer[0]!=0 else 0
            
            max_heap.add([ratio, offer])

    print(max_heap)

    sum = 0
    sold_shares = 0
    accepted_offers = []

    print("size: ", max_heap.size)
    for i in range(max_heap.size):
        print("i = ", i)
        root_offer = max_heap.poll()
        price_per_share = root_offer[1][0]
        max_shares = root_offer[1][1]
        
        sold_shares += max_shares
        print("sold_shares", sold_shares)
        print(root_offer[1])
        
        if(sold_shares == total_shares):
            sum += (price_per_share*max_shares)
            accepted_offers.append([i, max_shares, root_offer])
            break
        elif(sold_shares > total_shares):
            sold_shares -= max_shares
            diff = total_shares - sold_shares
            print("dif", diff)
            if(root_offer[1][2] < diff):
                sold_shares += diff
                sum += (diff*price_per_share)
                accepted_offers.append([i, diff, root_offer])
                break
        else:
            sum += (price_per_share*max_shares)
            accepted_offers.append([i, max_shares, root_offer])
        
        print(sold_shares)
        print("---------------------------")


    if(sold_shares < total_shares):
        gov_shares = total_shares - sold_shares
        print("gov_shares ", gov_shares)
        gov_price = buying_offers[-1][0]
        sum += (gov_price*gov_shares)
        accepted_offers.append([gov_shares, buying_offers[-1]])

    print("######################")


    return (sum, accepted_offers)



