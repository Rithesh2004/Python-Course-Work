# 🛒 Walmart Product Entry Interface
# Developed to handle inventory data collection with human-centric formatting

# ==== Step 1: Input Section ====

print("🔹 Welcome to Walmart's Internal Product Registration 🔹\n")

# Unique item identifier
item_id = int(input("Product Code (numeric): "))

# Product name input
item_name = input("Product Name: ").strip().title()

# Product price in INR
retail_price = float(input("Retail Price (in ₹): "))

# Product category input (stored as list)
raw_categories = input("Categories (comma-separated): ")
category_list = [c.strip().title() for c in raw_categories.split(",")]

# Stock details (stored as a tuple)
stock_available = int(input("Units in Warehouse: "))
stock_sold = int(input("Units Already Sold: "))
warehouse_stock = (stock_available, stock_sold)

# Discount percentage on product
discount_percent = float(input("Active Discount (%): "))

# Feature list (converted into a set to avoid repetition)
feature_input = input("Key Features (comma-separated): ")
features = set(f.strip().capitalize() for f in feature_input.split(","))

# Supplier details (stored as dictionary)
supplier_info = {
    "vendor": input("Supplier Name: ").strip(),
    "phone": input("Supplier Contact No.: ").strip(),
    "region": input("Supplier Location: ").strip().title()
}

# ==== Step 2: Output & Formatting Section ====

print("\n🧾 Generating Walmart Product Summary...\n")

# Method 1: Comma-separated printing
print("Product Snapshot:", item_id, item_name, retail_price, sep=" | ")

# Method 2: Percent-style formatting
print("🪙 Discount Tag: %.2f%% applied" % discount_percent)

# Method 3: f-string formatting
print(f"📦 Stock Report: {warehouse_stock[0]} units in stock | {warehouse_stock[1]} sold")
print(f"💰 Price: ₹{retail_price} | 🏷️ Discount: {discount_percent}%")
print(f"📁 Categories: {', '.join(category_list)}")
print(f"✨ Features: {', '.join(features)}")

# Method 4: Using .format() method
print("📡 Supplier Info: Name - {}, Contact - {}, Location - {}".format(
    supplier_info["vendor"],
    supplier_info["phone"],
    supplier_info["region"]
))

# Additional touch – overall status
total_units = sum(warehouse_stock)
print(f"\n📊 Overall Status: {total_units} units registered under Product ID {item_id}")
