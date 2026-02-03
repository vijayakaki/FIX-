from app import calculate_ejv_simplified

# Test the new simplified EJV calculation
result = calculate_ejv_simplified('supermarket_101', store_name='Local Grocer', zip_code='10001')

print('\n' + '='*60)
print('SIMPLIFIED EJV TEST RESULTS')
print('='*60)
print(f'\nEJV Score: {result["ejv_score"]} ({result["ejv_percentage"]}%)')
print(f'\nComponents:')
print(f'  W (Fair Wage):     {result["components"]["W_fair_wage"]}')
print(f'  P (Pay Equity):    {result["components"]["P_pay_equity"]}')
print(f'  L (Local Impact):  {result["components"]["L_local_impact"]}')
print(f'  A (Affordability): {result["components"]["A_affordability"]}')
print(f'  E (Environmental): {result["components"]["E_environmental"]}')
print(f'\nEconomic Impact:')
print(f'  ELVR (Local Retained): ${result["economic_impact"]["elvr"]}')
print(f'  EVL (Leakage):         ${result["economic_impact"]["evl"]}')
print(f'  Retention Rate:        {result["economic_impact"]["retention_percent"]}%')
print(f'\n{result["economic_impact"]["interpretation"]}')
print('='*60)
