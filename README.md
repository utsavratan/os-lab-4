# OPERATING SYSTEMS — PRACTICAL LAB

<div align="center">

# File-System Interface and Implementation

### Python-Based File-System Application & Simulation Laboratory

**Utsav Ratan**  
**Enrollment No.: 2401010046**  
**Programme: B.Tech CSE Core**  
**Section: B**  
**Subject: Operating Systems**

</div>

---

## 1. Practical Overview

This project is a complete **Python-based Operating Systems practical laboratory** for studying file-system interfaces and implementation concepts.

It deliberately separates two environments:

### 1. Controlled Real Linux File-System Layer

Actual Linux/Python file operations are performed **only inside the project's `sandbox/` directory**.

The real-file layer demonstrates:

- File creation
- Reading
- Writing
- Appending
- Renaming
- Copying
- Directory creation
- Directory listing
- File metadata
- Permission inspection
- Safe deletion
- Path validation

### 2. Independent Simulated File-System Layer

The simulated layer does **not** manipulate the real filesystem.

It models:

- File descriptors / file records
- Sequential access
- Direct access
- Directory organization
- Single-level directories
- Two-level directories
- Tree-structured directories
- Contiguous allocation
- Linked allocation
- Indexed allocation
- Free-space management
- Bitmap free-space tracking
- Free-list tracking
- File deletion
- File truncation
- Permissions
- Access-control checks
- Allocation/deallocation traces
- Consistency validation

The separation is intentional and is an important part of the practical.

---

# 2. Practical Objective

Develop a Python-based file-system application and simulation covering:

1. File operations.
2. File access methods.
3. Directory organization.
4. File allocation methods.
5. Free-space management.
6. File creation and deletion.
7. File truncation.
8. File permissions.
9. Access control.
10. File metadata.
11. Simulated disk-block allocation.
12. Controlled real Linux filesystem operations.
13. Detailed intermediate traces.
14. Automated correctness tests.

---

# 3. Core Design Principle

The project follows this architecture:

```text
                 FILE-SYSTEM LAB
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
  REAL LINUX SANDBOX          SIMULATED FILESYSTEM
     sandbox/                       memory
          │                         │
          │                         ├── Directories
          │                         ├── Files
          │                         ├── Blocks
          │                         ├── Allocation
          │                         ├── Free Space
          │                         └── Permissions
          │
          └── Actual OS operations
```

### Important Safety Rule

**The real filesystem layer is restricted to `sandbox/`.**

The program rejects paths that escape this directory through:

- `..`
- absolute paths
- symlink traversal
- path resolution outside the sandbox

The simulated filesystem uses Python objects and arrays only.

---

# 4. Learning Outcomes

After completing this practical, a student should be able to:

- Explain the file-system interface.
- Perform safe file operations using Python.
- Explain file metadata.
- Understand sequential and direct access.
- Explain directory structures.
- Compare directory organization methods.
- Explain contiguous file allocation.
- Explain linked file allocation.
- Explain indexed file allocation.
- Track free disk blocks.
- Implement bitmap free-space management.
- Implement free-list management.
- Delete and truncate simulated files.
- Explain file permissions.
- Implement access-control checks.
- Distinguish real and simulated filesystem operations.
- Trace every allocation and deletion decision.
- Validate filesystem consistency programmatically.

---

# 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.10+ | Implementation |
| `pathlib` | Safe filesystem paths |
| `os` | File metadata and permissions |
| `shutil` | Controlled copy operations |
| `stat` | Permission decoding |
| `dataclasses` | Filesystem models |
| `argparse` | CLI |
| `unittest` | Automated tests |

### Dependencies

**No third-party packages are required.**

Only the Python standard library is used.

---

# 6. System Requirements

Recommended:

- Linux / Ubuntu
- Python 3.10+
- Terminal
- Standard filesystem permissions

Verify:

```bash
python3 --version
uname -a
```

The simulation itself does not require root access.

---

# 7. Project Structure

