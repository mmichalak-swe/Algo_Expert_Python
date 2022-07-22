# Brute-Force Solution
# O(n^2) time | O(n) space
def arrayOfProducts(array):
    products = []
    for i in range(len(array)):
        product = 1
        for j in range(len(array)):
            if i == j:
                continue
            product *= array[j]
        products.append(product)

    return(products)
