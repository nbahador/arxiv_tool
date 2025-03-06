# arxiv-tool-analyzer

`arxiv-tool-analyzer` is a Python package for searching, fetching, and analyzing research papers from ArXiv. It allows you to search for papers based on specific authors, topics, and a date range. Additionally, it provides utilities to save results to Excel and search for specific terms within paper abstracts.

## Installation

To install the `arxiv-tool-analyzer` package, you can use `pip`. Run the following command in your terminal or command prompt:

For more details, you can visit the [PyPI page](https://pypi.org/project/arxiv-tool-analyzer/).

---

## Example Usage

After installing the package, you can use it in a Python script or execute it directly in the terminal using the `python -c` command.

### Example Command:

To run the example, execute the following command in your terminal:

```bash
python -c "from arxiv_tool_analyzer import fetch_arxiv_data, save_to_excel, merge_excel_files, search_terms_in_abstracts; 
authors = []; 
topics = ['large language model', 'single GPU']; 
start_date = '2025-01-01'; 
end_date = '2026-01-01'; 
df = fetch_arxiv_data(authors, topics, start_date, end_date); 
save_to_excel(df, 'arXiv_results.xlsx'); 
search_terms_in_abstracts('terms.txt', 'arXiv_results.xlsx', 'matches_output.txt')"
```

---

Directory Structure:

```
arxiv_tool/
│
├── arxiv_tool/
│   ├── __init__.py
│   ├── arxiv_search.py
│   ├── merge_files.py
│   └── search_terms.py
│
└── setup.py
```
---
