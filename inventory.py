products = []

def add_product():
    name = input("Tên sản phẩm: ")
    price = int(input("Giá bán: "))
    qty = int(input("Số lượng nhập: "))

    product = {
        'name': name,
        'price': price,
        'qty': qty
    }

    products.append(product)
    print(">> Đã nhập hàng thành công:", name)

def view_inventory():
    if len(products) == 0:
        print("Kho hiện đang trống.")
        return

    print("\n--- DANH SÁCH SẢN PHẨM TRONG KHO ---")
    for p in products:
        print(f"{p['name']} - Giá: {p['price']} - SL: {p['qty']}")

def check_low_stock():
    print("\n--- SẢN PHẨM SẮP HẾT HÀNG (SL < 5) ---")
    found = False

    for p in products:
        if p['qty'] < 5:
            print(f"{p['name']} - SL: {p['qty']}")
            found = True

    if not found:
        print("Không có sản phẩm nào sắp hết hàng.")

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
