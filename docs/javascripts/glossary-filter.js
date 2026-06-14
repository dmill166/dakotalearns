// Live in-page filter for the Glossary. No-ops on every other page.
// Filters the term sections (each <h2> + its following content) as you type.
(function () {
  function init() {
    var input = document.getElementById("glossary-filter");
    if (!input) return;
    var scope = input.closest(".md-content__inner") || document;

    // Build groups: each h2 heading plus the siblings until the next h2.
    var groups = [];
    scope.querySelectorAll("h2").forEach(function (h) {
      var els = [h], n = h.nextElementSibling;
      while (n && n.tagName !== "H2") { els.push(n); n = n.nextElementSibling; }
      groups.push({ text: els.map(function (e) { return e.textContent.toLowerCase(); }).join(" "), els: els });
    });

    var empty = document.getElementById("glossary-empty");
    input.addEventListener("input", function () {
      var q = this.value.trim().toLowerCase();
      var anyShown = false;
      groups.forEach(function (g) {
        var show = !q || g.text.indexOf(q) > -1;
        if (show) anyShown = true;
        g.els.forEach(function (e) { e.style.display = show ? "" : "none"; });
      });
      if (empty) empty.style.display = anyShown ? "none" : "";
    });
  }
  // Run on first load and on Material's instant-navigation page swaps.
  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(init);
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
