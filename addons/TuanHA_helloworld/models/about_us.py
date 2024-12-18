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

    def _get_default_image(self, image_name):
        """
        Trả về dữ liệu base64 của hình ảnh mặc định từ static/src/img.
        """
        image_path = modules.get_module_resource('TuanHA_helloworld', 'static/src/img', image_name)
        if image_path:
            with open(image_path, 'rb') as f:
                return tools.image_resize_image_big(base64.b64encode(f.read()))
        return False

    # Trường Icon với ảnh mặc định
    twitter_icon = fields.Binary(
        string="Twitter Icon", 
        default=_get_default_image,
        attachment=True
    )
    facebook_icon = fields.Binary(
        string="Facebook Icon", 
        default=_get_default_image,
        attachment=True
    )
    github_icon = fields.Binary(
        string="GitHub Icon", 
        default=_get_default_image,
        attachment=True
    )
    linkedin_icon = fields.Binary(
        string="LinkedIn Icon", 
        default=_get_default_image,
        attachment=True
    )
    youtube_icon = fields.Binary(
        string="YouTube Icon", 
        default=_get_default_image,
        attachment=True
    )
    instagram_icon = fields.Binary(
        string="Instagram Icon", 
        default=_get_default_image,
        attachment=True
    )
    tiktok_icon = fields.Binary(
        string="TikTok Icon", 
        default=_get_default_image,
        attachment=True
    )
    zalo_icon = fields.Binary(
        string="Zalo Icon", 
        default=_get_default_image,
        attachment=True
    )

    def _get_default_twitter_icon(self):
        return self._get_default_image('twitter.png')

    def _get_default_facebook_icon(self):
        return self._get_default_image('facebook.png')

    def _get_default_github_icon(self):
        return self._get_default_image('github.png')

    def _get_default_linkedin_icon(self):
        return self._get_default_image('linkedin.png')

    def _get_default_youtube_icon(self):
        return self._get_default_image('youtube.png')

    def _get_default_instagram_icon(self):
        return self._get_default_image('instagram.png')

    def _get_default_tiktok_icon(self):
        return self._get_default_image('tiktok.png')

    def _get_default_zalo_icon(self):
        return self._get_default_image('zalo.png')

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
    # @api.model
    # def write(self, vals):
    #     """
    #     Gửi tín hiệu cập nhật dữ liệu sau khi có thay đổi.
    #     """
    #     result = super(ResCompany, self).write(vals)
    #     if 'about_us' in vals or any(key.endswith('_account') for key in vals):
    #         self._send_update_signal()
    #     return result
    
    # def _send_update_signal(self):
    #     """
    #     Hàm này được dùng để gửi tín hiệu cập nhật (nếu cần thiết).
    #     Hiện tại chỉ in ra log, có thể mở rộng nếu cần.
    #     """
    #     _logger = logging.getLogger(__name__)
    #     _logger.info(f"Updating About Us data for company: {self.name}")