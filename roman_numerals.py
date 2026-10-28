
def to_roman_lazy(num):
  roman_obj={
    1:"I",
    5:"V",
    10:"X",
    50:"L",
    100:"C",
    500:"D",
    1000:"M"
  }
  
  arabic_nums = list(roman_obj.keys())
  arabic_nums.reverse()
  arabic_nums_that_work = list(filter(lambda i: num//i>=1, arabic_nums))

  roman_version = ""
  
  
  for number in range(len(arabic_nums_that_work)):
    quotient = num//arabic_nums_that_work[number]
    remainder = num%arabic_nums_that_work[number]
    if remainder==0 and quotient*arabic_nums_that_work[number]==num:
      roman_version+=roman_obj[arabic_nums_that_work[number]]*quotient
      break
    else:
      roman_version+=roman_obj[arabic_nums_that_work[number]]*quotient
      num=remainder
  return roman_version


def to_roman(num):
  roman_obj_two={
    1:"I",
    4:"IV",
    5:"V",
    9:"IX",
    10:"X",
    40:"XL",
    50:"L",
    100:"C",
    400:"CD",
    500:"D",
    900:"CM",
    1000:"M"
  }
  arabic_nums=list(roman_obj_two.keys())
  arabics_that_work = list(filter(lambda number: num//number>=1, arabic_nums))
  arabics_that_work.reverse()
  roman_version_two =""
  for number in range(len(arabics_that_work)):
    quotient=num//arabics_that_work[number]
    remainder = num%arabics_that_work[number]
    if remainder==0 and quotient*arabics_that_work[number]==num:
      roman_version_two+=roman_obj_two[arabics_that_work[number]]*quotient
      break
    else:
      roman_version_two+=roman_obj_two[arabics_that_work[number]]*quotient
      num=remainder
    
  
  return roman_version_two

print(to_roman(1), to_roman(40), to_roman(400), to_roman(450))




