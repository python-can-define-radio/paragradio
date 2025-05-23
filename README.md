# paragradio
    
paragradio (Parallel GNU Radio) module.
    
Note that much of the functionality also depends on GNU Radio. However, `gnuradio` is not listed in the dependencies as it is not pip-installable (as far as the authors know).

Most of the flowgraphs also use PyQt5, which you likely have if you have gnuradio.
    
### Example usage

Example for version 2025.03:

```python3
from paragradio.v2025_03 import SpecAnSim

SpecAnSim.config(running=True)
```

### Documentation

We haven't yet written documentation other than the lessons in our [sdr-course](https://github.com/python-can-define-radio/sdr-course/). We recommend starting with the [Spectrum Analyzer lesson](https://github.com/python-can-define-radio/sdr-course/blob/main/classroom_activities/Ch01_Diving_in_Headfirst/020_Spec_A_paragradio.md).

### Version / breaking changes policy

Versions are marked by year and month. We will adhere to the following policy:
    
- Before the version's month and year, that version is unstable, and changes will be made freely.
- Once that version's month and year arrive, that version is stable, and only non-breaking changes will be made.

Examples:

| Version  | Unstable              | Stable                 |
|----------|-----------------------|------------------------|
| v2025_02 | Before Feb 1, 2025    | Starting Feb 1, 2025   | 
| v2025_05 | Before May 1, 2025    | Starting May 1, 2025   | 
| v2026_01 | Before Jan 1, 2026    | Starting Jan 1, 2026   | 
| etc.     |                       |                        |

### License

Same license as GNU Radio.