```text
filesystem_interface_implementation_lab/
│
├── README.md
├── LICENSE
├── requirements.txt
├── run.py
├── .gitignore
├── SUBMISSION_INFO.txt
│
├── sandbox/
│   └── .gitkeep
│
├── fs_lab/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── real_fs.py
│   ├── access_methods.py
│   ├── directories.py
│   ├── allocation.py
│   ├── free_space.py
│   ├── permissions.py
│   └── simulated_fs.py
│
├── scripts/
│   └── fs-lab
│
└── tests/
    ├── test_real_fs.py
    ├── test_access_methods.py
    ├── test_directories.py
    ├── test_allocation.py
    ├── test_free_space.py
    ├── test_permissions.py
    └── test_simulated_fs.py
```

---

# 8. Setup

Extract the project and enter the directory:

```bash
cd filesystem_interface_implementation_lab
```

Optional virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

No package installation is required.

Verify the application:

```bash
python3 -m fs_lab --help
```

Or:

```bash
./scripts/fs-lab --help
```

---

# 9. Main Commands

```text
real
access
directories
allocation
free-space
permissions
simulated
all
```

Run:

```bash
python3 -m fs_lab --help
```

---

# 10. Experiment 1 — Controlled Real File-System Interface

## Objective

To demonstrate actual Linux file operations safely inside the project sandbox.

## Run

```bash
python3 -m fs_lab real
```

The demonstration performs:

```text
Create directory
      ↓
Create file
      ↓
Write
      ↓
Read
      ↓
Append
      ↓
Copy
      ↓
Rename
      ↓
Metadata inspection
      ↓
Permission inspection
      ↓
Delete
```

All paths are created under:

```text
sandbox/
```

---

# 11. Real File-System Safety

The real filesystem module exposes only controlled operations.

For example:

```python
sandbox / "demo.txt"
```

is allowed.

A path such as:

```text
/etc/passwd
```

is rejected.

A path such as:

```text
../../important-file
```

is rejected.

The path is resolved and verified to remain inside the configured sandbox root.

This is intentionally implemented to satisfy the practical requirement that real Linux operations must remain inside a controlled test directory.

---

# 12. Real File Operations

The real filesystem demonstration covers:

### Create

```text
create_file()
```

### Write

```text
write_text()
```

### Append

```text
append_text()
```

### Read

```text
read_text()
```

### Copy

```text
copy_file()
```

### Rename

```text
rename()
```

### Delete

```text
delete()
```

### Directory

```text
mkdir()
list_dir()
```

### Metadata

```text
stat()
```

The trace prints the operation and resulting state.

---

# 13. File Metadata

The real filesystem demonstration reports useful metadata such as:

```text
Path
Size
Mode
Owner UID
Group GID
Modification Time
Directory/File Type
```

The exact UID/GID interpretation depends on the Linux environment.

---

# 14. Experiment 2 — File Access Methods

## Objective

To demonstrate sequential and direct/random file access.

Run:

```bash
python3 -m fs_lab access
```

---

# 15. Sequential Access

Sequential access processes data from beginning to end.

Example:

```text
Record 0
   ↓
Record 1
   ↓
Record 2
   ↓
Record 3
```

The simulation creates fixed-size logical records and reads them in order.

The trace shows:

```text
READ record=0
READ record=1
READ record=2
...
```

---

# 16. Direct Access

Direct access allows a logical record to be accessed by its index.

Example:

```text
READ record=4
READ record=1
READ record=7
```

The program reports the requested record and resulting data.

This demonstrates the conceptual difference between:

```text
Sequential:
0 → 1 → 2 → 3 → ...

Direct:
4
1
7
```

---

# 17. Experiment 3 — Directory Organization

## Objective

To simulate common directory structures.

Run:

```bash
python3 -m fs_lab directories
```

The project demonstrates:

- Single-level directory
- Two-level directory
- Tree-structured directory

---

# 18. Single-Level Directory

All files are stored in one directory.

```text
ROOT
├── file1
├── file2
├── file3
└── file4
```

Advantages:

- Simple implementation.

Limitations:

