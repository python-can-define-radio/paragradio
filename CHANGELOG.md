# Changelog

Starting with versions after `v2025_03`, we will note changes here.

The format is roughly based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to the `year.month` version scheme documented in the README.

## [Unreleased]

### Changed

- Commands to parallel GNU Radio process are now sent synchronously. For version 2025.03 and earlier, the commands were put into a queue which the parallel GNU Radio process consumed with a 1 millisecond delay (approx) between commands. The new approach may cause timing changes if you do very frequent adjustments to your flowgraph. Further discussion [here](https://github.com/python-can-define-radio/paragradio/issues/1).
- Many of the errors that GNU Radio produces will now be visible when calling the `.config` method. Before, the errors were usually silenced.

### Other notes

james-pcdr; 2025-05-23: I realize that the history is sparse before this point. Now that we've decided that this project is useful enough to continue using, I'm going to keep better changelog notes.

## [2025.03.2] - 2025-02-05

### Changed

- Better handling of setting `running` to `True` or `False`.
