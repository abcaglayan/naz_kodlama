# ürünler = [["çikolata",50],["biskuvi",40],["şeker",60],["un",48]]
# sepet_tutarı= 0
#
# for ürün in ürünler:
#     isim = ürün[0]
#     fiyat = ürün[1]
#     print(f"{isim} -> {fiyat}")
#
# hak = 5
# while hak > 0:
#     hak -= 1
#     ürün_stok = False
#     if hak == 0:
#         alınacak_ürün = input("Hoşgeldin, hangi ürünü alak istersin?(ürün almak istemiyorsan hayır)")
#     else:
#         alınacak_ürün = input("Başka hangi ürünü alak istersin?(ürün almak istemiyorsan hayır)")
#
#     if alınacak_ürün == 'hayır':
#         # option 1
#         hak = 0
#         # option 2
#         break
#     if alınacak_ürün != "hayır":
#         for ürün in ürünler:
#             isim = ürün[0]
#             fiyat = ürün[1]
#             if alınacak_ürün == isim:
#                 sepet_tutarı += fiyat
#                 ürün_stok = True
#
#     if ürün_stok == False:
#         print("ürün stokta yok")
#
#     print(sepet_tutarı)

# range 1-100 arası olacak şekilde 3ün katlarını 3peer - <sayı> formatında yazdır

# current = 0
# while (current < 100):
#     current += 1
#
#     if current % 3 == 0:
#         print (f"3peer - {current}")


# kullanıcı 0 inputu girene kadar girilen sayıları topla

# sum = 0
# number = int(input("Enter a number: "))
# sum = number + sum
# print(sum)
#
# while (number != 0):
#     number = int(input("Enter a number: "))
#     sum = number + sum
#     print(sum)
#
# sum = 0
# while True:
#     number = int(input("Enter a number: "))
#
#     if number == 0:
#         print("exiting...")
#         break
#
#     sum = number + sum
#     print(f"sum is {sum} since you entered {number}")

# ispalindrome defabcbaasd


# kullanıcıdan input alalım sayı tek mi çif mi kontrol edelim
# çift ise even listesine
# tek ise odd listesine ekle

even = []
odd = []
while True:
    number = int(input("Enter a number (100 to break the function): "))

    if number == 100:
        print(f"the even list is {even}")
        print(f"the odd list is {odd}")
        break

    if number%2 == 0:
        even.append(number)
        print(f"{number}-> even list")
    else:
        odd.append(number)
        print(f"{number}-> odd list")