- Naming conflicts
- Poor scalability
- No user/project grouping

---

# 19. Two-Level Directory

Each user has a separate directory.

```text
ROOT
├── user1
│   ├── a.txt
│   └── b.txt
│
└── user2
    ├── a.txt
    └── c.txt
```

This allows the same filename to exist for different users.

---

# 20. Tree-Structured Directory

Directories may contain subdirectories.

```text
ROOT
├── home
│   ├── utsav
│   │   ├── documents
│   │   └── projects
│   └── student
│
└── system
    ├── logs
    └── config
```

The simulation prints the resulting tree.

---

# 21. Experiment 4 — File Allocation Methods

## Objective

To simulate how file data blocks can be allocated on a disk.

Run:

```bash
python3 -m fs_lab allocation
```

Supported methods:

- Contiguous allocation
- Linked allocation
- Indexed allocation

The simulation uses a fixed block array.

---

# 22. Contiguous Allocation

A file receives consecutive disk blocks.

Example:

```text
File A → [10, 11, 12, 13]
```

The trace reports:

```text
REQUEST: A blocks=4
SEARCH: suitable contiguous region
ALLOCATE: 10-13
```

### Advantages

- Excellent sequential access.
- Simple addressing.
- Good locality.

### Limitation

- External fragmentation.
- Difficult growth when adjacent blocks are unavailable.

---

# 23. Linked Allocation

A file's blocks may be located anywhere.

Example:

```text
A → 4 → 17 → 2 → 25
```

Each logical block points to the next block.

The trace displays:

```text
ALLOCATE block=4
ALLOCATE block=17
ALLOCATE block=2
ALLOCATE block=25

CHAIN:
4 → 17 → 2 → 25
```

### Advantage

Files can grow without requiring contiguous space.

### Limitation

Direct/random access is less convenient because the chain must be followed.

---

# 24. Indexed Allocation

An index block contains pointers to the file's data blocks.

Example:

```text
Index Block 7
│
├── 2
├── 9
├── 15
└── 18
```

The simulation reports:

```text
INDEX BLOCK: 7
DATA BLOCKS: [2, 9, 15, 18]
```

### Advantage

Supports direct access through the index.

### Limitation

Requires index-block overhead.

---

# 25. Allocation Verification Trace

Every allocation experiment reports:

```text
File
Requested Blocks
Candidate Blocks
Selected Blocks
Allocation Method
Final File Mapping
Free Blocks Remaining
```

Therefore, a student can manually verify each allocation.

---

# 26. Experiment 5 — Free-Space Management

## Objective

To demonstrate how an operating system can track free disk blocks.

Run:

```bash
python3 -m fs_lab free-space
```

Supported methods:

- Bitmap
- Free list

---

# 27. Bitmap Free-Space Management

A bitmap uses one bit/value per block.

Example:

```text
Block: 0 1 2 3 4 5 6 7
State: 1 1 0 0 1 0 1 0
```

Where:

```text
0 = free
1 = allocated
```

The program prints the bitmap after each allocation and release.

---

# 28. Free-List Management

A free list stores the identifiers of available blocks.

Example:

```text
FREE LIST:
[2, 3, 5, 7, 8, 11]
```

Allocation removes blocks from the free list.

Release adds them back.

The trace shows:

```text
BEFORE
AFTER ALLOCATION
AFTER RELEASE
```

---

# 29. Experiment 6 — File Deletion

## Objective

To demonstrate file deletion and block reclamation.

Run:

```bash
python3 -m fs_lab simulated
```

The simulation performs:

```text
CREATE FILE
      ↓
ALLOCATE BLOCKS
      ↓
WRITE
      ↓
DELETE FILE
      ↓
RELEASE BLOCKS
      ↓
UPDATE DIRECTORY
```

A deleted file's allocated blocks return to the free-space manager.

---

# 30. File Truncation

Truncation removes a file's data while retaining the file entry.

Conceptually:

```text
Before:
FILE A
Blocks: [4,5,6,7]

TRUNCATE

After:
FILE A
Blocks: []
Size: 0
```

