# Proposed ratchets

Generated from this pass's codebase-profile inference (Guides 11, G#2907) — informational
only. Nothing here is wired into `pm-agent.yaml` automatically. To adopt one: save its
script under the path shown, run it once with `--update-baseline` to seed a real baseline
(or `ibuild engine ratchet add <template>`, which does both steps for you), and add its
manifest snippet to `pm-agent.yaml`.

## `any` casts (`any-casts`)

`as any` / `: any` occurrences must not grow — name the real type instead.

Category: `coding-conventions`

**Script** — save as `scripts/ci/ratchets/any-casts.mjs`:

```javascript
/**
 * `any` casts ratchet — `node any-casts.mjs`.
 *
 * `as any` / `: any` occurrences must not grow — name the real type instead.
 *
 * Scaffolded by `ibuild engine ratchet add any-casts` (Guides 11, G#2907) — generalized from
 * InteractorOSS/website's `scripts/style-ratchet.mjs`, the reference implementation this
 * shape is ported from. The baseline only ratchets DOWN: when a PR reduces a count, lower the
 * number in any-casts.ratchet.json in the same PR. Raising it is a deliberate, reviewable decision —
 * never a side effect.
 *
 * Declare it in pm-agent.yaml:
 *   ratchets:
 *     - name: any-casts
 *       command: [node any-casts.mjs]
 *       description: "`as any` / `: any` occurrences must not grow — name the real type instead."
 *       category: coding-conventions
 */
import { readdirSync, readFileSync, statSync, writeFileSync, realpathSync, existsSync } from "node:fs";
import { join, relative, dirname } from "node:path";
import { fileURLToPath } from "node:url";

/** Realpath-normalized self-exec check: `import.meta.url` and `process.argv[1]` can disagree on
 *  whether a directory a symlink resolves to (e.g. macOS's /var -> /private/var) is canonical, so a
 *  bare string comparison can read "not main" for the very process running this file. Falls back to
 *  the plain comparison if either path can't be resolved (never crashes the guard itself). */
function isMainModule() {
  if (!process.argv[1]) return false;
  const here = fileURLToPath(import.meta.url);
  try {
    return realpathSync(here) === realpathSync(process.argv[1]);
  } catch {
    return here === process.argv[1];
  }
}

/** Walk up from this script's own directory to find the repo root (a `.git` dir), so `srcDir`
 *  resolves correctly REGARDLESS of how deep this script is scaffolded (repo root, scripts/,
 *  scripts/ci/ratchets/, …). Falls back to the script's own directory if none is found (e.g. a
 *  repo checked out without .git) — the same directory the reference implementation assumed. */
function findRepoRoot(start) {
  let dir = start;
  for (let i = 0; i < 20; i++) {
    if (existsSync(join(dir, ".git"))) return dir;
    const parent = dirname(dir);
    if (parent === dir) break;
    dir = parent;
  }
  return start;
}

const HERE = dirname(fileURLToPath(import.meta.url));
const SRC = join(findRepoRoot(HERE), "apps/web/src");
const BASELINE_PATH = join(HERE, "any-casts.ratchet.json");
const EXTENSIONS = ["ts", "tsx"];

export const PATTERNS = {
  "anyCast": /\bas any\b|:\s*any\b/g,
};

/**
 * Blank out everything that is NOT code — comments and string literals — before the patterns run.
 *
 * WHY THIS EXISTS. The patterns are deliberately plain regexes, and `: any` matches ordinary
 * English: "on purpose: any step can come back as skipped", "the ONLY boundary: any page throw",
 * "the same path as any other reference cell". Every one of those is a doc comment, and every one
 * counted as a cast. At the time this was added, 208 of the tree's 446 matches — 46.6% — came from
 * comments and strings, so the number was measuring prose about as much as it measured `any`.
 *
 * That is not cosmetic. A ratchet's whole value is that a rising number means new debt, and this
 * one rose when somebody WROTE A COMMENT. The baseline had been raised nine times, and the commit
 * messages say what was happening: "inherited, and not a cast at all", "inherited from main, not
 * from this goal", "stop a doc comment from counting as a cast". Four separate goals raised it
 * 425 -> 427 for the same drift they had not caused. Each raise made the next real regression
 * harder to see.
 *
 * CHARACTERS ARE REPLACED, NEVER REMOVED — spaces for content, newlines kept — so every offset
 * and line number in the blanked text still matches the original file. A future change that wants
 * to report the line a cast sits on gets that for free rather than having to re-derive it.
 *
 * TEMPLATE SUBSTITUTIONS STAY CODE. Inside a backtick string, `${...}` is executable, and a cast
 * can legitimately live there — `` `${(x as any).id}` `` is a real cast that must still count.
 * The scanner tracks brace depth inside a substitution so a nested object literal or a nested
 * template does not end it early.
 *
 * NOT HANDLED, deliberately: a regex literal containing `: any`. Distinguishing `/` division from
 * a regex needs real parsing, and guessing wrong would blank live code and HIDE a cast — a false
 * negative, which is the one failure mode a ratchet must never have. A regex containing `: any`
 * would still over-count, exactly as today; it is rare, and over-counting is the safe direction.
 */
/** Whether a match inside a string literal is a FALSE POSITIVE for this ratchet — see
 *  patternLivesInStrings in the generator. Comments are always stripped; strings are not. */
const STRIP_STRINGS = true;

export function stripNonCode(source) {
  let out = "";
  let i = 0;
  const n = source.length;
  // `code` | `line` | `block` | `sq` | `dq` | `tpl`
  let state = "code";
  // Open `${` substitutions, innermost last; each entry is that substitution's brace depth.
  const tplStack = [];
  let braceDepth = 0;

  const keep = (ch) => (ch === "\n" ? "\n" : " ");

  while (i < n) {
    const c = source[i];
    const d = source[i + 1];

    if (state === "code") {
      if (c === "/" && d === "/") { state = "line"; out += "  "; i += 2; continue; }
      if (c === "/" && d === "*") { state = "block"; out += "  "; i += 2; continue; }
      if (STRIP_STRINGS && c === "'") { state = "sq"; out += " "; i += 1; continue; }
      if (STRIP_STRINGS && c === '"') { state = "dq"; out += " "; i += 1; continue; }
      if (STRIP_STRINGS && c === "`") { state = "tpl"; out += " "; i += 1; continue; }
      // Track braces only while inside a template substitution, so `}` can close it.
      if (tplStack.length > 0) {
        if (c === "{") braceDepth += 1;
        else if (c === "}") {
          if (braceDepth === tplStack[tplStack.length - 1]) {
            braceDepth = tplStack.pop();
            state = "tpl";
            out += " ";
            i += 1;
            continue;
          }
          braceDepth -= 1;
        }
      }
      out += c;
      i += 1;
      continue;
    }

    if (state === "line") {
      if (c === "\n") { state = "code"; out += "\n"; } else out += " ";
      i += 1;
      continue;
    }

    if (state === "block") {
      if (c === "*" && d === "/") { state = "code"; out += "  "; i += 2; continue; }
      out += keep(c);
      i += 1;
      continue;
    }

    if (state === "sq" || state === "dq") {
      const quote = state === "sq" ? "'" : '"';
      if (c === "\\") { out += "  "; i += 2; continue; }
      if (c === quote) { state = "code"; out += " "; i += 1; continue; }
      out += keep(c);
      i += 1;
      continue;
    }

    // state === "tpl"
    if (c === "\\") { out += "  "; i += 2; continue; }
    if (c === "`") { state = "code"; out += " "; i += 1; continue; }
    if (c === "$" && d === "{") {
      // Re-enter code for the substitution; remember the depth that closes it.
      tplStack.push(braceDepth);
      state = "code";
      out += "  ";
      i += 2;
      continue;
    }
    out += keep(c);
    i += 1;
  }

  return out;
}

export function countInSource(source) {
  // Count against CODE only — see stripNonCode for why a plain match over raw text was measuring
  // English prose alongside real casts.
  const code = stripNonCode(source);
  const counts = {};
  for (const [name, re] of Object.entries(PATTERNS)) {
    counts[name] = (code.match(re) ?? []).length;
  }
  return counts;
}

function matchesExtension(file) {
  return EXTENSIONS.some((ext) => file.endsWith("." + ext));
}

function* walk(dir) {
  let entries;
  try {
    entries = readdirSync(dir);
  } catch {
    return;
  }
  for (const entry of entries) {
    if (entry === "node_modules" || entry.startsWith(".")) continue;
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) yield* walk(full);
    else if (matchesExtension(full)) yield full;
  }
}

