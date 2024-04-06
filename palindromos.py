import unittest

def is_palindrome(mystring):
    for indice in range(0,len(mystring)):
        print(mystring[indice] + "-->" + mystring[-(indice +1)])
        if mystring[indice] != mystring[-(indice +1)]:
            print("no es un palindromo")
            return False
    return True
   # return mystring[0] == mystring[-1]



class TestPalindrome(unittest.TestCase):
    def test_a(self):
        resultado=is_palindrome('a')
        self.assertEqual(resultado, True)

    def test_aa(self):
        resultado=is_palindrome('aa')
        self.assertEqual(resultado, True)

    def test_ab(self):
        resultado=is_palindrome('ab')
        self.assertEqual(resultado, False)

    def test_aCb(self):
        resultado=is_palindrome('aCb')
        self.assertEqual(resultado, False)

    def test_aCs(self):
        resultado=is_palindrome('aCs')
        self.assertEqual(resultado, False)

    def test_ABBA(self):
        resultado=is_palindrome('ABBA')
        self.assertEqual(resultado, True)

    def test_ABCA(self):
        resultado=is_palindrome('ABCA')
        self.assertEqual(resultado, False)

    def test_ABCBA(self):
        resultado=is_palindrome('ABCBA')
        self.assertEqual(resultado, True)

    def test_ABCCBA(self):
        resultado=is_palindrome('ABCCBA')
        self.assertEqual(resultado, True)

    def test_ZBCCBA(self):
        resultado=is_palindrome('ZBCCBA')
        self.assertEqual(resultado, False)

    def test_neuquen(self):
        resultado=is_palindrome('neuquen')
        self.assertEqual(resultado, True)

    def test_neuqueM(self):
        resultado=is_palindrome('neuqueM')
        self.assertEqual(resultado, False)

    def test_quequen(self):
        resultado=is_palindrome('quequen')
        self.assertEqual(resultado, False)
        
    def test_nuequen(self):
        resultado=is_palindrome('nuequen')
        self.assertEqual(resultado, False)

unittest.main()
