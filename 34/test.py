def police_check(age: int) -> bool: # <-- Type hint
    '''
    Sample function, checks age
    '''
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

print(police_check("twelve"))