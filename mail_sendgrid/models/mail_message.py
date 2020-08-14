# Copyright 2016-2020 Compassion CH (http://www.compassion.ch)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)


class MailMessage(models.Model):
    """ Add SendGrid related fields so that they dispatch in all
    subclasses of mail.message object
    """
    _inherit = 'mail.message'

    body_text = fields.Text(help='Text only version of the body')
    sent_date = fields.Datetime(copy=False)
    substitution_ids = fields.Many2many(
        'sendgrid.substitution', string='Substitutions', copy=True)
    sendgrid_template_id = fields.Many2one(
        'sendgrid.template', 'Sendgrid Template')
    send_method = fields.Char(compute='_compute_send_method')

    @api.multi
    def _compute_send_method(self):
        """ Check whether to use traditional send method, sendgrid or disable.
        """
        send_method = self.env['ir.config_parameter'].get_param(
            'mail_sendgrid.send_method', 'traditional')
        for email in self:
            email.send_method = send_method

    @api.model
    def _message_read_dict_postprocess(self, messages, message_tree):
        """Preare values to be used by the chatter widget"""
        res = super()._message_read_dict_postprocess(
            messages, message_tree)

        # Overload to use sendgrid statuses instead of email notifications
        for mail in self:
            # We find all mails that were delivered by sendgrid
            delivery_ids = []
            for tracking in mail.mail_tracking_ids:
                if tracking.state in ["opened", "delivered"] and \
                        tracking.partner_id:
                    delivery_ids.append(tracking.partner_id.id)

            # We update the list of people to resend and check if all
            # messages were delivered
            for message_dict in messages:
                if message_dict["id"] == mail.id:
                    customer_email_data = message_dict["customer_email_data"]
                    customer_to_deliver = []
                    for customer in customer_email_data:
                        partner_id = customer[0]
                        partner_delivered = False
                        for delivery_id in delivery_ids:
                            if delivery_id == partner_id:
                                partner_delivered = True
                                break
                        if not partner_delivered:
                            customer_to_deliver.append(customer)
                    message_dict["customer_email_data"] = customer_to_deliver
                    if len(customer_to_deliver) == 0:
                        message_dict["customer_email_status"] = "delivered"

        return res
