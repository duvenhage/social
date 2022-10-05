import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-social",
    description="Meta package for oca-social Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-base_search_mail_content',
        'odoo12-addon-email_template_qweb',
        'odoo12-addon-fetchmail_thread_default',
        'odoo12-addon-mail_activity_board',
        'odoo12-addon-mail_activity_done',
        'odoo12-addon-mail_activity_partner',
        'odoo12-addon-mail_activity_reminder',
        'odoo12-addon-mail_activity_team',
        'odoo12-addon-mail_attach_existing_attachment',
        'odoo12-addon-mail_attach_existing_attachment_account',
        'odoo12-addon-mail_check_mailbox_size',
        'odoo12-addon-mail_debrand',
        'odoo12-addon-mail_drop_target',
        'odoo12-addon-mail_footer_notified_partner',
        'odoo12-addon-mail_full_expand',
        'odoo12-addon-mail_history',
        'odoo12-addon-mail_improved_tracking_value',
        'odoo12-addon-mail_inline_css',
        'odoo12-addon-mail_notification_custom_subject',
        'odoo12-addon-mail_optional_autofollow',
        'odoo12-addon-mail_optional_follower_notification',
        'odoo12-addon-mail_outbound_static',
        'odoo12-addon-mail_preview_audio',
        'odoo12-addon-mail_preview_base',
        'odoo12-addon-mail_private',
        'odoo12-addon-mail_restrict_follower_selection',
        'odoo12-addon-mail_send_copy',
        'odoo12-addon-mail_show_follower',
        'odoo12-addon-mail_template_substitute',
        'odoo12-addon-mail_track_diff_only',
        'odoo12-addon-mail_tracking',
        'odoo12-addon-mail_tracking_mailgun',
        'odoo12-addon-mail_tracking_mass_mailing',
        'odoo12-addon-mass_mailing_custom_unsubscribe',
        'odoo12-addon-mass_mailing_custom_unsubscribe_event',
        'odoo12-addon-mass_mailing_event_registration_exclude',
        'odoo12-addon-mass_mailing_list_dynamic',
        'odoo12-addon-mass_mailing_newsletter_welcome_mail',
        'odoo12-addon-mass_mailing_partner',
        'odoo12-addon-mass_mailing_resend',
        'odoo12-addon-mass_mailing_unique',
        'odoo12-addon-message_auto_subscribe_notify_own',
        'odoo12-addon-test_mail_private',
        'odoo12-addon-website_mass_mailing_name',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
