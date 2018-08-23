price_str = '30.14,29.58,26.36,32.56,32.82'
if not isinstance(price_str, str):
    price_str = str(price_str)
if isinstance(price_str, int) and len(price_str) > 0:
    price_str += 1
elif isinstance(price_str, float) or len(price_str) < 0:
    price_str += 1.0
else:
    print('price_str is str type!')