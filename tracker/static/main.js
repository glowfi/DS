window.addEventListener('DOMContentLoaded', () => {
    /* -------------------------------------------------
       1️⃣  Reorder topics (accordion) – unchanged
       ------------------------------------------------- */
    const accordion = document.getElementById('topics-accordion');
    if (accordion) {
        Sortable.create(accordion, {
            animation: 150,
            handle: '.accordion-header',
            onEnd: () => {
                const ids = Array.from(
                    accordion.querySelectorAll('.accordion-item')
                ).map((item) => item.dataset.id);
                fetch('/topics/reorder', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(ids)
                });
            }
        });
    }

    /* -------------------------------------------------
       2️⃣  Reorder questions inside each topic
       ------------------------------------------------- */
    document.querySelectorAll('tbody[id^="questions-"]').forEach((tbody) => {
        const topicId = tbody.id.split('-')[1]; // e.g. "questions-3" → "3"

        Sortable.create(tbody, {
            animation: 150,
            handle: 'td', // drag by any cell (you can change to a specific column)
            onEnd: () => {
                const qIds = Array.from(tbody.querySelectorAll('tr')).map(
                    (tr) => tr.dataset.id
                );

                // POST the new order for this specific topic
                fetch(`/questions/reorder/${topicId}`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(qIds)
                });
            }
        });
    });

    /* -------------------------------------------------
       3️⃣  Collapse / Expand all (unchanged)
       ------------------------------------------------- */
    const expandBtn = document.getElementById('expand-all');
    const collapseBtn = document.getElementById('collapse-all');
    const collapseEls = accordion.querySelectorAll('.accordion-collapse');

    expandBtn.addEventListener('click', () => {
        collapseEls.forEach((el) => {
            const bs =
                bootstrap.Collapse.getInstance(el) ||
                new bootstrap.Collapse(el);
            bs.show();
        });
    });
    collapseBtn.addEventListener('click', () => {
        collapseEls.forEach((el) => {
            const bs =
                bootstrap.Collapse.getInstance(el) ||
                new bootstrap.Collapse(el);
            bs.hide();
        });
    });

    /* -------------------------------------------------
       4️⃣  Toggle question completion
       ------------------------------------------------- */
    document.querySelectorAll('.q-toggle').forEach((cb) => {
        cb.addEventListener('change', async () => {
            const qId = cb.dataset.id;
            const tbody = cb.closest('tbody');
            const topicId = tbody.id.split('-')[1]; // "questions-<topicId>"

            try {
                const resp = await fetch('/question/toggle/' + qId, {
                    method: 'POST'
                });
                if (!resp.ok) throw new Error('toggle failed');

                // update per‑topic fraction and global left count
                refreshFraction(topicId);
                refreshGlobalLeft();
            } catch (err) {
                console.error(err);
            }
        });
    });

    /* -------------------------------------------------
       5️⃣  Edit a question
       ------------------------------------------------- */

    document.querySelectorAll('.edit-btn').forEach((btn) => {
        btn.addEventListener('click', () => {
            const row = btn.closest('tr');
            const qId = btn.dataset.id;

            document.getElementById('edit-q-id').value = qId;
            document.getElementById('edit-problem').value = row
                .querySelector('.editable-problem')
                .textContent.trim();
            document.getElementById('edit-pattern').value = row
                .querySelector('.editable-pattern')
                .textContent.trim();
            document.getElementById('edit-link').value = row
                .querySelector('.question-link')
                .href.trim();

            new bootstrap.Modal(
                document.getElementById('editQuestionModal')
            ).show();
        });
    });

    document
        .getElementById('editQuestionForm')
        .addEventListener('submit', async (e) => {
            e.preventDefault();
            const qId = document.getElementById('edit-q-id').value;
            const problem = document.getElementById('edit-problem').value;
            const pattern = document.getElementById('edit-pattern').value;
            const link = document.getElementById('edit-link').value;

            const resp = await fetch(`/question/edit/${qId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: new URLSearchParams({ problem, pattern, link })
            });
            const data = await resp.json();
            if (data.ok) location.reload();
            else alert(data.error || 'Update failed');
        });
    // document.querySelectorAll('.edit-btn').forEach((btn) => {
    //     btn.addEventListener('click', () => {
    //         const id = btn.dataset.id;
    //         const row = btn.closest('tr');
    //         const problem = row
    //             .querySelector('.editable-problem')
    //             .textContent.trim();
    //         const pattern = row
    //             .querySelector('.editable-pattern')
    //             .textContent.trim();
    //         const questionLink = row
    //             .querySelector('.question-link')
    //             .href.trim();

    //         const newProblem = prompt('Edit problem:', problem);
    //         if (newProblem === null) return;
    //         const newPattern = prompt('Edit pattern:', pattern);
    //         if (newPattern === null) return;
    //         const newQuestionLink = prompt('Edit question link:', questionLink);
    //         if (newQuestionLink === null) return;

    //         fetch(`/question/edit/${id}`, {
    //             method: 'POST',
    //             headers: {
    //                 'Content-Type': 'application/x-www-form-urlencoded'
    //             },
    //             body: new URLSearchParams({
    //                 problem: newProblem,
    //                 pattern: newPattern,
    //                 link: newQuestionLink
    //             })
    //         })
    //             .then((r) => r.json())
    //             .then((data) => {
    //                 if (data.ok) location.reload();
    //                 else alert(data.error || 'Failed to update');
    //             });
    //     });
    // });

    /* -------------------------------------------------
       6️⃣  Delete a question
       ------------------------------------------------- */
    document.querySelectorAll('.delete-btn').forEach((btn) => {
        btn.addEventListener('click', () => {
            if (!confirm('Delete this question?')) return;
            fetch(`/question/delete/${btn.dataset.id}`, { method: 'POST' })
                .then((r) => r.json())
                .then((data) => {
                    if (data.ok) location.reload();
                    else alert('Delete failed');
                });
        });
    });

    /* -------------------------------------------------
       7️⃣  Copy problem text
       ------------------------------------------------- */
    document.querySelectorAll('.copy-btn').forEach((btn) => {
        btn.addEventListener('click', async () => {
            const row = btn.closest('tr');
            const problem = row
                .querySelector('.editable-problem')
                .textContent.trim();
            const pattern = row
                .querySelector('.editable-pattern')
                .textContent.trim();
            const link = row.querySelector('.question-link').href.trim();

            const text = `${problem};${pattern};${link}`;

            try {
                await navigator.clipboard.writeText(text);
                const originalTitle = btn.title;
                btn.title = 'Copied!';
                btn.classList.add('text-success');

                setTimeout(() => {
                    btn.title = originalTitle;
                    btn.classList.remove('text-success');
                }, 1500);
            } catch (err) {
                console.error('Copy failed', err);
                alert(
                    'Unable to copy text. Your browser may block clipboard access.'
                );
            }
        });
    });

    /* -------------------------------------------------
       8️⃣  Helper: per‑topic fraction (completed/total)
       ------------------------------------------------- */
    function refreshFraction(topicId) {
        const tbody = document.getElementById(`questions-${topicId}`);
        const rows = tbody ? tbody.querySelectorAll('tr') : [];
        const total = rows.length;
        let completed = 0;
        rows.forEach((r) => {
            const chk = r.querySelector('.q-toggle');
            if (chk && chk.checked) completed++;
        });

        const fractionEl = document.querySelector(`#status-${topicId}`);
        if (fractionEl) {
            const left = total - completed;
            fractionEl.textContent = `${completed} / ${total} completed (${left} left)`;
        }
    }

    /* -------------------------------------------------
       9️⃣  Helper: global left count (all topics)
       ------------------------------------------------- */
    function refreshGlobalLeft() {
        const rows = document.querySelectorAll('tbody tr');
        let left = 0;
        rows.forEach((row) => {
            const chk = row.querySelector('.q-toggle');
            if (chk && !chk.checked) left++;
        });

        const badge = document.getElementById('global-left-badge');
        if (badge) badge.textContent = `${left} left`;
    }

    // Initialise global left badge on first load
    refreshGlobalLeft();

    // Batch delete
    document
        .getElementById('delete-selected-questions')
        .addEventListener('click', async () => {
            const selected = Array.from(
                document.querySelectorAll('.q-batch-select:checked')
            ).map((cb) => cb.dataset.id);
            if (selected.length === 0) return alert('No questions selected');

            if (
                !confirm(
                    `Are you sure you want to delete ${selected.length} question(s)?`
                )
            )
                return;

            const resp = await fetch('/questions/delete_batch', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(selected)
            });
            const data = await resp.json();
            if (data.ok) location.reload();
            else alert('Delete failed');
        });

    // Move questions
    document
        .getElementById('move-selected-questions')
        .addEventListener('change', async (e) => {
            const targetTopicId = e.target.value;
            if (!targetTopicId) return;

            const selected = Array.from(
                document.querySelectorAll('.q-batch-select:checked')
            ).map((cb) => cb.dataset.id);
            if (selected.length === 0) return alert('No questions selected');

            const targetTopicName =
                e.target.options[e.target.selectedIndex].text;
            if (
                !confirm(
                    `Move ${selected.length} question(s) to "${targetTopicName}"?`
                )
            )
                return;

            const resp = await fetch('/questions/move', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    question_ids: selected,
                    target_topic_id: targetTopicId
                })
            });
            const data = await resp.json();
            if (data.ok) location.reload();
            else alert('Move failed');
        });

    // Select / deselect all questions in a topic
    document.querySelectorAll('.select-all-questions').forEach((cb) => {
        cb.addEventListener('change', () => {
            const topicId = cb.dataset.topicId;
            const checkboxes = document.querySelectorAll(
                `#questions-${topicId} .q-batch-select`
            );
            checkboxes.forEach((qcb) => (qcb.checked = cb.checked));
        });
    });

    document
        .getElementById('delete-selected-topics')
        .addEventListener('click', async () => {
            const selected = Array.from(
                document.querySelectorAll('.topic-batch-select:checked')
            ).map((cb) => cb.dataset.id);
            if (selected.length === 0) return alert('No topics selected');
            if (
                !confirm(
                    `Are you sure you want to delete ${selected.length} topic(s) and all their questions?`
                )
            )
                return;

            const resp = await fetch('/topics/delete_batch', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(selected)
            });
            const data = await resp.json();
            if (data.ok) location.reload();
            else alert('Delete failed');
        });

    document
        .getElementById('select-all-topics')
        .addEventListener('change', (e) => {
            const checked = e.target.checked;
            document
                .querySelectorAll('.topic-batch-select')
                .forEach((cb) => (cb.checked = checked));
        });

    /* -------------------------------------------------
       10️⃣  Rename Topic
       ------------------------------------------------- */
    document.querySelectorAll('.rename-topic-btn').forEach((btn) => {
        btn.addEventListener('click', () => {
            const topicId = btn.dataset.id;
            const currentName = btn.dataset.name;

            document.getElementById('rename-topic-id').value = topicId;
            document.getElementById('rename-topic-name').value = currentName;

            new bootstrap.Modal(
                document.getElementById('renameTopicModal')
            ).show();
        });
    });

    document
        .getElementById('renameTopicForm')
        .addEventListener('submit', async (e) => {
            e.preventDefault();
            const topicId = document.getElementById('rename-topic-id').value;
            const newName = document
                .getElementById('rename-topic-name')
                .value.trim();

            if (!newName) {
                alert('Name cannot be empty');
                return;
            }

            const resp = await fetch(`/topic/rename/${topicId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: new URLSearchParams({ name: newName })
            });

            const data = await resp.json();
            if (data.ok) {
                // Update the name in the UI without a full reload
                const header = document.querySelector(
                    `.accordion-item[data-id="${topicId}"] strong`
                );
                if (header) header.textContent = data.name;

                // Also update the data-name attribute on the rename button
                const renameBtn = document.querySelector(
                    `.rename-topic-btn[data-id="${topicId}"]`
                );
                if (renameBtn) renameBtn.dataset.name = data.name;

                // Hide modal
                bootstrap.Modal.getInstance(
                    document.getElementById('renameTopicModal')
                ).hide();
            } else {
                alert(data.error || 'Rename failed');
            }
        });
});
