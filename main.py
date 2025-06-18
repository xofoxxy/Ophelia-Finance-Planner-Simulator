import account

if __name__ == '__main__':
    seth_account = account.Account("Seth", balance=1200, appreciation=1.10, costs=1200, income=15000)
    #seth_account.simple_project_balance(10)
    #seth_account.graph_everything()

    # def bridge_income(year):
    #     return 12000*1.10**year
    # bridgette_account = account.Account("Bridgette", balance=10000, appreciation=1.06, costs=6000, income=bridge_income)
    # bridgette_account.simple_project_balance(10)
    # bridgette_account.graph_everything()


    def kids_costs(year):
        return 10000
    kids_cost = account.Account("Kids", balance=0, costs=kids_costs)
    kids_cost.simple_project_balance(10)
    kids_cost.graph_everything()