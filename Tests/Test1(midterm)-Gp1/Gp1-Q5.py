def compareStrings(s1,s2):
    """
    Input: two strings s1 and s2
    Output:
    - return ">" if s1 is lexicographically greater than s2.
    - return "<" if s1 is lexicographically less than s2.
    - return "=" if s1 is lexicographically equal to s2.
    """
    i = 0
    while i < min(len(s1),len(s2)):
        if s1[i] > s2[i]:
            return ">"
        elif s1[i] < s2[i]:
            return "<"
        i = i + 1

    if len(s1) > len(s2):
        return ">"
    elif len(s1) < len(s2):
        return "<"
    else:
        return "="

# I print out more information to make it more readable.
# But you were asked to just print out >, <, or =
print("alpha", compareStrings("alpha","omega"), "omega") 
print("omega", compareStrings("omega","alpha"), "alpha")
print("alphaomega", compareStrings("alphaomega","alphaomega"), "alphaomega") 
print("", compareStrings("","omega"), "omega")
print("Benjamen", compareStrings("Benjamen","Ben"), "Ben")
print("", compareStrings("",""), "")
