#converts lexi's paper length to actual feet

def paperToFeet(paperLength):
    feet = (float(paperLength) / 2) * 22.25 / 12
    return '%.2f'% feet

print(paperToFeet(4.5))