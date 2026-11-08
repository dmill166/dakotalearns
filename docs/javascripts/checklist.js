/**
 * Dakota Learns - persistent page checklists.
 *
 * Markdown task lists (`- [ ] item`, rendered by pymdownx.tasklist) arrive
 * as DISABLED checkboxes. This script enables them and persists each page's
 * checked state in localStorage, so a learner working through a "Done looks
 * like" list keeps their progress across visits - on this browser only.
 * No accounts, no server, nothing leaves the machine (matches the course
 * platform decision: light browser-side state, no stored progress).
 *
 * Storage: one key per page path ("dl-checks:<pathname>") holding a JSON
 * array of the checked items' indexes in document order.
 */
(function () {
  "use strict";

  var KEY = "dl-checks:" + window.location.pathname;

  /**
   * Read this page's saved checkbox indexes.
   * @returns {number[]} Indexes of checked items (empty on any error).
   */
  function load() {
    try {
      return JSON.parse(window.localStorage.getItem(KEY)) || [];
    } catch (e) {
      return [];
    }
  }

  /**
   * Persist the currently-checked indexes for this page.
   * @param {HTMLInputElement[]} boxes - All task-list checkboxes, in order.
   * @returns {void}
   */
  function save(boxes) {
    var checked = [];
    boxes.forEach(function (box, i) {
      if (box.checked) checked.push(i);
    });
    try {
      window.localStorage.setItem(KEY, JSON.stringify(checked));
    } catch (e) {
      /* storage full/blocked - checklist still works, just not persisted */
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    var boxes = Array.prototype.slice.call(
      document.querySelectorAll(".md-typeset .task-list-item input[type=checkbox]")
    );
    if (!boxes.length) return;
    var saved = load();
    boxes.forEach(function (box, i) {
      box.disabled = false;
      box.checked = saved.indexOf(i) !== -1;
      box.addEventListener("change", function () {
        save(boxes);
      });
    });
  });
})();
