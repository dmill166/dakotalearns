/**
 * Dakota Learns - self-check renderers: quiz (single-answer MCQ) and
 * Parsons (order-the-lines).
 *
 * Data is authored as fenced ```quiz / ```parsons JSON blocks in the COURSE
 * repo's markdown (format spec: cs-teaching/interactive_checks.md), so it
 * rides the normal *.md content sync. pymdownx.superfences (mkdocs.yml
 * custom_fences) renders each block to <div class="quiz">…</div> /
 * <div class="parsons">…</div>; this script progressively enhances those
 * divs into widgets. If JavaScript fails or the JSON is malformed, the raw
 * block stays visible (readable, never a blank hole).
 *
 * Accessibility (cs-teaching/a11y.md): native radios/buttons only (keyboard
 * + focus for free), visible focus ring, feedback through aria-live, and
 * result state carried by icon + words + color - never color alone.
 * Drag-and-drop always has a keyboard equivalent (move up/down buttons).
 *
 * Documentation standard: JSDoc headers on every function (the JS
 * counterpart of our PEP 8 + docstrings rule for Python - see
 * cs-teaching/STYLE.md "Code style").
 */
(function () {
  "use strict";

  /** Monotonic counter for unique radio-group names across all widgets. */
  var uid = 0;

  /**
   * Escape a string for safe insertion into HTML.
   * @param {string} s - Raw text (may contain &, <, >, ").
   * @returns {string} HTML-safe text.
   */
  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  /**
   * Render the deliberate inline-markdown subset used in quiz/Parsons
   * text: `code` and **bold**. Everything else is escaped verbatim.
   * @param {string} s - Author-written prompt/option/explanation text.
   * @returns {string} HTML with <code>/<strong> applied.
   */
  function inline(s) {
    return escapeHtml(s)
      .replace(/`([^`]+)`/g, "<code>$1</code>")
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  }

  /**
   * Parse a fenced block's JSON payload.
   * @param {Element} el - The <div class="quiz|parsons"> holding raw JSON.
   * @returns {?Object} Parsed data, or null (block is left as-is) on error.
   */
  function parseBlock(el) {
    try {
      return JSON.parse(el.textContent);
    } catch (e) {
      console.warn("Dakota Learns self-check: bad JSON block left as-is.", e, el);
      return null;
    }
  }

  /**
   * Create the shared feedback element. aria-live="polite" makes screen
   * readers announce result changes without stealing focus.
   * @returns {HTMLParagraphElement} Empty feedback paragraph.
   */
  function feedbackEl() {
    var p = document.createElement("p");
    p.className = "dl-feedback";
    p.setAttribute("aria-live", "polite");
    return p;
  }

  /**
   * Write a result into a feedback element. Meaning is carried on three
   * channels: the ✓/✗ icon (aria-hidden), the words, and the color class.
   * @param {HTMLElement} p - Feedback element from feedbackEl().
   * @param {boolean} ok - Whether the answer/order was correct.
   * @param {string} html - Pre-rendered (trusted) message HTML.
   * @returns {void}
   */
  function setFeedback(p, ok, html) {
    p.classList.remove("dl-ok", "dl-no");
    p.classList.add(ok ? "dl-ok" : "dl-no");
    p.innerHTML =
      '<span class="dl-mark" aria-hidden="true">' + (ok ? "✓" : "✗") + "</span> " + html;
  }

  /* ────────────────────────────────────────────────────────────────────
   * Quiz widget
   * Data shape: {title?, questions: [{prompt, options[], answer,
   * explain?, hint?, fixed_order?}]}
   * `answer` is the correct option's text, matching one entry of
   * `options` exactly. Options are shuffled on every load unless
   * `fixed_order` is true (True/False pairs, deliberate sequences).
   * A question whose answer matches no option leaves the whole block
   * raw, with a console warning (the site gate fails such blocks at
   * build time). Learners may retry
   * until correct; a wrong pick never reveals the answer. `hint`
   * renders as a collapsed "Need a hint?" toggle available before
   * answering (a native <details>, keyboard-accessible by default).
   * ──────────────────────────────────────────────────────────────────── */

  /**
   * Replace a raw quiz block with an interactive multiple-choice widget.
   * @param {Element} el - The raw <div class="quiz"> to replace.
   * @param {?Object} data - Parsed quiz JSON (null = leave block as-is).
   * @returns {void}
   */
  function buildQuiz(el, data) {
    if (!data || !Array.isArray(data.questions)) return;
    var bad = data.questions.filter(function (q) {
      return !Array.isArray(q.options) || q.options.indexOf(q.answer) === -1;
    });
    if (bad.length) {
      console.warn("Dakota Learns quiz: answer matches no option; block left as-is.", bad);
      return;
    }
    var root = document.createElement("div");
    root.className = "dl-widget dl-quiz";
    if (data.title) {
      var h = document.createElement("p");
      h.className = "dl-widget-title";
      h.innerHTML = inline(data.title);
      root.appendChild(h);
    }

    data.questions.forEach(function (q, qi) {
      var name = "dl-q" + ++uid; // unique radio group per question
      var fs = document.createElement("fieldset");
      fs.className = "dl-question";
      var lg = document.createElement("legend");
      lg.innerHTML = (data.questions.length > 1 ? qi + 1 + ". " : "") + inline(q.prompt);
      fs.appendChild(lg);

      displayOrder(q).forEach(function (oi) {
        var opt = q.options[oi];
        var label = document.createElement("label");
        label.className = "dl-option";
        var input = document.createElement("input");
        input.type = "radio";
        input.name = name;
        input.value = String(oi);
        label.appendChild(input);
        var span = document.createElement("span");
        span.innerHTML = inline(opt);
        label.appendChild(span);
        fs.appendChild(label);
      });

      if (q.hint) {
        var hint = document.createElement("details");
        hint.className = "dl-hint";
        var sum = document.createElement("summary");
        sum.textContent = "Need a hint?";
        hint.appendChild(sum);
        var hp = document.createElement("p");
        hp.innerHTML = inline(q.hint);
        hint.appendChild(hp);
        fs.appendChild(hint);
      }

      var fb = feedbackEl();
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "dl-btn";
      btn.textContent = "Check my answer";
      btn.addEventListener("click", function () {
        var picked = fs.querySelector("input:checked");
        if (!picked) {
          setFeedback(fb, false, "Pick an answer first.");
          return;
        }
        if (q.options[Number(picked.value)] === q.answer) {
          setFeedback(fb, true, "<strong>Correct!</strong>" + (q.explain ? " " + inline(q.explain) : ""));
        } else {
          setFeedback(fb, false, "Not quite, try again.");
        }
      });
      fs.appendChild(btn);
      fs.appendChild(fb);
      root.appendChild(fs);
    });

    el.replaceWith(root);
  }

  /**
   * Choose the order a question's options are shown in.
   * @param {Object} q - One quiz question.
   * @returns {number[]} Indexes into `q.options`: authored order when
   *   `q.fixed_order` is true, otherwise a fresh random shuffle.
   */
  function displayOrder(q) {
    var idx = q.options.map(function (_, i) { return i; });
    if (q.fixed_order === true) return idx;
    for (var j = idx.length - 1; j > 0; j--) {
      var k = Math.floor(Math.random() * (j + 1));
      var t = idx[j];
      idx[j] = idx[k];
      idx[k] = t;
    }
    return idx;
  }

  /* ────────────────────────────────────────────────────────────────────
   * Parsons widget
   * Data shape: {title?, prompt?, lines[], code?}
   * `lines` are authored in the CORRECT order; the widget shuffles on
   * load (never into the already-correct order) and checks exact order.
   * `code: true` renders lines in monospace.
   * ──────────────────────────────────────────────────────────────────── */

  /**
   * Produce a shuffled index order 0..n-1 that is never the identity
   * (so a Parsons problem can't start out accidentally solved).
   * @param {number} n - Number of lines.
   * @returns {number[]} Shuffled indexes.
   */
  function shuffled(n) {
    var idx = [];
    for (var i = 0; i < n; i++) idx.push(i);
    do {
      for (var j = n - 1; j > 0; j--) {
        var k = Math.floor(Math.random() * (j + 1));
        var t = idx[j];
        idx[j] = idx[k];
        idx[k] = t;
      }
    } while (n > 1 && idx.every(function (v, i2) { return v === i2; }));
    return idx;
  }

  /**
   * Replace a raw parsons block with an order-the-lines widget
   * (HTML5 drag-and-drop + always-available move up/down buttons).
   * @param {Element} el - The raw <div class="parsons"> to replace.
   * @param {?Object} data - Parsed parsons JSON (null = leave block as-is).
   * @returns {void}
   */
  function buildParsons(el, data) {
    if (!data || !Array.isArray(data.lines) || !data.lines.length) return;
    var root = document.createElement("div");
    root.className = "dl-widget dl-parsons";
    var title = document.createElement("p");
    title.className = "dl-widget-title";
    title.innerHTML = inline(data.title || "Put the lines in order");
    root.appendChild(title);
    if (data.prompt) {
      var pr = document.createElement("p");
      pr.innerHTML = inline(data.prompt);
      root.appendChild(pr);
    }

    var list = document.createElement("ol");
    list.className = "dl-parsons-list";

    /**
     * Build one draggable line item. `data-key` remembers the line's
     * correct position; the check compares DOM order against it.
     * @param {number} lineIdx - Index into data.lines (= correct slot).
     * @returns {HTMLLIElement} The list item.
     */
    function makeItem(lineIdx) {
      var li = document.createElement("li");
      li.className = "dl-parsons-line";
      li.dataset.key = String(lineIdx);
      li.draggable = true;
      var text = document.createElement(data.code ? "code" : "span");
      text.className = "dl-line-text";
      text.textContent = data.lines[lineIdx];
      li.appendChild(text);

      // Keyboard path: real buttons, so Tab/Enter/Space work natively.
      ["up", "down"].forEach(function (dir) {
        var b = document.createElement("button");
        b.type = "button";
        b.className = "dl-btn dl-move";
        b.textContent = dir === "up" ? "↑" : "↓";
        b.setAttribute(
          "aria-label",
          "Move “" + data.lines[lineIdx] + "” " + (dir === "up" ? "up" : "down")
        );
        b.addEventListener("click", function () {
          var sib = dir === "up" ? li.previousElementSibling : li.nextElementSibling;
          if (!sib) return;
          if (dir === "up") list.insertBefore(li, sib);
          else list.insertBefore(sib, li);
          b.focus(); // keep keyboard focus on the button that moved
        });
        li.appendChild(b);
      });

      li.addEventListener("dragstart", function (ev) {
        dragging = li;
        li.classList.add("dl-dragging");
        ev.dataTransfer.effectAllowed = "move";
        ev.dataTransfer.setData("text/plain", ""); // Firefox needs data set
      });
      li.addEventListener("dragend", function () {
        li.classList.remove("dl-dragging");
        dragging = null;
      });
      return li;
    }

    /** Currently dragged <li>, or null when no drag is in progress. */
    var dragging = null;
    list.addEventListener("dragover", function (ev) {
      if (!dragging) return;
      ev.preventDefault();
      var over = ev.target.closest("li.dl-parsons-line");
      if (!over || over === dragging) return;
      // Insert above or below depending on which half the pointer is in.
      var rect = over.getBoundingClientRect();
      var before = ev.clientY < rect.top + rect.height / 2;
      list.insertBefore(dragging, before ? over : over.nextElementSibling);
    });

    shuffled(data.lines.length).forEach(function (i) {
      list.appendChild(makeItem(i));
    });
    root.appendChild(list);

    var fb = feedbackEl();
    var check = document.createElement("button");
    check.type = "button";
    check.className = "dl-btn";
    check.textContent = "Check my order";
    check.addEventListener("click", function () {
      var keys = Array.prototype.map.call(list.children, function (li) {
        return Number(li.dataset.key);
      });
      var right = keys.filter(function (k, i) { return k === i; }).length;
      if (right === keys.length) {
        setFeedback(fb, true, "<strong>Correct order!</strong>");
      } else {
        setFeedback(fb, false, "Not quite: " + right + " of " + keys.length + " lines are in the right spot. Keep going.");
      }
    });
    var reset = document.createElement("button");
    reset.type = "button";
    reset.className = "dl-btn dl-btn-quiet";
    reset.textContent = "Shuffle again";
    reset.addEventListener("click", function () {
      var items = Array.prototype.slice.call(list.children);
      shuffled(items.length).forEach(function (i) {
        var li = items.filter(function (x) { return Number(x.dataset.key) === i; })[0];
        list.appendChild(li);
      });
      fb.textContent = "";
      fb.classList.remove("dl-ok", "dl-no");
    });
    root.appendChild(check);
    root.appendChild(reset);
    root.appendChild(fb);

    el.replaceWith(root);
  }

  // Enhance every quiz/parsons block once the page's DOM is ready.
  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("div.quiz").forEach(function (el) {
      buildQuiz(el, parseBlock(el));
    });
    document.querySelectorAll("div.parsons").forEach(function (el) {
      buildParsons(el, parseBlock(el));
    });
  });
})();