export function countTree(root = SRC) {
  const totals = Object.fromEntries(Object.keys(PATTERNS).map((k) => [k, 0]));
  const perFile = [];
  for (const file of walk(root)) {
    const c = countInSource(readFileSync(file, "utf8"));
    for (const k of Object.keys(totals)) totals[k] += c[k];
    if (Object.values(c).some((n) => n > 0)) perFile.push({ file: relative(root, file), ...c });
  }
  return { totals, perFile };
}

export function compare(totals, baseline) {
  const failures = [];
  const improvements = [];
  for (const [k, max] of Object.entries(baseline)) {
    const n = totals[k] ?? 0;
    if (n > max) failures.push({ metric: k, actual: n, baseline: max });
    else if (n < max) improvements.push({ metric: k, actual: n, baseline: max });
  }
  return { failures, improvements };
}

function readBaseline() {
  try {
    return JSON.parse(readFileSync(BASELINE_PATH, "utf8"));
  } catch {
    return Object.fromEntries(Object.keys(PATTERNS).map((k) => [k, 0]));
  }
}

if (isMainModule()) {
  const { totals, perFile } = countTree();

  if (process.argv.includes("--update-baseline")) {
    writeFileSync(BASELINE_PATH, JSON.stringify(totals, null, 2) + "\n");
    console.log("any-casts" + "-ratchet: baseline updated to " + JSON.stringify(totals));
    process.exit(0);
  }

  const baseline = readBaseline();
  const { failures, improvements } = compare(totals, baseline);

  for (const k of Object.keys(baseline)) {
    console.log("any-casts" + "-ratchet: " + k + " = " + totals[k] + " (baseline " + baseline[k] + ")");
  }
  if (failures.length > 0) {
    for (const f of failures) {
      console.error("\n" + "any-casts" + "-ratchet: " + f.metric + " is " + f.actual + ", above the baseline of " + f.baseline + ".");
    }
    const top = [...perFile]
      .sort((a, b) => Object.keys(PATTERNS).reduce((s, k) => s + (b[k] ?? 0) - (a[k] ?? 0), 0))
      .slice(0, 8);
    if (top.length > 0) {
      console.error("Largest contributors:");
      for (const f of top) {
        const counts = Object.keys(PATTERNS).map((k) => (f[k] ?? 0) + " " + k).join(", ");
        console.error("  " + f.file + ": " + counts);
      }
    }
    console.error(
      "\nIf the increase is genuinely a one-off, raise the number in " + "any-casts.ratchet.json" +
        " in this PR and say why in the PR body (goal-pr-body.ts's ratchetRaise declaration).",
    );
    process.exit(1);
  }
  if (improvements.length > 0) {
    console.log(
      "\n" + "any-casts" + "-ratchet: counts dropped below the baseline — run with --update-baseline " +
        "to lower " + improvements.map((i) => i.metric + "=" + i.actual).join(", ") + " in this PR.",
    );
  }
}
```

**pm-agent.yaml snippet:**

```yaml
ratchets:
  - name: any-casts
    command: [node scripts/ci/ratchets/any-casts.mjs]
    description: "`as any` / `: any` occurrences must not grow — name the real type instead."
    category: coding-conventions
