
def find_category_and_product_only(user_input, product_list):
    # Minimal: just echo the input and product_list for demo
    return f"{user_input} | {product_list}"

def get_products_and_category():
    return ["smartx pro phone", "fotosnap camera", "dslr", "tv", "tvs"]

def read_string_to_list(category_and_product_response):
    return [category_and_product_response]

def generate_output_string(category_and_product_list):
    return "\n".join(str(x) for x in category_and_product_list)




def get_products_from_query(customer_msg):
    # Example: simple keyword-based extraction
    msg = customer_msg.lower()
    products = []
    # Add your product list here
    product_list = [
        "smartx pro phone", "fotosnap camera", "dslr", "tv", "tvs"
    ]
    for product in product_list:
        if product in msg:
            products.append(product)
    return ", ".join(products)  # Or return as a list if preferred






def read_string_to_list(product_str):
    # Converts a comma-separated string to a list
    return [p.strip() for p in product_str.split(",") if p.strip()]

def get_mentioned_product_info(product_list):
    # Dummy: returns info for each product
    info = []
    for product in product_list:
        info.append(f"{product}: Example info.")
    return "\n".join(info)

def answer_user_msg(user_msg, product_info):
    # Dummy: combines user message and product info
    return f"User asked: {user_msg}\nProduct info:\n{product_info}"



