a_string = "FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
print a_string
print len(a_string)

def palindromes(a_string):
    
    i = 0
    pals = []
    new_pal = ""

    while i < len(a_string):
        try:
            now = a_string[i]
            next = a_string[i+1]
            before = a_string[i-1]
        except IndexError:
            return pals
        if now == next:
            back = i
            front = i + 1
            new_pal = now + next
        elif before == next:
            back = i-1
            front = i + 1
            new_pal = before + now + next
        
        if new_pal:
            pals.append(new_pal)
            add_pals(a_string,pals,new_pal,front,back)
            new_pal = ""
        
        i = i + 1
    
    return pals

def add_pals(a_string,pals,new_pal,front,back):
    while front < len(a_string):
        front = front + 1
        back = back - 1
        if back < 0:
            break
        try:
            if a_string[front] == a_string[back]:
                new_pal = a_string[front] + new_pal + a_string[back]
                pals.append(new_pal)
            else:
                return
        except IndexError:
            return

pals = palindromes(a_string)
print "--o-o--"
print len(pals)
for pal in pals:
    print pal
