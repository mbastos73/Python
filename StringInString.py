def fix_machine(debris, product):
  for let in product:
    if let not in debris:
      return "Give me something that's not useless next time."
  return product

### TEST CASES ###
print(fix_machine('UdaciousUdacitee', 'Udacity'))
print(fix_machine('buy me dat Unicorn', 'Udacity'))
print(fix_machine('AEIOU and sometimes y... c', 'Udacity'))
print(fix_machine('wsx0-=mttrhix', 't-shirt'))

print()
print()
print()

print("Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time.")
print("Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity')
print("Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity')
print("Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt')
