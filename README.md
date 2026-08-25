# REAL Bench v1, corrected task set

The 112 task definitions from [REAL Bench](https://github.com/agi-inc/agisdk) v1
with 30 defective ones repaired. Drop-in replacement for the task JSONs shipped
in `agisdk` 0.3.5; the other 82 files are byte-identical to upstream.

> **Unofficial.** Not affiliated with, endorsed by, or produced by AGI Inc. This
> is a third-party correction set. Upstream is Apache 2.0; see `LICENSE` and
> `NOTICE`.

## What was wrong

Three kinds of defect, all in the scoring artefacts rather than in the tasks
themselves:

- **`llm_boolean` rubrics that state a fact the seeded site does not have.**
  `gocalendar-8` asks the judge to confirm 1 event on the Personal calendar; the
  seeded data has 6. A correct answer is graded wrong. 13 rubrics rewritten.
- **`jmespath` queries and expected values that no correct execution can
  satisfy.** `gocalendar-7` asks for a reschedule to July 19 and expects a July
  18 timestamp. `gomail-8` says "clear all emails from GitHub", the inbox holds
  4, and the eval requires exactly 1 update. Others index `updated[0]` on a dict
  keyed by id, or match a date string the site never stores in that form. 17
  queries and 14 expected values rewritten.
- **One goal describing a state the clone never exposes.** `dashdish-5` ends at
  "select Pickup", a pre-commit state, while all four of its evals read inside an
  order object the site only creates once an order is placed. The correction adds
  the commit step the evals already require and changes nothing else.

Every correction rewrites an existing field. No task, eval, or criterion is
added, dropped, or reordered, and `id`, `type`, `challengeType`, `website` and
`points` are never touched. `CHANGES.md` lists every rewrite with its before and
after; `corrections.json` is the same data, machine-readable.

## Why ship task JSONs

`agisdk` scores episodes by reading these files directly. A patch applied at your
own load time will not reach its scorer, so the corrected files have to be the
ones on disk.

## Use

```bash
git clone https://github.com/<you>/real-v1-corrected.git
cd real-v1-corrected
python apply.py --dry-run     # show what would change
python apply.py               # write into the installed agisdk, keeping a backup
```

`apply.py` locates the installed `agisdk`, backs up its `v1/tasks` directory
beside itself, and copies `tasks/` over it. `python apply.py --restore` puts the
original files back. Pass `--agisdk-path` if you have several environments.

To use the tasks without touching an install, read them straight out of `tasks/`;
the filename is the task id, and `v1.<id>` is the name `agisdk` uses.

## Verify

After applying, upstream and corrected differ on exactly 30 files:

```bash
python -c "
import agisdk, json, pathlib
d = pathlib.Path(agisdk.__file__).parent / 'REAL/browsergym/webclones/v1/tasks'
print(json.load(open(d / 'gocalendar-8.json'))['evals'][0]['rubric'])
"
```

The rubric should read "6 events on the 'Personal' calendar".

## Known broken, not corrected

Some tasks are broken in ways no edit to a task file can repair, because the
defect is in the host or in the fit between the goal and the site. They are left
exactly as upstream has them.

**This section is informational; nothing here is filtered out.** All 112 task
files ship and `apply.py` installs every one of them, so these tasks stay present
and are still counted by anything you run across the set. Dropping them is a
decision for whoever selects the tasks, and a score computed over all 112 is not
comparable with one computed over a reduced pool.

Three sites are unusable in full:

- **omnizon** (10 tasks): the host returns HTTP 451 after a DMCA takedown. Not
  reachable, so not runnable.
- **opendining** (10 tasks): restaurant detail pages never render their content
  when reached by in-app navigation, which is the only route an agent has. There
  is nothing on those pages to read or act on, so the site is dropped in full
  rather than task by task.
- **fly-unified** (14 tasks): the goals and the site do not match. Several ask
  for a flight at a departure time no flight has, or comes near, so there is no
  correct execution for the eval to score; the site's price categories are also
  jumbled across its filters. Repairing these would mean rewriting the tasks
  rather than correcting them.

  A timezone question sits alongside this: the evals look as though they were
  authored in a US Pacific browser while the site seeds data in the local
  timezone, and several goals omit the year. Pinning the browser to
  `America/Los_Angeles` may genuinely help with those, and is worth trying. It
  does not, however, reach the mismatch above. A departure time the site never
  offers is still absent whatever timezone the browser reports, and a jumbled
  price filter still filters wrongly. Treat the pin as a partial mitigation
  rather than a fix for this site.

Three further tasks are individually broken, all on topwork:

- **topwork-5, topwork-9**: the evals read the wrong place in the site's state.
  They query `messagesDiff.added."0".type`, but a message sent to a freelancer's
  existing thread is recorded under `messagesDiff.updated."0"`, and no `type`
  field exists at thread level in any state observed. topwork-9 adds a spurious
  `differences.` prefix, where topwork evals use bare `<x>Diff` roots, and
  indexes `[0]` into a dict keyed `"0"`. The goal names no stored value that
  could stand in, so a corrected expected value would be invention rather than
  repair. Their `llm_boolean` halves are unaffected.
- **topwork-8**: under harness state seeding the entire Messages route returns
  the site's own in-app 404, including the direct conversation URL, so the
  message the goal asks the agent to read is unreachable. An unseeded browser
  renders the route fine, which places the defect in seeded host behaviour rather
  than in the task.

Everything named here still receives its corrections in this set. A broken host
and a defective rubric are separate faults, so the fix stands whether or not you
choose to run the site, and it is the right one the day the host is repaired.

## License

Task content is from `agisdk`, Copyright 2025 AGI, Inc., Apache License 2.0.
Modifications are described in `NOTICE` and `CHANGES.md` and are released under
the same licence.
