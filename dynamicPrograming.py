def lcs(seq1, seq2, ind1=0, ind2=0):
    if (ind1==len(seq1) or ind2==len(seq2)):
        return 0
    elif (seq1[ind1]==seq2[ind2]):
        return 1 + lcs(seq1,seq2,ind1+1,ind2+1)
    else:
        option1 = lcs(seq1,seq2,ind1+1,ind2)
        option2 = lcs(seq1,seq2,ind1,ind2+1)

        return max(option1,option2)



def main():
    seq1 = "serendipitous"
    seq2 = "precipitation"
    val = lcs(seq1,seq2)
    print(val)

if __name__ == "__main__":
    main()