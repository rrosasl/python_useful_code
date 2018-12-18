#this can be used to separate email from phone number when they are in the same column_name
#df.contact would have both phone number and email (sometimes in different order)

#Extract phone number to new column
#The weird code is regex   https://stackoverflow.com/questions/16699007/regular-expression-to-match-standard-10-digit-phone-number

df['phone_number'] = df['contact'].str.extract('((?:\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})',expand=True)

#Extract email to new column
#For email https://emailregex.com/
df['email'] = df['contact'].str.extract('([a-zA-Z][a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+[a-zA-Z])', expand=True)
