import pandas as pd

def save(df, filename):
    writer = pd.ExcelWriter('data/'+filename)
    df.to_excel(writer, sheet_name='sheet1', index=False) # index를 설정하지 않음.
    writer.close()
    # writer.save() # save()는 더 이상 사용하지 않음. .close()로 대체됨.
