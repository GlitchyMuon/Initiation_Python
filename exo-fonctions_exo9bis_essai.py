def TVA_include(price):
    TVA = 1.21
    
    return price * TVA


def sum_pricelist_TVA(price1, price2, price3, price4, price5):
    
    return (price1 + price2 + price3 + price4 + price5)

# --- main

print(TVA_include(sum_pricelist_TVA(2, 15, 25, 7, 5)))

# YAY réussi sans aide! mais il fallait les prix dans une liste !


