def smart_power(podstawa, wykladnik):
    if wykladnik == 1:
        return podstawa
    if not(wykladnik % 2):
        return smart_power(podstawa, wykladnik//2)*smart_power(podstawa, wykladnik//2)
    else:
        return smart_power(podstawa, wykladnik//2)*smart_power(podstawa, wykladnik//2)*podstawa

def is_palindrome(tested_string):
    for i in range(len(tested_string)//2):
        if (tested_string[i]==tested_string[-(i+1)]):
            bool_value = True
        else: 
            return False
    return bool_value
    
def occurance(tested_list):
    count = 0
    for i in set(tested_list): 
        number_of_occurances = tested_list.count(i)
        if(number_of_occurances>count):
            count = number_of_occurances
            value =i
    return value


def main():
    print(smart_power(2,7))
    print(is_palindrome('xDddd'))
    print(occurance([1,1,1,4,5,3,3,5,3,2,3,3,3]))
if __name__ == "__main__":
    main()
