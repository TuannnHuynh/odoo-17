/** @odoo-module **/
import publicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";
import { renderToElement } from "@web/core/utils/render";

let AboutUsSnippet = publicWidget.Widget.extend({
  selector: ".about",
  start: function () {
    jsonrpc("/about_us", {})
      .then((res) => {
        if (res) {
          const aboutUsContainer = this.$el.find(".about-us");
          aboutUsContainer.html(`
                <div>
                        <p>${res.about_us}</p>
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
        }
      })
      .catch((err) => {
        console.error("Error fetching about data:", err);
      });
  },
});

publicWidget.registry.AboutUsSnippet = AboutUsSnippet;
