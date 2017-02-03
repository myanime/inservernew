##### END OF DAY SCRIPT #####

'''
This should be run at the end of every day. It will remove all but the current
dates listings, thus ensuring that the file for the current month will not
become too big, and simillarly ensuring that on the next day of scraping
duplicates are not entered.
'''

import time
import pandas as pd

#Open May
month_name = [line.rstrip('\n') for line in open("filename")][0]
months_output = month_name + '.csv'

yesterday = "21_05_2016"
todays_date = "22_05_2016"

df_month_output = pd.read_csv(months_output, names = ['jobNumber','job_title','job_location','job_description','original_link','original_link_clean','job_company','job_money_unchanged','job_money','salary_description','range_lower','range_upper','original_link_emails','original_link_telephones','image_src_link','image_src_link_path','image_src_link_file','image_link','job_date','indeed_date','original_plain_text','original_html','company_description_indeed','company_revenue_indeed','company_employees_indeed','company_industry_indeed','company_links_indeed'])
df_month_output_deduped = df_month_output.drop_duplicates('original_link')
df_month_output_deduped = df_month_output_deduped.sort('job_date')

today_deduped = df_month_output_deduped[(df_month_output_deduped['job_date'] == todays_date) | (df_month_output_deduped['job_date'] == yesterday)]
today_deduped.to_csv(months_output, float_format='%.0f', index=False)

