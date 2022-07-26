def intToRoman(self, num: int) -> str:
    # ans = ''
    # while(num>0):
    #     if num>=1000:
    #         ans+='M'
    #         num-=1000
    #     elif 900<=num<1000:
    #         ans+='CM'
    #         num-=900
    #     elif 500<=num<900:
    #         ans+='D'
    #         num-=500
    #     elif 400<=num<500:
    #         ans+='CD'
    #         num-=400
    #     elif 100<=num<400:
    #         ans+='C'
    #         num-=100
    #     elif 90<=num<100:
    #         ans+='XC'
    #         num-=90
    #     elif 50<=num<90:
    #         ans+='L'
    #         num-=50
    #     elif 40<=num<50:
    #         ans+='XL'
    #         num-=40
    #     elif 10<=num<40:
    #         ans+='X'
    #         num-=10
    #     elif 9<=num<10:
    #         ans+='IX'
    #         num-=9
    #     elif 5<=num<9:
    #         ans+='V'
    #         num-=5
    #     elif 4<=num<5:
    #         ans+='IV'
    #         num-=4
    #     else:
    #         ans+='I'
    #         num-=1
    # return ans
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    res = ""
    for i, v in enumerate(values):
        res += (num//v) * numerals[i]
        num %= v
    return res