from openpyxl import load_workbook

def getOpenxls():
    f = 'C:\\Users\\Wei\\NCBI\\'
    burl = 'https://www.ncbi.nlm.nih.gov/pubmed/'
    f_a = f + 'I001_coronary_heart_disease_panel.xlsx'
    wb = load_workbook(f_a)
    sheet1 = wb.get_sheet_by_name('condition')
    sheet2 = wb.get_sheet_by_name('snp_score')
    xlpath = sheet1['D4'].value
    urlpath = []
    for r in range(1,sheet2.max_row):
        url = sheet2['C'][r].value
        if url:
            urlpath.append(burl + str(url))

    return set(urlpath)
