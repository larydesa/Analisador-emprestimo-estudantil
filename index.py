age = int(input("Digite sua idade: "))
income = float(input("Digite sua renda: "))
loan_amount = float(input("Valor do empréstimo: "))
installments = int(input("Valor das parcelas: "))

monthly_installment = loan_amount / installments

if age < 18:
  print("\033[31mReprovado! Você precisa ser maior de idade\033[m")
elif income < 1500:
  print("\033[31mReprovado! Sua renda deve ser acima de 1.500\033[m")
elif monthly_installment <= (income * 0.30):
  print("\033[32mAprovado para o empréstimo de R${} dividido em {} de {}x!\033[m".format(loan_amount, monthly_installment, installments))
else:
  print("\033[31mReprovado: Parcela muito alta para sua renda.\033[m")
