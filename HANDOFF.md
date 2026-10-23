# Project Handoff

## Project

- Repository: `/Users/qiaoyawu/Desktop/qiaoyawu.github.io`
- GitHub remote: `https://github.com/QiaoyaWu/qiaoyawu.github.io.git`
- Main branch: `master`
- Site: `https://qiaoyawu.github.io`

## Recent website work

- Added CV navigation and PDF preview page.
- Added Life section with Nova photo gallery and Travel map.
- Travel map loads editable data from `travelmap/visited-countries.csv`.
- Added research-page section dividers and figure layouts.
- Added the AGN photoionization/self-shadowing research update and figures.
- Latest content update pushed in commit `dbc69d9`.

## Repository cleanup

- Removed unused Academic Pages demo pages and empty collections: `_posts/`, `_portfolio/`, `_teaching/`, `_talks/`, and `_publications_old/`.
- Removed unused archive pages, Talks tools, old blog archive, and deployment/template files.
- Removed tracked `.DS_Store` files and added `.DS_Store` to `.gitignore`.
- Kept `talkmap/leaflet_dist/` because the Travel map still uses its Leaflet assets.
- Cleanup commit: `3cb0e29` on branch `codex/cleanup-unused-files`.
- Pull Request: https://github.com/QiaoyaWu/qiaoyawu.github.io/pull/1
- The cleanup branch was pushed to GitHub; merge status should be checked on the Pull Request.

## Validation note

- Static reference checks and `git diff --check` passed.
- Local Jekyll build was not completed because the environment could not provide a working `jekyll` executable.
