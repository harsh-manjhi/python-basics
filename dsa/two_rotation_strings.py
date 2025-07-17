#A = 'ABCD'

def are_rotation(A,B):
    if len(A) != len(B) :
        return False
    else :
        doubled = A + A
        if B in doubled :
            return True
        else :
            return False
        
A = input("\n Enter first string : ")
B = input("\n String To check : ")
check = are_rotation(A,B)
print(f"\n Is {B} a rotation of {A} : ",check)