```

## Skipped tests (`skipped-tests`)

`.skip(` / `xit(` occurrences must not grow — a skipped test is a debt, not a pass.

Category: `testing`

**Script** — save as `scripts/ci/ratchets/skipped-tests.mjs`:

```javascript
/**
 * Skipped tests ratchet — `node skipped-tests.mjs`.
 *
 * `.skip(` / `xit(` occurrences must not grow — a skipped test is a debt, not a pass.
 *
 * Scaffolded by `ibuild engine ratchet add skipped-tests` (Guides 11, G#2907) — generalized from
 * InteractorOSS/website's `scripts/style-ratchet.mjs`, the reference implementation this
 * shape is ported from. The baseline only ratchets DOWN: when a PR reduces a count, lower the
 * number in skipped-tests.ratchet.json in the same PR. Raising it is a deliberate, reviewable decision —
 * never a side effect.
 *
 * Declare it in pm-agent.yaml:
 *   ratchets:
 *     - name: skipped-tests
 *       command: [node skipped-tests.mjs]
 *       description: "`.skip(` / `xit(` occurrences must not grow — a skipped test is a debt, not a pass."
 *       category: testing
 */
import { readdirSync, readFileSync, statSync, writeFileSync, realpathSync, existsSync } from "node:fs";
import { join, relative, dirname } from "node:path";
import { fileURLToPath } from "node:url";

/** Realpath-normalized self-exec check: `import.meta.url` and `process.argv[1]` can disagree on
 *  whether a directory a symlink resolves to (e.g. macOS's /var -> /private/var) is canonical, so a
 *  bare string comparison can read "not main" for the very process running this file. Falls back to
 *  the plain comparison if either path can't be resolved (never crashes the guard itself). */
function isMainModule() {
  if (!process.argv[1]) return false;
  const here = fileURLToPath(import.meta.url);
  try {
    return realpathSync(here) === realpathSync(process.argv[1]);
  } catch {
    return here === process.argv[1];
  }
}

/** Walk up from this script's own directory to find the repo root (a `.git` dir), so `srcDir`
 *  resolves correctly REGARDLESS of how deep this script is scaffolded (repo root, scripts/,
 *  scripts/ci/ratchets/, …). Falls back to the script's own directory if none is found (e.g. a
 *  repo checked out without .git) — the same directory the reference implementation assumed. */
function findRepoRoot(start) {
  let dir = start;
  for (let i = 0; i < 20; i++) {
    if (existsSync(join(dir, ".git"))) return dir;
    const parent = dirname(dir);
    if (parent === dir) break;
    dir = parent;
  }
  return start;
}

const HERE = dirname(fileURLToPath(import.meta.url));
const SRC = join(findRepoRoot(HERE), "apps/web/src");
const BASELINE_PATH = join(HERE, "skipped-tests.ratchet.json");
const EXTENSIONS = ["ts", "tsx"];

export const PATTERNS = {
  "skippedTest": /\.skip\(|\bxit\(/g,
};

/**
 * Blank out everything that is NOT code — comments and string literals — before the patterns run.
 *
 * WHY THIS EXISTS. The patterns are deliberately plain regexes, and `: any` matches ordinary
 * English: "on purpose: any step can come back as skipped", "the ONLY boundary: any page throw",
 * "the same path as any other reference cell". Every one of those is a doc comment, and every one
 * counted as a cast. At the time this was added, 208 of the tree's 446 matches — 46.6% — came from
 * comments and strings, so the number was measuring prose about as much as it measured `any`.
 *
 * That is not cosmetic. A ratchet's whole value is that a rising number means new debt, and this
 * one rose when somebody WROTE A COMMENT. The baseline had been raised nine times, and the commit
 * messages say what was happening: "inherited, and not a cast at all", "inherited from main, not
 * from this goal", "stop a doc comment from counting as a cast". Four separate goals raised it
 * 425 -> 427 for the same drift they had not caused. Each raise made the next real regression
 * harder to see.
 *
 * CHARACTERS ARE REPLACED, NEVER REMOVED — spaces for content, newlines kept — so every offset
 * and line number in the blanked text still matches the original file. A future change that wants
 * to report the line a cast sits on gets that for free rather than having to re-derive it.
 *
 * TEMPLATE SUBSTITUTIONS STAY CODE. Inside a backtick string, `${...}` is executable, and a cast
 * can legitimately live there — `` `${(x as any).id}` `` is a real cast that must still count.
 * The scanner tracks brace depth inside a substitution so a nested object literal or a nested
 * template does not end it early.
 *
 * NOT HANDLED, deliberately: a regex literal containing `: any`. Distinguishing `/` division from
 * a regex needs real parsing, and guessing wrong would blank live code and HIDE a cast — a false
 * negative, which is the one failure mode a ratchet must never have. A regex containing `: any`
 * would still over-count, exactly as today; it is rare, and over-counting is the safe direction.
 */
/** Whether a match inside a string literal is a FALSE POSITIVE for this ratchet — see
 *  patternLivesInStrings in the generator. Comments are always stripped; strings are not. */
const STRIP_STRINGS = true;

export function stripNonCode(source) {
  let out = "";
  let i = 0;
  const n = source.length;
  // `code` | `line` | `block` | `sq` | `dq` | `tpl`
  let state = "code";
  // Open `${` substitutions, innermost last; each entry is that substitution's brace depth.
  const tplStack = [];
  let braceDepth = 0;

  const keep = (ch) => (ch === "\n" ? "\n" : " ");

  while (i < n) {
    const c = source[i];
    const d = source[i + 1];

    if (state === "code") {
      if (c === "/" && d === "/") { state = "line"; out += "  "; i += 2; continue; }
      if (c === "/" && d === "*") { state = "block"; out += "  "; i += 2; continue; }
      if (STRIP_STRINGS && c === "'") { state = "sq"; out += " "; i += 1; continue; }
      if (STRIP_STRINGS && c === '"') { state = "dq"; out += " "; i += 1; continue; }
      if (STRIP_STRINGS && c === "`") { state = "tpl"; out += " "; i += 1; continue; }
      // Track braces only while inside a template substitution, so `}` can close it.
      if (tplStack.length > 0) {
        if (c === "{") braceDepth += 1;
        else if (c === "}") {
          if (braceDepth === tplStack[tplStack.length - 1]) {
            braceDepth = tplStack.pop();
            state = "tpl";
            out += " ";
            i += 1;
            continue;
          }
          braceDepth -= 1;
        }
      }
      out += c;
      i += 1;
      continue;
    }

    if (state === "line") {
      if (c === "\n") { state = "code"; out += "\n"; } else out += " ";
      i += 1;
      continue;
    }

    if (state === "block") {
      if (c === "*" && d === "/") { state = "code"; out += "  "; i += 2; continue; }
      out += keep(c);
      i += 1;
      continue;
    }

    if (state === "sq" || state === "dq") {
      const quote = state === "sq" ? "'" : '"';
      if (c === "\\") { out += "  "; i += 2; continue; }
      if (c === quote) { state = "code"; out += " "; i += 1; continue; }
      out += keep(c);
      i += 1;
      continue;
    }

    // state === "tpl"
    if (c === "\\") { out += "  "; i += 2; continue; }
    if (c === "`") { state = "code"; out += " "; i += 1; continue; }
    if (c === "$" && d === "{") {
      // Re-enter code for the substitution; remember the depth that closes it.
      tplStack.push(braceDepth);
      state = "code";
      out += "  ";
      i += 2;
      continue;
    }
    out += keep(c);
    i += 1;
  }

  return out;
}

export function countInSource(source) {
  // Count against CODE only — see stripNonCode for why a plain match over raw text was measuring
  // English prose alongside real casts.
  const code = stripNonCode(source);
  const counts = {};
  for (const [name, re] of Object.entries(PATTERNS)) {
    counts[name] = (code.match(re) ?? []).length;
  }
  return counts;
}

function matchesExtension(file) {
  return EXTENSIONS.some((ext) => file.endsWith("." + ext));
}

function* walk(dir) {
  let entries;
  try {
    entries = readdirSync(dir);
  } catch {
    return;
  }
  for (const entry of entries) {
    if (entry === "node_modules" || entry.startsWith(".")) continue;
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) yield* walk(full);
    else if (matchesExtension(full)) yield full;
  }
}

export function countTree(root = SRC) {
  const totals = Object.fromEntries(Object.keys(PATTERNS).map((k) => [k, 0]));
  const perFile = [];
  for (const file of walk(root)) {
    const c = countInSource(readFileSync(file, "utf8"));
    for (const k of Object.keys(totals)) totals[k] += c[k];
    if (Object.values(c).some((n) => n > 0)) perFile.push({ file: relative(root, file), ...c });
  }
  return { totals, perFile };
}

export function compare(totals, baseline) {
  const failures = [];
  const improvements = [];
  for (const [k, max] of Object.entries(baseline)) {
    const n = totals[k] ?? 0;
    if (n > max) failures.push({ metric: k, actual: n, baseline: max });
    else if (n < max) improvements.push({ metric: k, actual: n, baseline: max });
  }
  return { failures, improvements };
}

function readBaseline() {
  try {
    return JSON.parse(readFileSync(BASELINE_PATH, "utf8"));
  } catch {
    return Object.fromEntries(Object.keys(PATTERNS).map((k) => [k, 0]));
  }
}

if (isMainModule()) {
  const { totals, perFile } = countTree();

  if (process.argv.includes("--update-baseline")) {
    writeFileSync(BASELINE_PATH, JSON.stringify(totals, null, 2) + "\n");
    console.log("skipped-tests" + "-ratchet: baseline updated to " + JSON.stringify(totals));
    process.exit(0);
  }

  const baseline = readBaseline();
  const { failures, improvements } = compare(totals, baseline);

  for (const k of Object.keys(baseline)) {
    console.log("skipped-tests" + "-ratchet: " + k + " = " + totals[k] + " (baseline " + baseline[k] + ")");
  }
  if (failures.length > 0) {
    for (const f of failures) {
      console.error("\n" + "skipped-tests" + "-ratchet: " + f.metric + " is " + f.actual + ", above the baseline of " + f.baseline + ".");
    }
    const top = [...perFile]
      .sort((a, b) => Object.keys(PATTERNS).reduce((s, k) => s + (b[k] ?? 0) - (a[k] ?? 0), 0))
      .slice(0, 8);
    if (top.length > 0) {
      console.error("Largest contributors:");
      for (const f of top) {
        const counts = Object.keys(PATTERNS).map((k) => (f[k] ?? 0) + " " + k).join(", ");
        console.error("  " + f.file + ": " + counts);
      }
    }
    console.error(
      "\nIf the increase is genuinely a one-off, raise the number in " + "skipped-tests.ratchet.json" +
        " in this PR and say why in the PR body (goal-pr-body.ts's ratchetRaise declaration).",
    );
    process.exit(1);
  }
  if (improvements.length > 0) {
    console.log(
      "\n" + "skipped-tests" + "-ratchet: counts dropped below the baseline — run with --update-baseline " +
        "to lower " + improvements.map((i) => i.metric + "=" + i.actual).join(", ") + " in this PR.",
    );
  }
}
```

**pm-agent.yaml snippet:**

```yaml
ratchets:
  - name: skipped-tests
    command: [node scripts/ci/ratchets/skipped-tests.mjs]
    description: "`.skip(` / `xit(` occurrences must not grow — a skipped test is a debt, not a pass."
    category: testing
```

## Unstructured logs (`unstructured-logs`)

`console.log` outside an explicit allowlist must not grow — use the repo's logger instead.

Category: `observability`

**Script** — save as `scripts/ci/ratchets/unstructured-logs.mjs`:

```javascript
/**
 * Unstructured logs ratchet — `node unstructured-logs.mjs`.
 *
 * `console.log` outside an explicit allowlist must not grow — use the repo's logger instead.
 *
 * Scaffolded by `ibuild engine ratchet add unstructured-logs` (Guides 11, G#2907) — generalized from
 * InteractorOSS/website's `scripts/style-ratchet.mjs`, the reference implementation this
 * shape is ported from. The baseline only ratchets DOWN: when a PR reduces a count, lower the
 * number in unstructured-logs.ratchet.json in the same PR. Raising it is a deliberate, reviewable decision —
 * never a side effect.
 *
 * Declare it in pm-agent.yaml:
 *   ratchets:
 *     - name: unstructured-logs
 *       command: [node unstructured-logs.mjs]
 *       description: "`console.log` outside an explicit allowlist must not grow — use the repo's logger instead."
 *       category: observability
 */
import { readdirSync, readFileSync, statSync, writeFileSync, realpathSync, existsSync } from "node:fs";
import { join, relative, dirname } from "node:path";
import { fileURLToPath } from "node:url";

/** Realpath-normalized self-exec check: `import.meta.url` and `process.argv[1]` can disagree on
 *  whether a directory a symlink resolves to (e.g. macOS's /var -> /private/var) is canonical, so a
 *  bare string comparison can read "not main" for the very process running this file. Falls back to
 *  the plain comparison if either path can't be resolved (never crashes the guard itself). */
function isMainModule() {
  if (!process.argv[1]) return false;
  const here = fileURLToPath(import.meta.url);
  try {
    return realpathSync(here) === realpathSync(process.argv[1]);
  } catch {
    return here === process.argv[1];
  }
}

/** Walk up from this script's own directory to find the repo root (a `.git` dir), so `srcDir`
 *  resolves correctly REGARDLESS of how deep this script is scaffolded (repo root, scripts/,
 *  scripts/ci/ratchets/, …). Falls back to the script's own directory if none is found (e.g. a
 *  repo checked out without .git) — the same directory the reference implementation assumed. */
function findRepoRoot(start) {
  let dir = start;
  for (let i = 0; i < 20; i++) {
    if (existsSync(join(dir, ".git"))) return dir;
    const parent = dirname(dir);
    if (parent === dir) break;
    dir = parent;
  }
  return start;
}

const HERE = dirname(fileURLToPath(import.meta.url));
const SRC = join(findRepoRoot(HERE), "apps/web/src");
const BASELINE_PATH = join(HERE, "unstructured-logs.ratchet.json");
const EXTENSIONS = ["ts", "tsx"];

export const PATTERNS = {
  "consoleLog": /console\.log\(/g,
};

/**
 * Blank out everything that is NOT code — comments and string literals — before the patterns run.
 *
 * WHY THIS EXISTS. The patterns are deliberately plain regexes, and `: any` matches ordinary
 * English: "on purpose: any step can come back as skipped", "the ONLY boundary: any page throw",
 * "the same path as any other reference cell". Every one of those is a doc comment, and every one
 * counted as a cast. At the time this was added, 208 of the tree's 446 matches — 46.6% — came from
 * comments and strings, so the number was measuring prose about as much as it measured `any`.
 *
 * That is not cosmetic. A ratchet's whole value is that a rising number means new debt, and this
 * one rose when somebody WROTE A COMMENT. The baseline had been raised nine times, and the commit
 * messages say what was happening: "inherited, and not a cast at all", "inherited from main, not
 * from this goal", "stop a doc comment from counting as a cast". Four separate goals raised it
 * 425 -> 427 for the same drift they had not caused. Each raise made the next real regression
 * harder to see.
 *
 * CHARACTERS ARE REPLACED, NEVER REMOVED — spaces for content, newlines kept — so every offset
 * and line number in the blanked text still matches the original file. A future change that wants
 * to report the line a cast sits on gets that for free rather than having to re-derive it.
 *
 * TEMPLATE SUBSTITUTIONS STAY CODE. Inside a backtick string, `${...}` is executable, and a cast
 * can legitimately live there — `` `${(x as any).id}` `` is a real cast that must still count.
 * The scanner tracks brace depth inside a substitution so a nested object literal or a nested
 * template does not end it early.
 *
 * NOT HANDLED, deliberately: a regex literal containing `: any`. Distinguishing `/` division from
 * a regex needs real parsing, and guessing wrong would blank live code and HIDE a cast — a false
 * negative, which is the one failure mode a ratchet must never have. A regex containing `: any`
 * would still over-count, exactly as today; it is rare, and over-counting is the safe direction.
 */
/** Whether a match inside a string literal is a FALSE POSITIVE for this ratchet — see
 *  patternLivesInStrings in the generator. Comments are always stripped; strings are not. */
const STRIP_STRINGS = true;

export function stripNonCode(source) {
  let out = "";
  let i = 0;
  const n = source.length;
  // `code` | `line` | `block` | `sq` | `dq` | `tpl`
  let state = "code";
  // Open `${` substitutions, innermost last; each entry is that substitution's brace depth.
  const tplStack = [];
  let braceDepth = 0;

  const keep = (ch) => (ch === "\n" ? "\n" : " ");

  while (i < n) {
    const c = source[i];
    const d = source[i + 1];

    if (state === "code") {
      if (c === "/" && d === "/") { state = "line"; out += "  "; i += 2; continue; }
      if (c === "/" && d === "*") { state = "block"; out += "  "; i += 2; continue; }
      if (STRIP_STRINGS && c === "'") { state = "sq"; out += " "; i += 1; continue; }
      if (STRIP_STRINGS && c === '"') { state = "dq"; out += " "; i += 1; continue; }
      if (STRIP_STRINGS && c === "`") { state = "tpl"; out += " "; i += 1; continue; }
      // Track braces only while inside a template substitution, so `}` can close it.
      if (tplStack.length > 0) {
        if (c === "{") braceDepth += 1;
        else if (c === "}") {
          if (braceDepth === tplStack[tplStack.length - 1]) {
            braceDepth = tplStack.pop();
            state = "tpl";
            out += " ";
            i += 1;
            continue;
          }
          braceDepth -= 1;
        }
      }
      out += c;
      i += 1;
      continue;
    }

    if (state === "line") {
      if (c === "\n") { state = "code"; out += "\n"; } else out += " ";
      i += 1;
      continue;
    }

    if (state === "block") {
      if (c === "*" && d === "/") { state = "code"; out += "  "; i += 2; continue; }
      out += keep(c);
      i += 1;
      continue;
    }

    if (state === "sq" || state === "dq") {
      const quote = state === "sq" ? "'" : '"';
      if (c === "\\") { out += "  "; i += 2; continue; }
      if (c === quote) { state = "code"; out += " "; i += 1; continue; }
      out += keep(c);
      i += 1;
      continue;
    }

    // state === "tpl"
    if (c === "\\") { out += "  "; i += 2; continue; }
    if (c === "`") { state = "code"; out += " "; i += 1; continue; }
    if (c === "$" && d === "{") {
      // Re-enter code for the substitution; remember the depth that closes it.
      tplStack.push(braceDepth);
      state = "code";
      out += "  ";
      i += 2;
      continue;
    }
    out += keep(c);
    i += 1;
  }

  return out;
}

export function countInSource(source) {
  // Count against CODE only — see stripNonCode for why a plain match over raw text was measuring
  // English prose alongside real casts.
  const code = stripNonCode(source);
  const counts = {};
  for (const [name, re] of Object.entries(PATTERNS)) {
    counts[name] = (code.match(re) ?? []).length;
  }
  return counts;
}

function matchesExtension(file) {
  return EXTENSIONS.some((ext) => file.endsWith("." + ext));
}

function* walk(dir) {
  let entries;
  try {
    entries = readdirSync(dir);
  } catch {
    return;
  }
  for (const entry of entries) {
    if (entry === "node_modules" || entry.startsWith(".")) continue;
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) yield* walk(full);
    else if (matchesExtension(full)) yield full;
  }
}

export function countTree(root = SRC) {
  const totals = Object.fromEntries(Object.keys(PATTERNS).map((k) => [k, 0]));
  const perFile = [];
  for (const file of walk(root)) {
    const c = countInSource(readFileSync(file, "utf8"));
    for (const k of Object.keys(totals)) totals[k] += c[k];
    if (Object.values(c).some((n) => n > 0)) perFile.push({ file: relative(root, file), ...c });
  }
  return { totals, perFile };
}

export function compare(totals, baseline) {
  const failures = [];
  const improvements = [];
  for (const [k, max] of Object.entries(baseline)) {
    const n = totals[k] ?? 0;
    if (n > max) failures.push({ metric: k, actual: n, baseline: max });
    else if (n < max) improvements.push({ metric: k, actual: n, baseline: max });
  }
  return { failures, improvements };
}

function readBaseline() {
  try {
    return JSON.parse(readFileSync(BASELINE_PATH, "utf8"));
  } catch {
    return Object.fromEntries(Object.keys(PATTERNS).map((k) => [k, 0]));
  }
}

if (isMainModule()) {
  const { totals, perFile } = countTree();

  if (process.argv.includes("--update-baseline")) {
    writeFileSync(BASELINE_PATH, JSON.stringify(totals, null, 2) + "\n");
    console.log("unstructured-logs" + "-ratchet: baseline updated to " + JSON.stringify(totals));
    process.exit(0);
  }

  const baseline = readBaseline();
  const { failures, improvements } = compare(totals, baseline);

  for (const k of Object.keys(baseline)) {
    console.log("unstructured-logs" + "-ratchet: " + k + " = " + totals[k] + " (baseline " + baseline[k] + ")");
  }
  if (failures.length > 0) {
    for (const f of failures) {
      console.error("\n" + "unstructured-logs" + "-ratchet: " + f.metric + " is " + f.actual + ", above the baseline of " + f.baseline + ".");
    }
    const top = [...perFile]
      .sort((a, b) => Object.keys(PATTERNS).reduce((s, k) => s + (b[k] ?? 0) - (a[k] ?? 0), 0))
      .slice(0, 8);
    if (top.length > 0) {
      console.error("Largest contributors:");
      for (const f of top) {
        const counts = Object.keys(PATTERNS).map((k) => (f[k] ?? 0) + " " + k).join(", ");
        console.error("  " + f.file + ": " + counts);
      }
    }
    console.error(
      "\nIf the increase is genuinely a one-off, raise the number in " + "unstructured-logs.ratchet.json" +
        " in this PR and say why in the PR body (goal-pr-body.ts's ratchetRaise declaration).",
    );
    process.exit(1);
  }
  if (improvements.length > 0) {
    console.log(
      "\n" + "unstructured-logs" + "-ratchet: counts dropped below the baseline — run with --update-baseline " +
        "to lower " + improvements.map((i) => i.metric + "=" + i.actual).join(", ") + " in this PR.",
    );
  }
}
```

**pm-agent.yaml snippet:**

```yaml
ratchets:
  - name: unstructured-logs
    command: [node scripts/ci/ratchets/unstructured-logs.mjs]
    description: "`console.log` outside an explicit allowlist must not grow — use the repo's logger instead."
    category: observability
```

## Inline styles (`inline-styles`)

JSX `style={{ }}` objects must not grow — use a design-system class or shared component instead.

Category: `design-system`

**Script** — save as `scripts/ci/ratchets/inline-styles.mjs`:

```javascript
/**
 * Inline styles ratchet — `node inline-styles.mjs`.
 *
 * JSX `style={{ }}` objects must not grow — use a design-system class or shared component instead.
 *
 * Scaffolded by `ibuild engine ratchet add inline-styles` (Guides 11, G#2907) — generalized from
 * InteractorOSS/website's `scripts/style-ratchet.mjs`, the reference implementation this
 * shape is ported from. The baseline only ratchets DOWN: when a PR reduces a count, lower the
 * number in inline-styles.ratchet.json in the same PR. Raising it is a deliberate, reviewable decision —
 * never a side effect.
 *
 * Declare it in pm-agent.yaml:
 *   ratchets:
 *     - name: inline-styles
 *       command: [node inline-styles.mjs]
 *       description: "JSX `style={{ }}` objects must not grow — use a design-system class or shared component instead."
 *       category: design-system
 */
import { readdirSync, readFileSync, statSync, writeFileSync, realpathSync, existsSync } from "node:fs";
import { join, relative, dirname } from "node:path";
import { fileURLToPath } from "node:url";

/** Realpath-normalized self-exec check: `import.meta.url` and `process.argv[1]` can disagree on
 *  whether a directory a symlink resolves to (e.g. macOS's /var -> /private/var) is canonical, so a
 *  bare string comparison can read "not main" for the very process running this file. Falls back to
 *  the plain comparison if either path can't be resolved (never crashes the guard itself). */
function isMainModule() {
  if (!process.argv[1]) return false;
  const here = fileURLToPath(import.meta.url);
  try {
    return realpathSync(here) === realpathSync(process.argv[1]);
  } catch {
    return here === process.argv[1];
  }
}

/** Walk up from this script's own directory to find the repo root (a `.git` dir), so `srcDir`
 *  resolves correctly REGARDLESS of how deep this script is scaffolded (repo root, scripts/,
 *  scripts/ci/ratchets/, …). Falls back to the script's own directory if none is found (e.g. a
 *  repo checked out without .git) — the same directory the reference implementation assumed. */
function findRepoRoot(start) {
  let dir = start;
  for (let i = 0; i < 20; i++) {
    if (existsSync(join(dir, ".git"))) return dir;
    const parent = dirname(dir);
    if (parent === dir) break;
    dir = parent;
  }
  return start;
}

const HERE = dirname(fileURLToPath(import.meta.url));
const SRC = join(findRepoRoot(HERE), "apps/web/src");
const BASELINE_PATH = join(HERE, "inline-styles.ratchet.json");
const EXTENSIONS = ["tsx"];

export const PATTERNS = {
  "inlineStyle": /style=\{\{/g,
};

/**
 * Blank out everything that is NOT code — comments and string literals — before the patterns run.
 *
 * WHY THIS EXISTS. The patterns are deliberately plain regexes, and `: any` matches ordinary
 * English: "on purpose: any step can come back as skipped", "the ONLY boundary: any page throw",
 * "the same path as any other reference cell". Every one of those is a doc comment, and every one
 * counted as a cast. At the time this was added, 208 of the tree's 446 matches — 46.6% — came from
 * comments and strings, so the number was measuring prose about as much as it measured `any`.
 *
 * That is not cosmetic. A ratchet's whole value is that a rising number means new debt, and this
 * one rose when somebody WROTE A COMMENT. The baseline had been raised nine times, and the commit
 * messages say what was happening: "inherited, and not a cast at all", "inherited from main, not
 * from this goal", "stop a doc comment from counting as a cast". Four separate goals raised it
 * 425 -> 427 for the same drift they had not caused. Each raise made the next real regression
 * harder to see.
 *
 * CHARACTERS ARE REPLACED, NEVER REMOVED — spaces for content, newlines kept — so every offset
 * and line number in the blanked text still matches the original file. A future change that wants
 * to report the line a cast sits on gets that for free rather than having to re-derive it.
 *
 * TEMPLATE SUBSTITUTIONS STAY CODE. Inside a backtick string, `${...}` is executable, and a cast
 * can legitimately live there — `` `${(x as any).id}` `` is a real cast that must still count.
 * The scanner tracks brace depth inside a substitution so a nested object literal or a nested
 * template does not end it early.
 *
 * NOT HANDLED, deliberately: a regex literal containing `: any`. Distinguishing `/` division from
 * a regex needs real parsing, and guessing wrong would blank live code and HIDE a cast — a false
 * negative, which is the one failure mode a ratchet must never have. A regex containing `: any`
 * would still over-count, exactly as today; it is rare, and over-counting is the safe direction.
 */
/** Whether a match inside a string literal is a FALSE POSITIVE for this ratchet — see
 *  patternLivesInStrings in the generator. Comments are always stripped; strings are not. */
const STRIP_STRINGS = true;

export function stripNonCode(source) {
  let out = "";
  let i = 0;
  const n = source.length;
  // `code` | `line` | `block` | `sq` | `dq` | `tpl`
  let state = "code";
  // Open `${` substitutions, innermost last; each entry is that substitution's brace depth.
  const tplStack = [];
  let braceDepth = 0;

  const keep = (ch) => (ch === "\n" ? "\n" : " ");

  while (i < n) {
    const c = source[i];
    const d = source[i + 1];

    if (state === "code") {
      if (c === "/" && d === "/") { state = "line"; out += "  "; i += 2; continue; }
      if (c === "/" && d === "*") { state = "block"; out += "  "; i += 2; continue; }
      if (STRIP_STRINGS && c === "'") { state = "sq"; out += " "; i += 1; continue; }
      if (STRIP_STRINGS && c === '"') { state = "dq"; out += " "; i += 1; continue; }
      if (STRIP_STRINGS && c === "`") { state = "tpl"; out += " "; i += 1; continue; }
      // Track braces only while inside a template substitution, so `}` can close it.
      if (tplStack.length > 0) {
        if (c === "{") braceDepth += 1;
        else if (c === "}") {
          if (braceDepth === tplStack[tplStack.length - 1]) {
            braceDepth = tplStack.pop();
            state = "tpl";
            out += " ";
            i += 1;
            continue;
          }
          braceDepth -= 1;
        }
      }
      out += c;
      i += 1;
      continue;
    }

    if (state === "line") {
      if (c === "\n") { state = "code"; out += "\n"; } else out += " ";
      i += 1;
      continue;
    }

    if (state === "block") {
      if (c === "*" && d === "/") { state = "code"; out += "  "; i += 2; continue; }
      out += keep(c);
      i += 1;
      continue;
    }

    if (state === "sq" || state === "dq") {
      const quote = state === "sq" ? "'" : '"';
      if (c === "\\") { out += "  "; i += 2; continue; }
      if (c === quote) { state = "code"; out += " "; i += 1; continue; }
      out += keep(c);
      i += 1;
      continue;
    }

    // state === "tpl"
    if (c === "\\") { out += "  "; i += 2; continue; }
    if (c === "`") { state = "code"; out += " "; i += 1; continue; }
    if (c === "$" && d === "{") {
      // Re-enter code for the substitution; remember the depth that closes it.
      tplStack.push(braceDepth);
      state = "code";
      out += "  ";
      i += 2;
      continue;
    }
    out += keep(c);
    i += 1;
  }

  return out;
}

export function countInSource(source) {
  // Count against CODE only — see stripNonCode for why a plain match over raw text was measuring
  // English prose alongside real casts.
  const code = stripNonCode(source);
  const counts = {};
  for (const [name, re] of Object.entries(PATTERNS)) {
    counts[name] = (code.match(re) ?? []).length;
  }
  return counts;
}

function matchesExtension(file) {
  return EXTENSIONS.some((ext) => file.endsWith("." + ext));
}

function* walk(dir) {
  let entries;
  try {
    entries = readdirSync(dir);
  } catch {
    return;
  }
  for (const entry of entries) {
    if (entry === "node_modules" || entry.startsWith(".")) continue;
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) yield* walk(full);
    else if (matchesExtension(full)) yield full;
  }
}

export function countTree(root = SRC) {
  const totals = Object.fromEntries(Object.keys(PATTERNS).map((k) => [k, 0]));
  const perFile = [];
  for (const file of walk(root)) {
    const c = countInSource(readFileSync(file, "utf8"));
    for (const k of Object.keys(totals)) totals[k] += c[k];
    if (Object.values(c).some((n) => n > 0)) perFile.push({ file: relative(root, file), ...c });
  }
  return { totals, perFile };
}

export function compare(totals, baseline) {
  const failures = [];
  const improvements = [];
  for (const [k, max] of Object.entries(baseline)) {
    const n = totals[k] ?? 0;
    if (n > max) failures.push({ metric: k, actual: n, baseline: max });
    else if (n < max) improvements.push({ metric: k, actual: n, baseline: max });
  }
  return { failures, improvements };
}

function readBaseline() {
  try {
    return JSON.parse(readFileSync(BASELINE_PATH, "utf8"));
  } catch {
    return Object.fromEntries(Object.keys(PATTERNS).map((k) => [k, 0]));
  }
}

if (isMainModule()) {
  const { totals, perFile } = countTree();

  if (process.argv.includes("--update-baseline")) {
    writeFileSync(BASELINE_PATH, JSON.stringify(totals, null, 2) + "\n");
    console.log("inline-styles" + "-ratchet: baseline updated to " + JSON.stringify(totals));
    process.exit(0);
  }

  const baseline = readBaseline();
  const { failures, improvements } = compare(totals, baseline);

  for (const k of Object.keys(baseline)) {
    console.log("inline-styles" + "-ratchet: " + k + " = " + totals[k] + " (baseline " + baseline[k] + ")");
  }
  if (failures.length > 0) {
    for (const f of failures) {
      console.error("\n" + "inline-styles" + "-ratchet: " + f.metric + " is " + f.actual + ", above the baseline of " + f.baseline + ".");
    }
    const top = [...perFile]
      .sort((a, b) => Object.keys(PATTERNS).reduce((s, k) => s + (b[k] ?? 0) - (a[k] ?? 0), 0))
      .slice(0, 8);
    if (top.length > 0) {
      console.error("Largest contributors:");
      for (const f of top) {
        const counts = Object.keys(PATTERNS).map((k) => (f[k] ?? 0) + " " + k).join(", ");
        console.error("  " + f.file + ": " + counts);
      }
    }
    console.error(
      "\nIf the increase is genuinely a one-off, raise the number in " + "inline-styles.ratchet.json" +
        " in this PR and say why in the PR body (goal-pr-body.ts's ratchetRaise declaration).",
    );
    process.exit(1);
  }
  if (improvements.length > 0) {
    console.log(
      "\n" + "inline-styles" + "-ratchet: counts dropped below the baseline — run with --update-baseline " +
        "to lower " + improvements.map((i) => i.metric + "=" + i.actual).join(", ") + " in this PR.",
    );
  }
}
```

**pm-agent.yaml snippet:**

```yaml
ratchets:
  - name: inline-styles
    command: [node scripts/ci/ratchets/inline-styles.mjs]
    description: "JSX `style={{ }}` objects must not grow — use a design-system class or shared component instead."
    category: design-system
```

## Hard-coded colors (`hardcoded-colors`)

Hex color literals outside token files must not grow — use a design-token instead.

Category: `design-system`

**Script** — save as `scripts/ci/ratchets/hardcoded-colors.mjs`:

```javascript
/**
 * Hard-coded colors ratchet — `node hardcoded-colors.mjs`.
 *
 * Hex color literals outside token files must not grow — use a design-token instead.
 *
 * Scaffolded by `ibuild engine ratchet add hardcoded-colors` (Guides 11, G#2907) — generalized from
 * InteractorOSS/website's `scripts/style-ratchet.mjs`, the reference implementation this
 * shape is ported from. The baseline only ratchets DOWN: when a PR reduces a count, lower the
 * number in hardcoded-colors.ratchet.json in the same PR. Raising it is a deliberate, reviewable decision —
 * never a side effect.
 *
 * Declare it in pm-agent.yaml:
 *   ratchets:
 *     - name: hardcoded-colors
 *       command: [node hardcoded-colors.mjs]
 *       description: "Hex color literals outside token files must not grow — use a design-token instead."
 *       category: design-system
 */
import { readdirSync, readFileSync, statSync, writeFileSync, realpathSync, existsSync } from "node:fs";
import { join, relative, dirname } from "node:path";
import { fileURLToPath } from "node:url";

/** Realpath-normalized self-exec check: `import.meta.url` and `process.argv[1]` can disagree on
 *  whether a directory a symlink resolves to (e.g. macOS's /var -> /private/var) is canonical, so a
 *  bare string comparison can read "not main" for the very process running this file. Falls back to
 *  the plain comparison if either path can't be resolved (never crashes the guard itself). */
function isMainModule() {
  if (!process.argv[1]) return false;
  const here = fileURLToPath(import.meta.url);
  try {
    return realpathSync(here) === realpathSync(process.argv[1]);
  } catch {
    return here === process.argv[1];
  }
}

/** Walk up from this script's own directory to find the repo root (a `.git` dir), so `srcDir`
 *  resolves correctly REGARDLESS of how deep this script is scaffolded (repo root, scripts/,
 *  scripts/ci/ratchets/, …). Falls back to the script's own directory if none is found (e.g. a
 *  repo checked out without .git) — the same directory the reference implementation assumed. */
function findRepoRoot(start) {
  let dir = start;
  for (let i = 0; i < 20; i++) {
    if (existsSync(join(dir, ".git"))) return dir;
    const parent = dirname(dir);
    if (parent === dir) break;
    dir = parent;
  }
  return start;
}

const HERE = dirname(fileURLToPath(import.meta.url));
const SRC = join(findRepoRoot(HERE), "apps/web/src");
const BASELINE_PATH = join(HERE, "hardcoded-colors.ratchet.json");
const EXTENSIONS = ["tsx"];

export const PATTERNS = {
  "hardcodedColor": /#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3}(?:[0-9a-fA-F]{2})?)?\b/g,
};

/**
 * Blank out everything that is NOT code — comments and string literals — before the patterns run.
 *
 * WHY THIS EXISTS. The patterns are deliberately plain regexes, and `: any` matches ordinary
 * English: "on purpose: any step can come back as skipped", "the ONLY boundary: any page throw",
 * "the same path as any other reference cell". Every one of those is a doc comment, and every one
 * counted as a cast. At the time this was added, 208 of the tree's 446 matches — 46.6% — came from
 * comments and strings, so the number was measuring prose about as much as it measured `any`.
 *
 * That is not cosmetic. A ratchet's whole value is that a rising number means new debt, and this
 * one rose when somebody WROTE A COMMENT. The baseline had been raised nine times, and the commit
 * messages say what was happening: "inherited, and not a cast at all", "inherited from main, not
 * from this goal", "stop a doc comment from counting as a cast". Four separate goals raised it
 * 425 -> 427 for the same drift they had not caused. Each raise made the next real regression
 * harder to see.
 *
 * CHARACTERS ARE REPLACED, NEVER REMOVED — spaces for content, newlines kept — so every offset
 * and line number in the blanked text still matches the original file. A future change that wants
 * to report the line a cast sits on gets that for free rather than having to re-derive it.
 *
 * TEMPLATE SUBSTITUTIONS STAY CODE. Inside a backtick string, `${...}` is executable, and a cast
 * can legitimately live there — `` `${(x as any).id}` `` is a real cast that must still count.
 * The scanner tracks brace depth inside a substitution so a nested object literal or a nested
 * template does not end it early.
 *
 * NOT HANDLED, deliberately: a regex literal containing `: any`. Distinguishing `/` division from
 * a regex needs real parsing, and guessing wrong would blank live code and HIDE a cast — a false
 * negative, which is the one failure mode a ratchet must never have. A regex containing `: any`
 * would still over-count, exactly as today; it is rare, and over-counting is the safe direction.
 */
/** Whether a match inside a string literal is a FALSE POSITIVE for this ratchet — see
 *  patternLivesInStrings in the generator. Comments are always stripped; strings are not. */
const STRIP_STRINGS = false;

export function stripNonCode(source) {
  let out = "";
  let i = 0;
  const n = source.length;
  // `code` | `line` | `block` | `sq` | `dq` | `tpl`
  let state = "code";
  // Open `${` substitutions, innermost last; each entry is that substitution's brace depth.
  const tplStack = [];
  let braceDepth = 0;

  const keep = (ch) => (ch === "\n" ? "\n" : " ");

  while (i < n) {
    const c = source[i];
    const d = source[i + 1];

    if (state === "code") {
      if (c === "/" && d === "/") { state = "line"; out += "  "; i += 2; continue; }
      if (c === "/" && d === "*") { state = "block"; out += "  "; i += 2; continue; }
      if (STRIP_STRINGS && c === "'") { state = "sq"; out += " "; i += 1; continue; }
      if (STRIP_STRINGS && c === '"') { state = "dq"; out += " "; i += 1; continue; }
      if (STRIP_STRINGS && c === "`") { state = "tpl"; out += " "; i += 1; continue; }
      // Track braces only while inside a template substitution, so `}` can close it.
      if (tplStack.length > 0) {
        if (c === "{") braceDepth += 1;
        else if (c === "}") {
          if (braceDepth === tplStack[tplStack.length - 1]) {
            braceDepth = tplStack.pop();
            state = "tpl";
            out += " ";
            i += 1;
            continue;
          }
          braceDepth -= 1;
        }
      }
      out += c;
      i += 1;
      continue;
    }

    if (state === "line") {
      if (c === "\n") { state = "code"; out += "\n"; } else out += " ";
      i += 1;
      continue;
    }

    if (state === "block") {
      if (c === "*" && d === "/") { state = "code"; out += "  "; i += 2; continue; }
      out += keep(c);
      i += 1;
      continue;
    }

    if (state === "sq" || state === "dq") {
      const quote = state === "sq" ? "'" : '"';
      if (c === "\\") { out += "  "; i += 2; continue; }
      if (c === quote) { state = "code"; out += " "; i += 1; continue; }
      out += keep(c);
      i += 1;
      continue;
    }

    // state === "tpl"
    if (c === "\\") { out += "  "; i += 2; continue; }
    if (c === "`") { state = "code"; out += " "; i += 1; continue; }
    if (c === "$" && d === "{") {
      // Re-enter code for the substitution; remember the depth that closes it.
      tplStack.push(braceDepth);
      state = "code";
      out += "  ";
      i += 2;
      continue;
    }
    out += keep(c);
    i += 1;
  }

  return out;
}

export function countInSource(source) {
  // Count against CODE only — see stripNonCode for why a plain match over raw text was measuring
  // English prose alongside real casts.
  const code = stripNonCode(source);
  const counts = {};
  for (const [name, re] of Object.entries(PATTERNS)) {
    counts[name] = (code.match(re) ?? []).length;
  }
  return counts;
}

function matchesExtension(file) {
  return EXTENSIONS.some((ext) => file.endsWith("." + ext));
}

function* walk(dir) {
  let entries;
  try {
    entries = readdirSync(dir);
  } catch {
    return;
  }
  for (const entry of entries) {
    if (entry === "node_modules" || entry.startsWith(".")) continue;
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) yield* walk(full);
    else if (matchesExtension(full)) yield full;
  }
}

export function countTree(root = SRC) {
  const totals = Object.fromEntries(Object.keys(PATTERNS).map((k) => [k, 0]));
  const perFile = [];
  for (const file of walk(root)) {
    const c = countInSource(readFileSync(file, "utf8"));
    for (const k of Object.keys(totals)) totals[k] += c[k];
    if (Object.values(c).some((n) => n > 0)) perFile.push({ file: relative(root, file), ...c });
  }
  return { totals, perFile };
}

export function compare(totals, baseline) {
  const failures = [];
  const improvements = [];
  for (const [k, max] of Object.entries(baseline)) {
    const n = totals[k] ?? 0;
    if (n > max) failures.push({ metric: k, actual: n, baseline: max });
    else if (n < max) improvements.push({ metric: k, actual: n, baseline: max });
  }
  return { failures, improvements };
}

function readBaseline() {
  try {
    return JSON.parse(readFileSync(BASELINE_PATH, "utf8"));
  } catch {
    return Object.fromEntries(Object.keys(PATTERNS).map((k) => [k, 0]));
  }
}

if (isMainModule()) {
  const { totals, perFile } = countTree();

  if (process.argv.includes("--update-baseline")) {
    writeFileSync(BASELINE_PATH, JSON.stringify(totals, null, 2) + "\n");
    console.log("hardcoded-colors" + "-ratchet: baseline updated to " + JSON.stringify(totals));
    process.exit(0);
  }

  const baseline = readBaseline();
  const { failures, improvements } = compare(totals, baseline);

  for (const k of Object.keys(baseline)) {
    console.log("hardcoded-colors" + "-ratchet: " + k + " = " + totals[k] + " (baseline " + baseline[k] + ")");
  }
  if (failures.length > 0) {
    for (const f of failures) {
      console.error("\n" + "hardcoded-colors" + "-ratchet: " + f.metric + " is " + f.actual + ", above the baseline of " + f.baseline + ".");
    }
    const top = [...perFile]
      .sort((a, b) => Object.keys(PATTERNS).reduce((s, k) => s + (b[k] ?? 0) - (a[k] ?? 0), 0))
      .slice(0, 8);
    if (top.length > 0) {
      console.error("Largest contributors:");
      for (const f of top) {
        const counts = Object.keys(PATTERNS).map((k) => (f[k] ?? 0) + " " + k).join(", ");
        console.error("  " + f.file + ": " + counts);
      }
    }
    console.error(
      "\nIf the increase is genuinely a one-off, raise the number in " + "hardcoded-colors.ratchet.json" +
        " in this PR and say why in the PR body (goal-pr-body.ts's ratchetRaise declaration).",
    );
    process.exit(1);
  }
  if (improvements.length > 0) {
    console.log(
      "\n" + "hardcoded-colors" + "-ratchet: counts dropped below the baseline — run with --update-baseline " +
        "to lower " + improvements.map((i) => i.metric + "=" + i.actual).join(", ") + " in this PR.",
    );
  }
}
```

**pm-agent.yaml snippet:**

```yaml
ratchets:
  - name: hardcoded-colors
    command: [node scripts/ci/ratchets/hardcoded-colors.mjs]
    description: "Hex color literals outside token files must not grow — use a design-token instead."
    category: design-system
```

## Raw HTML tags with a component available (`raw-tags-where-component-exists`)

Raw tags that have a design-system component (button, input, …) must not grow.

Category: `design-system`

**Script** — save as `scripts/ci/ratchets/raw-tags-where-component-exists.mjs`:

```javascript
/**
 * Raw HTML tags with a component available ratchet — `node raw-tags-where-component-exists.mjs`.
 *
 * Raw tags that have a design-system component (button, input, …) must not grow.
 *
 * Scaffolded by `ibuild engine ratchet add raw-tags-where-component-exists` (Guides 11, G#2907) — generalized from
 * InteractorOSS/website's `scripts/style-ratchet.mjs`, the reference implementation this
 * shape is ported from. The baseline only ratchets DOWN: when a PR reduces a count, lower the
 * number in raw-tags-where-component-exists.ratchet.json in the same PR. Raising it is a deliberate, reviewable decision —
 * never a side effect.
 *
 * Declare it in pm-agent.yaml:
 *   ratchets:
 *     - name: raw-tags-where-component-exists
 *       command: [node raw-tags-where-component-exists.mjs]
 *       description: "Raw tags that have a design-system component (button, input, …) must not grow."
 *       category: design-system
 */
import { readdirSync, readFileSync, statSync, writeFileSync, realpathSync, existsSync } from "node:fs";
import { join, relative, dirname } from "node:path";
import { fileURLToPath } from "node:url";

/** Realpath-normalized self-exec check: `import.meta.url` and `process.argv[1]` can disagree on
 *  whether a directory a symlink resolves to (e.g. macOS's /var -> /private/var) is canonical, so a
 *  bare string comparison can read "not main" for the very process running this file. Falls back to
 *  the plain comparison if either path can't be resolved (never crashes the guard itself). */
function isMainModule() {
  if (!process.argv[1]) return false;
  const here = fileURLToPath(import.meta.url);
  try {
    return realpathSync(here) === realpathSync(process.argv[1]);
  } catch {
    return here === process.argv[1];
  }
}

/** Walk up from this script's own directory to find the repo root (a `.git` dir), so `srcDir`
 *  resolves correctly REGARDLESS of how deep this script is scaffolded (repo root, scripts/,
 *  scripts/ci/ratchets/, …). Falls back to the script's own directory if none is found (e.g. a
 *  repo checked out without .git) — the same directory the reference implementation assumed. */
function findRepoRoot(start) {
  let dir = start;
  for (let i = 0; i < 20; i++) {
    if (existsSync(join(dir, ".git"))) return dir;
    const parent = dirname(dir);
    if (parent === dir) break;
    dir = parent;
  }
  return start;
}

const HERE = dirname(fileURLToPath(import.meta.url));
const SRC = join(findRepoRoot(HERE), "apps/web/src");
const BASELINE_PATH = join(HERE, "raw-tags-where-component-exists.ratchet.json");
const EXTENSIONS = ["tsx"];

export const PATTERNS = {
  "raw_button": /<button\b/g,
  "raw_input": /<input\b/g,
  "raw_select": /<select\b/g,
  "raw_textarea": /<textarea\b/g,
};

/**
 * Blank out everything that is NOT code — comments and string literals — before the patterns run.
 *
 * WHY THIS EXISTS. The patterns are deliberately plain regexes, and `: any` matches ordinary
 * English: "on purpose: any step can come back as skipped", "the ONLY boundary: any page throw",
 * "the same path as any other reference cell". Every one of those is a doc comment, and every one
 * counted as a cast. At the time this was added, 208 of the tree's 446 matches — 46.6% — came from
 * comments and strings, so the number was measuring prose about as much as it measured `any`.
 *
 * That is not cosmetic. A ratchet's whole value is that a rising number means new debt, and this
 * one rose when somebody WROTE A COMMENT. The baseline had been raised nine times, and the commit
 * messages say what was happening: "inherited, and not a cast at all", "inherited from main, not
 * from this goal", "stop a doc comment from counting as a cast". Four separate goals raised it
 * 425 -> 427 for the same drift they had not caused. Each raise made the next real regression
 * harder to see.
 *
 * CHARACTERS ARE REPLACED, NEVER REMOVED — spaces for content, newlines kept — so every offset
 * and line number in the blanked text still matches the original file. A future change that wants
 * to report the line a cast sits on gets that for free rather than having to re-derive it.
 *
 * TEMPLATE SUBSTITUTIONS STAY CODE. Inside a backtick string, `${...}` is executable, and a cast
 * can legitimately live there — `` `${(x as any).id}` `` is a real cast that must still count.
 * The scanner tracks brace depth inside a substitution so a nested object literal or a nested
 * template does not end it early.
 *
 * NOT HANDLED, deliberately: a regex literal containing `: any`. Distinguishing `/` division from
 * a regex needs real parsing, and guessing wrong would blank live code and HIDE a cast — a false
 * negative, which is the one failure mode a ratchet must never have. A regex containing `: any`
 * would still over-count, exactly as today; it is rare, and over-counting is the safe direction.
 */
/** Whether a match inside a string literal is a FALSE POSITIVE for this ratchet — see
 *  patternLivesInStrings in the generator. Comments are always stripped; strings are not. */
const STRIP_STRINGS = true;

export function stripNonCode(source) {
  let out = "";
  let i = 0;
  const n = source.length;
  // `code` | `line` | `block` | `sq` | `dq` | `tpl`
  let state = "code";
  // Open `${` substitutions, innermost last; each entry is that substitution's brace depth.
  const tplStack = [];
  let braceDepth = 0;

  const keep = (ch) => (ch === "\n" ? "\n" : " ");

  while (i < n) {
    const c = source[i];
    const d = source[i + 1];

    if (state === "code") {
      if (c === "/" && d === "/") { state = "line"; out += "  "; i += 2; continue; }
      if (c === "/" && d === "*") { state = "block"; out += "  "; i += 2; continue; }
      if (STRIP_STRINGS && c === "'") { state = "sq"; out += " "; i += 1; continue; }
      if (STRIP_STRINGS && c === '"') { state = "dq"; out += " "; i += 1; continue; }
      if (STRIP_STRINGS && c === "`") { state = "tpl"; out += " "; i += 1; continue; }
      // Track braces only while inside a template substitution, so `}` can close it.
      if (tplStack.length > 0) {
        if (c === "{") braceDepth += 1;
        else if (c === "}") {
          if (braceDepth === tplStack[tplStack.length - 1]) {
            braceDepth = tplStack.pop();
            state = "tpl";
            out += " ";
            i += 1;
            continue;
          }
          braceDepth -= 1;
        }
      }
      out += c;
      i += 1;
      continue;
    }

    if (state === "line") {
      if (c === "\n") { state = "code"; out += "\n"; } else out += " ";
      i += 1;
      continue;
    }

    if (state === "block") {
      if (c === "*" && d === "/") { state = "code"; out += "  "; i += 2; continue; }
      out += keep(c);
      i += 1;
      continue;
    }

    if (state === "sq" || state === "dq") {
      const quote = state === "sq" ? "'" : '"';
      if (c === "\\") { out += "  "; i += 2; continue; }
      if (c === quote) { state = "code"; out += " "; i += 1; continue; }
      out += keep(c);
      i += 1;
      continue;
    }

    // state === "tpl"
    if (c === "\\") { out += "  "; i += 2; continue; }
    if (c === "`") { state = "code"; out += " "; i += 1; continue; }
    if (c === "$" && d === "{") {
      // Re-enter code for the substitution; remember the depth that closes it.
      tplStack.push(braceDepth);
      state = "code";
      out += "  ";
      i += 2;
      continue;
    }
    out += keep(c);
    i += 1;
  }

  return out;
}

export function countInSource(source) {
  // Count against CODE only — see stripNonCode for why a plain match over raw text was measuring
  // English prose alongside real casts.
  const code = stripNonCode(source);
  const counts = {};
  for (const [name, re] of Object.entries(PATTERNS)) {
    counts[name] = (code.match(re) ?? []).length;
  }
  return counts;
}

function matchesExtension(file) {
  return EXTENSIONS.some((ext) => file.endsWith("." + ext));
}

function* walk(dir) {
  let entries;
  try {
    entries = readdirSync(dir);
  } catch {
    return;
  }
  for (const entry of entries) {
    if (entry === "node_modules" || entry.startsWith(".")) continue;
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) yield* walk(full);
    else if (matchesExtension(full)) yield full;
  }
}

export function countTree(root = SRC) {
  const totals = Object.fromEntries(Object.keys(PATTERNS).map((k) => [k, 0]));
  const perFile = [];
  for (const file of walk(root)) {
    const c = countInSource(readFileSync(file, "utf8"));
    for (const k of Object.keys(totals)) totals[k] += c[k];
    if (Object.values(c).some((n) => n > 0)) perFile.push({ file: relative(root, file), ...c });
  }
  return { totals, perFile };
}

export function compare(totals, baseline) {
  const failures = [];
  const improvements = [];
  for (const [k, max] of Object.entries(baseline)) {
    const n = totals[k] ?? 0;
    if (n > max) failures.push({ metric: k, actual: n, baseline: max });
    else if (n < max) improvements.push({ metric: k, actual: n, baseline: max });
  }
  return { failures, improvements };
}

function readBaseline() {
  try {
    return JSON.parse(readFileSync(BASELINE_PATH, "utf8"));
  } catch {
    return Object.fromEntries(Object.keys(PATTERNS).map((k) => [k, 0]));
  }
}

if (isMainModule()) {
  const { totals, perFile } = countTree();

  if (process.argv.includes("--update-baseline")) {
    writeFileSync(BASELINE_PATH, JSON.stringify(totals, null, 2) + "\n");
    console.log("raw-tags-where-component-exists" + "-ratchet: baseline updated to " + JSON.stringify(totals));
    process.exit(0);
  }

  const baseline = readBaseline();
  const { failures, improvements } = compare(totals, baseline);

  for (const k of Object.keys(baseline)) {
    console.log("raw-tags-where-component-exists" + "-ratchet: " + k + " = " + totals[k] + " (baseline " + baseline[k] + ")");
  }
  if (failures.length > 0) {
    for (const f of failures) {
      console.error("\n" + "raw-tags-where-component-exists" + "-ratchet: " + f.metric + " is " + f.actual + ", above the baseline of " + f.baseline + ".");
    }
    const top = [...perFile]
      .sort((a, b) => Object.keys(PATTERNS).reduce((s, k) => s + (b[k] ?? 0) - (a[k] ?? 0), 0))
      .slice(0, 8);
    if (top.length > 0) {
      console.error("Largest contributors:");
      for (const f of top) {
        const counts = Object.keys(PATTERNS).map((k) => (f[k] ?? 0) + " " + k).join(", ");
        console.error("  " + f.file + ": " + counts);
      }
    }
    console.error(
      "\nIf the increase is genuinely a one-off, raise the number in " + "raw-tags-where-component-exists.ratchet.json" +
        " in this PR and say why in the PR body (goal-pr-body.ts's ratchetRaise declaration).",
    );
    process.exit(1);
  }
  if (improvements.length > 0) {
    console.log(
      "\n" + "raw-tags-where-component-exists" + "-ratchet: counts dropped below the baseline — run with --update-baseline " +
        "to lower " + improvements.map((i) => i.metric + "=" + i.actual).join(", ") + " in this PR.",
    );
  }
}
```

**pm-agent.yaml snippet:**

```yaml
ratchets:
  - name: raw-tags-where-component-exists
    command: [node scripts/ci/ratchets/raw-tags-where-component-exists.mjs]
    description: "Raw tags that have a design-system component (button, input, …) must not grow."
    category: design-system
```
