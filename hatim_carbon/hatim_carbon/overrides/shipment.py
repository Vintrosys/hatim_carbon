# apps/hatim_carbon/hatim_carbon/overrides/shipment.py

import frappe
from frappe import _
from frappe.contacts.doctype.contact.contact import get_default_contact
from erpnext.accounts.party import get_party_shipping_address
from erpnext.stock.doctype.shipment.shipment import Shipment as ShipmentBase


class Shipment(ShipmentBase):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from erpnext.stock.doctype.shipment_delivery_note.shipment_delivery_note import ShipmentDeliveryNote
        from erpnext.stock.doctype.shipment_parcel.shipment_parcel import ShipmentParcel
        from frappe.types import DF

        amended_from: DF.Link | None
        awb_number: DF.Data | None
        carrier: DF.Data | None
        carrier_service: DF.Data | None
        delivery_address: DF.SmallText | None
        delivery_address_name: DF.Link
        delivery_company: DF.Link | None
        delivery_contact: DF.SmallText | None
        delivery_contact_email: DF.Data | None
        delivery_contact_name: DF.Link | None
        delivery_customer: DF.Link | None
        delivery_supplier: DF.Link | None
        delivery_to: DF.Data | None
        delivery_to_type: DF.Literal["Company", "Customer", "Supplier"]
        description_of_content: DF.SmallText
        incoterm: DF.Link | None
        pallets: DF.Literal["No", "Yes"]
        parcel_template: DF.Link | None
        pickup: DF.Data | None
        pickup_address: DF.SmallText | None
        pickup_address_name: DF.Link
        pickup_company: DF.Link | None
        pickup_contact: DF.SmallText | None
        pickup_contact_email: DF.Data | None
        pickup_contact_name: DF.Link | None
        pickup_contact_person: DF.Link | None
        pickup_customer: DF.Link | None
        pickup_date: DF.Date
        pickup_from: DF.Time
        pickup_from_type: DF.Literal["Company", "Customer", "Supplier"]
        pickup_supplier: DF.Link | None
        pickup_to: DF.Time
        pickup_type: DF.Literal["Pickup", "Self delivery"]
        service_provider: DF.Data | None
        shipment_amount: DF.Currency
        shipment_delivery_note: DF.Table[ShipmentDeliveryNote]
        shipment_id: DF.Data | None
        shipment_parcel: DF.Table[ShipmentParcel]
        shipment_type: DF.Literal["Goods", "Documents"]
        status: DF.Literal["Draft", "Submitted", "Booked", "Cancelled", "Completed"]
        total_weight: DF.Float
        tracking_status: DF.Literal["", "In Progress", "Delivered", "Returned", "Lost"]
        tracking_status_info: DF.Data | None
        tracking_url: DF.SmallText | None
        value_of_goods: DF.Currency
    # end: auto-generated types

    def validate(self):
        # 🔹 Custom logic BEFORE
        frappe.logger().info("Custom Shipment validate from hatim_carbon")

        super().validate()

        # 🔹 Custom logic AFTER
        # example:
        # self.custom_flag = 1

    


# ----------------------------
# Whitelisted methods
# ----------------------------

@frappe.whitelist()
def get_address_name(ref_doctype, docname):
    return get_party_shipping_address(ref_doctype, docname)


@frappe.whitelist()
def get_contact_name(ref_doctype, docname):
    return get_default_contact(ref_doctype, docname)


@frappe.whitelist()
def get_company_contact(user):
    contact = frappe.db.get_value(
        "User",
        user,
        [
            "first_name",
            "last_name",
            "email",
            "phone",
            "mobile_no",
            "gender",
        ],
        as_dict=1,
    )
    if not contact.phone:
        contact.phone = contact.mobile_no
    return contact

