def calculate_discounted_price(original_price, discount_percent):
    discount = (original_price * discount_percent) / 100
    discounted_price = original_price - discount
    return discounted_price

nama = input("Masukkan nama: ")
nim = input("Masukkan NIM: ")
harga_setiap_mobil = float(input("Masukkan harga setiap mobil: "))

tesla_discount = 17
toyota_discount = 21
hyundai_discount = 23

tesla_price_after_discount = calculate_discounted_price(harga_setiap_mobil, tesla_discount)
toyota_price_after_discount = calculate_discounted_price(harga_setiap_mobil, toyota_discount)
hyundai_price_after_discount = calculate_discounted_price(harga_setiap_mobil, hyundai_discount)

harga_modulus = harga_setiap_mobil % 7

print(f"Mobil Tesla seharga {harga_setiap_mobil} diskon 17% menjadi {tesla_price_after_discount:.2f}, "
      f"Mobil Toyota seharga {harga_setiap_mobil} diskon 21% menjadi {toyota_price_after_discount:.2f}, "
      f"Mobil Hyundai seharga {harga_setiap_mobil} diskon 23% menjadi {hyundai_price_after_discount:.2f}, "
      f"dan harga_setiap_mobil modulus 7 adalah {harga_modulus:.2f}.")

