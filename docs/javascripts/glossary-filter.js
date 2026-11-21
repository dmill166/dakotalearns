// Purpose: The Glossary's live filter box: hides terms that don't match what
//   you type.
// Live in-page filter for the Glossary. No-ops on every other page.
// Filters the terms (each <h3> + its content) as you type; a section
// heading (<h2>) hides when none of its terms match.
(function () {
  function init() {
    var input = document.getElementById("glossary-filter");
    if (!input) return;
    var scope = input.closest(".md-content__inner") || document;

    // Build groups: each term (an h3) plus its content up to the next
    // heading. Section headings (h2) hide when none of their terms match.
    var groups = [], sections = [];
    scope.querySelectorAll("h2").forEach(function (h2) {
      var sec = { head: h2, intro: [], groups: [] };
      var n = h2.nextElementSibling, cur = null;
      while (n && n.tagName !== "H2") {
        if (n.tagName === "H3") { cur = { els: [n] }; sec.groups.push(cur); groups.push(cur); }
        else if (cur) { cur.els.push(n); }
        else { sec.intro.push(n); }
        n = n.nextElementSibling;
      }
      sec.groups.forEach(function (g) {
        g.text = g.els.map(function (e) { return e.textContent.toLowerCase(); }).join(" ");
      });
      if (sec.groups.length) sections.push(sec);
    });

    var empty = document.getElementById("glossary-empty");
    input.addEventListener("input", function () {
      var q = this.value.trim().toLowerCase();
      var anyShown = false;
      sections.forEach(function (sec) {
        var secShown = false;
        sec.groups.forEach(function (g) {
          var show = !q || g.text.indexOf(q) > -1;
          if (show) { anyShown = true; secShown = true; }
          g.els.forEach(function (e) { e.style.display = show ? "" : "none"; });
        });
        [sec.head].concat(sec.intro).forEach(function (e) {
          e.style.display = secShown ? "" : "none";
        });
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
