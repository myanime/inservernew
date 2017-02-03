import time
import pandas as pd
month_name = [line.rstrip('\n') for line in open("filename")][0]
months_output = month_name + '.csv'
months_output_path = './' + month_name + '.csv'
post_codes_csv = 'post_codes.csv'
todays_date = time.strftime("%d_%m_%Y")

df_month_output = pd.read_csv(months_output, names = ['jobNumber','job_title','job_location','job_description','original_link','original_link_clean','job_company','job_money_unchanged','job_money','salary_description','range_lower','range_upper','original_link_emails','original_link_telephones','image_src_link','image_src_link_path','image_src_link_file','image_link','job_date','indeed_date','original_plain_text','original_html','company_description_indeed','company_revenue_indeed','company_employees_indeed','company_industry_indeed','company_links_indeed'])

df_month_output_deduped = df_month_output.drop_duplicates('original_link')
df_month_output_deduped = df_month_output_deduped.sort('job_date')
df_month_output_deduped.to_csv(months_output, float_format='%.0f', index=False)

df_post_codes = pd.read_csv(post_codes_csv)
df_month_output_deduped = df_month_output_deduped.merge(df_post_codes, on='job_location', how='left')

today_deduped = df_month_output_deduped[df_month_output_deduped['job_date'] == todays_date]
today_deduped.to_csv('./transfer/V1au_' + todays_date + ".csv", float_format='%.0f')
