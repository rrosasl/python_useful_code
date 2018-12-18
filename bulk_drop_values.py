#USe loop to drop many values
#This may not be the most effective way to do it... but hey! it works

todrop_values = {'A','B','Z','D'}

for todropv in todrop_values:
    df = df[df['column'] != todropv]
