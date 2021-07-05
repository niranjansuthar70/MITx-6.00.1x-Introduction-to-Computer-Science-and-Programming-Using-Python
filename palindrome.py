def isPalid(s):
    def char(s):
        s.lower()
        asn=""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxz":
                asn=asn+c
        return asn

    def isPal(s):
        if len(s)<=1:
            return True
        else:
            return s[0]==s[-1] and isPal(s[1:-1])

    return isPal(char(s))


print(isPalid("aabbba"))
