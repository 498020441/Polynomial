class Polynomial(object):

    def __init__(self, polynomial):
        self.polynomial = polynomial

    def get_polynomial(self):
        return tuple(self.polynomial)

    def __neg__(self):
        subset = []
        for r in range(len(self.polynomial)):
            subset.append((-self.polynomial[r][0], self.polynomial[r][1]))
        return Polynomial(subset)

    def __add__(self, other):
        return Polynomial((self.polynomial + other.get_polynomial()))

    def __sub__(self, other):
        return Polynomial((self.polynomial + (Polynomial.__neg__(other)).get_polynomial()))

    def __mul__(self, other):
        other = other.get_polynomial()
        subset = []
        for i in range(len(self.polynomial)):
            for j in range(len(other)):
                subset.append((self.polynomial[i][0] * other[j][0], self.polynomial[i][1] + other[j][1]))
        return Polynomial(subset)

    def __call__(self, x):
        total = sum((self.polynomial[i][0] * (x ** self.polynomial[i][1]) for i in range(len(self.polynomial))))
        return total

    def simplify(self):
        polynomial_list = list(self.polynomial)
        subset = []
        l = len(polynomial_list)
        for i in range(l):
            for j in range(i + 1, l):
                if polynomial_list[i][1] == polynomial_list[j][1]:
                    if polynomial_list[i][0] + polynomial_list[j][0] == 0:
                        polynomial_list[i] = (0, 0)
                        polynomial_list[j] = (0, 0)
                    if not polynomial_list[i][0] + polynomial_list[j][0] == 0:
                        polynomial_list[j] = (polynomial_list[i][0] + polynomial_list[j][0], polynomial_list[j][1])
                        polynomial_list[i] = (0, 0)
        for i in range(len(polynomial_list)):
            if not polynomial_list[i][0] == 0:
                subset.append(polynomial_list[i])
        subset.sort(key=lambda x: x[1], reverse=True)
        if len(subset) == 0:
            subset.append((0, 0))
        Polynomial(subset)
        self.polynomial = subset
        return self

    def __str__(self):
        to_str = ''
        i = 0
        polynomial_list = list(self.polynomial)
        for element in polynomial_list:
            # print(element)
            if i == 0:
                if element[1] > 1:
                    if (element[0] <= 0 and not element[0] == -1) or element[0] > 1:
                        to_str += '{0}x^{1}'.format(element[0], element[1])
                    if element[0] == 1:
                        to_str += 'x^{0}'.format(element[1])
                    if element[0] == -1:
                        to_str += '-x^{0}'.format(element[1])
                elif element[1] == 1:
                    if element[0] == -1:
                        to_str += '-x'
                    elif element[0] == 1:
                        to_str += 'x'
                    else:
                        to_str += '{0}x'.format(element[0])
                elif element[1] == 0:
                    to_str += '{0}'.format(element[0])
            else:
                if element[1] > 1:
                    if element[0] > 1:
                        to_str += ' + {0}x^{1}'.format(element[0], element[1])
                    if element[0] == 1:
                        to_str += ' + x^{0}'.format(element[1])
                    if element[0] == -1:
                        to_str += ' - x^{0}'.format(element[1])
                    if element[0] == 0:
                        to_str += ' + 0x^{0}'.format(element[1])
                    if element[0] < 0 and not element[0] == -1:
                        element = (-element[0], element[1])
                        to_str += ' - {0}x^{1}'.format(element[0], element[1])
                elif element[1] == 1:
                    if element[0] == -1:
                        to_str += ' - x'
                    elif element[0] == 1:
                        to_str += ' + x'
                    else:
                        if element[0] == 0:
                            to_str += ' + 0x'
                        if element[0] > 1:
                            to_str += ' + {0}x'.format(element[0], element[1])
                        if element[0] < 0 and not element[0] == -1:
                            element = (-element[0], element[1])
                            to_str += ' - {0}x'.format(element[0], element[1])
                elif element[1] == 0:
                    if element[0] >= 1:
                        to_str += ' + {0}'.format(element[0], element[1])
                    elif element[0] < 0:
                        element = (-element[0], element[1])
                        to_str += ' - {0}'.format(element[0], element[1])
                    else:
                        to_str += ' '
            i += 1
        return to_str
