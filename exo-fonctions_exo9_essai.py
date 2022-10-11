def tva_include(price): # pas utiliser de majuscules
    TVA = 1.21
    
    return price * TVA
    

# --- main
result = tva_include(2)
print(result)