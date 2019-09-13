#https://github.com/mutux/kmp/blob/master/kmp.py
def kmp(P, T):
    # Compute the start position (number of chars) of the longest suffix that matches a prefix,
    # and store them into list K, the first element of K is set to be -1, the second
    #
    K = []  # K[t] store the value that when mismatch happens at t, should move Pattern P K[t] characters ahead
    t = -1  # K's length is len(P) + 1, the first element is set to be -1, corresponding to no elements in P.
    K.append(t)# Add the first element, keep t = -1.
    print('K',K)
    for k in range(0, len(P)):
        print('k',k)
        # traverse all the elemtn in P, calculate the corresponding value for each element.
        while(t >= 0 and P[t] != P[k]):# if t=-1, then let t = 0, if t>=0 and current suffix doesn't match, then try a shorter suffix
            print('K',K,'t',t)
            t = K[t]
            print('t',t)
            #print('t=K[t]',t)
        t = t + 1# If it matches, then the matching position should be one character ahead.
        print('t+1後的t',t)
        K.append(t)# record the matching postion for k
        print('K',K,'最終')
    print(K)

    # Match the String T with P
    m = 0  # Record the current matching position in P when compared with T
    for i in range(0, len(T)):  # traverse T one-by-one
        while (m >= 0 and P[m] != T[i]):  # if mismatch happens at position m, move P forward with K[m] characters and restart comparison
            m = K[m]
            print('m',m)
        m = m + 1  # if position m matches, move P forward to next position
        if m == len(P):  # if m is already the end of K (or P), the a fully match is found. Continue comparison by move P forward K[m] characters
            #print (i - m + 1, i)
            print(i-m+1)
            m = K[m]


if __name__ == "__main__":
    kmp('abcbabcade', 'abcbabcabcbabcbabcbabcabcbabcbabca')
    #kmp('abab', 'ababcabababc')
    #kmp('ababcde','abcbabcabcbabcbabcbabcabcbabcbabcaababcde')
'''
[-1, 0, 0, 0, 0, 1, 2, 3, 1]
0 7
15 22
26 33
[-1, 0, 0, 1, 2]
0 3
5 8
7 10
'''
