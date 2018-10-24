class Lab05:

    def solve01(self, list1, list2):
        x=set(list1)
        y=set(list2)
        z=list(y-x)
        return z

        #Write your solution here.
        #Remember to replace "pass" with your own return statement!
        pass

    def solve02(self, S):
        a=[]
        for i in range(len(S)):
            b=S[:i]+S[i+1:]
            a.append(b)
        c=set(a)
        d=len(c)
        return (d)
        #Write your solution here.
        #Remember to replace "pass" with your own return statement!
        pass

    def solve03(self, N, a):
        b=[]
        for j in a:
             if j not in b:
                 b.append(j)
        c=len(a)
        d=len(b)
        e=c-d
        return e
        #Write your solution here.
        #Remember to replace "pass" with your own return statement!
        pass

    def solve04(self, arr, A, B):
        a=0
        for i in arr:
            if i in A:
                a=a+1
            elif i in B:
                a=a-1
            else:
                a=a
        return a
        #Write your solution here.
        #Remember to replace "pass" with your own return statement!
        pass

    def solve05(self, n, guesses):
        
        #Write your solution here.
        #Remember to replace "pass" with your own return statement!
        pass

    def solve06(self, S, Q, engines, queries):
        #Write your solution here.
        #Remember to replace "pass" with your own return statement!
        pass

    def solve07(self, n):
        #Write your solution here.
        #Remember to replace "pass" with your own return statement!
        pass

    def solve08(self, wires):
        #Write your solution here.
        #Remember to replace "pass" with your own return statement!
        pass

    def solve09(self, elevations):
        #Write your solution here.
        #Remember to replace "pass" with your own return statement!
        pass

    def solve10(self, ratings):
        #Write your solution here.
        #Remember to replace "pass" with your own return statement!
        pass

#--------IMPORTANT:
#--------Before uploading this file on gradescope, delete or comment out all the lines below.

#These print statements will show the output for the given test cases.
#Feel free to experiment with your own.


# soln = Lab05()

# print(soln.solve01(['BCE017', 'BIT049', 'BCE017'],
#                    ['BCE017', 'BIT059', 'BIT049', 'BIT059']))
# # Expected Output: ['BIT059']

# print(soln.solve02("ABA"))
# # Expected Output: 3

# print(soln.solve02("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"))
# # Expected Output: 1

# print(soln.solve03(4, [1, 2, 3, 2]))
# # Expected Output: 1

# print(soln.solve03(3, [1, 2, 3]))
# # Expected Output: 0

# print(soln.solve04([5, 1, 3, 3, 2], [1, 3], [5, 7]))
# # Expected Output: 1

# print(soln.solve05(10, [("1 2 3 4 5", "YES"), ("2 4 6 8 10", "NO")]))
# # Expected Output: "1 3 5"

# print(soln.solve06(5, 10, ["Yeehaw", "NSM", "Dont Ask", "B9", "Googol"],
#                    ["Yeehaw", "Yeehaw", "Googol", "B9", "Googol", "NSM", "B9", "NSM", "Dont Ask", "Googol"]))
# # Expected Output: 1

# print(soln.solve07(3))
# # Expected Output: [2, 3, 1]

# print(soln.solve08([(1, 10), (5, 5), (7, 7)]))
# # Expected Output: 2

# print(soln.solve09([[9, 6, 3], [5, 9, 6], [3, 5, 9]]))
# # Expected Output: [['a', 'b', 'b'], ['a', 'a', 'b'], ['a', 'a', 'a']]

# print(soln.solve09([[0, 1, 2, 3, 4, 5, 6, 7, 8, 7]]))
# # Expected Output: [['a','a','a','a','a','a','a','a','a','b']]

# print(soln.solve10([1, 2, 2]))
# # Expected Output: 4

# print(soln.solve10([2, 4, 2, 6, 1, 7, 8, 9, 2, 1]))
# # Expected Output: 19
