class Solution:
    def addBinary(self, a, b):
        carry = 0
        output = ""
        diff = abs(len(a) - len(b))
        if len(a) > len(b):
            for i in range(diff):
                b = "0" + b

        if len(b) > len(a):
            for i in range(diff):
                a = "0" + a

        i = len(a) - 1
        while i >= 0:
            if (int(a[i]) + int(b[i]) + carry) >= 2:
                output = output + str(int(a[i]) + int(b[i]) + carry - 2)
                carry = 1
            else:
                output = output + str(int(a[i]) + int(b[i]) + carry)
                carry = 0
            i = i - 1
            
        if carry:
            output = output + "1"

        reverseoutput = ""
        i = len(output) - 1
        while i >= 0:
            reverseoutput = reverseoutput + output[i]
            i = i - 1

        return reverseoutput