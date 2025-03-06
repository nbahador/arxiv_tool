from arxiv_tool_analyzer import fetch_arxiv_data, save_to_excel, merge_excel_files, search_terms_in_abstracts

# Define variables
authors = []
topics = ['large language model', 'single GPU']
start_date = '2025-01-01'
end_date = '2026-01-01'

# Fetch arXiv data
df = fetch_arxiv_data(authors, topics, start_date, end_date)

# Save the data to an Excel file
save_to_excel(df, 'arXiv_results.xlsx')

# Search for terms in the abstracts and output matches
search_terms_in_abstracts('terms.txt', 'arXiv_results.xlsx', 'matches_output.txt')
