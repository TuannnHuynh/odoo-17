/** @odoo-module **/

import options from "@web_editor/js/editor/snippets.options";

options.registry.AboutBorder = options.Class.extend({
  setBorder: function (previewMode, widgetValue, params) {
    const borderStyle = params.data.border; // Lấy kiểu border
    this.$target.css("border-style", borderStyle); // Áp dụng border cho phần tử
  },
});

export default {
  AboutBorder: options.registry.AboutBorder,
};
