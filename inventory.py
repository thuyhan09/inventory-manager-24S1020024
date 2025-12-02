# Biến lưu trữ dữ liệu: Mỗi sản phẩm là một dict {'name': '...', 'price': 0, 'qty': 0}
products = []


def add_product(name, price, quantity):
    """
    Thêm sản phẩm mới vào danh sách products.

    Args:
        name (str): Tên sản phẩm
        price (float/int): Giá bán sản phẩm
        quantity (int): Số lượng tồn kho
    """
    product = {
        'name': name,
        'price': price,
        'qty': quantity
    }
    products.append(product)
    print(f"Đã thêm sản phẩm: {product}")

# Ví dụ sử dụng
add_product("Mì tôm", 5000, 100)
add_product("Bánh mì", 12000, 50)

# In ra danh sách hiện tại
print(products)


def add_product():
  # Nhập tên, giá, số lượng -> append vào products
  print("Đã nhập hàng thành công.")

def view_inventory():
  # Duyệt list products và in ra
  # Ví dụ: Mì tôm - Giá: 5000 - SL: 100 
  pass

def check_low_stock():
  # Duyệt list, kiểm tra nếu qty < 5 thì in ra cảnh báo
  pass

def main():
  while True:
    print("\n--- QUẢN LÝ KHO HÀNG ---")
    print("1. Nhập hàng mới")
    print("2. Xem tồn kho")
    print("3. Cảnh báo hết hàng")
    print("4. Thoát")

    choice = input("Chọn chức năng: ")
    if choice == '1':
      add_product()
    elif choice == '2':
      view_inventory()
    elif choice == '3':
      check_low_stock()
    elif choice == '4':
      print("Kết thúc chương trình.")
      break
    else:
      print("Lựa chọn không hợp lệ.")
if __name__ == "__main__":
  main()
def view_inventory():
    """
    In ra thông tin tất cả sản phẩm trong kho.
    """
    if not products:
        print("Kho đang trống!")
        return

    print("Danh sách sản phẩm trong kho:")
    for i, product in enumerate(products, start=1):
        print(f"{i}. Tên: {product['name']}, Giá: {product['price']}, Số lượng: {product['qty']}")
