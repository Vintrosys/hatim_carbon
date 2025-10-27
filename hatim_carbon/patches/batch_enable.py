import frappe

def execute():

    excluded_groups = [
    "Adhesives & Resins",
    "Dies & Tooling",
    "Electrical Items",
    "Machined FG Products",
    "Machinery Tools",
    "Oils & Lubricants",
    "Tubes & Rods",
    "Sleeving",
    "Packaging Material",
    "Fasteners"
]


    items = frappe.get_all(
        "Item",
        filters=[
            ["disabled", "=", 0],
            ["is_stock_item", "=", 1],           
            ["has_batch_no", "=", 0],           
            ["item_group", "not in", excluded_groups]
        ],
        fields=["name", "item_code", "item_name"]
    )

    print(f"Found {len(items)} items to update batch.")

    for i, item in enumerate(items, start=1):

        item_doc = frappe.get_doc("Item", item.name)        

        frappe.db.set_value("Item", item.name, {
            "allow_negative_stock": 1,
            "has_batch_no": 1,
            "create_new_batch": 1
        })

        frappe.db.commit()
        print(f"Batch enabled for Item: {item_doc.name}\n")


   
