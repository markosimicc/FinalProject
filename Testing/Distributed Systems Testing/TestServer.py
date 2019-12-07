import TEST
import unittest
import json
#TestClass for Server
class TestServerMethods(unittest.TestCase):
#    def setUp(self):
#        TEST.insertItem('Doritos','4.99',0)
#        TEST.insertItem('apple','2.50',3)
#       TEST.insertItem('Chips','3.00',56)
#    #Tests Decreasing the quantity
    def test_1DecreaseQuantity(self):
        m1 = '{"messageid":1,"id":2,"func":"decrease","amount":3}'
        print("Recieved message .... " + m1)
        y = json.loads(m1)
        messagenum = y["messageid"]
        i = y["id"]
        a = y["amount"]
        function = y["func"]
        T = TEST.getQuantity(i) - 3
        P = TEST.decreaseQuantity(i,a)
        self.assertEqual(T,P);
        print(" Test 1: Actual: " + str(T) + " Expected : " + str(P))
        x = {'messageid': 1, 'complete': True}
        send = json.dumps(x)
        print("Sending message ... " + send)
        
    #Tests Increasing the quantity
    def test_2IncreaseQuantity(self):
        m2 = '{"messageid":2,"id":2,"func":"increase","amount":3}'
        print("Recieved message .... " + m2)
        y = json.loads(m2)
        messagenum = y["messageid"]
        i = y["id"]
        a = y["amount"]
        function = y["func"]
        A = TEST.getQuantity(i) + 3
        B = TEST.increaseQuantity(i,a)
        self.assertEqual(A,B);
        print(" Test 2: Actual: " + str(A) + " Expected : " + str(B))
        x = {'messageid': messagenum, 'complete': True}
        send = json.dumps(x)
        print("Sending message .... " + send)

    def test_3Empty(self):
        b = TEST.isEMPTY(1)
        print(" Test 3: Actual: " + str(b) + " Expected : " + "True")
        self.assertTrue(b)
        m3 = '{"messageid":1,"id":1,"func":"empty"}'
        print("Sending message .... " + m3)
    #Tests to make sure shelf isnt empty
    def test_4Full(self):
        TEST.increaseQuantity(2,3)
        C = TEST.isEMPTY(3)
        self.assertFalse(C)
        print(" Test 4: Actual: " + str(C) + " Expected : " + "False")
#    #Tests getting price of given item
    def test_5GetPrice(self):
        m4 = '{"messageid":4,"id":2,"func":"price"}'
        print("Recieved message .... " + m4)
        y = json.loads(m4)
        messagenum = y["messageid"]
        i = y["id"]
        function = y["func"]
        p = TEST.getPrice(i)
        self.assertEqual(p,'2.50')
        print(" Test 5: Actual: " + p + " Expected :" + '2.50')
        x = {'messageid': messagenum,'id': i, 'price':p }
        send = json.dumps(x)
        print("Sending message .... " + send)
#    #tests getting quantity of given item
    def test_6GetQuantity(self):
        m5 = '{"messageid":5,"id":3,"func":"quantity"}'
        print("Recieved message .... " + m5)
        y = json.loads(m5)
        messagenum = y["messageid"]
        i = y["id"]
        function = y["func"]
        q = TEST.getQuantity(i)
        self.assertEqual(q,56)
        print(" Test 6: Actual: " + str(q) + " Expected :" + str(50))
        x = {'messageid': messagenum,'id': i, 'quantity':q }
        send = json.dumps(x)
        print("Sending message .... " + send)
#    #Tests faulty input of inserting tem should arise an error
    def test_7Faulty(self):
        m6 = '{"messageid":7,"id":"90","faulty":3,"ad":"bad"}'
        y = json.loads(m6)
        messagenum = y["messageid"]
        print("Recieved message .... " + m6)
        print(" Test 7: TypeError")
        x = {'messageid': messagenum, 'complete': False}
        send = json.dumps(x)
        print("Sending message .... " + send)
        with self.assertRaises(TypeError):
            TEST.insertItem(1,10,10,'56')
#    #Tests getting price of item nt in database should arise an error
    def test_8IDnotavailable(self):
        m7 = '{"messageid":8,"id": 700,"func":"price"}'
        print("Recieved message .... " + m7)
        y = json.loads(m7)
        messagenum = y["messageid"]
        i = y["id"]
        function = y["func"]
        print(" Test 8: UnboundedLocalError, ID is not in the database")
        with self.assertRaises(UnboundLocalError):
            a = TEST.getPrice(i)
        x = {'messageid': messagenum, 'complete': False}
        send = json.dumps(x)
        print("Sending message .... " + send)

if __name__ =='__main__':
    unittest.main()
        
    
        
    
