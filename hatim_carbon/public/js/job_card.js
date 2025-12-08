frappe.ui.form.on("Job Card", {
    onload(frm) {
        frm.set_query("employee", "time_logs", function() {
            return {
                filters: {
                    name: ["like", "HR-WRKR-%"],
                    status: "Active"
                }
            };
        });
        frm.set_query("employee", () => {
            return {
                filters: {
                    name: ["like", "HR-WRKR-%"],
                    status: "Active"
                }
            };
        });
    },
    refresh(frm) {

       ["Start Job", __("Start Job")].forEach(label => {
            frm.remove_custom_button(label);
            frm.page.remove_inner_button(label);
        });
        if (!frm.doc.started_time && !frm.doc.current_time) {
        if (frm.doc.employee[0]) {
            frm.add_custom_button(__("Start Job"), () => {

                frm.events.start_job(frm, "Work In Progress", frm.doc.employee);

            }).addClass("btn-primary");
        }
    }

    }
});
