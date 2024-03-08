---
name: Bug report
about: Create a report to help us improve loggingpython
title: "[BUG]"
labels: buga
assignees: mr-major-k-programmer

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**

1. insert the following code into your script:

```python
import loggingpython as lp

# Write logs
logger = lp.getLogger()

filehandler = lp.FileHandler(logger.name)
logger.addHandler(filehandler)

logger.debug("Test message")
```

2. Execute the script.

3. Check the "app.log" file. The file should be empty.

**Expected behavior**

The test message "Test message" should be logged in the "app.log" file.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Desktop (please complete the following information):**
 - OS: [e.g. iOS]
 - Version [e.g. 22]

**Additional context**
Add any other context about the problem here.
