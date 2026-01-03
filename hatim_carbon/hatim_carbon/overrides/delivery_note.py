import frappe
from frappe.model.mapper import get_mapped_doc


@frappe.whitelist()
def make_shipment(source_name, target_doc=None):
    def set_missing_values(source, target):
        # Parent-level values
        target.pickup_from_type = "Company"
        target.delivery_to_type = "Customer"

        target.value_of_goods = source.grand_total or 0
        target.pickup_date = frappe.utils.today()

    doc = get_mapped_doc(
        "Delivery Note",
        source_name,
        {
            "Delivery Note": {
                "doctype": "Shipment",
            },
            "Delivery Note Item": {
                "doctype": "Shipment Item",
                "field_map": {
                    "item_code": "item_code",
                    "item_name": "item_name",
                    "qty": "qty",
                    "uom": "uom",
                    "stock_uom": "stock_uom",
                },
            },
        },
        target_doc,
        set_missing_values,
    )

    # INNER BOXES
    if hasattr(doc, "inner_boxes"):
        for item in doc.items:
            if not item.qty:
                continue

            doc.append("inner_boxes", {
                "item_code": item.item_code,
                "qty": item.qty,
            })

    # OUTER BOXES
    if hasattr(doc, "outer_boxes"):
        doc.append("outer_boxes", {
            "box_no": 1,
            "description": "Auto created from Delivery Note",
        })

    return doc
