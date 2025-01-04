/** @odoo-module **/
import publicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";
import { renderToElement } from "@web/core/utils/render";

let SocialSnippet = publicWidget.Widget.extend({
  selector: ".user-info-box",
  start: function () {
    // Fetch dữ liệu từ API
    jsonrpc("/about_us", {})
      .then((res) => {
        if (res) {
          // Xử lý cho social-normal
          const aboutUsContainer = this.$el.find(".social-normal");
          aboutUsContainer.html(`
                <div>
                    <div class="social-media">
                        ${Object.entries(res.social_accounts)
                          .map(
                            ([platform, link]) => `
                            ${
                              link
                                ? `
                                <a href="${link}" target="_blank" style="text-decoration: none; margin-right: 5px">
                                    <img src="${res.social_icons[platform]}" alt="${platform}" style="width:24px;height:24px;">
                                </a>`
                                : ""
                            }
                        `
                          )
                          .join("")}
                    </div>
                </div>
            `);

          // Xử lý cho social-premium (dropdown)
          const premiumContainer = this.$el.find(".social-premium");
          premiumContainer.html(`
                <div class="dropdown-social">
                    <button class="dropdown-toggle-social"><i class="fa-brands fa-cloudversify"></i></button>
                    <div class="dropdown-menu-social">
                        ${Object.entries(res.social_accounts)
                          .map(
                            ([platform, link]) => `
                            ${
                              link
                                ? `
                                <a href="${link}" target="_blank" class="dropdown-item-social">
                                    <img src="${res.social_icons[platform]}" alt="${platform}" style="width:24px;height:24px; margin-right: 5px;">
                                </a>`
                                : ""
                            }
                        `
                          )
                          .join("")}
                    </div>
                </div>
            `);
        }
      })
      .catch((err) => {
        console.error("Error fetching about data:", err);
      });
  },
});

publicWidget.registry.SocialSnippet = SocialSnippet;
