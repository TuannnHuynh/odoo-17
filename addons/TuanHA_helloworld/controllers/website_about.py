from odoo import http
from odoo.http import request, Response
import json

class WebsiteAbout(http.Controller):
    @http.route('/about_us', type='json', auth='public')
    def get_about_data(self):
        """
        Trả về dữ liệu "About Us" và các tài khoản mạng xã hội của công ty hiện tại.
        """
        company = request.env.user.company_id
        if not company:
            return {"error": "No company found for the current user"}

        # Chuẩn bị dữ liệu của công ty hiện tại
        company_data = {
            "about_us": company.about_us or "About Us content not available.",
            "social_accounts": {
                "twitter": company.twitter_account or "",
                "facebook": company.facebook_account or "",
                "github": company.github_account or "",
                "linkedin": company.linkedin_account or "",
                "youtube": company.youtube_account or "",
                "instagram": company.instagram_account or "",
                "tiktok": company.tiktok_account or "",
                "zalo": company.zalo_account or "",
            },
            "social_icons": {
                "twitter": f"data:image/png;base64,{company.twitter_icon.decode()}" if company.twitter_icon else "/TuanHA_helloworld/static/src/img/twitter.png",
                "facebook": f"data:image/png;base64,{company.facebook_icon.decode()}" if company.facebook_icon else "/TuanHA_helloworld/static/src/img/facebook.png",
                "github": f"data:image/png;base64,{company.github_icon.decode()}" if company.github_icon else "/TuanHA_helloworld/static/src/img/github.png",
                "linkedin": f"data:image/png;base64,{company.linkedin_icon.decode()}" if company.linkedin_icon else "/TuanHA_helloworld/static/src/img/linkedin.png",
                "youtube": f"data:image/png;base64,{company.youtube_icon.decode()}" if company.youtube_icon else "/TuanHA_helloworld/static/src/img/youtube.png",
                "instagram": f"data:image/png;base64,{company.instagram_icon.decode()}" if company.instagram_icon else "/TuanHA_helloworld/static/src/img/instagram.png",
                "tiktok": f"data:image/png;base64,{company.tiktok_icon.decode()}" if company.tiktok_icon else "/TuanHA_helloworld/static/src/img/tiktok.png",
                "zalo": f"data:image/png;base64,{company.zalo_icon.decode()}" if company.zalo_icon else "/TuanHA_helloworld/static/src/img/zalo.png",
            },
        }
        return company_data