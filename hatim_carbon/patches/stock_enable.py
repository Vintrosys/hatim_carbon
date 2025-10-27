import frappe

def execute():
    # Filter for non-stock items
    items = frappe.get_all(
        "Item",
        filters={
            "is_stock_item": 0,
            "has_batch_no": 0,
            "disabled": 0
        },
        fields=["name", "item_code", "item_name"]
    )

    print(f"Found {len(items)} items to update stock.")

    for i, item in enumerate(items, start=1):
        item_doc = frappe.get_doc("Item", item.name)        

        frappe.db.set_value("Item", item.name, {            
            "is_stock_item": 1,
            "allow_negative_stock": 1
        })

        frappe.db.commit()
        print(f"Stock enabled for Item: {item_doc.name}\n")
	frappe.db.set_value("Item","ST100659","is_stock_item",0)
	frappe.db.commit()
