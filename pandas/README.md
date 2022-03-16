### pandas 튜토리얼
https://ml-ko.kr/homl2/tools_pandas.html

### .apply, .map. .applymap
#### First major difference: DEFINITION
* map is defined on <font color='red'>Series ONLY</font>
* applymap is defined on <font color='blue'>DataFrames ONLY</font>
* apply is defined on <font color='blue'>BOTH</font>

#### Second major difference: INPUT ARGUMENT
* map accepts dicts, Series, or callable
* applymap and apply accept callables only

#### Third major difference: BEHAVIOR
* map is elementwise for Series
* applymap is elementwise for DataFrames
* apply also works elementwise but is suited to more complex operations and aggregation. The behaviour and return value depends on the function.

#### Fourth major difference (the most important one): USE CASE
* map is meant for mapping values from one domain to another, so is optimised for performance (e.g., df['A'].map({1:'a', 2:'b', 3:'c'}))
* applymap is good for elementwise transformations across multiple rows/columns (e.g., df[['A', 'B', 'C']].applymap(str.strip))
* apply is for applying any function that cannot be vectorised (e.g., df['sentences'].apply(nltk.sent_tokenize)).
