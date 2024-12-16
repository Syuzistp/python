# def filter_words():

#     # bacenq fayly text-y kardalu hamar
#     with open('filter_words.txt', 'r') as file:

#         # spliti mijocov texty bajanum enq bareri
#         text = file.read().split()

    
#         filter_text = {} # ays dict-i mej havaqelu enq baolor handipac barery ev dranc hajaxakanutyunnery

    
#         for i in text:
#             if i.isalpha():
#                 # ete bary chka dict-i mej avelacnum enq
#                 if i not in filter_text:
#                     filter_text[i] = 1
#                 # ete ka dict-i mej avelacnum enq 1ov
#                 else:
#                     filter_text[i] += 1
            
#         # sortavorum enq yst handipac bareri hajaxakanutyan
#         sorted_words = sorted(filter_text.items(),key=lambda x: x[1],reverse=True)
        
#         # cuyc enq talis amenashat handipac 10 barery
#         top_ten = sorted_words[:10]

        
#         return top_ten


# top_words = filter_words()

# # tpum enq 10 amenshat handipac barery ev dranc hajaxakanutyuny
# for k,w in top_words:
#     print(k,w)