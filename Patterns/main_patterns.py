from Factory_pattern.Factory import Factory


factory = Factory()

product_code = input("Ingresa el producto que querés comprar: ")
product = Factory.create_product("cactus")


print(f"usted ha comprado un: {product.return_price_with_iva()}")