# 🔍 Hash Table Keyword Counter

**Course:** Data Structures
**Language:** Python  

---

## 📘 Overview
This Python program builds a **hash table** from one text file and compares it against another file to count keyword occurrences.  
It demonstrates:
- Custom hash function design  
- Collision handling using **linear probing**  
- Text parsing and frequency analysis  
- Program runtime measurement  

---

## ⚙️ How It Works
1. The program reads the **first file** and inserts each word into a hash table of size `29`.  
2. The **second file** is then scanned, and each word is checked against the hash table.  
3. Keywords found in both files are counted, and statistics are displayed.  

### 🧩 Hash Function
```python
hashCode += ord(element) * (a ** (wordLen - 1 - i))
indexInTable = hashCode % tableSize

Author: Rohan Katare
