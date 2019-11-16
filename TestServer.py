import TEST
import unittest

#TestClass for Server
class TestServerMethods(unittest.TestCase):
#    def setUp(self):
#        TEST.insertItem('Doritos','4.99',0)
    #Tests Decreasing the quantity
    def test_1DecreaseQuantity(self):
        T = TEST.getQuantity(9) - 3
        P = TEST.decreaseQuantity(9,3)
        self.assertEqual(T,P);
        print(" Test 1: Actual: " + str(T) + " Expected : " + str(P))
    #Tests Increasing the quantity
    def test_2IncreaseQuantity(self):
        A = TEST.getQuantity(9) + 3
        B = TEST.increaseQuantity(9,3)
        self.assertEqual(A,B);
        print(" Test 2: Actual: " + str(A) + " Expected : " + str(B))
    #Tests to make sure self is empty
    def test_3Empty(self):
        b = TEST.isEMPTY(42)
        print(" Test 3: Actual: " + str(b) + " Expected : " + "True")
        self.assertTrue(b)
    #Tests to make sure shelf isnt empty
    def test_4Full(self):
        TEST.increaseQuantity(11,3)
        C = TEST.isEMPTY(11)
        self.assertFalse(C)
        print(" Test 4: Actual: " + str(C) + " Expected : " + "False")
    #Tests getting price of given item
    def test_5GetPrice(self):
        p = TEST.getPrice(10)
        self.assertEqual(p,'2.50')
        print(" Test 5: Actual: " + p + " Expected :" + '2.50')
    #tests getting quantity of given item
    def test_6GetQuantity(self):
        q = TEST.getQuantity(10)
        self.assertEqual(q,30)
        print(" Test 6: Actual: " + str(q) + " Expected :" + str(30))
    #Tests faulty input of inserting tem should arise an error
    def test_7Faulty(self):
        print(" Test 7: TypeError is expected and recieved")
        with self.assertRaises(TypeError):
            TEST.insertItem(1,10,10,'56')
    #Tests getting price of item nt in database should arise an error
    def test_8IDnotavailable(self):
        print(" Test 8: UnboundedLocalError, ID is not in the database")
        with self.assertRaises(UnboundLocalError):
            a = TEST.getPrice(90)

if __name__ =='__main__':
    unittest.main()
        
    