def add_dict(*dicts):
    dsum = {}
    d_k = []
    d_v = []
    for dic in dicts:
        d_k.extend(list(dic.keys()))  # sum keys list
        d_v.extend(list(dic.values()))  # sum values list
    for i in range(len(d_k)):
        dsum[d_k[i]] = d_v[i]
    return dsum
  
  dict_add = add_dict(code_mid, code_bad, code_good)