The file remains in the directory while its data blocks become available again.

---

# 31. Experiment 7 — Permissions and Access Control

## Objective

To simulate Unix-style permission checks.

Run:

```bash
python3 -m fs_lab permissions
```

The project models:

```text
Owner
Group
Others
```

with:

```text
Read    r
Write   w
Execute x
```

---

# 32. Permission Representation

Example:

```text
rw-r-----
```

Conceptually:

```text
Owner  = rw-
Group  = r--
Others = ---
```

The simulator converts permissions into symbolic form and checks requested operations.

---

# 33. Access-Control Checks

Example:

```text
USER: owner
OPERATION: read
PERMISSION: granted
```

Another example:

```text
USER: other
OPERATION: write
PERMISSION: denied
```

The trace reports:

```text
IDENTITY
REQUESTED OPERATION
EFFECTIVE PERMISSION
ALLOW / DENY
```

---

# 34. Simulated File-System

## Objective

To integrate directories, files, allocation, free-space management and permissions into one simulated filesystem.

Run:

```bash
python3 -m fs_lab simulated
```

The integrated simulator supports:

```text
mkdir
create
write
read
list
delete
truncate
chmod
open/read/write access checks
```

The simulated filesystem does not touch the actual filesystem.

---

# 35. Simulated File Metadata

A simulated file record contains information such as:

```text
Name
Path
Size
Owner
Group
Permissions
Allocation Method
Allocated Blocks
Created/Modified Metadata
```

This allows file-system concepts to be observed without changing the host system.

---

# 36. File-System Consistency

The simulator performs consistency validation.

It checks that:

- A block is not allocated to multiple files.
- Allocated blocks are marked unavailable.
- Free blocks are not simultaneously assigned.
- Directory entries point to existing files/directories.
- Deleted files no longer occupy blocks.
- File block lists are valid.
- Indexed allocation references valid blocks.
- Linked allocation chains terminate correctly.

Run:

```bash
python3 -m fs_lab simulated
```

The final trace includes a consistency result.

---

# 37. Complete Demonstration

Run:

```bash
python3 -m fs_lab all
```

This executes:

```text
Controlled Real Filesystem
          ↓
Sequential / Direct Access
          ↓
Directory Organization
          ↓
File Allocation
          ↓
Free-Space Management
          ↓
Deletion / Truncation
          ↓
Permissions
          ↓
Integrated Simulated Filesystem
          ↓
Consistency Verification
```

---

# 38. Detailed Trace Design

The practical specifically requires enough intermediate output to verify operations.

The project therefore reports:

## Real Filesystem

```text
SANDBOX ROOT
OPERATION
RESOLVED PATH
RESULT
METADATA
```

## Access Methods

```text
ACCESS MODE
RECORD INDEX
DATA
```

## Directories

```text
DIRECTORY OPERATION
PATH
ENTRY
RESULTING TREE
```

## Allocation

```text
REQUEST
CANDIDATES
SELECTED BLOCKS
FILE MAPPING
```

## Free Space

```text
BEFORE
OPERATION
AFTER
```

## Permissions

```text
IDENTITY
MODE
REQUEST
ALLOW / DENY
```

## Deletion

```text
FILE
ALLOCATED BLOCKS
RELEASED BLOCKS
DIRECTORY UPDATE
```

This makes the project suitable for a practical demonstration and viva.

---

# 39. Real vs Simulated Operations

| Operation | Real Sandbox | Simulated FS |
|---|---:|---:|
| Create file | Yes | Yes |
| Read file | Yes | Yes |
| Write file | Yes | Yes |
| Append | Yes | Simulated |
| Rename | Yes | Yes |
| Copy | Yes | Simulated |
| Directory tree | Yes | Yes |
| File metadata | Yes | Yes |
| Allocation | OS-managed | Explicit simulation |
| Free-space bitmap | Not modified | Yes |
| Linked allocation | Not modified | Yes |
| Indexed allocation | Not modified | Yes |
| Permissions | Linux metadata | Simulated |
| Delete | Yes, sandbox only | Yes |
| Truncate | Simulated through model | Yes |

