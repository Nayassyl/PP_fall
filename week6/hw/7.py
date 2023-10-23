import re
class creditCard():
    def __init__(self, inp):
        self.number = inp
        if not self.is_only_digits():
            print('Invalid')
        elif not self.check_first_digits():
            print('Invalid')
        elif not self.four_or_less_repeat():
            print('Invalid')
        else:
            print('Valid')

    def check_first_digits(self):
        if self.number[0] == '4' or self.number[0] == '5' or self.number[0] == '6':
            return True
        else:
            return False

    def four_or_less_repeat(self):
        test_str = ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999']
        for test_dig in test_str:
            match = re.findall(test_dig, self.number)
            if len(match):
                return False
            else:
                continue
        return True

    def is_only_digits(self):
        match = ''.join(re.findall(r'[^\d]', self.number))
        if self.number.isdigit() and len(self.number) == 16:
            return True
        if len(match) != 3:
            return False
        match = ''.join(re.findall(r'[^-]', match))
        if len(match):
            print('More ---')
            return False
        groups = self.number.split('-')
        if len(groups) != 4:
            return False
        for i in groups:
            if len(i) != 4:
                return False
        match = ''.join(re.findall(r'[\d]', self.number))
        if match.isdigit() and len(match) == 16:
            self.number = match
            return True
        else:
            return False

n = int(input())
while n:
    creditCard(input())
    n -= 1