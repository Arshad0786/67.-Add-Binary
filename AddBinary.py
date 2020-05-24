class Solution:
    def addBinary(self, a, b):
        Aindex = len(a) - 1
        Bindex = len(b) - 1
        carry = 0
        output = ""
        while Aindex >= 0 and Bindex >= 0:
            if int(a[Aindex]) + int(b[Bindex]) + carry >= 2:
                output = output + str(int(a[Aindex]) + int(b[Bindex]) + carry - 2)
                carry = 1
            else:
                output = output + str(int(a[Aindex]) + int(b[Bindex]) + carry)
                carry = 0
            Aindex = Aindex - 1
            Bindex = Bindex - 1

        while Aindex >= 0:
            if int(a[Aindex]) + carry == 2:
                output = output + str(int(a[Aindex]) + carry - 2)
                carry = 1
            else:
                output = output + str(int(a[Aindex]) + carry)
                carry = 0
            Aindex = Aindex - 1

        while Bindex >= 0:
            if int(b[Bindex]) + carry == 2:
                output = output + str(int(b[Bindex]) + carry - 2)
                carry = 1
            else:
                output = output + str(int(b[Bindex]) + carry)
                carry = 0
            Bindex = Bindex - 1
            
        if carry == 1:
            output = output + "1"

        reverseoutput = ""
        i = len(output) - 1
        while i >= 0:
            reverseoutput = reverseoutput + output[i]
            i = i - 1

        return reverseoutput


a = Solution()
print(a.addBinary("11", "1"))
