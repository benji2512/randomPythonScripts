def BinaryToDecimal(num):
    num = list(num)
    numr = num[::-1]
    numn = []
    i = 0
    while i < len(numr):
        c = int(numr[i]) * (2 ** i)
        numn.append(c)
        i += 1
    print(sum(numn))

def DecimalToBinary(num):
    binary = []
    while num >= 1:
        rem = num % 2
        binary.append(str(rem))
        num = num // 2
    i = 0
    decimals = ''
    while i < len(binary):
        decimals = decimals + binary[i]
        i += 1
    print(decimals[::-1])

def main():
   askq = input('Would you like to try a number?(yes/no) : ')
   while askq == 'yes':
      dec = input('Is your number Decimal or Binary? : ')
      if dec == 'Decimal':
         num = int(input('What is your number : '))
         DecimalToBinary(num)
      elif dec == 'Binary':
         num = input('What is your number : ')
         BinaryToDecimal(num)
      else:
         print('Please enter Decimal or Binary!')
      askq = input('Would you like to try a number?(yes/no) : ')

if __name__ == '__main__':
    main()
