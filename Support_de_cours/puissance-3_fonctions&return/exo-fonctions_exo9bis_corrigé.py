def vat(price):
    
    return price * 1.21 # ou price + (price * 0.21)


def sum_vat(prices):
    sum_prices = 0
    for price in prices:
        sum_prices += vat(price)
    return (sum_prices)

# --- main

prices = [5, 1, 6, 3, 11, 4, 5] # on peut utiliser les mêmes noms de variables que celles dans la fonction car ce ne sont pas les mêmes
print(sum_vat(prices))

# YAY réussi sans aide!


