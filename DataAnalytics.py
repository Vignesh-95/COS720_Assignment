import pandas as pd
import pandas_profiling
from datetime import datetime


def get_var_category(series):
    unique_count = series.nunique(dropna=False)
    total_count = len(series)
    if pd.api.types.is_numeric_dtype(series):
        return 'Numerical'
    elif pd.api.types.is_datetime64_dtype(series):
        return 'Date'
    elif unique_count == total_count:
        return 'Text (Unique)'
    else:
        return 'Categorical'


def print_categories(df):
    for column_name in df.columns:
        print(column_name, ": ", get_var_category(df[column_name]))

if __name__ == "__main__":
    emails = pd.read_csv("/home/vignesh/PycharmProjects/CyberSecurityEnronEmails/emails.csv")
    emails.pop("file")

    emails['MessageID'] = emails['message'].str.extract("Message-ID: (.*)\n")
    emails['Date'] = emails['message'].str.extract("Date: (.*)\n")
    emails['From'] = emails['message'].str.extract("From: (.*)\n")
    emails['To'] = emails['message'].str.extract("To: (.*)\n")
    emails['Subject'] = emails['message'].str.extract("Subject: (.*)\n")
    emails['MimeVersion'] = emails['message'].str.extract("Mime-Version: (.*)\n")
    emails['ContentType'] = emails['message'].str.extract("Content-Type: (.*)\n")
    emails['ContentTransferEncoding'] = emails['message'].str.extract("Content-Transfer-Encoding: (.*)\n")
    emails['XFrom'] = emails['message'].str.extract("X-From: (.*)\n")
    emails['XTo'] = emails['message'].str.extract("X-To: (.*)\n")
    emails['Xcc'] = emails['message'].str.extract("X-cc: (.*)\n")
    emails['Xbcc'] = emails['message'].str.extract("X-bcc: (.*)\n")
    emails['XFolder'] = emails['message'].str.extract("X-Folder: (.*)\n")
    emails['XOrigin'] = emails['message'].str.extract("X-Origin: (.*)\n")
    emails['XFileName'] = emails['message'].str.extract("X-FileName: (.*)\n")

    emails.pop("message")

    # print_categories(emails)
    # pandas_profiling.ProfileReport(emails)
    # print("\nData Types: \n", emails.dtypes)
    print("\nSome Descriptive Statistics: \n", emails.describe(include='all'))
    # print("\nFirst 5 (Head) emails: \n", emails.head())
    # print("\nFirst 5 (Tail) emails: \n", emails.tail())
    print("\nData: \n", emails)
