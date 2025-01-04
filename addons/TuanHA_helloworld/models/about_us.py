from odoo import fields, models, tools, modules, api
from odoo.exceptions import ValidationError
from odoo.modules.module import get_module_resource
import logging
import re
import base64
import os

class ResCompany(models.Model):
    _inherit = "res.company"

    about_us = fields.Text(
        string="About Us",
        default="This is about company"
    )

    # Trường Account
    twitter_account = fields.Char(string="Twitter Account")
    facebook_account = fields.Char(string="Facebook Account")
    github_account = fields.Char(string="GitHub Account")
    linkedin_account = fields.Char(string="LinkedIn Account")
    youtube_account = fields.Char(string="YouTube Account")
    instagram_account = fields.Char(string="Instagram Account")
    tiktok_account = fields.Char(string="TikTok Account")
    zalo_account = fields.Char(string="Zalo Account")


    twitter_icon = fields.Binary(string="Twitter Icon")
    facebook_icon = fields.Binary(string="Facebook Icon")
    github_icon = fields.Binary(string="GitHub Icon")
    linkedin_icon = fields.Binary(string="LinkedIn Icon")
    youtube_icon = fields.Binary(string="YouTube Icon")
    instagram_icon = fields.Binary(string="Instagram Icon")
    tiktok_icon = fields.Binary(string="TikTok Icon")
    zalo_icon = fields.Binary(string="Zalo Icon")

    @api.constrains(
    'twitter_account', 'facebook_account', 'github_account', 'linkedin_account',
    'youtube_account', 'instagram_account', 'tiktok_account', 'zalo_account'
    )
    def _check_account_urls(self):
        """
        Kiểm tra định dạng URL hợp lệ cho các trường account.
        """
        url_regex = re.compile(
            r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-zA-Z0-9]+([\-\.]{1}[a-zA-Z0-9]+)*\.[a-zA-Z]{2,5}(:[0-9]{1,5})?(\/.*)?$'
        )
        for record in self:
            for field_name, specific_checks in [
                ('twitter_account', ['twitter.com/','https://twitter.com/']),
                ('facebook_account', ['facebook.com/', 'https://www.facebook.com/']),
                ('github_account', ['github.com/','https://github.com/']),
                ('linkedin_account', ['linkedin.com/in/','https://linkedin.com/in/']),
                ('youtube_account', ['youtube.com/@','https://www.youtube.com/@']),
                ('instagram_account', ['instagram.com/','https://instagram.com/']),
                ('tiktok_account', ['www.tiktok.com/@','https://www.tiktok.com/@']),
                ('zalo_account', ['zalo.me/','https://zalo.me/']),
            ]:
                field_value = getattr(record, field_name)
                if field_value:
                    # Kiểm tra URL hợp lệ
                    if not url_regex.match(field_value):
                        raise ValidationError(
                            (f"Giá trị '{field_value}' trong trường {field_name.replace('_', ' ')} không phải là một URL hợp lệ.")
                        )
                    
                    # Kiểm tra các tiền tố cụ thể
                    if specific_checks and not any(field_value.startswith(check) for check in specific_checks):
                        raise ValidationError(
                            (f"Link trong trường {field_name.replace('_', ' ')} phải bắt đầu bằng một trong các giá trị sau: {', '.join(specific_checks)}.")
                        )