
# .Writeafunctionthattakesthelengthsofthreesides:side1,side2andside3of
# thetriangleastheinputfrom theuserusinginputfunctionandreturnthearea
# andperimeterofthetriangleasatuple.Also,assertthatsumofthelengthofany
# twosidesisgreaterthanthethirdside

from math import sqrt


def perimeter_area(s1, s2, s3):
    # Asserting validity of sides
    assert s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1, "Invalid sides"

    perimeter = s1 + s2 + s3
    s = perimeter / 2
    area = sqrt(s * (s - s1) * (s - s2) * (s - s3))
    return perimeter, area

a = float(input("Enter side 1 : "))
b = float(input("Enter side 2 : "))
c = float(input("Enter side 3 : "))

perimeter,area = perimeter_area(a,b,c)
print(f"Perimeter : {perimeter}")
print(f"Area : {area}")