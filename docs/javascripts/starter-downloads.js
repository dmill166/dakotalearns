/**
 * Dakota Learns - starter-file downloads.
 *
 * Course pages link starter files with plain relative links
 * (`starter/checkpoint_1.py`), which open the file's page on GitHub and
 * the file itself here. The sync copies each `starter/` folder next to its
 * page, so on the site this script marks those links as downloads: the
 * browser saves the file instead of showing it as text.
 */
(function () {
  "use strict";

  /**
   * Add the `download` attribute to every same-site link into a
   * `starter/` folder.
   * @returns {void}
   */
  function markStarterLinks() {
    document.querySelectorAll("article a[href]").forEach(function (a) {
      var url = new URL(a.getAttribute("href"), window.location.href);
      if (url.origin !== window.location.origin) return;
      if (!/\/starter\/[^/]+$/.test(url.pathname)) return;
      var name = url.pathname.split("/").pop();
      a.setAttribute("download", name);
      a.setAttribute("title", "Download " + name);
    });
  }

  // Material's instant navigation swaps pages without a full load;
  // document$ fires on each page when it is enabled.
  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(markStarterLinks);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", markStarterLinks);
  } else {
    markStarterLinks();
  }
})();