The real layer demonstrates the interface safely; the simulated layer demonstrates internal OS concepts.

---

# 40. Important Safety Guarantees

The real filesystem layer:

- Uses only `sandbox/`.
- Rejects absolute paths.
- Rejects paths containing `..`.
- Resolves paths before access.
- Rejects symlink escapes.
- Does not require root.
- Does not modify `/etc`, `/home`, `/usr`, `/var`, `/tmp`, or other system directories.
- Does not alter partitions.
- Does not manipulate raw disks.
- Does not change real filesystem allocation structures.

The simulated filesystem is completely independent.

---

# 41. Automated Tests

Run:

```bash
python3 -m unittest discover -v
```

The test suite verifies:

- Safe sandbox path handling
- Real file creation/read/write
- Sequential access
- Direct access
- Directory organization
- Contiguous allocation
- Linked allocation
- Indexed allocation
- Bitmap operations
- Free-list operations
- Permission checks
- File creation
- File deletion
- File truncation
- Block reclamation
- Simulated filesystem consistency

---

# 42. Recommended Practical Demonstration

### Step 1 — Controlled real filesystem

```bash
python3 -m fs_lab real
```

### Step 2 — Access methods

```bash
python3 -m fs_lab access
```

### Step 3 — Directory organization

```bash
python3 -m fs_lab directories
```

### Step 4 — Allocation

```bash
python3 -m fs_lab allocation
```

### Step 5 — Free-space management

```bash
python3 -m fs_lab free-space
```

### Step 6 — Permissions

```bash
python3 -m fs_lab permissions
```

### Step 7 — Integrated simulation

```bash
python3 -m fs_lab simulated
```

### Step 8 — Everything

```bash
python3 -m fs_lab all
```

### Step 9 — Tests

```bash
python3 -m unittest discover -v
```

---

# 43. Important Viva Questions

### Q1. What is a file-system interface?

It is the set of operations through which users and programs interact with files and directories, such as create, open, read, write, close and delete.

### Q2. What is sequential access?

Data is processed in a predetermined sequence from one logical position to the next.

### Q3. What is direct access?

A specific logical record or block can be accessed without processing all preceding records.

### Q4. What is contiguous allocation?

All blocks belonging to a file are stored consecutively.

### Q5. What is linked allocation?

File blocks may be scattered and linked together through pointers.

### Q6. What is indexed allocation?

An index block stores references to the data blocks belonging to a file.

### Q7. What is free-space management?

It is the mechanism used to track which disk blocks are currently available for allocation.

### Q8. What is a bitmap?

A bitmap maintains a bit/value representing the allocation state of each block.

### Q9. What is file truncation?

Truncation removes a file's data and releases its data blocks while retaining the file entry.

### Q10. What are file permissions?

Permissions specify which identities may read, write or execute a file.

### Q11. What is access control?

Access control determines whether a requested operation should be allowed for a particular identity.

### Q12. What is a directory?

A directory is a filesystem structure that organizes and maps names to filesystem objects.

### Q13. What is external fragmentation?

External fragmentation is free storage divided into separated regions such that a contiguous allocation may fail despite sufficient total free space.

### Q14. Why is linked allocation useful?

It allows file blocks to be allocated non-contiguously and supports file growth without requiring one large contiguous region.

### Q15. Why does indexed allocation use an index block?

The index block stores pointers to the file's data blocks, allowing direct lookup of block locations.

---

# 44. Important Comparisons

## Allocation

| Method | Main Benefit | Main Limitation |
|---|---|---|
| Contiguous | Fast sequential/direct access | External fragmentation and growth difficulty |
| Linked | Easy non-contiguous growth | Pointer overhead and weaker direct access |
| Indexed | Direct access through index | Index-block overhead |

## Directory Organization

| Organization | Characteristic |
|---|---|
| Single-level | One common directory |
| Two-level | Separate directory per user |
| Tree | Hierarchical directories |

