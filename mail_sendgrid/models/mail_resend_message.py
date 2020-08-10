# Copyright 2020 Compassion CH (http://www.compassion.ch)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, api

class MailResendMessage(models.TransientModel):
    _inherit = "mail.resend.message"

    @api.model
    def default_get(self, fields):
        rec = super().default_get(fields)
        message_id = self._context.get('mail_message_to_resend')
        if message_id:
            # Override to use sendgrid statuses instead of mail notifications
            mail_message_id = self.env['mail.message'].browse(message_id)
            tracking_ids = mail_message_id.mail_tracking_ids.filtered(
                lambda x: x.state != "delivered"
            )
            if any(tracking_ids):
                rec['partner_ids'] = [
                    (0, 0, {
                        "partner_id": tracking.partner_id.id,
                        "name": tracking.partner_id.name,
                        "email": tracking.partner_id.email,
                        "resend": True,
                        "message": tracking.error_description,
                    }) for tracking in tracking_ids if tracking.partner_id
                ]
        return rec
