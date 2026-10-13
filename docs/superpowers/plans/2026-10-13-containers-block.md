# Containers Block Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the eight container-task solutions from `Desktop.zip` to `vacuum-xvx/algo` with matching task documentation and repository navigation.

**Architecture:** Add a self-contained `containers/` learning block parallel to `sorting/` and `binary_search/`. Preserve the archive files byte-for-byte, document only tasks A–H, and expose the block through the root README without touching existing solution code.

**Tech Stack:** Python 3.10+, Markdown, Git

**Spec:** `docs/superpowers/specs/2026-10-13-containers-block-design.md`

## Global Constraints

- The source of solutions is `/home/vacuum/Downloads/Telegram Desktop/Desktop.zip`.
- Add only `A.py` through `H.py`; do not import task N from the reference repository.
- Do not modify `sorting/` or `binary_search/`.
- Preserve each solution's contents from the archive.

---

### Task 1: Add the container solutions

**Files:**
- Create: `containers/A.py`
- Create: `containers/B.py`
- Create: `containers/C.py`
- Create: `containers/D.py`
- Create: `containers/E.py`
- Create: `containers/F.py`
- Create: `containers/G.py`
- Create: `containers/H.py`

**Interfaces:**
- Consumes: stdin in each contest problem's documented format.
- Produces: stdout in each contest problem's required format.

- [ ] **Step 1: Confirm the destination files do not exist**

Run:

```bash
test ! -e containers/A.py && test ! -e containers/H.py
```

Expected: exit status 0.

- [ ] **Step 2: Add the archive files without changing their contents**

Create `containers/A.py` through `containers/H.py` with the exact corresponding content from `Desktop.zip`.

- [ ] **Step 3: Verify archive identity**

Run:

```bash
tmp_dir=$(mktemp -d)
unzip -q '/home/vacuum/Downloads/Telegram Desktop/Desktop.zip' -d "$tmp_dir"
for file in A.py B.py C.py D.py E.py F.py G.py H.py; do
  cmp "$tmp_dir/$file" "containers/$file"
done
```

Expected: exit status 0 and no output.

- [ ] **Step 4: Check Python syntax**

Run:

```bash
python -m py_compile containers/A.py containers/B.py containers/C.py containers/D.py containers/E.py containers/F.py containers/G.py containers/H.py
```

Expected: exit status 0 and no output.

- [ ] **Step 5: Run focused smoke examples**

Run:

```bash
printf 'size\npush 1\nback\npop\nexit\n' | python containers/A.py
printf '([]{})\n' | python containers/B.py
printf '8 9 + 1 7 - *\n' | python containers/C.py
printf 'push 1\nfront\npop\nexit\n' | python containers/D.py
printf 'push_front 1\npush_back 2\nfront\nback\nexit\n' | python containers/E.py
printf '7 3\n1 3 2 4 5 3 1\n' | python containers/F.py
printf '3\n1 2 3\n' | python containers/G.py
printf '5\n+ 1\n+ 2\n* 3\n-\n-\n' | python containers/H.py
```

Expected outputs, in order:

```text
0
ok
1
1
bye
yes
-102
ok
1
1
bye
ok
ok
1
2
bye
1
2
2
3
1
YES
1
3
```

- [ ] **Step 6: Commit the solutions**

```bash
git add containers/A.py containers/B.py containers/C.py containers/D.py containers/E.py containers/F.py containers/G.py containers/H.py
git commit -m "feat: add container task solutions"
```

### Task 2: Document and expose the block

**Files:**
- Create: `containers/README.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: solution filenames `A.py`–`H.py`.
- Produces: repository navigation from `README.md` to `containers/README.md`, and task links from the block README to each solution.

- [ ] **Step 1: Add the block README**

Create `containers/README.md` with headings and full problem statements for tasks A–H, following the section structure used by `sorting/README.md` and `binary_search/README.md`. End each task section with its exact relative solution link, for example `### [Решение](A.py)`.

- [ ] **Step 2: Add root navigation**

Append this item to the existing root list:

```markdown
- [Контейнеры](containers/)
```

- [ ] **Step 3: Validate Markdown targets and scope**

Run:

```bash
python - <<'PY'
from pathlib import Path
import re

for readme in (Path('README.md'), Path('containers/README.md')):
    text = readme.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^]]+\]\(([^)]+)\)', text):
        if '://' not in target:
            assert (readme.parent / target).exists(), (readme, target)

containers = sorted(path.name for path in Path('containers').glob('*.py'))
assert containers == [f'{letter}.py' for letter in 'ABCDEFGH'], containers
PY
git diff --check HEAD~1
git diff --name-only HEAD~1 -- sorting binary_search
```

Expected: all commands exit with status 0; the last command prints nothing.

- [ ] **Step 4: Commit the documentation**

```bash
git add README.md containers/README.md
git commit -m "docs: document container tasks"
```

### Task 3: Final repository verification

**Files:**
- Verify: all files introduced by Tasks 1 and 2.

**Interfaces:**
- Consumes: the completed repository tree.
- Produces: evidence that the repository is ready to publish.

- [ ] **Step 1: Inspect the final tree and history**

Run:

```bash
find containers -maxdepth 1 -type f -printf '%f\n' | sort
git status --short --branch
git log -4 --oneline
```

Expected: `A.py`–`H.py` and `README.md`; a clean `main` branch ahead of `origin/main`; documentation and solution commits at the top of history.

- [ ] **Step 2: Re-run all syntax and link checks**

Run:

```bash
python -m py_compile containers/*.py
python - <<'PY'
from pathlib import Path
import re

for readme in (Path('README.md'), Path('containers/README.md')):
    for target in re.findall(r'\[[^]]+\]\(([^)]+)\)', readme.read_text(encoding='utf-8')):
        if '://' not in target:
            assert (readme.parent / target).exists(), (readme, target)
PY
```

Expected: exit status 0 and no output.

- [ ] **Step 3: Publish the approved commits**

Run:

```bash
git push origin main
```

Expected: GitHub accepts the fast-forward update to `vacuum-xvx/algo`.
