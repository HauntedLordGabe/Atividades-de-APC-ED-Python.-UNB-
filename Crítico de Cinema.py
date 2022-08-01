def nota(n):
    stars = '|'
    for i in range(n):
        stars+='★'
    for i in range(10-n):
        stars+='☆'
    stars+='|'    
    print(stars)
