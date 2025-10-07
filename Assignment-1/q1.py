def generate_bill(item,price,quantity=1,discount=0,tax_rate=0.05):
    subtotal = price*quantity


    discount_amt=(discount/100)*subtotal
    discounted_amt=subtotal-discount_amt
    
    tax_amt=discounted_amt*tax_rate
    final_bill=discounted_amt+tax_amt

    print("----- BILL SUMMARY -----")
    print(f"Item: {item}")
    print(f"Quantity: {quantity}")
    print(f"Price per item: {price}")
    print(f"Subtotal: {subtotal}")
    print(f"Discount: {discount}% (-{discount_amt})")
    print(f"Tax Rate: {tax_rate * 100}% (+{tax_amt})")
    print(f"Total Payable Amount: {final_bill}")
    print("------------------------\n")

generate_bill("Notebook",200)

generate_bill("Pen",10,quantity=5)

generate_bill("Desk",3000,discount=15,tax_rate=0.08)

generate_bill("Laptop",5000,quantity=2,discount=10,tax_rate=0.05)