## Free-Space Management

| Method | Representation |
|---|---|
| Bitmap | One state bit/value per block |
| Free list | Linked/listed available blocks |

---

# 45. File Operations Summary

Typical filesystem interface operations include:

```text
create
open
read
write
append
seek
close
rename
delete
truncate
mkdir
list
stat
chmod
```

The practical maps these interface concepts to either:

```text
Controlled Linux operation
```

or:

```text
Pure simulation
```

depending on whether the operation should demonstrate actual OS behavior or internal filesystem implementation.

---

# 46. Permission Model

The simulated permission model uses:

```text
OWNER
GROUP
OTHERS
```

and:

```text
READ
WRITE
EXECUTE
```

For example:

```text
rwxr-x---
```

means:

```text
Owner : rwx
Group : r-x
Other : ---
```

The simulator checks the appropriate identity class before allowing the operation.

---

# 47. Design Quality

The project follows a modular design:

```text
CLI
 │
 ├── Real Filesystem
 │
 ├── Access Methods
 │
 ├── Directories
 │
 ├── Allocation
 │
 ├── Free Space
 │
 ├── Permissions
 │
 └── Simulated Filesystem
```

Algorithmic modules are independent from command-line presentation and are directly testable.

---

# 48. Quick Reference

| Practical | Command |
|---|---|
| Help | `python3 -m fs_lab --help` |
| Real filesystem | `python3 -m fs_lab real` |
| Access methods | `python3 -m fs_lab access` |
| Directories | `python3 -m fs_lab directories` |
| Allocation | `python3 -m fs_lab allocation` |
| Free space | `python3 -m fs_lab free-space` |
| Permissions | `python3 -m fs_lab permissions` |
| Simulation | `python3 -m fs_lab simulated` |
| Everything | `python3 -m fs_lab all` |
| Tests | `python3 -m unittest discover -v` |

---

# 49. Submission Checklist

Before submission, verify:

- [ ] Python environment verified
- [ ] Controlled sandbox demonstrated
- [ ] File creation demonstrated
- [ ] File reading demonstrated
- [ ] File writing demonstrated
- [ ] File appending demonstrated
- [ ] File copying demonstrated
- [ ] File renaming demonstrated
- [ ] File deletion demonstrated
- [ ] Metadata inspected
- [ ] Sequential access demonstrated
- [ ] Direct access demonstrated
- [ ] Single-level directory demonstrated
- [ ] Two-level directory demonstrated
- [ ] Tree directory demonstrated
- [ ] Contiguous allocation demonstrated
- [ ] Linked allocation demonstrated
- [ ] Indexed allocation demonstrated
- [ ] Bitmap free-space management demonstrated
- [ ] Free-list management demonstrated
- [ ] File deletion and block reclamation demonstrated
- [ ] File truncation demonstrated
- [ ] Permission checks demonstrated
- [ ] Access-control decisions demonstrated
- [ ] Simulated filesystem demonstrated
- [ ] Consistency validation passed
- [ ] Intermediate traces inspected
- [ ] Automated tests passed

---

# 50. Final Conclusion

This practical provides a complete hands-on study of the **File-System Interface and Implementation**.

It connects filesystem theory with two clearly separated environments:

```text
Actual Linux File Operations
          │
          ▼
     Controlled Sandbox
          │
          │
          └──────────────┐
                         │
                         ▼
               Filesystem Concepts
                         │
                         ▼
                Simulated Filesystem
```

The practical covers:

```text
File Interface
      ↓
Access Methods
      ↓
Directory Organization
      ↓
File Allocation
      ↓
Free-Space Management
      ↓
Deletion & Truncation
      ↓
Permissions & Access Control
      ↓
Filesystem Consistency
```

The detailed traces make every major operation and simulated filesystem decision inspectable and verifiable.

---

<div align="center">

## OPERATING SYSTEMS PRACTICAL

**Utsav Ratan — 2401010046**  
**B.Tech CSE Core — Section B**

### File-System Interface and Implementation

</div>
