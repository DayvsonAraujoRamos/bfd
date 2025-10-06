# lista = [1,2,3,4,5]
# print (list(map(lambda num:num*2, lista) ))
# #=========================================
# lista = [10,15,20,25,30]
# print (list(filter(lambda num:num%2 ==0 ,lista)))
# # ==========================================
# from functools import reduce
# lista =[1,2,3,4,5]
# print (reduce(lambda x,y: x+y,lista))
# # ==============
# fruta =  ["uva", "banana", "maçã", "laranja"]
# ordenadas = sorted(fruta,key = lambda x:len(x))
# print(ordenadas)
# # =====================================
# nomes = ["ana","pedro","maria"]
# nomes_c = list(map(lambda x:x.capitalize(),nomes))
# print(nomes_c)
# # ============================
# from functools import reduce
# lista = [2,3,4,5]
# print(reduce(lambda x,y:x*y,lista))
# # ================================
frutas = ["banana","uva","maçã","laranja"] 
ordenadas = sorted(frutas, key=lambda x: x[-1])
print(ordenadas)
